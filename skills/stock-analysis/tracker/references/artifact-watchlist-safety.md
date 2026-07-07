# Tracker Artifact and Watchlist Safety

This is command-local support for !track. It does not replace GLOBAL.md, SOURCES.md, CLASSIFICATIONS.md, SCORING.md, OUTPUT.md, ARTIFACTS.md, or tracker contracts.

## Purpose

Use this note to keep tracker roster, artifact, and no-write boundaries clean. Canonical paths and artifact standards remain governed by ARTIFACTS.md and SKILL.md.

## Roster vs stock watchlist

- Normal !track may update the tracker roster only if current SKILL behavior permits it.
- Tracker roster state is separate from the Midas stock watchlist.
- !track must not modify `data/midas_watchlist.json`.
- !track must not auto-add disclosed tickers to the Midas stock watchlist.
- A disclosed ticker is a research lead, not a watchlist entry, holding, or recommendation.

## Tracker artifacts

- Tracker artifacts are optional and should follow current command behavior plus ARTIFACTS.md.
- Do not claim a tracker artifact, profile, report, index, roster, or watchlist was saved or updated unless the write actually happened.
- Do not show saved paths in normal short tracker output unless the user asks, a save/export was requested and completed, or a write failure must be explained.
- Do not use ticker artifact paths for person/fund tracker reports unless a separate ticker command is explicitly creating a ticker artifact.
- Do not create backup, version, pointer, archive, source-cache, schema, proof-packet, evidence-ledger, or source-manifest files unless explicitly requested and approved.

## Raw source handling

- Use raw SEC/API JSON, downloaded filings, page HTML, PDFs, and parsed tables internally for evidence extraction only.
- Do not attach, upload, print, or display raw SEC/API JSON in normal tracker output.
- Do not persist raw JSON/source dumps unless the user explicitly requests debug/source-cache files and the requested path/scope is allowed.
- If a source needs citation, cite concise source names by default and raw links only when asked.

## Audit no-write boundary

- !track -audit writes nothing by default.
- !track -audit disables artifact writes, watchlist writes, tracker roster writes, workspace writes, downstream command auto-runs, and persistence claims.
- !track -audit may summarize verification state in memory, but must not create schemas, persisted proof packets, evidence ledgers, source manifests, artifacts, source dumps, archives, or pointer files.
- If no-write audit execution cannot be guaranteed, stop before gathering sources and report the block.

## Authority boundary

- References may remind future edits about artifact/watchlist safety, but they do not create new command behavior.
- ARTIFACTS.md owns canonical artifact paths and save/display standards.
- SKILL.md owns current tracker roster behavior.
- OUTPUT.md owns visible display and save-confirmation presentation.
