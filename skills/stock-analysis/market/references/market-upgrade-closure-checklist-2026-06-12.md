# `!market` Upgrade Closure Checklist — 2026-06-12

Use this reference when finishing a staged `!market` implementation, cleanup, or documentation-only maintenance pass.

## Why this exists

The June 2026 full/expanded-mode upgrade ended with a documentation-only Stage 7. The useful durable pattern was not the specific stage narrative; it was the closure discipline:

- remove stale "next stage" / handoff wording after work is complete
- preserve the compact-success display invariant
- verify no provider behavior changed during cleanup
- keep reusable mock verifiers runnable after path or directory changes
- prove read-only behavior by checking watchlist/artifact mutation guards

## Closure steps

1. **Confirm scope**
   - If the pass is documentation-only, do not modify provider selection, fallback behavior, render logic, or command runtime behavior.
   - If runtime code changed, treat it as a new scoped implementation and rerun the relevant staged evals.

2. **Remove stale active handoff language**
   - Search market references and plans for wording such as:
     - `Next recommended stage`
     - `next step is`
     - `handoff`
     - `remaining stage`
   - Convert stale future-tense wording to historical/completed wording when the work is done.

3. **Preserve compact success output**
   - Default compact `!market [ticker]` success still ends at exactly:
     - `Source: [provider]`
   - Do not add fallback/provider notes, caveats, or debug metadata to normal compact success.

4. **Verify full/expanded behavior separately**
   - `full` / `expanded` may render more fields, but must stay market-data-only.
   - Supplements must follow the selected-provider contract and must not trigger provider fallback solely to fill missing expanded fields.

5. **Run the reusable validation set**
   - Main mock harness:
     ```bash
     python3 evals/market_stage6_validation.py
     ```
   - Finnhub supplement mock verifier:
     ```bash
     python3 skills/stock-analysis/market/scripts/verify_finnhub_supplement_mock.py
     ```
   - Python compile checks for touched scripts.
   - `git diff --check`.

6. **Guard read-only invariants**
   - Confirm `!market` did not alter:
     - `data/midas_watchlist.json`
     - `workspace/tickers/`
   - For docs-only cleanup, compare watchlist checksum before/after when practical.

7. **Secret-safety check**
   - Scan the diff for accidental API keys, bearer tokens, raw provider responses containing credentials, or `.env` leakage.
   - Keep provider errors sanitized.

## Reporting pattern

Final status should distinguish:

- what changed
- what did not change
- which validations passed
- whether watchlist/artifact mutation guards remained clean
- any unrelated pre-existing modified files that were intentionally not touched

Keep the final response concise and Telegram-readable.
