#!/usr/bin/env python3
"""Minimal read-only repository validator.

This tool performs Phase 0.5 structural checks only. It does not modify files,
repair files, fetch network resources, or judge historical content quality.

Checks:
- every directory has INDEX.md
- every INDEX.md lists direct files and direct subdirectories only
- CSV headers match the current repository index schema
- repository-relative paths in selected indexes exist
- IDs are unique within each CSV index
"""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

IGNORED_DIRS = {
    ".git",
    ".github",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
}

EXPECTED_CSV_HEADERS = {
    "indexes/targets.csv": [
        "target_id",
        "title",
        "target_type",
        "status",
        "primary_path",
        "period_start",
        "period_end",
        "geography",
        "source_status",
        "confidence",
    ],
    "indexes/reports.csv": [
        "report_id",
        "target_id",
        "title",
        "artifact_type",
        "pillar",
        "path",
        "source_status",
        "confidence",
        "updated",
    ],
    "indexes/sources.csv": [
        "source_id",
        "title",
        "author_or_creator",
        "publisher_or_holder",
        "publication_date",
        "source_tier",
        "source_type",
        "related_targets",
        "path",
        "reliability_status",
    ],
    "indexes/facts.csv": [
        "fact_id",
        "statement",
        "related_target",
        "related_report",
        "source_ids",
        "confidence",
        "status",
    ],
    "indexes/claims.csv": [
        "claim_id",
        "statement",
        "related_target",
        "related_report",
        "supporting_fact_ids",
        "source_ids",
        "confidence",
        "status",
    ],
    "indexes/lessons.csv": [
        "lesson_id",
        "statement",
        "related_targets",
        "related_claims",
        "theme_ids",
        "transferability",
        "confidence",
        "status",
    ],
    "indexes/patterns.csv": [
        "pattern_id",
        "statement",
        "supporting_lesson_ids",
        "supporting_target_count",
        "theme_ids",
        "confidence",
        "status",
    ],
    "indexes/principles.csv": [
        "principle_id",
        "statement",
        "supporting_pattern_ids",
        "counterexamples_considered",
        "confidence",
        "status",
    ],
    "indexes/relationships.csv": [
        "relationship_id",
        "subject_id",
        "relationship",
        "object_id",
        "evidence_path",
        "source_ids",
        "confidence",
        "status",
    ],
    "indexes/themes.csv": [
        "theme_id",
        "preferred_label",
        "alternative_labels",
        "broader",
        "related",
        "definition",
        "status",
    ],
}

PATH_FIELDS = {
    "indexes/targets.csv": ["primary_path"],
    "indexes/reports.csv": ["path"],
    "indexes/sources.csv": ["path"],
    "indexes/relationships.csv": ["evidence_path"],
}

INDEX_ENTRY_RE = re.compile(r"^- `([^`]+)`")


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix() if path != ROOT else "."


def iter_repo_dirs() -> list[Path]:
    dirs: list[Path] = []
    for path in sorted(ROOT.rglob("*")):
        if not path.is_dir():
            continue
        if any(part in IGNORED_DIRS for part in path.relative_to(ROOT).parts):
            continue
        dirs.append(path)
    return [ROOT] + dirs


def parse_index_entries(index_path: Path) -> set[str]:
    entries: set[str] = set()
    for line in index_path.read_text(encoding="utf-8").splitlines():
        match = INDEX_ENTRY_RE.match(line.strip())
        if match:
            entries.add(match.group(1))
    return entries


def expected_direct_entries(directory: Path) -> set[str]:
    entries: set[str] = set()
    for child in sorted(directory.iterdir()):
        if child.name in IGNORED_DIRS:
            continue
        if child.name.startswith("."):
            continue
        if child.is_dir():
            entries.add(f"{child.name}/")
        elif child.is_file():
            entries.add(child.name)
    return entries


def check_indexes(errors: list[str]) -> None:
    for directory in iter_repo_dirs():
        index_path = directory / "INDEX.md"
        if not index_path.exists():
            errors.append(f"{rel(directory)}: missing INDEX.md")
            continue

        listed = parse_index_entries(index_path)
        expected = expected_direct_entries(directory)

        missing = sorted(expected - listed)
        extra = sorted(listed - expected)

        for item in missing:
            errors.append(f"{rel(index_path)}: missing direct entry `{item}`")
        for item in extra:
            errors.append(f"{rel(index_path)}: listed entry does not exist as direct child `{item}`")


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def check_csv_headers(errors: list[str]) -> None:
    for repo_path, expected_header in EXPECTED_CSV_HEADERS.items():
        path = ROOT / repo_path
        if not path.exists():
            errors.append(f"{repo_path}: missing expected CSV index")
            continue
        actual_header, _rows = read_csv(path)
        if actual_header != expected_header:
            errors.append(
                f"{repo_path}: header mismatch; expected {expected_header}, found {actual_header}"
            )


def check_unique_ids(errors: list[str]) -> None:
    for repo_path in EXPECTED_CSV_HEADERS:
        path = ROOT / repo_path
        if not path.exists():
            continue
        header, rows = read_csv(path)
        if not header:
            continue
        id_field = header[0]
        seen: set[str] = set()
        for row_number, row in enumerate(rows, start=2):
            object_id = row.get(id_field, "").strip()
            if not object_id:
                continue
            if object_id in seen:
                errors.append(f"{repo_path}:{row_number}: duplicate `{id_field}` value `{object_id}`")
            seen.add(object_id)


def split_path_values(value: str) -> list[str]:
    if not value.strip():
        return []
    return [part.strip() for part in value.split(";") if part.strip()]


def check_index_paths(errors: list[str]) -> None:
    for repo_path, fields in PATH_FIELDS.items():
        path = ROOT / repo_path
        if not path.exists():
            continue
        _header, rows = read_csv(path)
        for row_number, row in enumerate(rows, start=2):
            for field in fields:
                for value in split_path_values(row.get(field, "")):
                    if not (ROOT / value).exists():
                        errors.append(f"{repo_path}:{row_number}: `{field}` path does not exist: {value}")


def main() -> int:
    errors: list[str] = []
    check_indexes(errors)
    check_csv_headers(errors)
    check_unique_ids(errors)
    check_index_paths(errors)

    if errors:
        print("Repository validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Repository validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
