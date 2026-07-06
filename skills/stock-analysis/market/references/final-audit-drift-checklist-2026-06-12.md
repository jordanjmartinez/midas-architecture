# `!market` Final Audit / Drift Checklist — 2026-06-12

Use this reference when the user asks for a final `!market` audit, stale-data check, drift check, or post-layout verification.

## Purpose

Catch drift between runtime renderer, active docs, evals, references, and user-facing output after market command changes.

## Audit Scope

Check all active contracts together:

- `tools/market_data_snapshot.py`
- `skills/stock-analysis/market/SKILL.md`
- `skills/stock-analysis/market/OUTPUT.md`
- `skills/stock-analysis/market/references/full-mode-display-contract.md`
- `evals/market.eval.md`
- `evals/market_stage6_validation.py`
- `skills/stock-analysis/market/scripts/verify_finnhub_supplement_mock.py`

Historical references may preserve old terms if clearly labeled historical/superseded. Active docs must not present stale layout as current behavior.

## Stale-Term Scan

For active runtime/docs/evals, stale-positive usages should be absent except negative assertions, failure paths, or historical notes:

- `## Quote`
- `## Market Size`
- `Shares Outstanding:`
- `## Trend / Liquidity`
- normal-success `## Source / Limitations`
- normal-success `Fallbacks Used:`
- normal-success `Limitations:`

Current full/expanded success layout must be:

```md
## Profile
## Price Action
## Liquidity
## Trend
```

`## Price Action` must show `Market Cap:` above `Price:`.

## Runtime Verification

Run the standard validation path:

```bash
python3 -m py_compile tools/market_data_snapshot.py evals/market_stage6_validation.py skills/stock-analysis/market/scripts/verify_finnhub_supplement_mock.py
python3 evals/market_stage6_validation.py
python3 skills/stock-analysis/market/scripts/verify_finnhub_supplement_mock.py
python3 tools/market_data_snapshot.py HOOD --render compact
python3 tools/market_data_snapshot.py HOOD --render full
python3 tools/market_data_snapshot.py RCAT --render compact
python3 tools/market_data_snapshot.py RCAT --render full
python3 tools/market_data_snapshot.py RCAT
 git diff --check
```

Expected:

- HOOD FMP compact/full path works.
- RCAT fallback path works when FMP returns plan-limited status such as `402` and Finnhub returns usable price.
- Compact success shows `Source: [provider]` directly under `As of:` and no profile/trend/full sections.
- Full success shows Source directly under As of, no routine footer clutter, no provider error block, no recommendation language.
- Fallback detail appears only in JSON/debug/source/failure-style output, not normal compact/full success.

## User-Facing Summary Style

Keep the final audit summary concise:

- state PASS/issue status
- list what was checked
- mention any doc drift fixed
- say `Verified; no watchlist/artifact changes` if relevant

Do **not** dump raw SHA/checksum strings unless the user explicitly asks for them.
