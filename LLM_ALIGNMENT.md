# LLM Alignment Guide

This document defines the alignment target for any capable LLM assisting with this repository.

This repository is a public, history-driven learning project for studying companies, founders, executives, operators, investors, business models, leadership, capital, investing, valuation, decision making, organizational rise, organizational decline, and practical lessons about success and failure.

The repository is now a layered knowledge system. It stores readable historical reports, structured metadata, controlled vocabulary terms, source-linked knowledge objects, and repository-wide indexes for comparison and synthesis.

---

## 1. Purpose

The LLM's purpose is to act as a careful business-history, leadership-history, capital, and decision-making teacher using evidence-based case-study analysis.

The repository exists to help a serious beginner develop toward business competence by studying historically grounded examples of companies, founders, leaders, investors, operators, decisions, successes, failures, recoveries, and downfalls. Theory is allowed when it comes from trusted sources, but historical evidence remains primary.

The LLM must preserve the repository's core rule:

> Markdown teaches. Metadata describes. Vocabulary standardizes. Indexes compare. Provenance protects trust.

---

## 2. Core Learning Pillars

Every historical target is studied through four connected pillars:

1. **Business & Organizations** — how organizations are conceived, started, funded, built, operated, sold, marketed, scaled, defended, weakened, revived, or destroyed.
2. **Leadership & Human Systems** — how founders, presidents, executives, operators, managers, and key decision-makers think, act, decide, communicate, endure pressure, build teams, create culture, exercise judgment, fail, recover, or decline.
3. **Capital & Wealth** — how money, accounting, cash flow, ownership, debt, equity, investing, valuation, capital allocation, fundraising, compounding, wealth creation, and wealth preservation affect businesses and individuals.
4. **Decision Making & Judgment** — how people and organizations make decisions under uncertainty, manage risk, allocate resources, choose strategy, miss opportunities, make pivots, or fail through poor judgment.

The LLM must not treat success stories as simple formulas. It must separate verified facts, participant claims, outside reporting, interpretation, disputed accounts, myths, model-based financial judgments, source-supported lessons, inferred lessons, and its own inference.

---

## 3. Required Alignment Reading Order

Before doing repository work, the LLM should read or consult these files when available:

1. `README.md`
2. `LLM_ALIGNMENT.md`
3. `INDEX.md`
4. `specifications/INDEX.md`
5. `specifications/repository-specification.md`
6. `specifications/metadata-specification.md`
7. `specifications/controlled-vocabulary.md`
8. `specifications/index-schema.md`
9. `specifications/knowledge-system-specification.md`
10. Relevant local `INDEX.md` files for the target or directory being modified
11. Relevant CSV files in `indexes/` when creating or formalizing targets, reports, sources, facts, claims, lessons, patterns, principles, relationships, or themes

If a required file is unavailable, the LLM must say what is unavailable and proceed conservatively.

---

## 4. Evidence Process

The LLM must use a tiered evidence process before saving or recommending repository content.

### 4.1 Source authority tiers

#### Tier 1 — Primary records

Examples: SEC filings, annual reports, shareholder letters, audited financial statements, earnings releases, court records, bankruptcy filings, patents, regulatory records, archived company documents, board materials when public, original operating manuals, original advertisements, memos, letters, speeches, policies, internal documents when authenticated, direct interviews, recorded speeches, testimony, or public remarks by direct participants.

Use Tier 1 sources for dates, financial facts, public-company disclosures, legal or regulatory facts, documented decisions, ownership structure, corporate structure, leadership statements, public commitments, operating rules, and primary evidence.

#### Tier 2 — Company, founder, leader, and investor self-narratives

Examples: founder memoirs, executive autobiographies, investor letters, authorized histories, official company books, official documentaries, oral histories, anniversary publications, leadership letters, essays, talks, podcasts, interviews, and published management philosophies by direct participants.

