# `!market` Full/Expanded Data Upgrades Implementation Plan

> **For Hermes:** Implement this plan stage-by-stage. Do not collapse stages. Verify each stage before moving forward.

**Goal:** Expand `!market full` / `!market expanded` with useful trend, liquidity, and profile context while preserving compact `!market [ticker]` as a terse read-only market snapshot.

**Architecture:** Keep `!market` as a thin consumer of `tools/market_data_snapshot.py`. Add selected-provider supplements only after a provider has already returned a usable price. Do not call fallback providers solely to fill missing fields. Compact success must still end at `Source: [provider]`.

**Tech Stack:** Python helper (`tools/market_data_snapshot.py`), Midas Markdown rules/skills/evals, provider APIs via existing environment keys.

---

## Non-Negotiable Guardrails

- No changes may create or modify `workspace/tickers/` artifacts.
- No changes may mutate `data/midas_watchlist.json`.
- No API keys, raw credential-bearing URLs, Authorization headers, or secret values may be printed, saved, or logged.
- Default compact success output must remain unchanged and end at `Source: [provider]`.
- No Buy/Sell/Hold, price targets, sizing, entries, exits, trade instructions, Midas scores, setup classifications, or thesis conclusions.
- Market data remains Tier 2 context and must not be presented as evidence of business quality.
- New endpoint calls must be selected-provider supplements, not field-level fallback enrichment.

---

## Stage 1: Low-Risk Parser Fix

**Objective:** Fix FMP percent-change parsing without adding endpoints or changing compact output shape.

**Files:**
- Modify: `tools/market_data_snapshot.py`
- Modify: `evals/market.eval.md`

**Tasks:**

1. In `get_fmp_snapshot()`, parse both FMP percent-change spellings:
   - `changePercentage`
   - `changesPercentage`
2. Keep `source_fields.change_percentage` accurate for whichever key is used.
3. Add/adjust eval coverage showing FMP quote returns `changePercentage` and helper produces non-null `change_percentage`.
4. Run AST syntax verification without bytecode:

```bash
python3 - <<'PY'
import ast, pathlib
ast.parse(pathlib.Path('tools/market_data_snapshot.py').read_text())
PY
```

5. Run one live helper smoke test only if approved for runtime validation:

```bash
python3 tools/market_data_snapshot.py HOOD
```

**Expected result:** Existing compact output can render `$ change / % change` from FMP correctly. No output-section changes yet.

---

## Stage 2: Rule / Contract Approval For Full-Mode Additions

**Objective:** Add the approved endpoint labels and display contract before changing provider behavior.

**Files:**
- Modify: `rules/MARKET_DATA.md`
- Modify: `skills/stock-analysis/market/SKILL.md`
- Modify: `skills/stock-analysis/market/OUTPUT.md`
- Modify: `evals/market.eval.md`

**Tasks:**

1. In `MARKET_DATA.md`, add approved selected-provider supplement endpoint labels:
   - `FMP: profile`, only after FMP quote has selected FMP.
   - `FMP: stock-price-change`, only after FMP quote has selected FMP.
   - `Finnhub: stock/metric`, only after Finnhub quote has selected Finnhub as fallback.
2. Explicitly state these supplements must not trigger provider fallback.
3. In `market/SKILL.md`, define full/expanded additions as market-data-only.
4. In `market/OUTPUT.md`, add full/expanded sections:
   - `## Trend / Liquidity`
   - `## Profile`
5. Add eval cases for:
   - compact unchanged despite new helper fields
   - full mode shows new sections when fields exist
   - fallback provider is not called when FMP succeeds
   - supplement failure degrades gracefully

**Expected result:** Docs/evals authorize the new behavior before helper implementation.

---

## Stage 3: FMP Selected-Provider Supplements

**Objective:** When FMP quote is selected, optionally enrich the selected FMP snapshot with FMP-side data only.

**Files:**
- Modify: `tools/market_data_snapshot.py`
- Modify: `evals/market.eval.md`

**Tasks:**

1. Add a safe `get_fmp_profile_supplement(symbol)` helper.
2. Add a safe `get_fmp_price_change_supplement(symbol)` helper.
3. Call these only after `get_fmp_snapshot(symbol)` returns usable price.
4. If either supplement fails, keep the snapshot usable and add sanitized provider limitation metadata; do not fallback solely because a supplement failed.
5. Add fields to helper output when available:
   - `average_volume`
   - `relative_volume`
   - `beta`
   - `sector`
   - `industry`
   - `country`
   - `ipo_date`
   - `issuer_flags` or equivalent booleans: ETF / ADR / fund / actively trading
   - `price_avg_50`
   - `price_avg_200`
   - `price_vs_50d_avg_percentage`
   - `price_vs_200d_avg_percentage`
   - `performance_5d_percentage`
   - `performance_1m_percentage`
   - `performance_3m_percentage`
   - `performance_6m_percentage`
   - `performance_ytd_percentage`
   - `performance_1y_percentage`
6. Keep `provider_endpoints` as endpoint labels only.
7. Keep raw debug output secret-safe.

**Expected result:** FMP-selected snapshots include full-mode-ready fields without changing compact behavior.

---

## Stage 4: Full / Expanded Output Rendering

**Objective:** Render the new fields only in explicit `full` / `expanded` mode.

**Files:**
- Modify: command rendering logic, wherever `!market` output is assembled
- Modify: `skills/stock-analysis/market/OUTPUT.md` if any display details need refinement
- Modify: `evals/market.eval.md`

**Tasks:**

1. Preserve compact mode exactly:

```md
Price
Market Cap
Change
Volume
Exchange
Source
```

2. In full/expanded mode, add:

