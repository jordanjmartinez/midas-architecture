# `!market` Output Contract

Status: Active
Command: `!market`
Skill: `skills/stock-analysis/market/SKILL.md`
Eval: `evals/market.eval.md`
Registry: `docs/COMMAND_REGISTRY.md`
Writes Artifacts: No

This file defines the user-facing display contract for:

```md
!market [ticker]
```

`!market` is a thin utility command. It displays the result from the canonical helper and does not add separate research, scoring, classification, recommendation, or artifact logic.

This output contract must follow `/home/jordan/.hermes/profiles/midas/rules/MARKET_DATA.md`. If this file conflicts with `MARKET_DATA.md`, `MARKET_DATA.md` controls market-data behavior.

## Default Output Mode

Supported normal output:

- Standard Market Snapshot

Unsupported as normal market snapshot modes:

- Compact
- Full
- Deep

Former mode/style words such as `compact`, `quick`, `brief`, `short`, `summary`, `concise`, `full`, `expanded`, `detailed`, `deep`, `deep-dive`, and `deepdive` must not select separate snapshot layouts. If such words appear with a ticker, still return the same Standard Market Snapshot unless the user is clearly requesting explicit raw/debug output.

Raw/debug JSON is allowed only when explicitly requested for diagnostics. Raw/debug is not a normal market snapshot mode.

The response should be readable in Telegram/terminal and should not dump raw API JSON unless the user explicitly requests raw/debug output.

## Required Standard Market Snapshot Shape

Normal successful output must use this shape:

```md
[TICKER] | [Company Name] Market Snapshot
As of: [human-readable timestamp, e.g. Jun 5, 2026, 1:36 AM ET]
Source: [provider]

## Profile

Sector: [sector or Not available]
Industry: [industry or Not available]
Country: [country or Not available]
Exchange: [exchange or Not available]
IPO Date: [ipo_date or Not available]
Issuer Type: [Common stock / ETF / ADR / Fund / Not available]
Actively Trading: [Yes / No / Not available]

## Price Action

Market Cap: [market_cap or Not available]
Price: [price]
Change: [dollar_change] / [percent_change]
Previous Close: [previous_close or Not available]
Open: [open or Not available]
Day High: [day_high or Not available]
Day Low: [day_low or Not available]
52-Week High: [week_52_high or Not available]
52-Week Low: [week_52_low or Not available]

## Liquidity

Volume: [volume or Not available]
Average Volume: [average_volume or Not available]
Relative Volume: [relative_volume or Not available]

## Trend

5D Performance: [performance_5d_percentage or Not available]
1M Performance: [performance_1m_percentage or Not available]
3M Performance: [performance_3m_percentage or Not available]
6M Performance: [performance_6m_percentage or Not available]
YTD Performance: [performance_ytd_percentage or Not available]
1Y Performance: [performance_1y_percentage or Not available]
50D Avg: [price_avg_50 or Not available]
200D Avg: [price_avg_200 or Not available]
Price vs 50D Avg: [price_vs_50d_avg_percentage or Not available]
Price vs 200D Avg: [price_vs_200d_avg_percentage or Not available]
Beta: [beta or Not available]
```

Do not use `Full Market Snapshot` in the title. The richer former full-style layout is now the Standard Market Snapshot.

## Title Rules

- If helper output includes `company_name`, use `[TICKER] | [Company Name] Market Snapshot`.
- If helper output does not include `company_name`, use `[TICKER] | Market Snapshot`.
- Do not include `!market` in the title.
- Do not use an em dash in the title.
- Do not include `Full` in the title.

## Timestamp / Source Rules

Every normal successful response must show:

- ticker and company name in the title when `company_name` is available
- human-readable as-of timestamp
- one simple source line directly below `As of:`: `Source: [provider]`

Render `as_of` as a human-readable timestamp, preferably `Mon D, YYYY, H:MM AM/PM ET` when the helper timezone is `America/New_York`.

Preserve helper-provided timestamp semantics; this is a rendering rule only.

## Metric Display Rules

Follow `/home/jordan/.hermes/profiles/midas/rules/METRICS.md` for metric labels, units, source/as-of discipline, calculated fields, and stale-data handling.

Preserve:

- metric name
- provider/source
- as-of date/time/timezone
- currency, unit, percent, and volume formatting
- calculated-ratio labeling when relevant
- no false precision
- no stale market data presented as current

