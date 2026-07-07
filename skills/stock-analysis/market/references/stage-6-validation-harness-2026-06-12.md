# Stage 6 `!market` Validation Harness — 2026-06-12

Use this reference when validating future `!market` provider-policy or rendering changes.

## Harness path

```bash
evals/market_stage6_validation.py
```

Run from the Midas profile root:

```bash
python3 evals/market_stage6_validation.py
```

## What it verifies

The harness is offline/mock-only. It imports `tools/market_data_snapshot.py`, monkeypatches provider functions, and verifies six contract cases:

1. FMP quote success with FMP supplements.
2. FMP quote success with FMP supplement failures.
3. FMP failure plus Finnhub quote/profile/metric success.
4. FMP failure plus Finnhub quote success with Finnhub metric failure.
5. FMP and Finnhub failure plus Alpha Vantage success.
6. All providers fail.

## Contract checks

- FMP usable quote prevents fallback provider calls.
- Supplement failures do not trigger provider fallback.
- Finnhub `stock/metric` is selected-provider-only.
- Alpha Vantage is reached only after FMP and Finnhub fail/no usable price.
- Compact render omits full sections and places `Source: [provider]` directly below `As of:`.
- Full render includes the expected full sections.
- Secret markers used in mock errors are redacted from payloads/renders.
- Output avoids recommendation/scoring/trade framing.

## Stage 6 live smoke pattern

After mock validation, run live smoke checks:

```bash
python3 tools/market_data_snapshot.py HOOD
python3 tools/market_data_snapshot.py HOOD --render compact
python3 tools/market_data_snapshot.py HOOD --render full
python3 tools/market_data_snapshot.py KEEL
python3 tools/market_data_snapshot.py KEEL --render compact
python3 tools/market_data_snapshot.py KEEL --render full
```

Expected:

- HOOD or another FMP-success ticker remains FMP-selected.
- KEEL or another known fallback ticker remains Finnhub-selected if FMP lacks access/coverage.
- Compact source lines appear directly below `As of:` for each successful render.
- Full output includes `## Profile` near the top, includes `## Trend`, and omits routine success footers.

## Mutation guard

Before and after live smoke checks, compare the scoped git status for watchlist/artifact paths:

```bash
git status --short -- data/midas_watchlist.json workspace/tickers | sort
```

Known pre-existing workspace/watchlist changes may appear, but Stage 6 should not introduce any new mutation.
