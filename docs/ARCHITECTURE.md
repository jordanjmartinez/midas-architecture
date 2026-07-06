# MIDAS Architecture

## Purpose

ARCHITECTURE.md explains how MIDAS is organized.

It is the system map for the MIDAS profile.

It should help the user, future agents, and command builders understand:

- Where different kinds of instructions belong
- How global rules connect to command skills
- How templates, evals, schemas, docs, and artifacts fit together
- How to build new commands without duplicating rules
- How to keep MIDAS modular, maintainable, and testable

ARCHITECTURE.md is not a command skill.

ARCHITECTURE.md is not a runtime rulebook.

ARCHITECTURE.md should not duplicate the full contents of global rule files.

---

# Core Architecture Principle

MIDAS uses a layered architecture.

Each layer has one job.

```md
SOUL.md       = identity
AGENTS.md     = maintainer / agent onboarding guide
rules/        = shared runtime standards
skills/       = command-specific workflows
docs/         = architecture and planning documents
templates/    = reusable command-building scaffolds
evals/        = regression tests and golden examples
schemas/      = shared data/artifact structures
workspace/    = generated research artifacts
```

The goal is to prevent command spaghetti.

Global behavior should live in `rules/`.

Command behavior should live in `skills/`.

Generated research should live in `workspace/`.

Reusable design helpers should live in `templates/`, `evals/`, `schemas/`, and `docs/`.

---

# High-Level Folder Map

Recommended MIDAS profile structure:

```bash
/home/jordan/.hermes/profiles/midas/
├── SOUL.md
├── AGENTS.md
├── rules/
│   ├── GLOBAL.md
│   ├── SOURCES.md
│   ├── CLASSIFICATIONS.md
│   ├── SCORING.md
│   ├── METRICS.md
│   ├── OUTPUT.md
│   └── ARTIFACTS.md
├── docs/
│   ├── ARCHITECTURE.md
│   ├── BUILD_ORDER.md
│   └── COMMAND_REGISTRY.md
├── templates/
│   ├── COMMAND_SKILL_TEMPLATE.md
│   ├── COMMAND_OUTPUT_TEMPLATE.md
│   └── COMMAND_EVAL_TEMPLATE.md
├── evals/
│   ├── README.md
│   ├── gems.eval.md
│   ├── track.eval.md
│   ├── research.eval.md
│   └── full.eval.md
├── schemas/
│   ├── research_artifact.schema.md
│   ├── watchlist.schema.md
│   ├── scorecard.schema.md
│   └── command_output.schema.md
├── skills/
│   └── stock-analysis/
│       ├── gems/
│       ├── track/
│       ├── research/
│       ├── financials/
│       ├── thesis/
│       ├── risk/
│       ├── full/
│       ├── earnings/
│       └── updates/
└── workspace/
    ├── tickers/
    ├── watchlists/
    ├── trackers/
    └── reports/
```

Not every folder needs to be fully built immediately.

The architecture should grow as MIDAS grows.

---

# Layer 1 — Identity Layer

## File

```bash
SOUL.md
```

## Purpose

SOUL.md defines who MIDAS is.

It should capture:

- Mission
- Identity
- Tone
- Research philosophy
- High-level guardrail spirit
- Relationship to global rules and skills

SOUL.md should be concise.

It should not duplicate detailed source, scoring, metric, output, or command rules.

---

# Layer 2 — Maintainer / Agent Onboarding Layer

## File

```bash
AGENTS.md
```

## Purpose

AGENTS.md tells future AI agents, coding agents, or maintainers how to work on MIDAS safely.

It is an onboarding guide.

It is not the runtime constitution.

It should answer:

- What files should be read first?
- Where do shared rules live?
- Where do command workflows live?
- How should new commands be built?
- What should not be duplicated?
- How should files be edited safely?

AGENTS.md should point to the rules, not restate them.

---

# Layer 3 — Global Rules Layer

## Folder

```bash
rules/
```

## Purpose

