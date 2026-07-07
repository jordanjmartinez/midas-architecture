# MIDAS Market Data Standards

## Purpose

`MARKET_DATA.md` is the global MIDAS rule file for live market-data usage, similar in authority to `SOURCES.md` and `METRICS.md`.

It governs how MIDAS retrieves, labels, displays, and uses live/current market snapshots across commands.

Market data is useful context. It is not filing-backed evidence, not a recommendation engine, and not a replacement for SEC filings or company primary disclosures.

---

## Source Role

Live market data is **Tier 2 market context**.

It can support:

- current/recent share price
- provider market capitalization
- enterprise value inputs
- valuation multiples when denominators are separately sourced and clean
- price performance
- trading volume and liquidity context
- rerating context
- market-cap or liquidity filters for screens/watchlists

It cannot prove:

- business quality
- revenue, margin, cash-flow, debt, dilution, or balance-sheet facts
- segment performance
- customer concentration
- risk-factor claims
- legal/regulatory claims
- management statements
- filing-backed thesis or risk evidence

Use SEC filings, company reports, earnings releases, and official disclosures for those facts.

If market data conflicts with SEC filings or company primary disclosures for financial-statement facts, prefer the filings and label the timing mismatch.

---

## Relationship to Other MIDAS Rules

This file specializes but does not replace:

- `rules/GLOBAL.md`
- `rules/SOURCES.md`
- `rules/RERATING.md`
- `rules/METRICS.md`
- `rules/OUTPUT.md`
- `rules/ARTIFACTS.md`

Market data can support rerating context, price-performance context, liquidity, valuation multiples, and crowding/recognition analysis, but `rules/RERATING.md` governs setup interpretation. Market data does not prove business quality, financial quality, or thesis validity.

---

## Command vs Helper Architecture

`MARKET_DATA.md` governs live market-data behavior across MIDAS.

`tools/market_data_snapshot.py` is the canonical read-only helper for retrieving live market snapshots.

`!market` is a thin standalone utility command and testable consumer of the helper. It is not the market-data architecture itself.

Other commands should not depend on `!market` output text. When commands such as `!thesis`, `!financials`, `!risk`, or future screen/watchlist workflows need live market context, they should follow this rule file and call the canonical helper directly.

Architecture:

```md
Command workflow
→ MARKET_DATA.md
→ tools/market_data_snapshot.py
→ approved market-data providers
```

---

## Canonical Helper

Canonical helper path:

```md
tools/market_data_snapshot.py
```

Canonical invocation:

```bash
python3 tools/market_data_snapshot.py [TICKER]
```

The helper must:

- be read-only
- return structured JSON to stdout
- return `ok: true` only when a provider returns a usable price
- return `ok: false` if no provider returns a usable price
- preserve provider/as-of/timezone/limitations metadata
- preserve sanitized provider errors when relevant
- never write ticker artifacts
- never expose API keys

Commands should call the helper instead of duplicating provider-specific market-data API logic.

---

## Approved Provider Calls

Use endpoint labels in rules, command output, artifacts, and debug summaries. Exact URLs, query parameters, and provider-specific request construction belong in the helper, not in command output or saved artifacts.

Approved v1 endpoint labels:

- FMP: quote
- FMP: market-capitalization, only as an FMP-side supplement when the selected FMP quote lacks market cap
- FMP: profile, only as an FMP-side supplement after FMP quote has selected FMP
- FMP: stock-price-change, only as an FMP-side supplement after FMP quote has selected FMP
- Finnhub: quote, only when FMP fails or returns no usable price
- Finnhub: profile2, only when Finnhub is the selected fallback provider and company or market-cap context is needed
- Finnhub: stock/metric, only as a Finnhub-side supplement after Finnhub quote has selected Finnhub as fallback
- Alpha Vantage: GLOBAL_QUOTE, only when FMP and Finnhub fail or return no usable price

Do not add new providers or endpoint families without updating this rule file, the helper, and eval coverage.

Do not expose raw credential-bearing URLs.

---

## Usable Quote Standard

