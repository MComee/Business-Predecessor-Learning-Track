# Step-by-Step Phase Plan

Adoption plan for strengthening `Business-Predecessor-Learning-Track` from a strong public learning scaffold into a governed, source-grounded, historically tested, machine-checkable business knowledge system.

This file is itself a governed repository artifact. It uses lowercase hyphenated naming to comply with the repository naming rule.

---

## Strategic Goal

Convert this repository into a public, repository-native business-history learning system that remains easy for humans and LLMs to use while becoming deterministic enough to validate locally and through CI.

The repository core remains:

1. **Business & Organizations**
2. **Leadership & Human Systems**
3. **Capital & Wealth**
4. **Decision Making & Judgment**

The knowledge ladder remains:

```text
Sources -> Facts -> Claims -> Lessons -> Patterns -> Principles
```

Knowledge is promoted upward only when evidence supports it.

The repository should stay GitHub-native for access and collaboration, but it must become locally and remotely machine-checkable through a repository-contained validator.

Operating rule:

```text
Remote-native for access.
Local/CI-checked for truth.
Branch-based for change.
Validator-gated for maturity.
```

---

## Authoritative Verification Baseline

This phase plan is aligned against these checks:

| Check | Baseline |
|---|---|
| Check 1 — Source code | No executable code is added until the validator phase. When code is added, it is read-only first and follows NIST SSDF principles. |
| Check 2 — NIST | LLM governance maps to NIST AI RMF. Future validator and CI work maps to NIST SP 800-218 SSDF. Resilience/cyber planning concepts should cite NIST where relevant. |
| Check 3 — Offensive security | Cybersecurity content is defensive, business-risk, continuity, governance, and resilience oriented only. OWASP LLM risks guide LLM safety. |
| Check 4 — Computer science | The plan preserves separation of concerns, stable IDs, schemas, validation, deterministic checks, and composable text artifacts. |
| Check 5 — Domain sources | SBA business-plan categories are used as planning lenses, not proof. Historical evidence remains the proof source. |
| Check 6 — Little LISPer / Little Schemer | Repair base cases before recursion: sources before facts, facts before claims, claims before lessons, lessons before patterns, patterns before principles. |
| Check 7 — Unix Philosophy | Keep files small, text-first, composable, locally indexed, and independently useful. |

Authoritative references to use when implementing this plan:

- NIST SP 800-218, *Secure Software Development Framework (SSDF) Version 1.1* — secure software development practices for future validator and CI work.
- NIST AI Risk Management Framework — AI/LLM governance and trustworthiness considerations.
- OWASP Top 10 for Large Language Model Applications — prompt injection, insecure output handling, excessive agency, overreliance, and related LLM risks.
- GitHub Actions workflow syntax documentation — event-triggered CI and workflow permissions.
- U.S. Small Business Administration business-plan guidance — traditional and lean business-plan categories used only as historical planning lenses.
- Repo-native specifications — the governing truth source for structure, metadata, indexes, knowledge promotion, and local navigation.

---

## Universal Definition of Done

A new or modified repository artifact is not complete until all applicable items are satisfied:

- filename is lowercase, hyphenated, descriptive, stable, human-readable, and LLM-readable;
- local `INDEX.md` is updated for every affected directory;
- YAML front matter exists when required, or an explicit exemption is documented;
- source-grounded claims cite or identify source records;
- unsupported material is labeled as candidate, uncertain, disputed, or source-debt;
- facts, claims, lessons, patterns, principles, targets, reports, sources, relationships, themes, and planning signals update CSV indexes when formalized;
- controlled vocabulary is reused before new terms are introduced;
- no claim is promoted without source and fact support;
- no pattern or principle is promoted before evidence thresholds are met;
- validator passes when a validator exists;
- unresolved source debt is recorded instead of hidden.

---

## Repository Change-Control Rule

All non-trivial changes should occur on a branch.

`main` should represent the latest validated public state.

LLM-assisted repository edits must state:

- branch used;
- files changed;
- reason for change;
- validation performed;
- unresolved source debt;
- whether any claims, lessons, patterns, or principles were promoted.

Direct writes to `main` should be reserved for explicitly authorized emergency documentation repair.

Recommended branch patterns:

```text
plan/<short-purpose>
audit/<short-purpose>
content/<target-or-topic>
validation/<short-purpose>
```

---

## Rollback and Repair Rule

If validation fails after a phase:

