# Metadata Specification

## 1. Purpose

This specification defines YAML metadata requirements for repository artifacts.

Metadata makes reports and knowledge objects findable, comparable, reusable, and easier for humans and LLMs to navigate.

## 2. Required Metadata for Reports

Every report should begin with YAML front matter.

```yaml
---
id: report:<target-type>:<target-slug>:<report-slug>
target_id: target:<target-type>:<target-slug>
title: <Human-readable title>
artifact_type: report
pillar: <business-and-organization | leadership-and-human-systems | capital-and-wealth | decision-making-and-judgment | cross-pillar>
topics:
  - <controlled-topic-term>
themes:
  - <controlled-theme-term>
industries:
  - <controlled-industry-term>
period:
  start: <year-or-null>
  end: <year-or-null>
geography:
  - <controlled-geography-term>
source_status: <none | developing | partial | strong | primary-supported>
confidence: <low | medium | high>
related_reports:
  - <report-id>
updated: <YYYY-MM-DD>
---
```

## 3. Required Metadata for Targets

Each target should have a `target.yaml` file.

```yaml
id: target:<target-type>:<target-slug>
title: <Target name>
target_type: <person | company | event | comparison | failure-case | industry>
status: <scaffold | researching | developing | mature | archived>
primary_pillars:
  - <pillar>
industries:
  - <industry>
period:
  start: <year-or-null>
  end: <year-or-null>
geography:
  - <geography>
related_targets:
  - <target-id>
source_status: <none | developing | partial | strong | primary-supported>
confidence: <low | medium | high>
```

## 4. Required Metadata for Sources

```yaml
id: source:<slug>
title: <Source title>
author_or_creator: <name>
publisher_or_holder: <name>
publication_date: <date-or-null>
access_date: <YYYY-MM-DD-or-null>
source_tier: <1 | 2 | 3 | 4 | 5 | 6>
source_type: <book | article | filing | court-record | interview | archive | report | other>
related_targets:
  - <target-id>
reliability_notes: <short note>
```

## 5. Required Metadata for Knowledge Objects

Facts, claims, lessons, patterns, and principles should receive stable IDs.

```yaml
id: <object-type>:<slug>
object_type: <fact | claim | lesson | pattern | principle>
status: <candidate | accepted | disputed | retired>
confidence: <low | medium | high>
supporting_sources:
  - <source-id>
supporting_objects:
  - <fact-or-claim-or-lesson-id>
related_targets:
  - <target-id>
related_themes:
  - <theme-id>
```

## 6. Status Values

### Source status

- `none` — no sources attached.
- `developing` — initial sources identified.
- `partial` — enough sources for preliminary analysis.
- `strong` — multiple reliable source types support the artifact.
- `primary-supported` — key factual claims are supported by primary records.

### Confidence

- `low` — early, weak, incomplete, or disputed.
- `medium` — supported but still needs more verification.
- `high` — strong evidence and low reasonable dispute.

## 7. Metadata Discipline

Metadata must not overstate certainty.

If source support is incomplete, use `developing`, `partial`, or `low` confidence rather than implying completion.