The `rules/` folder defines shared MIDAS-wide standards.

These rules apply across multiple commands.

They should not contain command-specific workflows.

## Current Rule Files

### `rules/GLOBAL.md`

Master operating policy.

Defines core behavior, rule precedence, agent operating loop, guardrails, risk discipline, no copy-trading rules, tool discipline, file/artifact discipline, and uncertainty behavior.

### `rules/SOURCES.md`

Evidence and source policy.

Defines source hierarchy, filing-first rules, claim-to-source mapping, freshness rules, conflict rules, social/crowding limits, tracker-source behavior, and source display principles.

### `rules/CLASSIFICATIONS.md`

Setup classification policy.

Defines primary setup classifications, optional modifiers, when classifications should be used, and how classifications relate to scoring and source quality.

### `rules/SCORING.md`

Scoring architecture.

Defines Global Research Score, overlay scores, evidence confidence, score caps, and relationship between scores and classifications.

### `rules/METRICS.md`

Financial metric standards.

Defines formulas, period conventions, GAAP vs non-GAAP discipline, valuation multiple rules, sector-specific metrics, red flags, and metric quality grades.

### `rules/OUTPUT.md`

Shared output standards.

Defines output modes, formatting standards, classification display, score display, evidence confidence display, source notes, as-of dates, risk display, and failure output.

### `rules/ARTIFACTS.md`

Artifact standards.

ARTIFACTS.md — artifact paths, save/update/append/replace behavior, workspace organization, and reference-folder policy.

## Rule Layer Boundary

Global rules should define shared standards.

They should not define full command workflows.

Example:

Good global rule:

```md
Use Setup Classification when a command evaluates a stock.
```

Bad global rule:

```md
When the user types !gems, first gather candidates, then rank them, then write the report.
```

That belongs in the `!gems` skill.

---

# Layer 4 — Command Skills Layer

## Folder

```bash
skills/
```

## Purpose

The `skills/` folder contains command-specific workflows.

Each command should have its own skill folder when possible.

A command skill should define:

- Trigger syntax
- Aliases
- Required inputs
- Optional inputs
- Workflow steps
- Source/tool needs
- Output requirements
- Artifact behavior
- Failure behavior
- Relevant global rule references

## Recommended Skill Structure

Example:

```bash
skills/stock-analysis/gems/
├── SKILL.md
└── OUTPUT.md
```

Optional later:

```bash
skills/stock-analysis/gems/
├── SKILL.md
├── OUTPUT.md
├── EXAMPLES.md
└── NOTES.md
```

## Skill Files

### `SKILL.md`

Defines what the command does.

Should include:

- Purpose
- When to use
- Inputs
- Workflow
- Sources/tools
- Scoring/classification use
- Artifact behavior
- Failure behavior

### `OUTPUT.md`

Defines the command-specific output format.

Should reference global `rules/OUTPUT.md` instead of duplicating it.

Command-specific output templates may live here.

## Skill Boundary

Skills should not duplicate global rules.

Instead, skills should reference global rules.

Good skill instruction:

```md
Use Setup Classification from `/home/jordan/.hermes/profiles/midas/rules/CLASSIFICATIONS.md`.
```

Bad skill instruction:

```md
Paste all setup classification definitions here again.
```

Duplicate rules create drift.

---

# Layer 5 — Docs Layer

## Folder

```bash
docs/
```

## Purpose

The `docs/` folder stores design documents, maps, registries, and planning files.

Docs are for understanding and maintaining MIDAS.

Docs are not runtime rules unless explicitly referenced by a rule or skill.

## Recommended Docs

### `docs/ARCHITECTURE.md`

System map.

Explains how MIDAS is organized.

### `docs/BUILD_ORDER.md`

Optional build plan.

Can track:

- What global files are complete
- What templates are complete
- What skills need refactoring
- What evals need building
- What commands are stable

### `docs/COMMAND_REGISTRY.md`

Optional command index.

Can list command name, aliases, purpose, skill folder, output type, artifact behavior, and status.

