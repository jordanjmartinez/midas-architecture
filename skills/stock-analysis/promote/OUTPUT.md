# Midas Command Output Contract: !promote

This file owns the visible output shapes and the promotion artifact shapes for
`!promote`. Shared display standards inherit from `rules/OUTPUT.md`. Packet
data-shape law is `library/schemas/promotion-packet.schema.json`; this file
does not redefine it.

## Standard Success Output

```md
📤 [Display Name] ($[TICKER]) | Promotion Registered

Registered: library/registry/promotions/[ticker]/[YYYY-MM-DD]/
Score: [n]/100 | Classification: [primary] | Evidence: [A-D]
Artifacts: research [as-of] | financials [as-of] | thesis [as-of] | risk [as-of]

Saved to: workspace/tickers/[ticker]/promotion.md
```

No additional commentary, no recommendations, no next-command suggestion
unless the shared Best Next Command standard in `rules/OUTPUT.md` applies.

## Failure Outputs

All failures use the `rules/COMMAND_INTERFACE.md` failure shape. Required
messages:

**Missing artifacts:**

```md
Unable to complete: [TICKER] is not eligible for promotion.

Reason: missing [list, e.g. risk.md, thesis.md].

Run the missing commands first:
- `!risk [TICKER]`
- `!thesis [TICKER]`
```

**Stale artifacts:** same shape; Reason names each stale artifact with its
as-of date and age against the freshness window, and next steps name the
refresh commands.

**Library not set up:**

```md
Unable to complete: the Pathos Library is not reachable.

Reason: the `library` symlink is missing or `library/LIBRARY.md` was not
found.

Restore the symlink to ~/pathos/library and retry.
```

**Already promoted today:** Reason states the existing registry path and that
registered packets are immutable; next step is promoting on a later date
after artifact updates.

**Registration tool failure:** Reason includes the tool's FAIL lines
verbatim, states that intake files were left at
`library/intake/midas/[TICKER]/[date]/` for inspection, and that no workspace
artifact was written.

## packet.md Required Sections

Header block first:

```md
# 📤 [Display Name] ($[TICKER]) | Promotion Packet

Producer: midas | Produced: [ISO date-time]
Legal entity: [Company Name]
Score: [n]/100 | Classification: [primary; modifiers] | Evidence: [A-D]
Artifact as-of: research [date] | financials [date] | thesis [date] | risk [date]
Framing: research only. This packet contains no trade instructions.
```

Then, in order (inherited from the promote seed template in
`docs/plans/2026-07-05-promote-command-seed.md`):

1. Executive Summary
2. Business Summary
3. Financial Summary
4. Long-Term Thesis
5. Thesis Pillars
6. Growth Drivers and Catalysts
7. Risk Assessment
8. Bear Case
9. What to Monitor
10. Final Research View
11. Sources

The packet must be self-contained: downstream agents never read the Midas
workspace, so nothing in the packet may depend on it. Final Research View
stays within research framing per `rules/GLOBAL.md`: setup quality and
evidence assessment, never a trade call.

## packet.json

Conforms to `library/schemas/promotion-packet.schema.json`. The `ticker`
field is the only value downstream agents may ever treat as an executable
parameter, per `library/LIBRARY.md`.

## promotion.md (Midas workspace record)

```md
# [TICKER] Promotion Record

Promoted: [YYYY-MM-DD]
Registry: library/registry/promotions/[ticker]/[YYYY-MM-DD]/
Score: [n]/100 | Classification: [primary] | Evidence: [A-D]
Artifact as-of at promotion: research [date] | financials [date] | thesis [date] | risk [date]
```

Append one block per promotion; never rewrite earlier blocks. Standard
artifact header rules from `rules/ARTIFACTS.md` apply.

## Prohibited in all !promote output

- Buy/hold/sell language, price targets framed as advice, position sizing, or
  any trade directive.
- Auto-running any other command.
- Editing anything under `library/registry/`, or writing outside
  `library/intake/midas/` and the ticker's workspace folder.
- Pasting the four artifacts together instead of synthesizing.
