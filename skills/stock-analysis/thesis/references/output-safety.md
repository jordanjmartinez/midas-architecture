# !thesis Output Safety Support

This is command-local support for !thesis. It does not replace GLOBAL.md, SOURCES.md, METRICS.md, OUTPUT.md, ARTIFACTS.md, CLASSIFICATIONS.md, SCORING.md, or RERATING.md.

## Purpose

Use this reference to avoid recurring output bloat, stale structures, false saved claims, and artifact drift.

OUTPUT.md owns visible display templates and section order. ARTIFACTS.md owns global artifact standards.

## Readability hygiene

- Lead with thesis synthesis, not methodology.
- Avoid field dumps where every section becomes repeated labels.
- Avoid metric dumps; `Financial Support` should include thesis-relevant metrics only and should not become a mini `!financials` report.
- Avoid caveat overload; source limitations should be clear but concise.
- Avoid Telegram-unfriendly long bullets that combine multiple ideas into one line.
- Avoid repeating the same risk, concentration issue, valuation caveat, or cash-flow point in every section unless each mention adds a distinct read-through.
- Do not provide a receipt-only response when the user requested a normal thesis memo.

## Stale structures not active by default

Do not use these as normal-output requirements:

- old Full-mode structures,
- Evidence Ledger,
- Pillar Evidence Audit,
- Bull / Base / Bear as a default slash heading,
- Monitoring Dashboard,
- raw source dumps,
- old output templates,
- old section names from historical reference notes.

OUTPUT.md remains the authority for current headings.

## Artifact and saved-path safety

Normal `!thesis [ticker]` writes only:

`workspace/tickers/[ticker]/thesis.md`

`!thesis update [ticker]` writes the same `thesis.md` only after loading the existing baseline and completing the refresh.

Do not create by default:

- `thesis.compact.md`,
- `thesis-update.md`,
- timestamped history,
- backup files,
- version files,
- pointer files,
- archive files,
- source manifests,
- evidence ledgers,
- proof packets,
- schemas,
- fixture files.

Do not create backup, version, pointer, or archive files unless the user explicitly asks.

Show `Saved to:` only after the intended write succeeds and has been verified. Do not make false saved claims.

## Audit no-write boundary

`!thesis [ticker] -audit` and `!thesis update [ticker] -audit` write nothing and must not show `Saved to:`.

Audit mode must not create folders, artifacts, temp evidence files, source dumps, validation logs, manifests, ledgers, proof packets, schemas, fixture files, watchlist changes, index updates, or downstream command outputs.

If no-write behavior cannot be guaranteed, stop before source gathering and return the blocked audit fallback from SKILL.md / OUTPUT.md.
