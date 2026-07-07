# Midas Command Output Contract — !research

Template source: `templates/COMMAND_OUTPUT_TEMPLATE.md`

---

## Command

Command: `!research`

Skill File: `skills/stock-analysis/research/SKILL.md`

Output File: `skills/stock-analysis/research/OUTPUT.md`

Registry Entry: `docs/COMMAND_REGISTRY.md`

Status: `Active`

---

## Registry Consistency

This output contract should match the command’s Registry Metadata block in `skills/stock-analysis/research/SKILL.md` and the command row in:

`docs/COMMAND_REGISTRY.md`

Check:

- Command name: `!research`
- Skill path: `skills/stock-analysis/research/SKILL.md`
- Output path: `skills/stock-analysis/research/OUTPUT.md`
- Status: `Active`
- Classification usage: `Optional`
- Scoring usage: `Optional`
- Metrics usage: `Optional`
- Artifact behavior: `Yes`

If this output file and the registry disagree, treat that as registry drift.

---

## Purpose

This file defines the command-specific output contract for `!research`.

It explains what the Standard-only business-model research note should return, how `-audit` output should appear, which sections are required or prohibited, and how artifacts, optional classifications, optional scores, optional metrics, sources, risks, and failures should appear.

This file should not redefine global output standards.

---

## Output / Workflow Boundary

This file defines output shape only.

Workflow, parser behavior, source gathering, and artifact writing procedures belong in `skills/stock-analysis/research/SKILL.md`.

This file should answer:

- What sections should appear?
- Which sections are required, optional, or prohibited?
- Which output modes are supported?
- How should audit, scores, classifications, metrics, sources, risks, failures, and artifacts be displayed?

This file should not answer:

- How sources are gathered
- How companies are screened
- How scores are calculated
- How metrics are computed
- How artifacts are written
- How the command routes or executes

---

## Global Output Inheritance

`!research` must follow the global Midas output rules in:

- `rules/GLOBAL.md`
- `rules/OUTPUT.md`

Depending on command behavior, it may also inherit from:

- `rules/SOURCES.md`
- `rules/CLASSIFICATIONS.md`
- `rules/SCORING.md`
- `rules/METRICS.md`
- `rules/ARTIFACTS.md`
- `rules/MARKET_DATA.md` only when explicit current-market context is included or market-data boundary discipline is being applied.

If this file conflicts with a global rule file, the global rule file wins unless the exception is explicitly documented here.

---

## Output Philosophy

`!research` output should be:

- Plain-English and filing-backed.
- Useful before it is exhaustive.
- Thesis-driven enough to explain why the business-model evidence matters, without becoming `!thesis`.
- Clear about what is disclosed, inferred, and not disclosed.
- Specific enough to support deeper diligence with `!financials`, `!thesis`, or `!risk`.

Avoid:

- Hype.
- False precision.
- Unsupported conviction.
- Long generic market commentary.
- Repeating global rule language.
- Dumping raw filing excerpts without interpretation.
- Turning business-model research into a full financial analysis or valuation model.
- Turning business-model research into a market-data, price-action, quote, or trading report.
- Letting market data support filing-backed business-model conclusions.

---

## Supported Output Modes

`!research` supports only two command states:

- Normal: supported. This is the default Standard-only filing-backed business-model report.
- Audit: supported only through `-audit`. This is no-write verification output.

Default:

`Normal Standard-only business-model report`

Unsupported:

- Compact mode.
- Full mode.
- Deep mode.

Mode-boundary enforcement:

- `!research [ticker]` always uses the Standard-only business-model report.
- `!research [ticker] -audit` uses the no-write audit output contract.
- Former compact-style words such as `compact`, `quick`, `brief`, `short`, `concise`, and `summary` are style hints or boundary prompts, not modes.
- Former full/deep-style words such as `full`, `deep`, `detailed`, `expanded`, `deep-dive`, and `deepdive` are not modes.
- Do not add hidden output-mode exceptions for channel limits, output limits, Telegram behavior, or artifact-only delivery.

Unsupported-mode display:

Compact-style request:

```md
`!research` now uses one Standard filing-backed business-model report. I can keep the report concise, but it still preserves source visibility and saves the canonical research artifact.
```

Full/deep packet request:

```md
`!research` is scoped to business-model research. Use `!thesis [ticker]` for thesis work, `!financials [ticker]` for financial statements, or `!risk [ticker]` for downside pressure-testing.
```

Do not auto-run these commands.

---

## Normal Standard-Only Output Contract

Every successful normal `!research [ticker]` response should include the Standard-only sections unless the command cannot complete.

