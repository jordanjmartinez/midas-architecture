# `!market full` / `!market expanded` Proposal

Historical session-derived proposal for explicit expanded market snapshot mode. This proposal has been implemented and superseded by the current active contract in `SKILL.md`, `OUTPUT.md`, `tools/market_data_snapshot.py`, and `references/full-mode-display-contract.md`.

## Trigger

```md
!market [ticker] full
!market [ticker] expanded
```

## Boundary

Full/expanded mode must remain market-data-only. It must not become research, thesis, scoring, classification, recommendation, price target, sizing, entry/exit, or trade advice.

Do not include valuation multiples by default unless every denominator is cleanly sourced, period-labeled, and handled under `rules/METRICS.md`.

## Current Output Shape

```md
[Display Name] ($[TICKER]) Full Market Snapshot
As of: [human-readable timestamp]
Source: [provider]

## Profile
Sector: [sector or Not available]
Industry: [industry or Not available]
Country: [country or Not available]
IPO Date: [ipo_date or Not available]
Issuer Type: [issuer type or Not available]
Actively Trading: [Yes / No / Not available]

## Price Action
Market Cap: [market_cap or Not available]
Price: [price]
Change: [dollar_change] / [percent_change]
Previous Close: [previous_close or Not available]
Open: [open or Not available]
Day High / Low: [day_high or Not available] / [day_low or Not available]
52-Week High / Low: [week_52_high or Not available] / [week_52_low or Not available]

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

## Helper Fields Currently Available

- `ok`
- `ticker`
- `provider`
- `primary_provider`
- `fallbacks_used`
- `provider_errors`
- `provider_endpoints`
- `as_of`
- `timezone`
- `display_fields`
- `company_name`
- `exchange`
- `currency`
- `price`
- `market_cap`
- `market_cap_source`
- `volume`
- `change`
- `change_percentage`
- `source_fields`
- `limitations`

## Helper Fields Likely Needed

- `previous_close`
- `open`
- `day_high`
- `day_low`
- `week_52_high`
- `week_52_low`
- `average_volume`
- optional `relative_volume` or compute from `volume / average_volume`
- source-field labels for each added metric

## Implementation Notes

- Keep default `!market [ticker]` compact and clean.
- Do not reintroduce provider metadata blocks by default.
- Show fallback/provider warnings only in failure/debug/raw paths, and always sanitize them.
- Update `OUTPUT.md`, helper schema, and evals together if implementing full/expanded mode.
