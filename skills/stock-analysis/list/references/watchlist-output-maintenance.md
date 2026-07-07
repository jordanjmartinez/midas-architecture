# Watchlist output maintenance notes

Use this reference when changing `!list`, `!watchlist`, or `!list` visible output or aliases.

## Durable lessons from activation and cleanup

- Keep `!list show` title as `Watchlist`, not `Midas Watchlist`.
- For display-only watchlist output, omit `Status:` while all entries have the same non-actionable status.
- Preferred `!list show` entry shape:

```md
1. Company Name
   Ticker: SYMBOL
   Date Added: YYYY-MM-DD
```

- Store tickers in JSON with one leading `$`, but display the `Ticker:` line without `$` in `!list show`.
- `!watchlist` and `!list` are full alias families for `!list`, including add/rm/show/updates.
- When alias or display fields change, patch all contract surfaces together:
  - `skills/stock-analysis/list/SKILL.md`
  - `skills/stock-analysis/list/OUTPUT.md`
  - `evals/list.eval.md`
  - `docs/COMMAND_REGISTRY.md`
- Do not mutate `data/midas_watchlist.json` for display/alias/contract patches.
- For live smoke tests, prefer display-only `!list show` / `!list show` before mutation-capable commands.

## Pitfall

Do not preserve a visible field just because it exists in storage. The JSON `status` field may remain for future lifecycle support, but visible output should stay useful and uncluttered.