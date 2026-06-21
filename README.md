# Business Predecessor Learning Track

A public, history-driven learning repository for studying business, leadership, capital, and decision making through real companies, real people, real incentives, real failures, and real outcomes.

This repository is intended to become a structured library of historical business knowledge. It is not a generic business-school note collection, motivational quote archive, or theory-first curriculum.

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
- and what mistakes should be avoided.

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

Examples of possible targets include McDonald's, NVIDIA, Starbucks, Walmart, Apple, Amazon, Toyota, Berkshire Hathaway, Kodak, Blockbuster, Ray Kroc, Sam Walton, Howard Schultz, Warren Buffett, or other historically important organizations and people.

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

## How to use this repository

A human learner can use this repository in several ways.

### Option 1: Study an existing target

Open the target's directory and read:

1. `overview.md` or `profile.md`
2. the Four Pillar files
3. `lessons-to-copy.md`
4. `lessons-to-avoid.md`
5. `sources.md`

### Option 2: Ask an LLM to align to the repository

Start by directing the LLM to read:

```text
LLM_ALIGNMENT.md
README.md
INDEX.md
```

Then ask it to follow the repository rules.

Useful prompts:

```text
Align yourself to this repository using LLM_ALIGNMENT.md, then ask whether I want to analyze existing knowledge, continue a target, compare targets, discover a target, or create a new target.
```

```text
Recommend five historical business targets we have not studied yet. Explain which Four Pillars each one strengthens and why each target is educationally valuable.
```

```text
Create a source-grounded historical profile for McDonald's using the Four Pillars and save it according to the repository structure.
```

```text
Compare lessons from McDonald's and Starbucks. Separate business, leadership, capital, and decision-making lessons.
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

### Option 4: Build cross-target lessons

After multiple targets are studied, use the synthesis files to identify patterns across companies and people.

Examples:

- recurring success patterns;
- recurring failure patterns;
- capital-allocation lessons;
- leadership failure patterns;
- decision-making errors;
- operational excellence patterns;
- differences between companies that declined and companies that stayed dominant.

---

## Repository structure

The repository is organized as a navigable file tree.

Each directory should contain its own local `INDEX.md` file.

A local `INDEX.md` only describes the files and subdirectories directly inside that directory. It does not recursively list the entire repository.

Recommended structure:

```text
/
  README.md
  LLM_ALIGNMENT.md
  INDEX.md

  targets/
    INDEX.md

    companies/
      INDEX.md
      example-company/
        INDEX.md
        overview.md
        business-and-organization.md
        leadership-and-human-systems.md
        capital-and-wealth.md
        decision-making-and-judgment.md
        lessons-to-copy.md
        lessons-to-avoid.md
        sources.md

    people/
      INDEX.md
      example-person/
        INDEX.md
        profile.md
        companies.md
        leadership-and-human-systems.md
        capital-and-wealth.md
        decision-making-and-judgment.md
        lessons-to-copy.md
        lessons-to-avoid.md
        sources.md

    comparison-studies/
      INDEX.md

    failure-cases/
      INDEX.md

  synthesis/
    INDEX.md
    recurring-patterns.md
    cross-company-lessons.md
    failure-patterns.md
```

This structure may expand, but names should remain clear, stable, and readable by both humans and LLMs.

---

## Indexing rules

Indexes are part of the repository's navigation system.

Every directory should contain:

```text
INDEX.md
```

Each local index should list only:

- files directly inside that directory;
- subdirectories directly inside that directory;
- short descriptions of what each item is for.

Whenever a file or directory is created, renamed, moved, or deleted, the affected local indexes should be updated immediately.

The root index should not try to describe every file in the repository. It should only describe what is visible at the root.

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

When a target is selected, expanded, compared, corrected, or synthesized, the repository should be updated in the proper location, with sources and local indexes maintained.

The repository should become more useful over time instead of repeatedly rediscovering the same information.
