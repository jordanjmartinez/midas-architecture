# MIDAS Contract Authority

## Purpose

CONTRACT_AUTHORITY.md defines where MIDAS rules, contracts, references, templates, schemas, docs, eval requirements, and command-specific behavior belong.

The goal is to prevent secondary law: command-local files, output contracts, evals, references, templates, docs, or archived notes becoming hidden global rulebooks.

Every MIDAS rule should have one authoritative home.

Command files may specialize global behavior, but they must not become hidden global law.

Do not duplicate global policy inside command files.

Do not hide cross-command behavior inside command-local references.

Do not preserve stale local rules after a behavior has been globalized.

## Core Rule

Before adding, expanding, or editing any MIDAS rule, contract, reference, template, schema, doc, eval requirement, or command-local instruction, MIDAS must answer the Contract Authority Check.

If MIDAS cannot answer the check, it must stop and ask before patching.

## Required Contract Authority Check

```md
Contract Authority Check:
- Existing global authority checked: [files]
- Existing command authority checked: [files]
- Proposed new or changed behavior: [summary]
- Applies to: [one command / multiple commands / global]
- Correct home: [rules / SKILL.md / OUTPUT.md / contracts / evals / docs / templates / schemas / references / archive]
- Reason: [why]
- Duplication risk: [none / possible / confirmed]
- Action: [point to existing rule / create global rule / create command-local rule / archive / defer]
```

## Placement Decision Tree

### 1. Already global

If the rule already exists in `rules/`, do not duplicate it.

Use a short pointer instead:

```md
Follow `/home/jordan/.hermes/profiles/midas/rules/[RULE].md`.
```

### 2. Applies to multiple commands

If the behavior applies to multiple commands or future commands, do not place it only inside one command.

Choose:

- `rules/` if it changes shared runtime behavior
- `docs/` if it explains architecture
- `templates/` if it is reusable scaffolding
- `schemas/` if it defines structured data
- `evals/` if it tests shared behavior already stated in an active contract

Then add short pointers from affected command files when needed.

### 3. Applies to one command only

If the behavior is truly command-specific:

- workflow belongs in command `SKILL.md`
- display shape belongs in command `OUTPUT.md`
- regression coverage belongs in command evals
- examples, extraction notes, fixtures, and edge cases may live in command `references/`

Command-local contracts may define only the delta from global behavior.

Good:

```md
Follow `rules/ARTIFACTS.md`.

Command-specific artifact behavior:
- Standard mode writes to `workspace/tickers/[ticker]/research.md`.
- Compact mode does not save by default.
```

Bad:

```md
[Full copy of the global artifact policy pasted into the command skill.]
```

### 4. Historical incident

If the content describes what happened in a past patch, runtime incident, one-off migration, or implementation stage, do not make it active law by default.

Place it in `references/archive/` when preservation is useful.

Archived means:

- preserved for context
- not active routing law
- not automatically loaded as a current rule
- not authoritative unless an active contract explicitly cites it

Archived does not mean deleted.

## Authority Layers

### `rules/`

Use for shared runtime standards that apply across commands.

Examples:

- source standards
- artifact behavior
- output standards
- scoring rules
- setup classifications
- metric definitions
- investment-language guardrails
- shared market-data behavior
- shared best-next-command behavior
- shared contract-authority behavior

If multiple commands need the behavior, start by considering `rules/`.

### Command `SKILL.md`

Use for command-specific controller behavior.

Allowed:

- trigger syntax
- aliases
- required and optional inputs
- command-specific workflow
- command-specific source needs
- command-specific artifact behavior
- command-specific guardrails
- failure behavior
- short pointers to global rules

Not allowed:

- full copies of global source, output, artifact, scoring, classification, metric, or guardrail rules
- cross-command standards
- hidden global behavior
- unrelated command behavior
- historical patch notes treated as active rules

### Command `OUTPUT.md`

Use for command-specific display shape.

Allowed:

- compact, standard, and full section order
- required, optional, and prohibited sections
- command-specific artifact confirmation wording
- command-specific failure output shape
- command-specific examples of output shape

Not allowed:

- source hierarchy rules
- scoring formulas
- metric definitions
- artifact policy beyond command-specific display behavior
- command workflow steps
- cross-command output standards that belong in `rules/OUTPUT.md`

### Command `contracts/`

Use for command-local intelligence contracts: decision logic too large or too dense for `SKILL.md`.

A command-local contract governs how one command reasons. Examples: promotion and demotion gates, eligibility filters, triage lenses, signal matrices, evidence-pack requirements, false-positive libraries, and ranking discipline for a single command.

