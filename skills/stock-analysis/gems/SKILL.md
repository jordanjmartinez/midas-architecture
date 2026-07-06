---
name: gems
description: Use when the user invokes !gems, !gems [theme], !gems [theme] [subtheme], or canonical -audit variants to discover or audit potentially overlooked, misunderstood, underfollowed, or asymmetric small/mid-cap public companies for further research. Applies MIDAS hidden-gem quality controls, saves discovery artifacts to the Midas workspace for standard runs only, and follows OUTPUT.md for visible chat formatting.
version: 1.14.0
author: Midas / Hermes Agent
license: MIT
tags:
  - stocks
  - discovery
  - gems
  - small-cap
  - mid-cap
  - asymmetric
  - undervalued
  - underfollowed
  - midas
related_skills:
  - research
  - financials
  - thesis
  - risk
  - earnings
  - updates
  - full
  - wl
---

# MIDAS Gems Command Prompt

## Purpose

`!gems` is MIDAS' asymmetric small/mid-cap discovery engine. Use it to find potentially overlooked, misunderstood, underfollowed, or mispriced public companies that may deserve deeper research.

This skill produces **research candidates only**. It does not make investment recommendations, build a full research memo, add tickers to the watchlist, give Buy/Sell/Hold ratings, give price targets, give position sizing, or provide trade-execution advice.

Detailed hidden-gem eligibility, evidence, scoring interaction, demotion, and no-clean-candidate rules live in `contracts/hidden-gems.md`.

## Registry Metadata

Command: `!gems`
Aliases: `None`
Category: `Stock Discovery`
Status: `Draft`
Skill Path: `skills/stock-analysis/gems/SKILL.md`
Output Path: `skills/stock-analysis/gems/OUTPUT.md`
Eval File: `evals/gems.eval.md`
Uses Classification: `Required`
Uses Scoring: `Required`
Uses Metrics: `Optional`
Writes Artifacts: `Yes`
Primary Global Rules: `GLOBAL.md, COMMAND_INTERFACE.md, SOURCES.md, CLASSIFICATIONS.md, SCORING.md, RERATING.md, METRICS.md, OUTPUT.md, ARTIFACTS.md`

## Intelligence Contract / Contract Authority

`contracts/hidden-gems.md` is the active command-local intelligence contract for `!gems`.

It owns:

* Source contract.
* Eligibility filters.
* Entity/security resolution gates.
* Promotion gates.
* Demotion/blocking rules.
* Hidden-Gem Fit discipline.
* Business / Financial Validation discipline.
* Variant View / Information Gap discipline.
* Rerating / post-rerate discipline.
* Social / hype / promotional-source limits.
* Evidence Confidence interaction.
* Hidden-Gem Overlay score interaction.
* Classification usage for `!gems`.
* Disconfirming-evidence handling.
* No-clean-candidate rule.

`SKILL.md` owns controller/workflow only:

* Command purpose.
* Input parsing.
* Standard input routing.
* Canonical no-write `-audit` routing.
* High-level workflow.
* References to command-local authority files.
* Command boundaries.

`SKILL.md` does not own detailed source hierarchy, scoring math, promotion gates, output templates, artifact path mechanics, or global rule definitions.

`OUTPUT.md` owns visible output shape, candidate-card fields, failure/no-candidate output, source-caveat display, score/confidence display, and saved/index display lines. `OUTPUT.md` does not own intelligence logic, ranking logic, or scoring calculation.

Artifact and index mechanics are governed by `references/artifact-index.md`, subject to `/home/jordan/.hermes/profiles/midas/rules/ARTIFACTS.md`. `!gems` must not mutate watchlists unless a separate approved watchlist command is explicitly run. Saved/updated/index claims remain allowed only when the write actually succeeded.

For intelligence logic, `contracts/hidden-gems.md` is the active authority. For artifact/index mechanics, `references/artifact-index.md` is the active command-local authority. For visible output and saved/index confirmation wording, `OUTPUT.md` is the active display authority.

This controller preserves standard `!gems` behavior, scoring discipline, promotion gates, artifact/index behavior, registry status, and eval expectations. Standard runs may write the approved `workspace/gems/...` artifacts and index when successful. Audit runs are no-write and do not create schemas, persisted proof packets, persisted source manifests, persisted evidence ledgers, fixture files, artifacts, or watchlist entries.

