# Full-Mode Price Action Layout — Market Cap, No Shares Outstanding

Date: 2026-06-12

## Trigger

Use this note when maintaining `!market full` / `!market expanded` rendering, docs, or evals.

## User correction

FMP does not reliably provide shares outstanding. For normal successful full/expanded output, do not show a separate `## Market Size` section and do not render `Shares Outstanding:`.

The former `## Quote` section should be renamed to:

```md
## Price Action
```

Within `## Price Action`, render `Market Cap` above `Price`:

```md
## Price Action

Market Cap: ...
Price: ...
Change: ...
Previous Close: ...
Open: ...
Day High / Low: ...
52-Week High / Low: ...
```

## Scope

This is a full/expanded-mode layout rule only.

Do not change:

- compact output
- provider selection
- fallback behavior
- supplement calls
- raw/debug/source output
- watchlists
- artifacts
- scoring/classification/research behavior

## Verification checklist

Run the normal market validation path after layout changes:

```bash
python3 -m py_compile tools/market_data_snapshot.py evals/market_stage6_validation.py skills/stock-analysis/market/scripts/verify_finnhub_supplement_mock.py
python3 evals/market_stage6_validation.py
python3 skills/stock-analysis/market/scripts/verify_finnhub_supplement_mock.py
python3 tools/market_data_snapshot.py HOOD --render full
git diff --check
```

Confirm:

- `## Profile` appears before `## Price Action`
- `Market Cap:` appears before `Price:`
- `## Quote` is absent
- `## Market Size` is absent
- `Shares Outstanding:` is absent
- no watchlist or artifact files are changed
