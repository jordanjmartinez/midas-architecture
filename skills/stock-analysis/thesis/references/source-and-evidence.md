# !thesis Source and Evidence Support

This is command-local support for !thesis. It does not replace GLOBAL.md, SOURCES.md, METRICS.md, OUTPUT.md, ARTIFACTS.md, CLASSIFICATIONS.md, SCORING.md, or RERATING.md.

## Purpose

Use this reference to keep `!thesis` source work filing-first, concise, and artifact-safe without turning SKILL.md into a source playbook.

## Source retrieval support

- Start by resolving the issuer: legal company name, ticker, exchange, CIK or non-U.S. filing identifier when available, and whether it is an SEC filer.
- For SEC filers, normally anchor the thesis in the latest relevant annual filing and latest interim filing, usually Form 10-K and Form 10-Q.
- Review material later disclosures when they affect thesis pillars, catalysts, risks, thesis breakers, update direction, source freshness, valuation setup, or rerating context:
  - Form 8-K,
  - earnings release,
  - investor presentation,
  - transcript,
  - acquisition filing,
  - financing or debt filing,
  - material company release.
- For non-SEC filers, use annual reports, interim reports, exchange filings, regulator filings, and official company disclosures as primary-source equivalents.

SOURCES.md owns source hierarchy, source confidence, freshness, amendment handling, and conflict handling.

## Workspace artifacts

- Same-ticker workspace artifacts may be read as secondary synthesis inputs when useful:
  - `research.md`,
  - `financials.md`,
  - `risk.md`,
  - `earnings.md`,
  - `updates.md`,
  - `full.md`.
- Workspace artifacts do not replace primary-source review.
- If a workspace artifact conflicts with primary disclosures, primary disclosures win unless the artifact identifies a newer primary source that must be checked.
- Do not create missing workspace artifacts while running `!thesis` unless the user explicitly asks.

## Source freshness and not-disclosed handling

- State when the source base is stale, incomplete, unaudited, limited, or not directly comparable.
- If a material thesis fact is not disclosed, say it is not disclosed rather than inferring it as fact.
- Separate reported facts, management claims, Midas interpretation, and assumptions.
- Management TAM, targets, guidance, or long-term goals are claims or assumptions until supported by reported results or other primary evidence.

## Source Notes discipline

Normal Source Notes should stay concise.

Preferred normal format:

- `[Filing type] — filed [date]; period ended [date]; used for [source basis].`
- `[Company release / earnings release] — dated [date]; used for [source basis].`
- `[Investor presentation] — dated [date]; used for [source basis], if material.`
- `[Existing workspace artifact] — dated [date or unknown]; used as secondary synthesis input only, if used.`

Normal Source Notes do not require raw SEC URLs or accession numbers by default. Accession numbers and URLs may remain internal or appear in audit, source-recovery, debug, or disambiguation contexts when useful.

## Temporary implementation aids

- Normal implementation may use temporary filing corpora, line-numbered extracts, or source snippets as non-artifact aids for reading and citation recovery.
- These aids are not durable thesis artifacts and should not be saved in ticker workspaces as command output.
- The final saved thesis should be clean Markdown only.

## Audit no-write caveat

`!thesis -audit` and `!thesis update -audit` must not persist manifests, extracts, source dumps, ledgers, proof packets, schemas, artifacts, workspace files, temp evidence files, validation logs, or runtime smoke outputs.

Audit mode may read or retrieve sources in memory only when no-write behavior is guaranteed.
