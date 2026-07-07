---
name: promote
description: Use when the user invokes !promote [ticker] or /promote [ticker], or asks to promote a ticker's completed research to the Pathos Library. Requires research.md, financials.md, thesis.md, and risk.md to exist and be fresh; synthesizes the handoff packet and registers it. Does not run other commands.
version: 0.1.0
author: Midas / Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [stocks, pipeline, handoff, pathos-library, promotion]
    related_skills: [research, financials, thesis, risk]
---

# MIDAS Command Skill: !promote

## Registry Metadata

Command: `!promote`
Aliases: `/promote`
Category: `Full Report`
Status: `Draft`
Skill Path: `skills/stock-analysis/promote/SKILL.md`
Output Path: `skills/stock-analysis/promote/OUTPUT.md`
Eval File: `evals/promote.eval.md`
Uses Classification: `Required`
Uses Scoring: `Required`
Uses Metrics: `Optional`
Writes Artifacts: `Yes`
Output Modes: `Not supported` (single standard output shape; no Compact/Full modes)
Primary Global Rules: `GLOBAL.md, COMMAND_INTERFACE.md, SOURCES.md, CLASSIFICATIONS.md, SCORING.md, OUTPUT.md, ARTIFACTS.md, CONTRACT_AUTHORITY.md`

## Purpose

`!promote [ticker]` is the MIDAS pipeline exit. When the four core artifacts
for a ticker are complete and fresh, it synthesizes them into one promotion
packet, registers the packet in the Pathos Library, and records the promotion
in the MIDAS workspace. Downstream Pathos agents consume registered packets;
they never read the MIDAS workspace.

`!promote` synthesizes existing artifacts. It never runs `!research`,
`!financials`, `!thesis`, `!risk`, or any other command, and never gathers
new sources. If the artifacts are missing or stale, it fails and names the
exact commands that fix it.

## Relationship to the Pathos Library

The shared space is governed by `library/LIBRARY.md` (reachable through the
`library` symlink in the profile root). That constitution wins over this file
for everything under the library root. Key obligations restated as deltas:

- MIDAS writes only inside `library/intake/midas/`.
- `library/registry/` is written only by `library/tools/register_packet.py`.
  Never edit registry contents directly.
- Registered packets are immutable. Corrections are a new dated version.
- Interim librarian rule: until the Cadmus profile exists, `!promote` runs the
  registration tool itself. When Cadmus goes live, `!promote` stops at
  `intake/` and this section is updated.

## Trigger and Inputs

- Trigger: `!promote [ticker]` or `/promote [ticker]`.
- Exactly one ticker argument. Normalize per `rules/ARTIFACTS.md` (uppercase,
  strip any leading `$`). Ambiguous or missing tickers follow the shared
  clarification behavior in `rules/COMMAND_INTERFACE.md`.
- Extra tokens (including mode words) are not supported and fail per the
  standard failure shape in `rules/COMMAND_INTERFACE.md`.

## Eligibility Gates

All gates must pass before anything is written anywhere. Check in order and
report every failed gate, not just the first.

1. **Library present.** The `library` symlink resolves and
   `library/LIBRARY.md` exists. If not, fail with the library-setup message
   in `OUTPUT.md`.
2. **Artifacts present.** All four exist:
   `workspace/tickers/[ticker]/research.md`, `financials.md`, `thesis.md`,
   `risk.md`.
3. **Headers valid.** Each artifact has the required header per
   `rules/ARTIFACTS.md`, including a parseable as-of date.
4. **Artifacts fresh.** Each as-of date is within the freshness window. The
   authoritative window is defined in `library/tools/register_packet.py`
   (currently 30 days); this gate pre-checks the same window to fail fast
   before any library write.
5. **Not already registered today.** If
   `library/registry/promotions/[ticker]/[today]/` exists, fail with the
   already-promoted message. A new promotion requires a later date or an
   updated artifact set on a later day.

## Workflow

1. Parse and normalize the ticker. Run the eligibility gates.
2. Read the four artifacts. Extract each as-of date and any recorded
   Evidence Confidence.
3. Derive the Setup Classification per `rules/CLASSIFICATIONS.md` and the
   Global Research Score and overall Evidence Confidence per
   `rules/SCORING.md`, grounded only in the four artifacts. Do not gather new
   sources. If the artifacts cannot support a score or classification, fail
   and say which artifact is insufficient rather than guessing.
4. Synthesize `packet.md` per the required sections in `OUTPUT.md`. This is a
   synthesis, not a concatenation: integrate, do not paste the four reports
   together. Research framing only; no trade language of any kind.
5. Build `packet.json` conforming to
   `library/schemas/promotion-packet.schema.json`.
6. Write both files to `library/intake/midas/[TICKER]/[YYYY-MM-DD]/`.
7. Run `python3 library/tools/register_packet.py --register
   intake/midas/[TICKER]/[YYYY-MM-DD]`.
8. If the tool fails: report its FAIL lines verbatim in the failure output,
   leave the intake files in place for inspection, and write nothing to the
   MIDAS workspace. Never retry silently and never bypass the tool.
9. On success: write `workspace/tickers/[ticker]/promotion.md` per
   `OUTPUT.md`, then display the standard success output.

## Guardrails (deltas on global rules)

- Never write outside `library/intake/midas/` and the ticker's own workspace
  folder.
- Never edit `library/registry/`, `library/trust/`, `library/portfolio/`,
  `library/log/` (the registration tool appends the event), or any other
  agent's intake or returns directories.
- The packet contains no buy/hold/sell language, price targets framed as
  advice, position sizes, or trade directives, per `rules/GLOBAL.md` and
  `library/LIBRARY.md`. The registration tool enforces this structurally;
  passing the tool does not license weaker drafting.
- No auto-run of any other command, before or after promotion.

## Failure Behavior

All failures use the standard shape from `rules/COMMAND_INTERFACE.md`
(`Unable to complete: [reason]`, a Reason line, and concrete next steps), with
the exact messages defined in `OUTPUT.md`. A failed `!promote` writes no
workspace artifact. A failure after intake but before registration leaves
intake files in place and says so.

## Re-promotion

Artifacts updated on a later day may be promoted again; registration creates a
new dated version and the library index points at latest. `!promote` never
modifies or deletes an earlier registered version.
