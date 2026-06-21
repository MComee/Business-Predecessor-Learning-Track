# Repository Specification

## 1. Purpose

This specification governs how the repository is organized, navigated, expanded, and preserved.

The repository is a layered historical business-learning knowledge system. It stores readable reports, structured metadata, controlled vocabulary terms, source-linked knowledge objects, and cross-target indexes.

## 2. Governing Architecture

The repository uses five layers:

1. **Narrative layer** — Markdown reports for human learning.
2. **Metadata layer** — YAML front matter and structured descriptors for reports, targets, sources, concepts, and knowledge objects.
3. **Vocabulary layer** — controlled terms for themes, strategies, risks, industries, roles, and recurring concepts.
4. **Index layer** — CSV indexes for comparing targets, reports, sources, facts, claims, lessons, patterns, principles, and relationships.
5. **Knowledge layer** — source-linked facts, claims, lessons, patterns, and principles.

## 3. Directory Rules

Every directory must contain a local `INDEX.md` file.

Each local index must list only:

- files directly inside that directory;
- subdirectories directly inside that directory;
- short descriptions of each direct item.

Indexes must not recursively enumerate the repository.

## 4. Root Structure

Canonical top-level structure:

```text
/
  README.md
  LLM_ALIGNMENT.md
  INDEX.md

  specifications/
  indexes/
  targets/
  concepts/
  knowledge/
  synthesis/
  templates/
```

## 5. Target Structure

Targets are the primary historical units of study.

Target categories include:

- people;
- companies;
- events;
- comparison studies;
- failure cases;
- industries or markets when justified.

A deep target may include:

```text
INDEX.md
target.yaml
profile.md
timeline.md
historical-context.md
companies.md
business-and-organization.md
leadership-and-human-systems.md
capital-and-wealth.md
decision-making-and-judgment.md
lessons-to-copy.md
lessons-to-avoid.md
sources.md

business-and-organization/
leadership-and-human-systems/
capital-and-wealth/
decision-making-and-judgment/
lessons/
sources/
```

## 6. Naming Rules

Names must be:

- lowercase;
- hyphenated;
- descriptive;
- stable;
- human-readable;
- LLM-readable.

Prefer:

```text
cornelius-vanderbilt
wealth-creation
leadership-style
infrastructure-control
```

Avoid:

```text
misc
notes
research2
final-final
```

## 7. Expansion Rules

A file should be decomposed into a subdirectory when it becomes too large, mixes multiple distinct subjects, or becomes hard to navigate.

When decomposing:

1. Create a descriptive subdirectory.
2. Add `INDEX.md` to that subdirectory.
3. Move or create focused report files.
4. Update affected local indexes.
5. Preserve links and related metadata.

## 8. Knowledge System Rule

The repository separates knowledge into levels:

1. Sources — evidence artifacts.
2. Facts — directly supported statements.
3. Claims — interpretations of facts.
4. Lessons — teachable takeaways from claims.
5. Patterns — repeated lessons across targets.
6. Principles — durable abstractions supported by multiple patterns.

Knowledge should not be promoted upward without evidence and provenance.

## 9. Promotion Rules

- A fact requires source support.
- A claim requires supporting facts and source provenance.
- A lesson requires at least one supported claim.
- A pattern requires at least three targets, unless marked `candidate-pattern`.
- A strong pattern requires five or more targets across multiple industries, eras, or contexts.
- A principle requires at least three strong patterns and at least one considered counterexample.

## 10. Integrity Rules

- Every file must be indexed locally.
- Every important claim must preserve provenance.
- Every report should include YAML metadata unless explicitly exempted.
- Controlled vocabulary terms should be reused rather than reinvented.
- Duplicated knowledge should be avoided unless cross-reference or comparison requires it.
- Uncertainty must be preserved.
- Source-grounded facts must be separated from interpretation.

## 11. Implementation Order

Before expanding large target reports, maintain these specifications and indexes:

- `metadata-specification.md`
- `controlled-vocabulary.md`
- `index-schema.md`
- `knowledge-system-specification.md`
- `indexes/*.csv`

## 12. Operating Summary

Markdown teaches.

Metadata describes.

Vocabulary standardizes.

Indexes compare.

Provenance protects trust.