```md
## Trend / Liquidity

5D Performance: [x or Not available]
1M Performance: [x or Not available]
3M Performance: [x or Not available]
6M Performance: [x or Not available]
YTD Performance: [x or Not available]
1Y Performance: [x or Not available]
50D Avg: [x or Not available]
200D Avg: [x or Not available]
Price vs 50D Avg: [x or Not available]
Price vs 200D Avg: [x or Not available]
Average Volume: [x or Not available]
Relative Volume: [x or Not available]
Beta: [x or Not available]
```

3. Add optional profile context:

```md
## Profile

Sector: [sector or Not available]
Industry: [industry or Not available]
Country: [country or Not available]
IPO Date: [ipo_date or Not available]
Issuer Type: [Common stock / ETF / ADR / Fund / Not available]
Actively Trading: [Yes / No / Not available]
```

4. Avoid valuation-multiple language by default.
5. Avoid thesis/scoring/recommendation language.

**Expected result:** Full mode becomes materially more useful; compact remains unchanged.

---

## Stage 5: Finnhub Fallback Supplement

**Objective:** Improve full/expanded output when FMP fails and Finnhub is selected.

**Files:**
- Modify: `tools/market_data_snapshot.py`
- Modify: `evals/market.eval.md`

**Tasks:**

1. Add `Finnhub: stock/metric` only after Finnhub quote is selected.
2. Pull only market-snapshot-safe fields:
   - 10-day average trading volume
   - 3-month average trading volume
   - 52-week high / low and dates
   - beta
   - selected price-performance windows
   - market capitalization if profile is unavailable or incomplete
3. Do not add analyst recommendations.
4. Do not add earnings surprises.
5. Do not call Finnhub metrics when FMP succeeded.
6. Add eval coverage for selected-provider-only supplement behavior.

**Expected result:** Finnhub fallback full/expanded output is more useful without becoming a field-level enrichment engine.

---

## Stage 6: Validation / Smoke Tests — Completed

**Objective:** Verify behavior without artifacts, watchlist mutation, or secret exposure.

**Files:**
- Added: `evals/market_stage6_validation.py`
- Modified: `evals/market.eval.md`
- Modified: `skills/stock-analysis/market/SKILL.md`
- Added: `skills/stock-analysis/market/references/stage-6-validation-harness-2026-06-12.md`

**Completed validation:**

1. Python compile verification passed for helper and Stage 6 harness.
2. Offline mock harness passed six provider-policy/rendering cases:
   - FMP success.
   - FMP supplement failure.
   - Finnhub fallback with metric success.
   - Finnhub fallback with metric failure.
   - Alpha Vantage fallback after FMP/Finnhub failure.
   - All-provider failure.
3. Live FMP-success smoke checks passed with HOOD:

```bash
python3 tools/market_data_snapshot.py HOOD
python3 tools/market_data_snapshot.py HOOD --render compact
python3 tools/market_data_snapshot.py HOOD --render full
```

4. Live Finnhub-fallback smoke checks passed with KEEL:

```bash
python3 tools/market_data_snapshot.py KEEL
python3 tools/market_data_snapshot.py KEEL --render compact
python3 tools/market_data_snapshot.py KEEL --render full
```

5. Confirmed:
   - no API secrets printed in rendered smoke outputs
   - compact output final lines preserved
   - full output includes added sections
   - watchlist hash unchanged during Stage 6 smoke tests
   - `workspace/tickers/` / watchlist git status unchanged from the pre-existing baseline

**Expected result:** Stage implementation is ready for use without changing command status or artifact behavior.

---

## Stage 7: Post-Implementation Cleanup — Completed

**Objective:** Keep the system maintainable after validation.

**Files:**
- Modified: `docs/plans/2026-06-12-market-full-mode-upgrades.md`
- Modified: `evals/market.eval.md`
- Modified: `skills/stock-analysis/market/SKILL.md`
- Modified: `skills/stock-analysis/market/references/staged-full-mode-upgrade-plan-2026-06-12.md`
- Modified: `skills/stock-analysis/market/references/stage-4-rendering-and-stage-5-handoff-2026-06-12.md`
- Modified: `skills/stock-analysis/market/scripts/verify_finnhub_supplement_mock.py`
- Added: `skills/stock-analysis/market/references/full-mode-upgrade-completion-2026-06-12.md`

**Completed cleanup:**

1. Recorded durable completion notes without changing helper/provider behavior.
2. Kept detailed implementation/testing notes in references instead of expanding `SKILL.md` substantially.
3. Updated eval run log only after Stage 6 validation had passed.
4. Removed stale active handoff wording that still described Stage 5 as the next recommended stage.
5. Did not promote unrelated commands or alter registry status.
6. Fixed the Stage 5 mock verifier's profile-root path so the documented validation command runs from the Midas profile root.

**Expected result:** The implementation is documented without prompt bloat or policy drift.

---

## Historical Execution Order

1. Stage 1 first — safest, fixes an existing bug.
2. Stage 2 — rules/output/evals before behavior.
3. Stage 3 — FMP-selected supplement implementation.
4. Stage 4 — full/expanded rendering.
5. Stage 5 — Finnhub fallback supplement.
6. Stage 6 — validation.
7. Stage 7 — cleanup/reference updates.

## Historical Stop Points

- Stage 1 was the minimal parser-fix stop point.
- Stage 4 was the FMP/full-rendering stop point.
- Stage 5 was added because fallback full-mode quality justified the selected-provider Finnhub metric supplement.

## Approval State

User approved planning and implementation in stages on 2026-06-12. Stages 1–7 are now completed; future changes should open a new scoped plan rather than extending this completed sequence by default.
