# `!wl` Output Contract

Status: Active
Command: `!wl`
Aliases: `!wl add`, `!wl rm`, `!wl show`, `!wl updates`, `!watchlist`, `!watchlist add`, `!watchlist rm`, `!watchlist show`, `!watchlist updates`, `!list`, `!list add`, `!list rm`, `!list show`, `!list updates`
Purpose: Define the visible output shape for the MIDAS watchlist command.

`!wl` manages the persistent MIDAS stock watchlist stored at:

`/home/jordan/.hermes/profiles/midas/data/midas_watchlist.json`

`!watchlist` and `!list` are full alias families for `!wl`; their add/rm/show/updates variants use the same output shapes and guardrails as the corresponding `!wl` variant.

The watchlist JSON file is the source of truth. Do not store watchlist entries in memory.

## Global Output Rules

- Keep outputs short and Telegram-readable.
- Use plain English.
- Use ticker format with one leading `$`, for example `$RKLB`.
- Do not give Buy, Sell, Hold, price targets, position sizing, or trade execution advice.
- Do not describe watchlist entries as recommendations.
- Do not run or imply deep research from `!wl add`, `!wl rm`, or `!wl show`.
- Do not auto-add tickers from `!gems`, `!track`, `!research`, or any other command.
- Show saved artifact paths only when an artifact was actually written or updated.
- If no artifact was written, do not show a fake `Saved to:` line.
- If company identity or ticker mapping is ambiguous, ask for clarification instead of guessing.

## `!wl add [ticker or company]`

Use when adding a stock to the persistent watchlist.

### Success

```md
Added to Watchlist: [Company Name] ($TICKER)
Status: Monitoring
Date Added: [YYYY-MM-DD]
```

### Already on watchlist

```md
Already on Watchlist: [Company Name] ($TICKER)
Status: [Status]
Date Added: [YYYY-MM-DD or Unknown]
```

### Ambiguous input

```md
Watchlist Add Needs Clarification

I found multiple possible matches for `[input]`:

1. [Company Name] ($TICKER) — [exchange/source if known]
2. [Company Name] ($TICKER) — [exchange/source if known]

Which one should I add?
```

### Unable to resolve

```md
Watchlist Add Failed

I could not confidently resolve `[input]` to a public-company ticker.

Try again with the ticker symbol or official company name.
```

## `!wl rm [ticker or company]`

Use when removing a stock from the persistent watchlist.

### Success

```md
Removed from Watchlist: [Company Name] ($TICKER)
```

### Not found

```md
Not on Watchlist: [input]

No matching ticker or company name was found in the MIDAS watchlist.
```

### Ambiguous match

```md
Watchlist Remove Needs Clarification

I found multiple watchlist matches for `[input]`:

1. [Company Name] ($TICKER) — Added [YYYY-MM-DD or Unknown]
2. [Company Name] ($TICKER) — Added [YYYY-MM-DD or Unknown]

Which one should I remove?
```

## `!wl show`

Use when displaying the current watchlist.

### Non-empty watchlist

```md
Watchlist

1. [Company Name]
   Ticker: TICKER
   Date Added: [YYYY-MM-DD or Unknown]

2. [Company Name]
   Ticker: TICKER
   Date Added: [YYYY-MM-DD or Unknown]

3. [Company Name]
   Ticker: TICKER
   Date Added: [YYYY-MM-DD or Unknown]
```

### Empty watchlist

```md
Watchlist

Your MIDAS watchlist is currently empty.
```

### Storage unavailable or unreadable

```md
Watchlist Unavailable

I could not read the MIDAS watchlist file.

Source of truth: `/home/jordan/.hermes/profiles/midas/data/midas_watchlist.json`
Issue: [short explanation]
```

## `!wl updates`

Use when checking all watched stocks for important recent updates.

This is a short monitoring scan, not a deep research command.

### Standard output

```md
Watchlist Updates

As of: [YYYY-MM-DD]

1. [Company Name] ($TICKER)
- Important update: [Yes / No]
- Update type: [Price Move / Filing / Earnings / Guidance / News / Legal / Crypto or Security / Financing / M&A / Other / None]
- Summary: [brief summary]
- Likely driver: [brief explanation if a major price move or material update is identified]
- Saved to: `workspace/tickers/[normalized-lowercase-ticker]/updates.md` [only if an updates artifact was actually saved]

2. [Company Name] ($TICKER)
- Important update: [Yes / No]
- Update type: [Price Move / Filing / Earnings / Guidance / News / Legal / Crypto or Security / Financing / M&A / Other / None]
- Summary: [brief summary]
- Likely driver: [brief explanation if relevant]
- Saved to: `workspace/tickers/[normalized-lowercase-ticker]/updates.md` [only if saved]
```

### No meaningful updates

```md
Watchlist Updates

As of: [YYYY-MM-DD]

No meaningful watchlist updates found.
```

### Empty watchlist

```md
Watchlist Updates

Your MIDAS watchlist is currently empty.
```

## `!wl updates [ticker or company]`

Use when checking one watchlist entry for important recent updates.

### Stock is on watchlist

```md
Watchlist Update | [Company Name] ($TICKER)

As of: [YYYY-MM-DD]

Important update: [Yes / No]
Update type: [Price Move / Filing / Earnings / Guidance / News / Legal / Crypto or Security / Financing / M&A / Other / None]
Summary: [brief summary]
Likely driver: [brief explanation if relevant]
Saved to: `workspace/tickers/[normalized-lowercase-ticker]/updates.md` [only if an updates artifact was actually saved]
```

### Stock is not on watchlist

```md
Not on Watchlist: [Company Name or input] ($TICKER if resolved)

This ticker is not currently in the MIDAS watchlist.

If you want to monitor it, use:
`!wl add $TICKER`
```

## Update Scan Boundaries

`!wl updates` may summarize:

- Major price movement.
- New 10-K, 10-Q, or 8-K filings.
- Earnings releases.
- Guidance updates.
- Investor presentations.
- Major company announcements.
- Major company news.
- Regulatory or legal developments.
- Crypto, blockchain, or security incidents.
- Financing, dilution, debt, or M&A.
- Management changes.
- Major product, customer, or platform issues.

`!wl updates` must not create:

- A full research report.
- A thesis.
- A risk report.
- A financial report.
- An earnings review.
- A full memo.

Route deeper work to the relevant command only when useful:

- `!research [ticker]`
- `!financials [ticker]`
- `!risk [ticker]`
- `!thesis [ticker]`
- `!earnings [ticker]`

Do not auto-run those commands from `!wl`.

## Artifact Display Rules

- Add/remove/show operations do not create ticker research artifacts.
- `!wl updates` may write `workspace/tickers/[normalized-lowercase-ticker]/updates.md` only when a meaningful update is found.
- Show `Saved to:` only after the artifact was actually written or updated.
- If no meaningful update was found, do not create or claim an artifact.
- Follow `/home/jordan/.hermes/profiles/midas/rules/ARTIFACTS.md` for save-order and path discipline.

## Source Limits

Use a short source-limit line only when material:

```md
Source limits: [brief limitation, such as source unavailable, filing feed lag, quote/news source stale, or company identity ambiguous]
```

Do not add a long source-limit section to normal watchlist add/remove/show output.

## Failure Output

Use when the command cannot safely complete.

```md
Watchlist Action Failed

Action: [Add / Remove / Show / Updates]
Reason: [short explanation]
Source of truth: `/home/jordan/.hermes/profiles/midas/data/midas_watchlist.json`
```

Never silently overwrite, drop, or duplicate watchlist entries when storage or schema is uncertain.
