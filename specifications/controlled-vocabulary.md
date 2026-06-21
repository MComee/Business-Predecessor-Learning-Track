# Controlled Vocabulary

## 1. Purpose

This file defines controlled vocabulary terms for recurring concepts in the repository.

Controlled vocabulary prevents drift between similar phrases such as `route-control`, `chokepoint-control`, and `infrastructure-control`.

## 2. Term Format

Terms should use this format:

```yaml
id: theme:<preferred-label>
preferred_label: <preferred-label>
alternative_labels:
  - <alternate-label>
broader:
  - <theme-id>
narrower:
  - <theme-id>
related:
  - <theme-id>
definition: <clear definition>
status: <candidate | accepted | retired>
```

## 3. Initial Theme Terms

### theme:infrastructure-control

```yaml
id: theme:infrastructure-control
preferred_label: infrastructure-control
alternative_labels:
  - chokepoint-control
  - route-control
  - infrastructure-bottleneck
broader:
  - theme:competitive-advantage
related:
  - theme:distribution-control
  - theme:monopoly-power
  - theme:network-control
definition: Control over physical or institutional infrastructure that affects access, cost, movement, or market participation.
status: accepted
```

### theme:capital-allocation

```yaml
id: theme:capital-allocation
preferred_label: capital-allocation
alternative_labels:
  - reinvestment
  - capital-deployment
broader:
  - theme:capital-and-wealth
related:
  - theme:wealth-creation
  - theme:ownership-control
definition: Decisions about how money, assets, profits, credit, or investment capacity are deployed.
status: accepted
```

### theme:wealth-creation

```yaml
id: theme:wealth-creation
preferred_label: wealth-creation
alternative_labels:
  - value-creation
  - fortune-building
broader:
  - theme:capital-and-wealth
related:
  - theme:capital-allocation
  - theme:ownership-control
definition: The mechanisms by which economic value is produced, captured, compounded, or converted into durable wealth.
status: accepted
```

### theme:ownership-control

```yaml
id: theme:ownership-control
preferred_label: ownership-control
alternative_labels:
  - control-rights
  - asset-control
broader:
  - theme:capital-and-wealth
related:
  - theme:capital-allocation
  - theme:infrastructure-control
definition: The use of ownership, voting power, asset rights, or practical control to direct economic outcomes.
status: accepted
```

### theme:founder-dependence

```yaml
id: theme:founder-dependence
preferred_label: founder-dependence
alternative_labels:
  - key-person-risk
  - founder-centralization
broader:
  - theme:leadership-and-human-systems
related:
  - theme:succession-risk
  - theme:institutional-durability
definition: A condition where an organization or fortune depends heavily on one founder's judgment, authority, reputation, or relationships.
status: accepted
```

### theme:succession-risk

```yaml
id: theme:succession-risk
preferred_label: succession-risk
alternative_labels:
  - inheritance-risk
  - transition-risk
broader:
  - theme:leadership-and-human-systems
related:
  - theme:founder-dependence
  - theme:wealth-preservation
definition: Risk created when leadership, ownership, authority, or wealth must transfer from one generation or leader to another.
status: accepted
```

### theme:price-war

```yaml
id: theme:price-war
preferred_label: price-war
alternative_labels:
  - fare-war
  - rate-war
broader:
  - theme:competition
related:
  - theme:cost-advantage
  - theme:market-pressure
definition: Aggressive price competition intended to gain customers, pressure rivals, reshape markets, or force negotiation.
status: accepted
```

### theme:cost-advantage

```yaml
id: theme:cost-advantage
preferred_label: cost-advantage
alternative_labels:
  - low-cost-position
broader:
  - theme:competitive-advantage
related:
  - theme:price-war
  - theme:operational-efficiency
definition: A durable ability to produce or deliver at lower cost than rivals.
status: accepted
```

### theme:operational-efficiency

```yaml
id: theme:operational-efficiency
preferred_label: operational-efficiency
alternative_labels:
  - operating-discipline
  - process-efficiency
broader:
  - theme:business-and-organization
related:
  - theme:cost-advantage
  - theme:scale
definition: The ability to produce, deliver, or operate with less waste, lower cost, greater reliability, or higher throughput.
status: accepted
```

### theme:strategic-pivot

```yaml
id: theme:strategic-pivot
preferred_label: strategic-pivot
alternative_labels:
  - business-pivot
  - capability-transfer
broader:
  - theme:decision-making-and-judgment
related:
  - theme:capital-allocation
  - theme:technology-transition
definition: A major shift from one market, technology, business model, or asset base into another.
status: accepted
```

## 4. Vocabulary Rules

- Prefer existing terms before creating new terms.
- Add aliases instead of inventing duplicates.
- Mark unclear terms as `candidate`.
- Retire terms rather than deleting them when they become obsolete.
- Use controlled terms in metadata, indexes, and knowledge objects.
