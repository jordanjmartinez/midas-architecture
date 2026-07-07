# MIDAS Command Output Contract — !risk

## Command

Command: `!risk`

Skill File: `skills/stock-analysis/risk/SKILL.md`

Output File: `skills/stock-analysis/risk/OUTPUT.md`

Registry Entry: `docs/COMMAND_REGISTRY.md`

Status: `Draft`

---

## Registry Consistency

This output contract should match the command’s Registry Metadata block in `skills/stock-analysis/risk/SKILL.md` and the command row in:

`docs/COMMAND_REGISTRY.md`

Expected registry values:

- Command: `!risk`
- Aliases: `/risk`, `risk`
- Category: `Risk Assessment`
- Status: `Draft`
- Skill path: `skills/stock-analysis/risk/SKILL.md`
- Output path: `skills/stock-analysis/risk/OUTPUT.md`
- Eval file: `evals/risk.eval.md`
- Classification: `Optional`
- Scoring: `Optional`
- Metrics: `Required`
- Artifacts: `Yes`

If this output file and the registry disagree, treat that as registry drift.

---

## Purpose

This file defines the command-specific output contract for `!risk`.

`!risk` output should present one filing-backed company risk assessment. It should identify the risks most likely to weaken or break a thesis, explain the evidence and uncertainty behind those risks, preserve source visibility, and avoid investment recommendations.

This file does not redefine global output standards.

---

## Output / Workflow Boundary

This file defines output shape only.

Workflow, parser behavior, source retrieval, artifact writing, and audit no-write control belong in:

`skills/stock-analysis/risk/SKILL.md`

Source hierarchy belongs in:

`rules/SOURCES.md`

Risk, scoring, classification, metric, and artifact standards belong in:

- `rules/GLOBAL.md`
- `rules/CLASSIFICATIONS.md`
- `rules/SCORING.md`
- `rules/RERATING.md`
- `rules/METRICS.md`
- `rules/ARTIFACTS.md`

This file should answer:

- Which output surfaces `!risk` supports.
- Which sections are required, optional, or prohibited.
- How source notes, audit output, artifacts, failures, and guardrails should appear.

This file should not answer:

- How sources are gathered.
- How SEC filings are parsed.
- How risk evidence is extracted.
- How artifacts are written.
- How command routing is implemented.

---

## Global Output Inheritance

`!risk` must follow the global MIDAS output rules in:

- `rules/GLOBAL.md`
- `rules/OUTPUT.md`
- `rules/SOURCES.md`
- `rules/MARKET_DATA.md`
- `rules/RERATING.md`
- `rules/METRICS.md`
- `rules/ARTIFACTS.md`

When classification or broader scoring is used, also follow:

- `rules/CLASSIFICATIONS.md`
- `rules/SCORING.md`

If this file conflicts with a global rule file, the global rule file wins unless the exception is explicitly documented here.

---

## Output Philosophy

`!risk` output should be:

- Filing-backed.
- Skeptical but fair.
- Ranked by materiality, not filing order.
- Clear about what could actually break the thesis.
- Specific about what to verify next.
- Conservative when evidence is missing or stale.
- Concise without losing source visibility or material risk coverage.

Avoid:

- Hype or fearmongering.
- Exaggerating low-probability risks.
- Treating boilerplate risk factors as equally important.
- Unsupported risk claims.
- Business-model report drift.
- Financial-statement review drift.
- Thesis memo drift.
- Complete packet drift.
- Price targets, Buy/Sell/Hold language, position guidance, entry/exit levels, support/resistance, breakout analysis, moving-average/trendline analysis, or trade timing.

---

## Supported Output Surfaces

Supported:

- Normal: supported. This is the default Standard-only filing-backed company risk assessment.
- Audit: supported only through `-audit`. This is no-write verification output.

Unsupported:

- Compact mode.
- Full mode.
- Deep mode.

Default output surface:

`Normal Standard-only filing-backed risk assessment`

Routing display rules:

- `!risk [ticker]` always uses the normal Standard-only risk assessment.
- `!risk [ticker] -audit` uses the no-write audit output contract.
- Former compact-style words such as `compact`, `quick`, `brief`, `short`, `concise`, and `summary` are style hints or boundary prompts, not modes.
- Former full/deep-style words such as `full`, `deep`, `detailed`, `expanded`, `deep-dive`, and `deepdive` are not modes.
- `-audit` is no-write and uses the audit output contract below.
- `--audit` is unsupported and should display: `Use -audit for !risk audit mode.`