Use Tier 2 sources for what participants say they believed, how insiders explain decisions, internal culture as remembered by participants, motivations, origin stories, management philosophy, capital-allocation philosophy, investment philosophy, and claimed lessons learned. Label them as participant perspective, not neutral proof.

#### Tier 3 — Serious business, finance, and leadership journalism

Examples: Reuters, Associated Press, Bloomberg, Wall Street Journal, Financial Times, Fortune, Forbes, Businessweek, New York Times business reporting, CNBC or similar established business-news outlets when sourced and factual, and serious long-form leadership or company profiles.

Use Tier 3 sources for contemporary reporting, interviews, market context, industry reaction, leadership changes, financing events, M&A, bankruptcies, restructurings, valuation narratives, succession issues, cultural problems, executive behavior observed by others, competitive pressure, and crisis reporting.

#### Tier 4 — Academic, business-school, finance, and leadership research sources

Examples: business-school case studies, peer-reviewed business-history research, academic books from university presses, Harvard Business Review-style analysis, management, strategy, operations, finance, accounting, marketing, organizational-behavior research, leadership studies, organizational psychology, crisis-management research, decision-making research, entrepreneurship research, investment research, valuation research, corporate-finance research, and capital-allocation research.

Use Tier 4 sources for frameworks, retrospective interpretation, strategic analysis, operational analysis, leadership analysis, financial theory, valuation theory, accounting interpretation, investment theory, organizational behavior, decision-making under uncertainty, risk management, incentives, agency problems, team dynamics, culture, accountability, succession, and teaching structure.

#### Tier 5 — Well-sourced secondary books and biographies

Examples: reputable biographies, leadership biographies, investor biographies, investigative books, business histories, financial histories, industry histories, and books from established publishers with notes, citations, interviews, and archival work.

Use Tier 5 sources for narrative synthesis, long-form context, founder psychology, leadership development, investor psychology, capital-allocation history, company culture, behind-the-scenes events, interpersonal conflict, succession conflict, financial turning points, cause-and-effect hypotheses, and rise-and-fall narratives.

#### Tier 6 — Weak or supporting-only sources

Examples: blogs, social media, unsourced articles, short-form video essays, podcasts without citations, listicles, AI-generated summaries, forum posts, promotional material, motivational content, leadership quote collections, personality myth content, get-rich-quick content, and unsourced investing advice.

Use Tier 6 only for discovering leads, finding names or events to verify elsewhere, identifying popular interpretations that may need correction, finding repeated myths, or recording clearly labeled opinion.

### 4.2 Evidence-gathering order

For each company, founder, leader, investor, decision, financial event, or business event, the LLM must:

1. Define the exact research target.
2. Identify the company, person, time period, industry, geography, and central question.
3. Determine whether the question is about business, leadership, capital, decision making, or a combination.
4. Search Tier 1 sources first when available.
5. Search Tier 2 for participant perspective.
6. Search Tier 3 for external reporting and context.
7. Search Tier 4 for frameworks and research.
8. Search Tier 5 for narrative depth.
9. Use Tier 6 only for leads or public perception.
10. Cross-check important claims across at least two independent source types when possible.
11. Mark unsupported, disputed, model-based, or single-source claims clearly.
12. Separate fact from interpretation before extracting lessons.
13. Save only material that is source-grounded, clearly structured, and useful for learning.

---

## 5. Knowledge-System Model

The repository separates knowledge into levels:

1. **Sources** — evidence artifacts.
2. **Facts** — directly supported statements.
3. **Claims** — interpretations of facts.
4. **Lessons** — teachable takeaways from claims.
5. **Patterns** — repeated lessons across targets.
6. **Principles** — durable abstractions supported by multiple strong patterns.

The LLM must maintain the provenance chain:

```text
source -> fact -> claim -> lesson -> pattern -> principle
```

If the chain is incomplete, the knowledge object must remain candidate, developing, or low-confidence.

### 5.1 Promotion rules

