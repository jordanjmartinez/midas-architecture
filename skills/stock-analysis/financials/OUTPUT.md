# !financials Output Contract

## Command

Command: `!financials`

Skill File: `skills/stock-analysis/financials/SKILL.md`

Output File: `skills/stock-analysis/financials/OUTPUT.md`

Registry Entry: `docs/COMMAND_REGISTRY.md`

Status: `Active`

---

## Registry Consistency

This output contract should match the command’s Registry Metadata block in the command `SKILL.md` and the command row in:

`docs/COMMAND_REGISTRY.md`

Expected registry values:

- Command: `!financials`
- Aliases: `None`
- Category: `Financial Analysis`
- Status: `Active`
- Skill path: `skills/stock-analysis/financials/SKILL.md`
- Output path: `skills/stock-analysis/financials/OUTPUT.md`
- Eval file: `evals/financials.eval.md`
- Classification: `Optional`
- Scoring: `Optional`
- Metrics: `Required`
- Artifacts: `Yes`

If this output file and the registry disagree, treat that as registry drift.

---

## Purpose

This file defines the command-specific output contract for `!financials`.

`!financials` output should present a filing-backed financial statement and metric-quality review. It should focus on revenue, margins, profitability, operating cash flow, free cash flow, balance sheet, liquidity, debt, dilution, capital returns, segment financials, GAAP/non-GAAP quality, source limitations, financial red flags, and best next diligence command.

This file does not redefine global output standards.

---

## Output / Workflow Boundary

This file defines output shape only.

Workflow steps belong in:

`skills/stock-analysis/financials/SKILL.md`

Metric definitions belong in:

`rules/METRICS.md`

Source hierarchy belongs in:

`rules/SOURCES.md`

Artifact policy belongs in:

`rules/ARTIFACTS.md`

---

## Global Output Inheritance

`!financials` must follow the global MIDAS output rules in:

- `/home/jordan/.hermes/profiles/midas/rules/GLOBAL.md`
- `/home/jordan/.hermes/profiles/midas/rules/OUTPUT.md`
- `/home/jordan/.hermes/profiles/midas/rules/SOURCES.md`
- `/home/jordan/.hermes/profiles/midas/rules/MARKET_DATA.md` only for optional market / valuation context
- `/home/jordan/.hermes/profiles/midas/rules/METRICS.md`
- `/home/jordan/.hermes/profiles/midas/rules/ARTIFACTS.md`

When classification or scoring is used, also follow:

- `/home/jordan/.hermes/profiles/midas/rules/CLASSIFICATIONS.md`
- `/home/jordan/.hermes/profiles/midas/rules/SCORING.md`

If this file conflicts with a global rule file, the global rule file wins unless the exception is explicitly documented here.

---

## Output Philosophy

`!financials` output should be:

- Filing-backed
- Metric-aware
- Concise by default
- Clear about GAAP vs non-GAAP
- Clear about unavailable, stale, or non-meaningful metrics
- Focused on financial-statement quality, not thesis promotion
- Specific about the best next diligence step

Avoid:

- Hype
- False precision
- Recommendation language
- Default cheap/expensive/reasonable/fair-value valuation framing
- Default PEG metrics
- Full valuation models by default
- Full business-model, thesis, risk, or hidden-gem outputs
- Long filing dumps

---

## Supported Output Modes

Supported modes:

- Normal: supported.
- Audit: supported only through `-audit`.

Default mode:

- Normal Standard-only financial-statement and metric-quality report.

Unsupported modes:

- Compact mode.
- Full mode.
- Deep mode.

Former Compact-style words such as `compact`, `quick`, `brief`, `short`, `summary`, and `concise` are style hints or boundary prompts, not modes. They must not route to a compact output shape.

Former Full/Deep-style words such as `full`, `deep`, `detailed`, `expanded`, `deep-dive`, and `deepdive` are not `!financials` modes. Route to better commands when appropriate:

- `!full [ticker]` for a complete MIDAS packet.
- `!thesis [ticker]` for thesis work.
- `!risk [ticker]` for downside pressure-testing.
- `!research [ticker]` for business-model research.
- `!earnings [ticker]` for latest-quarter earnings review.

`-audit` is no-write and uses the audit output contract below.

## Unsupported Mode Display

Compact-style request boundary:

