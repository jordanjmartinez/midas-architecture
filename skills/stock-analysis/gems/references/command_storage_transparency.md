# MIDAS Command Storage Transparency

Use this note when a user asks whether a MIDAS command stores information, or when a command creates artifacts/caches beyond the final chat response.

## General answer pattern

- Answer directly: yes/no/partially.
- Name the exact paths affected by the command.
- Distinguish durable artifacts from ephemeral session/tool logs.
- Mention whether the command updates an index or watchlist.
- Do not imply that candidates are added to the watchlist unless the command explicitly does that.

## `!gems` storage behavior

- Full detailed scan artifact is saved under `workspace/gems/...`.
- `workspace/gems/index.md` is updated automatically.
- Candidates are not automatically added to `data/midas_watchlist.json`.
- If supporting filing extracts, market-data caches, or temporary research files are retained under the artifact folder, include a `Sources` or `Supporting Files` note in the saved artifact so the user can see what was stored.
- Final Telegram response should still end with the normal `Saved to:` and `Updated index:` lines.

## Example concise answer

"Yes. For `!gems`, the full scan is saved to `workspace/gems/[theme]/[subtheme].md` and the gems dashboard is updated at `workspace/gems/index.md`. It does not add names to the watchlist unless you run `!wl add [ticker]`."