Do not show empty sections. If a required business-model area is not disclosed or not applicable, say so in the relevant section or in `Source Notes`.

Do not leave placeholder text in active command outputs.

Normal output should include, in this order:

1. Report title
2. Introduction
3. Summary
4. Why It Matters
5. Business Model
6. Revenue Mechanics
7. Customers
8. Geography
9. Recurrence
10. Pricing Power
11. Business Risks
12. What To Verify Next
13. Source Notes
14. Best Next Command, when useful
15. Saved-path confirmation

### Normal Format

#### Report Title

`# 🔍 [Display Name] ($[TICKER]) | Business Analysis`

Example:

`# 🔍 Robinhood Markets ($HOOD) | Business Analysis`

If a saved artifact includes the metadata header required by `rules/ARTIFACTS.md`, preserve that artifact header first, then begin the visible report body with this required report title.

#### Introduction

`[2-4 sentence explanation of what the report analyzes, source base used, scope of !research, and that it is business-model research rather than full financial analysis, valuation, or buy/sell advice]`

#### Summary

`[1-3 sentence filing-backed business-model conclusion, including the main research implication and the most important caveat]`

#### Why It Matters

`[Why the business-model evidence is worth researching further, what is potentially distinctive, and what remains uncertain. Keep it evidence-backed and non-promotional.]`

#### Business Model

`[Products/services, platform/assets/operations, value-chain position, disclosed differentiators, and how the company creates value for customers]`

#### Revenue Mechanics

`[Revenue streams, monetization mechanics, revenue recognition when relevant, segments, revenue categories, contribution, growth/decline, and undisclosed items]`

#### Customers

`[Customer types, concentration, industries/verticals, channels, purchasing context, and end-market exposure if disclosed]`

#### Geography

`[Revenue by geography, operating regions, international exposure, region-specific risks or growth drivers, and undisclosed geography limits]`

#### Recurrence

`[Recurring/repeat/transactional/project/cyclical nature, contract length, renewals, backlog/RPO/deferred revenue/retention if disclosed. Do not call revenue recurring unless source-backed.]`

#### Pricing Power

`[Evidence for or against pricing power, pricing pressure, seasonality, discretionary/nondiscretionary demand, recession exposure, and cyclicality. Use measured conclusions only when supported.]`

#### Business Risks

`[Most important filing-backed business risks, model fragilities, concentration risks, source limitations, and assumptions that could undermine the business-model view. Keep this business-model focused; do not turn it into a full !risk memo.]`

#### What To Verify Next

`[Evidence or disclosures that would improve, weaken, confirm, or invalidate the current business-model view; include the best next diligence question. Keep this as follow-up verification, not a !thesis section.]`

#### Source Notes

`[Primary filings and official sources used, filing dates, report periods or report dates, source-basis descriptions, citation approach, source freshness, missing disclosures, and source limitations. Keep accession numbers available internally, but do not include accession numbers or raw SEC URLs in normal output by default.]`

This section is required. For SEC filers, include the latest 10-K and latest 10-Q when available, with filing date, report period or report date, and concise source-basis description. Keep accession numbers available internally, but do not include them in normal output by default. Accession numbers may appear when the user asks for detailed filing identifiers, audit/debug/source-recovery context makes them useful, or multiple same-form filings on similar dates would otherwise be ambiguous. Do not include raw SEC URLs in normal output by default. Include raw URLs only if the user explicitly asks for source links, a non-standard source cannot be clearly identified by filing type/date, or audit/debug/source-recovery context makes the URL useful. If a primary filing is unavailable, state the source limitation. Explicitly state `not disclosed in the reviewed filings` when a relevant business-model fact is missing.

Preferred normal Source Notes format:

```md
- [Filing type] — filed [date]; period ended [date]; used for [key sections/tables/source basis].
- [Filing type] — filed [date]; report date [date]; used for [key sections/tables/source basis].
```

#### Best Next Command

When useful, use:

`` `!command TICKER` — Reason. ``

Do not recommend a next command when it would be noisy or unnecessary.

#### Saved-Path Confirmation

The final line after a successful normal artifact write must be:

`Saved to: workspace/tickers/[ticker]/research.md`

The saved-path line must appear exactly once and must be the final line. Do not use `Saved artifact:` as the normal confirmation wording. Do not include a separate Artifact section by default.

---

## Audit Output Contract

Use this output only for:

`!research [ticker] -audit`

Audit output is no-write verification output. It must not claim that an artifact was saved.

### Audit Format

