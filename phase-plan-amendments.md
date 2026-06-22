# Phase Plan Amendments

This document amends and strengthens `Phase Plan.md` prior to implementation.

## Amendment 1 — Negative Knowledge System

Add formal support for:

- rejected facts
- rejected claims
- rejected lessons
- retired patterns
- rejected principles

Create either:

```text
knowledge/rejected/
```

or:

```text
indexes/rejections.csv
```

Purpose:

Preserve what was disproven, why it was disproven, and what evidence caused retirement.

---

## Amendment 2 — Time-Sensitivity Classification

Extend lesson and pattern metadata.

Add:

```text
time_horizon:
  short-term
  medium-term
  long-term
  structural
```

Purpose:

Distinguish durable principles from era-specific observations.

---

## Amendment 3 — Assumptions Registry

Add explicit assumption tracking.

Every major claim, pattern, and principle should document:

- assumptions
- dependency conditions
- invalidation triggers

Purpose:

Preserve reasoning context and detect when facts remain true but assumptions change.

---

## Amendment 4 — Pattern Failure Conditions

Extend pattern requirements.

Every accepted pattern should document:

- success conditions
- failure conditions
- limits
- transferability

Purpose:

Teach not only when a pattern works but when it stops working.

---

## Amendment 5 — Competing Interpretations

Add explicit support for:

```text
competing_interpretations
```

within major claims and synthesis artifacts.

Purpose:

Preserve legitimate historical disagreement and avoid false certainty.

---

## Amendment 6 — Early Validation Phase

Insert:

```text
Phase 0.5 — Minimal Validation Foundation
```

before large-scale expansion.

Minimum checks:

- INDEX presence
- path validity
- CSV header validation
- ID uniqueness

Purpose:

Prevent structural errors from compounding.

---

## Amendment 7 — Early LLM Governance

Move LLM governance from Phase 8 into a Phase 1.5 governance gate.

Purpose:

The repository is LLM-assisted from the beginning; governance should be established before growth.

---

## Amendment 8 — Elevate Falsification Protocol

Treat:

```text
counterexample-and-falsification-protocol.md
```

as a foundational repository specification equal in importance to the knowledge-system specification.

Purpose:

Reduce survivorship bias, winner bias, and principle inflation.

---

## Acceptance Requirement

No principle may be accepted unless:

- supporting patterns exist
- counterexamples are documented
- assumptions are documented
- failure conditions are documented
- competing interpretations have been considered
- provenance remains traceable

These amendments become part of the governing phase-plan architecture and should be incorporated into future implementation work packets, specifications, workflows, metadata schemas, and validation rules.