1. Do not continue to the next phase.
2. Create a repair note or issue.
3. Fix index, schema, path, metadata, source, or provenance errors first.
4. Do not add new target content while integrity is broken.
5. Re-run validation before continuing.

The repository should not accumulate knowledge on top of inconsistent structure.

---

## Phase -1 — Repository Operating Model

### Purpose

Define how humans, LLMs, GitHub branches, local clones, validators, and CI interact before structural changes begin.

### Operating Model

```text
GitHub repository = canonical source of truth
local clone = validation and repair workspace
GitHub Actions = remote machine-check gate
LLM sessions = controlled editors and reviewers, not final validators
```

### Required Policy

Define and document:

```yaml
canonical_branch: main
work_branch_pattern:
  - plan/<short-purpose>
  - audit/<short-purpose>
  - content/<target-or-topic>
  - validation/<short-purpose>
direct_main_writes: prohibited except explicitly authorized emergency documentation repair
local_validation: preferred before push
remote_validation: required once CI exists
llm_write_mode: branch-first unless user explicitly authorizes direct commit
merge_condition: validator passes
```

### Acceptance Criteria

- This operating model is present in `phase-plan.md`.
- Root `INDEX.md` references `phase-plan.md` using lowercase hyphenated naming.
- Future work begins from branches where practical.
- LLM-assisted writes report changed files and validation status.

### Seven-Check Gate

| Check | Gate |
|---|---|
| Source code | No executable code added. |
| NIST | Establish governance before automation. |
| Offensive security | No offensive content. |
| Computer science | Define source of truth and validation boundary. |
| Domain sources | Repo-native specifications remain authoritative. |
| Little Schemer / LISPer | Establish base operating case before recursive work. |
| Unix Philosophy | Separate storage, editing, validation, and publication concerns. |

---

## Phase 0 — Baseline Integrity Repair

### Purpose

Fix structural inconsistencies before adding new knowledge. This prevents the repository from scaling with broken navigation, weak provenance, or inconsistent names.

### Work Items

#### 0.1 Rename phase plan file

Rename:

```text
Phase Plan.md
```

to:

```text
phase-plan.md
```

Update root `INDEX.md` accordingly.

#### 0.2 Fix `specifications/INDEX.md`

Update it to list all direct specification files:

```text
repository-specification.md
metadata-specification.md
controlled-vocabulary.md
index-schema.md
knowledge-system-specification.md
```

Local indexes must list direct files and direct subdirectories only.

#### 0.3 Add missing Vanderbilt `target.yaml`

Add:

```text
targets/people/cornelius-vanderbilt/target.yaml
```

The file must agree with `indexes/targets.csv`.

#### 0.4 Repair claim-to-fact linkage

Every claim in `indexes/claims.csv` must have:

- `source_ids`; and
- `supporting_fact_ids`, or a clear exception status such as `needs-fact-linkage` if the schema is extended to support that status.

No claim may be promoted beyond candidate until the base evidence chain is valid.

#### 0.5 Add source-record resolution rule

Every source ID used in facts, claims, reports, or lessons must resolve to a source row and, where applicable, a source metadata file.

For the current Vanderbilt scaffold, `source:the-first-tycoon` must resolve before further Vanderbilt expansion.

### Acceptance Criteria

- `phase-plan.md` exists and `Phase Plan.md` is removed.
- Root `INDEX.md` references `phase-plan.md`.
- Every direct file in `specifications/` appears in `specifications/INDEX.md`.
- Vanderbilt has `target.yaml`.
- `targets.csv` and Vanderbilt `target.yaml` agree.
- Every claim has `source_ids`.
- Every claim has `supporting_fact_ids` or an explicit exception status.
- Every referenced source ID resolves.
- No accepted lessons, patterns, or principles are promoted during this phase.
- No claim confidence is raised above `medium` unless primary-source support exists.

### Seven-Check Gate

| Check | Gate |
|---|---|
| Source code | No executable code added. |
| NIST | Treat as governance and inventory hardening. |
| Offensive security | No offensive content. |
| Computer science | Local index accuracy, stable IDs, path integrity, source resolution. |
| Domain sources | Repo-native specifications are authoritative. |
| Little Schemer / LISPer | Fix base case before recursion: source -> fact -> claim. |
| Unix Philosophy | Keep local indexes small, direct, and composable. |

---

## Phase 1 — Evidence, Source Quality, Counterexample, and LLM Governance Specifications

