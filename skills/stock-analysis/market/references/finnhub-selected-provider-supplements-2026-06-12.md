# Stage 5 Finnhub Selected-Provider Supplements — 2026-06-12

Use this reference when reviewing or extending the `!market full` / `expanded` Finnhub fallback path.

## What Stage 5 adds

When FMP fails or returns no usable price and Finnhub quote becomes the selected provider, the helper may enrich the returned snapshot with Finnhub-side supplements:

- `Finnhub: stock/profile2` for selected-provider company/profile context already used by the fallback path.
- `Finnhub: stock/metric` for selected-provider market-data context.

The supplement call happens only after Finnhub `quote` has returned a usable price. It must not determine provider selection.

## Fields mapped from `stock/metric`

The Stage 5 implementation maps available fields such as:

- `52WeekHigh` / `52WeekLow` → 52-week range
- `10DayAverageTradingVolume` or `3MonthAverageTradingVolume` → average volume
- `beta` → beta
- `50DayMovingAverage` / `200DayMovingAverage` when available → moving averages
- `5DayPriceReturnDaily`, `13WeekPriceReturnDaily`, `26WeekPriceReturnDaily`, `yearToDatePriceReturnDaily`, `52WeekPriceReturnDaily` → selected performance windows

It also derives price-vs-average percentages when both price and moving average are available.

## Guardrails

- Do not call Finnhub `stock/metric` when FMP succeeds.
- Do not call Alpha Vantage because a Finnhub supplement failed or omitted fields.
- Supplement failure must not make an otherwise usable Finnhub quote unusable.
- Compact render must remain unchanged and end at `Source: Finnhub` for a successful Finnhub fallback.
- Full/expanded render may display missing supplement fields as `Not available`.
- Keep output market-data-only: no valuation conclusion, score, classification, recommendation, price target, sizing, entry/exit, or trade advice.
- Endpoint labels must remain labels only; do not expose raw credential-bearing URLs.

## Validation pattern

Mock the provider function so that:

1. FMP fails.
2. Finnhub quote succeeds.
3. Finnhub profile and metric succeed.
4. Alpha Vantage would raise if called.

Then assert:

- payload provider is `Finnhub`
- `fallbacks_used` includes `Finnhub`
- `provider_endpoints["Finnhub"]` includes `Finnhub: stock/metric`
- full render includes the mapped metric values
- compact render lacks full sections and ends at `Source: Finnhub`

Also test metric failure: the payload should still be `ok: true`, full render should degrade cleanly, and Alpha Vantage should not be called.
