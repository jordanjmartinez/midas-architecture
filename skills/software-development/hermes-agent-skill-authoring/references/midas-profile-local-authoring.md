# Midas Profile-Local Skill and Rule Authoring

Use this when editing Midas profile-local files under ``, especially `skills/stock-analysis/*/SKILL.md` and shared rules under `rules/`.

## Exact-content replacements

When the user says to replace a profile-local skill with exact content:

1. Overwrite only the named `SKILL.md` with the provided content.
2. Do not preserve old sections unless they are included in the supplied replacement.
3. Validate frontmatter after the write.
4. Do not run the command described by the skill.
5. Do not create runtime data files, watchlists, workspace artifacts, cron jobs, alerts, or background jobs unless explicitly asked.
6. If the user requests an exact confirmation line, final response must be exactly that line.

## Shared Midas architecture/support files

When the user asks to create or replace Midas profile-local support files such as `SOUL.md`, `AGENTS.md`, `docs/*.md`, `templates/*.md`, `evals/*.md`, or `schemas/*.md`:

1. Use the exact requested path under ``.
2. Create missing parent folders when needed.
3. Replace the target file cleanly; do not append a new version below an older version.
4. Do not create duplicate files with alternate names.
5. Keep architecture/docs/templates/evals/schema files distinct from command skills and runtime rules.
6. Do not update command skills, watchlists, workspace artifacts, cron jobs, or runtime data unless explicitly asked.
7. Verify the file exists and contains the requested top-level sections or key metadata fields.
8. If a template gains registry or lifecycle metadata, verify those exact checklist items are present.

## Shared Midas rules files

When the user asks to create a shared Midas rules file under `rules/`:

1. Treat it as a shared vocabulary/rule document, not a command skill.
2. Create the requested Markdown file exactly in the requested path.
3. Do not update command skills to consume the rule unless explicitly asked.
4. Do not create runtime artifacts or alter watchlist JSON files.
5. Verify that the file exists and contains the requested top-level sections.

Current Midas shared rule files:

- `rules/GLOBAL.md` — master operating policy for rule precedence, shared operating principles, guardrails, risk discipline, artifact discipline, and command/global separation.
- `rules/SOURCES.md` — filing-first source hierarchy, freshness/conflict handling, claim-to-source mapping, social/crowding guardrails, no-hype rules, and source display behavior.
- `rules/CLASSIFICATIONS.md` — shared Setup Classification vocabulary for evaluations, rankings, final views, research leads, and setup summaries.
- `rules/SCORING.md` — shared scoring architecture: Global Research Score, setup overlays, evidence confidence grades, caps/gates, and scoring/classification linkage.
- `rules/METRICS.md` — shared financial metric formulas, labeling, periods/as-of dates, GAAP/non-GAAP discipline, valuation/sector metric rules, quality grades, and metric red flags.
- `rules/OUTPUT.md` — shared formatting/output conventions, output modes, classification/score/evidence display, risk/disconfirming evidence display, source/as-of notes, artifact confirmations, and failure output.

When creating or replacing a shared rule file from user-supplied content:

1. Use `write_file` to replace the target file cleanly; do not append the new version below the old version.
2. Keep the file as a global rule document, not a command skill.
3. Do not duplicate the full contents of sibling rule files; reference them by absolute path when the user asks for a concise control-layer file.
4. Verify required headings and cross-file references after writing.
5. Update compact durable memory when a new shared rule file becomes part of the Midas standard library.

When the user later asks to connect command skills to a shared Midas rules file:

1. Patch each named skill lightly with a short section that references the shared file by absolute path.
2. Do not duplicate the shared rule definitions inside each command skill.
3. Preserve the command skill's existing workflow, output templates, storage paths, and watchlist behavior.
4. Verify that each target skill contains the shared rule path exactly once.
5. If the shared rule is meant to apply only when a command produces an evaluation/ranking/final view/research lead/setup summary, state that condition explicitly so raw data-only outputs are not over-classified.

## Midas templates, evals, and registry maintenance

When creating or replacing Midas support files such as command templates, eval templates, eval README files, or command registries:

- Treat user-supplied content as an exact clean replacement for the requested file.
- Keep these files in `templates/`, `evals/`, or `docs/` as requested; do not move them into command skills.
- Do not create command-specific eval files or output files unless explicitly requested.
- Do not update watchlists, workspace artifacts, command runtime data, cron jobs, or command skills unless explicitly requested.
- Verify both section headings and lifecycle/registry metadata fields when they are part of the requested file.
- When a template gains registry metadata, verify that the corresponding stability checklist includes registry-update requirements.
- When a command registry is created or replaced, verify the registry table, metadata standard, freshness rule, drift checks, and relationships to `!commands`, evals, and architecture.

When the user requests a patch/update-only change to a Midas template or support file:

- Patch the existing file instead of rewriting the whole file unless a targeted patch is not feasible.
- Do not edit adjacent templates or sibling files that the user explicitly excluded.
- Before patching, record a checksum for any explicitly excluded sibling file when useful; after patching, verify that checksum is unchanged.
- Verify each requested insertion/replacement and verify removed placeholders or obsolete path examples are gone.
- Preserve existing checklist items and append requested checklist additions in the specified location when possible.

## Command-menu maintenance

When updating the Midas `commands` skill:

- Patch only the visible menu lines requested.
- Keep it short and Telegram-friendly.
- Do not add `!help` or rename `!commands`.
- Do not bump versions or rewrite examples unless explicitly requested.

## Tracker skill maintenance

When updating the Midas `tracker` skill:

- Respect the current version's command model; remove stale old-command behavior when the user replaces the skill.
- Do not create `tracker_watchlist.json`, tracker workspace artifacts, or modify `midas_watchlist.json` while merely editing the skill.
- If the tracker is being simplified toward research leads, avoid reintroducing profile-viewing, positions-viewing, refresh, alerting, or automation behavior unless the user asks.