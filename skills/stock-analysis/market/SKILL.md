---
name: market
description: Thin read-only MIDAS utility command for `!market [ticker]` Standard Market Snapshots.
version: 0.2.0
status: Active
author: Midas / Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [midas, stock-analysis, market-data, command]
---

# `!market` Command

Use this skill when the user invokes:

```md
!market [ticker]
```

## Registry Metadata

Command: `!market`
Aliases: `None`
Category: `System / Utility`
Status: `Active`
Skill Path: `skills/stock-analysis/market/SKILL.md`
Output Path: `skills/stock-analysis/market/OUTPUT.md`
Eval File: `evals/market.eval.md`
Uses Classification: `Not used`
Uses Scoring: `Not used`
Uses Metrics: `Optional`
Writes Artifacts: `No`
Primary Global Rules: `GLOBAL.md`, `SOURCES.md`, `MARKET_DATA.md`, `METRICS.md`, `OUTPUT.md`

## Purpose

`!market` is a thin standalone utility command for one Standard live market snapshot.

It exposes the canonical market-data helper to the user directly. It is not the market-data architecture itself; the architecture lives in:

```md
/home/jordan/.hermes/profiles/midas/rules/MARKET_DATA.md
```

The helper lives at:

```md
/home/jordan/.hermes/profiles/midas/tools/market_data_snapshot.py
```

Other MIDAS commands should not depend on `!market` output text. If `!thesis`, `!financials`, `!risk`, `!full`, or future screen/watchlist workflows need live market context, they should follow `MARKET_DATA.md` and call the canonical helper directly.

## Mandatory Rule Inheritance

Follow:

- `/home/jordan/.hermes/profiles/midas/rules/GLOBAL.md`
- `/home/jordan/.hermes/profiles/midas/rules/MARKET_DATA.md`
- `/home/jordan/.hermes/profiles/midas/rules/SOURCES.md`
- `/home/jordan/.hermes/profiles/midas/rules/METRICS.md` when displaying market-cap, valuation-related, calculated, or performance metrics
- `/home/jordan/.hermes/profiles/midas/rules/OUTPUT.md`

If this command skill conflicts with `MARKET_DATA.md`, `MARKET_DATA.md` controls market-data behavior.

Command-specific display rules live in:

```md
/home/jordan/.hermes/profiles/midas/skills/stock-analysis/market/OUTPUT.md
```

Market references remain historical/support material only until separately cleaned up. Do not let stale reference wording reintroduce Compact, Full, Expanded, or Deep as normal modes.

## Inputs

Supported normal command:

```md
!market [ticker]
```

Examples:

```md
!market HOOD
!market AAPL
```

Former mode/style words are not separate market snapshot modes:

```md
compact
quick
brief
short
summary
concise
full
expanded
detailed
deep
deep-dive
deepdive
```

If one of these words appears with a ticker, still return the same Standard Market Snapshot unless the request is clearly asking for explicit raw/debug output. Do not render the old skinny compact snapshot. Do not render a title saying `Full Market Snapshot`. Do not auto-run other commands.

Raw/debug JSON is allowed only when explicitly requested for diagnostics:

```md
!market HOOD raw json
!market HOOD debug
```

Raw/debug requests are not normal market snapshot modes. They must not create artifacts and should not be parsed by other commands as user-facing source text.

## Thin Utility Workflow

1. Parse the ticker.
2. If the ticker is missing or invalid, return a clean input failure and do not call providers.
3. For normal command display, call the canonical read-only helper in Standard render mode:

```bash
python3 /home/jordan/.hermes/profiles/midas/tools/market_data_snapshot.py [TICKER] --render standard
```

4. If a former render token such as `compact`, `full`, or `expanded` reaches the helper, treat it as a compatibility alias for the same Standard Market Snapshot, not as a separate mode.
5. Preserve provider/as-of/timezone/limitations and sanitized provider errors.
6. If raw/debug JSON was explicitly requested, show JSON only after confirming secrets are not present.

Do not add command-specific provider logic inside `!market`. Provider behavior belongs in `MARKET_DATA.md` and `tools/market_data_snapshot.py`.

## Provider Fallback Policy

`!market` uses the helper’s v1 provider policy:

- FMP first.
- Stop if FMP returns usable price.
- Finnhub only if FMP fails or returns no usable price.
- Stop if Finnhub returns usable price.
- Alpha Vantage only if FMP and Finnhub fail or return no usable price.
- Return `ok:false` if no provider returns usable price.

Fallback is triggered only by missing usable price.

Do not call fallback providers solely to fill:

- market cap
- currency
- volume
- high/low
- prior close
- 52-week range
- exchange
- company name
- sector/industry/country
- moving averages
- performance windows
- beta

## Display Role

Normal successful `!market` output is the Standard Market Snapshot:

- title: `[TICKER] | [Company Name] Market Snapshot` when `company_name` is available from the helper; otherwise `[TICKER] | Market Snapshot`
- human-readable as-of timestamp, e.g. `Jun 5, 2026, 1:20 AM ET`
- one simple source line: `Source: [provider]` directly under the `As of:` timestamp
- `Profile`
- `Price Action`
- `Liquidity`
- `Trend`

Do not include `Full` in the title. Do not include `!market` or an em dash in the title.

The Standard snapshot should include the richer former full-style fields when available:

- Sector
- Industry
- Country
- Exchange
- IPO Date
- Issuer Type
- Actively Trading
- Market Cap
- Price
- Change
- Previous Close
- Open
- Day High
- Day Low
- 52-Week High
- 52-Week Low
- Volume
- Average Volume
- Relative Volume
- 5D / 1M / 3M / 6M / YTD / 1Y performance
- 50D Avg
- 200D Avg
- Price vs 50D Avg
- Price vs 200D Avg
- Beta

Do not show provider metadata blocks by default on normal success. Specifically omit default `Provider`, `Primary provider`, `Fallbacks used`, `Provider errors`, `Provider endpoints`, `Source fields`, and `Provider note` lines unless the command fails or the user explicitly asks for source/debug/raw output.

Market cap remains a default displayed field when available. Missing market cap alone is not a provider fallback trigger.

## Selected-Provider Supplement Contract

Selected-provider supplements may enrich the Standard Market Snapshot after the quote provider has already been selected:

- If FMP quote is selected, the helper may use FMP-side `profile` and `stock-price-change` supplements.
- If Finnhub quote is selected as fallback, the helper may use Finnhub-side `stock/metric` supplement.
- Supplements must not trigger provider fallback.
- Supplement failures must degrade gracefully; keep the selected quote usable and render missing fields as `Not available` or omit them cleanly.

Do not include valuation multiples by default unless denominators are cleanly sourced and labeled under `METRICS.md`.

## Metric Discipline

Follow `METRICS.md` for metric labels, units, source/as-of discipline, calculated fields, and stale-data handling.

Preserve:

- metric name
- provider/source
- as-of date/time/timezone
- currency, unit, percent, and volume formatting
- calculated-ratio labeling when relevant
- no false precision
- no stale market data presented as current

Market data is context only. It is not filing-backed proof of business quality, financial quality, risk, or thesis validity.

## Guardrails

`!market` must not:

- write ticker workspace artifacts
- create `workspace/tickers/[ticker]/market.md`
- report `Saved to:`
- update indexes
- update watchlists
- classify setups
- score stocks
- give Buy/Sell/Hold recommendations
- provide price targets
- suggest sizing, entries, exits, or trades
- call the stock cheap, expensive, or fair-value by default
- infer investment action from price action
- present market data as proof of business quality or thesis validity
- replace SEC filings or company primary disclosures
- become `!research`, `!financials`, `!thesis`, `!risk`, `!full`, or `!gems`
- auto-run downstream commands
- print, log, save, or expose API keys

## Failure Behavior

If input is missing or invalid:

- explain the input issue
- show example usage
- do not call providers

If no provider returns usable price:

- report that market data is unavailable
- show sanitized provider errors if available
- do not fabricate price, market cap, or valuation metrics
- do not proceed into filing-backed research unless the user separately asks

If timestamps are stale or uncertain:

- label the limitation clearly
- avoid wording like “current” unless provider/as-of support it

If provider data is partial, stale, conflicting, unavailable, or rate-limited, show a short limitation line. Do not add a routine limitation/footer on clean normal success.

## Artifact Behavior

`!market` is read-only.

It must not create, modify, or report paths under:

```md
/home/jordan/.hermes/profiles/midas/workspace/tickers/
```

It must not create source manifests, evidence ledgers, proof packets, schemas, fixtures, market artifacts, or index/watchlist mutations.

## Maintenance Notes

Current evals still need later lean alignment because older tests expect compact default and separate full/expanded mode behavior. Do not patch evals unless the user explicitly approves an eval stage.

Current references include historical full/compact upgrade notes and may contain stale language. Do not patch references unless the user explicitly approves a reference-cleanup stage.

## Final Rule

`!market` returns one Standard Market Snapshot. It is a thin market snapshot utility, not an investment recommendation, stock score, thesis, risk report, valuation model, or filing-backed research artifact.
