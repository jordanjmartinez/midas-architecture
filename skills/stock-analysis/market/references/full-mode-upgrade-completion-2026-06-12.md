# `!market` Full/Expanded Upgrade Completion Notes — 2026-06-12

Use this reference as the post-Stage-7 overview for the June 2026 `!market full` / `expanded` upgrade.

## Final state

The staged upgrade is complete through Stage 7.

- Compact `!market [ticker]` remains the frozen default display contract with `Source: [provider]` directly below `As of:` on success.
- Default helper invocation still emits JSON:

```bash
python3 tools/market_data_snapshot.py HOOD
```

- Human-readable helper render modes are available:

```bash
python3 tools/market_data_snapshot.py HOOD --render compact
python3 tools/market_data_snapshot.py HOOD --render full
python3 tools/market_data_snapshot.py HOOD --render expanded
python3 tools/market_data_snapshot.py HOOD full
```

## Provider behavior

- FMP remains primary.
- Finnhub is used only when FMP fails or returns no usable price.
- Alpha Vantage is used only when FMP and Finnhub fail or return no usable price.
- Missing non-price fields never trigger provider fallback.
- Selected-provider supplements are allowed only after a provider has already returned usable price and become selected:
  - FMP-selected snapshots may use `FMP: profile` and `FMP: stock-price-change`.
  - Finnhub-selected fallback snapshots may use `Finnhub: stock/metric`.

## Validation assets

Reusable validation assets:

```bash
python3 evals/market_stage6_validation.py
python3 skills/stock-analysis/market/scripts/verify_finnhub_supplement_mock.py
```

Run both from the MIDAS profile root.

## Stage 7 cleanup result

Stage 7 was documentation/cleanup only for the user-facing helper path. It did not change provider behavior, helper logic, compact/full rendering logic, watchlist data, or ticker artifacts. It also fixed the reusable Stage 5 mock verifier path so the documented validation command runs from the MIDAS profile root.

Stage 7 cleaned stale handoff language, marked the implementation plan as completed through Stage 7, and preserved detailed implementation/testing notes in references rather than bloating `SKILL.md`.

## Guardrails for future changes

Future `!market` changes should start with the Stage 6 harness and then add narrowly scoped eval cases before behavior changes. Do not alter compact output or provider fallback policy without explicit user approval and rule/eval updates first.