For v1, a provider response is usable when it includes:

- requested ticker or resolved ticker
- numeric price greater than zero
- provider name
- retrieval timestamp or provider data timestamp
- no provider error, rate-limit response, symbol-not-found response, or empty payload that invalidates the quote

Missing market cap, currency, volume, exchange, change percentage, range fields, company name, or prior close does not make a quote unusable by itself.

Fallback providers should be called only when the selected provider fails or returns no usable price.

Market cap is a core displayed market field when available, but missing market cap alone is not a v1 fallback trigger.

---

## Provider Policy

Provider hierarchy for v1:

1. FMP is primary.
2. Finnhub is fallback only if FMP fails or returns no usable price.
3. Alpha Vantage is fallback only if FMP and Finnhub fail or return no usable price.

Fallback trigger:

- Missing usable price is the only v1 fallback trigger.

Do not call fallback providers solely to fill:

- market cap
- currency
- volume
- open
- day high / day low
- prior close
- 52-week range
- company name
- exchange
- any other non-price field

If a non-price field is missing, display `Not available`, omit it, or label it as unavailable. Do not build a field-level enrichment engine for v1.

Market cap remains a default displayed field when available, but missing market cap alone must not trigger fallback calls.

### Selected-Provider Supplements

Selected-provider supplements may enrich explicit full/expanded market snapshots only after the provider has already returned a usable quote and become the selected provider.

Allowed v1 selected-provider supplements:

- If `FMP: quote` returns usable price and selects FMP, the helper may call `FMP: profile` and `FMP: stock-price-change` for market-data-only context such as average volume, beta, sector, industry, country, issuer flags, 50D/200D averages, and price-performance windows.
- If `Finnhub: quote` returns usable price after FMP failed or returned no usable price, the helper may call `Finnhub: stock/metric` for market-data-only context such as average volume, beta, 52-week range, market capitalization, and price-performance windows.

Supplement rules:

- Supplements must not determine provider selection.
- Supplement failure must not make an otherwise usable quote unusable.
- Supplement failure must not trigger fallback to another provider.
- Missing supplement fields should display as `Not available`, be omitted cleanly, or be summarized as a non-material provider limitation.
- Supplement endpoint labels may appear in debug/source output and helper metadata, but compact successful `!market [ticker]` output must remain unchanged.
- Do not call Finnhub supplements when FMP succeeds solely to enrich FMP snapshots.
- Do not call Alpha Vantage solely for supplemental fields.

---

## Provider Keys and API-Key Safety

Primary provider key:

```bash
FMP_API_KEY
```

Fallback provider keys, if available:

```bash
FINNHUB_API_KEY
ALPHA_API_KEY
```

Rules:

- Read keys only from runtime environment variables.
- Do not hardcode keys in scripts, rules, prompts, evals, artifacts, or command outputs.
- Never print, log, save, or expose API keys.
- Strip query parameters from endpoint strings.
- Redact `apiKey`, `apikey`, `token`, `key`, `secret`, `Authorization`, and similar credential-like values from errors/debug output.
- Prefer endpoint labels such as `FMP: quote` over raw URLs.
- Raw JSON/debug output is allowed only when explicitly requested and must still redact secrets.

---

## Required Snapshot Metadata

Every successful market snapshot must include:

- `ok`
- `ticker`
- `provider`
- `primary_provider`
- `fallbacks_used`
- `as_of`
- `timezone`
- `limitations`

Include when relevant:

- `provider_errors` with sanitized error/notice strings
- `provider_endpoints` using endpoint labels, not raw credential-bearing URLs
- `source_fields` using field-level labels for displayed values

When available, helper output may preserve:

- `retrieved_at`: when MIDAS/helper retrieved the data
- `provider_data_as_of`: provider-supplied quote or trading timestamp
- `as_of`: displayed timestamp used by command output

Do not make all three timestamp fields mandatory for every provider if unavailable, but preserve them when available. Keep `timezone` visible.

Schema semantics:

