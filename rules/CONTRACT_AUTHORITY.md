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

## Auto-Created Skill and Reference Promotion Gate

Hermes may create skills, references, lessons, notes, support files, or migration files during command work.

These files are not automatically active MIDAS policy.

Auto-created files are Draft / Unpromoted by default unless they pass this promotion gate.

This rule exists to prevent:

- Unlimited skill and reference bloat
- Ticker-specific lessons becoming global rules
- Session notes becoming secondary contracts
- Command-local references duplicating global policy
- Hidden rule systems inside references/
- Contradictory output, source, metric, artifact, scoring, classification, or registry behavior
- Auto-created maintenance files changing MIDAS behavior without review

### Authority Principle

A file becomes authoritative only when its authority is explicit.

The following do not make a file authoritative by themselves:

- Hermes generated it.
- It was saved under a command folder.
- It was saved under references/.
- It was linked once during a session.
- It contains strong language such as must, always, never, or required.
- It captures a runtime lesson from one ticker or one command test.
- It was created as part of a migration or refactor.

Active MIDAS behavior must come from one of these approved locations:

- `/home/jordan/.hermes/profiles/midas/rules/` for shared runtime behavior
- A command `SKILL.md` for command workflow, routing, inputs, and command boundaries
- A command `OUTPUT.md` for command-specific output shape
- `/home/jordan/.hermes/profiles/midas/evals/` for regression and behavior checks
- `/home/jordan/.hermes/profiles/midas/docs/` for architecture explanation
- `/home/jordan/.hermes/profiles/midas/templates/` for reusable scaffolding
- `/home/jordan/.hermes/profiles/midas/schemas/` for structured artifact shapes

### Guard Agent Role

When maintaining MIDAS files, the Guard Agent role is to reduce rule surface area, not create more of it.

Before creating, linking, promoting, or retaining any auto-created skill/reference/support file, MIDAS must ask:

1. Is this file solving a recurring MIDAS problem, not just documenting one session?
2. Is it command-local, or does it apply across commands?
3. Does an existing global rule, command skill, output contract, template, doc, or eval already cover this?
4. Does it introduce new behavior, or only examples/support?
5. Does it duplicate, contradict, weaken, or fork an existing rule?
6. Is the trigger narrow enough that the file will not load unnecessarily?
7. Is this better as a short patch to an existing rule/eval instead of a new file?
8. Is the file still useful after removing ticker-specific and session-specific details?

If the answer is unclear, the file remains Draft / Unpromoted.

### Promotion Criteria

An auto-created file may be promoted only if all applicable criteria are satisfied.

For a command-local reference:

- It supports exactly one command.
- It contains examples, extraction notes, citation examples, edge cases, API quirks, or read-on-demand material.
- It does not define cross-command source, metric, scoring, classification, output, artifact, registry, or watchlist policy.
- It starts with a clear deferral to the relevant global rules when touching shared behavior.
- It is linked from the command `SKILL.md` with a narrow trigger.
- It does not add a second active output contract or hidden workflow contract.
- It is not merely a one-off ticker runtime note unless the ticker-specific nature is explicit.

For a shared rule:

- It belongs under `/home/jordan/.hermes/profiles/midas/rules/`.
- It changes shared runtime behavior across commands.
- It does not duplicate the full contents of sibling rule files.
- It references sibling rule files by path when needed.
- It is concise enough to remain a control layer.
- It has or is paired with eval coverage when it prevents a real regression.

For an eval:

- It belongs under `/home/jordan/.hermes/profiles/midas/evals/`.
- It tests a real failure mode, regression, or guardrail.
- It has clear pass/fail criteria.
- It does not redefine runtime policy.
- It avoids overfitting to one ticker unless the failure is explicitly ticker-specific.

For a doc/template/schema:

- It is explanatory, reusable, or structural.
- It does not secretly change runtime command behavior.
- Runtime behavior is still governed by rules, skills, output contracts, and evals.

### Prohibited Auto-Promotion

MIDAS must not auto-promote:

