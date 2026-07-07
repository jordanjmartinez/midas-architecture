# `!market` Full Mode Display Contract Notes

Session learning captured after implementing explicit `!market [ticker] full` / `expanded` support.

## Durable User Preferences

- Default `!market [ticker]` output is accepted and should remain clean/compact.
- Do not reintroduce provider metadata blocks by default on normal success.
- Default title should include company name when helper output includes `company_name`:
  - `📈 [Display Name] ($[TICKER]) | Market Snapshot`
  - fallback: `📈 $[TICKER] | Market Snapshot`
- Full mode must be explicit only:
  - `!market [ticker] full`
  - `!market [ticker] expanded`

## Full Mode Boundaries

Full mode remains market-data-only. It must not become:

- research
- valuation conclusion
- thesis
- scoring
- setup classification
- recommendation
- price target
- sizing
- trade advice

Do not include valuation multiples by default unless denominator inputs are cleanly sourced and labeled under `METRICS.md`.

## Provider/Fallback Pitfall

Expanded fields must not create field-level enrichment.

Provider behavior must remain:

1. FMP first.
2. If FMP returns usable price, stop even if expanded/full-mode fields are missing.
3. Finnhub only if FMP fails or returns no usable price.
4. Alpha Vantage only if FMP and Finnhub fail or return no usable price.

Missing full-mode fields should render as `Not available` or be omitted cleanly.

## Full Mode Sections

Expected sections:

1. Header
   - `[Display Name] ($[TICKER]) Full Market Snapshot`
   - human-readable as-of timestamp
   - `Source: [provider]` directly below `As of:`
2. Profile
   - Sector
   - Industry
   - Country
   - IPO Date
   - Issuer Type
   - Actively Trading
3. Price Action
   - Market Cap
   - Price
   - Change: dollar / percent
   - Previous Close
   - Open
   - Day High / Low
   - 52-Week High / Low
4. Liquidity
   - Volume
   - Average Volume
   - Relative Volume only when both volume and average volume are available
5. Trend
   - Price-performance windows
   - 50D/200D averages and price vs averages
   - Beta

Normal successful full/expanded output must not include a trailing `## Source / Limitations` section, `Fallbacks Used:`, or routine `Limitations:` label. Failure/debug/raw paths may still show sanitized provider details.

## Helper Fields Added For Full Mode

- `previous_close`
- `open`
- `day_high`
- `day_low`
- `week_52_high`
- `week_52_low`
- `average_volume`
- `relative_volume`

## Eval Coverage Added

Full mode eval coverage should include:

- full mode renders `Full Market Snapshot`
- fallback logic unchanged
- FMP usable price stops fallback even if expanded fields are missing
- missing full-mode fields handled cleanly
- relative volume only when both inputs exist
- no score/classification/recommendation/price target/sizing/trade instruction
- no artifacts written
- raw/debug/source output remains explicit only