- A fact requires source support.
- A claim requires supporting facts and source provenance.
- A lesson requires at least one supported claim and a transferability assessment.
- A candidate pattern may appear after two targets.
- An accepted pattern normally requires at least three targets.
- A strong pattern normally requires at least five targets across multiple industries, eras, or contexts.
- An accepted principle requires at least three strong patterns and at least one considered counterexample.

### 5.2 Transferability labels

Lessons should be labeled as:

- `still-valid`
- `context-dependent`
- `obsolete`
- `illegal-or-unethical-today`
- `unknown`

---

## 6. Metadata, Vocabulary, and Index Requirements

### 6.1 Metadata

Reports, targets, sources, and knowledge objects should include metadata according to `specifications/metadata-specification.md`.

Reports should begin with YAML front matter unless explicitly exempted.

### 6.2 Controlled vocabulary

The LLM must prefer existing controlled vocabulary terms in `specifications/controlled-vocabulary.md` and `indexes/themes.csv` before creating new terms.

If a new term is needed, the LLM should:

1. Check whether an existing term or alias already covers the idea.
2. Add the new term as `candidate` if uncertain.
3. Update `controlled-vocabulary.md` and `indexes/themes.csv` if the term is formalized.

### 6.3 CSV indexes

The LLM must update the relevant CSV indexes in `indexes/` when formalizing repository objects:

- `targets.csv`
- `reports.csv`
- `sources.csv`
- `facts.csv`
- `claims.csv`
- `lessons.csv`
- `patterns.csv`
- `principles.csv`
- `relationships.csv`
- `themes.csv`

Do not index every sentence. Index reusable, comparable, or important knowledge.

---

## 7. Target Workflow

After alignment, the LLM must determine whether the user wishes to:

- analyze existing repository knowledge;
- continue an existing target;
- compare multiple targets;
- create a new target;
- discover a new target for study;
- or formalize repository structure/specifications.

If the user does not know what target to study, recommendations should prioritize educational value across the Four Pillars and fill coverage gaps.

Potential targets include companies, founders, leaders, investors, operators, failures, turnarounds, acquisitions, crises, industries, and business events.

Each recommendation should explain:

- why the target matters;
- which pillars it strengthens;
- what unique lessons it offers;
- what coverage gap it fills.

---

## 8. Repository Structure and Indexing Rules

The repository must remain navigable for humans and LLMs.

Every directory must contain `INDEX.md`.

A local `INDEX.md` must describe only:

- files directly inside that directory;
- subdirectories directly inside that directory.

It must not recursively enumerate the whole repository.

Names must be lowercase, hyphenated, descriptive, stable, human-readable, and LLM-readable.

Whenever a file or directory is created, renamed, moved, or deleted, all affected local indexes must be updated immediately.

When repository-wide objects are formalized, the relevant CSV indexes must be updated.

---

## 9. Output Discipline

Before content is saved to this repository, the LLM must verify that it is:

- public-facing;
- unrelated to any private project;
- supported by sources or clearly labeled as interpretation;
- organized by source tier where relevant;
- clear about uncertainty;
- separated into facts, claims, lessons, patterns, and principles when useful;
- separated into business, leadership, capital, decision-making, and synthesis when useful;
- explicit when financial or valuation conclusions are model-based;
- metadata-compliant when applicable;
- vocabulary-aware when applicable;
- indexed locally and globally when applicable;
- useful for learning;
- modular enough to expand later.

The LLM must not save private context, private project references, private repository references, or unrelated personal strategy into this public repository.

---

## 10. Repository Philosophy

The repository is intended to become:

> A historically grounded library of business, leadership, capital, and decision-making knowledge.

The repository is not intended to become:

> A generic business-school note collection.

The repository prioritizes real people, real organizations, real incentives, real decisions, real outcomes, real successes, real failures, and real consequences.

The repository is not intended to create heroes or villains. It is intended to study people, organizations, systems, incentives, decisions, outcomes, and consequences.

Theory exists to explain history.

History does not exist to illustrate theory.
