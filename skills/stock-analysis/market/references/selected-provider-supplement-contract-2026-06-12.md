# `!market` Selected-Provider Supplement Contract — 2026-06-12

Use this reference when implementing or reviewing `!market full` / `!market expanded` enrichment after the Stage 2 rules/evals update.

## Contract

Supplements are allowed only after a quote provider has already returned a usable price and become the selected provider.

Approved supplement labels:

- `FMP: profile` — only after `FMP: quote` selects FMP.
- `FMP: stock-price-change` — only after `FMP: quote` selects FMP.
- `Finnhub: stock/metric` — only after `Finnhub: quote` selects Finnhub as fallback.

## Non-negotiables

- Supplement calls must not determine provider selection.
- Supplement failure must not make an otherwise usable quote unusable.
- Supplement failure must not trigger fallback to another provider.
- Do not call Finnhub supplements when FMP succeeds solely to enrich FMP snapshots.
- Do not call Alpha Vantage solely for supplemental fields.
- Compact `!market [ticker]` output must remain lean with `Source: [provider]` directly below `As of:`.

## Full / expanded display additions

Explicit full/expanded mode may add:

- `## Trend`
- `## Profile`

Allowed field families include price-performance windows, 50D/200D averages, price-vs-average percentages, average/relative volume, beta, sector, industry, country, IPO date, issuer type flags, and actively-trading status.

## Eval implications

Coverage should include:

- compact output unchanged despite new helper fields
- full mode shows new sections when fields exist
- FMP usable price prevents fallback even when supplements fail or omit fields
- Finnhub `stock/metric` is selected-provider-only
- supplement failures degrade gracefully with `Not available`, clean omission, or summarized non-material limitations

## Boundary

These fields are market-data context only. They must not become valuation conclusions, thesis evidence, setup classification, score, recommendation, price target, sizing, entry/exit, or trade advice.
