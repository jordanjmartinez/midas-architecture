# !financials Non-SEC and FPI Notes

This is command-local support for !financials. It does not replace GLOBAL.md, SOURCES.md, METRICS.md, OUTPUT.md, or ARTIFACTS.md.

Use this when the issuer does not map cleanly to SEC 10-K/10-Q filings, is a foreign private issuer, or has primary disclosure outside U.S. domestic forms.

## Identity and source basis

- Resolve legal issuer name, primary listing, reporting currency, exchange, and any secondary/OTC ticker before analysis.
- Do not pretend SEC 10-K/10-Q filings were reviewed when using non-SEC source equivalents.
- Normal Source Notes should identify source type, date, period/report date, and source basis.
- Raw URLs/accessions are optional and mostly internal unless audit, source-recovery, debug, ambiguity, or user request requires them.

## Foreign private issuers

- Annual financials usually come from Form 20-F or the issuer annual report.
- Interim results may come from Form 6-K exhibits, issuer releases, half-year reports, quarterly reports, or local exchange disclosures.
- Do not assume the primary 6-K document contains financial statements; inspect the filing index or issuer release for exhibits such as earnings releases, MD&A, operating results, and reconciliation tables.
- Label IFRS, local GAAP, or other reporting-standard basis when relevant.

## Non-SEC source equivalents

- Prefer issuer financial statements, annual reports, interim reports, MD&A, regulator filings, exchange disclosures, and official company financial disclosures.
- Company-hosted PDFs are acceptable when they are official issuer documents or linked from official issuer pages.
- If PDFs are not text-friendly, use bounded local extraction and state extraction/source limitations when relevant.
- Use secondary sources only for context, not as primary proof of financial-statement metrics.

## Currency and comparability

- Preserve reporting currency and units.
- Label currency conversions only when used, including source/as-of context.
- Avoid mixing IFRS/local GAAP metrics with U.S. GAAP-style interpretations without a caveat.
- Distinguish fiscal periods, interim periods, and trailing-period calculations.

## Source limitations

- Make missing 10-Q/10-K, PDF-only disclosure, limited segment detail, unavailable cash-flow tables, or non-U.S. disclosure cadence visible in Source Notes / What To Verify Next.
- If annual and interim reports use different formats or levels of detail, state the limitation rather than forcing comparability.
