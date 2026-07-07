# Watchlist Display Contract Notes

Use this when maintaining the `!list`, `!watchlist`, or `!list` command family.

Session-learned preferences:

- Treat `!list`, `!watchlist`, and `!list` as full alias families for the same watchlist command behavior.
- For show/display output, keep entries simple and Telegram-readable.
- Do not show `Status:` in `show` output unless status has a real product purpose and the user explicitly approves reintroducing it.
- Preferred entry shape:

```md
1. [Company Name]
   Ticker: TICKER
   Date Added: YYYY-MM-DD or Unknown
```

Implementation guidance:

- Keep internal JSON schema stable unless the user explicitly asks for schema migration.
- It is acceptable for stored tickers to retain `$TICKER` internally while display output renders the bare ticker as `Ticker: TICKER`.
- Patch output contracts and eval expectations together when display shape changes.
- Do not mutate `data/midas_watchlist.json` for output-only patches.
