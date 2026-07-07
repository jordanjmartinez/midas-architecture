# `!earnings` Output Contract

## Purpose

`!earnings` is the concise latest-quarter earnings review command.

It answers:

- What happened this quarter?
- What improved?
- What got worse?
- What did management say?
- Did guidance change?
- Did the quarter strengthen, weaken, or leave the thesis unchanged?
- Did the quarter increase or reduce risk?
- What should be watched next quarter?

It is quarter-specific. It is not a broad material-update monitor.

## Command Identity

Use `!earnings [ticker or company]` for a focused review of the most recent reported quarter using earnings-specific sources:

- earnings release
- latest 10-Q if available
- earnings-related 8-K
- earnings call transcript if available
- shareholder letter or investor presentation if material
- guidance / outlook disclosures

Keep the output concise, source-backed, and useful for deciding the next diligence step.

## Boundary With `!updates`

`!updates` is the broad recent-material-change triage command. `!earnings` is the deeper latest-quarter review command.

If the user wants broad recent company changes, route:

```md
## Best Next Command

`!updates TICKER` — broad recent company-update triage.
```

If an earnings review surfaces a non-earnings material event that needs separate tracking, mention it briefly and route to `!updates TICKER`. Do not perform a full `!updates` workflow inside `!earnings`.

## Non-Goals / Boundaries

`!earnings` must not become:

- a broad material-update scan
- a full business-model research report
- a full financial statement analysis
- a full thesis memo
- a full risk memo
- a full Midas packet
- a price-action recap
- a social hype recap
- a Buy/Sell/Hold recommendation
- a price-target, sizing, or trade-advice output

Do not auto-run `!updates`, `!research`, `!financials`, `!thesis`, `!risk`, or any other command.

Do not modify watchlist state.

## Preferred Chat Output Shape

Use this standard visible format unless the user asks for a different mode:

```md
# 📅 [Display Name] ($[TICKER]) | Earnings Review

[Short lead paragraph: what happened this quarter and whether it matters.]

## Sources Used

[Compact source summary: earnings release, 10-Q if available, transcript if available, and any material supporting document.]

## Key Numbers

- Revenue: $X, up/down X% YoY.
- Gross margin: X%.
- Operating income/loss: $X.
- Net income/loss: $X.
- Adjusted EBITDA: $X, if relevant and labeled non-GAAP.
- Operating cash flow: $X.
- Free cash flow: $X, defined as CFO minus capex unless company-defined and clearly labeled.
- Cash / debt: $X / $X.
- Guidance: [short summary or “Not provided.”]

## What Improved

[Short bullets or short prose.]

## What Got Worse

[Short bullets or short prose.]

## Guidance / Outlook

[What changed, what management guided, and what remains uncertain.]

## Management Commentary

[Separate reported facts from management claims / forward-looking assumptions.]

## Thesis Impact

Final Earnings View: [Thesis Strengthened / Thesis Unchanged / Thesis Under Review / Thesis Weakened / Thesis Broken]

[Short explanation.]

## Risk Update

[Whether risk increased, reduced, or stayed unchanged, and why.]

## Key Metrics To Watch Next Quarter

[Short numbered checklist.]

## Source / Evidence Limitations

[Missing 10-Q, missing transcript, unaudited figures, unavailable consensus, stale data, or source caveats.]

## Best Next Command

`![command] TICKER` — [reason]

Saved to: workspace/tickers/[ticker]/earnings.md
```

Rules:

- Use narrative synthesis first.
- Keep sections concise.
- Use selective evidence; do not dump source metadata in chat.
- Do not use giant tables by default.
- Do not include full transcript dumps.
- Do not perform a full financial-statement walkthrough.
- Do not use repeated `Category / Evidence / Why it matters` field stacks.
- Use one useful Best Next Command when possible.
- Use backticks around the next command.
- Do not use recommendation language.

## Key Numbers Behavior

`## Key Numbers` should be compact and period-labeled.

Preferred style:

```md
## Key Numbers

- Revenue: $X, up/down X% YoY.
- Gross margin: X%.
- Operating income/loss: $X.
- Net income/loss: $X.
- Adjusted EBITDA: $X, if relevant and labeled non-GAAP.
- Operating cash flow: $X.
- Free cash flow: $X, defined as CFO minus capex unless company-defined and clearly labeled.
- Cash / debt: $X / $X.
- Guidance: [short summary or “Not provided.”]
```

Rules:

- Label GAAP vs non-GAAP.
- Define FCF.
- Use period labels.
- Show calculations when calculating growth rates, margins, or cash-flow metrics.
- If a metric is unavailable, not disclosed, or not meaningful, say so briefly.
- Do not create a full `!financials` review.

## Beat / Miss / Meet Behavior

Do not force a Beat / Miss / Meet section.

Use beat/miss/meet only if reliable consensus estimates are available.

