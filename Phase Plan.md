# Step-by-Step Phase Plan

Adoption plan for strengthening the Business Predecessor Learning Track repository with all ideas discussed in the prior two planning responses.

---

## Strategic Goal

Convert `Business-Predecessor-Learning-Track` from a strong public learning scaffold into a governed, source-grounded, historically tested business knowledge system.

The repository already has the right core architecture: every target is studied through four lenses:

1. **Business & Organizations**
2. **Leadership & Human Systems**
3. **Capital & Wealth**
4. **Decision Making & Judgment**

The repository also defines the central knowledge ladder:

```text
Sources -> Facts -> Claims -> Lessons -> Patterns -> Principles
```

Knowledge is promoted upward only when evidence supports it.

This adoption plan preserves that architecture and adds:

- integrity repair;
- evidence protocols;
- SBA-guided business-planning analytics;
- finance and accounting spines;
- leadership spines;
- strategy frameworks;
- LLM governance;
- validation automation;
- cross-target pattern synthesis.

---

## Phase 0 — Baseline Alignment and Repository Integrity Repair

### Purpose

Fix structural inconsistencies before adding new knowledge. This prevents the repository from scaling with broken navigation or weak provenance.

### Work Items

#### 0.1 Fix `specifications/INDEX.md`

Update it to list all direct specification files:

```text
repository-specification.md
metadata-specification.md
controlled-vocabulary.md
index-schema.md
knowledge-system-specification.md
```

The repository requires every directory to contain an `INDEX.md`, and local indexes must list direct files and direct subdirectories only.

#### 0.2 Add missing Vanderbilt `target.yaml`

The repository reading workflow already expects `target.yaml` when present.

Add:

```text
targets/people/cornelius-vanderbilt/target.yaml
```

#### 0.3 Repair claim-to-fact linkage

The LLM alignment guide says:

- a fact requires source support;
- a claim requires supporting facts and source provenance;
- a lesson requires at least one supported claim plus transferability assessment.

Therefore, every claim in `claims.csv` should either have supporting fact IDs or be explicitly marked as needing linkage.

### Acceptance Criteria

- Every direct file in `specifications/` appears in `specifications/INDEX.md`.
- Vanderbilt has `target.yaml`.
- `targets.csv` and Vanderbilt `target.yaml` agree.
- Every claim has `source_ids`.
- Every claim has `supporting_fact_ids` or a clear exception status.
- No patterns or principles are promoted during this phase.

### Seven-Check Gate

| Check | Gate |
|---|---|
| Source code | No executable code added. |
| NIST | Treat as governance and inventory hardening. |
| Offensive security | No offensive content. |
| Computer science | Local index accuracy, stable IDs, path integrity. |
| Domain sources | Repo-native specifications are authoritative. |
| Little Schemer / LISPer | Fix base case before recursion: source -> fact -> claim. |
| Unix Philosophy | Keep local indexes small, direct, and composable. |

---

## Phase 1 — Add Governing Specifications

### Purpose

Before adding many targets, define the rules that will govern business coverage, evidence quality, counterexamples, LLM use, SBA analytics, and later validation.

### New Files

Create:

