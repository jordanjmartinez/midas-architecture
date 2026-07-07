# Maintenance Reference Manifest

This folder separates active reusable maintenance playbooks from archived historical notes.

Active references are operating playbooks.

Archived references are preserved context, not active routing law.

A reference is not active merely because it exists, was historically linked, or lives in a `references/` folder.

Do not treat archived references as active rules unless `MAINTENANCE.md`, an active playbook, or the user explicitly names them.

## Folders

- `active/` — short reusable playbooks for recurring maintenance workflows
- `archive/` — historical patch notes, staged implementation records, incident records, and narrow one-off lessons

## Legacy Source After Migration

Former legacy source:

`skills/stock-analysis/midas-maintenance/references/`

The legacy maintenance folder was removed after the canonical maintenance skill, durable contract, output contract, reference manifest, active playbooks, and eval were installed.

Do not recreate or bulk-link the old legacy folder.

Do not treat deleted historical references as active routing law.

## Active Playbooks

Active playbooks should be reusable across future MIDAS maintenance tasks.

They should be short, operational, and general enough to guide repeated work.

Planned active playbook set:

- `exact-scope-edits.md` — read-first, exact-scope patching and prohibited adjacent cleanup
- `command-lifecycle.md` — command creation, output contracts, evals, validation, activation, and status discipline
- `registry-metadata.md` — command registry and command metadata consistency checks
- `eval-maintenance.md` — eval creation, fixture use, status labels, run logs, and regression coverage
- `artifact-policy-maintenance.md` — shared artifact policy, workspace boundaries, and save-path discipline
- `dirty-worktree-verification.md` — scoped verification when the profile already has unrelated dirty files
- `staged-contract-authority-checks.md` — placing Contract Authority Checks in staged maintenance plans before approval/execution
- `template-change-discipline.md` — avoiding template bloat and preferring short pointers over full maintenance ceremony

The approved active playbook set has been created.

Do not expand this set without a clear reusable-playbook reason.

## Archived Historical Notes

Historical notes should be preserved but not treated as default instructions.

Planned archive buckets:

- `market-data/` — market-data standards, helper behavior, fallback policy, runtime activation, and display cleanup history
- `tracker/` — tracker migrations, Alpha Queue work, contract layers, validation stages, and activation history
- `research/` — research command boundary patches, output drift, and chat-display regressions
- `financials/` — financials output polish, status activation, and section-separation history
- `risk-thesis/` — risk/thesis readability, rerating, market-context, and best-next-command work
- `commands-menu/` — `!commands` menu/output/eval/readiness history
- `updates/` — updates output/eval/fixture cleanup history
- `watchlist/` — `!wl`, `!watchlist`, and `!list` output/eval/alias staging history
- `earnings/` — earnings output/eval/activation history
- `gems/` — gems output polish and validation history
- `registry/` — registry cleanup, metadata normalization, and command maturity audit history
- `global-output/` — shared output, best-next-command, artifact, Telegram readability, and display-rule work
- `contract-authority/` or dated contract-authority notes — historical Contract Authority placement, stage-gate, and template-bloat cleanup records

Archive buckets are retained as a classification scheme for future reference work, but the old legacy folder has been deleted.

Do not recreate historical archive buckets unless the user explicitly asks to preserve or import external historical notes.

## Triage Rules

Put a reference in `active/` only if it answers:

- When should this reusable playbook be used?
- What exact steps should future maintenance follow?
- What files or authority layers usually matter?
- What should verification prove?
- What pitfalls should be avoided repeatedly?

Put a reference in `archive/` if it mainly records:

- a past patch
- a one-off incident
- a command-specific staged rollout
- a temporary migration note
- a narrow validation record
- a historical status activation
- a previous user's exact-scope instruction that should not become general law

When in doubt, archive the historical note and distill only the reusable lesson into an active playbook.

## Policy

The active maintenance contract is:

`skills/maintenance/MAINTENANCE.md`

The skill loader is:

`skills/maintenance/SKILL.md`

This README is a manifest and triage guide, not a hidden global rulebook.

Prefer fewer active references.

Prefer small reusable playbooks over large historical records.

Prefer explicit user scope over inferred legacy precedent.
