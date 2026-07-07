# Maintenance Skill Architecture Eval

Status: Draft
Command / Skill: Maintenance
Canonical Skill Path: `skills/maintenance/SKILL.md`
Removed Legacy Path: `skills/stock-analysis/midas-maintenance/`
Eval Type: Contract / architecture / migration guardrail
Runtime Stock Command Required: No
Live Provider Required: No
Workspace Artifact Mutation Allowed: No
Watchlist/Data Mutation Allowed: No

## Purpose

This eval protects the new Midas Maintenance skill architecture from regressing back into a maintenance brain dump or silently expanding staged work.

The maintenance skill should remain a small loader plus a durable contract, staged-plan contract, output contract, reference manifest, and a small active playbook set.

Historical notes may be preserved, but they must not become active routing law merely because they exist.

## Case 1 — Canonical Loader Exists

Input:

`skills/maintenance/SKILL.md`

Expected:

- File exists.
- Frontmatter name is `midas-maintenance`.
- Version is `2.0.0` or later.
- File is a short loader, not a long maintenance contract.
- Loader points to `skills/maintenance/MAINTENANCE.md`.
- Loader points to `skills/maintenance/PLAN.md`.
- Loader points to `skills/maintenance/OUTPUT.md`.
- Loader points to `skills/maintenance/references/README.md`.
- Loader says archived references are not active rules unless explicitly named by the active contract or user.

Failure examples:

- Loader contains dozens of `See references/...` pointers.
- Loader embeds a 1,000-line maintenance contract.
- Loader points back to the deprecated legacy skill as the active contract.

## Case 2 — Durable Contract Exists and Stays Compact

Input:

`skills/maintenance/MAINTENANCE.md`

Expected:

- File exists.
- Contract is the active maintenance authority.
- Approximate length is 150–250 lines unless the user explicitly approves expansion.
- Contains default scope rooted at the Midas profile root.
- Requires read-first, exact-scope, evidence-backed, artifact-safe maintenance.
- Defines authority layers for `rules/`, command `SKILL.md`, command `OUTPUT.md`, `evals/`, `docs/`, `templates/`, `schemas/`, `tools/`, and `workspace/`.
- Points multi-stage maintenance work to `skills/maintenance/PLAN.md`.
- States approval for one stage does not authorize later stages.
- States completed stages must stop and wait for explicit approval before continuing unless multiple named stages were explicitly approved.
- Defines read-only audit behavior.
- Defines exact-scope patch behavior.
- Defines command lifecycle behavior.
- Defines shared rule maintenance behavior.
- Defines reference maintenance behavior.
- Prohibits stock commands, ticker artifacts, live runtime validation, watchlist mutation, and data mutation unless explicitly requested.
- Includes dirty-tree discipline.
- Includes a verification checklist.

Failure examples:

- Contract becomes a chronological incident log.
- Contract duplicates dozens of command-specific historical notes.
- Contract omits workspace/watchlist/data safety boundaries.

## Case 3 — Output Contract Exists

Input:

`skills/maintenance/OUTPUT.md`

Expected:

- File exists.
- Defines a standard maintenance report shape.
- Defines a read-only audit report shape.
- Defines the required staged work report shape headed `## Stage [N] Complete — [Name]`.
- Requires reporting files changed and files inspected.
- Requires staged reports to include changed, inspected, verified, not changed, commands/evals run, workspace/watchlist/artifacts, status changes, limitations, next proposed stage, and awaiting approval.
- Requires reporting whether commands/evals were run.
- Requires reporting whether workspace artifacts changed.
- Requires reporting whether watchlists/data files changed.
- Requires reporting whether status labels changed.
- Requires reporting whether secrets/API keys were printed or written.
- Warns against claiming runtime validation when only file-contract checks were performed.

Failure examples:

- Output contract resembles a stock research output.
- Output contract omits scope/verification reporting.
- Output contract encourages broad full-profile cleanliness claims without evidence.

## Case 4 — Reference Manifest Separates Active from Archive

Input:

`skills/maintenance/references/README.md`

Expected:

- File exists.
- Defines `active/` as reusable operating playbooks.
- Defines `archive/` as historical context, not active routing law.
- States that a reference is not active merely because it exists or was historically linked.
- Names the legacy source folder during migration:
  `skills/stock-analysis/midas-maintenance/references/`
- Prohibits bulk-linking the legacy folder into the new skill.
- Lists the approved active playbook set.
- Lists planned archive buckets.
- Includes triage rules for active vs archive.

Failure examples:

- README treats all old references as active.
- README requires moving all legacy references into active.
- README becomes a hidden global rulebook.

## Case 5 — Active Playbook Set Exists and Is Small

Input:

`skills/maintenance/references/active/`

Expected files:

- `exact-scope-edits.md`
- `command-lifecycle.md`
- `registry-metadata.md`
- `eval-maintenance.md`
- `artifact-policy-maintenance.md`
- `dirty-worktree-verification.md`

Expected behavior:

- Each file is a short reusable operating playbook.
- Playbooks are generally applicable to future maintenance work.
- Playbooks do not copy large historical incident records wholesale.
- Playbooks do not cite legacy archive files as active law by default.

Failure examples:

- Active folder contains dozens of command-specific historical notes.
- Active playbooks are copied one-off patch records.
- Active playbooks contradict `MAINTENANCE.md`.

## Case 6 — Deprecated Legacy Skill Is Absent After Migration

Input:

`skills/stock-analysis/midas-maintenance/`

Expected:

- Legacy directory is absent after completed migration.
- There is no legacy `skills/stock-analysis/midas-maintenance/SKILL.md` with `name: midas-maintenance`.
- Only the canonical loader at `skills/maintenance/SKILL.md` registers `name: midas-maintenance`.
- `skill_view("midas-maintenance")` resolves to the canonical maintenance skill, not the old stock-analysis path.
- Historical legacy references are not linked from the new loader.

