# `!earnings` Activation and Runtime Validation Notes

Use this reference when maintaining, activating, or regression-testing the `!earnings` command after changes.

## Staged activation pattern proven in this session

1. Fixture/format review first: verify `SKILL.md`, `OUTPUT.md`, eval coverage, registry row, and canonical artifact behavior before live use.
2. Limited live test second: run exactly one ticker, retrieve only earnings-specific sources, and save only `workspace/tickers/[ticker]/earnings.md` if the command completes successfully.
3. Read-only activation review third: inspect command files, eval, registry row, and the live-test artifact; do not retrieve live data or patch during the review.
4. Metadata cleanup, if needed: patch only the specific registry metadata mismatch; keep status unchanged.
5. Activation patch last: change only the registry status from `Planned` to `Active`; do not alter metadata, skill files, evals, workspace artifacts, or watchlist files.

## Registry checks before activation

For `!earnings`, the registry row should reflect:

- Status: `Active` only after explicit activation approval.
- Classification: `Optional`.
- Scoring: `Optional`.
- Metrics: `Required`.
- Artifacts: `Yes`.
- Skill path: `skills/stock-analysis/earnings/SKILL.md`.
- Output path: `skills/stock-analysis/earnings/OUTPUT.md`.
- Eval path: `evals/earnings.eval.md`.

## Runtime validation checks

A healthy live `!earnings` output should remain concise and quarter-specific. Verify:

- Sources Used names earnings release / 8-K, 10-Q if available, and transcript status.
- Key Numbers are compact and period-labeled.
- GAAP vs non-GAAP labels are clear.
- FCF is defined if used.
- Consensus is omitted or explicitly unavailable unless reliable consensus was actually retrieved.
- Management commentary separates reported facts, claims, and forward-looking assumptions.
- Guidance is bounded to disclosed company outlook and does not become a forecast model.
- Thesis Impact and Risk Update stay quarter-specific.
- No drift into `!financials`, `!thesis`, `!risk`, `!updates`, `!full`, price-action recap, or recommendation language.
- Artifact confirmation appears only after writing `workspace/tickers/[ticker]/earnings.md`.
- No `updates.md`, watchlist, or legacy `workspace/[ticker]/earnings.md` write occurs.

## Watch item

Transcript availability can tempt over-expansion. Even when transcript detail exists, summarize only the management commentary needed to explain the quarter; do not turn `!earnings` into a full transcript memo or thesis rewrite.
