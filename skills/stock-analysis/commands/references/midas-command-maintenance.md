# MIDAS Command Maintenance Reference

Use this reference when changing MIDAS stock-analysis command wording, aliases, workspace artifact behavior, or adding a new MIDAS command skill.

## Command menu rules

- `commands/SKILL.md` controls the `!commands` workflow; `commands/OUTPUT.md` is the visible compact menu display contract. Preferred commands and status labels should be reflected in `OUTPUT.md`, not duplicated ad hoc in chat.
- Deprecated fallbacks may remain functional in their owning skill, but should be removed from the visible `!commands` menu unless the user explicitly wants them shown.
- When replacing a command, update all of these together:
  - command list in the menu display contract
  - examples section
  - related skills/frontmatter when a new command skill is introduced
  - stale-alias mentions in the visible menu
  - critical rules when the new command has guardrails such as "not recommendations" or "do not auto-add to watchlist"
- Keep the visible menu concise and Telegram-friendly.

## Status-sync / eval metadata patches

When the user asks for a status-only sync patch after activation or audit:

1. Respect the scoped file list exactly. If they name only `skills/stock-analysis/commands/OUTPUT.md` and `evals/commands.eval.md`, do not edit the registry, owning command skills, tracker files, watchlists, or workspace artifacts.
2. Patch only stale display/eval metadata such as `Draft` -> `Active`; do not change command behavior, aliases, artifact wording, lookup behavior, or menu grouping unless explicitly requested.
3. Keep `!commands` menu-only: lookup remains deferred, `!help` remains unsupported, no research execution is added, and no artifact behavior is introduced.
4. Verify with scoped checks: inspect the two allowed files for the expected status labels and run `git diff --check -- skills/stock-analysis/commands/OUTPUT.md evals/commands.eval.md` from the MIDAS profile root.
5. In the final response, report files changed, exact status-sync updates, behavior unchanged, tracker/watchlists/artifacts untouched, and the scoped `git diff --check` result.

## Adding a new stock-analysis command skill

When the user asks to create a new MIDAS command skill:

1. Create the skill under `/home/jordan/.hermes/profiles/midas/skills/stock-analysis/[name]/SKILL.md` unless the user specifies a different path.
2. If the supplied frontmatter description contains colons, dollar ranges, brackets, or long punctuation-heavy text, use a YAML folded scalar:
   ```yaml
   description: >-
     Use when ...
   ```
   Then validate that the frontmatter parses.
3. Update `commands/SKILL.md` only when the user asks to update the command menu.
4. When updating `commands/SKILL.md`, update:
   - `metadata.hermes.related_skills`
   - visible command list
   - examples, if useful
   - critical rules / guardrails for the new command
5. Do not modify watchlist storage or JSON schema when adding discovery, update, or research commands unless the user explicitly asks.

## Alias/deprecation pattern

- Preferred command goes in `commands/SKILL.md`.
- Deprecated fallback stays documented only in the implementation/fallback skill.
- Example: `!thesis update [ticker]` is the preferred thesis-update command; `!update-thesis [ticker]` remains a backward-compatible fallback in `update_thesis/SKILL.md` but should not appear in the visible menu.

## Thesis update living-file behavior

- `!thesis [ticker]` creates or rebuilds `workspace/tickers/[ticker]/thesis.md`.
- `!thesis update [ticker]` treats `workspace/tickers/[ticker]/thesis.md` as the latest living thesis file.
- Thesis updates should load the living thesis first, then review available workspace artifacts when present:
  - `updates.md`
  - `earnings.md`
  - `research.md`
  - `financials.md`
  - `risk.md`
- Thesis updates overwrite `workspace/tickers/[ticker]/thesis.md` by default.
- Do not create timestamped thesis history files or a separate `thesis_update.md` unless the user explicitly asks to preserve versions.
- End thesis update responses with: `Saved to: workspace/tickers/[ticker]/thesis.md`.

## Watchlist command changes

- Do not change watchlist storage or JSON schema unless explicitly asked.
- Watchlist storage remains `/home/jordan/.hermes/profiles/midas/data/midas_watchlist.json`.
- Command wording changes like `!wl check` -> `!wl updates` should not modify `!wl add`, `!wl rm`, or `!wl show` behavior.
- Watchlist update scans should stay short and should not trigger full research, financials, thesis, risk, earnings, or full memo unless explicitly asked.

## Workspace artifact commands

- Research artifact outputs save under `/home/jordan/.hermes/profiles/midas/workspace/[normalized-lowercase-ticker]/`.
- Use the normalized lowercase ticker for folder names; strip a leading `$` from user input.
- Overwrite the same analysis file by default unless the user asks to preserve versions.
- End saved-artifact responses with the short confirmation line: `Saved to: workspace/tickers/[ticker]/[file].md`.
- Discovery artifacts such as `!gems` save under `workspace/gems/[file].md` and should remain research candidates, not recommendations.
- `!gems` candidates must not be added to the watchlist automatically; the user chooses manually with `!wl add [ticker]`.

## Verification commands

Use grep-style checks after command renames:

```bash
grep -Rni "old-command" /home/jordan/.hermes/profiles/midas/skills/stock-analysis/commands/SKILL.md || true
grep -Rni "new-command" /home/jordan/.hermes/profiles/midas/skills/stock-analysis/commands/SKILL.md
```

For watchlist command renames, also check `wl/SKILL.md` directly for stale command strings.

For new command skills, validate at minimum:

- file exists at the requested path
- YAML frontmatter parses
- description length is within Hermes limits
- `commands/SKILL.md` contains the new visible commands if menu update was requested
- guardrails requested by the user appear in the owning skill and/or command menu