Unsupported compact-style request boundary:

```md
!risk now uses one Standard filing-backed risk assessment. I can keep the sections concise, but the command still preserves source visibility, material risk coverage, and saves the canonical risk artifact.
```

Unsupported full/deep complete-packet request boundary:

```md
!risk is scoped to company risk assessment. Use !thesis [ticker] for thesis work, !research [ticker] for business-model research, !financials [ticker] for financial-statement review, or !earnings [ticker] for latest-quarter earnings review.
```

Do not auto-run those commands.

---

## Normal Standard-Only Output Contract

Every successful normal `!risk [ticker]` response should include the Standard-only sections unless the command cannot complete.

Normal output should be complete but bounded. It should not become a full filing audit, financial-statement report, valuation model, thesis memo, complete packet, source dump, or trade view.

### Normal Format

```md
#🗡️ [TICKER] | [Company Name] Risk Assessment

## Introduction

[2–4 sentence scope statement covering the company, source base, risk-assessment scope, and non-recommendation boundary.]

## Summary

[Concise conclusion identifying overall risk level when evidence is sufficient, the main thesis-breaking risk, and the biggest evidence limitation.]

## Key Risks

1. [Title Case Risk Name]

[Short paragraph explaining the material risk, why it matters, source-backed evidence, and whether it could break the thesis.]

Key monitor: [Specific metric, event, filing disclosure, covenant, customer issue, legal/regulatory development, or condition to watch.]

Severity: [Low / Moderate / High / Critical, only when evidence supports the label.]

2. [Title Case Risk Name]

[Short paragraph.]

Key monitor: [Specific monitor.]

Severity: [Low / Moderate / High / Critical, only when evidence supports the label.]

[Usually include 3–5 key risks. Do not force weak evidence into a ranked risk.]

## Balance Sheet Risk

[Discuss liquidity, cash, debt, maturities, covenants, financing needs, dilution, or capital structure risk when material. Label missing or undisclosed items.]

## Cash Flow Risk

[Discuss operating cash flow, FCF, working capital, capex, margin pressure, profitability, cash conversion, or cash burn when material. Label metric definitions, periods, and source basis.]

## Concentration Risk

[Discuss customer, revenue, product, segment, geography, supplier, partner, channel, or platform concentration when disclosed or materially inferable. Say not disclosed or not verified when needed.]

## Competitive Risk

[Discuss competitive pressure, pricing pressure, technology substitution, customer switching, market-share pressure, or moat durability risks when source-backed.]

## Regulatory Risk

[Discuss regulatory, legal, litigation, compliance, licensing, investigation, sanction, environmental, product-safety, data/privacy, or policy risk when material. Legal risk belongs here unless a separate legal discussion is clearly necessary inside the body.]

## Execution Risk

[Discuss operational execution, strategy, integration, management execution, capacity, product launch, cost program, manufacturing, supply chain, or go-to-market risk when material.]

## Thesis Breakers

[Identify the risks or evidence changes that could most clearly weaken or break the thesis. Separate verified evidence from possible or unverified failure points.]

## What To Verify Next

[Short list of next diligence items, missing disclosures, stale sources, risk metrics, events, filings, or disconfirming evidence to check. Include source limitations that drive next-step work.]

## Source Notes

- [Filing type] — filed [date]; period ended [date]; used for [source basis].
- [Company release / earnings release] — dated [date]; used for [source basis], if material.
- [Credit agreement / debt filing / covenant filing] — filed [date]; used for [source basis], if material.
- [Source limitation] — [missing, stale, unavailable, not disclosed, or not meaningful item].

## Best Next Command

`!command TICKER` — Reason.

Saved to: workspace/tickers/[ticker]/risk.md
```

For normal output, `Saved to: workspace/tickers/[ticker]/risk.md` must appear exactly once and only as the final line of the user-facing response after the report body is complete and the artifact write has succeeded.

### Required Normal Sections

The following sections are required for normal Standard-only output, in order:

1. `# ⚖️ [TICKER] | [Company Name] Risk Assessment`
2. `## Introduction`
3. `## Summary`
4. `## Key Risks`
5. `## Balance Sheet Risk`
6. `## Cash Flow Risk`
7. `## Concentration Risk`
8. `## Competitive Risk`
9. `## Regulatory Risk`
10. `## Execution Risk`
11. `## Thesis Breakers`
12. `## What To Verify Next`
13. `## Source Notes`
14. `## Best Next Command`
15. Final line: `Saved to: workspace/tickers/[ticker]/risk.md` after successful save

Optional content may be included inside the required sections when useful, but do not add or substitute compact-style, full-style, or deep-style structures.

---

## Title and Introduction

Required title format:

```md
# ⚖️ [TICKER] | [Company Name] Risk Assessment
```

The introduction should usually be 2–4 sentences and explain:

- What the report is assessing.
- Which primary sources are being used.
- That the command is focused on company risk assessment.
- That it is not a valuation model, thesis memo, recommendation, capital-allocation instruction, or trading view.

---

## Source Notes

Normal Source Notes should be concise.

Do not require raw SEC URLs by default.
Do not require accession numbers by default unless needed for disambiguation.

Preferred normal Source Notes format:

```md
- [Filing type] — filed [date]; period ended [date]; used for [source basis].
- [Company release / earnings release] — dated [date]; used for [source basis].
- [Credit agreement / debt filing / covenant filing] — filed [date]; used for [source basis], if material.
- [Source limitation] — [missing, stale, unavailable, not disclosed, or not meaningful item].
```

Accession numbers and URLs may remain internal and may appear in audit, source-recovery, or debug contexts when useful.

Normal Source Notes should preserve:

- Filing/source type.
- Filing/source date.
- Period or report date.
- Source basis.
- Source freshness.
- Missing disclosures.
- Source limitations.
- Calculated metric labeling when relevant.

Source Notes should not become a raw source dump, long filing excerpt block, hidden reasoning, tool log, or full SEC URL list by default.

---

## Risk Severity and Overall Risk Level

Risk severity labels allowed for individual risks when evidence supports a label:

- `Low`
- `Moderate`
- `High`
- `Critical`

Use only these exact fixed labels. Do not use mixed or range labels such as `Moderate to High`, `Low / Moderate`, or `High-to-Critical`. If nuance is needed, keep the fixed severity label and explain the nuance in the risk text.

Overall Risk Level may appear in `## Summary` when evidence is sufficient:

- `Overall Risk Level: Low`
- `Overall Risk Level: Moderate`
- `Overall Risk Level: High`
- `Overall Risk Level: Critical`

Overall Risk Level is a risk-specific research label, not an investment recommendation.

If evidence is insufficient, withhold precise rating language or state that evidence is insufficient.

---

## Classification Behavior

Classification usage: `Optional`

This command does not use Setup Classification by default.

If the user explicitly asks for setup classification, or if the output includes a setup view beyond risk level, output may include:

```md
Setup Classification: [classification]
Setup Modifiers: [modifier 1], [modifier 2]
Evidence Confidence: [A / B / C / D]
```

Do not force Setup Classification into a raw risk assessment. Overall Risk Level is not the same as Setup Classification.

Do not create new classification labels.

---

## Scoring Behavior

Scoring usage: `Optional`

`!risk` may include Overall Risk Level when evidence supports it. This is not a Global Research Score.

Do not create a new risk scoring formula.
Do not produce a Global Research Score by default.

If broader scoring is requested, use `rules/SCORING.md`. Risk can affect the Global Research Score’s Risk / Fragility / Downside Protection pillar, but `!risk` should not produce a full Global Research Score by default.

If the user wants a complete scored packet and Best Next Command is useful, use the standalone report-style format:

```md
## Best Next Command

```

---

## Metrics Behavior

Metrics usage: `Required` when available and material to risk.

Risk-relevant metrics should be used when available and material. This does not mean `!risk` should become `!financials`.

Risk metric areas to check when relevant:

- Cash, debt, net debt/net cash, liquidity, maturities, and covenants.
- Operating cash flow and free cash flow.
- Revenue growth, margin pressure, or profitability deterioration.
- Share count, dilution, SBC, ATM programs, converts, warrants, or financing risk.
- Customer, product, segment, geography, supplier, or partner concentration.
- Backlog, RPO, book-to-bill, retention, churn, capacity, utilization, or other operating visibility metrics.
- Valuation, rerating, liquidity, trading-volume, market-cap/scale, price-performance, or market-expectations context only when explicitly requested or materially needed to frame risk.

Metric constraints:

- Follow `rules/METRICS.md`.
- Preserve period, source, unit, and GAAP/non-GAAP status when relevant.
- If a metric is not meaningful, stale, unavailable, or not calculable, say so.
- Do not use undefined FCF, adjusted EBITDA, customer concentration, or valuation metrics.
- Do not make cheap/expensive conclusions from one multiple.
- Do not create price targets.

Market-data constraints:

- Use market data only when explicitly requested or materially needed to frame valuation risk, rerating risk, liquidity/trading-volume risk, market-cap/scale context, price-performance context, or market-expectations risk.
- Market data must not prove business-model risk, revenue risk, margin risk, cash-flow risk, filing-derived debt/liquidity risk, filing-derived dilution risk, customer concentration, supplier concentration, regulatory/legal risk, or management execution risk.
- Market data must not prove business quality, financial quality, customer demand, revenue, margins, cash flow, debt/liquidity facts, dilution, legal/regulatory claims, thesis validity, or any company-specific risk claim requiring filing-backed evidence.
- Market data output must follow `MARKET_DATA.md` display and boundary requirements.
- If market data is unavailable, stale, incomplete, plan-limited, or not usable, state that market-data-based risk was not assessed. Do not infer missing price, market cap, volume, enterprise value, valuation multiple, or price-performance data.

Valuation or rerating risk may appear only when explicitly requested or material to risk framing, usually inside `## Key Risks`, `## Thesis Breakers`, or `## What To Verify Next`.

---

## Best Next Command

Best Next Command is required in normal output unless no useful next command exists. When included, it must be a standalone section after `## Source Notes` and before the final saved-path line.

Required format:

```md
## Best Next Command

`!command TICKER` — Reason.
```

Display rules:

- Wrap the command in backticks.
- Use command-first format: `!command TICKER` — Reason.
- The reason after the dash should begin with a capital letter and end with a period when sentence-style.
- Do not repeat `Best Next Command:` under the section heading.
- Do not recommend a next command when it would be noisy or unnecessary.
- Do not auto-run the recommended command.

Common choices after workspace-aware routing:

- `!research [TICKER]` when the business-model evidence base is missing.
- `!financials [TICKER]` when financial-fragility questions require financial-statement work and `financials.md` is missing, stale, incomplete, missing material filings, or insufficient.
- `!thesis [TICKER]` when research, financials, and risk evidence exist but thesis is missing.
- `!thesis update [TICKER]` when thesis exists but the risk report used materially newer evidence than the existing thesis.
- `!earnings [TICKER]` when latest-quarter results are the main evidence gap.
- When research, financials, risk, and thesis artifacts all exist and are current, note that the core research set for the ticker is complete and `!promote [TICKER]` is eligible.

---

## Audit Output Contract

Use this output only for `!risk [ticker] -audit`.

Audit output is no-write verification output. It must not claim that an artifact was saved.

Audit format:

```md
# [TICKER] | !risk Audit

Audit Result: Pass / Partial / Blocked

## Source / Filing Basis

[Latest annual/interim source basis, source freshness, and whether primary sources are sufficient for a normal risk review.]

## Existing Artifact Status

[Whether `workspace/tickers/[ticker]/risk.md` exists, appears current by lightweight header/source-period review, is missing, stale, incomplete, or was not inspected. Read-only only.]

## Standard Output Contract Check

[Whether the existing or expected output matches the Standard-only section/order/save-path contract.]

## Risk Coverage

[Coverage of key risks, balance sheet, cash flow, concentration, competitive, regulatory, execution, and thesis-breaker areas.]

## Missing Evidence

[Missing, stale, unavailable, not disclosed, or not meaningful evidence.]

## Source Limitations

[Concise source limitations. Do not dump raw sources.]

## Output Safety

[No recommendation, no price target, no trade advice, no unsupported risk claims, no unlabeled metrics, no downstream command execution.]

## Artifact / Write Boundary

[Confirmation that audit mode wrote nothing, created no artifacts/folders, and made no saved-path claim.]

## Recommended Next Step

[Next research step or command, if useful. Do not auto-run it.]

No files changed — audit mode was read-only.
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
- Watchlist mutation claims.
- Downstream command run claims.

If no-write cannot be guaranteed, use the blocked fallback from `SKILL.md` and stop before source gathering.

---

## Artifact Behavior

Writes artifacts: `Yes` for normal output; `No` for audit mode.

Artifact behavior follows:

`rules/ARTIFACTS.md`

Normal artifact behavior:

- Normal `!risk [ticker]` saves by default when complete.
- Normal output saves only to `workspace/tickers/[ticker]/risk.md` using canonical ticker normalization.
- Normal output should include the final saved-path confirmation only after successful write verification:

```md
Saved to: workspace/tickers/[ticker]/risk.md
```

No-write audit artifact behavior:

- Audit writes nothing.
- Audit must not include saved-path confirmation.
- Audit must not claim an artifact was written.

Do not claim an artifact was written unless it was actually created.
Do not use old artifact paths that place ticker folders directly under the workspace root.
Do not save incomplete output as `risk.md`.
Do not save validation notes, audit output, runtime-test summaries, source manifests, evidence ledgers, proof packets, schemas, fixtures, or scratch work as `risk.md`.
Do not include a separate `Artifact` section by default.
Do not mutate watchlists or update indexes as part of normal artifact saving.

---

## Standard Pre-Save Validation

Generic command-generated artifact save-order discipline is governed by `rules/ARTIFACTS.md`: validate before first write, save only after validation passes, verify the saved artifact, and show the saved-path confirmation only after a successful write.

Hard-stop and do not save until the draft passes all checks:

- Required normal sections are missing or out of order.
- The output contains compact-style, full-style, deep-style, receipt-style, or completion-summary replacement structure instead of the required Standard-only sections.
- Any Markdown section heading is followed by body text on the same line or without one blank line before body text.
- `## Key Risks` omits source-backed evidence, materiality, thesis impact, or practical monitors for material risks when evidence supports them.
- Artifact path is anything other than `workspace/tickers/[ticker]/risk.md` for normal output.
- A saved-path confirmation appears before successful save/verification, appears more than once, is not the final line after save, or names any path other than `workspace/tickers/[ticker]/risk.md`.
- Any risk severity or final risk level uses a mixed/range label instead of exactly `Low`, `Moderate`, `High`, or `Critical`.
- A section becomes a full business-model report, full financial statement review, thesis memo, valuation model, source audit trail, or filing dump.
- `## Balance Sheet Risk` omits material liquidity, debt, maturity, covenant, financing, or dilution evidence that was available and risk-relevant.
- `## Cash Flow Risk` omits material CFO, FCF, working-capital, capex, margin-pressure, cash-burn, or cash-conversion evidence that was available and risk-relevant.
- `## Concentration Risk` omits disclosed customer, revenue, product, segment, geography, supplier, partner, channel, or platform concentration evidence that was available and risk-relevant.
- `## Regulatory Risk` omits material legal, litigation, regulatory, compliance, licensing, investigation, or policy risk evidence that was available and risk-relevant.
- `## Thesis Breakers` fails to identify the clearest evidence-backed failure points or mixes possible/unverified risks with verified risks without labeling uncertainty.
- `## Source Notes` becomes a raw source dump, full URL list, accession block, tool log, or hidden reasoning section by default.
- `## Best Next Command`, when included, is not a standalone section after `## Source Notes` and before the final saved-path line, or does not use command-first format with the command wrapped in backticks.
- Best Next Command recommends a repeat command when the relevant artifact already exists and appears current enough, without explicitly stating staleness, incompleteness, missing material evidence, or insufficiency.
- The report contains validation/runtime-test language such as `## Verification`, `Verification`, `Clean runtime checks passed`, `runtime checks passed`, `Checks Passed`, `eval`, `smoke test`, or checklist language about contract validation.
- Material risk claims are not tied to filing/source support in the relevant section, not just a generic source list.
- Market data appears without provider/source and as-of context when used.
- Market data is used to prove business-model, revenue, margin, cash-flow, debt/liquidity, dilution, customer concentration, supplier concentration, regulatory/legal, management execution, or thesis-validity claims.
- Valuation/rerating risk appears as a default standalone section instead of being included only when explicitly requested or material to risk framing.
- The report contains price targets, Buy/Sell/Hold calls, position sizing, entry/exit levels, support/resistance, breakout analysis, moving-average or trendline analysis, trade timing, or claims that price action proves fundamentals.
- Audit output includes saved-path confirmation, artifact write claims, folder creation claims, index updates, watchlist mutations, downstream command runs, schemas, proof packets, source manifests, evidence ledgers, or fixture creation.