- `provider`: provider used for the returned snapshot.
- `primary_provider`: same as `provider` for v1; the first provider in the hierarchy that returned usable price.
- `fallbacks_used`: providers tried after FMP because prior providers failed or returned no usable price. This is provider-level fallback, not field-level enrichment.
- `provider_errors`: sanitized failures/notices from providers that failed or returned no usable price.
- `as_of`: displayed timestamp used by command output.
- `timezone`: timezone for `as_of`.
- `limitations`: freshness, delay, plan, missing-field, and boundary caveats.

---

## Common Market Snapshot Fields

Common display fields for `!market` and other compact market snapshots:

- price
- market cap when available
- currency when available, defaulted, or labeled
- change/change percent when available
- volume when available
- exchange when available

Optional display fields may be shown if available from the selected provider, but must not trigger fallback calls by themselves.

Commands should display only the market-data fields relevant to their workflow. For example, `!thesis` may need market cap or valuation context, while `!market` may show a broader quote snapshot.

If market cap is missing, use wording such as:

```md
Market cap: Not available from selected provider snapshot.
```

---

## Valuation / Metrics Integration

When live market data is used to calculate valuation metrics, follow:

```md
rules/METRICS.md
```

Market data may provide inputs such as:

- share price
- provider market capitalization
- price performance
- volume/liquidity
- quote timestamp
- provider-sourced market context

Filing or company-primary sources should provide fundamentals such as:

- share count when precision matters
- cash
- debt
- preferred stock
- minority interest
- revenue
- EBITDA
- EBIT
- net income
- free cash flow
- segment financials

When mixing current market data with filing-derived financial inputs, label the timing mismatch.

Do not define valuation formulas in `MARKET_DATA.md`. Use `METRICS.md` for formulas, denominator discipline, GAAP/non-GAAP labeling, period labeling, and stale-data handling.

---

## Boundary Rules

Market data must be labeled with provider and as-of timestamp.

Market data must not contaminate filing-backed facts:

- Do not use provider market data as evidence for revenue, margins, cash flow, balance-sheet values, dilution, segment results, customer concentration, or risk-factor claims.
- Do not let provider market cap override filing-derived share-count or dilution analysis where filing precision matters.
- When mixing current market data with filing-derived cash/debt/share-count inputs, label the timing mismatch.

Market data must not produce:

- Buy/Sell/Hold recommendations
- price targets
- sizing
- entry/exit instructions
- trade advice
- unsupported “cheap/expensive” conclusions
- thesis proof by price action alone

Market data can support valuation or rerating context only when clearly labeled as context.

`!thesis`, `!financials`, and `!risk` may use market data for valuation/rerating context, but filing-backed evidence must remain separate.

`!research` should not use live market data by default unless explicitly needed for context.

---

## Command Usage Rules

### `!market`

`!market [ticker]` is a thin standalone utility command that calls the canonical helper and displays a compact market snapshot.

It is read-only, writes no artifacts, performs no classification/scoring, and gives no recommendations or trade advice.

Detailed command workflow and display requirements live in:

- `skills/stock-analysis/market/SKILL.md`
- `skills/stock-analysis/market/OUTPUT.md`
- `evals/market.eval.md`

### Filing-backed commands

Commands such as `!thesis`, `!financials`, `!risk`, and future screen/watchlist workflows may use market data for valuation, market-cap, liquidity, price-performance, or rerating context.

They must keep market data separate from SEC filing-backed business, financial, and risk evidence.

Do not inject live market-data sections into filing-backed outputs by default unless the command workflow calls for valuation/rerating context or the user asks for current market context.

---

## Failure Behavior

If market-data retrieval fails:

- do not fabricate price, market cap, or valuation metrics
- return or display a clear limitation
- preserve sanitized provider errors when relevant
- continue filing-backed analysis only if market data was not required for the requested task

If a provider returns stale, delayed, end-of-day, or plan-limited data, label that limitation.

---

## Final Rule

Market data should make MIDAS valuation and rerating context more current and useful.

It must stay separate from filing-backed evidence and must not turn MIDAS into a trading system, recommendation engine, price-target machine, or API dump.
