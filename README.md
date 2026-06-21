# Business Predecessor Learning Track

A public, history-driven learning repository for studying business, leadership, capital, and decision making through real companies, real people, real incentives, real failures, and real outcomes.

This repository is intended to become a structured historical business-learning knowledge system. It is not a generic business-school note collection, motivational quote archive, hero-worship project, villain-making project, or theory-first curriculum.

Theory is allowed when it helps explain history. History is not used merely to decorate theory.

---

## What this repository is for

This repository helps learners study how businesses and businesspeople actually developed over time.

The goal is to understand:

- how companies began;
- how founders moved from idea to execution;
- how businesses were funded, operated, scaled, defended, weakened, revived, or destroyed;
- how leaders made decisions under uncertainty;
- how capital, ownership, cash flow, valuation, debt, equity, reinvestment, and incentives shaped outcomes;
- how success was built;
- how decline happened;
- what warning signs appeared;
- what lessons are worth copying;
- what mistakes should be avoided;
- and which lessons become recurring patterns or durable principles after comparison across targets.

The repository is built around historical targets, such as:

- companies;
- founders;
- executives;
- investors;
- operators;
- industries;
- failures;
- turnarounds;
- acquisitions;
- crises;
- or comparison studies.

Examples of possible targets include Cornelius Vanderbilt, John D. Rockefeller, Andrew Carnegie, J. P. Morgan, McDonald's, NVIDIA, Starbucks, Walmart, Apple, Amazon, Toyota, Berkshire Hathaway, Kodak, Blockbuster, Ray Kroc, Sam Walton, Howard Schultz, Warren Buffett, or other historically important organizations and people.

A learner does not need to already know which target to study. One purpose of this repository is to help identify strong historical targets that teach useful lessons.

---

## The Four Pillars

Every target is studied through four connected lenses.

### 1. Business & Organizations

How the organization was conceived, started, funded, built, sold, marketed, operated, scaled, defended, weakened, revived, or destroyed.

This includes business models, products, customers, distribution, operations, competition, market timing, scaling, category dominance, and decline.

### 2. Leadership & Human Systems

How founders, executives, operators, managers, investors, and key decision-makers thought, acted, communicated, built teams, handled pressure, created culture, enforced standards, failed, recovered, or declined.

This includes leadership style, decision rights, incentives, delegation, conflict, accountability, succession, ethics, and culture.

### 3. Capital & Wealth

How money moved into, through, and out of the business.

This includes funding, ownership, equity, debt, cash flow, reinvestment, capital allocation, valuation, dilution, compounding, wealth creation, wealth loss, solvency, and preservation.

This repository is educational and historical. It is not investment advice.

### 4. Decision Making & Judgment

How people and organizations made decisions under uncertainty.

This includes risk, timing, opportunity cost, incentives, assumptions, alternatives, pivots, missed opportunities, crisis decisions, overconfidence, ignored evidence, feedback loops, and hindsight.

---

## Knowledge-system model

The repository is not only a set of reports. It is a layered knowledge system.

```text
Sources -> Facts -> Claims -> Lessons -> Patterns -> Principles
```

| Level | Meaning | Example |
|---|---|---|
| Sources | Evidence artifacts | A biography, filing, court record, interview, report, or archival document |
| Facts | Directly supported statements | Vanderbilt died in 1877 |
| Claims | Interpretations of facts | Vanderbilt's advantage appears partly tied to infrastructure control |
| Lessons | Teachable takeaways | Study bottlenecks because they may reveal where business power concentrates |
| Patterns | Repeated lessons across targets | Infrastructure control appears across several major business builders |
| Principles | Durable abstractions supported by multiple strong patterns | Control over movement, access, or distribution can create durable advantage when paired with discipline and capital control |

Knowledge is promoted upward only when evidence supports it.

---

## How to use this repository

A human learner can use this repository in several ways.

### Option 1: Study an existing target

Open the target's directory and read:

1. `INDEX.md`
2. `target.yaml` when present
3. `profile.md`
4. `timeline.md`
5. `historical-context.md`
6. the Four Pillar reports and subdirectories
7. `lessons/`
8. `sources/`

### Option 2: Ask an LLM to align to the repository

Start by directing the LLM to read:

```text
README.md
LLM_ALIGNMENT.md
INDEX.md
specifications/INDEX.md
specifications/repository-specification.md
specifications/metadata-specification.md
specifications/controlled-vocabulary.md
specifications/index-schema.md
specifications/knowledge-system-specification.md
```

Then ask it to follow the repository rules.

Useful prompts:

```text
Align yourself to this repository using LLM_ALIGNMENT.md and the specifications, then ask whether I want to analyze existing knowledge, continue a target, compare targets, discover a target, or create a new target.
```

