---
name: maintenance
description: Maintain Midas profile rules, command architecture, registries, evals, docs, templates, schemas, tools, and workspace conventions with exact-scope edits, read-first audits, and verification.
version: 2.0.0
author: Midas / Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [midas, maintenance, rules, command-architecture, exact-scope, verification]
---

# Midas Maintenance Skill Loader

## Registry Metadata

Command: `maintenance` (skill trigger; no `!` command syntax)
Aliases: `None`
Category: `System / Utility`
Status: `Active`
Skill Path: `skills/maintenance/SKILL.md`
Output Path: `skills/maintenance/OUTPUT.md`
Eval File: `evals/maintenance.eval.md`
Uses Classification: `Not used`
Uses Scoring: `Not used`
Uses Metrics: `Not used`
Writes Artifacts: `No` (edits Midas profile files under the maintenance contracts; does not write workspace research artifacts)
Primary Global Rules: `GLOBAL.md, CONTRACT_AUTHORITY.md, ARTIFACTS.md, COMMAND_INTERFACE.md`

Use this skill for Midas maintenance, refactors, audits, installs, verification, command lifecycle work, registry cleanup, eval maintenance, shared-rule cleanup, and artifact-policy maintenance.

Do not substitute the protected `hermes-agent` skill for Midas profile maintenance. Load `hermes-agent` only when the user is configuring, troubleshooting, or extending Hermes Agent itself; for Midas skills/rules/contracts/reference cleanup, this maintenance skill is the governing umbrella.

Active contracts:

- `skills/maintenance/MAINTENANCE.md` — maintenance scope, authority layers, exact-scope behavior, verification.
- `skills/maintenance/PLAN.md` — staged plan presentation, approval gates, execution boundaries, and stop rules.
- `skills/maintenance/OUTPUT.md` — maintenance report/output format.

Follow `MAINTENANCE.md` as the active maintenance contract.

Follow `PLAN.md` for staged maintenance work.

Follow `OUTPUT.md` when reporting maintenance work, audits, staged changes, verification, and limitations.

Reference policy:

`skills/maintenance/references/README.md`

Do not treat archived references as active rules unless the active contract or user explicitly names them.

Active playbooks:

- `skills/maintenance/references/active/skill-library-curation.md` — use when reviewing sessions for skill-library updates; keep Midas skills class-level, extract reusable rules, and archive one-off history instead of promoting it to routing law.
- `skills/maintenance/references/active/global-rule-reference-audit.md` — use for read-only audits of global rule references, pointer accuracy, bloat, spiderweb risk, and stale rule-routing references; report staged recommendations before patching.
- `skills/maintenance/references/active/staged-contract-authority-checks.md` — use when staged maintenance work needs Contract Authority Checks placed before approval/execution.

Skill-library update rule:

When a session includes explicit user correction about maintenance workflow, staged approvals, reporting format, scope boundaries, or skill-library curation, patch the relevant class-level skill or active support file immediately. Prefer improving this maintenance umbrella over creating narrow one-session skills. Preserve the lesson as reusable procedure, not as a task narrative.

Session-review update rule:

When the user asks to review the conversation and update the skill library after Midas maintenance work, treat `skills/maintenance/SKILL.md` and its companion contracts as the default first patch target unless a more specific loaded skill clearly governs the lesson. Do not create one-session skills for maintenance corrections. If a lookup/loading path is awkward but the canonical maintenance files are already known, update `skills/maintenance/SKILL.md` or its support files rather than recording the awkward lookup as a durable tool limitation.

Contract-authority update rule:

When maintenance work adds or changes rules, contracts, references, templates, schemas, docs, eval requirements, or command-local instructions, perform the Contract Authority Check before patching. Make the proposed authority layer visible in the stage report. If the behavior applies across commands, prefer `rules/` plus short pointers over expanding a command-local file. If the content is historical or one-off, place it in `references/archive/` rather than active routing law.

Shared-rule ownership tightening rule:

When tightening Midas shared rule files, keep each file in its authority lane instead of letting it become a mini-registry or spiderweb. For `rules/OUTPUT.md`, preserve it as shared display guidance: command-specific `SKILL.md` and command-specific `OUTPUT.md` own exact required/optional/prohibited sections, mode behavior, and command-specific artifact behavior; `rules/ARTIFACTS.md` owns artifact paths/state/save behavior; `rules/GLOBAL.md` owns the shared rule-library pointer. Avoid broad global wording that forces optional command behavior, such as forcing Setup Classification into factual business-model research, or forcing artifact replacement summaries when a command contract only wants `Saved to:`.

Reference creation discipline:

When Midas maintenance would create a new command-local `references/` folder or add any new reference file, follow the Reference Creation Gate in `rules/ARTIFACTS.md` before creating files. Ask first unless the current user message explicitly approved the exact path and purpose. Perform the Reference Creation Check and verify the material is durable command-local support, not shared behavior that belongs in `rules/`, `docs/`, `templates/`, `schemas/`, `evals/`, command `SKILL.md`, command `OUTPUT.md`, or command-local `contracts/`. Do not create reference files just to preserve one-off incidents, staged implementation notes, or historical patch records; ask whether to archive, summarize into an active rule, or omit.

Duplicate skill/path preflight:

Before creating, moving, deleting, or reorganizing Midas skills, verify the canonical target path and search for duplicate or nested `SKILL.md` files with the same skill name. Do not create a nested duplicate skill such as `skills/maintenance/midas-maintenance/` when the intended class-level skill is already `skills/maintenance/`. If cleanup requires deletion, state the exact directory to be removed and preserve the canonical skill directory before running a destructive command.

Git push discipline:

When the user asks to push Midas maintenance work, do not bulk-stage the dirty profile. First inspect branch/upstream and status, then stage only the explicitly approved maintenance files for the current task. Commit those scoped files with a concise maintenance/docs message, push the current branch to its upstream, and verify ahead/behind is `0 0`. Report any unrelated dirty or untracked files as caveats, but do not include runtime/session state, memories, gateway files, caches, broad skill deletions, or unrelated tracker/workspace changes unless the user explicitly approved them.

Archived support notes:

- `references/archive/contract-authority-stage-gate-2026-06-14.md` — session-specific context for the contract-authority/stage-gate correction; archived context only, not active routing law.
- `references/archive/contract-authority-placement-2026-06-14.md` — historical placement/template-bloat note; archived because the reusable lesson is distilled into `references/active/template-change-discipline.md` and `rules/CONTRACT_AUTHORITY.md`.

When the user asks to review a session and update the skill library, be active: assume most sessions have at least one reusable skill-library improvement unless the session was genuinely smooth and produced no correction, workflow lesson, technique, or loaded-skill gap. First patch the currently loaded or consulted class-level skill if it governs the lesson. If no loaded skill fits, patch an existing umbrella skill before creating anything new. Embed user workflow/style corrections in the governing `SKILL.md` body, and put session-specific details only in concise `references/` support files. Do not create narrow one-session-one-skill entries when a class-level umbrella can absorb the lesson.
