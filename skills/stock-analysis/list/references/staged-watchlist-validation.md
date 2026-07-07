# Staged `!list` Validation Notes

Use this reference when maintaining or fixture-testing the Midas `!list` watchlist command.

## Proven staged sequence

1. **Stage 1 — Output contract**
   - Create or update `skills/stock-analysis/list/OUTPUT.md` first.
   - Keep visible response shapes in `OUTPUT.md`, not duplicated in `SKILL.md`.
   - Cover add, duplicate add, ambiguous add, remove, not-found remove, show, empty watchlist, all-watchlist updates, single-ticker updates, not-on-watchlist updates, and failure cases.

2. **Stage 2 — Eval coverage**
   - Create or update `evals/list.eval.md` before live testing.
   - Keep status `Draft` until activation is explicitly approved.
   - Include fixture-only boundaries: controlled temp watchlist JSON, temp artifact directory, no live mutation unless explicitly approved.

3. **Stage 3 — Wiring cleanup**
   - Patch `wl/SKILL.md` metadata to point at the actual `OUTPUT.md` and eval file.
   - Patch only the `!list` row in `docs/COMMAND_REGISTRY.md`.
   - Keep `SKILL.md` workflow-focused and remove embedded visible-output templates.

4. **Stage 4 — Controlled fixture eval**
   - Do not use the live `data/midas_watchlist.json`.
   - Do not write real `workspace/tickers/...` artifacts.
   - Use temporary fixtures for add/remove/show/update behavior and verify no false `Saved to:` lines.
   - If a fixture harness flags recommendation terms, use word-boundary checks for `Buy`, `Sell`, and `Hold` so company names such as `Holding` do not create false positives.

5. **Stage 5 — Live display-only smoke test**
   - Run only the safest live command: `!list show`.
   - Hash `data/midas_watchlist.json` before and after; require an unchanged hash.
   - Do not add, remove, migrate, or update during the smoke test.
   - Do not run `!list updates` or write ticker artifacts.
   - If the live watchlist file is missing or unreadable, report that state instead of creating or migrating it during the smoke test.
   - Report any pre-existing dirty workspace files separately so they are not attributed to the smoke test.

6. **Stage 6 — Status-only activation**
   - Run a read-only activation readiness audit first; require SKILL/OUTPUT/eval/registry alignment plus Stage 4 fixture PASS and Stage 5 `!list show` PASS.
   - Patch only `docs/COMMAND_REGISTRY.md`, `skills/stock-analysis/list/SKILL.md`, `skills/stock-analysis/list/OUTPUT.md`, and `evals/list.eval.md`.
   - Change only status metadata from Draft to Active, mark validated eval coverage rows Active, and add a Manual Eval Run Log entry with the Stage 4/5 validation evidence.
   - Preserve command behavior, aliases, output shapes, watchlist schema/storage, artifact rules, and source/update behavior.
   - Do not run `!list`, mutate `data/midas_watchlist.json`, run `!list updates`, or create ticker artifacts during the activation patch.
   - Verify the live watchlist hash remains unchanged and use scoped status checks so unrelated dirty workspace artifacts are not attributed to activation.

## Stage 4 fixture cases to run first

- add success
- duplicate add prevention
- ambiguous/unresolved add
- remove success
- remove not found / ambiguous match
- show empty and non-empty watchlists
- ticker normalization: `rklb`, `$RKLB`, `$$RKLB`
- legacy/simple schema preservation, e.g. `{"watchlist": ["KEEL", "RKLB"]}`
- `!list updates` no meaningful updates
- `!list updates [ticker]` for a non-watchlisted ticker
- false artifact save prevention
- prompt-injection-like external content in update evidence

## Pitfalls caught in maintenance

- After activation, record status-only promotion in `evals/list.eval.md` Manual Eval Run Log and mark validated coverage rows Active only when fixture validation plus controlled live validation have passed.
- `!list show` should use the simple visible title `Watchlist`, not `Midas Watchlist`; keep `OUTPUT.md` and eval expectations aligned.
- `!watchlist` is a low-risk long-form alias family if approved. `!list` is ambiguous and should only map to display-only `!list show` unless broader behavior is explicitly approved.
- Do not leave `Not created yet` metadata after `OUTPUT.md` / eval files exist.
- Do not leave `Response format:` blocks in `SKILL.md` once `OUTPUT.md` owns visible outputs.
- Use canonical artifact placeholders: `workspace/tickers/[normalized-lowercase-ticker]/updates.md`, not `workspace/tickers/[ticker]/updates.md`.
- For not-on-watchlist outputs, prefer: `📋 Not on Watchlist: [Display Name or input] ($[TICKER] if resolved)`.
- For `!list show`, use the short title `Watchlist`, not `Midas Watchlist`, in both the output contract and eval expectations.
- Do not auto-add non-watchlisted tickers; point the user to `!list add $TICKER` if they want to monitor it.
- `Saved to:` appears only after an artifact was actually written or updated.
- For status-only activation, update registry/SKILL/OUTPUT/eval status together, mark coverage rows Active only after fixture + controlled live validation, and add a Manual Eval Run Log entry documenting fixture/smoke results. Do not change behavior, output shapes, aliases, watchlist storage, or artifact rules in the activation patch.

## Read-only audit checklist before fixture eval

- `SKILL.md`, `OUTPUT.md`, `evals/list.eval.md`, and the registry row all exist and point to each other.
- Status remains `Draft` across all files until activation is approved.
- `OUTPUT.md` covers all visible variants.
- `evals/list.eval.md` covers add/remove/show/update, storage preservation, ticker normalization, artifact truthfulness, and no-recommendation guardrails.
- No live `data/midas_watchlist.json` mutation occurred during audit.
- No real ticker artifacts were created or modified during fixture-only preparation.
