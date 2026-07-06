# `!market` Stage 4 Rendering + Stage 5 Handoff — 2026-06-12

Use this historical note when reviewing how Stage 4 handed off to the now-completed Stage 5 work.

## Stage 4 result

Stage 4 implemented helper-side render modes while preserving JSON as the default helper output:

```bash
python3 tools/market_data_snapshot.py HOOD
python3 tools/market_data_snapshot.py HOOD --render compact
python3 tools/market_data_snapshot.py HOOD --render full
python3 tools/market_data_snapshot.py HOOD --render expanded
python3 tools/market_data_snapshot.py HOOD full
```

## Compact contract preserved

Default compact output remains a frozen display contract and must end at:

```md
Source: [provider]
```

Compact mode must not add full-mode sections, provider endpoint metadata, source fields, provider notes, or routine disclaimer/footer text.

## Current full / expanded display contract

This handoff note is retained for implementation history, but the active display contract is now in `SKILL.md`, `OUTPUT.md`, and `references/full-mode-display-contract.md`.

Current full/expanded output should include market-data-only sections in this order:

- `## Profile`
- `## Price Action`
- `## Liquidity`
- `## Trend`

Normal successful full/expanded output keeps `Source: [provider]` directly below `As of:` and does not add a trailing source/limitations footer.

Stage 3 supplement fields should display only in full/expanded mode, including price-performance windows, moving averages, beta, sector, industry, country, IPO date, issuer type, and actively trading status when available. Missing fields should render as `Not available` or be omitted cleanly.

## Verification pattern used

Before treating a rendering change as complete, run:

- AST/syntax check for `tools/market_data_snapshot.py`
- default JSON helper parse check
- mock compact/full render checks
- live compact smoke check confirming final line is `Source: [provider]`
- live full smoke check confirming current active sections from `references/full-mode-display-contract.md`
- `git diff --check`
- secret-marker scan on rendered output

## Stage 5 handoff — completed

Stage 5 implemented Finnhub selected-provider supplement support for full/expanded mode only. This section is retained as historical context, not an active next-step instruction.

Guardrails:

- If FMP succeeds, do not call Finnhub for enrichment.
- If FMP fails and Finnhub is the selected quote provider, full/expanded mode may call Finnhub supplemental metrics.
- Do not enrich compact output.
- Do not trigger Alpha Vantage or other fallback providers merely to fill missing supplemental fields.
- Supplement failure must not invalidate a usable quote; degrade to `Not available` / clean omissions.

Useful Stage 5 candidate fields from Finnhub metrics, if available and clearly sourced:

- 52-week high/low
- beta
- 50D / 200D moving averages
- 10D / 3M average volume or equivalent liquidity fields

Acceptance tests for Stage 5 included mock FMP failure + Finnhub success, compact invariant preservation, full render supplement display, supplement-failure degradation, syntax/diff checks, and secret scanning. Stage 6 later consolidated broader provider-policy validation in `evals/market_stage6_validation.py`.
