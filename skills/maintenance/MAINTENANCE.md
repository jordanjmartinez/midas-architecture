# MIDAS Maintenance Contract

Use this contract when the user asks to maintain, refactor, install, verify, audit, migrate, or clean MIDAS profile files.

This is a class-level maintenance contract. It is not a stock research command.

Do not run stock commands, create ticker artifacts, mutate watchlists, or perform live runtime validation unless the user explicitly asks.

## Default Scope

Profile root:

the MIDAS profile root

Stay inside the active MIDAS profile unless the user explicitly provides an external path.

Do not search broadly when the user gives exact paths or says the task is narrow.

Do not modify another Hermes profile's skills, rules, plugins, cron jobs, or memories unless the user explicitly directs it.

## Core Principle

Maintenance work must be:

- read-first
- exact-scope
- evidence-backed
- artifact-safe
- reversible where practical
- honest about what changed and what did not

## Plan and Stage-Gate Contract

For any multi-stage maintenance task, follow:

`skills/maintenance/PLAN.md`

Approval for one stage does not authorize later stages.

When a stage completes, stop and wait for explicit approval before continuing unless the user explicitly approved multiple named stages in the same message.

## Contract Authority

For rule placement, command contract cleanup, reference migration, and anti-duplication work, follow:

`rules/CONTRACT_AUTHORITY.md`

Before creating or expanding any command-local contract, check whether the behavior already exists globally or belongs globally.

## Authority Layers

- `rules/` = shared runtime standards
- command `SKILL.md` = command routing, workflow, inputs, source needs, artifact behavior, failure behavior, guardrails
- command `OUTPUT.md` = command-specific output shape and display contract
- `evals/` = regression and behavior checks
- `docs/` = architecture, registry, planning, and explanation
- `templates/` = reusable scaffolding
- `schemas/` = structured artifact/data conventions
- `tools/` = helper scripts and local utilities
- `workspace/` = generated research artifacts, not policy

Do not duplicate global rulebooks inside command files.

Prefer short pointers to authoritative shared rules.

Do not hide shared behavior inside a command-local `references/` folder.

## Supported Maintenance Modes

### 1. Read-Only Audit

Use when the user asks to inspect, verify, compare, or report.

Rules:

- Do not edit files.
- Do not run commands that create artifacts.
- Read only listed files unless the user allows prerequisite checks.
- Prefer targeted reads over broad discovery.
- Label findings as `present`, `missing`, `drift`, `blocked`, or `not verified within scope`.
- Stop after the report if requested.

### 2. Exact-Scope Patch

Use when the user approves specific edits.

Rules:

- Inspect target files before editing.
- Patch only approved files.
- Avoid adjacent cleanups unless required to make the requested edit coherent.
- Do not modify command behavior unless behavior change is in scope.
- Do not modify eval status unless eval status change is in scope.
- Do not modify registry status unless registry status change is in scope.
- Do not modify workspace artifacts or watchlists unless in scope.
- Verify only scoped files unless broader verification is approved.

### 3. Command Lifecycle Work

Use for creating, refactoring, validating, or activating commands.

Check:

- command `SKILL.md`
- command `OUTPUT.md`
- command eval file
- `docs/COMMAND_REGISTRY.md`
- command status
- artifact behavior
- guardrails
- registry metadata consistency

Status remains `Draft` unless the user explicitly asks for promotion and validation supports it.

Do not promote command status as a side effect of cleanup.

Do not run the command during architecture or contract work unless the user explicitly requests runtime validation.

### 4. Shared Rule Maintenance

Use when behavior belongs across multiple commands.

Rules:

- Put runtime behavior in `rules/`.
- Put architecture explanation in `docs/`.
- Put reusable scaffolding in `templates/`.
- Put data/artifact shapes in `schemas/`.
- Put command-local workflow only in command `SKILL.md`.
- Put command-local display shape only in command `OUTPUT.md`.

Shared rules should stay concise and reusable.

Command files should point to shared rules instead of copying them.

### 5. Reference Maintenance

Use when cleaning maintenance notes, playbooks, incident records, or staged migration records.

Rules:

- Active references should be short reusable playbooks.
- Historical patch notes should be archived unless generally reusable.
- Staged implementation notes should be archived unless they guide future staged work.
- Incident-specific lessons should be archived unless distilled into a general playbook.
- Do not link broad historical folders as active skill references.
- Do not let `references/` become a hidden global rule system.

## File and Artifact Boundaries

During maintenance, avoid creating generated research artifacts.

Do not write under `workspace/tickers/` unless the user explicitly asks for artifact work.

Do not mutate `data/midas_watchlist.json` or tracker/watchlist data files unless the user explicitly asks for watchlist/data work.

Do not print or save API key values.

Do not use live provider calls as a shortcut for file-contract verification.

## Dirty-Tree Discipline

A dirty profile does not prove the current task changed every dirty file.

When checking scope:

- inspect the files involved in the current task
- distinguish pre-existing dirt from current changes when possible
- avoid reverting unrelated dirty files
- report unrelated dirty state as a caveat, not as current-task evidence

If the user forbids broad checks, do not run broad checks just to prove cleanliness.

## Verification Checklist

Before final response, report:

- Files changed
- Files inspected
- Whether files outside scope changed
- Whether commands/evals were run
- Whether workspace artifacts were created or modified
- Whether watchlists/data files changed
- Whether status labels changed
- Whether secrets/API keys were printed or written
- Any limitations or unverified items

Use `present`, `missing`, `drift`, `blocked`, and `not verified within scope` when reporting audit findings.

## Pitfalls

- Do not broaden scope because nearby files look related.
- Do not run stock commands as a verification shortcut.
- Do not create ticker workspace artifacts during maintenance.
- Do not treat whole-profile dirty status as current-task changes.
- Do not patch old interrupted tasks after a new user scope arrives.
- Do not save API keys in rules, scripts, artifacts, evals, logs, or responses.
- Do not treat archived references as active rules by default.
- Do not turn one-off incident records into permanent routing law.
- Do not duplicate global rules inside command-local contracts.
- Do not promote Draft status labels without explicit approval.

## Final Rule

MIDAS maintenance should make the system smaller, clearer, safer, and easier to verify.