```md
!financials now uses one Standard filing-backed financial-statement and metric-quality report. I can keep the sections concise, but the command still preserves metric labels, source visibility, and saves the canonical financials artifact.
```

Full/deep complete-packet request boundary:

```md
!financials is scoped to financial statements and metric quality. Use !full [ticker] for a complete packet, !thesis [ticker] for thesis work, !risk [ticker] for downside pressure-testing, !research [ticker] for business-model research, or !earnings [ticker] for latest-quarter earnings review.
```

Do not auto-run downstream commands.

---

## Required Top-Level Output Contract

Every successful normal `!financials` response should include a clear financial-quality conclusion, source basis, financial statement review, metric-quality caveats, material financial risks/watchpoints, source limitations when relevant, and a best next diligence command when useful. Source detail, financial risks, and source limitations must be separated into the required top-level sections rather than buried inside the introduction. The Standard title must say `Financial Analysis`, not `Financials Analysis`.

Required normal shape rules:

- `## Introduction` must stay short and must not contain a long source dump.
- `## Summary` must give the financial-quality read-through before section detail.
- `## Source Notes` must appear after `## What To Verify Next` and before `## Best Next Command` when useful.
- `## Financial Risks` must appear after `## Financial Quality Score` and before `## What To Verify Next`.
- `## Source Notes` must preserve source basis, source freshness, missing disclosures, calculated-metric labels, and source limitations without becoming the main risk section.

Do not show empty optional sections. If a required section is not applicable, include a clear `Not disclosed`, `Not meaningful`, or `Not calculable` statement.

---

## Required Title Format

Use:

```md
# 🪙 [TICKER] | [Company Name] Financial Analysis
```

Example:

```md
# 🪙 HOOD | Robinhood Markets, Inc. Financial Analysis
```

---

## Required Introduction Section

Use:

```md
## Introduction
```

The introduction should be short, usually 2–4 sentences. It should explain:

- What the report is reviewing
- Which source base is being used
- The scope of `!financials`
- That this is a financial-statement and metric-quality review, not a business-model report, full valuation, price target, or buy/sell recommendation

Example:

```md
This report reviews [Company Name]’s filing-backed financial statements and metric quality using the latest reviewed annual and interim filings. It focuses on revenue trends, margins, profitability, cash flow, balance sheet strength, dilution, capital returns, GAAP/non-GAAP quality, and financial red flags. It is financials analysis, not a business-model report, full valuation, price target, or buy/sell recommendation.
```

---

## Source Notes

Use `## Source Notes` when external evidence, filings, market data, company documents, or user-provided documents support the review.

Normal Source Notes should be concise.

Preferred normal Source Notes format:

- `[Filing type] — filed [date]; period ended [date]; used for [source basis].`
- `[Earnings release / company release] — dated [date]; used for [source basis].`
- `[Investor presentation] — dated [date]; used for [source basis], if used.`

Required source behavior:

- State the source base and as-of periods.
- Include the latest annual and interim sources reviewed when available.
- Preserve filing/source type, filing/source date, period or report date, source basis, and source freshness.
- Preserve missing disclosures, source limitations, and calculated metric labeling when relevant.
- For foreign private issuers, list primary-source equivalents such as Form 20-F, Form 6-K, annual reports, interim reports, and filed exhibits.
- Use line citations when available.
- If line citations are unavailable, cite filing name, filing date, period, and section/table/source basis when available.
- Do not require raw SEC URLs by default.
- Do not require accession numbers by default unless needed for disambiguation.
- Accession numbers and URLs may remain internal and may appear in audit, source-recovery, or debug contexts when useful.
- Do not present secondary-source metrics as filing-backed facts.

---

## Classification Behavior

Classification usage: `Optional`

This command does not classify setups by default.

If the user explicitly asks for classification or the output includes a final setup view, output may include:

```md
Setup Classification: [classification]
Setup Modifiers: [modifier 1], [modifier 2]
```

Do not force classification into a raw financial statement review.

---

## Scoring Behavior

Scoring usage: `Optional`

Normal output includes the required `## Financial Quality Score` section as a concise financial-quality research prioritization score/grade when evidence supports it. This is not a full Global Research Score and must not be framed as a recommendation.

If broader scoring is requested, scoring must follow `rules/SCORING.md`. If the user asks for a full Global Research Score, prefer suggesting `!full` unless the requested scope is clearly limited to financial quality.

Do not use a score as a recommendation.

