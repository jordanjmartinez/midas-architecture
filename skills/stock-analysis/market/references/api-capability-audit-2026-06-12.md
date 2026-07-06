# `!market` API Capability Audit — 2026-06-12

Use this reference when deciding whether to expand the MIDAS `!market` helper/output beyond the current compact snapshot.

## Scope

Read-only provider capability probe using `HOOD` as the sample ticker. No artifacts/watchlist mutations; no API keys printed. Provider calls were made only to inspect available fields and shape, not to change command behavior.

Configured provider keys observed in the runtime environment:

- `FMP_API_KEY`: present
- `FINNHUB_API_KEY`: present
- `ALPHA_API_KEY`: present

## Existing `!market` Fields

The current helper already supports:

- price
- market cap
- currency
- dollar change
- volume
- exchange
- previous close
- open
- day high / low
- 52-week high / low
- shares outstanding when available
- average volume / relative volume when available
- provider/as-of/source metadata for debug/failure paths

Compact success must remain lean and end at `Source: [provider]`.

## Low-Risk Fix

### FMP percent change parsing

FMP `quote` returned `changePercentage`, but the helper looked for `changesPercentage`; this caused `change_percentage: null` despite the provider returning a value.

Future helper update should parse both:

- `changePercentage`
- `changesPercentage`

This improves existing compact `Change: $ / %` output without adding an endpoint.

## Useful Full/Expanded-Mode Additions

### FMP `quote`

Useful fields observed:

- `priceAvg50`
- `priceAvg200`
- `timestamp`
- `changePercentage`

Recommended use: full/expanded trend context only. Example fields:

- 50D average
- 200D average
- price vs 50D average
- price vs 200D average

### FMP `profile`

Useful fields observed:

- `averageVolume`
- `beta`
- `range`
- `exchangeFullName`
- `industry`
- `sector`
- `country`
- `ipoDate`
- `isEtf`
- `isAdr`
- `isFund`
- `isActivelyTrading`

Recommended use: full/expanded profile and liquidity context. If added, treat as an FMP-side supplement only after FMP quote is selected; do not call fallback providers just to enrich missing profile fields.

### FMP `stock-price-change`

Useful fields observed:

- `5D`
- `1M`
- `3M`
- `6M`
- `ytd`
- `1Y`

Recommended use: full/expanded price-performance context. Label as price action only, not business quality or thesis evidence.

### Finnhub `stock/metric`

Useful fallback-provider fields observed:

- 10-day average trading volume
- 3-month average trading volume
- 52-week high / low and dates
- beta
- market capitalization
- 5D, MTD, YTD, 13-week, 26-week, and 52-week returns
- relative performance vs S&P 500 over several windows

Recommended use: only when Finnhub is the selected fallback provider. Do not call Finnhub when FMP succeeds solely to enrich fields.

## Fields Not Recommended For `!market`

Avoid adding these to compact/default `!market`:

- analyst recommendations / ratings counts — too close to recommendation/sentiment framing
- earnings surprise — better for `!earnings`
- broad TTM valuation/profitability ratios — better for `!financials`, `!full`, or valuation sections with period labels and filing cross-checks
- enterprise value endpoint by default — sample may be dated and mixes filing-derived inputs; use only with clear as-of labels
- historical EOD payloads by default — useful for calculations but too heavy for a thin snapshot

## Recommended Upgrade Path

1. Fix FMP percent-change parsing in the existing helper.
2. Keep compact mode unchanged.
3. For explicit full/expanded mode, consider adding:
   - price-performance windows
   - 50D / 200D averages and price-vs-average calculations
   - average volume / relative volume
   - beta
   - sector / industry / issuer-type flags
4. Update `rules/MARKET_DATA.md`, `tools/market_data_snapshot.py`, `OUTPUT.md`, and evals together before changing behavior.

## Guardrails

- No Buy/Sell/Hold, price target, sizing, entry, exit, or trade advice.
- Market data remains Tier 2 market context.
- Compact success remains terse and stops after `Source: [provider]`.
- New endpoints must be selected-provider supplements, not field-level fallback enrichment.
- Provider detail belongs in debug/source/raw or failure paths, not compact success.
