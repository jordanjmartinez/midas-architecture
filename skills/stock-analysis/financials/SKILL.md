---
name: financials
description: Use when the user invokes !financials [company name or ticker] to produce a filing-backed financial statement and metric-quality review.
version: 2.0.0
author: Midas / Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [stocks, equity-research, sec-filings, financial-analysis, metric-quality]
    related_skills: [research, thesis, risk, full]
---

# MIDAS Command Skill — !financials

## Command

`!financials`

## Registry Metadata

Command: `!financials`
Aliases: `None`
Category: `Financial Analysis`
Status: `Active`
Skill Path: `skills/stock-analysis/financials/SKILL.md`
Output Path: `skills/stock-analysis/financials/OUTPUT.md`
Eval File: `evals/financials.eval.md`
Uses Classification: `Optional`
Uses Scoring: `Optional`
Uses Metrics: `Required`
Writes Artifacts: `Yes`
Primary Global Rules: `GLOBAL.md, COMMAND_INTERFACE.md, SOURCES.md, MARKET_DATA.md, METRICS.md, OUTPUT.md, ARTIFACTS.md, CLASSIFICATIONS.md, SCORING.md`

## Purpose

`!financials` reviews a public company’s financial statements and metric quality. It helps the user understand revenue trends, margins, profitability, cash generation, balance-sheet strength, dilution, capital returns, GAAP/non-GAAP quality, segment financials, financial red flags, and the best next diligence command.

This command is a filing-backed financial-statement review, not a full business-model report, thesis, downside-only risk memo, full MIDAS packet, hidden-gem ranking, price target, or buy/sell recommendation.

---

## When To Use

Use this command when:

- The user invokes `!financials [company or ticker]`.
- The user asks for a company’s financial statements, margins, cash flow, FCF, balance sheet, debt, liquidity, dilution, capital returns, or metric quality.
- The user needs financial-statement diligence before `!thesis` or `!risk`.

Do not use this command when:

- The user wants a full business-model report. Use `!research`.
- The user wants bull/base/bear cases or a thesis debate. Use `!thesis`.
- The user wants a downside-only pressure test. Use `!risk`.
- The user wants a complete MIDAS packet. Recommend completing `!research`, `!thesis`, and `!risk`.
- The user wants hidden-gem discovery or ranking. Use `!gems`.
- The user asks for buy/sell/hold instructions, position sizing, or a price target. Reframe as financial-quality research.

---

## Inputs

### Required Inputs

- Company name or ticker.

### Optional Inputs

- Specific period, filing, segment, metric focus, source preference, or financial-statement focus.
- Limited valuation or current-market context if explicitly requested or materially needed to frame financial scale.
- Request to classify or score the setup.
- Optional audit flag: `-audit`.

Normal `!financials [ticker]` always produces the one Standard filing-backed financial-statement and metric-quality report.

`-audit` is the only alternate mode.

### Input Clarification Rules

Ask for clarification only when missing or ambiguous identity would materially change the result. If a ticker or company name is ambiguous, resolve the legal company name, ticker, exchange, and SEC CIK where applicable; if multiple plausible matches remain, ask the user to clarify before analysis.

---

## Aliases

Command aliases: `None`

---

## Output Modes / Parser Behavior

Normal routing:

- `!financials [ticker]` → produce the one Standard filing-backed financial-statement and metric-quality report.
- `!financials [ticker] -audit` → run no-write audit mode.

Audit flag:

- Single-dash `-audit` is canonical.
- If the user uses `--audit`, return this short correction and do not run the command:

```md
Use -audit for !financials audit mode.
```

Former Compact-style words such as `compact`, `quick`, `brief`, `short`, `concise`, and `summary` are not output modes for `!financials`.

- Treat them as style hints only when compatible with the Standard report.
- If the request conflicts with required Standard output, use this boundary message:

```md
!financials now uses one Standard filing-backed financial-statement and metric-quality report. I can keep the sections concise, but the command still preserves metric labels, source visibility, and saves the canonical financials artifact.
```

Former Full/Deep-style words such as `full`, `deep`, `detailed`, `expanded`, `deep-dive`, and `deepdive` are not output modes for `!financials`.

- If the request asks for a complete packet, recommend completing `!research [ticker]`, `!thesis [ticker]`, and `!risk [ticker]`.
- If the request asks for thesis work, recommend `!thesis [ticker]`.
- If the request asks for downside or thesis-breaking risk, recommend `!risk [ticker]`.
- If the request asks for business-model research, recommend `!research [ticker]`.
- If the request asks for latest-quarter or earnings update work, recommend `!earnings [ticker]`.
- If the request asks for a specific financial metric, period, filing, segment, or financial-statement focus, keep it inside normal `!financials`.