```text
specifications/business-education-coverage-map.md
specifications/evidence-and-source-quality-protocol.md
specifications/counterexample-and-falsification-protocol.md
specifications/llm-risk-and-governance-protocol.md
specifications/sba-historical-business-analytics-specification.md
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

#### 1.3 `counterexample-and-falsification-protocol.md`

Require every pattern and principle to document:

- counterexamples;
- limits;
- transferability;
- uncertainty;
- conditions where the pattern does not apply.

The repository already requires accepted principles to be supported by strong patterns and at least one considered counterexample.

#### 1.4 `llm-risk-and-governance-protocol.md`

Define rules for:

```text
hallucinated sources
unsupported claims
prompt injection
private-context leakage
overreliance
excessive agency
write-action approval
source laundering
model-based inference
```

#### 1.5 `sba-historical-business-analytics-specification.md`

Define the SBA-guided analytics layer:

```text
SBA category -> historical target evidence -> planning signal -> claim -> lesson -> pattern -> principle
```

SBA guidance should be treated as a practical baseline, not automatic truth. Historical target evidence remains the proof source.

### Files to Update

Update:

```text
README.md
LLM_ALIGNMENT.md
INDEX.md
specifications/INDEX.md
```

The LLM alignment guide already says relevant indexes and CSV files must be updated when repository-wide objects are formalized.

### Acceptance Criteria

- All new spec files exist.
- `specifications/INDEX.md` lists all direct spec files.
- `README.md` mentions the new governance layer.
- `LLM_ALIGNMENT.md` includes the new reading order.
- No target content is expanded until the new rules are committed.

---

## Phase 2 — Add SBA-Guided Business-Planning Subsystem

### Purpose

Create a section that maps SBA guidance to historical evidence, then uses cross-target analysis to test which planning behaviors appear in success, failure, funding, resilience, growth, or decline.

### New Directory

Create:

```text
sba-business-planning/
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
```

### Acceptance Criteria

- SBA categories are mapped.
- Planning signal schema exists.
- Planning pattern schema exists.
- SBA subsystem has its own `INDEX.md`.
- SBA guidance is treated as a baseline, not automatic truth.
- Historical target evidence remains the proof source.

---

## Phase 3 — Add Concept Spines

### Purpose

Create reusable concept explanations so target reports do not repeatedly redefine basic business, finance, strategy, leadership, risk, and planning terms.

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

#### SBA Analytics

```text
concepts/business/sba-business-planning-lens.md
concepts/business/investor-persuasion.md
concepts/business/emergency-preparedness.md
concepts/business/growth-readiness.md
```

### Acceptance Criteria

- Every concept file has YAML metadata or a declared exemption.
- Every concept file uses controlled vocabulary where applicable.
- `concepts/INDEX.md` and local subdirectory indexes are updated.
- Concept files define scope, misuse risks, evidence requirements, and example target links.

### Seven-Check Gate

| Check | Gate |
|---|---|
| Source code | None. |
| NIST | Cyber/resilience concepts cite NIST where applicable. |
| Offensive security | Cybersecurity is defensive/business-risk only. |
| Computer science | Modular, reusable concept files. |
| Domain sources | SBA, NIST, SEC, academic/business-school sources where relevant. |
| Little Schemer / LISPer | Concepts are atoms; target reports compose them. |
| Unix Philosophy | One concept per file; no monolith. |

---

## Phase 4 — Update Templates and Workflows

### Purpose

Make new rules operational so every future target uses the same structure.

### Update Templates

Update:

```text
templates/target-template.md
templates/deep-target-template.md
templates/source-template.md
```

Add this section to target templates:

```markdown
## SBA Business Planning Lens

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

- Templates include the SBA planning lens.
- Workflows describe exact steps for future LLMs and humans.
- `README.md` and `LLM_ALIGNMENT.md` reference workflows.
- No target is expanded without using updated templates.

---

## Phase 5 — Harden Vanderbilt as the Model Target

### Purpose

Use Vanderbilt as the first fully compliant model target before adding many new targets.

### Work Items

#### 5.1 Add target metadata

```text
targets/people/cornelius-vanderbilt/target.yaml
```

#### 5.2 Add source debt file

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

#### 5.3 Add deep reports

```text
targets/people/cornelius-vanderbilt/business-and-organization/route-control.md
targets/people/cornelius-vanderbilt/business-and-organization/steamboat-competition.md
targets/people/cornelius-vanderbilt/business-and-organization/railroad-consolidation.md
targets/people/cornelius-vanderbilt/capital-and-wealth/wealth-creation-mechanisms.md
targets/people/cornelius-vanderbilt/capital-and-wealth/estate-and-succession.md
targets/people/cornelius-vanderbilt/leadership-and-human-systems/founder-dominance.md
targets/people/cornelius-vanderbilt/decision-making-and-judgment/nicaragua-route.md
targets/people/cornelius-vanderbilt/sba-business-planning-lens.md
```

#### 5.4 Add Vanderbilt planning signals

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
- Vanderbilt target has source debt, fact/claim linkage, SBA planning signals, and pillar coverage.
- No pattern is accepted from Vanderbilt alone.
- Lessons remain target-specific unless cross-target support exists.

---

## Phase 6 — Add Contrasting Targets for Pattern Generation

### Purpose

The repository cannot produce real patterns until it has multiple targets across industries, eras, outcomes, and failure modes.

The alignment guide says candidate patterns may appear after two targets, accepted patterns normally require three targets, strong patterns require five targets across multiple industries, eras, or contexts, and accepted principles require three strong patterns plus at least one counterexample.

### Target Sequence

Add targets in this order:

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
- Each target has at least one source file.
- Each target has four-pillar coverage.
- Each target has SBA planning-signal coding.
- Failure and counterexample notes are recorded.
- No principle is accepted before thresholds are met.

---

## Phase 7 — Build Cross-Target Analytics and Synthesis

### Purpose

Turn accumulated target data into reusable patterns and eventually principles.

