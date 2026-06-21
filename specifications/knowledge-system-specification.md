# Knowledge System Specification

## 1. Purpose

This specification defines how repository knowledge is created, promoted, compared, and preserved.

The repository is not merely a collection of reports. It is a historical knowledge system that separates evidence, facts, claims, lessons, patterns, and principles.

## 2. Knowledge Levels

### Level 0 — Sources

Sources are evidence artifacts.

Examples:

- books;
- filings;
- court records;
- interviews;
- newspapers;
- academic research;
- archived letters;
- company records.

A source provides evidence. It is not automatically truth.

### Level 1 — Facts

Facts are directly supported statements.

Example:

```text
Cornelius Vanderbilt died in 1877.
```

Facts must cite sources.

### Level 2 — Claims

Claims are interpretations of facts.

Example:

```text
Vanderbilt's advantage came partly from infrastructure control.
```

Claims must identify supporting facts and sources.

### Level 3 — Lessons

Lessons are teachable takeaways derived from claims.

Example:

```text
Control over critical routes can create strategic advantage.
```

Lessons must identify transferability and limits.

### Level 4 — Patterns

Patterns are repeated lessons across multiple targets.

A pattern normally requires at least three targets.

Example:

```text
Infrastructure control appears as a competitive advantage across multiple major business builders.
```

### Level 5 — Principles

Principles are durable abstractions supported by multiple strong patterns and tested against counterexamples.

Example:

```text
Control over movement, access, or distribution can create durable strategic advantage when paired with operational discipline and capital control.
```

## 3. Promotion Rules

### Fact Promotion

A statement may become a fact when:

- it is directly supported by at least one reliable source;
- it is not merely interpretation;
- uncertainty is preserved if sources conflict.

### Claim Promotion

A claim may become accepted when:

- it is supported by facts;
- at least one reliable source chain exists;
- competing interpretations are acknowledged when material.

### Lesson Promotion

A lesson may become accepted when:

- it is derived from one or more accepted or well-supported claims;
- transferability is evaluated;
- modern context is considered;
- limits are documented.

### Pattern Promotion

A lesson may become a candidate pattern after appearing in two targets.

A pattern may become accepted after appearing in at least three targets.

A pattern may become strong after appearing in at least five targets across multiple industries, eras, or contexts.

### Principle Promotion

A principle may become accepted only when:

- at least three strong patterns support it;
- counterexamples have been considered;
- scope limits are documented;
- source provenance remains traceable.

## 4. Transferability Classification

Every lesson should be classified as one of:

- `still-valid` — broadly transferable today.
- `context-dependent` — useful only with adaptation.
- `obsolete` — dependent on historical conditions no longer present.
- `illegal-or-unethical-today` — should be studied only as warning or history.
- `unknown` — insufficient evidence.

## 5. Provenance Rule

Every important claim must trace backward:

```text
source -> fact -> claim -> lesson -> pattern -> principle
```

If the chain is incomplete, the knowledge object must remain candidate or developing.

## 6. Comparison Rule

Cross-target comparison should compare like with like.

Examples:

- lesson to lesson;
- pattern to pattern;
- strategy to strategy;
- capital mechanism to capital mechanism;
- leadership behavior to leadership behavior.

Do not compare vague narratives when structured knowledge objects can be compared.

## 7. Uncertainty Rule

The repository must preserve uncertainty.

Use clear status values:

- `candidate`
- `accepted`
- `disputed`
- `retired`

Do not erase uncertainty merely to make the repository cleaner.

## 8. Practical Rule

Do not create a separate Markdown file for every small fact at the beginning.

Start with:

- CSV index rows for facts and claims;
- source-linked report sections;
- separate Markdown files only for major lessons, patterns, and principles when they become substantial.

This keeps the repository scalable without creating file explosion too early.