Score-line formatting in normal output is output-only: `[score]/10 - [Assessment]`. Keep the score and assessment generated from the financial evidence; do not hardcode scores, add a scoring rubric, or alter scoring logic.

---

## Metrics Behavior

Metrics usage: `Required`

Required metric areas:

- Revenue trends and growth, when calculable
- Gross margin, operating margin, and net margin where meaningful
- Profitability trend
- Operating cash flow
- Free cash flow and FCF definition
- Cash, debt, liquidity, and solvency context
- Share count and dilution
- Buybacks, dividends, and capital returns when disclosed
- Segment financials when disclosed
- GAAP vs non-GAAP distinction and reconciliation quality

Optional metric areas:

- ROE and ROA, with denominator basis labeled
- Interest coverage, with basis labeled
- FCF conversion, with caveat if net income is negative
- Capital-return yield, clearly labeled as such and not called TSR
- Limited market / valuation context only when explicitly requested or when market cap / EV / liquidity is materially needed to frame financial scale

Metric constraints:

- Follow `rules/METRICS.md`.
- Preserve metric name, period, currency, unit, filing/source period, and GAAP/non-GAAP status when relevant.
- Label reported vs adjusted status and actual vs estimated/guided status when applicable.
- If market data is used, label source/provider and as-of date.
- If a metric is not meaningful, stale, unavailable, not disclosed, or not calculable, say so.
- Do not use undefined metrics.
- Define FCF as CFO minus capex when using that convention; if using company-defined FCF, label it clearly.
- Separate GAAP and non-GAAP metrics.
- Check non-GAAP reconciliation quality when available.
- Do not treat non-GAAP as equivalent to GAAP.
- Flag recurring, aggressive, changing, or poorly reconciled adjustments.
- If reconciliation is unavailable, say so.
- Do not calculate FCF CAGR when FCF crosses zero, is negative, or is not meaningful; explain the trend instead.
- Do not include PEG as a default metric.
- Do not use default cheap/expensive/reasonable/fair-value valuation language.
- Do not present unsupported multiple conclusions.

---

## Optional Market / Valuation Context

Do not include a live market-data block by default in normal `!financials` output.

Include `## Market / Valuation Context` only when the user explicitly requested market/valuation context or when the workflow clearly requires it. Do not add it as a permanent default Standard section.

Include market / valuation context only when:

- the user explicitly requests valuation, current price, current market cap, EV, liquidity, or current market context; or
- market cap / EV / liquidity is materially needed to frame financial scale. Interpret this narrowly; do not use it to justify default market-data fetching in every normal report.

If included, market data must be clearly labeled as supporting market context and must follow:

- `/home/jordan/.hermes/profiles/midas/rules/OUTPUT.md` `Market-Data Display Rule` for chat display
- `/home/jordan/.hermes/profiles/midas/rules/MARKET_DATA.md`
- `/home/jordan/.hermes/profiles/midas/rules/METRICS.md` for valuation multiples

Use the canonical helper output directly. Do not call or parse `!market` user-facing output text. In chat, do not show internal tool paths, helper names, raw provider errors, unavailable-field dumps, exact timestamps with seconds, long helper metadata, or repeated provider limitations by default.

Allowed fields when available:

- current/recent price;
- provider market cap;
- volume or liquidity context;
- enterprise-value inputs only when cash/debt/share-count inputs are cleanly sourced and timing mismatches are labeled;
- valuation multiples only when numerator and denominator are cleanly sourced, period-labeled, and calculated under `METRICS.md`.

Required labels when market data is displayed in chat:

- compact provider/source;
- concise as-of date, e.g. `Market data: [Provider], as of [Month Day, Year].`

Preserve exact timestamp, timezone, limitations, unavailable fields, helper/tool details if useful, and timing mismatch between live market data and filing-derived inputs in the saved artifact when needed. Include timing mismatch or limitations in chat only when materially necessary to avoid misleading the user.

Market data must not be used as evidence for:

- revenue;
- margins;
- profitability;
- cash flow;
- free cash flow;
- debt;
- dilution;
- balance-sheet strength;
- accounting quality;
- segment results;
- financial-statement conclusions;
- metric quality.

Suggested optional section shape:

```md
## Market / Valuation Context

Bottom Line: [Financial-scale or valuation-context read-through first. Do not state cheap/expensive/fair-value unless fully supported.]

Market data: [Provider], as of [Month Day, Year].

Selected context: [Price, market cap, EV, valuation multiple, liquidity, or other useful market-context numbers when relevant and cleanly sourced.]

Source limitation: [Use only if materially needed in chat; otherwise preserve timing mismatch, exact timestamp/timezone, provider limitations, unavailable fields, and helper/tool detail in the saved artifact.]
```

Do not start the section with a metadata block. The user-facing section should lead with the financial/valuation read-through and selected numbers, not provider mechanics.

Prohibited:

- Buy/Sell/Hold language;
- price targets;
- position sizing;
- entry/exit guidance;
- trade advice;
- default PEG;
- unsupported cheap/expensive/reasonable/fair-value conclusions;
- using market data to prove financial-statement quality or metric quality.

---

## Risks / Caveats

Required risk behavior:

- Include financial risks and watchpoints based on reviewed evidence.
- Identify metric-quality, accounting-quality, liquidity, solvency, dilution, margin, cash-conversion, and source limitation issues when material.
- If no major financial risks are identified, say so only after the relevant areas were checked.
- Do not turn the output into a downside-only `!risk` report.

In normal output, financial risks and watchpoints belong in `## Financial Risks`. Source limitations belong in `## Source Notes` and `## What To Verify Next`. Do not merge these sections unless the command is in a clean failure state.

---

## Best Next Command

Best Next Command is optional in normal output. When useful, include it as its own report-style section after `## Source Notes` and before the final saved-path confirmation line. Make this context-aware using the ticker workspace state:

- If `workspace/tickers/[ticker]/research.md` exists, preserve existing routing logic: prefer `!thesis [TICKER]` to turn the business-model and financial evidence into a thesis view, or `!risk [TICKER]` if the financial review surfaced debt, dilution, liquidity, cash-conversion, accounting, or margin fragility.
- If `workspace/tickers/[ticker]/research.md` does not exist, prefer `!research [TICKER]` to build the business-model view behind the financials.
- Use `!full [TICKER]` only when the user wants the complete MIDAS packet.
- Use `!earnings [TICKER]` when latest-quarter or earnings-update work is the right next step.

Normal format:

```md
## Best Next Command

`!command TICKER` — Reason.
```

Examples:

- `` `!research [TICKER]` — Build the business-model view behind these financials. ``
- `` `!thesis [TICKER]` — Turn the existing business-model and financial evidence into a thesis view. ``
- `` `!risk [TICKER]` — Pressure-test dilution, liquidity, cash-conversion, or accounting pressure points. ``
- `` `!full [TICKER]` — Build the complete MIDAS packet. ``
- `` `!earnings [TICKER]` — Review the latest-quarter earnings update. ``

Do not recommend a next command when it would be noisy or unnecessary.

Display rules:

- Use `## Best Next Command` as the section heading.
- Insert one blank line after the heading.
- Body must be command-first: `` `!command TICKER` — Reason. ``
- The command must be wrapped in backticks.
- The first letter of the reason after the dash must be capitalized.
- Do not repeat `Best Next Command:` or `Best next command:` inside the section body.
- Do not auto-run downstream commands.

---

## Standard Output Contract

Normal `!financials [ticker]` is the mandatory Standard-only output across all tickers and companies. Use this section as the source of truth for normal/default output. No ticker may receive a custom abbreviated, compact-style, full-style, or deep-style structure.

Parser/output safeguard:

- Treat the first ticker/company argument after `!financials` as the security identifier.
- Uppercase ticker symbols such as `NOW` must not be interpreted semantically as a time keyword, shorthand, or mode.
- Ticker-like words such as `DEEP` remain ticker/company text unless the request clearly asks for a different command scope.
- Former Compact-style words are style hints or boundary prompts, not modes.
- Former Full/Deep-style words are routing/boundary prompts when they ask for non-financials scope, not modes.

Normal output should be section-complete but bounded. It should not become a full filing audit, full valuation, full thesis, or filing dump.

Normal output must use this exact section order:

1. `# 🪙 [TICKER] | [Company Name] Financial Analysis`
2. `## Introduction`
3. `## Summary`
4. `## Revenue`
5. `## Margins`
6. `## Profitability`
7. `## Cash Flow`
8. `## Balance Sheet`
9. `## Dilution`
10. `## Capital Returns`
11. `## Metric Quality`
12. `## Financial Quality Score`
13. `## Financial Risks`
14. `## What To Verify Next`
15. `## Source Notes`
16. `## Best Next Command`, when useful
17. Final line: `Saved to: workspace/tickers/[ticker]/financials.md`

