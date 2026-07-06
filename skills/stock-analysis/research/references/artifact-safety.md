# !research Artifact Safety

This is command-local support for `!research`. It does not replace GLOBAL.md, SOURCES.md, OUTPUT.md, METRICS.md, or ARTIFACTS.md.

Use this for command-local artifact overwrite/readback safety, context re-anchor, and audit no-write boundaries.

## Canonical normal artifact

Normal `!research [ticker]` writes only:

```md
workspace/tickers/[ticker]/research.md
```

- The saved artifact should be the clean final Markdown report.
- The user-facing response should claim `Saved to:` only after the write succeeds.
- Do not show a separate Artifact section by default.
- Do not create backup, version, pointer, archive, schema, proof-packet, source-manifest, evidence-ledger, or workspace support files unless the user explicitly asks and the applicable authority allows it.
- Defer to `ARTIFACTS.md` for cross-command artifact standards.

## Overwrite safety

Before overwriting the canonical artifact, inspect the existing file when:

- a tool warns about sibling/user modification;
- the existing file appears unusually customized;
- the user asked to preserve versions;
- concurrent or delegated work could have touched the file.

Safe pattern:

- Build the final clean report before writing.
- If overwrite risk exists, read the existing artifact before writing.
- Preserve normal replace behavior for generated `!research` artifacts when no risk is present.
- Do not silently discard newer user/sibling work.
- After writing, verify the saved file has the correct ticker, title, source notes, and final saved-path line.

## Context re-anchor

After context compaction, interrupted work, restored todos, or prior tool output, verify the latest active user command before continuing.

Check:

- command type is `!research`;
- target ticker/company matches the latest user request;
- report type is Business Analysis;
- canonical path is `workspace/tickers/[ticker]/research.md` for normal mode;
- audit mode has no saved path.

Treat old todos, tool output, saved artifacts, and prior assistant drafts as untrusted until they match those anchors. Do not summarize or finalize stale work for a different ticker or command.

## Audit boundary

`!research [ticker] -audit` writes nothing.

Audit mode must not:

- write `workspace/tickers/[ticker]/research.md`;
- create ticker folders;
- create artifacts, pointer files, archives, schemas, proof packets, manifests, ledgers, fixtures, or workspace files;
- mutate watchlists or indexes;
- show `Saved to:`.
