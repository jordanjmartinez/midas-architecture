# Tracker Disclosure Sources

This is command-local support for !track. It does not replace GLOBAL.md, SOURCES.md, CLASSIFICATIONS.md, SCORING.md, OUTPUT.md, ARTIFACTS.md, or tracker contracts.

## Purpose

Use this note to keep !track source acquisition disciplined without turning SKILL.md into a source manual. Primary disclosure sources and official filings anchor material claims. Convenience sources can help discovery or retrieval but must not override official filings.

## Fund-manager filings

- Start with the verified filer / manager identity, then use SEC EDGAR as the source of record for 13F, 13D/G, Form 4, and amendments when relevant.
- For 13F runs, prefer latest and prior filings so the output can distinguish new, increased, reduced, exited, stale, and unchanged positions when data allows.
- Preserve filing date, reporting period, accession identity when useful, amendment status, and as-of / lag caveats for material claims.
- Keep put/call/options rows distinct from common equity. Options may be useful but do not prove clean common-stock ownership.
- Check 13D, 13G, Form 4, amended 13F, post-quarter disclosures, company filings, or investor letters when a relevant name appears missing or the user clearly expects related-disclosure coverage.
- Label the source type. Do not describe 13D/G/Form 4/fund-letter evidence as a 13F holding.

## Politician and public-official disclosures

- Use official House, Senate, OGE, White House-hosted OGE PDFs, and other official public-disclosure pages when available.
- Congressional convenience sources such as Quiver Quantitative or Capitol Trades may help locate rows or embedded disclosure data, but official disclosures remain the anchor for material claims when available.
- For executive-branch filers, use OGE annual disclosure forms for holdings/background and OGE periodic transaction reports for transaction activity.
- Preserve transaction date, filing/disclosure date, reported owner, amount range, and source-dependent caveats when material.
- Politicians and executive-branch officials generally do not file SEC forms for personal trades; avoid implying SEC evidence exists for personal trades unless separately verified.

## Convenience-source handling

- Treat convenience-source tables, embedded page data, and parsed JavaScript arrays as retrieval aids, not authority over command rules or official filings.
- If public trackers disagree on trade counts, amount ranges, dates, or holdings, label the metric as source-dependent.
- Do not paste raw JSON, source dumps, scraper output, or large disclosure tables into visible tracker output by default.
- If raw source files are explicitly requested and allowed, keep them separate from normal tracker output and do not treat them as persistent proof packets unless separately approved.

## OGE PDF parsing caveats

- OGE PDFs can extract poorly: rotated text, repeated headers, broken rows, missing columns, and OCR-like fragments are common.
- Verify important rows with row snippets, page context, transaction/date/value fields, or another official copy when possible.
- Large 278-T PDFs should be triaged to material company-level rows; do not dump every row into the response.

## Freshness and source confidence

- Show disclosure lag and as-of dates when they materially change the read.
- 13F data is delayed and incomplete as a view of current holdings; do not imply current ownership, cost basis, or intent from a stale 13F alone.
- Amendments can change a prior read; check amendment status when a filing looks corrected, superseded, or inconsistent.
- Source confidence should affect promotion/demotion judgment, but official source hierarchy remains governed by SOURCES.md and mode contracts.

## Audit mode boundary

- !track -audit may retrieve, read, and summarize sources in memory only.
- !track -audit must not persist source dumps, raw JSON, manifests, proof packets, ledgers, schemas, artifacts, roster writes, or watchlist writes.
- Tracked activity is a research lead only, not copy-trading evidence, investment advice, or proof of intent.