- A new `SKILL.md` created only to manage other skills or references.
- A reference file that defines global policy.
- A reference file that contradicts `rules/GLOBAL.md`, `rules/SOURCES.md`, `rules/METRICS.md`, `rules/OUTPUT.md`, `rules/ARTIFACTS.md`, `rules/CLASSIFICATIONS.md`, `rules/SCORING.md`, or `rules/COMMAND_INTERFACE.md`.
- A ticker-specific runtime lesson that changes behavior for all tickers.
- A command test note that becomes a mandatory output contract.
- A migration note that remains as active policy after the migration is complete.
- A duplicate copy of an existing global rule.
- A vague lessons learned file linked from a command without a narrow trigger.
- A file that adds broad must/always/never requirements without eval coverage.
- A file that causes a command to drift into another command’s job.

### Required Status Labels

When an auto-created file is reviewed, classify it as one of:

- Draft Reference — useful note, not active policy.
- Promoted Command Reference — active command-local support file with narrow trigger.
- Global Rule Candidate — should be moved or condensed into `/home/jordan/.hermes/profiles/midas/rules/`.
- Eval Candidate — should become a regression or guardrail eval.
- Docs / Template Candidate — explanatory or reusable scaffolding, not runtime policy.
- Archive / Delete Candidate — obsolete, duplicative, over-specific, contradictory, or not durable.

Unreviewed auto-created files are always treated as Draft Reference.

### Cleanup Actions

When reviewing auto-created files, choose the smallest safe action:

1. Keep as command-local reference with a clear deferral notice.
2. Condense into an existing command reference.
3. Move shared behavior into an existing global rule.
4. Convert a failure mode into an eval.
5. Move architecture explanation into docs.
6. Move reusable structure into templates or schemas.
7. Replace with a short pointer to the authoritative rule.
8. Archive or delete if duplicative, stale, contradictory, or too specific.

Do not create a new file when a smaller patch to an existing file is enough.

### Reference Deferral Notice

Any retained command-local reference that touches shared behavior should begin with a notice like:

```text
This is a command-local support reference. It is not a global MIDAS policy. If this file conflicts with the applicable files listed in `rules/GLOBAL.md` under Shared Rule Library, the global rule files control.
```

Use a narrower notice when only one or two global rule files are relevant.

### Conflict Rule

If an auto-created skill, reference, note, or migration file conflicts with an active MIDAS rule or command contract:

1. Do not follow the conflicting file as policy.
2. Treat the conflict as drift.
3. Preserve useful command-specific details only if they can be made non-conflicting.
4. Move the durable lesson to the correct authority layer.
5. Add or update an eval if the conflict represents a likely regression.

### Self-Improvement Write Gate

MIDAS may notice reusable lessons during research, maintenance, audits, regressions, or command work, but noticing a lesson is not permission to change architecture.

Do not create, patch, promote, link, or reorganize MIDAS skills, rules, contracts, active references, templates, schemas, docs, or evals as a self-improvement action unless the user explicitly asks for that change or explicitly confirms it after it is proposed.

During read-only audits, MIDAS must not perform self-improvement writes. In read-only mode, self-improvement should be limited to a recommendation in the final response.

If a lesson would affect command behavior, output shape, routing, source standards, scoring, classifications, artifacts, watchlist behavior, or maintenance architecture, treat it as an architecture change and route it through the Contract Authority Check before editing.

### Skill-Creation Guard

Creating a new skill is a high-friction action.

Do not create a new skill when the issue can be solved by:

- Patching an existing command `SKILL.md`
- Patching an existing command `OUTPUT.md`
- Patching an existing global rule
- Adding an eval
- Adding a short command-local reference with a narrow trigger
- Updating docs/templates/schemas

A new skill is allowed only when the user explicitly asks for or confirms the new skill and it defines a genuinely new recurring command/workflow with clear trigger syntax, inputs, outputs, boundaries, artifact behavior, registry entry, and eval plan.

### Maintenance Sweep Rule

During MIDAS maintenance, refactors, migrations, or command activation work, check for newly created or recently modified skill/reference/support files.

For each suspicious file, decide:

- Promote
- Condense
- Move
- Convert to eval
- Replace with pointer
- Archive/delete
- Leave Draft / Unpromoted

Do not leave many narrow near-duplicate files active by default.

### Promotion Gate Final Rule

MIDAS should learn from repeated failures, but learning should make the system smaller, clearer, and more reliable.

Auto-created files are notes until promoted.

References support commands; they do not govern MIDAS.

Global behavior belongs in global rules.

Regressions belong in evals.

Command behavior belongs in command skills and command output contracts.

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
