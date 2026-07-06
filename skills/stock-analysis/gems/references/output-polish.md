# !gems Output Polish Notes

Use this reference when maintaining or evaluating the `!gems` user-facing chat output. It records durable formatting preferences from live `!gems` testing and should not change candidate selection, scoring, source hierarchy, artifact/index behavior, or watchlist behavior.

## Visible title

- Use `# Hidden Gems | [Theme]`.
- Do not use `MIDAS Gems — [Theme]` as the visible chat/report title.
- Use a pipe separator, not an em dash.
- Keep the theme in Title Case when possible.

## Opening lead

- Put the short lead paragraph directly under the title.
- Do not show a visible `Bottom Line` heading.
- Keep the lead concise; do not expand it into a full report.

## Candidate headers

- Use `TICKER | Company Name`.
- Preserve ticker capitalization exactly as displayed.
- Do not use an em dash between ticker and company name.

Example:

```markdown
1. OSPN | OneSpan Inc.
```

## Screened-out / watch-only lines

- Keep each line to one sentence.
- Do not expand watch-only names into full candidate cards.
- If company name is known, use `TICKER | Company Name — Reason`.
- If company name is not known, use `TICKER | Reason`.
- Do not insert `watch-only` after the pipe.
- Capitalize the first letter of the reason sentence after the pipe or em dash.

Examples:

```markdown
- TENB | Tenable Holdings, Inc. — Strong exposure-management platform, but more discovered than the cleaner candidates.
- TENB | Strong exposure-management platform, but more discovered than the cleaner candidates.
```

## Best next command

- Use exactly one best next command per surfaced candidate.
- Wrap the command in backticks.
- Do not auto-run the command.

Example:

```markdown
Best next command: `!research OSPN`
```

## Preserve

- Concise output.
- 1–5 candidates by default.
- Hidden-Gem Overlay score/wording.
- Evidence Confidence.
- Setup Classification.
- Main risk.
- Screened-out / watch-only names when useful.
- No recommendation language, price targets, position sizing, or trade advice.