Docs should not become command logic.

---

# Layer 6 — Templates Layer

## Folder

```bash
templates/
```

## Purpose

Templates standardize how new commands, outputs, and evals are created.

Templates reduce drift and make commands easier to build and review.

Recommended templates:

```bash
templates/
├── COMMAND_SKILL_TEMPLATE.md
├── COMMAND_OUTPUT_TEMPLATE.md
└── COMMAND_EVAL_TEMPLATE.md
```

When creating or refactoring a command:

1. Start from `COMMAND_SKILL_TEMPLATE.md`.
2. Define the command purpose.
3. Add trigger syntax and aliases.
4. Add workflow steps.
5. Reference relevant global rules.
6. Define artifact behavior.
7. Define failure behavior.
8. Create command evals.

---

# Layer 7 — Evals Layer

## Folder

```bash
evals/
```

## Purpose

Evals are regression tests and golden examples.

They help ensure MIDAS commands continue behaving correctly after changes.

Evals should test:

- Command routing
- Output format
- Source discipline
- Classification usage
- Scoring usage
- Metric usage
- No buy/sell recommendation language
- No copy-trading framing
- Risk visibility
- Failure behavior
- Artifact behavior

Recommended eval files:

```bash
evals/
├── README.md
├── gems.eval.md
├── track.eval.md
├── research.eval.md
├── financials.eval.md
├── thesis.eval.md
├── risk.eval.md
└── full.eval.md
```

Every major command should eventually have at least:

- Normal success case
- Weak/missing evidence case
- Guardrail case

---

# Layer 8 — Schemas Layer

## Folder

```bash
schemas/
```

## Purpose

Schemas define shared artifact and data-shape conventions.

Schemas are useful when MIDAS starts saving structured research artifacts.

They help prevent inconsistent watchlist items, research reports, scorecards, and tracker leads.

Recommended schemas:

```bash
schemas/
├── research_artifact.schema.md
├── watchlist.schema.md
├── tracker_lead.schema.md
├── scorecard.schema.md
└── command_output.schema.md
```

Schemas are optional early on.

Build them when artifacts become important.

---

# Layer 9 — Workspace / Artifact Layer

## Folder

```bash
workspace/
```

## Purpose

The `workspace/` folder stores generated research artifacts.

Artifacts should be organized and easy to find.

Recommended workspace structure:

```bash
workspace/
├── tickers/
│   └── [ticker]/
│       ├── research.md
│       ├── financials.md
│       ├── thesis.md
│       ├── risk.md
│       ├── scorecard.md
│       └── updates.md
├── watchlists/
│   ├── main_watchlist.md
│   └── hidden_gems.md
├── trackers/
│   ├── managers/
│   ├── insiders/
│   └── politicians/
└── reports/
    └── full/
```

Commands should define command-specific artifact behavior in their skill file and follow `/home/jordan/.hermes/profiles/midas/rules/ARTIFACTS.md`.

---

# Command Lifecycle

Every MIDAS command should move through a simple lifecycle.

## 1. Idea

Define what the command should do.

## 2. Skill Design

Create or update:

```bash
skills/[category]/[command]/SKILL.md
```

Define:

- Purpose
- Inputs
- Workflow
- Sources/tools
- Classification/scoring usage
- Output behavior
- Artifact behavior
- Failure behavior

## 3. Output Design

Create or update:

```bash
skills/[category]/[command]/OUTPUT.md
```

Reference:

```bash
rules/OUTPUT.md
```

Do not duplicate global output standards.

## 4. Eval Design

Create evals in:

```bash
evals/[command].eval.md
```

At minimum test:

- Normal case
- Weak evidence case
- Guardrail case

## 5. Artifact Design

If the command writes files, define:

- Where it writes
- Whether it creates, replaces, appends, or updates
- What happens if a file already exists
- Whether a schema applies

## 6. Review

Check the command against:

- `rules/GLOBAL.md`
- `rules/SOURCES.md`
- `rules/CLASSIFICATIONS.md`
- `rules/SCORING.md`
- `rules/METRICS.md`
- `rules/OUTPUT.md`
- `rules/ARTIFACTS.md` when a command writes artifacts

## 7. Stabilize

A command is stable when:

- Workflow is clear
- Output is consistent
- Evals exist
- Artifacts are predictable
- Guardrails are respected
- No global rules are duplicated inside the skill

---

# Command-Building Standard

Every command should answer these questions:

```md
1. What does this command do?
2. When should it be used?
3. What inputs does it require?
4. What optional inputs does it accept?
5. What sources/tools does it use?
6. What workflow steps does it follow?
7. Does it classify the setup?
8. Does it score the setup?
9. Does it use metrics?
10. What output format does it use?
11. Does it create or update artifacts?
12. How does it fail gracefully?
13. What evals prove it works?
```

If a command cannot answer these, it is not ready.

---

# Global Rule Reference Pattern

Skills should reference global rule files explicitly.

Example:

```md
This command must follow:

- `/home/jordan/.hermes/profiles/midas/rules/GLOBAL.md`
- `/home/jordan/.hermes/profiles/midas/rules/SOURCES.md`
- `/home/jordan/.hermes/profiles/midas/rules/OUTPUT.md`

Use when applicable:

- `/home/jordan/.hermes/profiles/midas/rules/CLASSIFICATIONS.md`
- `/home/jordan/.hermes/profiles/midas/rules/SCORING.md`
- `/home/jordan/.hermes/profiles/midas/rules/METRICS.md`
- `/home/jordan/.hermes/profiles/midas/rules/ARTIFACTS.md` when a command writes artifacts
```

This prevents duplication and keeps shared behavior centralized.

---

# Data Flow

Typical research command data flow:

```md
User request
→ command routing
→ skill workflow
→ source/evidence gathering
→ metric extraction if needed
→ analysis
→ classification/scoring if appropriate
→ risk/disconfirming evidence
→ output formatting
→ artifact save/update if required
```

Example: `!gems`

```md
Theme or screen request
→ identify candidate universe
→ gather evidence
→ apply source standards
→ apply Hidden-Gem Overlay
→ classify setup
→ rank candidates
→ show risks and next command
```

Example: `!track`

```md
Manager / insider / politician / disclosure request
→ identify latest disclosure
→ compare with prior disclosure when possible
→ identify changes
→ treat changes as research leads
→ classify/rank leads if appropriate
→ show limitations
→ suggest next diligence command
```

Example: `!full`

```md
Ticker request
→ gather full company evidence
→ analyze business, financials, moat, management, valuation, risks
→ apply scoring/classification
→ produce full report
→ save/update artifact
```

---

# What Not To Duplicate

Do not duplicate:

- Source hierarchy inside skills
- Full classification definitions inside skills
- Full scoring frameworks inside skills
- Full metric formula library inside skills
- Full output standards inside skills
- Full artifact policy inside skills or skill-local references
- Global guardrails inside every command

Instead, reference the correct global rule file.

Duplication causes drift.

Drift causes inconsistent behavior.

---

# What Belongs Where

## Put in `SOUL.md`

- Identity
- Mission
- Research temperament
- High-level philosophy

## Put in `AGENTS.md`

- Read order
- Folder map
- Agent editing instructions
- Build process
- Maintainer guidance

## Put in `rules/`

- Shared standards
- Source rules
- Scoring rules
- Metric definitions
- Classification standards
- Output standards
- Runtime guardrails

## Put in `skills/`

- Command triggers
- Command workflows
- Command-specific output details
- Command-specific artifact behavior
- Command-specific failure behavior

## Put in `templates/`

- Reusable scaffolds
- New command templates
- Eval templates
- Output templates

## Put in `evals/`

- Golden examples
- Regression tests
- Guardrail tests

## Put in `docs/`

- Architecture
- Command registry
- Build plans
- Design notes

## Put in `schemas/`

- Artifact shape definitions
- Watchlist item formats
- Scorecard formats
- Evidence ledger formats

