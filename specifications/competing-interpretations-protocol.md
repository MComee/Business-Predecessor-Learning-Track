# Competing Interpretations Protocol

## Purpose

This protocol defines how to document legitimate competing explanations when evidence supports more than one plausible interpretation.

The repository should not collapse complex business history into a single attractive narrative when multiple explanations remain credible.

## Applies To

Use this protocol for:

- major claims;
- controversial lessons;
- synthesis artifacts;
- candidate patterns;
- accepted patterns;
- principles.

## Minimum Requirements

When competing interpretations are material, record:

```text
interpretation_id
statement
supporting_evidence_ids
conflicting_evidence_ids
confidence
status
preferred_interpretation
reason_preferred
```

## Interpretation Status

Use these values:

- `candidate`
- `supported`
- `preferred`
- `disputed`
- `rejected`
- `retired`

## Preference Rule

One interpretation may be preferred only when the reason is explicit.

Acceptable reasons include:

- stronger source tier;
- more direct evidence;
- better chronological fit;
- better explanation of conflicting facts;
- lower dependence on speculation;
- stronger cross-target support.

## Uncertainty Rule

If two interpretations remain plausible, preserve both.

Do not force certainty for readability.

## Promotion Guard

A claim or pattern with unresolved competing interpretations may still be useful, but its confidence must not exceed the evidence.
