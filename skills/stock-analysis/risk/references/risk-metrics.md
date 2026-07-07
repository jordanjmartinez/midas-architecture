# !risk Metric Interpretation

This is command-local support for !risk. It does not replace GLOBAL.md, SOURCES.md, METRICS.md, OUTPUT.md, ARTIFACTS.md, CLASSIFICATIONS.md, or SCORING.md.

Use this when metrics sharpen a company risk assessment. METRICS.md owns metric definitions, formulas, period conventions, labeling, GAAP/non-GAAP discipline, and calculation standards. This file is only command-local support for interpreting risk-relevant metrics.

## Authority boundary

- Do not define local FCF, net debt, leverage, valuation, price-performance, dilution, or coverage formulas here.
- Do not create a new risk scoring formula or metric framework.
- Do not produce a Global Research Score by default.
- Do not turn !risk into !financials; use only the metrics needed to understand risk severity, evidence gaps, and monitors.

## Risk-relevant metric areas

Use metrics when available and material, especially for:

- Liquidity: cash, equivalents, restricted cash, revolver availability, regulatory capital, collateral, debt maturities, covenant headroom, or financing access.
- Cash flow: CFO, FCF, capex, working-capital swings, cash burn, cash runway, margin pressure, profitability, and cash-conversion quality.
- Capital structure: debt, converts, preferred equity, warrants, ATM programs, SBC, share count, dilution, refinancing needs, and maturity walls.
- Concentration: customers, suppliers, counterparties, channels, products, geographies, segments, platforms, or revenue mix.
- Operating visibility: backlog, RPO, book-to-bill, retention, churn, utilization, capacity, order trends, deposits, assets, subscribers, or sector-specific KPIs.
- Financial-platform risks: client balances, segregated assets, securities borrowed/loaned, credit losses, receivables, custody exposure, rate sensitivity, and market-maker or liquidity-provider dependence.

## Labeling discipline

- Preserve period, source, unit, currency, and GAAP/non-GAAP status when relevant.
- Label metrics as reported, adjusted, company-defined, or Midas-calculated when applicable.
- State when a metric is stale, unavailable, not disclosed, not meaningful, or not comparable.
- Avoid metric dumps. Include the metric because it changes risk understanding, not because it is available.

## Market and rerating context

- Market data and valuation/rerating context are not default !risk sections.
- Use market data only when explicitly requested or materially needed to frame risk, and label provider/source and as-of time.
- Do not use market data to prove filing-backed business, revenue, margin, cash-flow, debt, dilution, customer concentration, regulatory, legal, management, or thesis-validity claims.
- Do not create price targets, cheap/expensive conclusions, valuation models, or trading setup analysis.
- If market data is unavailable, stale, incomplete, or plan-limited, say that market-data-based risk was not assessed and continue with filing-backed risk work when possible.