Do not auto-run downstream commands.

## Command References

- `references/source-acquisition.md` — SEC/EDGAR, Company Facts/XBRL, filing HTML, earnings-release/reconciliation source handling, and audit no-write caveat.
- `references/metric-quality.md` — command-local metric-quality checks that defer formulas to METRICS.md.
- `references/non-sec-and-fpi.md` — non-SEC/FPI, 20-F/6-K/local-report handling, currency/reporting-standard limitations, and non-U.S. disclosure caveats.
- `references/sector-financial-edge-cases.md` — compact reusable financial-statement edge cases for sector-specific financial-quality review.
- `references/artifact-safety.md` — normal artifact overwrite/readback safety, stale ticker/context reanchor, and audit no-write boundary.

---

## Global Rules

This command must follow:

- `rules/GLOBAL.md`
- `rules/COMMAND_INTERFACE.md`
- `rules/SOURCES.md`
- `rules/MARKET_DATA.md` only for optional market / valuation context
- `rules/METRICS.md`
- `rules/OUTPUT.md`
- `rules/ARTIFACTS.md`

Use when applicable:

- `rules/CLASSIFICATIONS.md`
- `rules/SCORING.md`

Do not duplicate global rule content inside this command. Reference global rules instead.

---

## Workflow

Follow this command-specific workflow:

1. Parse the request and identify the target company or ticker.
2. Determine whether the request is normal `!financials [ticker]` or no-write audit mode `!financials [ticker] -audit`.
3. If the request uses `--audit`, return `Use -audit for !financials audit mode.` and stop.
4. Confirm the active requested ticker/company is the latest real user command target after any context-compaction or reference-only block; do not inherit ticker, artifact path, todo status, tool output, verification state, final-summary draft, or prior skill-maintenance summaries from interrupted/compacted runs. If the transcript contains recent skill-library edits, regression-patch chatter, stale tool/todo state for another ticker, or a saved-path/title mismatch, use `references/artifact-safety.md` before drafting the user-facing response. If the immediately preceding work was command maintenance, eval/contract cleanup, artifact-format verification, or another non-report task, and the user says only `continue`, do not silently resume an older `!financials [ticker]` report; continue the visible active todo/maintenance thread when available, or ask a brief clarification if the intended continuation is materially ambiguous.
5. Resolve the company identity: legal company name, ticker, exchange, and SEC CIK where applicable. If no SEC CIK resolves or the issuer is primarily non-U.S./OTC-linked, use `references/non-sec-and-fpi.md` before gathering documents.
6. Determine whether the command has enough input to proceed; clarify only if ambiguity remains material.
7. For no-write audit mode, follow the No-Write Audit Rule below before any source gathering.
8. Gather source evidence using `rules/SOURCES.md` and the command-specific source needs below.
9. Identify the latest relevant annual and interim financial sources.
10. Record filing dates, report periods, source identifiers, and source basis; keep URLs or accessions internal unless needed for disambiguation, audit/source-recovery/debug context, or user-requested source links.
11. Extract targeted financial evidence rather than dumping full filings.
12. Review revenue trends and disclosed drivers.
13. Review margins and profitability, including gross margin, operating margin, net margin, and net income where meaningful.
14. Review operating cash flow and free cash flow; state the FCF definition used.
15. Review balance sheet, cash, debt, liquidity, solvency risk, maturities, and covenants where disclosed.
16. Review share count, dilution, buybacks, dividends, and whether capital returns appear covered by earnings or cash flow.
17. Review segment financials when disclosed.
18. Review GAAP vs non-GAAP metrics, reconciliations, changes in definitions, and metric quality.
19. Identify financial risks/watchpoints separately from source, citation, missing-data, stale-data, and unavailable-metric limitations.
20. Label all material metrics with period, source, unit, GAAP/non-GAAP status where applicable, and reported/adjusted/calculated status where applicable.
21. Label missing, not disclosed, stale, unavailable, or not meaningful metrics.
22. Include limited market / valuation context only if the user asks for valuation or current market context, or market cap / EV / liquidity is materially needed to frame financial scale. Interpret scale framing narrowly; do not use it to justify default market-data fetching in every Standard report. If market data is used, follow `rules/OUTPUT.md` `Market-Data Display Rule` for chat display and `rules/MARKET_DATA.md` for helper/source behavior. Call the canonical helper directly, keep the financial/valuation read-through first, show one compact provider/date line in chat, and preserve exact timestamp/timezone, provider limitations, unavailable fields, helper/tool detail if useful, and timing mismatch in the saved artifact when needed. Do not call or parse `!market` user-facing output text.
23. Apply Setup Classification only if the user asks or the output explicitly includes a final setup view.
24. Include the required `## Financial Quality Score` as a concise financial-quality research score/grade when evidence supports it. This is not a full Global Research Score and must not become a recommendation; if evidence is insufficient, state the limitation inside that section.
25. Produce output using `skills/stock-analysis/financials/OUTPUT.md` and `rules/OUTPUT.md`. In normal mode, use the mandatory Standard-only template in `OUTPUT.md`; do not invent a ticker-specific abbreviated structure.
26. Save the final clean report to `workspace/tickers/[ticker]/financials.md` for normal `!financials [ticker]` only, according to this command’s artifact behavior and `rules/ARTIFACTS.md`.
27. Before saving or sending normal output, run a ticker-consistency finalization check. The active user ticker/company, resolved issuer, report title, artifact path, saved-path line, and source base must all match. If multiple tickers appeared in the transcript or context was compacted/interrupted, use `references/artifact-safety.md`. If any element does not match, hard stop and regenerate for the active ticker from sources; do not patch only the title/path.
28. If a best next command is useful, include it as `## Best Next Command` after `## Source Notes` and before the final saved-path line. If `workspace/tickers/[ticker]/research.md` exists, prefer `!thesis [TICKER]` or `!risk [TICKER]` depending on the financial issues surfaced, and if no research artifact exists, suggest `!research [TICKER]`.
29. End normal successful responses with the required saved-path confirmation only after the artifact was actually written.

