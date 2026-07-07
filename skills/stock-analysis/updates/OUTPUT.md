# `!updates` Output Contract

## Purpose

`!updates` is the broad, lightweight material-update triage command.

It answers:

- What changed recently?
- Is it material or just noise?
- Does it affect thesis direction?
- Does it affect risk direction?
- What should the user run next in Midas?

It is not a full report command.

## Command Identity

Use `!updates [ticker or company]` for concise company-update monitoring across material recent disclosures and events, including:

- new 8-Ks or other material filings
- company press releases and investor-relations updates
- guidance updates
- financing, debt, or equity issuance
- M&A or restructuring
- leadership changes
- legal or regulatory developments
- major customer, contract, product, or operational announcements
- meaningful price-move context when tied to a plausible company-specific or market event
- earnings headline only when earnings is the latest material update

Keep the output short, practical, and source-aware.

## Non-Goals / Boundaries

`!updates` must not become:

- a full earnings review
- a full business-model research report
- a full financial statement analysis
- a full thesis update
- a full risk memo
- a full combined report
- a broad news dump
- a price-action-only recap
- a social hype recap
- a Buy/Sell/Hold recommendation
- a price-target, sizing, or trade-advice output

Do not auto-run `!earnings`, `!research`, `!financials`, `!thesis`, `!risk`, or any other command.

Do not modify watchlist state.

## Earnings Routing

`!earnings` remains the deeper latest-quarter review command. Do not perform the full earnings workflow inside `!updates` by default.

If earnings are the latest material update, `!updates` may summarize the headline briefly, then route:

```md
Earnings appear to be the main recent update. This is a brief update summary, not a full quarter review.

## Best Next Command

`!earnings TICKER` — full quarter review.
```

If the user asks `!updates TICKER earnings`, do not run a full earnings review by default. Route or suggest:

```md
## Best Next Command

`!earnings TICKER` — full quarter review.
```

Do not auto-run `!earnings`.

## Chat Output Shape

Preferred visible format:

```md
# 🔄 [Display Name] ($[TICKER]) | Updates

[Short lead paragraph: what changed recently and whether it matters.]

## What Changed

1. [Material update] — [date/source period if known]
   - [One-sentence summary and why it matters.]

2. [Material update] — [date/source period if known]
   - [One-sentence summary and why it matters.]

## Why It Matters

[Plain-English thesis/risk read-through.]

## Thesis / Risk Impact

Thesis direction: [Strengthened / Unchanged / Under Review / Weakened / Not enough evidence]

Risk direction: [Reduced / Unchanged / Increased / Not enough evidence]

## Source / Evidence Note

[Compact source summary, as-of/review period, and limitations.]

## Best Next Command

`![command] TICKER` — [reason]

Saved to: workspace/tickers/[ticker]/updates.md
```

Rules:

- Use narrative synthesis first.
- Include only 1–5 material updates.
- Do not include a long news list.
- Do not over-structure each item with repeated `Category / Evidence / Why it matters` labels.
- Do not show source dumps in chat.
- Do not use wide tables by default.
- Do not force scoring or Setup Classification by default.
- Use one clear Best Next Command when useful.
- Use backticks around the next command.
- Do not use recommendation language.

## No Meaningful Update Output

Use this shape when no material company-specific update is found:

```md
# 🔄 [Display Name] ($[TICKER]) | Updates

No meaningful company-specific update was found in the reviewed period.

Checked: [compact source scope]

Best next step: [wait for next filing / broaden date range / run a specific command]
```

Rules:

- Do not force fake updates.
- Do not invent catalysts.
- Do not use random ticker suggestions.
- Explain the reviewed period or checked source scope when available.
- Do not claim an artifact was saved unless it actually was.
- No-update outputs should not write to `updates.md` by default unless the user explicitly asks to log the no-update check or the command has completed a full source check worth preserving.

## Artifact Behavior

Canonical path:

```md
workspace/tickers/[ticker]/updates.md
```

Standard successful material-update outputs replace the latest `updates.md` artifact for the ticker unless the user explicitly asks to preserve versions.

No-update outputs should not save or replace `updates.md` by default. Do not show a saved-path confirmation unless the user explicitly asks to log the no-update check or a write actually happens under the command contract.

Use this confirmation only after the file is actually written:

```md
Saved to: workspace/tickers/[ticker]/updates.md
```

Do not write to `earnings.md`. If earnings are the main update, briefly summarize the headline and route to `!earnings TICKER` for the full quarter review.

Do not use append wording or append-style behavior while replace-latest is the current command contract.

## Source / Evidence Discipline

`!updates` should distinguish:

- material company updates
- market noise
- price movement
- filings
- company press releases
- news articles
- management commentary
- social/crowding signals
- market data
- stale information

Rules:

- Primary/company sources anchor material claims.
- News may provide context, but should not override filings or company sources.
- Price moves are context, not thesis proof.
- Social/crowding is not thesis proof.
- Management commentary should be separated from reported facts.
- Time-sensitive claims need as-of dates or source periods.
- Market data follows the global Market-Data Display Rule.
- If source evidence is weak, stale, incomplete, indirect, or missing, say so.

## Scoring / Classification Behavior

- `!updates` does not score by default.
- Do not include Global Research Score by default.
- Do not include overlay scoring by default.
- Setup Classification is optional and should appear only if the update materially changes setup view.
- Evidence Confidence may be used when source quality materially affects the conclusion.
- Thesis direction and risk direction are the normal update-level classifications.

## Required Guardrails

`!updates` must not:

- use Buy/Sell/Hold language
- provide price targets
- suggest position sizing
- give trade advice
- treat price movement as thesis proof
- treat social chatter as thesis proof
- treat news headlines as primary evidence when filings or company sources conflict
- produce a full earnings review
- produce a full research, financials, thesis, risk, or full report
- auto-run `!earnings` or any other command
- modify watchlist state

## Final Output Verification

Before finalizing a `!updates` response, verify:

- output is concise and materiality-focused
- 1–5 material updates maximum
- thesis direction and risk direction are included when evidence allows
- source/evidence note is compact and not a source dump
- earnings, if present, is routed rather than expanded into a full quarter review
- no recommendation language, price targets, sizing, or trade advice
- no watchlist mutation
- saved line is truthful