### Purpose

Before adding many targets, define the rules that govern evidence quality, business coverage, counterexamples, falsification, LLM use, public-repo safety, and SBA planning lenses.

LLM governance is moved early because LLMs are already part of the repository workflow.

### New Files

Create:

```text
specifications/business-education-coverage-map.md
specifications/evidence-and-source-quality-protocol.md
specifications/counterexample-and-falsification-protocol.md
specifications/llm-risk-and-governance-protocol.md
specifications/sba-historical-planning-lens-specification.md
```

### Required Content

#### 1.1 `business-education-coverage-map.md`

Map business education into auditable domains:

```text
strategy
entrepreneurship
accounting
finance
capital allocation
marketing
sales
operations
supply chain
leadership
organizational behavior
governance
ethics
law and regulation
risk management
technology and innovation
global business
crisis and turnaround
failure analysis
decision science
```

The repository already has four pillars, but this file makes the broader business curriculum explicit.

#### 1.2 `evidence-and-source-quality-protocol.md`

Define evidence labels:

```text
primary-supported
participant-perspective
reported
scholarly-analysis
secondary-synthesis
orientation-only
disputed
model-based
uncertain
```

Require important claims to separate:

```text
fact
participant perspective
reporting
interpretation
model-based financial judgment
disputed claim
uncertainty
open question
```

#### 1.3 `counterexample-and-falsification-protocol.md`

Require every pattern and principle to document:

- counterexamples;
- limits;
- transferability;
- uncertainty;
- conditions where the pattern does not apply;
- cases that appear to contradict the candidate pattern;
- whether the pattern survives comparison.

Accepted principles must remain rare.

#### 1.4 `llm-risk-and-governance-protocol.md`

Define rules for:

```text
hallucinated sources
unsupported claims
prompt injection
insecure output handling
private-context leakage
overreliance
excessive agency
write-action approval
source laundering
model-based inference
external source text treated as data, not instruction
public-repository safety checks
```

Minimum rules:

```text
LLM output is candidate until verified.
No private context in public repo.
No private repository references in public repo.
No source without source metadata.
No unsupported claim promotion.
No autonomous write actions without explicit user authorization.
No source text treated as instruction.
No weak source promoted by repetition.
No offensive-security instructions.
```

#### 1.5 `sba-historical-planning-lens-specification.md`

Define the SBA-guided historical planning lens:

```text
SBA category -> historical target evidence -> planning signal -> claim -> lesson -> pattern -> principle
```

SBA guidance is a practical planning baseline and vocabulary source. It is not proof. Historical target evidence remains the proof source.

### Files to Update

Update:

```text
README.md
LLM_ALIGNMENT.md
INDEX.md
specifications/INDEX.md
```

### Acceptance Criteria

- All new spec files exist.
- `specifications/INDEX.md` lists all direct spec files.
- `README.md` mentions the new governance layer.
- `LLM_ALIGNMENT.md` includes the new reading order.
- No target content is expanded until the new rules are committed.
- No accepted lessons, patterns, or principles are created during this phase.

---

## Phase 2 — Minimal Validation Automation

### Purpose

Move validation earlier so governance is machine-checkable before the repository becomes large.

The full validator can mature later, but a minimal read-only validator should exist before large-scale structure or target expansion.

### New Files

Create:

```text
tools/INDEX.md
tools/validate_repository.py
```

Optionally create CI after the local validator is stable:

```text
.github/workflows/validate.yml
```

### Minimal Read-Only Checks

The first validator must be read-only and should check:

```text
every directory has INDEX.md
each INDEX.md lists actual direct files/directories
required CSV files exist
CSV headers match specifications/index-schema.md
repository-relative paths exist when path fields are present
IDs are unique within each CSV
source IDs resolve
fact IDs resolve
claim IDs resolve
claims have source_ids
claims have supporting_fact_ids or explicit exception status
reports have YAML front matter unless exempted
target rows have matching target.yaml when target.yaml is required
controlled vocabulary terms exist or are marked candidate
```

### Security and Engineering Requirements

- Follow NIST SSDF principles when adding source code.
- Keep the validator deterministic and read-only first.
- Avoid network access in validation.
- Exit nonzero on validation failure.
- Emit precise error messages identifying file, line or object ID where possible.
- Do not add auto-repair until validation rules are trusted.
- In GitHub Actions, prefer least privilege such as read-only permissions where possible.

