# !financials Metric Quality Notes

This is command-local support for !financials. It does not replace GLOBAL.md, SOURCES.md, METRICS.md, OUTPUT.md, or ARTIFACTS.md.

Use this for financial-statement quality checks inside `!financials`.

## Authority boundary

- METRICS.md owns metric definitions and metric-labeling discipline.
- This file is command-local support for financial-statement quality checks only.
- Do not create a new scoring formula.
- Do not create a new metric framework.
- Do not treat Financial Quality Score as Global Research Score.

## Labeling checks

- Label material metrics as reported, adjusted, calculated, or guided when relevant.
- Distinguish GAAP from non-GAAP.
- Identify company-defined metrics separately from MIDAS-calculated metrics.
- Preserve period, unit, currency, source period, and source basis where material.
- If a metric is unavailable, stale, not disclosed, not meaningful, or not calculable, say so.

## Non-GAAP / adjustment quality

- Check whether non-GAAP metrics are reconciled.
- Flag recurring, aggressive, changing, poorly reconciled, or central-to-thesis adjustments.
- Watch SBC add-backs, restructuring adjustments, acquisition-related adjustments, amortization exclusions, fair-value adjustments, and one-time labels that recur.
- Do not treat non-GAAP as equivalent to GAAP.

## Cash-flow quality

- State the FCF convention used and defer formulas to METRICS.md.
- Separate CFO from FCF and separate filing-based cash flow from company-defined FCF.
- Do not calculate FCF CAGR when FCF crosses zero, is negative, or is not meaningful; explain the trend instead.
- For brokerage, custody, clearing, fintech, banks, insurers, or other balance-sheet-heavy platforms, caveat CFO/FCF when client cash, segregated cash, securities borrowed/loaned, user payables, receivables, deposits, or other balance-sheet flows distort operating cash flow.
- Use wording like: filing-based FCF is not clean owner earnings when client or segregated-cash movements materially affect CFO.

## Capital intensity / dilution checks

- For capex-heavy or infrastructure-dependent businesses, compare operating cash flow with capex needs and explain whether growth appears self-funding.
- Make depreciation, leases, convertibles, capitalized software, asset impairments, and project timing visible when material.
- Track share count, SBC, warrants, converts, ATM programs, offerings, preferred stock, and post-period issuance when material.
- Treat equity-funded liquidity as real but lower-quality than internally generated financial strength.

## Valuation boundary

- Do not include PEG as a default metric.
- Do not present unsupported cheap/expensive/reasonable/fair-value conclusions.
- If market-data-derived valuation is used, keep it separate from filing-backed financial-statement conclusions and follow MARKET_DATA.md and METRICS.md.