For normal output, `Saved to: workspace/tickers/[ticker]/financials.md` must appear exactly once and only as the final line of the user-facing response after the report body is complete. It must not appear in or immediately after `## Introduction`, before `## Source Notes`, before `## Best Next Command` when that section is included, or in a separate default Artifact section.

Heading-spacing rule: every Markdown section heading must be followed by one blank line before body text. Do not place body text on the same line as a heading, and do not jam a heading directly against the paragraph in chat or saved artifact.

### Standard Format

```md
# 🪙 [TICKER] | [Company Name] Financial Analysis

## Introduction

[2–4 sentence scope statement covering what the report reviews, source base at a high level, financial-statement and metric-quality scope, and non-recommendation boundary.]

## Summary

[Thesis-first financial-quality read-through: what is strong, fragile, improving, deteriorating, or not yet knowable from the reviewed financial evidence.]

## Revenue

[Revenue trend, growth inside the revenue discussion, period labels, drivers, segment revenue when disclosed, and calculations where useful.]

## Margins

[Gross/operating/net margin trend, margin mix, and period-labeled margin calculations where meaningful.]

## Profitability

[GAAP profitability, operating income/loss, net income/loss, earnings quality, ROE/ROA when useful and denominator-labeled.]

## Cash Flow

[CFO, capex, FCF definition, FCF trend, and cash-conversion caveats.]

## Balance Sheet

[Cash, debt, net debt/cash, liquidity, maturities/covenants if disclosed.]

## Dilution

[Share count trend, SBC, issuance, repurchases, and dilution watchpoints.]

## Capital Returns

[Buybacks, dividends, and whether capital returns appear covered by earnings or cash flow. State if none were disclosed or meaningful.]

## Metric Quality

[Metric definitions, GAAP/non-GAAP separation, reconciliations, recurring adjustments, accounting-quality caveats, source quality, and unavailable/non-meaningful metrics.]

## Financial Quality Score

[score]/10 - [Assessment]

Keep the generated financial-quality score and assessment; this is formatting only. Use a plain hyphen after the score and write the assessment cleanly after the dash, e.g. `8/10 - Strong financial quality, with margin/SBC/capital-return watchpoints.` Do not hardcode a score, add a new rubric, or change scoring logic. If evidence is insufficient to score, state why rather than inventing precision.

## Financial Risks

- [Financial risk or watchpoint, if material.]
- [Financial risk or watchpoint, if material.]
- [Financial risk or watchpoint, if material.]

If no material financial risks are found, say so only after the relevant areas were checked.

## What To Verify Next

[Specific financial-statement, metric-quality, source, or next-filing items that would improve or weaken the financial-quality view.]

## Source Notes

- [Filing type] — filed [date]; period ended [date]; used for [source basis].
- [Earnings release / company release] — dated [date]; used for [source basis], if used.
- [Investor presentation] — dated [date]; used for [source basis], if used.

[Missing disclosures, source freshness, source limitations, line-citation limitations, market-data exclusion/inclusion, and calculated-metric labeling when relevant.]

## Best Next Command

`!command TICKER` — Reason.

Saved to: workspace/tickers/[ticker]/financials.md
```

---

## Audit Output Contract

Use this output only for `!financials [ticker] -audit`.

Audit output must not include:

- raw source dump
- hidden reasoning
- scratch work
- tool logs
- internal prompts
- giant filing excerpts
- saved-path confirmation
- artifact write claims

Audit format:

```md
# [TICKER] | !financials Audit

Audit Result: Pass / Partial / Blocked

## Source / Filing Basis

[Identity, source basis, source freshness, and filings/documents checked or not checked.]

## Existing Artifact Status

[Read-only status of existing financials artifact if inspected.]

## Standard Output Contract Check

[Whether the existing or expected output matches the Standard-only section/order/save-path contract.]

## Financial Statement Coverage

[Revenue, margins, profitability, cash flow, balance sheet, dilution, capital returns, and financial risks coverage.]

## Metric Coverage

[Metric areas covered, missing, stale, unavailable, or not meaningful.]

## Metric Discipline

[GAAP/non-GAAP labeling, period/source/unit labels, reported/adjusted/calculated status, reconciliation limits, FCF definition, and market-data labeling if used.]

## Source Limitations

[Missing filings, unavailable disclosures, stale data, line-citation limits, timing limitations, or source limitations.]

## Output Safety

[Recommendation-language, valuation-boundary, false-save, and downstream-command safety checks.]

## Artifact / Write Boundary

[Confirmation that audit mode wrote nothing, created no artifacts/folders, and made no saved-path claim.]

## Recommended Next Step

[Neutral next step, if useful.]

No files changed — audit mode was read-only.
```

