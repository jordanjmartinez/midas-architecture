# Final Audit / Drift Cleanup — 2026-06-12

Use this note when doing a final `!market` audit after layout/provider changes.

## Durable lessons

- A final audit should check runtime, active docs, eval expectations, and reference notes together. Drift often lives in historical references even after runtime and evals pass.
- If old reference notes still show obsolete active output shapes, do not merely say they are historical if they can still mislead future maintenance. Either replace the obsolete example with the current active contract or clearly narrow it to implementation history.
- User-facing summaries should not dump checksum/SHA values unless explicitly requested. Prefer: `Verified; no watchlist/artifact changes.`
- When the user asks why a fallback provider was used, inspect helper JSON/provider_errors. For RCAT in this session, FMP returned `status=402`, meaning likely plan/paywall-limited access, then Finnhub returned usable price.

## Current full-mode layout invariant

```md
## Profile
## Price Action
## Liquidity
## Trend
```

Full/expanded success should:

- keep `Source: [provider]` directly under `As of:`
- use `## Price Action`, not `## Quote`
- render `Market Cap:` above `Price:`
- omit a separate market-size section
- omit `Shares Outstanding:`
- omit routine success footer/source/limitations/fallback blocks

## Suggested final audit sequence

```bash
python3 -m py_compile tools/market_data_snapshot.py evals/market_stage6_validation.py skills/stock-analysis/market/scripts/verify_finnhub_supplement_mock.py
python3 evals/market_stage6_validation.py
python3 skills/stock-analysis/market/scripts/verify_finnhub_supplement_mock.py
python3 tools/market_data_snapshot.py HOOD --render compact
python3 tools/market_data_snapshot.py HOOD --render full
python3 tools/market_data_snapshot.py RCAT --render compact
python3 tools/market_data_snapshot.py RCAT --render full
python3 tools/market_data_snapshot.py RCAT
# Then assert full-mode ordering and fallback/provider_errors behavior programmatically or by focused scan.
git diff --check
```

## Stale-term scan targets

Scan active contracts and relevant references for stale active-use occurrences of:

- old quote-section wording
- old market-size section wording
- shares-outstanding render lines
- old combined trend/liquidity section wording
- routine success source/limitations/footer wording
- raw watchlist checksum instructions in user-facing verification notes

Negative assertions are okay, but stale positive examples should be corrected.