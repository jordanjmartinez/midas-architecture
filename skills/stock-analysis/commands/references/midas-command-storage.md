# Midas Command Storage Reference

Use this when the user asks a meta-question such as “when we do a command, does the information get stored anywhere?” or “where did that command save things?”

## Answer directly first

Do not run a Midas command, refresh data, inspect profiles, or change files just because the user asks where command information is stored. This is a storage/explanation question, not an action request.

## Storage locations to mention

- Stock research artifacts are saved under `workspace/[normalized-lowercase-ticker]/`.
  - Common files: `research.md`, `financials.md`, `thesis.md`, `risk.md`, `earnings.md`, `full.md`, `updates.md`.
- `!gems` artifacts are saved under the Midas workspace gem path used by the gems skill, and should be described as research-candidate artifacts, not recommendations.
- Person tracker artifacts are saved under `workspace/tracker/[normalized-person-name].md`.
- Person tracker watchlist state is stored in `data/tracker_watchlist.json`.
- Stock watchlist state is stored in `data/midas_watchlist.json`.
- Conversation transcripts/session logs may also exist in Hermes’ session database, but they are not the same as Midas research artifacts.
- Persistent memories/skills are only updated when there is durable preference/procedure value or the user explicitly asks; do not imply every command becomes memory.
- Skill-library changes are persistent files under the active profile’s skills directory, e.g. `skills/`; distinguish these from normal Midas command outputs.

## User-facing framing

Keep the answer concise and practical:

- “Yes — if a Midas command creates an artifact, it is saved under the Midas profile workspace/data paths.”
- “Not every command saves the same thing: `!commands` just displays a menu; research commands save Markdown artifacts; watchlist/tracker commands update JSON state and/or profile artifacts.”
- “I should tell you the saved path in the reply whenever I create or update a file.”

## Pitfall

After context compaction or command-heavy sessions, do not resume the previous operational command if the latest user message is a storage/meta-question. Answer the latest question only unless the user explicitly asks to continue the previous task.