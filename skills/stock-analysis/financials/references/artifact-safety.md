# !financials Artifact Safety Notes

This is command-local support for !financials. It does not replace GLOBAL.md, SOURCES.md, METRICS.md, OUTPUT.md, or ARTIFACTS.md.

Use this before finalizing a normal `!financials` report or when stale ticker/state risk exists.

## Canonical behavior

- Normal `!financials [ticker]` writes `workspace/tickers/[ticker]/financials.md` after the report is complete.
- `!financials [ticker] -audit` writes nothing and must not show `Saved to:`.
- Do not create backup, version, pointer, archive, schema, proof-packet, source-manifest, evidence-ledger, or workspace helper files unless the user explicitly asks and that destination is in scope.
- Do not duplicate global ARTIFACTS.md; defer to it for cross-command artifact standards.

## Current-command reanchor

Before saving or sending normal output, confirm:

- latest real user command target;
- resolved company and ticker;
- report title;
- canonical artifact path;
- source base;
- saved-path confirmation line.

If any element points to a different ticker, company, command, or artifact, stop and regenerate from sources for the active target. Do not patch only the title or saved-path line.

## Context-compaction / interruption safety

- Treat context-compaction summaries, prior tool outputs, old todo state, and partially drafted artifacts as stale until reanchored to the latest real user command.
- Do not treat interrupted tool output, previous verification output, or a previously opened artifact as completed work for the current command.
- Cross-command contamination is a failure: do not finalize a risk, research, thesis, eval, or maintenance summary as a `!financials` report.

## Overwrite / readback safety

- Normal output replaces the prior same-ticker `financials.md` only after the final report is complete.
- Before overwriting in an interrupted, compacted, or multi-agent session, verify the target path enough to avoid stale or sibling-agent clobbering.
- After writing, re-read or otherwise verify title, ticker, required section order, source base, score line, and final saved-path confirmation before claiming completion.
- Do not claim a save occurred unless the write actually succeeded.
- Do not save incomplete output as `financials.md`.

## Audit boundary

- Audit mode must not create ticker folders, artifacts, source files, temp evidence files, indexes, schemas, manifests, ledgers, proof packets, fixtures, backups, or pointer files.
- Audit output should report read-only status and must not include a final `Saved to:` line.