---

## No-Write Audit Rule

`!financials [ticker] -audit` is the only alternate mode.

Audit mode must not:

- write `workspace/tickers/[ticker]/financials.md`
- write `workspace/tickers/[ticker]/financials.compact.md`
- create ticker folders
- create artifacts
- update indexes
- mutate watchlists
- auto-run downstream commands
- create schemas
- create proof packets
- create source manifests
- create evidence ledgers
- create fixture files
- claim `Saved to:`

Audit mode may:

- resolve ticker/company in memory
- retrieve/read sources in memory
- inspect existing artifact status read-only
- summarize source/filing basis
- summarize financial-statement coverage
- summarize metric coverage
- summarize missing evidence
- summarize source limitations
- summarize output safety
- summarize artifact status
- recommend next step

If no-write cannot be guaranteed, stop before source gathering and return:

```md
Audit Result: Blocked

Could not guarantee no-write behavior for !financials [ticker] -audit, so source gathering was not started.

Would have checked:
- source basis
- financial-statement coverage
- metric coverage
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
- Use earnings releases, Form 8-Ks, investor presentations, transcripts, or company reconciliations when needed for current financial tables or non-GAAP reconciliation.
- For non-SEC filers, use annual reports, interim reports, exchange filings, regulatory filings, and official company financial disclosures.
- Use secondary sources only for context, not as primary proof of financial metrics.
- Use market data only if valuation/current market context is requested, or market cap / EV / liquidity is materially needed to frame financial scale. Interpret scale framing narrowly; do not use it to justify default market-data fetching in every normal Standard report.
- Do not show valuation multiples without provider/source, as-of context, source context, clean denominators, and any material timing mismatch between live market data and filing-derived inputs.
- Every material financial claim should be source-backed.
- Use line citations when available; otherwise cite filing name, filing date, period, section/table, accession number, or URL when available.

Command-local support references:

- `references/source-acquisition.md` for SEC/EDGAR, Company Facts/XBRL, filing HTML, earnings-release/reconciliation source handling, source traceability, and audit no-write caveats.
- `references/non-sec-and-fpi.md` for non-SEC issuers, FPIs, 20-F/6-K/local-report handling, currency/reporting-standard limitations, and non-U.S. disclosure caveats.
- `references/sector-financial-edge-cases.md` for compact sector-specific financial-statement edge cases.
- `references/metric-quality.md` for command-local metric-quality checks that defer formulas to METRICS.md.
- `references/artifact-safety.md` for normal artifact overwrite/readback safety, stale ticker/context reanchor, and audit no-write boundary.

---

## Market Data Usage

`!financials` remains filing-backed by default.

Market data is optional supporting context. Use it under:

`rules/MARKET_DATA.md`

When market context is needed, call the canonical helper directly:

```bash
python3 tools/market_data_snapshot.py [TICKER]
```

Do not call or parse `!market` user-facing output text.

Allowed uses:

- User asks for valuation or current market context.
- Market cap, enterprise value, or liquidity is materially needed to frame financial scale. Interpret this narrowly; do not use it to justify default market-data fetching in every normal Standard report.

Default normal mode:

- Do not include a live market-data block by default.
- Do not fetch live market data solely because the command is running Standard mode.
- Filing-backed financial-statement review must remain complete without live market data unless the user requested market context or a specific, material scale/valuation framing requires it.

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

If market data is used in chat, label compactly under `rules/OUTPUT.md` `Market-Data Display Rule`:

- provider/source;
- concise as-of date.

Preserve exact timestamp, timezone, limitations, unavailable fields, helper/tool detail if useful, and timing mismatch between live market data and filing-derived inputs in the saved artifact when needed.

Valuation multiples must follow `rules/METRICS.md`.

Do not produce:

- Buy/Sell/Hold language;
- price targets;
- position sizing;
- entry/exit guidance;
- trade advice;
- default PEG;
- unsupported cheap/expensive/reasonable/fair-value conclusions.

---

## Classification / Scoring / Metrics Behavior

### Setup Classification

Use Setup Classification: `Optional`

Rule:

`rules/CLASSIFICATIONS.md`

Command-specific classification notes:

- Do not classify by default.
- Use Setup Classification only when the output includes a final setup view or the user explicitly asks for classification.
- Do not force classification into a raw financial statement review.

### Scoring

Use scoring: `Optional`

Rule:

`rules/SCORING.md`

Command-specific scoring notes:

- Normal output requires a concise `## Financial Quality Score` section as defined in `OUTPUT.md`; treat it as a financial-quality research prioritization score/grade, not as a full Global Research Score or recommendation.
- Score-line formatting is output-only: use `[score]/10 - [Assessment]`, preserving the generated score and assessment without hardcoding scores, adding a new rubric, or changing scoring logic.
- Do not add broader setup scoring, Global Research Score, overlays, or ranking by default.
- Use broader scoring only if the user asks for scoring or if the command explicitly produces a financial-quality setup view.
- If the user wants a full Global Research Score, apply it per `rules/SCORING.md` on explicit request.
- If evidence is insufficient, state the limitation rather than inventing precision.

