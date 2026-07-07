# Staged `!market` Full-Mode Upgrade Plan — 2026-06-12

Use this reference when continuing `!market` upgrades after the June 2026 audit/plan session.

Canonical plan artifact:

```md
docs/plans/2026-06-12-market-full-mode-upgrades.md
```

## Durable implementation lessons

- Treat compact `!market [ticker]` as a frozen contract unless the user explicitly approves a compact-output change.
- Fix correctness bugs before expanding provider calls. The first low-risk target was the FMP percent-change parser: support both `changePercentage` and `changesPercentage`.
- Add rule/contract/eval updates before enabling materially new full-mode behavior.
- Provider supplements should be selected-provider only:
  - If FMP quote wins, optional supplements may use FMP `profile` and `stock-price-change`.
  - If Finnhub wins as fallback, optional supplements may use Finnhub `stock/metric`.
  - Do not call fallback providers merely to fill missing supplemental fields.
- Full/expanded output may add market-data-only sections such as `Trend / Liquidity` and `Profile`, but must not drift into thesis, recommendation, score, setup classification, or filing-backed research.
- Validate in stages: syntax/AST, fixture or mock evals, then scoped live smoke tests. Confirm read-only behavior: no workspace/watchlist mutation and no secrets printed.

## Recommended stage order

1. Low-risk parser fix for FMP percent-change field variants.
2. Rule/contract/eval approval for selected-provider supplements.
3. FMP selected-provider supplements.
4. Full/expanded rendering updates. Completed in Stage 4: helper-side `--render compact|full|expanded` and positional full mode were added while preserving default JSON output and compact final-line behavior.
5. Finnhub fallback supplement. Completed in Stage 5: full/expanded mode now enriches Finnhub-selected fallback snapshots with Finnhub `stock/metric` fields without changing compact mode or provider fallback rules.
6. Validation and smoke tests. Completed in Stage 6: offline mock harness plus live HOOD/KEEL smoke checks verified provider policy, compact/full rendering contracts, secret hygiene, and no additional workspace/watchlist mutation.
7. Cleanup and reference/eval-run-log updates only after actual validation. Completed in Stage 7: stale handoff language was cleaned, final completion notes were added, and no provider/helper/rendering behavior was changed.

## Final status

Stages 1–7 are complete. Future `!market` changes should start from a new scoped plan, update rules/evals before behavior, and re-run the Stage 6 validation harness.
