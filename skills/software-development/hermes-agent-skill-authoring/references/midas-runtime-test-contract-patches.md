# MIDAS Runtime-Test Contract Patches

Use when the user reports a runtime test failure for a MIDAS command and asks to patch the command contract without rebuilding or rerunning the command.

## Patch scope

- Patch only the files the user named, usually the command `SKILL.md`, command `OUTPUT.md`, and the relevant `evals/*.eval.md` file.
- Do not run, rebuild, or regenerate the command unless the user explicitly asks.
- Preserve lifecycle status such as `Draft` unless promotion is explicitly requested.

## Output-contract fixes

- Put exact output order, title format, required headings, saved-path wording, and forbidden structures in `OUTPUT.md`.
- Mirror workflow-only logic in `SKILL.md`, especially conditional next-step behavior.
- Keep command output contracts distinct from global MIDAS rules; do not duplicate broad source/scoring/metric standards.

## Regression eval pattern

Add a named regression eval for the observed failure. Include:

- Purpose tied to the failed contract behavior.
- Required section list and heading/order expectations.
- `Must Include` and `Must Not Include` lists.
- Pass criteria that check the saved-path confirmation and guardrails.
- Any conditional behavior, such as choosing Best Next Command based on whether `workspace/tickers/[ticker]/research.md` exists.

## Failure-recovery language patches

When runtime tests reveal a failed company/ticker lookup or similar unresolved-identity failure, patch both the global output rule and the command-specific output contract if the issue is cross-command:

- Use neutral recovery language: `Best next step: Send a valid public-company ticker or exact company name.`
- Include `No artifact saved.` when no command artifact was written.
- Do not suggest a specific real ticker or company as a recovery example unless the user explicitly asked for examples, the ticker/company is part of the current request, or the output is command help/menu text.
- Add a regression eval for the exact failure shape and a coverage-matrix row if the eval file uses one.
- Check related command output contracts only for the same concrete issue; do not patch them just because they are adjacent.

Pitfall: examples like `e.g. !financials HOOD` in failed lookup output can look like prior-run leakage, ticker bias, or an unintended recommendation. Prefer a format-only example such as `Format: !financials [ticker or company name]` only when helpful.

## Compact-output runtime patches

When a compact-mode runtime test passes structure but exposes consistency drift, patch the command `OUTPUT.md` and eval rather than broad workflow files:

- Preserve compact mode as compact: do not promote it into Standard/Full, do not add default artifact saves, and do not rebuild or rerun the command unless requested.
- Require compact evidence labels to match the command contract exactly. For MIDAS financial compact outputs, prefer `Evidence Base / As-of` over generic `Sources:` when that is the tested contract.
- Require metric-definition consistency between compact and deeper modes for the same company. If compact mode cannot support the deeper-mode metric inputs, make the compact output decline calculation explicitly rather than silently switching definitions.
- For FCF specifically, patch both the compact output contract and compact eval to require either the same company-appropriate FCF definition/input set used by Standard/Full or a clear no-calculation sentence when required inputs are unavailable.
- Keep reusable output contracts fully ticker-neutral. Do not include real-ticker FCF examples in command-level `OUTPUT.md` files, even when labeled as examples, because they can leak into unrelated outputs. Put ticker-specific FCF examples only in evals, runtime test notes, or fixture notes.
- In evals, encode both positive requirements (`Evidence Base / As-of`, same company-appropriate FCF definition or no-calculation statement) and negative requirements (no `Sources:` label if disallowed, no real-ticker FCF examples in reusable `OUTPUT.md`, no ticker-specific formula presented as the default, no default save, no overwrite of canonical artifacts).

Pitfall: a compact output can be structurally correct while still drifting in metric definitions or evidence-label naming. Another subtle failure is hardcoding a single ticker's formula into the command-level contract; remove ticker-specific examples entirely from reusable output contracts instead of merely labeling them as examples. Treat these as output-contract regressions, not as reasons to rebuild the command.

## Verification checklist

- Requested old wording is gone across the requested files.
- Replacement wording is present in the expected files.
- Required headings are present exactly.
- Status remains unchanged when requested.
- No runtime workspace artifacts, watchlists, cron jobs, or command outputs were created by the authoring patch itself.
