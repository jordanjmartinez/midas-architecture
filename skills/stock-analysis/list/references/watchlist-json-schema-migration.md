# Watchlist JSON schema migration notes

During a Telegram command session, the active file existed at:

`data/midas_watchlist.json`

It contained a legacy/simple schema:

```json
{
  "watchlist": []
}
```

The agent added entries as strings:

```json
{
  "watchlist": ["KEEL", "RKLB"]
}
```

The class-level `wl` skill expects richer objects:

```json
{
  "watchlist": [
    {
      "company_name": "Example Company Inc.",
      "ticker": "EXMP",
      "date_added": "YYYY-MM-DD",
      "status": "Monitoring"
    }
  ]
}
```

Future `!list` handlers should accept both shapes. On load:

1. If an entry is a string, treat it as a ticker.
2. Strip a leading `$` and uppercase the ticker.
3. Resolve company name when practical using SEC/company sources; if unavailable, preserve the ticker as `company_name` temporarily rather than dropping it.
4. Add `date_added` if missing using the current date.
5. Add `status: "Monitoring"` if missing.
6. Save the migrated object schema after add/remove operations.

Also observed: the user used uppercase command text (`!WL add $RKLB`). Treat bang commands and subcommands case-insensitively.