### Metrics

Use financial metrics: `Required`

Rule:

`rules/METRICS.md`

Command-specific metric notes:

- Follow `METRICS.md`; do not redefine metric formulas locally except for pointing to `METRICS.md`, showing output-format examples, or defining FCF as CFO minus capex when using that convention.
- Displayed metrics should preserve metric name, period, currency, unit, filing/source period, and GAAP/non-GAAP status when relevant.
- Label reported vs adjusted status and actual vs estimated/guided status when applicable.
- If market data is used, label provider/source and as-of date.
- If a metric is not meaningful, stale, unavailable, not disclosed, or not calculable, say so.
- Do not use undefined metrics.
- Define FCF as cash flow from operations minus capital expenditures unless using a company-specific FCF definition; label company-defined FCF clearly.
- Separate GAAP and non-GAAP metrics.
- Check non-GAAP reconciliation quality when available.
- Do not treat non-GAAP metrics as equivalent to GAAP.
- Flag recurring, aggressive, changing, or poorly reconciled adjustments.
- If reconciliation is unavailable, say so.
- For brokerage, clearing, custody-heavy fintech, or similar balance-sheet-intensive financial companies, use `references/sector-financial-edge-cases.md` and `references/metric-quality.md`; caveat reported CFO/FCF when client, segregated-cash, securities-borrowed/loaned, or user-payable movements dominate cash flow.
- For software-heavy fintechs where separately disclosed, subtract both purchases of property/software/equipment and capitalization of internally developed software from CFO for a conservative filing-based FCF view; if not separately available, state the limitation.
- Do not calculate FCF CAGR when FCF crosses zero, is negative, or is not meaningful; explain the trend instead.
- Label ROE and ROA denominator basis.
- Label interest coverage basis.
- Do not include PEG as a default metric.
- Do not include default cheap/expensive/reasonable/fair-value valuation language.
- Do not present unsupported multiple conclusions.
- Market-data-derived valuation metrics must follow `MARKET_DATA.md` and `METRICS.md`, and must remain separate from filing-backed financial-statement conclusions.