```text
Recommend five historical business targets we have not studied yet. Explain which Four Pillars each one strengthens and why each target is educationally valuable.
```

```text
Create a source-grounded historical profile for McDonald's using the Four Pillars, metadata, source tracking, and indexes required by the repository specifications.
```

```text
Compare lessons from Vanderbilt, Rockefeller, and Carnegie. Separate facts, claims, lessons, candidate patterns, and possible principles.
```

### Option 3: Discover a new target

If you do not know what to study, ask for recommendations.

The repository should prefer targets that fill educational gaps, such as:

- underrepresented industries;
- failures instead of only successes;
- international companies instead of only American companies;
- older business history instead of only modern technology;
- capital-allocation cases instead of only leadership stories;
- small-company or founder-led cases when sources allow;
- turnarounds, collapses, and recoveries.

### Option 4: Build cross-target knowledge

After multiple targets are studied, use the indexes and synthesis files to identify patterns across companies and people.

Examples:

- recurring success patterns;
- recurring failure patterns;
- capital-allocation lessons;
- leadership failure patterns;
- decision-making errors;
- operational excellence patterns;
- differences between companies that declined and companies that stayed dominant;
- candidate principles supported by repeated patterns.

---

## Repository structure

The repository is organized as a navigable file tree plus machine-readable indexes.

Each directory should contain its own local `INDEX.md` file.

A local `INDEX.md` only describes the files and subdirectories directly inside that directory. It does not recursively list the entire repository.

Current top-level structure:

```text
/
  README.md
  LLM_ALIGNMENT.md
  INDEX.md

  specifications/
    INDEX.md
    repository-specification.md
    metadata-specification.md
    controlled-vocabulary.md
    index-schema.md
    knowledge-system-specification.md

  indexes/
    INDEX.md
    targets.csv
    reports.csv
    sources.csv
    facts.csv
    claims.csv
    lessons.csv
    patterns.csv
    principles.csv
    relationships.csv
    themes.csv

  targets/
    INDEX.md
    companies/
    people/
    comparison-studies/
    failure-cases/

  concepts/
    INDEX.md
    business/
    leadership/
    capital/
    decision-making/

  knowledge/
    INDEX.md
    facts/
    claims/
    lessons/
    patterns/
    principles/

  synthesis/
    INDEX.md

  templates/
    INDEX.md
```

---

## Specifications

The specifications are governing documents.

- `specifications/repository-specification.md` — structure, navigation, target layout, expansion, and integrity rules.
- `specifications/metadata-specification.md` — YAML metadata requirements for reports, targets, sources, and knowledge objects.
- `specifications/controlled-vocabulary.md` — approved terms for themes and concepts.
- `specifications/index-schema.md` — CSV schemas for repository-wide indexes.
- `specifications/knowledge-system-specification.md` — rules for sources, facts, claims, lessons, patterns, and principles.

---

## Indexing rules

Indexes are part of the repository's navigation and comparison system.

Every directory should contain:

```text
INDEX.md
```

Each local index should list only:

- files directly inside that directory;
- subdirectories directly inside that directory;
- short descriptions of what each item is for.

Repository-wide CSV indexes live in `indexes/` and make cross-target comparison possible.

Whenever a file or directory is created, renamed, moved, or deleted, the affected local indexes should be updated immediately.

Whenever a target, report, source, fact, claim, lesson, pattern, principle, relationship, or theme is formalized, the relevant CSV index should be updated.

---

## Source standards

Repository content should be source-grounded.

The preferred source order is:

1. Primary records such as filings, annual reports, audited financial statements, court records, patents, direct interviews, speeches, testimony, and archived company materials.
2. Company, founder, leader, and investor self-narratives, clearly labeled as participant perspective.
3. Serious business, finance, and leadership journalism.
4. Academic, business-school, finance, strategy, leadership, and decision-making research.
5. Well-sourced secondary books and biographies.
6. Weak or supporting-only sources, used only for leads, public perception, or opinion.

Important claims should separate:

- fact;
- self-narrative;
- reporting;
- interpretation;
- model-based financial judgment;
- disputed claims;
- uncertainty;
- and open questions.

---

## What this repository is not

This repository is not:

- investment advice;
- a motivational content archive;
- a hero-worship project;
- a villain-making project;
- a generic management course;
- a list of business quotes;
- or a theory-first curriculum.

It is intended to study people, organizations, systems, incentives, decisions, outcomes, successes, failures, and consequences.

---

## Working rule

When learning happens, preserve it.

When a target is selected, expanded, compared, corrected, or synthesized, the repository should be updated in the proper location, with sources, metadata, controlled vocabulary, local indexes, and CSV indexes maintained.

The repository should become more useful over time instead of repeatedly rediscovering the same information.
