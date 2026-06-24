# Negative Knowledge Protocol

## Purpose

This protocol defines how the repository preserves rejected, retired, disproven, or context-limited knowledge.

Negative knowledge prevents rediscovery of the same weak claims, myths, failed lessons, and overextended patterns.

## Object Types

Minimum object types:

- `rejected-fact`
- `rejected-claim`
- `rejected-lesson`
- `retired-pattern`
- `rejected-principle`

## Minimum Fields

Rejected or retired knowledge should preserve:

```text
rejection_id
object_type
object_id
statement
reason_rejected
disconfirming_evidence_ids
related_source_ids
replacement_object_id
status
review_date
```

## Status Values

Use these status values:

- `rejected`
- `retired`
- `superseded`
- `context-limited`
- `needs-review`

## Preservation Rule

Rejected objects should not be silently deleted when they are meaningful, recurring, plausible, or likely to be rediscovered.

Preserve:

- what was believed or proposed;
- why it was rejected;
- which evidence caused rejection;
- whether the rejection is final or context-dependent;
- what replaced it, if anything.

## Preferred Index

Use this index when created:

```text
indexes/rejections.csv
```

Optional later expansion:

```text
knowledge/rejected/
```

## Promotion Guard

A claim, lesson, pattern, or principle should not be promoted if materially similar rejected knowledge already exists unless the new object explains why it is different.
