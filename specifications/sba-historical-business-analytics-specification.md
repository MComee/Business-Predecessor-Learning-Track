# SBA Historical Business Analytics Specification

## Purpose

This specification defines how SBA business-planning guidance is used as an analytical lens for historical targets.

SBA guidance is a practical planning baseline. It is not automatic historical proof.

Historical target evidence remains the proof source.

## Core Model

```text
SBA category -> historical target evidence -> planning signal -> claim -> lesson -> pattern -> principle
```

## Traditional Business Plan Categories

Use these categories when historically relevant:

- executive-summary
- company-description
- market-analysis
- organization-and-management
- service-or-product-line
- marketing-and-sales
- funding-request
- financial-projections
- appendix-supporting-documents

## Lean Business Plan Categories

Use these categories when historically relevant:

- key-partnerships
- key-activities
- key-resources
- value-proposition
- customer-relationships
- customer-segments
- channels
- cost-structure
- revenue-streams

## Emergency and Resilience Categories

Use these categories when historically relevant:

- risk-assessment
- emergency-response-plan
- continuity-of-operations
- staff-practice
- financial-assistance-readiness
- mitigation
- cyberattack-preparedness

## Growth Categories

Use these categories when historically relevant:

- growth-funding
- new-location-readiness
- merger-acquisition-readiness
- federal-contracting-readiness
- export-readiness
- legal-compliance-for-expansion
- market-dependence-reduction

## Planning Signal Rule

A planning signal is a historically observed behavior mapped to a planning category.

A planning signal should preserve:

```text
signal_id
target_id
sba_category
observed_behavior
signal_type
outcome_type
source_ids
fact_ids
claim_ids
assumptions
invalidation_triggers
confidence
status
```

## Pattern Rule

A business-planning pattern may be proposed only after planning signals are compared across targets.

Planning patterns should preserve:

```text
pattern_id
sba_categories
statement
supporting_signal_ids
supporting_target_count
success_count
failure_count
counterexamples_considered
assumptions
failure_conditions
time_horizon
confidence
status
```

## Proof Rule

SBA categories organize analysis. They do not prove causation.

Do not convert planning advice into historical lessons unless target evidence supports it.

## Use Rule

This layer should help answer:

- which planning behaviors repeatedly appear before success;
- which planning gaps repeatedly appear before failure;
- which resilience behaviors appear before crisis survival;
- which capital, market, and operating signals appear before scale or decline.