Requirements for every file in a command `contracts/` folder:

- Lives at `skills/[category]/[command]/contracts/[name].md`.
- Linked from that command's `SKILL.md` with an explicit "must follow" statement.
- Begins with an `## Authority Boundaries` section listing what the contract owns and what it does not own.
- Defers to global rules by path for shared behavior and defines only command-local logic and deltas.

Allowed:

- command-local promotion, demotion, gating, triage, and ranking logic
- command-local signal interpretation and evidence-pack requirements
- interaction clauses with global scoring, classification, and rerating rules, without redefining them

Not allowed:

- cross-command behavior
- redefinition of global source, metric, scoring, classification, output, artifact, or guardrail rules
- output section templates, which belong in the command `OUTPUT.md`
- trigger syntax, routing, inputs, or workflow, which belong in the command `SKILL.md`
- large machine-readable data shapes, which belong in `schemas/`

Named command-local contract files outside a `contracts/` folder (for example a maintenance skill's `MAINTENANCE.md` or `PLAN.md`) follow the same requirements.

### `evals/`

Use for regression and behavior checks.

Evals may test contracts but must not create contracts.

Allowed:

- normal success cases
- weak-evidence cases
- guardrail cases
- artifact cases
- registry drift cases
- known regression cases

Not allowed:

- new runtime law that exists only in evals
- policy definitions not present in the relevant rule, command contract, schema, or template

If an eval requires behavior, that behavior must also exist in the relevant rule, command `SKILL.md`, command `OUTPUT.md`, schema, or template.

If the only place a requirement exists is an eval, treat that as contract drift.

### `docs/`

Use for architecture explanation, registries, migration plans, readiness notes, and human-readable design context.

Allowed:

- architecture maps
- command registry
- migration history
- staged rollout explanations
- design rationale

Not allowed:

- hidden runtime rules that commands must follow but do not reference from rules or skills

### `templates/`

Use for reusable scaffolding.

Allowed:

- command skill templates
- command output templates
- eval templates
- report templates
- recurring file skeletons

Not allowed:

- active runtime policy that should live in `rules/`

### `schemas/`

Use for structured data and artifact shapes.

Allowed:

- JSON schemas
- table schemas
- artifact data shape contracts
- machine-readable output shapes

Not allowed:

- prose workflow rules that belong in skills or rules

### `references/`

Use for command-local support material only.

Allowed:

- command-specific examples
- command-specific extraction notes
- command-specific citation examples
- command-specific edge cases
- command-specific API quirks
- long examples that keep `SKILL.md` lean

Not allowed:

- cross-command rules
- global source rules
- global artifact rules
- global output rules
- global metric rules
- global scoring rules
- global classification rules
- registry rules
- watchlist source-of-truth rules
- anything used by multiple commands

If a reference file applies to more than one command, promote the reusable part to the correct authority layer and archive the original note when preservation is useful.

### `references/archive/`

Use for historical incident notes and old implementation records.

Archived notes may preserve lessons, but the active rule should live in the correct authority layer.

## No Secondary Law Rule

Command-local files must not become secondary global rulebooks.

Secondary law includes:

- global behavior defined only in one command `SKILL.md`
- global output policy defined only in one command `OUTPUT.md`
- global artifact behavior hidden in a command reference
- eval assertions requiring behavior not stated in any active contract
- archived incident notes treated as current instructions
- duplicated global rules that drift from the authoritative file

When secondary law is found, MIDAS should propose one of:

- point to the existing global rule
- promote the reusable rule to `rules/`
- move architecture explanation to `docs/`
- move scaffolding to `templates/`
- move structure to `schemas/`
- keep only command-specific delta locally
- archive historical notes
- delete duplicated local policy only after approval

## Reference Alignment Rule

References may support active contracts but must not override them.

An active command reference must be:

- directly linked from the command `SKILL.md`
- command-local
- scoped to examples, extraction, fixtures, or edge cases
- non-conflicting with global rules

If a reference contains reusable cross-command behavior, promote the reusable part and archive the original note.

## Maintenance Behavior

When maintaining MIDAS contracts, prefer this order:

1. point to existing global rule
2. create or update a global rule if the behavior is shared
3. keep only command-specific delta locally
4. add eval coverage
5. archive historical notes
6. avoid duplicate active contracts

Do not create a new command-local contract just because it is faster.

## Final Rule

Every MIDAS rule should have one authoritative home.

The command files may specialize, but they must not become hidden global law.