## Invocation Triggers

Use this skill when the user runs any of:

* `!gems`
* `!gems [theme, sector, industry, or opportunity type]`
* `!gems [theme] [subtheme]`
* `!gems -audit`
* `!gems [theme] -audit`
* `!gems [theme] / [subtheme] -audit`

Treat command names case-insensitively. Standard `!gems` supports broad, theme, and theme/subtheme inputs. Audit mode uses canonical single-dash `-audit`. Do not treat `--audit` as canonical; if the user invokes `--audit`, return: `Use -audit for !gems audit mode.`

Examples:

* `!gems`
* `!gems space`
* `!gems semiconductors`
* `!gems semiconductor equipment`
* `!gems semiconductors equipment`
* `!gems ai infrastructure`
* `!gems energy infrastructure`
* `!gems -audit`
* `!gems semiconductors -audit`
* `!gems semiconductors / equipment -audit`

## Authority Files

Apply these command-local and global authorities by reference. Do not duplicate their full rules inside `SKILL.md`.

* `contracts/hidden-gems.md` — active `!gems` intelligence authority for source contract, eligibility, entity/security resolution, promotion gates, demotion/blocking, scoring interaction, classification usage, disconfirming evidence, and no-clean-candidate behavior.
* `OUTPUT.md` — visible chat/output authority for candidate cards, score/confidence display, source/evidence caveats, failure/no-candidate output, visible saved/index confirmation wording, and final response shape.
* `references/artifact-index.md` — active `!gems` command-local artifact/index mechanics for artifact paths, theme/subtheme parsing, slug behavior, folder creation, duplicate/cross-theme handling, saved-artifact requirements, and `workspace/gems/index.md` behavior.
* `/home/jordan/.hermes/profiles/midas/rules/GLOBAL.md` — shared MIDAS operating rules.
* `/home/jordan/.hermes/profiles/midas/rules/SOURCES.md` — global source standards.
* `/home/jordan/.hermes/profiles/midas/rules/CLASSIFICATIONS.md` — approved setup classifications and modifiers.
* `/home/jordan/.hermes/profiles/midas/rules/SCORING.md` — global scoring, Evidence Confidence, Hidden-Gem Overlay, and score-cap standards.
* `/home/jordan/.hermes/profiles/midas/rules/RERATING.md` — global rerating, post-rerate, overextension, vertical-move, consolidation, market-absorption, valuation-reset, and price-action discipline standards.
* `/home/jordan/.hermes/profiles/midas/rules/METRICS.md` — metric definitions and calculation standards when market cap, price performance, valuation, liquidity, or financial metrics are used.
* `/home/jordan/.hermes/profiles/midas/rules/OUTPUT.md` — shared output standards inherited by `OUTPUT.md`.
* `/home/jordan/.hermes/profiles/midas/rules/ARTIFACTS.md` — global artifact standards inherited by `references/artifact-index.md`.

Do not create new reference, helper, methodology, theme-specific `.md`, schema, proof-packet, source-manifest, evidence-ledger, or fixture files unless the user explicitly asks.

## Command Modes

### Broad Mode

If the user runs `!gems`:

* MODE: Broad
* THEME: General
* SUBTHEME: None
* MAX_CANDIDATES: 5
* ARTIFACT_PATH: `workspace/gems/general.md`

Run a broad discovery scan across acceptable themes.

### Theme Mode

If the user runs `!gems [theme]`:

* MODE: Theme
* THEME: normalized theme
* SUBTHEME: General
* MAX_CANDIDATES: 5
* ARTIFACT_PATH: `workspace/gems/[theme]/general.md`

Run a focused discovery scan for that theme.

### Theme/Subtheme Mode

If the user runs `!gems [theme] [subtheme]` or `!gems [theme] / [subtheme]`:

* MODE: Theme/Subtheme
* THEME: normalized theme
* SUBTHEME: normalized subtheme
* MAX_CANDIDATES: 5
* ARTIFACT_PATH: `workspace/gems/[theme]/[subtheme].md`