Important fields include price, market cap, change amount and percent, volume, average volume, relative volume, 52-week high/low, 50D/200D averages, price vs moving averages, price-performance windows, beta, exchange, actively trading, IPO date, sector, industry, and country.

`Relative Volume`, `Price vs 50D Avg`, and `Price vs 200D Avg` are calculated context fields when helper-derived. Display them as labeled context, not as thesis proof.

## Provider / Fallback Display Rules

- `provider` means the provider used for the returned snapshot.
- `primary_provider` is the first provider in the hierarchy that returned usable price.
- `fallbacks_used` should list provider-level fallbacks tried because prior providers failed or returned no usable price.
- `fallbacks_used` is not a field-level enrichment log.
- `provider_errors` must be sanitized.
- `provider_endpoints` should be endpoint labels, not raw URLs with query parameters.
- Normal successful output should collapse selected-provider metadata to one line directly below `As of:`: `Source: [provider]`.

Do not show these fields by default on normal success:

- `Provider`
- `Primary provider`
- `Fallbacks used`
- `Provider errors`
- `Provider endpoints`
- `Source fields`
- `Provider note`

Show fallback details, provider errors, provider endpoints, source fields, provider notes, or raw helper JSON only when:

- the command fails
- the user explicitly asks for source, debug, or raw output

Do not show raw URLs in normal output.

## Selected-Provider Supplement Rules

Use only fields returned by the selected provider through the canonical helper.

- FMP quote selection may use FMP-side `profile` and `stock-price-change` supplements.
- Finnhub quote selection as fallback may use Finnhub-side `stock/metric` supplement.
- Do not call fallback providers solely to fill missing Standard snapshot fields.
- Supplement failures must degrade gracefully and must not trigger fallback or make an otherwise usable quote unusable.
- Missing Standard fields should display as `Not available` or be omitted cleanly.
- Calculate `Relative Volume` only when both `volume` and `average_volume` are available.
- Do not include valuation multiples by default unless required denominators are cleanly sourced and labeled under `METRICS.md`.
- `Profile` and `Trend` sections are market-data-only context; do not use them to imply business quality, thesis confirmation, recommendation, or setup classification.

## Limitation Display

Normal successful responses should not include a routine disclaimer/footer.

Add a short limitation line only when provider data is partial, stale, conflicting, unavailable, rate-limited, or otherwise materially limited.

Failure and debug/raw outputs may include fuller sanitized limitations and provider metadata as needed.

## Raw / Debug Output

Raw JSON/debug output is allowed only when explicitly requested.

Even in raw/debug mode:

- do not expose API keys
- do not expose Authorization headers
- do not expose token/key/secret query parameters
- strip query parameters from endpoint strings
- keep provider/as-of/timezone/limitations visible
- do not include environment dumps
- do not create artifacts
- do not provide recommendations

Raw/debug output should not be used by other commands as a parsed user-facing data source. Other commands needing market data should call the canonical helper directly under `MARKET_DATA.md`.

## Failure Output

Missing ticker:

```md
!market needs a ticker.
Example: !market HOOD
```

Invalid ticker:

```md
!market could not run: invalid ticker symbol format.
Example: !market HOOD
```

Provider failure:

```md
!market [TICKER] — Market Data Unavailable
As of: [timestamp] [timezone]

No provider returned a usable price.
Provider errors: [sanitized provider errors]
Limitations: No price, market cap, or valuation metric should be inferred from this failure.
```

Rate limit or stale timestamp:

```md
Provider limitation: [provider] returned a rate-limit notice or stale/as-of timestamp. Treat the snapshot as limited; do not present it as fully current.
```

## Prohibited Output

Do not include:

- Buy/Sell/Hold
- price targets
- sizing or trade instructions
- MIDAS score
- setup classification
- thesis conclusion
- valuation conclusion by default, including cheap/expensive/fair-value language
- filing-backed research claims not supported by filings
- ticker workspace artifact paths
- `Saved to:`
- summary-only responses that hide ticker, as-of timestamp, or source/provider
- automatic next-command execution

## Artifact Boundary

`!market` writes nothing by default.

Do not create:

- `workspace/tickers/[ticker]/market.md`
- market snapshot artifacts
- source manifests
- evidence ledgers
- proof packets
- schemas
- index updates
- watchlist mutations

## Final Rule

`!market` returns one Standard Market Snapshot. It is market-data context only, not an investment recommendation, stock score, thesis, risk report, valuation model, or filing-backed research artifact.
