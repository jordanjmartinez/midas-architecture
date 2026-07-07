# MIDAS Profile Command Memory Sync

Use this reference when MIDAS stock-analysis command wording, preferred aliases, or artifact behavior changes.

## Why this exists

MIDAS command behavior is encoded in skills, but the Midas profile memory also carries a compact command summary that is injected into future sessions. If command wording changes only in skills, later sessions can still start with stale preferred commands from `USER.md`.

## Files to keep aligned

- Command menu skill: `skills/stock-analysis/commands/SKILL.md`
- Affected command skill(s): `skills/stock-analysis/<skill>/SKILL.md`
- Midas user profile memory: `memories/USER.md`

## Update pattern

1. Patch the affected command skill first, preserving its original analysis logic.
2. Patch `commands/SKILL.md` so `!commands` shows only the current preferred command wording.
3. If preferred commands changed, update the command paragraph in `USER.md` so the injected user profile matches the current menu.
4. Keep deprecated fallbacks functional when the user asks for backward compatibility, but remove them from the visible command menu unless explicitly requested otherwise.
5. Verify stale aliases are not listed as preferred commands. It is OK for them to appear only in an explicit “Do not use … as preferred commands” sentence.

## Verification examples

- Search `commands/SKILL.md` for deprecated visible menu aliases such as `!help`, `!update-thesis`, or `!wl check`.
- Search `USER.md` for the same aliases and confirm they are absent from the preferred-command list.
- Confirm new preferred commands appear in both the command menu and the Midas profile memory when they are durable preferences.

## Current MIDAS command-memory convention

The current preferred thesis-update command is `!thesis update [ticker]`; `!update-thesis [ticker]` is only a deprecated fallback.

The current watchlist update command is `!wl updates`; `!wl check` is not preferred.

The current command menu command is `!commands`; `!help` is not preferred.