## Put in `workspace/`

- Generated research
- Reports
- Watchlists
- Tracker artifacts
- Ticker files

---

# Build Order

Recommended build order:

```md
1. SOUL.md
2. Global rules
3. AGENTS.md
4. docs/ARCHITECTURE.md
5. templates/COMMAND_SKILL_TEMPLATE.md
6. evals/README.md
7. docs/COMMAND_REGISTRY.md
8. Core command skills
9. Command evals
10. Workspace/artifact schemas
11. Watchlist and tracker artifacts
12. Council or multi-agent workflows later
```

Do not build council/multi-agent complexity too early.

Maximize the single-agent MIDAS workflow first.

---

# Command Refactor Order

Recommended command refactor order:

```md
1. !commands
2. !gems
3. !track
4. !research
5. !financials
6. !thesis
7. !risk
8. !full
9. !earnings
10. !updates
```

Why this order:

- `!commands` defines user-facing command discovery.
- `!gems` and `!track` depend heavily on classifications, scoring, and sources.
- `!research`, `!financials`, `!thesis`, and `!risk` form the core research stack.
- `!full` combines other workflows and should come after the pieces are stable.
- `!earnings` and `!updates` can be lighter and may omit scoring/classification unless evaluating.

---

# Anti-Patterns

Avoid these architecture problems:

## 1. Rule Duplication

Problem:

```md
Every command repeats the same source hierarchy.
```

Fix:

```md
Reference `rules/SOURCES.md`.
```

## 2. Skill Bloat

Problem:

```md
A command skill becomes a giant rulebook.
```

Fix:

```md
Move shared standards into `rules/`.
Keep skill-specific workflow in `skills/`.
```

## 3. Output Sprawl

Problem:

```md
Every command invents a new output format.
```

Fix:

```md
Use `rules/OUTPUT.md` and command-specific `OUTPUT.md`.
```

## 4. No Evals

Problem:

```md
Commands change behavior after refactors.
```

Fix:

```md
Add evals before calling a command stable.
```

## 5. Artifact Chaos

Problem:

```md
Research files get scattered everywhere.
```

Fix:

```md
Use consistent `workspace/tickers/[ticker]/` paths for ticker artifacts.
Define command-specific artifact behavior in each skill and follow `rules/ARTIFACTS.md`.
```

## 6. Overbuilding

Problem:

```md
Creating council/multi-agent systems before core commands are stable.
```

Fix:

```md
Stabilize single-agent skills first.
```

## 7. Prompt Drift

Problem:

```md
New commands ignore global rules.
```

Fix:

```md
Every command skill should explicitly reference relevant global rules.
```

---

# Stability Standard

A MIDAS component is stable when:

- Its purpose is clear
- Its file location is correct
- It does not duplicate other layers
- It references the right rules
- It has predictable behavior
- It has eval coverage if important
- It does not break source, scoring, output, or guardrail standards

A command is not stable just because it works once.

A command is stable when it behaves consistently under normal, weak-evidence, and guardrail scenarios.

---

# Future Expansion

Possible future architecture additions:

```bash
docs/COMMAND_REGISTRY.md
docs/BUILD_ORDER.md
templates/COMMAND_OUTPUT_TEMPLATE.md
templates/COMMAND_EVAL_TEMPLATE.md
evals/[command].eval.md
schemas/research_artifact.schema.md
schemas/watchlist.schema.md
schemas/tracker_lead.schema.md
rules/ARTIFACTS.md
rules/WATCHLIST.md
rules/COUNCIL.md
```

Do not add these just to add them.

Add them when they solve a real problem.

---

# Final Rule

Architecture should make MIDAS easier to build, not harder.

Keep the system modular.

Keep global standards global.

Keep command workflows inside skills.

Keep outputs consistent.

Keep artifacts organized.

Keep evals close to commands.

Do not duplicate rules.

Do not overbuild too early.

Build the simplest version that is clean, testable, and easy to extend.