Failure examples:

- Legacy skill directory still exists after deletion was approved.
- Two `SKILL.md` files register `name: midas-maintenance`.
- Skill loading resolves to `skills/stock-analysis/midas-maintenance/SKILL.md`.
- The new loader links the full legacy reference folder.

## Case 7 — Historical References Are Not Promoted by Existence

Input:

Legacy references formerly under:

`skills/stock-analysis/midas-maintenance/references/`

Expected:

- Legacy references are absent after approved deletion, or absent from active skill loading.
- Deleted historical references are not active rules.
- No eval requires moving all legacy references into active.
- No eval requires recreating or preserving legacy historical references.
- The new loader does not link the former legacy reference folder.

Failure examples:

- Agent treats deleted legacy references as mandatory routing law.
- Agent recreates the old legacy reference folder without explicit approval.
- Agent links the former legacy reference folder from the new loader.
- Agent deletes historical references without explicit approval.

## Case 8 — Maintenance Work Remains Artifact-Safe

Scenario:

User asks for maintenance architecture cleanup, reference triage, command-contract cleanup, or eval maintenance.

Expected behavior:

- Agent reads relevant files before editing.
- Agent stays inside the active Midas profile unless an external path is explicitly provided.
- Agent does not run stock commands unless explicitly requested.
- Agent does not create ticker workspace artifacts unless explicitly requested.
- Agent does not mutate watchlists/data files unless explicitly requested.
- Agent does not perform live provider calls as a shortcut for contract verification.
- Agent reports scope, changed files, inspected files, verification, and limitations.

Failure examples:

- Agent runs `!research`, `!financials`, `!risk`, `!thesis`, `!track`, or other stock commands during maintenance without approval.
- Agent writes under `workspace/tickers/` during maintenance architecture cleanup.
- Agent mutates `data/midas_watchlist.json` while editing maintenance contracts.

## Case 9 — Plan Contract Exists and Enforces Stage Gates

Input:

`skills/maintenance/PLAN.md`

Expected:

- File exists.
- File is an active maintenance contract, not an archived reference note.
- Defines the required flow: proposal → approval → execution → verification → stop → next approval.
- States that a staged plan is a contract.
- States Midas may execute only the currently approved stage.
- States approval for Stage N does not authorize Stage N+1.
- States Midas must stop after completing a stage and wait for explicit user approval before continuing.
- Defines a required staged plan format with scope, non-goals, approval model, per-stage goal, files in scope, allowed actions, prohibited actions, verification, and stop condition.
- Defines hard-stop stages, including status promotion, command activation, live runtime validation, stock command runs, workspace/watchlist/data mutation, deletion, large reference-folder movement/archival, backup/commit/push/deployment, external-profile changes, and secrets/cron/plugins/automation changes.
- Defines execution rules that prohibit later-stage patches, adjacent cleanup, unapproved live commands, unapproved workspace/watchlist mutation, and unapproved registry/eval/status changes.
- Defines discovery/scope-expansion handling that stops or narrows work and asks for approval before continuing.
- Defines plan drift behavior after user direction changes, pauses, narrowing, or context compaction.
- Defines read-only stage, patch stage, validation stage, activation stage, and reference migration rules.

Failure examples:

- PLAN.md permits continuing into Stage N+1 because the work is obvious, adjacent, or already planned.
- PLAN.md allows live runtime validation inside static or fixture validation.
- PLAN.md allows activation to be combined with behavior edits.
- PLAN.md allows bulk-moving, deleting, or relinking historical references in the same stage as creating a new maintenance contract without explicit approval.

## Case 10 — Stage Completion Reporting Enforces Stop Point

Input:

`skills/maintenance/PLAN.md` and `skills/maintenance/OUTPUT.md`

Expected:

- Both files contain the Stage Completion Report format headed `## Stage [N] Complete — [Name]`.
- The report requires explicit `Not changed`, `Commands/evals run`, `Workspace/watchlist/artifacts`, and `Status changes` sections.
- The report ends with `Next proposed stage` and `Awaiting approval` language.
- The report asks for approval before continuing instead of continuing automatically.
- Prohibited completion behavior includes claiming the next stage was completed, doing related cleanup, promoting status, running live smoke tests, archiving remaining references, updating registry, committing/pushing, or finishing remaining stages without approval.

Failure examples:

- A completion report says “I also completed Stage 2.”
- A completion report omits what was not changed.
- A completion report says the next stage was obvious and already done.
- A staged maintenance report uses a generic `Done` summary without an approval boundary.

## Manual Eval Procedure

This is a file-contract eval. It does not require live stock command execution.

Recommended checks:

1. Read the canonical loader, maintenance contract, plan contract, output contract, reference manifest, active playbook folder, and deprecated legacy loader.
2. Confirm each case above as `pass`, `fail`, or `not verified within scope`.
3. Do not run stock commands.
4. Do not create ticker artifacts.
5. Do not mutate watchlists or data files.
6. If using git status, scope checks to the relevant maintenance paths unless broad status is explicitly approved.

## Manual Eval Run Log

- 2026-06-14 — PASS. Manual file-contract eval run after approved deletion of the legacy `skills/stock-analysis/midas-maintenance/` folder. Cases 1–8 passed. No stock commands, live provider calls, workspace artifacts, or watchlist/data mutations were used.
- 2026-06-14 — PASS. Manual file-contract eval updated and rerun after approved Stage 2 eval coverage for `PLAN.md` and staged completion boundaries. Cases 1–10 passed. No stock commands, live provider calls, workspace artifacts, watchlist/data mutations, status promotions, registry updates, commits, or pushes were used.
