# !risk Source Retrieval

This is command-local support for !risk. It does not replace GLOBAL.md, SOURCES.md, METRICS.md, OUTPUT.md, ARTIFACTS.md, CLASSIFICATIONS.md, or SCORING.md.

Use this when gathering sources for a bounded filing-backed company risk assessment. SOURCES.md remains the source hierarchy authority; this file only lists recurring !risk retrieval cues and no-write pitfalls.

## Source selection

- Resolve the issuer first: legal name, ticker, exchange, CIK or non-U.S. identifier when available.
- For SEC filers, start with the latest annual filing and latest interim filing when available.
- Review material subsequent filings only when they affect risk: 8-Ks, earnings releases, acquisition or financing filings, restructuring disclosures, credit agreements, covenant amendments, legal/regulatory updates, going-concern language, auditor/restatement items, and material contract exhibits.
- For non-SEC issuers or FPIs, use annual reports, interim reports, 20-F/6-K equivalents, exchange filings, regulator filings, and official company disclosures. State source limitations when disclosure is not comparable to U.S. SEC filers.
- Existing same-ticker Midas artifacts may help context and routing, but primary filings and official disclosures remain authoritative for material risk claims.

## Targeted risk retrieval cues

Prefer targeted source extraction over full filing dumps. Risk-relevant areas often include:

- Risk Factors.
- MD&A / liquidity and capital resources.
- Notes on debt, credit facilities, maturities, covenants, off-balance-sheet obligations, and guarantees.
- Legal proceedings, contingencies, investigations, sanctions, compliance, licensing, and regulatory matters.
- Revenue disaggregation, concentration of revenue or credit risk, major customers, suppliers, channels, geographies, and counterparties.
- Going-concern, auditor, restatement, internal-control, impairment, restructuring, acquisition, financing, or subsequent-event disclosures.
- Sector-specific operating metrics when they affect risk, such as backlog/RPO, churn/retention, funded customers, platform assets, credit losses, custody balances, or rate sensitivity.

## Source freshness and limits

- Preserve filing/source type, filing or source date, report period/date, and source basis in working notes and Source Notes when relevant.
- If a metric or disclosure is stale, unavailable, not disclosed, or not comparable, say so rather than filling the gap with inference.
- Earnings-release or furnished 8-K metrics can be useful but should be labeled as unaudited/furnished context when the audited annual filing is not yet available.
- Normal Source Notes do not require raw SEC URLs or accession numbers by default.
- Accession numbers and URLs may remain internal, or appear in audit, source-recovery, or debug contexts when useful.

## Audit and implementation boundary

- Normal implementation may use temporary filing corpora or extracts as non-artifact implementation aids.
- Normal output should not expose raw filing dumps, tool logs, or long excerpt blocks.
- !risk -audit must not persist manifests, extracts, source dumps, ledgers, proof packets, schemas, artifacts, workspace files, temp evidence files, validation logs, or runtime smoke outputs.
- If no-write cannot be guaranteed in audit mode, stop before retrieval and report the blocker under the audit contract.