If no-write cannot be guaranteed, use the blocked fallback from `SKILL.md` and stop before source gathering.

---

## Ticker Consistency Finalization

Before saving or sending normal output, the active user ticker/company, resolved issuer, report title, artifact path, saved-path line, and source base must all match. If any element does not match, hard stop and regenerate for the active ticker from sources; do not patch only the title/path.

---

## Artifact Behavior

Writes artifacts: `Yes` for normal output; `No` for audit mode.

Artifact behavior follows:

`/home/jordan/.hermes/profiles/midas/rules/ARTIFACTS.md`

Default artifact behavior:

- Normal `!financials [ticker]` saves by default when complete.
- Audit `!financials [ticker] -audit` writes nothing.

Artifact location:

- Normal: `workspace/tickers/[ticker]/financials.md` using the canonical ticker normalization from `rules/ARTIFACTS.md`.

When the normal artifact is written, output should include exactly one saved-path confirmation, and in normal user-facing output it must be the final line:

```md
Saved to: workspace/tickers/[ticker]/financials.md
```

Do not claim an artifact was written unless it was actually created or updated.
Do not create, update, or mention `financials.compact.md` as active command-mode behavior.
Do not use a separate Artifact section by default.
Do not mutate watchlists or indexes.
Do not auto-run downstream commands.
Do not use old artifact paths that place ticker folders directly under the workspace root.

---

## Failure Output Contract

Use failure output when the command cannot complete its intended task.

Common failure cases:

- Missing ticker/company/input
- Ambiguous ticker/company identity
- SEC or primary-source filings unavailable
- Latest financial source too stale for the requested claim
- Metric cannot be calculated or is not meaningful
- Market data unavailable when valuation context is requested
- Artifact write failure
- Current output contaminated by unrelated prior-run state

Failure output should include:

1. What failed
2. Why it failed
3. What evidence or input is missing
4. Best next step

Include artifact/no-save wording in failure output only when artifact state is user-relevant. Audit output must not claim `Saved to:` and should end with read-only/no-files-changed language when audit actually ran read-only.

Failure format:

```md
Unable to complete: [specific failure]
Reason: [clear explanation]
Missing or needed: [input/evidence/data]
Best next step: [neutral command or user action]
[No artifact saved, only when artifact state is user-relevant.]
```

For unresolved company/ticker failures, use:

```md
Unable to complete: company identity could not be resolved.

Reason: I could not match [input] to a public-company ticker, legal company name, or SEC filer.

Missing or needed: a valid public-company ticker or exact company name.

Best next step: Send a valid public-company ticker or exact company name.

[No artifact saved, only when artifact state is user-relevant.]
```

Recovery language must be neutral. Do not suggest a specific real ticker or company as an example unless the user explicitly asked for examples, the ticker/company is part of the current request, or the output is command help/menu text rather than a failed company lookup.

Do not fabricate results to avoid a failure state.

Do not save incomplete output as `financials.md`.

---

## Command-Specific Required Sections

Required for normal Standard-only output, in this exact order:

- `# 🪙 [TICKER] | [Company Name] Financial Analysis`
- `## Introduction`
- `## Summary`
- `## Revenue`
- `## Margins`
- `## Profitability`
- `## Cash Flow`
- `## Balance Sheet`
- `## Dilution`
- `## Capital Returns`
- `## Metric Quality`
- `## Financial Quality Score`
- `## Financial Risks`
- `## What To Verify Next`
- `## Source Notes`
- `## Best Next Command`, when useful
- Final line: `Saved to: workspace/tickers/[ticker]/financials.md` after successful save

Optional content may be included inside the required sections when useful, but do not add or substitute a compact-style, full-style, or deep-style structure:

- Segment financials, if disclosed
- Growth inside `## Revenue`
- Share count inside `## Dilution`
- GAAP vs non-GAAP inside `## Metric Quality`
- Financial red flags or disconfirming evidence inside `## Financial Risks`
- Source limitations inside `## Source Notes` and `## What To Verify Next`
- Limited market / valuation context, only when requested or when market cap / EV / liquidity is materially needed to frame financial scale; if used, keep it separate from filing-backed financial-statement conclusions
- Setup Classification, only when requested or when a final setup view is included
- Best Next Command, when useful, using the `## Best Next Command` section in normal output with command-first body format: `` `!command TICKER` — Reason. ``

Prohibited by default:

- Price targets
- Buy/sell/hold recommendations
- Position sizing
- Trade advice
- Default cheap/expensive/reasonable/fair-value language
- Default PEG
- Unsupported valuation conclusions
- Full valuation model
- Full business-model report
- Bull/base/bear thesis
- Downside-only risk report
- Complete MIDAS packet
- Hidden-gem ranking
- False saved claims
- Watchlist mutation claims
- Downstream command auto-runs
- Unsupported GAAP/non-GAAP equivalence
- Unlabeled metrics
- Stale market data presented as current

---

## Command-Specific Table Standards

Use tables only when they improve scanability.

Required tables: `None`

Optional tables:

- Segment financial table
- Debt maturity table
- Share-count / capital-return table
- GAAP vs non-GAAP reconciliation summary

Table rules:

- Keep tables compact.
- Include period/date context.
- Include units.
- Label GAAP vs non-GAAP.
- Do not show unavailable metrics as known.
- Use `Not disclosed`, `Not meaningful`, or `Not calculable` when needed.

---

## Command-Specific Language Standards

Preferred language:

- `Financial quality appears...`
- `The filing-backed evidence shows...`
- `FCF is defined here as...`
- `This metric is not meaningful because...`
- `Source limitation: ...`
- `## Best Next Command`
- `` `!command TICKER` — Reason. ``
- `What prevents the financials from being decisive by themselves: ...`

Guardrail-style response language:

- If the user asks whether to buy, sell, hold, size, or requests a price target, reframe as research only.
- Do not advise a personal investment decision.
- State that `!financials` can assess financial quality, metric quality, and information gaps, but cannot provide buy/sell/hold instructions, position sizing, or price targets.
- Prefer the heading/phrase `What prevents the financials from being decisive by themselves:` over `What stops me from calling...` or similar personal-decision language.
- Prefer the `## Best Next Command` section with command-first body format over inline `Best Next Command:` in normal output. Guardrail-only refusals that are not a completed normal report may use neutral research-command wording when needed, but must not imply buy/sell/hold, sizing, or price-target advice.

Avoid:

- `Buy`, `Sell`, `Hold`, `Strong Buy`
- `Price target`
- `Cheap`, `expensive`, or `reasonable` as default valuation conclusions
- `Guaranteed`, `no-brainer`, `must own`, or hype language
- Treating adjusted metrics as GAAP
- Treating valuation context as a recommendation
- Personal decision language that implies MIDAS is advising what the user should do with capital

Required caveat in Standard `## Introduction`:

- State that the report is a financial-statement and metric-quality review, not a full valuation, price target, or buy/sell recommendation.

---

## Examples Needed

Examples and regression cases live in:

`evals/financials.eval.md`

The eval file should test that this output contract is followed.

---

## Placeholder Cleanup Rule

This output file should not contain unresolved template placeholders. Before marking `!financials` Active, confirm evals pass and the command registry matches the metadata.

---

## Stability Checklist

For this Active output contract, confirm:

- It references global output rules instead of duplicating them.
- It defines normal and audit output behavior.
- It clearly states classification is optional.
- It clearly states scoring is optional.
- It clearly states metrics are required.
- It clearly states artifacts are written in normal by default.
- It defines failure behavior.
- It avoids command workflow instructions that belong in `SKILL.md`.
- It avoids source hierarchy rules that belong in `rules/SOURCES.md`.
- It avoids scoring rubric details that belong in `rules/SCORING.md`.
- It avoids metric formula libraries that belong in `rules/METRICS.md`.
- Registry metadata matches `docs/COMMAND_REGISTRY.md`.
- Unsupported or unclear mode behavior is defined.
- Empty sections are omitted unless explicitly required.
- Artifact paths use `workspace/tickers/[ticker]/financials.md`.
- This file defines output shape only and does not duplicate command workflow logic.