---

## Output Contract

Follow the command-specific output contract:

`skills/stock-analysis/financials/OUTPUT.md`

Follow shared output standards:

`rules/OUTPUT.md`

### Required Sections in Normal Standard-Only Output

Normal `!financials [ticker]` must use the mandatory Standard-only template in `OUTPUT.md` as the source of truth. The required section order is:

1. Report title: `# 🪙 [TICKER] | [Company Name] Financial Analysis`
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
17. Final saved-path confirmation line: `Saved to: workspace/tickers/[ticker]/financials.md`

In normal output, the saved-path confirmation must appear exactly once and be the final line of the user-facing response. If a next command is included, use a separate `## Best Next Command` section after `## Source Notes` and before the final saved-path line, then a blank line, then command-first body format: `` `!command TICKER` — Reason. `` Keep financial risks/watchpoints inside `## Financial Risks`, not buried in `## Source Notes` by default.

Before finalizing normal `!financials` output:

- Confirm the required Standard-only sections appear in order.
- Confirm `## Source Notes` appears after `## What To Verify Next` and before `## Best Next Command` when useful.
- Confirm source dates, periods, source basis, freshness, missing disclosures, source limitations, and calculated-metric labels are visible in `## Source Notes`.
- Confirm every material metric is labeled with period, source, unit, and GAAP/non-GAAP status when relevant.
- Confirm `## Financial Quality Score` uses `[score]/10 - [Assessment]`, or states why evidence is insufficient.
- Confirm `## Financial Risks` contains the main financial red flags/watchpoints.
- Confirm every required heading is followed by a blank line before body text.
- Confirm Best Next Command, when included, uses `## Best Next Command`, then a blank line, then `` `!command TICKER` — Reason. ``
- Confirm the reason after the dash starts with a capital letter.
- Confirm the saved-path line appears exactly once and is the final line.
- Confirm normal output does not add live market data by default.
- Confirm normal output does not use Compact, Full, or Deep mode behavior.

No ticker may receive a custom abbreviated, compact-style, full-style, or deep-style structure.

### Optional Audit Output

Audit output shape remains in `skills/stock-analysis/financials/OUTPUT.md`. Audit routing and no-write behavior are defined in this `SKILL.md`.

---

## Artifact Behavior

This command writes artifacts only in normal mode: `Yes`

Audit mode writes artifacts: `No`

Follow:

`rules/ARTIFACTS.md`

### Creates / Replaces

Normal `!financials [ticker]` saves by default to:

- `workspace/tickers/[ticker]/financials.md`

Audit `!financials [ticker] -audit` writes nothing.

### Replace Behavior

- Normal outputs replace the prior `financials.md` for the same normalized ticker unless the user explicitly asks to preserve versions.
- Before overwriting `workspace/tickers/[ticker]/financials.md` in an interrupted, compacted, or multi-agent session, read or otherwise verify the current target path enough to avoid stale/sibling-agent clobbering; after saving, re-read/verify title, ticker, required sections, score line, source base, and saved-path confirmation.
- If the target artifact was only read with pagination / partial view before overwrite, treat any write-tool warning as a stale-state signal: after saving, re-read or programmatically verify the full saved artifact before claiming completion. Do not rely on the partial pre-read as sufficient finalization evidence.
- If a write tool warns that the target artifact was modified by a sibling subagent or was never read by the current agent, treat that as a finalization risk: immediately verify the saved file before telling the user it was completed.
- Save only the final clean Markdown report after analysis is complete and verified.
- Do not save incomplete output as `financials.md`.
- Do not use legacy workspace-root ticker paths.
- Do not claim an artifact was saved unless the write actually succeeded.
- Do not mutate watchlists while saving financials artifacts.
- Do not auto-run downstream commands.
- Do not include a separate Artifact section by default.
- End normal successful responses with exactly one saved-path confirmation line only after the artifact was actually written:

```md
Saved to: workspace/tickers/[ticker]/financials.md
```

---

## Runtime / Work Budget Rule

`!financials` must be bounded.

