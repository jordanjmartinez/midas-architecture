# `!earnings` Staged Fixture / Limited Live Test Notes

Use this reference when maintaining or validating the Midas `!earnings` command after output-contract or eval changes.

## Formatting-only fixture test pattern

- Inspect only the command files needed for contract alignment: `SKILL.md`, `OUTPUT.md`, command eval file, and the command's registry row.
- Do not retrieve filings, prices, market data, transcripts, news, consensus estimates, or company data.
- Do not patch during a fixture-only test unless the user explicitly changes scope.
- Evaluate fixture scenarios against the output contract rather than producing live research.
- Fixture coverage should include: normal review, missing 10-Q, missing transcript, consensus unavailable, Key Numbers discipline, guidance/outlook, management-commentary separation, quarter-specific Thesis Impact, quarter-specific Risk Update, non-earnings event boundary, artifact path / false-save, command boundary, and Best Next Command formatting.

## Limited live test pattern

- Run exactly the requested ticker and period scope; do not run other Midas commands as follow-ups.
- Retrieve only the sources needed for the one test.
- Save/replace `workspace/tickers/[ticker]/earnings.md` only when the review completes successfully and the command contract requires saving.
- After writing, verify the artifact exists, the canonical path is used, no legacy `workspace/[ticker]/earnings.md` path was used, no `updates.md` write occurred, and watchlist files were not modified.
- Return a test report rather than a full research report if the user specifically asks for validation.

## Runtime drift watch

`!earnings` may borrow the logic of `!thesis` and `!risk`, but only as lightweight lenses. During fixture or live validation, fail or flag output that expands into:

- a full thesis memo
- bull/base/bear cases
- a 3–5 year thesis rewrite
- a full risk ranking or full risk memo
- a broad `!updates` scan
- a full `!financials`, `!research`, or `!full` packet

## Critical artifact/report checks

- Saved-path line must be truthful: `Saved to: workspace/tickers/[ticker]/earnings.md`.
- No false save claim on incomplete/failure outputs.
- No write or claimed write to `updates.md`.
- No watchlist mutation unless the user explicitly invokes a watchlist workflow.
- No Buy/Sell/Hold, price target, position sizing, or trade advice.