```md
# 🔍 $[TICKER] | Research Audit

## Audit Result

Pass / Partial / Blocked

## Source Basis
[Primary filings or source equivalents reviewed or expected]

## Business-Model Coverage

- Business model:
- Revenue mechanics:
- Customers:
- Geography:
- Recurrence:
- Pricing power:
- Risks:

## Missing Evidence

[Not disclosed / not verified / stale / unavailable]

## Source Limitations

[Freshness, filing gaps, non-SEC filer limits, line citation limits]

## Output Safety Check

- No recommendation language:
- No unsupported valuation:
- No market-data drift:
- No unsupported moat / recurrence / pricing-power claims:

## Artifact Status

No artifact written. Existing artifact inspected read-only: Yes / No.

## Best Next Step

[Patch/run/research recommendation]

No files changed — audit mode.
```

Audit output must not include:

- Raw source dump.
- Hidden reasoning.
- Scratch work.
- Tool logs.
- Internal prompts.
- Giant filing excerpts.
- Saved-path confirmation.
- Artifact write claims.

### Audit Blocked Fallback

If no-write cannot be guaranteed, use:

```md
Audit Result: Blocked

Could not guarantee no-write behavior for !research [ticker] -audit, so source gathering was not started.

Would have checked:
- source basis
- business-model coverage
- missing disclosures
- source limitations
- output safety
- artifact status

Required before audit can run:
- patch SKILL.md and OUTPUT.md to make -audit override all artifact, manifest, excerpt, index, watchlist, and downstream-command writes.

No files changed — audit blocked.
```

---

## Evidence / Source Notes

Use source notes because `!research` uses external evidence, filings, company documents, or user-provided documents. `!research` does not use live/current market data by default; if explicit current-market context is included, it must be labeled separately as Tier 2 market context and must not support filing-backed business-model conclusions.

Follow:

- `rules/SOURCES.md`
- `rules/OUTPUT.md`

Required source behavior:

- State which primary filings or official company sources were used.
- For SEC filers, include the latest 10-K and latest 10-Q when available.
- Include filing dates, report periods or report dates, and concise source-basis descriptions where available.
- If a 10-K, 10-Q, or primary-source equivalent is unavailable, state the limitation.
- Every material factual claim should remain citation-backed.
- If line citations are available, use them; otherwise cite filing name, filing date, report period/date, and section/table/source basis. Keep accession numbers available internally, but do not require or display them in normal output by default; include them only when the user asks for detailed filing identifiers, audit/debug/source-recovery context makes them useful, or multiple same-form filings on similar dates would otherwise be ambiguous. Do not include raw SEC URLs in normal output by default unless the user asks for source links, a non-standard source cannot be clearly identified by filing metadata, or audit/debug/source-recovery context makes the URL useful.
- If a relevant business-model fact is not disclosed in reviewed filings, explicitly say `not disclosed in the reviewed filings`.

Market-data display boundary:

- Do not add a normal market-data section to default normal `!research` output.
- Normal `!research` does not fetch live/current market data by default.
- If live/current market data is not used, no market-data disclaimer is required by default.
- If explicit current-market context is included, label it separately as Tier 2 market context.
- Include provider/source, as-of timestamp, timezone when available, limitations, and timing mismatch versus filing-derived inputs.
- State that market data is context only and does not prove or alter filing-backed business-model conclusions when needed.

---

## Classification Behavior

Use this section only if the command applies setup classification.

Follow:

- `rules/CLASSIFICATIONS.md`

Classification usage:

`Optional`

If used, output should include:

`Setup Classification: [classification]`

Optional:

`Setup Modifiers: [modifier 1], [modifier 2]`

Command-specific classification notes:

- Do not classify by default when the output is purely factual business-model research.
- Use classification only when the response includes a setup view or final research view.
- Keep classification clearly secondary to the filing-backed business-model evidence.

If classification is not used, omit the classification section unless the user asked why no classification was shown.

---

## Scoring Behavior

Use this section only if the command applies Midas scoring.

Follow:

- `rules/SCORING.md`

Scoring usage:

`Optional`

If used, output may include:

`Global Research Score: [score]/100`

Evidence confidence:

`Evidence Confidence: [A / B / C / D]`

Command-specific scoring notes:

- Do not score by default.
- Use scoring only if the user asks for a score or if the output explicitly includes setup evaluation.
- If full scoring is needed, apply it per `rules/SCORING.md` on explicit request.

If scoring is not used, omit the scoring section unless the user asked for score behavior.

---

## Metrics Behavior

Use this section only if the command displays, calculates, compares, or interprets financial metrics.

Follow:

- `rules/METRICS.md`
- `rules/ARTIFACTS.md`
- `rules/MARKET_DATA.md` only when explicit current-market context is included or market-data boundary discipline is being applied.

Metrics usage:

`Optional`

Required metrics:

`None by default`

Command-specific metric notes:

- Use lightweight business-performance metrics only when they support the business-model discussion.
- Examples include revenue trend, segment revenue, revenue category mix, backlog/RPO, customer concentration, geography, retention, or other disclosed operating metrics.
- Do not provide full margin, balance-sheet, cash-flow, valuation, or shareholder-return analysis; redirect to `!financials`.
- Label periods, source, and whether values are company-reported or calculated.
- Use tools for calculations.

---

## Best Next Command

When useful in normal output, end with the next most logical Midas command as its own section before the saved-path confirmation. Preserve command-first body format.

Allowed examples:

- `` `!financials [TICKER]` — Review financial statements, metric quality, margins, cash flow, balance sheet, and dilution. ``
- `` `!thesis [TICKER]` — Build the long-term thesis and what would need to go right. ``
- `` `!risk [TICKER]` — Pressure-test downside and thesis-breaking risks. ``
- `` `!market [TICKER]` — Use only for a current market snapshot. ``

Formatting:

- Use `## Best Next Command` as the section heading in normal output.
- Put the command body on the next non-empty line.
- Use command-first body format: `` `!command TICKER` — Reason. ``
- The command must be wrapped in backticks.
- The first letter of the reason after the dash must be capitalized.
- Do not repeat `Best next command:` or `Best Next Command:` inside the section body.
- Do not auto-run downstream commands.

---

## Artifact Behavior

Artifact output must follow:

`rules/ARTIFACTS.md`

Writes artifacts:

- Normal `!research [ticker]`: Yes.
- Audit `!research [ticker] -audit`: No.

Normal artifact behavior:

- Write the canonical Markdown research artifact automatically after the final answer is complete and verified.
- Artifact location: `workspace/tickers/[ticker]/research.md`
- User-facing relative path: `workspace/tickers/[ticker]/research.md`
- Artifact type: `Markdown research note`
- Saved artifacts must include the required report title and `Introduction` section.
- Saving the artifact does not permit an artifact-only or completion-summary-only chat response.
- When the normal artifact is written, output should include the saved-path confirmation as the final line:

`Saved to: workspace/tickers/[ticker]/research.md`

No-write audit artifact behavior:

- Audit writes nothing.
- Audit must not include saved-path confirmation.
- Audit must not claim an artifact was written.

Separate Artifact section:

- Do not include a separate Artifact section by default.
- Only include a separate Artifact section if there is extra artifact context beyond a normal save confirmation, such as multiple artifacts created, a versioned artifact preserved, the artifact path changed, a save failed, or the user explicitly asked for artifact details.

Legacy path handling follows `rules/ARTIFACTS.md`.

---

## Failure Output Contract

Use failure output when the command cannot complete its intended task.

Common failure cases:

- Missing ticker/company/input.
- Ambiguous company identity.
- Insufficient primary-source evidence.
- Conflicting evidence.
- Data too stale.
- Filing access failure after reasonable retry.
- Artifact write failure.
- No-write audit cannot be guaranteed.

Failure output should include:

1. What failed.
2. Why it failed.
3. What evidence or input is missing.
4. Best next step.

### Failure Format

`Unable to complete: [specific failure]`

`Reason: [clear explanation]`

`Missing or needed: [input/evidence/data]`

`Best next step: [command or user action]`

Do not fabricate results to avoid a failure state.

Do not claim a saved artifact if no artifact was written.

---

## Command-Specific Required Sections

The following sections are required for normal Standard-only `!research` output, in order:

- Report title
- Introduction
- Summary
- Why It Matters
- Business Model
- Revenue Mechanics
- Customers
- Geography
- Recurrence
- Pricing Power
- Business Risks
- What To Verify Next
- Source Notes
- Best Next Command, when useful
- Saved-path confirmation

The following sections are required for audit output:

- Audit Result
- Source Basis
- Business-Model Coverage
- Missing Evidence
- Source Limitations
- Output Safety Check
- Artifact Status
- Best Next Step
- No-files-changed audit confirmation

The following sections are optional:

- Setup Classification
- Setup Modifiers
- Evidence Confidence
- Artifact section, only when extra artifact context is needed
- Open Questions when included under `What To Verify Next`; keep them as follow-up verification items, not a thesis section
- Metrics when lightweight and business-model-relevant

The following sections are prohibited by default:

- Buy/Hold/Sell recommendation
- Price target
- Full valuation model
- Full financial statement analysis
- Hidden-gem ranking
- Tracker/copy-trading framing
- False saved claims
- Watchlist mutation claims
- Downstream command auto-run claims

Normal source-visibility requirements:

- Include `Source Notes`.
- Include filing dates / report periods or report dates / source-basis descriptions where available; accession numbers and raw SEC URLs are not required in normal output by default.
- Cite or source-reference material factual claims.
- Explicitly state `not disclosed in the reviewed filings` when a required business-model fact is missing.
- Do not allow normal output to collapse into a citation-free summary.
- Do not include citation-free material factual claims.

---

## Command-Specific Table Standards

Use tables only when they improve scanability.

Required tables:

`None`

Optional tables:

- Source list.
- Segment or revenue category breakdown.
- Geographic revenue breakdown.
- Customer concentration or end-market table.
- Business-performance snapshot.

Table rules:

- Keep tables compact.
- Do not include decorative columns.
- Do not show unavailable metrics as if known.
- Use `Not disclosed` when the reviewed filings do not disclose a relevant fact.
- Include period/date context when metrics are shown.

---

## Command-Specific Language Standards

Preferred language:

- Filing-backed.
- Plain English.
- Fact vs interpretation clearly separated.
- Use `not disclosed in the reviewed filings` when appropriate.
- Use measured conclusions such as `strong`, `moderate`, `weak`, `mixed`, or `not enough information` for pricing power only when supported.
- `Market-data context, if included: [provider/source], as of [timestamp] [timezone], with limitations.`
- `Market data is Tier 2 context only and does not prove the filing-backed business-model view.`
- `For a current market snapshot, use !market [ticker].`

Avoid:

- `Buy`, `Hold`, `Sell`, `Strong Buy`, or equivalent recommendation language.
- `I'd classify it as` or equivalent classification phrasing unless the output explicitly includes `Setup Classification: [approved classification]` using an approved classification from `rules/CLASSIFICATIONS.md`.
- `Guaranteed`, `no-brainer`, `must-own`, or promotional phrasing.
- `Moat`, `pricing power`, `recurring`, `mission-critical`, or `recession-proof` unless supported by the reviewed sources.
- Full valuation or price-target language.
- `Price action proves the business model.`
- `Market cap proves business quality.`
- `The stock is up/down, so the thesis is confirmed.`
- Unsupported `cheap`, `expensive`, or `fair value` conclusions.
- Any market-data claim without provider/source, as-of timestamp, limitations, and boundary labeling when market data is included.

When refusing buy/sell/price-target requests, `!research` may provide research framing. Use `Business-model characterization: ...` for non-classification framing. Use `I'd classify it as` only when the output explicitly includes `Setup Classification: [approved classification]`.

Required disclaimers or caveats:

- If primary filings are missing or stale, label the source limitation.
- If a relevant fact is not disclosed, state that it is not disclosed rather than guessing.

---

## Examples Needed

Each command-specific output contract should eventually include or reference examples for:

- Normal success case.
- Audit case.
- Weak or incomplete evidence case.
- Failure case.
- Artifact-writing case.

Example coverage lives in the command eval file.

Eval file:

`evals/research.eval.md`

The eval file should test that this output contract is followed.

---

## Placeholder Cleanup Rule

This Active output file should not contain unresolved template placeholders.

No unresolved template placeholders are intended for runtime output.

---

## Stability Checklist

For Active output-contract stability, confirm:

- [x] It references global output rules instead of duplicating them
- [x] It defines normal Standard-only and audit output behavior
- [x] It clearly states whether classification is used
- [x] It clearly states whether scoring is used
- [x] It clearly states whether metrics are used
- [x] It clearly states whether artifacts are written
- [x] It defines failure behavior
- [x] It avoids command workflow instructions that belong in `SKILL.md`
- [x] It avoids source hierarchy rules that belong in `rules/SOURCES.md`
- [x] It avoids scoring rubric details that belong in `rules/SCORING.md`
- [x] It avoids metric formulas that belong in `rules/METRICS.md`
- [x] Skill and output paths are command-specific, not generic `skills/[command]/...` placeholders
- [x] Registry metadata matches `docs/COMMAND_REGISTRY.md`
- [x] Unsupported output mode behavior is defined
- [x] Empty sections are omitted unless explicitly required
- [x] Artifact paths use command-specific workspace paths, not generic placeholders
- [x] All template placeholders have been replaced or removed before marking Active
- [x] This file defines output shape only and does not duplicate command workflow logic
- [x] It is concise enough to serve as an interface contract
