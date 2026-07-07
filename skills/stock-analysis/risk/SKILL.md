---
name: risk
description: Filing-backed risk assessment for a public company or ticker. Use for !risk [ticker/company], /risk [ticker/company], risk [ticker/company], or natural-language stock risk assessment requests.
version: 2.1.0
author: Midas / Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [stocks, equity-research, sec-filings, risk-assessment, investment-risk]
    related_skills: [research, financials, thesis, full, earnings]
---

# Midas Command Skill — !risk

## Command

`!risk`

## Registry Metadata

Command: `!risk`
Aliases: `/risk`, `risk`
Category: `Risk Assessment`
Status: `Draft`
Skill Path: `skills/stock-analysis/risk/SKILL.md`
Output Path: `skills/stock-analysis/risk/OUTPUT.md`
Eval File: `evals/risk.eval.md`
Uses Classification: `Optional`
Uses Scoring: `Optional`
Uses Metrics: `Required`
Writes Artifacts: `Yes`
Primary Global Rules: `GLOBAL.md, COMMAND_INTERFACE.md, SOURCES.md, MARKET_DATA.md, RERATING.md, METRICS.md, OUTPUT.md, ARTIFACTS.md, CLASSIFICATIONS.md, SCORING.md`

## Purpose

`!risk` produces one filing-backed company risk assessment for a public company or ticker. It identifies the risks most likely to weaken or break a thesis, connects them to primary-source evidence, highlights missing or uncertain evidence, and recommends the best next research step.

This command is a focused company-risk command. It is not a business-model report, financial-statement review, thesis memo, complete Midas packet, hidden-gem ranking, valuation model, price-target output, or buy/sell recommendation.

---

## When To Use

Use this command when:

- The user invokes `!risk [company or ticker]`, `/risk [company or ticker]`, or `risk [company or ticker]`.
- The user asks for a risk assessment, downside pressure test, thesis-breaking risks, bear case, fragility review, or risk monitoring checklist for a public company.
- The user wants to know what could go wrong before building or updating a thesis.
- A prior `!research`, `!financials`, `!thesis`, `!earnings` output surfaced risks that need standalone review.

Do not use this command when:

- The user wants business-model research. Use or recommend `!research`.
- The user wants financial-statement and metric-quality analysis. Use or recommend `!financials`.
- The user wants bull/base/bear thesis construction. Use or recommend `!thesis`.
- The user wants a complete packet with scoring, classification, valuation, and integrated risks. Recommend completing `!research`, `!financials`, and `!thesis` so the four core artifacts form the packet.
- The user wants latest-quarter earnings review. Use or recommend `!earnings`.
- The user asks for buy/sell/hold instructions, position sizing, trade timing, or a price target. Reframe as risk research.

Do not auto-run downstream commands unless the user separately asks for them.

---

## Inputs

### Required Inputs

- Company name or ticker.

### Optional Inputs

- Specific risk focus: balance-sheet risk, liquidity, debt, covenants, cash-flow risk, FCF risk, customer concentration, revenue concentration, supplier concentration, competitive risk, regulatory risk, legal risk, litigation, execution risk, dilution, macro/cyclicality, commodity exposure, cyber risk, or another company-risk category.
- Period or filing focus: latest annual report, latest interim report, a named 10-K/10-Q/8-K, credit agreement, earnings release, investor presentation, legal/regulatory filing, acquisition/financing filing, or user-provided source.
- Source preference, when compatible with `rules/SOURCES.md`.
- Limited market or valuation context only when explicitly requested or materially needed to frame company-risk exposure.
- Request to classify the setup or include broader scoring.
- Optional audit flag: `-audit`.

### Input Clarification Rules

Ask for clarification only when missing or ambiguous identity would materially change the result.

If a ticker or company name is ambiguous, resolve the legal company name, ticker, exchange, and SEC CIK where applicable. If multiple plausible matches remain, ask the user to clarify before analysis.

If the company is clear enough to proceed, state the identity assumption and proceed.

---

## Aliases

Command aliases:

- `/risk`
- `risk`

There are no formal Compact, Full, or Deep output modes for `!risk`.

---

## Parser / Routing Behavior

Normal behavior:

- `!risk [ticker]` → run the normal Standard-only filing-backed company risk assessment.
- `!risk [ticker] -audit` → run no-write audit mode.

Audit flag:

- Single-dash `-audit` is canonical.
- If the user uses `--audit`, return this short correction and do not run the command:

```md
Use -audit for !risk audit mode.
```

Former compact-style words such as `compact`, `quick`, `brief`, `short`, `concise`, and `summary` are not output modes for `!risk`.

- Treat them as style hints only when compatible with the required Standard-only report.
- If the request conflicts with required source visibility, material risk coverage, or canonical artifact behavior, return:

```md
!risk now uses one Standard filing-backed risk assessment. I can keep the sections concise, but the command still preserves source visibility, material risk coverage, and saves the canonical risk artifact.
```

Former full/deep-style words such as `full`, `deep`, `detailed`, `expanded`, `deep-dive`, and `deepdive` are not `!risk` modes.

- If the request asks for a complete packet, recommend completing `!research [TICKER]`, `!financials [TICKER]`, and `!thesis [TICKER]`.
- If the request asks for thesis work, bull/base/bear framing, or a long-term view, recommend `!thesis [TICKER]`.
- If the request asks for business-model research, recommend `!research [TICKER]`.
- If the request asks for financial statements, metric quality, liquidity roll-forward, or full financial analysis, recommend `!financials [TICKER]`.
- If the request asks for latest-quarter or earnings-update work, recommend `!earnings [TICKER]`.
- If the request asks for a specific risk category, period, filing, covenant, litigation, regulation, customer concentration, balance-sheet risk, cash-flow risk, or thesis-breaking risk focus, keep it inside normal `!risk`.

Do not auto-run downstream commands.

---

## Global Rules

This command must follow:

- `rules/GLOBAL.md`
- `rules/COMMAND_INTERFACE.md`
- `rules/SOURCES.md`
- `rules/MARKET_DATA.md`
- `rules/RERATING.md`
- `rules/METRICS.md`
- `rules/OUTPUT.md`
- `rules/ARTIFACTS.md`

Use when applicable:

- `rules/CLASSIFICATIONS.md`
- `rules/SCORING.md`

Do not duplicate global rule content inside this command. Reference global rules instead.

---

## Command References

- `references/source-retrieval.md` — risk-source retrieval, latest annual/interim sources, material 8-Ks, debt/covenant/legal/regulatory source handling, source freshness, and audit no-write caveat.
- `references/risk-evidence.md` — disclosed vs inferred vs possible risk boundaries, thesis-breaker discipline, source limitations, and no unsupported/exaggerated risk claims.
- `references/risk-metrics.md` — command-local risk-metric interpretation that defers formulas and metric-labeling discipline to METRICS.md.
- `references/output-safety.md` — concise risk output hygiene, no old Full-mode structures, no false saved claims, canonical risk.md behavior, and audit no-write boundary.

---

## Workflow

Follow this command-specific workflow:

1. Parse the user request and determine whether it is normal `!risk [ticker]` or no-write audit mode `!risk [ticker] -audit`.
2. If the request uses `--audit`, return `Use -audit for !risk audit mode.` and stop.
3. Confirm the active requested ticker/company is the latest real user command target. Do not inherit ticker, artifact path, source state, or partial notes from interrupted or compacted prior runs.
4. Resolve company identity: legal company name, ticker, exchange, SEC CIK if applicable, and whether it is an SEC filer.
5. Determine whether the command has enough input to proceed. Clarify only if ambiguity remains material.
6. For no-write audit mode, follow the No-Write Audit Rule below before any source gathering.
7. Gather source evidence using `rules/SOURCES.md` and the command-specific source needs below.
8. Identify the latest relevant annual and interim risk sources. For SEC filers, prefer the latest Form 10-K and latest Form 10-Q when available.
9. Record filing dates, report periods, source identifiers, and source basis. Keep accession numbers and raw URLs available internally when useful, but do not require them in normal Source Notes unless needed for disambiguation, audit, source recovery, or debug context.
10. Review material recent 8-Ks, earnings releases, credit agreements, debt/covenant filings, acquisition filings, financing filings, legal/regulatory updates, investor presentations, or transcripts when they materially affect risk.
11. Review existing same-ticker workspace artifacts when available and useful: `research.md`, `financials.md`, `thesis.md`, `earnings.md`, `updates.md`, and `full.md`. Treat them as secondary synthesis inputs only; primary filings and official disclosures remain authoritative. Do not create missing artifacts unless the user explicitly asks.
12. Extract risk evidence from risk factors, MD&A, notes to financial statements, debt/liquidity footnotes, customer/segment/geography disclosures, legal proceedings, concentration disclosures, and material contracts or exhibits when relevant.
13. Separate filing-backed facts from management claims, interpretations, and future assumptions.
14. Separate disclosed risks from inferred risks. Label possible but unsupported risks as possible, not verified, or not disclosed.
15. Rank the most important risks by materiality and thesis-breaking potential, not by filing order or boilerplate length.
16. Review key risk areas: balance sheet, liquidity, debt/covenants, cash flow, FCF, concentration, competition, regulation/legal, execution, and thesis breakers.
17. Use risk-relevant metrics when available and material: cash, debt, liquidity, maturities, covenant risk, CFO/FCF, dilution, margin pressure, concentration, backlog/RPO, retention/churn, or other operating risk metrics.
18. Follow `rules/METRICS.md` whenever risk metrics appear. Preserve period, source, unit, and GAAP/non-GAAP status when relevant.
19. Avoid default live market data. Use market data only when explicitly requested or materially needed to frame valuation, rerating, liquidity/trading-volume, market-cap/scale, price-performance, or market-expectations risk.
20. When market data is used, follow `rules/MARKET_DATA.md` and keep it Tier 2 context. Do not call or parse `!market` user-facing output.
21. Do not use market data to prove business-model risk, revenue risk, margin risk, cash-flow risk, filing-derived debt/liquidity risk, filing-derived dilution risk, customer concentration, supplier concentration, regulatory/legal risk, management execution, thesis validity, business quality, financial quality, customer demand, revenue, margins, or cash flow.
22. If market data is unavailable, stale, incomplete, plan-limited, or not usable, complete the filing-backed risk review when possible and say the market-data-based risk was not assessed. Do not fabricate price, market cap, volume, enterprise value, valuation multiples, or price-performance data.
23. Include disconfirming evidence where useful, especially evidence that reduces or limits the apparent risk.
24. Avoid exaggerating risks. Do not invent unsupported risks. Say `not disclosed`, `not verified`, `not meaningful`, `stale`, or `unavailable` when needed.
25. Assign an Overall Risk Level only when evidence is sufficient. Allowed labels: Low, Moderate, High, Critical. Overall Risk Level is a risk-specific research label, not an investment recommendation.
26. Apply Setup Classification only when the user asks or the output explicitly includes a setup view beyond risk level.
27. Apply broader scoring only if the user asks or the output explicitly includes setup evaluation. Do not produce a Global Research Score by default.
28. Produce output using `skills/stock-analysis/risk/OUTPUT.md` and `rules/OUTPUT.md`.
29. For normal `!risk [ticker/company]`, produce the full Standard-only report in the final response. Do not collapse it into a compact summary, completion summary, verification section, or eval checklist.
30. Follow the global command-generated artifact save-order rule in `rules/ARTIFACTS.md` before writing `risk.md`.
31. Before saving the normal risk artifact, run the `!risk`-specific validation checks in `OUTPUT.md`. Hard-stop and do not save or claim a save if required sections, guardrails, source support, risk discipline, or the canonical `workspace/tickers/[ticker]/risk.md` path fail validation.
32. Save only the final clean Markdown report to `workspace/tickers/[ticker]/risk.md`.
33. Before finalizing Best Next Command, perform a workspace-aware routing check for same-ticker canonical artifacts using path existence and header/source-period freshness only. Do not edit artifacts during this routing check, and do not deep-parse existing artifacts unless they were already loaded for risk analysis.
34. Preserve issue-driven logic first: identify whether the risk review naturally points to business-model research, financial-statement work, thesis construction/update, earnings update, or full packet integration.
35. Apply artifact state as a routing guardrail: avoid recommending a repeat command when the relevant same-ticker artifact already exists and appears current enough by header/source-period review.
36. Recommend completing the remaining core artifacts only when packet completion is useful or when the user explicitly wants the complete Midas packet.
37. Before final response, perform a ticker-consistency finalization check: requested ticker/company, resolved issuer, report title, artifact path, saved-path line, and source state must all match the current command.
38. End normal responses with exactly one saved-path confirmation as the final line after successful artifact write verification under `ARTIFACTS.md`.

Keep this command focused on company risk assessment.

---

## No-Write Audit Rule

`!risk [ticker] -audit` is the only alternate mode.

Audit mode must not:

- Write `workspace/tickers/[ticker]/risk.md`.
- Write `workspace/tickers/[ticker]/risk.compact.md`.
- Create ticker folders.
- Create artifacts.
- Update indexes.
- Mutate watchlists.
- Auto-run downstream commands.
- Create schemas.
- Create proof packets.
- Create source manifests.
- Create evidence ledgers.
- Create fixture files.
- Claim `Saved to:`.

Audit mode may:

- Resolve ticker/company in memory.
- Retrieve or read sources in memory.
- Inspect existing artifact status read-only.
- Summarize source/filing basis.
- Summarize risk-category coverage.
- Summarize missing evidence.
- Summarize source limitations.
- Summarize output safety.
- Summarize artifact status.
- Recommend a next step.

Audit mode should use the audit output contract in `OUTPUT.md`.

If no-write cannot be guaranteed, stop before source gathering and return:

```md
Audit Result: Blocked

Could not guarantee no-write behavior for !risk [ticker] -audit, so source gathering was not started.

Would have checked:
- source basis
- risk-category coverage
- missing disclosures
- source limitations
- output safety
- artifact status

Required before audit can run:
- patch SKILL.md and OUTPUT.md to make -audit override all artifact, compact artifact, index, watchlist, manifest, ledger, proof-packet, schema, fixture, and downstream-command writes.

No files changed — audit blocked.
```

---

## Command-Specific Source Needs

Default source standards come from:

`rules/SOURCES.md`

Command-specific source needs:

- For SEC filers, prefer the latest Form 10-K and latest Form 10-Q.
- Use recent 8-Ks, earnings releases, investor presentations, credit agreements, debt/covenant filings, acquisition filings, financing filings, legal/regulatory disclosures, or transcripts only when materially relevant to risk.
- For non-SEC filers, use annual reports, interim reports, exchange filings, regulator filings, and official company disclosures.
- Use secondary sources only for context, not as primary proof of company-specific risk.
- Every material risk claim should be source-backed.
- Use line citations when available; otherwise cite filing name, filing date, period, section/table, or source basis when available.
- Keep accession numbers and URLs available internally; display them in normal output only when needed for disambiguation, source recovery, audit, debug context, or user-requested source links.
- If a risk is possible but not disclosed or supported, say so rather than presenting it as company-specific fact.
- Include source freshness, missing disclosures, and source limitations in Source Notes.

---

## Classification / Scoring / Metrics Behavior

### Setup Classification

Use Setup Classification: `Optional`

Rule:

`rules/CLASSIFICATIONS.md`

Command-specific classification notes:

- Do not classify by default.
- Overall Risk Level is not the same as Setup Classification.
- Use Setup Classification only when the output includes a setup view beyond risk level or the user explicitly asks for classification.
- Do not force classification into a raw risk assessment.
- Do not create new classification labels.

### Scoring

Use scoring: `Optional`

Rule:

`rules/SCORING.md`

Command-specific scoring notes:

- Do not create a new risk scoring formula.
- Do not produce a Global Research Score by default.
- Overall Risk Level may appear when evidence is sufficient, but it is a risk-specific research label and not an investment recommendation.
- If broader scoring is requested, risk findings may inform the Risk / Fragility / Downside Protection pillar and any score caps/gates under `SCORING.md`.
- If evidence is insufficient, withhold precise scoring/rating language or state that evidence is insufficient.
- If the user wants the complete scored packet, suggest completing `!research`, `!financials`, and `!thesis`.

### Metrics

Use financial and operating metrics: `Required` when available and material to risk.

Rule:

`rules/METRICS.md`

Command-specific metric notes:

- Use risk-relevant metrics when available and material.
- Displayed metrics should preserve period, source, unit, and GAAP/non-GAAP status when relevant.
- If a metric is not meaningful, stale, unavailable, or not calculable, say so.
- Do not use undefined metrics.
- Do not turn `!risk` into a financial statement review; redirect or recommend `!financials` when the user needs full financial analysis.
- Do not create price targets or unsupported valuation conclusions.
- Do not create red/yellow/green systems unless already explicitly supported by global rules.

---

## Output Contract

Follow the command-specific output contract:

`skills/stock-analysis/risk/OUTPUT.md`

Follow shared output standards:

`rules/OUTPUT.md`

### Required Sections in Normal Standard-Only Output

Normal `!risk [ticker/company]` must use the mandatory Standard-only template in `OUTPUT.md` as the source of truth. The required section order is:

