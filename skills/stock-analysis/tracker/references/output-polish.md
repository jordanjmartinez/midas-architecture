# Tracker Output Polish

This is command-local support for !track. It does not replace GLOBAL.md, SOURCES.md, CLASSIFICATIONS.md, SCORING.md, OUTPUT.md, ARTIFACTS.md, or tracker contracts.

## Authority boundary

OUTPUT.md owns visible display templates and section order. This file only supports compact output hygiene and recurring formatting pitfalls.

## Telegram-safe output

- Keep tracker output useful before exhaustive.
- Do not show raw URLs by default; Telegram link previews can overwhelm the message.
- If the user asks for sources, use concise source names by default and provide raw links only if asked.
- Do not show raw JSON, full disclosure dumps, scraper output, or long source tables in visible output by default.
- Keep section headings visually clear and separated by blank lines.

## Lead-card hygiene

- Separate disclosed fact, inferred lead, and next diligence step.
- Use plain-English reasons tied to the disclosure or filing change, not generic stock-quality claims.
- Candidate cards should explain why the name made the ranked section and why the signal might be weak when relevant.
- Do not duplicate the same ticker across ranked and lower-signal sections unless the repeat adds distinct source-type context.
- Do not bury relevant lower-signal tickers in a vague grouped list if each needs a specific demotion reason.
- Do not fill the ranked section just to reach a quota. If no clean company-level lead exists, say so.

## Bloat controls

Avoid by default:

- Full source dumps.
- Raw filing tables.
- Long examples or fixture-style cards.
- Separate internal scoring fields.
- Hidden contract labels or internal gate names.
- Repeated generic disclosure-lag caveats in every card.
- Saved-path or artifact-state explanations unless needed.

Prefer:

- One compact source caveat when material.
- Ticker-specific caveats only when they change the read.
- A concise best next command only when a researchable company-level ticker lead exists.
- Lower-signal context with specific reasons.

## Source caveat display

- Show disclosure lag, stale/as-of status, options ambiguity, convenience-source limits, and identity uncertainty when material.
- Do not imply current ownership, recent buying/selling intent, wrongdoing, or non-public information from delayed disclosures.
- Tracked activity is a research lead only, not a copy-trading signal or recommendation.

## Template boundary

- Do not copy old output templates into this reference.
- Do not add visible fields or section order here.
- If display behavior must change, patch OUTPUT.md under an approved scope.