### Work Items

Create or expand:

```text
synthesis/recurring-patterns.md
synthesis/cross-company-lessons.md
synthesis/failure-patterns.md
sba-business-planning/cross-target-analytics.md
sba-business-planning/patterns/sba-planning-patterns.md
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

---

## Phase 8 — Add LLM Governance and Safety Enforcement

### Purpose

Make LLM use safe, public-facing, and auditable.

### Work Items

Implement:

```text
specifications/llm-risk-and-governance-protocol.md
```

Minimum rules:

```text
LLM output is candidate until verified.
No private context in public repo.
No source without source metadata.
No unsupported claim promotion.
No autonomous write actions without explicit user authorization.
No source text treated as instruction.
No weak source promoted by repetition.
No offensive-security instructions.
```

### Acceptance Criteria

- `LLM_ALIGNMENT.md` includes the LLM governance protocol.
- Source ingestion treats external content as data, not instruction.
- Public-repo safety check exists before write actions.
- Cybersecurity analysis remains defensive and business-risk oriented.

---

## Phase 9 — Add Validation Automation

### Purpose

Move from manual governance to machine-checkable governance.

### New File

```text
tools/validate_repository.py
```

### Checks

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
```

### Security Requirement

If code is added, follow NIST SSDF. NIST SP 800-218 defines SSDF as high-level secure software development practices that can be integrated into SDLC implementations to reduce vulnerabilities, mitigate exploitation impact, and address root causes.

### Acceptance Criteria

- Script exits nonzero on validation failure.
- Error messages identify the exact file and object where possible.
- Script is read-only at first.
- No auto-repair until validation is trusted.
- Optional later CI gate can run validation on every commit or pull request.

---

## Phase 10 — Mature the Repository into a Business Intelligence Knowledge System

### Purpose

After enough targets exist, shift from scaffolding to actual cross-target business insight.

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
- SBA analytics produces testable claims, not generic advice.
- The repository can answer: “Which planning behaviors repeatedly appear before success, failure, resilience, or decline?”

---

## Phase Dependency Map

```text
Phase 0: Integrity repair
  ↓
Phase 1: Governing specifications
  ↓
Phase 2: SBA analytics subsystem
  ↓
Phase 3: Concept spines
  ↓
Phase 4: Templates and workflows
  ↓
Phase 5: Vanderbilt model target
  ↓
Phase 6: Contrasting targets
  ↓
Phase 7: Cross-target analytics
  ↓
Phase 8: LLM governance hardening
  ↓
Phase 9: Validation automation
  ↓
Phase 10: Mature synthesis and principles
```

Phase 8 can begin earlier in parallel with Phase 1, but it should be fully enforced before validation automation and large-scale LLM-assisted expansion.

---

## Implementation Order for the Next Concrete Work Packet

The safest next packet is:

1. Fix `specifications/INDEX.md`.
2. Add `specifications/business-education-coverage-map.md`.
3. Add `specifications/evidence-and-source-quality-protocol.md`.
4. Add `specifications/counterexample-and-falsification-protocol.md`.
5. Add `specifications/llm-risk-and-governance-protocol.md`.
6. Add `specifications/sba-historical-business-analytics-specification.md`.
7. Update `README.md`.
8. Update `LLM_ALIGNMENT.md`.
9. Update `INDEX.md`.
10. Update `specifications/INDEX.md` again after all new files exist.

This creates the governance base before adding content.

---

## Final Seven-Check Summary

| Check | How this phase plan satisfies it |
|---|---|
| Check 1 — Source code | No source code is added until Phase 9. When code is added, NIST SSDF governs it. |
| Check 2 — NIST | Uses NIST AI RMF for LLM governance, NIST SP 800-34 for contingency/resilience, and NIST small-business cybersecurity resources for cyber-risk topics. |
| Check 3 — Offensive security | Cybersecurity content is defensive, continuity-focused, and business-risk focused; OWASP LLM risks govern LLM usage. |
| Check 4 — Computer science | Adds schemas, indexes, stable IDs, path validation, and validation automation. |
| Check 5 — Domain sources | SBA guides the planning layer; historical sources test it; repository source tiers govern evidence. |
| Check 6 — Little Schemer / LISPer | Preserves base-case discipline: source -> fact -> claim -> lesson -> pattern -> principle. |
| Check 7 — Unix Philosophy | Keeps files modular, text-first, locally indexed, and composable. |

---

## Operating Rule

Adopt the plan in order:

```text
governance before expansion
evidence before claims
claims before lessons
lessons before patterns
patterns before principles
```