If validation fails, return failure output and do not claim a save. Never include validation/checklist language inside a final risk report or saved artifact.

---

## Failure Output Contract

Use failure output when the command cannot complete safely or honestly.

Failure output should include:

```md
Unable to complete:
[short reason]

Source limitation:
[what is missing, stale, unavailable, ambiguous, or not verifiable]

Best next step:
[what to check next, if useful]
```

Do not include `Saved to:` unless a valid normal artifact was actually saved.

Audit failure should follow the audit blocked fallback in `SKILL.md` when no-write cannot be guaranteed.

---

## Command-Specific Required Sections

Required for normal Standard-only output, in this exact order:

- Report title
- Introduction
- Summary
- Key Risks
- Balance Sheet Risk
- Cash Flow Risk
- Concentration Risk
- Competitive Risk
- Regulatory Risk
- Execution Risk
- Thesis Breakers
- What To Verify Next
- Source Notes
- Best Next Command
- Final saved-path confirmation after successful save

Required for audit output:

- Audit title
- Audit Result
- Source / Filing Basis
- Existing Artifact Status
- Standard Output Contract Check
- Risk Coverage
- Missing Evidence
- Source Limitations
- Output Safety
- Artifact / Write Boundary
- Recommended Next Step
- No-files-changed audit confirmation

---

## Command-Specific Table Standards

Avoid tables in normal Telegram-facing output unless they clearly improve readability. Bullets and short risk cards are preferred.

If tables are used in saved Markdown, they must be simple, readable, and not required for the core meaning.

---

## Command-Specific Language Standards

Preferred wording:

- `Filing-backed risk`
- `Source limitation`
- `Not disclosed in the reviewed filings`
- `Could not verify`
- `Possible but not verified`
- `Thesis breaker`
- `What to verify next`
- `Overall Risk Level`, only when evidence supports it

Avoid wording that implies advice or certainty beyond evidence:

- `Buy`, `Hold`, or `Sell` as recommendation language.
- `Price target`.
- `Position sizing`.
- `Entry`, `exit`, `breakout`, `support`, `resistance`, moving-average/trendline trading language, or trade timing.
- `Guaranteed`, `certain`, `obvious`, or unsupported severe-risk claims.
- `Cheap`, `expensive`, or `fair value` conclusions by default.

---

## Placeholder Cleanup Rule

Before finalizing output, remove placeholders such as:

- `[TICKER]`
- `[Company Name]`
- `[date]`
- `[source basis]`
- `[insert]`
- `[if material]`
- Template notes from this file.

Do not save output containing unresolved placeholders unless the placeholder is intentionally quoted as part of an example or failure explanation.

---

## Stability Checklist

Before this output contract is considered Active, confirm:

- It defines normal and audit output behavior.
- It does not define Compact, Full, or Deep modes.
- Normal section order matches `SKILL.md`.
- Audit output writes nothing and claims no save.
- Artifact behavior follows `rules/ARTIFACTS.md`.
- Source behavior follows `rules/SOURCES.md`.
- Metric behavior follows `rules/METRICS.md`.
- Classification/scoring optionality follows `rules/CLASSIFICATIONS.md` and `rules/SCORING.md`.
- Normal output saves only to `workspace/tickers/[ticker]/risk.md`.
- Saved-path confirmation appears exactly once and only after actual successful write.
- Unsupported compact/full/deep requests do not activate internal modes.
- Guardrails prevent recommendation, valuation, trading, and source-fabrication drift.
- Evals are aligned in a later stage.

## Final Rule

`!risk` should make risk research clearer, faster, and more disciplined. It should show what can break the thesis, what is source-backed, what is uncertain, and what to verify next without becoming a recommendation, valuation model, or complete research packet.