- Normal mode should produce a complete but concise financial review using the mandatory Standard-only template in `OUTPUT.md`; it must not collapse into former Compact behavior for any ticker, including `NOW`.
- Use targeted financial statements and notes rather than parsing entire filings when possible.
- For newly public or fiscal-year software companies, explicitly verify whether a newer 10-Q exists before assuming one; if the latest available realized results are a 10-K plus an earnings-release 8-K exhibit, say so and separate company guidance from filed results.
- Prioritize income statement, balance sheet, cash flow statement, segment tables, share-count footnotes, debt/liquidity footnotes, non-GAAP reconciliations, and MD&A financial drivers.
- Do not dump long filing excerpts.
- Do not attempt unlimited line-number extraction.
- Do not keep retrying SEC/source requests indefinitely.
- If line citations are slow or unavailable, use filing name, filing date, period, section/table, accession number, and URL.
- If data cannot be retrieved or calculated cleanly, return a bounded partial result with source limitations or fail cleanly.

---

## State Isolation Rule

Each `!financials` invocation must be isolated to the current requested company/ticker.

- Treat the latest active user command as authoritative for ticker/company identity; never let a previously verified artifact or previous ticker in the transcript override it.
- Do not include notes, partial progress, unresolved state, filing status, artifact status, or identity resolution from a previous interrupted run unless the user explicitly asks about that prior run.
- A saved artifact must contain only the final output for the current requested ticker/company.
- If current output contains unrelated prior-run text, do not save it as final.
- If the transcript includes multiple tickers or context compaction/handoff, explicitly verify title/path/saved line consistency before finalizing.

---

## Failure Behavior

If information is missing, weak, stale, or unavailable:

- Say what is missing.
- State the limitation clearly.
- Do not invent facts.
- Do not invent numbers.
- Do not force a metric or conclusion.
- Provide the best partial result when possible.
- Suggest the best next diligence step when useful.
- Do not save incomplete output as `financials.md`.

---

## Guardrails

This command must not:

- Use Buy/Hold/Sell recommendation language.
- Produce a price target.
- Present a full valuation model by default.
- Use default cheap/expensive/reasonable/fair-value valuation language.
- Use PEG by default.
- Treat non-GAAP metrics as GAAP.
- Present stale market data as current.
- Invent unavailable or unsupported metrics.
- Drift into `!research`, `!thesis`, `!risk`, or `!gems`.
- Duplicate global rules inside this skill.

### Guardrail-Style Response Language

When the user asks whether to buy, sell, hold, size a position, or requests a price target after a `!financials` review:

- Reframe as financial-quality research only; do not advise a personal investment decision.
- State that `!financials` can assess financial quality, metric quality, and information gaps, but cannot provide buy/sell/hold instructions, position sizing, or price targets.
- Prefer `What prevents the financials from being decisive by themselves:` over personal-decision wording such as `What stops me from calling...`.
- Prefer `Best next research command:` over `Best next diligence before any decision:`.
- Keep the useful financial read-through, but make clear that financials alone are not a complete investment decision.

Guardrail wording is governed by this section and the command output contract; do not route to a separate recommendation or price-target workflow.

---

## Eval Cases Needed

Eval coverage lives in:

`evals/financials.eval.md`

Required eval areas:

1. Normal Standard-only success
2. Missing/weak source handling
3. No recommendation or price target
4. Registry metadata match
5. Former Compact-style words handled as style hints or boundary prompts, not modes
6. Former Full/Deep-style words routed or bounded without mode drift
7. GAAP/non-GAAP labeling
8. FCF crossing zero / negative FCF handling
9. Stale market data handling
10. Artifact path and false-save prevention
11. Command boundary
12. Prompt-injection safety
13. Runtime boundedness
14. State isolation
15. Standard output contract regression, including required title, exact Standard-only section order, Metric Quality section, Financial Quality Score, Source Notes, Best Next Command formatting, and saved-path confirmation
16. Audit no-write behavior: `!financials [ticker] -audit` writes nothing, creates no artifacts or folders, does not claim `Saved to:`, and reports read-only audit status
17. Market-data boundary and no unsupported valuation conclusion

---

---

## Stability Checklist

Before this command is considered Active, confirm:

- Purpose is clear.
- Trigger syntax is clear.
- Required inputs are clear.
- Workflow is command-specific.
- Global rules are referenced, not duplicated.
- Output contract exists and matches this file.
- Artifact behavior follows `rules/ARTIFACTS.md`.
- Failure behavior is defined.
- Guardrails are included.
- Evals exist.
- Command registry metadata is filled in.
- `docs/COMMAND_REGISTRY.md` matches this metadata.
- The command does not conflict with other commands.

## Final Rule

`!financials` should make financial-statement diligence cleaner, faster, and more disciplined. It should surface metric quality, fragility, and information gaps without becoming a recommendation or a full research packet.
