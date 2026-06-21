# Index Schema Specification

## 1. Purpose

This specification defines CSV indexes used to compare and query repository knowledge without rereading every Markdown file.

Indexes are not the source of truth for narrative reports. They are navigation and analysis aids.

## 2. General CSV Rules

- Use UTF-8 CSV.
- First row must be the header.
- IDs must be stable.
- Paths must be repository-relative.
- Empty unknown fields should remain empty, not invented.
- Confidence values must be `low`, `medium`, or `high`.
- Status values must follow each index schema.

## 3. targets.csv

```csv
target_id,title,target_type,status,primary_path,period_start,period_end,geography,source_status,confidence
```

## 4. reports.csv

```csv
report_id,target_id,title,artifact_type,pillar,path,source_status,confidence,updated
```

## 5. sources.csv

```csv
source_id,title,author_or_creator,publisher_or_holder,publication_date,source_tier,source_type,related_targets,path,reliability_status
```

## 6. facts.csv

```csv
fact_id,statement,related_target,related_report,source_ids,confidence,status
```

Status values:

- `candidate`
- `accepted`
- `disputed`
- `retired`

## 7. claims.csv

```csv
claim_id,statement,related_target,related_report,supporting_fact_ids,source_ids,confidence,status
```

Status values:

- `candidate`
- `accepted`
- `disputed`
- `retired`

## 8. lessons.csv

```csv
lesson_id,statement,related_targets,related_claims,theme_ids,transferability,confidence,status
```

Transferability values:

- `still-valid`
- `context-dependent`
- `obsolete`
- `illegal-or-unethical-today`
- `unknown`

Status values:

- `candidate`
- `accepted`
- `disputed`
- `retired`

## 9. patterns.csv

```csv
pattern_id,statement,supporting_lesson_ids,supporting_target_count,theme_ids,confidence,status
```

Status values:

- `candidate-pattern`
- `accepted-pattern`
- `strong-pattern`
- `disputed-pattern`
- `retired-pattern`

## 10. principles.csv

```csv
principle_id,statement,supporting_pattern_ids,counterexamples_considered,confidence,status
```

Status values:

- `candidate-principle`
- `accepted-principle`
- `disputed-principle`
- `retired-principle`

## 11. relationships.csv

```csv
relationship_id,subject_id,relationship,object_id,evidence_path,source_ids,confidence,status
```

Relationship examples:

- `used-strategy`
- `operated-in`
- `controlled-asset`
- `related-to`
- `supports`
- `contradicts`
- `influenced`
- `founded`
- `acquired`
- `competed-with`

## 12. themes.csv

```csv
theme_id,preferred_label,alternative_labels,broader,related,definition,status
```

## 13. Update Rules

- When a target is created, update `targets.csv`.
- When a report is created, update `reports.csv`.
- When a source is added, update `sources.csv`.
- When a fact, claim, lesson, pattern, principle, or relationship is formalized, update its corresponding index.
- Do not index every sentence. Index only meaningful, reusable, or comparable knowledge.
