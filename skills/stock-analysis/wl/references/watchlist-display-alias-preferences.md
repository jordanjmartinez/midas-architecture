# Watchlist Display and Alias Preferences

Session learning from hardening `!wl` / `!watchlist` / `!list`.

## Durable display preferences

- The visible watchlist title should be `Watchlist`, not `MIDAS Watchlist`.
- `!wl show`, `!watchlist show`, and `!list show` should use the same simple display shape:

```md
## Watchlist

1. [Company Name]
   Ticker: [SYMBOL]
   Date Added: [YYYY-MM-DD or Unknown]
```

- Do not show `Status:` in normal watchlist display unless status later becomes meaningful and explicitly approved.
- Store tickers internally however the command schema requires, but display ticker lines without a leading `$` in `show` output.

## Alias policy

The user approved both `!watchlist` and `!list` as full alias families for `!wl`:

- `!watchlist`, `!watchlist add`, `!watchlist rm`, `!watchlist show`, `!watchlist updates`
- `!list`, `!list add`, `!list rm`, `!list show`, `!list updates`

These aliases should preserve the same behavior, mutation rules, output contract, and artifact rules as the equivalent `!wl` commands.

## Maintenance pitfall

When changing visible watchlist output, patch both:

- `skills/stock-analysis/wl/OUTPUT.md`
- `evals/wl.eval.md`

Do not mutate `data/midas_watchlist.json` for display-only changes.
