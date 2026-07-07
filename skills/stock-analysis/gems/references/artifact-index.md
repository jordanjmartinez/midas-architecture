# !gems Artifact / Index Reference

## Purpose and Scope

This file owns `!gems` command-local artifact/index mechanics.

It is subordinate to `rules/ARTIFACTS.md`, which owns Midas-wide artifact standards.

This file does not own global artifact standards.

This file does not own visible output wording; `OUTPUT.md` owns display.

This file does not own hidden-gem intelligence logic; `contracts/hidden-gems.md` owns intelligence.

This file does not authorize watchlist mutation.

This file does not create schemas, proof packets, source manifests, evidence ledgers, fixture files, automation, or live command runs.

## Authority Boundaries

- `rules/ARTIFACTS.md` owns cross-command artifact standards, artifact safety, path hygiene, source preservation, write-confirmation discipline, failure behavior, and global artifact/checklist rules.
- `references/artifact-index.md` owns `!gems` command-local path and index mechanics.
- `OUTPUT.md` owns visible saved/index confirmation wording and the user-facing display of artifact write success or failure.
- `SKILL.md` routes command-local artifact/index mechanics to this file.
- `contracts/hidden-gems.md` owns `!gems` intelligence logic, including source authority, eligibility, promotion gates, demotion/blocking, scoring interaction, classification discipline, disconfirming evidence, and no-clean-candidate behavior.
- `data/midas_watchlist.json` remains separate from generated `!gems` artifacts.

## Canonical !gems Artifact Paths

Use these canonical artifact paths for `!gems` runs:

Broad mode:

- `workspace/gems/general.md`

Theme mode:

- `workspace/gems/[theme]/general.md`

Theme/subtheme mode:

- `workspace/gems/[theme]/[subtheme].md`

Index:

- `workspace/gems/index.md`

Use `general.md` when no subtheme exists.

Do not save new scans to legacy flat files such as `workspace/gems/space.md`, `workspace/gems/semiconductor-equipment.md`, or `workspace/gems/defense-drones.md`.

Do not create duplicate timestamped artifacts, archive files, or history files unless the user explicitly requests history/archive behavior.

## Theme and Subtheme Normalization

Normalize first-position theme aliases before resolving the artifact path:

- `semiconductor`, `semiconductors`, `semi`, and `semis` -> `semiconductors`
- `datacenter`, `datacenters`, and `data centers` -> `datacenters`
- `defense tech` -> `defense`
- `AI` and `artificial intelligence` -> `ai`

Singular/plural forms should resolve to the same folder when the theme intent is clear.

Slug rules:

- Folder and file names are lowercase.
- Multi-word subthemes use underscores.
- Do not use hyphens in new `!gems` subtheme slugs when current behavior requires underscores.
- Do not save multi-word scans as flat files like `semiconductor-equipment.md`.
- Do not concatenate words into unclear slugs like `semiequipment.md`.
- Use `general.md` when there is no subtheme.
- Keep path names stable once created unless the user explicitly approves a migration.

## Anti-Confusion Rule

Ambiguous theme/subtheme commands should not silently write to the wrong path.

Do not over-map vague or ambiguous commands into a different theme family.

Example:

`!gems power semiconductors`

This could mean `power` as the theme or `semiconductors` as the theme. Do not silently save it as:

`workspace/gems/semiconductors/power_semis.md`

unless the command clearly starts with the semiconductor theme or a known semiconductor alias.

Preferred explicit commands:

- `!gems semiconductors power`
- `!gems semiconductors power semis`

Then save to:

- `workspace/gems/semiconductors/power_semis.md`

If the theme/subtheme parse is unclear, clarify or use the safest broad/theme path according to existing behavior. Do not create a new folder path from ambiguous input without confidence.

## Folder Creation

Create folders only when needed for an approved artifact write.

Typical folders:

- `workspace/gems/`
- `workspace/gems/[theme]/`

Folder creation is part of the artifact write path, not a separate watchlist or workspace mutation.

Do not create folders in read-only, audit, planning, validation, or no-write contexts.

## Legacy Flat Artifact Handling

Do not delete, move, rename, or migrate legacy flat artifacts unless the user explicitly asks.

New scans use folder-based theme/subtheme paths.

If a legacy flat artifact or stale index row exists for the same theme, it may be read only for duplicate-candidate context during an approved write run.

The index should point to the current actual path written by the current run, not a stale legacy path.

Legacy cleanup remains separate and should not happen automatically.

## Duplicate and Cross-Theme Handling

Before saving an artifact, check whether an artifact already exists at the target path.

If the target artifact exists:

- Read the existing candidate list.
- Do not duplicate the same ticker twice inside the same artifact.
- If a previous candidate still qualifies, include it once and label or note it as a repeated candidate when useful.
- If a previous candidate no longer qualifies, remove it from the new clean artifact or move it to an appropriate screened-out/watch-only area when the output authority calls for that.
- If a new candidate qualifies, add it.
- Overwrite/update the artifact with a clean current list unless the user explicitly asks for history/archive behavior.

If the same ticker appears across multiple theme artifacts, label or note cross-theme relevance rather than duplicating blindly or implying separate recommendations.

Do not create timestamped history files or archive files unless the user explicitly requests them.

## Saved Artifact Requirements

A saved `!gems` Markdown artifact should be clean user-facing output, not scratch work.

Command-local artifact expectations include:

- as-of date or run date when appropriate
- command used when useful for later review
- mode and theme/subtheme context
- search/filter context when useful
- candidate list
- setup classification when used
- Hidden-Gem Overlay score or score display when used
- Evidence Confidence when used
- source limitations or caveats
- main risk or verification need
- next research step when useful
- final saved path or artifact path when useful
- no recommendation language
- no raw scratch work, hidden reasoning, tool logs, or unfinished analysis
- no claim that a ticker was added to a watchlist unless a separate approved watchlist command actually ran

Do not redefine the full output card template here. `OUTPUT.md` owns visible card shape and visible response structure.

## Index Behavior

`workspace/gems/index.md` is the `!gems` dashboard/index.

Update the index after a successful artifact save when index behavior is part of the command run.

Index rules:

- Keep `index.md` clean, not an append-only log.
- List artifacts by theme folder when useful.
- Avoid duplicate artifact lines.
- If the same theme/subtheme runs again, update the relevant artifact line instead of piling duplicates.
- If the same ticker appears across multiple theme artifacts, cross-theme candidates can be marked or summarized.
- No separate command is required for `index.md` maintenance if normal `!gems` artifact behavior includes index update.

Do not claim the index was updated unless the index update actually succeeded.

## Output Confirmation Boundary

`OUTPUT.md` owns visible confirmation wording.

`Saved to:` may appear only if the artifact write actually succeeded.

`Updated index:` may appear only if the index update actually succeeded.

Do not claim saved, updated, written, added, tracked, or indexed unless the action occurred.

If a write fails, output must state the failure plainly and must not pretend success.

Use the actual canonical path written in any visible confirmation.

## Watchlist Boundary

`!gems` must not auto-add candidates to `data/midas_watchlist.json`.

Watchlist data remains separate from generated research artifacts.

A manual next command such as `!list add TICKER` may be suggested only when appropriate and only as an optional manual action.

Do not claim a ticker was added to a watchlist unless a separate approved watchlist command actually ran and succeeded.

A saved `!gems` artifact is not a watchlist entry, holding, recommendation, or trade instruction.

## No-Write / Read-Only Boundary

In read-only, audit, planning, validation, or other no-write contexts, do not create folders, artifacts, index updates, or watchlist mutations.

Do not show saved/index confirmation lines in no-write contexts.

No-write validation may describe the intended path, but it must not claim the path was written, saved, updated, indexed, or added.

## Relationship to Global ARTIFACTS.md

This file inherits global artifact standards from `rules/ARTIFACTS.md`.

If this file conflicts with global `ARTIFACTS.md`, global standards win unless a command-specific exception is explicitly approved.

This file should not duplicate global artifact rules except where needed to define `!gems` command-local path and index mechanics.

## Relationship to OUTPUT.md

`OUTPUT.md` owns visible sections, candidate cards, failure/no-candidate output, Best Next Command display, and saved/index confirmation display.

This file owns the mechanics behind which `!gems` artifact path and index should be written during an approved write run.

Do not put output templates here.

## Relationship to hidden-gems.md

`contracts/hidden-gems.md` owns intelligence logic.

Artifact mechanics must not affect candidate ranking, scoring, gates, or classification.

A candidate can be promoted, demoted, capped, blocked, or routed to watch-only by the intelligence contract independently of whether an artifact write occurs.

Artifact write success or failure must not convert a weak candidate into a stronger research candidate, and artifact mechanics must not override no-clean-candidate discipline.

## Legacy Artifact File Note

The prior command-local artifact support file for `!gems` has been removed after migration.

Its durable artifact/index mechanics have been migrated into this reference.

This reference is now the command-local artifact/index mechanics map.

Global `rules/ARTIFACTS.md` remains the cross-command artifact authority.

## Deferred / Not Included

This file does not create, require, or authorize:

- schemas
- persisted proof packets
- source manifest files
- evidence ledger files
- fixture files
- watchlist writes
- automation
- live command runs
- downstream command runs
- registry changes
- eval test cases

This file does not change paths, write behavior, output wording, or live `!gems` behavior by itself.