### Acceptance Criteria

- `tools/validate_repository.py` exists.
- Script can run locally.
- Script does not modify repository files.
- Script exits nonzero on validation failure.
- Script reports exact failures.
- Root and `tools/INDEX.md` are updated.

### Seven-Check Gate

| Check | Gate |
|---|---|
| Source code | Read-only validator; deterministic; SSDF-aligned. |
| NIST | Validator follows secure-development discipline and least privilege. |
| Offensive security | No offensive functionality. |
| Computer science | Machine-checkable invariants and clear failure states. |
| Domain sources | Repo-native specs drive validation. |
| Little Schemer / LISPer | Validator checks base cases before higher-level promotion. |
| Unix Philosophy | One tool does one job: validate repository integrity. |

---

## Phase 3 — SBA Historical Planning Lens

### Purpose

Create a planning lens that maps SBA guidance to historical evidence, then uses cross-target analysis to test which planning behaviors appear in success, failure, funding, resilience, growth, or decline.

This is a lens, not a second repository core. The core remains the Four Pillars plus the knowledge ladder.

### New Directory

Create:

```text
sba-historical-planning/
  INDEX.md
  sba-guidance-map.md
  historical-testing-protocol.md
  planning-category-schema.md
  target-scoring-template.md
  cross-target-analytics.md
  crisis-and-resilience/
    INDEX.md
    risk-assessment.md
    emergency-response-plan.md
    continuity-of-operations.md
    disaster-recovery-finance.md
    mitigation-and-prevention.md
  patterns/
    INDEX.md
  case-notes/
    INDEX.md
```

### SBA Categories to Encode

#### Traditional Plan Categories

Encode:

```text
executive-summary
company-description
market-analysis
organization-and-management
service-or-product-line
marketing-and-sales
funding-request
financial-projections
appendix-supporting-documents
```

#### Lean Plan Categories

Encode:

```text
key-partnerships
key-activities
key-resources
value-proposition
customer-relationships
customer-segments
channels
cost-structure
revenue-streams
```

#### Emergency and Resilience Categories

Encode:

```text
risk-assessment
emergency-response-plan
continuity-of-operations
staff-practice
financial-assistance-readiness
mitigation
cyberattack-preparedness
```

#### Growth Categories

Encode:

```text
growth-funding
new-location-readiness
merger-acquisition-readiness
federal-contracting-readiness
export-readiness
legal-compliance-for-expansion
market-dependence-reduction
```

### New CSV Indexes

Create:

```text
indexes/planning-signals.csv
indexes/business-planning-patterns.csv
```

Suggested headers:

```csv
signal_id,target_id,sba_category,observed_behavior,signal_type,outcome_type,source_ids,fact_ids,claim_ids,confidence,status
```

```csv
pattern_id,sba_categories,statement,supporting_signal_ids,supporting_target_count,success_count,failure_count,counterexamples_considered,confidence,status
```

### Files to Update

Update:

```text
indexes/INDEX.md
specifications/index-schema.md
README.md
LLM_ALIGNMENT.md
```

### Acceptance Criteria

- SBA categories are mapped.
- Planning signal schema exists.
- Planning pattern schema exists.
- SBA historical planning lens has its own `INDEX.md`.
- SBA guidance is treated as a baseline, not automatic truth.
- Historical target evidence remains the proof source.
- Validator passes.

---

## Phase 4 — Concept Spines

### Purpose

Create reusable concept explanations so target reports do not repeatedly redefine basic business, finance, accounting, strategy, leadership, risk, decision-making, and planning terms.

### New Files

#### Business / Strategy

```text
concepts/business/strategy-framework-registry.md
concepts/business/business-models.md
concepts/business/competitive-advantage.md
concepts/business/distribution-and-channels.md
concepts/business/operations-and-scale.md
concepts/business/marketing-and-sales.md
```

#### Capital / Finance / Accounting

```text
concepts/capital/accounting-basics.md
concepts/capital/financial-statements.md
concepts/capital/cash-flow.md
concepts/capital/unit-economics.md
concepts/capital/capital-structure.md
concepts/capital/valuation.md
concepts/capital/capital-allocation.md
concepts/capital/solvency-and-bankruptcy.md
```

#### Leadership

```text
concepts/leadership/leadership-style.md
concepts/leadership/culture-and-standards.md
concepts/leadership/incentives-and-accountability.md
concepts/leadership/delegation-and-control.md
concepts/leadership/succession-risk.md
concepts/leadership/ethical-leadership.md
concepts/leadership/crisis-leadership.md
```