Run a focused discovery scan for that theme/subtheme.

### Audit Mode

If the user runs an audit trigger, parse normal mode first, then set `AUDIT_MODE: true`:

* `!gems -audit` → MODE: Broad audit, THEME: General, SUBTHEME: None.
* `!gems [theme] -audit` → MODE: Theme audit, THEME: normalized theme, SUBTHEME: General.
* `!gems [theme] / [subtheme] -audit` → MODE: Theme/Subtheme audit, THEME: normalized theme, SUBTHEME: normalized subtheme.

Audit parsing must preserve existing normal broad/theme/theme-subtheme parsing. The canonical audit trigger is single-dash `-audit`. Do not silently normalize `--audit`; return the short correction `Use -audit for !gems audit mode.`

Audit mode uses the same intelligence authorities as standard mode, but all candidate discovery, source review, scoring, gate checks, and output-safety checks stay in memory and chat only.

## High-Level Workflow

1. Parse the command, identify broad/theme/theme-subtheme mode, audit status, theme, subtheme, max candidates, and the intended artifact path for standard runs.
2. If `--audit` appears, stop and return `Use -audit for !gems audit mode.`
3. If audit mode is active, verify no-write audit execution can be guaranteed before source gathering. If it cannot, stop with the blocked audit fallback below.
4. Resolve artifact path, theme aliases, slug behavior, duplicate/cross-theme handling, save semantics, and index mechanics through `references/artifact-index.md`, subject to global `ARTIFACTS.md`; in audit mode, resolve intended status only and do not create folders or write.
5. Build a public-company candidate universe appropriate to the requested mode and theme.
6. Apply `contracts/hidden-gems.md` for source authority, eligibility, entity/security resolution, promotion gates, demotion/blocking, Hidden-Gem Fit, Business / Financial Validation, Variant View / Information Gap, rerating discipline, social/hype limits, Evidence Confidence, Hidden-Gem Overlay score interaction, classification usage, disconfirming evidence, and no-clean-candidate behavior.
7. Use global `SOURCES.md`, `SCORING.md`, `CLASSIFICATIONS.md`, `RERATING.md`, `OUTPUT.md`, `ARTIFACTS.md`, and `METRICS.md` where their inherited standards apply.
8. For standard runs only: save the detailed artifact and update `workspace/gems/index.md` only when the command is actually run and the write succeeds. Preserve current artifact paths: `workspace/gems/general.md`, `workspace/gems/[theme]/general.md`, `workspace/gems/[theme]/[subtheme].md`, and `workspace/gems/index.md`.
9. For audit runs only: evaluate source quality, promotion gates, scoring / Evidence Confidence, candidate decisions, output safety, and artifact/index/watchlist status in memory; report no-write status in chat and make no saved/index confirmation claims.
10. Respond using `OUTPUT.md`. Do not paste full output templates in this controller.


## No-Write Audit Rule

In `!gems -audit` mode:

* Do not write artifacts.
* Do not update `workspace/gems/index.md`.
* Do not create folders.
* Do not mutate watchlists.
* Do not auto-run downstream commands.
* Do not create schemas.
* Do not create persisted proof packets.
* Do not create persisted source manifest files.
* Do not create persisted evidence ledger files.
* Do not create fixture files.
* Do not make `Saved to:` or `Updated index:` confirmation claims.

Audit mode may retrieve/read sources in memory, evaluate candidates in memory, and summarize source-contract, gate, scoring, candidate-decision, output-safety, and artifact/index/watchlist status in chat.

If no-write audit execution cannot be guaranteed, stop before source gathering and return a blocked audit result stating:

```md
# Gems Audit | Blocked

Unable to run audit safely.

Reason: no-write audit execution could not be guaranteed.

Status:
- no sources gathered
- no candidates promoted
- no artifacts written
- no index updated
- no watchlists modified
- no downstream commands run
```

Audit mode does not change standard `!gems` output, artifact/index write behavior, artifact paths, scoring formulas, promotion gates, registry status, candidate-card fields, or saved/index wording.

## Artifact / Index Boundary

`SKILL.md` preserves artifact behavior by reference only.

Use `references/artifact-index.md` plus `/home/jordan/.hermes/profiles/midas/rules/ARTIFACTS.md` for:

* `workspace/gems/general.md`
* `workspace/gems/[theme]/general.md`
* `workspace/gems/[theme]/[subtheme].md`
* `workspace/gems/index.md`
* theme/subtheme parsing
* slug behavior
* folder creation
* duplicate/cross-theme handling
* saved artifact requirements
* index update behavior
* artifact write mechanics

`references/artifact-index.md` owns `!gems` command-local artifact/index mechanics. It is subordinate to global `/home/jordan/.hermes/profiles/midas/rules/ARTIFACTS.md`. `OUTPUT.md` owns visible saved/index confirmation wording. `contracts/hidden-gems.md` owns intelligence logic.

Active command-local artifact/index mechanics route to `references/artifact-index.md`.

Do not change artifact paths, theme/subtheme parsing, slug behavior, folder creation behavior, duplicate/cross-theme handling, saved artifact requirements, index update behavior, write behavior, or legacy artifact handling from this controller. Do not claim `Saved to:` or `Updated index:` unless the write/update actually succeeded.

No artifacts, folders, index updates, or watchlist mutations happen in read-only, planning, validation, or other no-write contexts.

## Output Boundary

Use `/home/jordan/.hermes/profiles/midas/skills/stock-analysis/gems/OUTPUT.md` for visible output. That file owns chat shape, candidate-card fields, score/confidence display, source/evidence caveats, no-candidate/failure output, Best Next Command behavior, saved/index display lines, and no-recommendation wording.

This controller must not duplicate full output templates or change visible output format.

## Command Boundaries

Do not give Buy, Sell, or Hold ratings.

Do not give price targets.

Do not give position sizing.

Do not give direct trade execution advice.

Do not call candidates recommendations.

Do not treat social, crowding, promotional, influencer, or famous-investor signals as thesis proof.

Do not automatically add candidates to the MIDAS watchlist or modify `data/midas_watchlist.json`.

Do not run these commands unless the user explicitly asks:

* `!research`
* `!financials`
* `!thesis`
* `!thesis update`
* `!risk`
* `!earnings`
* `!updates`
* `!full`
* `!wl add`

It is okay to suggest the best next command when `OUTPUT.md` calls for it.

## Behavior Preservation

This controller cleanup preserves standard-mode behavior while removing the legacy support-folder architecture.

It does not:

* Change scoring formulas.
* Change promotion gates.
* Change artifact paths.
* Change theme/subtheme parsing.
* Change slug behavior.
* Change folder creation behavior.
* Change duplicate/cross-theme handling.
* Change saved artifact requirements.
* Change artifact/index behavior.
* Change output format.
* Change output wording for standard runs.
* Change registry status.
* Change normal eval expectations.
* Change standard artifact/index behavior.
* Create schemas, persisted proof packets, persisted source manifests, persisted evidence ledgers, or fixture files.
* Authorize watchlist mutation.
* Auto-run downstream commands.

Audit mode is the only no-write runtime verification path. It is additive and must not alter standard-mode behavior.

## Verification Checklist

Before finalizing a live `!gems` response, verify:

* Command mode was identified and parser behavior was preserved, including whether `-audit` is active.
* Theme/subtheme path was resolved through `references/artifact-index.md` and global `ARTIFACTS.md`; in audit mode, this remains no-write status only.
* `contracts/hidden-gems.md` was applied for intelligence logic.
* `OUTPUT.md` was applied for visible display.
* If no candidate passes the applicable gates, the response says no clean candidate was found rather than forcing a gem.
* No unapproved reference, helper, methodology, schema, proof-packet, source-manifest, evidence-ledger, fixture, or theme-specific file was created.
* No Buy/Sell/Hold rating, price target, position sizing, trade advice, recommendation framing, or social-proof-as-thesis language was included.
* No downstream command was run unless the user explicitly asked.
* No candidates were automatically added to the watchlist.
* Before claiming `Saved to:` or `Updated index:`, verify the artifact path exists and the index actually contains the new/updated row; do not rely on intended writes.
* For live `!gems` runs, verify `data/midas_watchlist.json` was not modified unless the user explicitly invoked a supported watchlist command.
