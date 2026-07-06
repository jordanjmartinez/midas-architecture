# `!market` Source Placement / Full Footer Preference (2026-06-12)

Session learning / durable rendering contract:

- Default compact mode renders `Source: [provider]` directly under `As of:`.
- Full/expanded mode renders `Source: [provider]` directly under `As of:`.
- Normal successful full/expanded output does **not** render a trailing source/limitations section.
- Normal successful full/expanded output does **not** render fallback or routine limitations labels.
- Failure/debug/raw paths may still show sanitized provider errors, fallbacks, and limitations.
- This is layout-only: do not change provider order, fallback policy, selected-provider supplements, raw/debug JSON, watchlist behavior, or artifact behavior.

Implementation checklist for future changes:

1. Runtime: update `tools/market_data_snapshot.py` renderers:
   - `render_compact_snapshot()`
   - `render_full_snapshot()`
2. Validation: update compact/full render expectations in:
   - `evals/market_stage6_validation.py`
   - `skills/stock-analysis/market/scripts/verify_finnhub_supplement_mock.py`
3. Docs/contracts: update display examples that still imply a trailing full-mode source/footer block.
4. Smoke test both modes with a fallback ticker and assert:
   - line 2 starts with `As of:`
   - line 3 is `Source: [provider]`
   - line 4 is blank
   - full output lacks routine source/footer labels

Suggested verification:

```bash
python3 -m py_compile tools/market_data_snapshot.py evals/market_stage6_validation.py skills/stock-analysis/market/scripts/verify_finnhub_supplement_mock.py
python3 evals/market_stage6_validation.py
python3 skills/stock-analysis/market/scripts/verify_finnhub_supplement_mock.py
python3 tools/market_data_snapshot.py IREN --render compact
python3 tools/market_data_snapshot.py IREN --render full
git diff --check
```