If reliable consensus is unavailable, say briefly in `## Source / Evidence Limitations` or the lead:

```md
Reliable consensus estimates were not available, so beat/miss/meet is not included.
```

Rules:

- Do not invent consensus.
- Do not treat analyst expectations as company-reported facts.
- Label consensus as external expectations, not company facts.

## Guidance / Outlook Behavior

Guidance should be concise.

Include when available:

- whether guidance was raised, lowered, initiated, maintained, or not provided
- period covered
- metric guided
- important assumption if disclosed
- source limitation if guidance is unclear

Do not turn guidance into a forecast model.

## Management Commentary Behavior

Separate:

- reported facts
- management claims
- forward-looking assumptions

Keep this concise.

Do not treat management optimism as fact.

## Thesis Impact Behavior

Use only these final view labels:

- Thesis Strengthened
- Thesis Unchanged
- Thesis Under Review
- Thesis Weakened
- Thesis Broken

Display as:

```md
Final Earnings View: Thesis [label]
```

This is a research classification, not a trade recommendation.

Do not turn `!earnings` into a full `!thesis` update by default.

## Risk Update Behavior

Risk update should be concise and quarter-specific.

It may mention:

- business risk
- financial risk
- growth risk
- execution risk
- competitive risk
- regulatory/legal risk
- macro risk
- valuation/rerating risk

Do not turn it into a full `!risk` memo.

## Missing Source Behavior

If the 10-Q is not yet available, say:

```md
Source limitation: The 10-Q was not available, so this review relies on the earnings release, call transcript, and company materials available.
```

If the transcript is not available, say:

```md
Source limitation: Earnings call transcript was not available, so management-commentary analysis is limited.
```

Do not pretend unavailable documents were reviewed.

## Failure / Incomplete Earnings Output

Use this shape when the earnings review cannot be completed:

```md
Unable to complete: [specific issue]

Reason: [why the earnings review cannot be completed]

Missing or needed: [earnings release / 10-Q / transcript / valid ticker / reliable source]

Best next step: [retry after filing, provide company/ticker, broaden source window]
```

Rules:

- Do not fabricate missing earnings results.
- Do not claim an artifact was saved if the review did not complete.
- Do not write a partial `earnings.md` unless the user explicitly asks to preserve an incomplete note.

## Artifact Behavior

Canonical path:

```md
workspace/tickers/[ticker]/earnings.md
```

Standard successful earnings reviews replace the latest `earnings.md` artifact for the ticker unless the user explicitly asks to preserve versions.

Do not write to `updates.md`.

Do not append earnings results to `updates.md`.

Do not modify watchlist files.

Use this confirmation only after the file is actually written:

```md
Saved to: workspace/tickers/[ticker]/earnings.md
```

## Source / Evidence Discipline

`!earnings` should distinguish:

- reported quarterly results
- company guidance
- management commentary
- analyst expectations
- market data
- news context
- estimates / consensus
- unaudited figures
- stale or missing data

Rules:

- Earnings releases, 10-Qs, and company filings anchor reported results.
- Transcript/commentary supports management color, not reported facts.
- Consensus estimates are external expectations, not company facts.
- Price moves are context, not thesis proof.
- Social/crowding is not thesis proof.
- Time-sensitive claims need as-of dates.
- Market data follows the global Market-Data Display Rule.
- If evidence is weak, stale, conflicting, or missing, say so.

## Scoring / Classification Behavior

- `!earnings` does not use Global Research Score by default.
- Do not include overlay scoring by default.
- Setup Classification is optional and should appear only if the quarter materially changes setup view.
- Evidence Confidence may be used when source quality materially affects the conclusion.
- Final Earnings View is not a Buy/Sell/Hold rating.
- `!earnings` should not become a full scoring command.

## Required Guardrails

`!earnings` must not:

- use Buy/Sell/Hold language
- provide price targets
- suggest position sizing
- give trade advice
- treat price movement as thesis proof
- treat social chatter as thesis proof
- treat management optimism as fact
- invent missing consensus estimates
- invent unavailable transcript commentary
- produce a full research, financials, thesis, risk, or full report
- auto-run another command
- modify watchlist state

## Final Output Verification

Before finalizing an `!earnings` response, verify:

- output is concise and latest-quarter focused
- reported results are separated from management commentary and analyst expectations
- Key Numbers are compact, period-labeled, and GAAP/non-GAAP labeled where relevant
- FCF is defined when used
- guidance/outlook is concise and not a forecast model
- missing 10-Q or transcript is clearly disclosed
- consensus is used only if reliable; otherwise beat/miss/meet is omitted or labeled unavailable
- Final Earnings View uses only the approved labels
- risk update is quarter-specific and not a full risk memo
- broad recent-update questions route to `!updates TICKER`
- no recommendation language, price targets, sizing, or trade advice
- no watchlist mutation
- saved line is truthful
