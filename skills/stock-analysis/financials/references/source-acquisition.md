# !financials Source Acquisition Notes

This is command-local support for !financials. It does not replace GLOBAL.md, SOURCES.md, METRICS.md, OUTPUT.md, or ARTIFACTS.md.

Use this when gathering filing-backed financial-statement evidence for `!financials`.

## Source selection

- For U.S. SEC filers, resolve legal company name, ticker, exchange, and CIK before analysis.
- Prefer the latest relevant annual filing and latest interim filing for realized financial statements.
- For domestic issuers, this usually means Form 10-K plus Form 10-Q unless a newer company filing or earnings release supersedes specific disclosed items.
- Use earnings releases, Form 8-K exhibits, investor releases, or reconciliation tables when they provide newer income-statement, balance-sheet, guidance, or non-GAAP information.
- Keep cash-flow calculations anchored to the latest filed cash-flow statement unless the newer release includes a full cash-flow statement.
- Label timing mismatches when an earnings release updates revenue/margins/earnings but not CFO/FCF.

## SEC / EDGAR workflow

- SEC submissions JSON can identify recent filings, filing dates, report periods, accessions, and primary documents.
- SEC Company Facts / XBRL can support core reported totals such as revenue, net income/loss, cash flow, cash, assets, liabilities, shares, SBC, and repurchase concepts when available.
- Filing HTML is often needed for segment tables, revenue disaggregation, customer concentration, debt/liquidity notes, share-count footnotes, equity offerings, non-GAAP reconciliations, backlog/RPO, and MD&A drivers.
- If standard XBRL tags are sparse, do not stall. Fall back to bounded filing HTML/table extraction with clear filing/source labels.
- If table parsing fails, use bounded text extraction around distinctive headings or table keywords rather than saving a thin or incomplete report.
- If SEC responses are compressed, decompress before parsing instead of treating the fetch as failed.

## Source traceability

- Preserve source type, filing/release date, report period, and source basis internally while extracting evidence.
- Normal Source Notes do not require raw SEC URLs or accession numbers by default.
- Accession numbers and URLs may remain internal or appear in audit, source-recovery, or debug contexts when useful.
- If line citations are unavailable or would make the run unbounded, cite by filing/report name, date, period, and section/table in normal output.
- Do not require raw URLs in normal Source Notes unless ambiguity, source recovery, audit/debug context, or user request makes them useful.

## Temporary implementation aids

- Normal implementation may use temporary filing corpora or extracts as non-artifact implementation aids.
- Temporary aids are not schemas, proof packets, source manifests, evidence ledgers, workspace artifacts, or user-facing outputs.
- Do not preserve temporary aids unless the user explicitly asks and the destination is in scope.

## Audit no-write caveat

- `!financials [ticker] -audit` must not persist manifests, extracts, source dumps, ledgers, proof packets, schemas, artifacts, workspace files, or temp evidence files.
- Audit mode can inspect and summarize source availability in memory, but it must not write source-acquisition artifacts.