#### Decision-Making

```text
concepts/decision-making/risk-and-uncertainty.md
concepts/decision-making/opportunity-cost.md
concepts/decision-making/counterfactual-analysis.md
concepts/decision-making/feedback-loops.md
concepts/decision-making/crisis-decisions.md
```

#### Historical Planning Lens

```text
concepts/business/sba-historical-planning-lens.md
concepts/business/investor-persuasion.md
concepts/business/emergency-preparedness.md
concepts/business/growth-readiness.md
```

### Acceptance Criteria

- Every concept file has YAML metadata or a declared exemption.
- Every concept file uses controlled vocabulary where applicable.
- `concepts/INDEX.md` and local subdirectory indexes are updated.
- Concept files define scope, misuse risks, evidence requirements, and example target links.
- Validator passes.

### Seven-Check Gate

| Check | Gate |
|---|---|
| Source code | No new executable code unless validator updates are required. |
| NIST | Cyber/resilience concepts cite NIST where applicable. |
| Offensive security | Cybersecurity remains defensive/business-risk only. |
| Computer science | Modular, reusable concept files. |
| Domain sources | SBA, NIST, SEC, academic/business-school sources where relevant. |
| Little Schemer / LISPer | Concepts are atoms; target reports compose them. |
| Unix Philosophy | One concept per file; no monolith. |

---

## Phase 5 — Templates and Workflows

### Purpose

Make new rules operational so every future target uses the same structure and workflow.

### Update Templates

Update:

```text
templates/target-template.md
templates/deep-target-template.md
templates/source-template.md
```

Add this section to target templates:

```markdown
## SBA Historical Planning Lens

### Strategic thesis / executive summary
### Company description / problem solved
### Market analysis
### Organization and management
### Product or service line
### Marketing and sales
### Funding and capital readiness
### Financial projections or expectations
### Key partnerships
### Key activities
### Key resources
### Value proposition
### Customer relationships
### Customer segments
### Channels
### Cost structure
### Revenue streams
### Emergency preparedness and resilience
### Cybersecurity and digital risk
### Growth, expansion, acquisition, or export readiness
### Evidence-grounded planning signals
### Lessons to copy
### Lessons to avoid
### Open questions
```

### Add Workflow Files

Create:

```text
workflows/
  INDEX.md
  target-research-workflow.md
  source-evaluation-workflow.md
  claim-promotion-workflow.md
  sba-planning-signal-workflow.md
  pattern-synthesis-workflow.md
  failure-case-workflow.md
  validation-workflow.md
```

### Acceptance Criteria

- Templates include the SBA historical planning lens.
- Workflows describe exact steps for future LLMs and humans.
- `README.md` and `LLM_ALIGNMENT.md` reference workflows.
- No target is expanded without using updated templates.
- Validator passes.

---

## Phase 6 — Vanderbilt as Fully Compliant Model Target

### Purpose

Use Vanderbilt as the first fully compliant model target before adding many new targets.

Vanderbilt should become the standard example for how a target is structured, sourced, indexed, and validated.

### Precondition

No Vanderbilt expansion until:

- source records exist for all cited sources;
- `source:the-first-tycoon` resolves;
- Vanderbilt `target.yaml` exists;
- claim-to-fact linkage is repaired;
- validator passes.

### Work Items

#### 6.1 Add target metadata

```text
targets/people/cornelius-vanderbilt/target.yaml
```

#### 6.2 Add source debt file

```text
targets/people/cornelius-vanderbilt/sources/source-debt.md
```

Track missing:

```text
estate records
court records
contemporary newspapers
railroad records
shipping records
specialized economic history
Vanderbilt University primary material
```

#### 6.3 Add source records

Create or update source records for every Vanderbilt source ID used in CSV indexes or reports.

At minimum:

```text
source:the-first-tycoon
```

#### 6.4 Add deep reports

```text
targets/people/cornelius-vanderbilt/business-and-organization/route-control.md
targets/people/cornelius-vanderbilt/business-and-organization/steamboat-competition.md
targets/people/cornelius-vanderbilt/business-and-organization/railroad-consolidation.md
targets/people/cornelius-vanderbilt/capital-and-wealth/wealth-creation-mechanisms.md
targets/people/cornelius-vanderbilt/capital-and-wealth/estate-and-succession.md
targets/people/cornelius-vanderbilt/leadership-and-human-systems/founder-dominance.md
targets/people/cornelius-vanderbilt/decision-making-and-judgment/nicaragua-route.md
targets/people/cornelius-vanderbilt/sba-historical-planning-lens.md
```