1. Report title: `# ⚖️ [Display Name] ($[TICKER]) | Risk Assessment`
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
15. Final saved-path confirmation line: `Saved to: workspace/tickers/[ticker]/risk.md`

No ticker may receive a custom abbreviated, compact-style, full-style, or deep-style structure.

### Optional Audit Output

Audit output shape remains in `skills/stock-analysis/risk/OUTPUT.md`. Audit routing and no-write behavior are defined in this `SKILL.md`.

---

## Artifact Behavior

This command writes artifacts: `Yes` for normal output.

Audit mode writes artifacts: `No`.

Follow:

`rules/ARTIFACTS.md`

### Creates / Replaces

Normal `!risk [ticker]` saves by default to:

- `workspace/tickers/[ticker]/risk.md`

Audit `!risk [ticker] -audit` writes nothing.

### Replace Behavior

- Normal output replaces the prior `risk.md` for the same normalized ticker unless the user explicitly asks to preserve versions.
- Do not save incomplete output as `risk.md`.
- Do not use legacy workspace-root ticker paths.
- Do not claim an artifact was saved unless the write actually succeeded.

### Command-Specific Rules

- Normalize ticker by removing a leading `$` and lowercasing the folder name.
- Create the ticker folder only when saving the normal artifact.
- Save only the completed final risk assessment, not drafts, scratch work, source extracts, source manifests, evidence ledgers, proof packets, schemas, fixture files, or incomplete analysis.
- Saved normal artifacts must include the required report title and `Introduction` section.
- Keep source visibility and source limitations intact.
- Normal user-facing responses must contain the full Standard-only report, not a compact summary, completion summary, verification section, or eval checklist.
- Normal user-facing responses should end with exactly one saved-path confirmation line after successful artifact write verification under `ARTIFACTS.md`.
- Do not include a separate `Artifact` section by default.
- Do not mutate watchlists while saving ticker research artifacts.
- Do not auto-run downstream commands.
- Do not save `risk.md` if the would-be artifact contains validation notes, eval/smoke-test language, missing required sections, unsupported risk claims, recommendation framing, or non-canonical artifact paths.
- Run the `OUTPUT.md` risk-specific validation gate before saving; do not save or claim a save if required risk sections, guardrails, source support, risk discipline, or the canonical `workspace/tickers/[ticker]/risk.md` path fail validation.

---

## Runtime / Work Budget Rule

`!risk` must be bounded.

- Normal output should produce a complete but concise risk assessment using the mandatory Standard-only template in `OUTPUT.md`.
- Use targeted filing sections and notes rather than parsing or dumping entire filings.
- Prioritize risk factors, MD&A, liquidity/debt notes, legal proceedings, concentration disclosures, customer/segment/geography disclosures, share-count/dilution notes, subsequent events, material contracts, and relevant 8-Ks.
- Use `references/source-retrieval.md`, `references/risk-evidence.md`, `references/risk-metrics.md`, and `references/output-safety.md` when command-local retrieval, evidence, metric, or output-safety support is useful.
- For fintech, brokerage, crypto, payments, credit, or other market-sensitive financial platforms, check revenue mix, counterparty concentration, customer/platform asset metrics, credit-loss provisions, custody exposure, legal/regulatory accruals, rate sensitivity, and liquidity before ranking risks when relevant.
- Do not dump long filing excerpts.
- Do not attempt unlimited line-number extraction.
- Do not keep retrying SEC/source requests indefinitely.
- If line citations are slow or unavailable, use filing name, filing date, period, section/table, and source basis.
- If data cannot be retrieved or interpreted cleanly, return a bounded partial result with source limitations or fail cleanly.

---

## State Isolation Rule

Each `!risk` invocation must be isolated to the current requested company/ticker.

- Treat the latest active user command as authoritative for ticker/company identity.
- Never let a previously verified artifact or previous ticker in the transcript override the current command.
- Do not include notes, partial progress, unresolved state, filing status, artifact status, or identity resolution from a previous interrupted run unless the user explicitly asks about that prior run.
- A saved artifact must contain only the final output for the current requested ticker/company.
- If current output contains unrelated prior-run text, do not save it as final.
- If the transcript includes multiple tickers or context compaction/handoff, explicitly verify title/path/saved line consistency before finalizing.

---

## Failure Behavior

If information is missing, weak, stale, unavailable, or ambiguous:

- Say what is missing.
- State the limitation clearly.
- Do not invent facts.
- Do not invent numbers.
- Do not force a risk conclusion.
- Do not exaggerate unsupported risks.
- Provide the best partial result when possible.
- Suggest the best next diligence step when useful.
- Do not save incomplete output as `risk.md`.

Useful phrases:

```md
Unable to complete:
```

```md
Source limitation:
```

```md
Could not verify:
```

```md
Not disclosed in the reviewed filings:
```

```md
Risk not assessed:
```

```md
Best next step:
```

---

## Guardrails

This command must not:

- Use Buy/Hold/Sell recommendation language.
- Produce a price target.
- Provide position sizing, trade timing, or execution advice.
- Present a valuation model by default.
- Present cheap/expensive/fair-value conclusions by default.
- Turn risk level into an investment recommendation.
- Treat standard boilerplate risk factors as thesis-breaking without company-specific evidence.
- Exaggerate unsupported risks.
- Hide material risks.
- Present unverified claims as facts.
- Treat social media as risk proof.
- Treat management optimism as risk reduction without reported evidence.
- Present stale market data as current.
- Invent unavailable or unsupported metrics.
- Drift into `!research`, `!financials`, `!thesis`, `!earnings`, or `!gems`.
- Use market data as proof of business-model risk, revenue risk, margin risk, cash-flow risk, filing-derived debt/liquidity risk, filing-derived dilution risk, customer concentration, supplier concentration, regulatory/legal risk, or management execution risk.
- Treat price action as proof that a filing-backed risk is real or thesis-breaking.
- Treat price action, market data, or narrative momentum as proof of business quality, financial quality, customer demand, revenue, margins, cash flow, or thesis validity.
- Assess technical chart setup, entries, exits, support/resistance, breakouts, trendlines, moving averages, or trade timing unless a future chart / technical-analysis layer is explicitly built and integrated.
- Call or parse `!market` user-facing output text.
- Add provider fallback logic outside `tools/market_data_snapshot.py`.
- Hide provider/as-of/limitation details when market data is used.
- Duplicate global rules inside this skill.

### Guardrail-Style Response Language

When the user asks whether to buy, sell, hold, size a position, or requests a price target after a `!risk` review:

- Reframe as risk research only.
- State that `!risk` can assess company-specific fragility, downside drivers, and warning signs, but cannot provide buy/sell/hold instructions, position sizing, or price targets.
- Keep the useful risk read-through.
- Prefer `What prevents the risk view from being decisive by itself:` over personal-decision wording.
- Prefer `Best next research command:` over `Best next diligence before any decision:`.

---

## Eval Cases Needed

Eval coverage lives in:

`evals/risk.eval.md`

The eval file still needs later lean alignment after this Stage 2 patch. Future eval coverage should focus on:

1. Normal Standard-only success.
2. Missing/weak source handling.
3. Clean failure and no recommendation or price target.
4. Registry metadata match.
5. Source discipline.
6. Metric discipline when risk metrics appear.
7. Classification/scoring optionality when used.
8. Artifact path and false-save prevention.
9. Prompt-injection safety.
10. Unsupported compact-style handling.
11. Unsupported full/deep-style handling and routing.
12. `-audit` no-write behavior.
13. State isolation and ticker consistency.
14. Workspace-aware Best Next Command routing.

Do not add fixtures, schemas, proof packets, source manifests, evidence ledgers, or giant golden outputs by default.

## Stability Checklist

Before this command is considered Active, confirm:

- Purpose is clear.
- Trigger syntax is clear.
- Required inputs are clear.
- Parser behavior defines normal and `-audit` only.
- Workflow is command-specific.
- Global rules are referenced, not duplicated.
- Output contract exists and matches this file.
- Artifact behavior follows `rules/ARTIFACTS.md`.
- Failure behavior is defined.
- Guardrails are included.
- Evals exist and are aligned in a later stage.
- Command registry metadata is filled in.
- `docs/COMMAND_REGISTRY.md` matches this metadata in a later registry-alignment stage if needed.
- Normal Standard-only output passes.
- `-audit` no-write behavior passes.
- Unsupported compact/full/deep behavior passes.
- Artifact behavior is verified.
- Source discipline passes on more than one normal ticker.
- The command does not conflict with `!research`, `!financials`, `!thesis`, `!earnings`, or `!gems`.

## Final Rule

`!risk` should make downside diligence clearer, faster, and more disciplined. It should identify what can break the thesis, what warning signs matter, and what evidence would reduce risk, without becoming a recommendation or a full research packet.