#### 6.5 Add Vanderbilt planning signals

Examples:

```text
channels -> route control
key resources -> vessels, capital, route access
cost structure -> cost discipline / price war exposure
growth funding -> reinvestment and asset control
succession planning -> estate concentration and family conflict
emergency/crisis -> wartime transportation, rail accident, market disruption
```

### Acceptance Criteria

- Every new file is indexed locally.
- Vanderbilt target has source debt, fact/claim linkage, source records, planning signals, and pillar coverage.
- No pattern is accepted from Vanderbilt alone.
- Lessons remain target-specific unless cross-target support exists.
- Validator passes.

---

## Phase 7 — Coverage Matrix and Contrasting Target Selection

### Purpose

Prevent overfitting the repository around one era, one country, one type of founder, one industry, or only success cases.

### New File

Create:

```text
synthesis/target-coverage-matrix.md
```

Optionally create:

```text
indexes/target-coverage.csv
```

### Required Coverage Fields

Track:

```text
target_id
era
industry
geography
success/failure/turnaround
primary pillar strengthened
capital relevance
leadership relevance
operations relevance
regulatory relevance
source availability
counterexample value
```

### Acceptance Criteria

- Proposed targets are justified by coverage gap.
- Failure, decline, crisis, and international cases are actively considered.
- Target additions are not driven only by fame or personal interest.
- Validator passes.

---

## Phase 8 — Add Contrasting Targets

### Purpose

The repository cannot produce real patterns until it has multiple targets across industries, eras, outcomes, geographies, governance environments, and failure modes.

Candidate patterns may appear after two targets, accepted patterns normally require three targets, strong patterns require five targets across multiple industries, eras, or contexts, and accepted principles require three strong patterns plus at least one counterexample.

### Initial Target Sequence

Use this as a starting queue, but verify it against the coverage matrix before implementation:

| Order | Target | Why |
|---:|---|---|
| 1 | John D. Rockefeller / Standard Oil | Integration, cost discipline, antitrust, scale |
| 2 | Andrew Carnegie / Carnegie Steel | Operations, technology, vertical integration, labor conflict |
| 3 | J. P. Morgan | Finance, consolidation, governance, systemic risk |
| 4 | Sears | Distribution, retail, catalog strength, decline |
| 5 | Toyota | Operations, quality systems, production discipline |
| 6 | Kodak | Innovation failure, disruption, incumbent blindness |
| 7 | Walmart / Sam Walton | Logistics, rural market strategy, culture, cost advantage |
| 8 | Starbucks / Howard Schultz | Brand, culture, scaling, capital markets |
| 9 | Berkshire Hathaway / Warren Buffett | Capital allocation, decentralization, insurance float |
| 10 | Blockbuster vs Netflix | Business-model transition, digital disruption |

### Acceptance Criteria

- Each target has `target.yaml`.
- Each target has at least one source record.
- Each target has four-pillar coverage.
- Each target has planning-signal coding where applicable.
- Failure and counterexample notes are recorded.
- No principle is accepted before thresholds are met.
- Validator passes.

---

## Phase 9 — Cross-Target Analytics and Synthesis

### Purpose

Turn accumulated target data into reusable patterns and eventually principles.

### Work Items

Create or expand:

```text
synthesis/recurring-patterns.md
synthesis/cross-company-lessons.md
synthesis/failure-patterns.md
sba-historical-planning/cross-target-analytics.md
sba-historical-planning/patterns/sba-planning-patterns.md
```

### Analytics Levels

#### Level 1 — Count signals

```text
How many targets show the signal?
How many successful targets?
How many failed targets?
How many crisis-survival cases?
How many source-supported cases?
```

#### Level 2 — Compare conditions

```text
industry
era
company age
capital structure
regulatory environment
technology transition
founder-led vs institution-led
crisis vs normal growth
```

#### Level 3 — Promote patterns

```text
candidate-pattern
accepted-pattern
strong-pattern
disputed-pattern
retired-pattern
```

#### Level 4 — Test principles

No accepted principle without:

```text
three strong patterns
counterexamples
scope limits
transferability label
source provenance
```

### Acceptance Criteria

- Pattern rows cite supporting lesson or planning-signal IDs.
- Counterexamples are recorded.
- Pattern confidence does not exceed evidence.
- Historical tactics are labeled if illegal, unethical, obsolete, or context-dependent today.
- Validator passes.

---

## Phase 10 — Full Validation Automation and CI Hardening

### Purpose

Mature from manual and minimal validation into full machine-checkable governance.

### Expand Validator

Expand:

```text
tools/validate_repository.py
```

Full checks should include:

```text
every directory has INDEX.md
every INDEX.md lists actual direct files/directories
CSV headers match specification
all repository-relative paths exist
IDs are unique
source IDs resolve
fact IDs resolve
claim IDs resolve
claims have supporting fact IDs or exception status
reports have YAML front matter unless exempted
target rows have matching target.yaml
planning signals resolve to source/fact/claim IDs
business-planning-pattern rows resolve to planning signals
controlled vocabulary terms exist or are candidate
pattern promotion thresholds are enforced
principle promotion thresholds are enforced
no accepted principle lacks counterexample review
```

### Add CI

Create or finalize:

```text
.github/workflows/validate.yml
```

Recommended CI behavior:

```text
run on pull_request
run on push to main
use read-only permissions where possible
run tools/validate_repository.py
fail on validation errors
```

### Acceptance Criteria

- Validator exits nonzero on validation failure.
- Error messages identify exact file and object where possible.
- CI runs validation on pull requests or pushes to `main`.
- No auto-repair until validation is trusted.
- Validator documentation exists.

---

## Phase 11 — Mature Business Intelligence Knowledge System

### Purpose

After enough targets exist, shift from scaffolding to cross-target business insight.

### Work Items

Create mature synthesis artifacts:

```text
knowledge/patterns/business-planning-patterns.md
knowledge/patterns/capital-allocation-patterns.md
knowledge/patterns/leadership-failure-patterns.md
knowledge/patterns/crisis-resilience-patterns.md
knowledge/principles/business-principles.md
knowledge/principles/capital-principles.md
knowledge/principles/leadership-principles.md
knowledge/principles/decision-making-principles.md
```

### Maturity Criteria

The repository becomes mature only when it has:

```text
10+ targets
3+ industries
3+ failure cases
3+ capital-allocation cases
3+ leadership/succession cases
3+ crisis/resilience cases
indexed planning signals
accepted patterns
counterexamples
validated indexes
source-grounded synthesis
```

### Acceptance Criteria

- Principles are rare and evidence-heavy.
- Patterns include counterexamples.
- SBA historical planning analytics produces testable claims, not generic advice.
- The repository can answer: “Which planning behaviors repeatedly appear before success, failure, resilience, or decline?”
- Validator passes.

---

## Phase Dependency Map

```text
Phase -1: Operating model
  ↓
Phase 0: Integrity repair
  ↓
Phase 1: Evidence, source quality, counterexample, and LLM governance specs
  ↓
Phase 2: Minimal validation automation
  ↓
Phase 3: SBA historical planning lens
  ↓
Phase 4: Concept spines
  ↓
Phase 5: Templates and workflows
  ↓
Phase 6: Vanderbilt model target
  ↓
Phase 7: Coverage matrix and target selection
  ↓
Phase 8: Contrasting targets
  ↓
Phase 9: Cross-target analytics and synthesis
  ↓
Phase 10: Full validation automation and CI hardening
  ↓
Phase 11: Mature business intelligence knowledge system
```

---

## Next Concrete Work Packet

The safest next packet after this file is adopted:

1. Fix `specifications/INDEX.md`.
2. Add `specifications/business-education-coverage-map.md`.
3. Add `specifications/evidence-and-source-quality-protocol.md`.
4. Add `specifications/counterexample-and-falsification-protocol.md`.
5. Add `specifications/llm-risk-and-governance-protocol.md`.
6. Add `specifications/sba-historical-planning-lens-specification.md`.
7. Update `README.md`.
8. Update `LLM_ALIGNMENT.md`.
9. Update root `INDEX.md`.
10. Update `specifications/INDEX.md` again after all new files exist.
11. Add the minimal read-only validator.

This creates governance and validation before adding bulk.

---

## Final Operating Rule

Adopt the plan in order:

```text
governance before expansion
evidence before claims
claims before lessons
lessons before patterns
patterns before principles
validation before scale
```
