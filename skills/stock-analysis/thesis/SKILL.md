---
name: thesis
description: Build or update a filing-backed long-term investment thesis for a public company or ticker. Use for !thesis [ticker/company], !thesis update [ticker/company], !thesis [ticker/company] -audit, !thesis update [ticker/company] -audit, /thesis [ticker/company], or natural-language thesis requests.
version: 2.1.0
author: Midas / Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [stocks, equity-research, sec-filings, investment-thesis, thesis-update]
    related_skills: [research, financials, risk, earnings, full]
---

# Midas Command Skill — !thesis

## Command References

- `references/source-and-evidence.md` — thesis-source retrieval, primary-source basis, workspace artifacts as secondary synthesis inputs, Source Notes discipline, and audit no-write source boundary.
- `references/thesis-evidence.md` — thesis pillars, facts vs interpretation, unproven assumptions, disconfirming evidence, thesis breakers, and no unsupported story-stock claims.
- `references/update-workflow.md` — living-thesis update mechanics, baseline requirement, same-file overwrite, local update labels, and update audit no-write boundary.
- `references/market-rerating.md` — conditional market / valuation / rerating context, provider/as-of labeling, no default market data, and METRICS.md / RERATING.md boundaries.
- `references/output-safety.md` — concise thesis output hygiene, no stale Full-mode structures, no false saved claims, canonical thesis.md behavior, and audit no-write boundary.

## Command

`!thesis`

## Registry Metadata

Command: `!thesis`
Aliases: `/thesis`, `thesis`
Category: `Thesis Analysis`
Status: `Draft`
Skill Path: `skills/stock-analysis/thesis/SKILL.md`
Output Path: `skills/stock-analysis/thesis/OUTPUT.md`
Eval File: `evals/thesis.eval.md`
Uses Classification: `Optional`
Uses Scoring: `Optional`
Uses Metrics: `Required`
Writes Artifacts: `Yes`
Primary Global Rules: `GLOBAL.md, COMMAND_INTERFACE.md, SOURCES.md, METRICS.md, MARKET_DATA.md, OUTPUT.md, ARTIFACTS.md, CLASSIFICATIONS.md, SCORING.md`

## Purpose

`!thesis` builds or updates a filing-backed long-term thesis for a public company. It synthesizes business evidence, financial support, variant view, catalysts, thesis-breaking risks, monitoring points, and source limitations into one durable living thesis artifact.

The command answers: what must be true for the company to become more valuable over a multi-year period, what evidence supports that possibility today, what remains unproven, what would validate the thesis, and what would break it.

This is a research workflow, not a buy/sell/hold recommendation, price target, position-sizing instruction, or trade plan.

---

## When To Use

Use this command when:

- The user invokes `!thesis [ticker/company]`, `/thesis [ticker/company]`, or `thesis [ticker/company]`.
- The user invokes `!thesis update [ticker/company]` to refresh an existing living thesis.
- The user invokes `!thesis [ticker/company] -audit` for a no-write new-thesis readiness audit.
- The user invokes `!thesis update [ticker/company] -audit` for a no-write update-readiness audit.
- The user asks for a long-term thesis, thesis pillars, variant view, catalysts, thesis breakers, what must be true, what to monitor, or update direction for a public company.
- The user wants synthesis after `!research`, `!financials`, and/or `!risk`.

Do not use this command when:

- The user wants only business-model research. Use or suggest `!research`.
- The user wants only financial-statement or metric-quality review. Use or suggest `!financials`.
- The user wants downside-only pressure testing. Use or suggest `!risk`.
- The user wants latest-quarter review. Use or suggest `!earnings`.
- The user wants a complete Midas packet with full scoring/classification. Suggest completing `!research`, `!financials`, and `!risk` so the four core artifacts form the packet.
- The user wants hidden-gem discovery or ranking. Use or suggest `!gems`.
- The user asks what to buy/sell/hold, asks for a price target, or asks for position sizing. Reframe as research only.

Do not auto-run downstream commands unless the user separately invokes them.

---

## Command Surface

### Supported Normal Commands

- `!thesis [ticker/company]`
- `!thesis update [ticker/company]`

### Supported Audit Commands

- `!thesis [ticker/company] -audit`
- `!thesis update [ticker/company] -audit`

### Unsupported as Formal Modes

- Compact
- Full
- Deep

`!thesis` is Standard-only for normal and update output. `update` is a subcommand / living-thesis workflow, not an output mode. `-audit` is no-write audit mode, not an output depth.

---

## Inputs

### Required Inputs

- Company name or ticker.

### Optional Inputs

- Subcommand/action: `update`.
- Audit flag: `-audit`.
- Specific thesis focus.
- Specific source, filing, transcript, investor presentation, acquisition filing, financing filing, or user-provided source.
- Specific thesis pillar.
- Catalysts focus.
- Variant view focus.
- Risks / thesis breakers focus.
- Update workflow via the `update` subcommand.
- Market / valuation / rerating context only when explicitly requested or materially needed.
- Version preservation only when explicitly requested.
- Setup Classification, scoring, or Evidence Confidence only when explicitly requested or when a setup view is included.

### Removed as Active Command Behavior

- Output depth: Compact, Standard, Full.
- Formal Compact mode.
- Formal Full mode.
- Deep mode.
- `thesis.compact.md` save behavior.
- Full-mode output behavior.
- Compact-mode output behavior.
- Mode-dependent artifact branching except audit no-write.

### Input Clarification Rules

Ask for clarification only when missing or ambiguous identity would materially change the result.

If a ticker or company name is ambiguous, resolve the legal company name, ticker, exchange, SEC CIK if applicable, and whether it is an SEC filer. If multiple plausible matches remain, ask the user to clarify before analysis.

If the company is clear enough to proceed, state the identity assumption and proceed.

---

## Parser / Routing Behavior

Mode routing and mode-conflict behavior inherit from:

`rules/COMMAND_INTERFACE.md`

Command-specific routing:

- `!thesis [ticker]` → normal Standard-only new thesis memo.
- `!thesis update [ticker]` → Standard-only living thesis refresh.
- `!thesis [ticker] -audit` → no-write new-thesis audit.
- `!thesis update [ticker] -audit` → no-write update audit.
- Single-dash `-audit` is canonical.
- If the user uses `--audit`, return this exact correction and stop:

```md
Use -audit for !thesis audit mode.
```

Parser safeguards:

- Treat `update` immediately after `!thesis`, `/thesis`, or `thesis` as the thesis-update subcommand, not as a ticker/company and not as an output mode.
- Treat the first ticker/company argument after the command or after `update` as the security identifier to resolve.
- Do not infer Compact, Full, or Deep mode from ticker symbol, company name, filing length, complexity, popularity, prior examples, or prior outputs.
- Do not treat `update` as an output mode.
- Do not auto-run downstream commands recommended as boundaries.

### Former Compact Words

Former compact words:

- `compact`
- `quick`
- `brief`
- `short`
- `concise`
- `summary`

Do not route these to Compact mode. Treat them as style hints only when compatible with the required Standard thesis memo. If the request conflicts with required Standard output, use this boundary:

```md
!thesis now uses one Standard filing-backed thesis memo. I can keep the sections concise, but the command still preserves thesis pillars, evidence, risks, monitoring points, source visibility, and saves the canonical thesis artifact.
```

### Former Full / Deep Words

Former full/deep words:

- `full`
- `deep`
- `detailed`
- `expanded`
- `deep-dive`
- `deepdive`

Do not route these to Full or Deep mode.

If the request asks for a complete packet, recommend completing the remaining core commands (`!research [ticker]`, `!financials [ticker]`, `!risk [ticker]`).

If the request asks for business model, recommend:

- `!research [ticker]`

If the request asks for financial statements or metric quality, recommend:

- `!financials [ticker]`

If the request asks for downside pressure testing, recommend:

- `!risk [ticker]`

If the request asks for latest-quarter earnings, recommend:

- `!earnings [ticker]`

If the request asks for a specific thesis component such as catalysts, thesis pillars, variant view, thesis breakers, what must be true, what to monitor, or update direction, keep it inside Standard `!thesis`.

Full/deep complete-packet boundary:

```md
!thesis is scoped to long-term thesis construction and living-thesis updates. Use !research [ticker] for business-model research, !financials [ticker] for financial-statement review, !risk [ticker] for downside pressure-testing, or !earnings [ticker] for latest-quarter earnings review.
```

---

## Aliases

Command aliases:

- `/thesis`
- `thesis`

Supported action:

- `update`

Supported flag:

- `-audit`

---

## Global Rules

This command must follow:

- `rules/GLOBAL.md`
- `rules/COMMAND_INTERFACE.md`
- `rules/SOURCES.md`
- `rules/METRICS.md` when metrics appear.
- `rules/MARKET_DATA.md` when market data is used.
- `rules/RERATING.md` when rerating, post-rerate, overextension, market-expectations, or valuation-setup language is used.
- `rules/OUTPUT.md`
- `rules/ARTIFACTS.md`

Use when applicable:

- `rules/CLASSIFICATIONS.md`
- `rules/SCORING.md`

Do not duplicate global rule content inside this command. Reference global rules instead.

---

## Normal New-Thesis Workflow

Use this workflow for:

`!thesis [ticker/company]`

1. Parse the user request and confirm the active target is the latest real user command target.
2. If resuming after context compaction, interruption, or stale tool/todo state, hard-reset command state from the latest user-visible command before doing any work.
3. Resolve company identity: legal company name, ticker, exchange, SEC CIK if applicable, and whether it is an SEC filer.
4. Determine whether the command has enough input to proceed. Clarify only if ambiguity remains material.
5. Gather source evidence using `rules/SOURCES.md` and the command-specific source needs below.
6. For SEC filers, identify the latest relevant annual and interim sources, usually latest Form 10-K and latest Form 10-Q when available. For non-SEC filers, identify closest primary-source equivalents.
7. Use material 8-Ks, earnings releases, investor presentations, acquisition filings, financing filings, transcripts, or other company sources only when material to thesis pillars, catalysts, risks, thesis breakers, update direction, valuation setup, or source freshness.
8. Review same-ticker workspace artifacts only when useful as secondary synthesis inputs:
   - `research.md`
   - `financials.md`
   - `risk.md`
   - `earnings.md`
   - `updates.md`
   - `full.md`
9. Treat workspace artifacts as secondary synthesis inputs only. Primary filings and official disclosures remain authoritative. Do not create missing workspace artifacts unless the user explicitly asks.
10. Separate reported facts, management claims, Midas interpretation, and unproven assumptions.
11. Separate current evidence from future assumptions.
12. Define the long-term thesis as a possibility, not a guaranteed outcome.
13. Identify what must be true for the thesis to work.
14. Identify what remains unproven.
15. Identify 3–6 thesis pillars when useful. For each pillar, state what must happen, evidence today, what remains unproven, and what to monitor.
16. Evaluate business evidence relevant to the thesis: business model, revenue mechanics, customers/end markets, recurrence/contract structure, customer/geographic concentration, pricing power, cyclicality, competitive position, and growth engine when material.
17. Evaluate financial support relevant to the thesis: revenue growth, margins, profitability, cash flow/FCF, cash/debt, capex needs, dilution/financing, and whether current financials support, weaken, or do not yet prove the thesis.
18. Include catalysts or milestones with timing only when disclosed or reasonably source-backed.
19. Include risks and thesis breakers.
20. Include disconfirming evidence when useful.
21. Include what to monitor and what to verify next.
22. Apply market / valuation / rerating context only under the boundary below.
23. Apply Setup Classification only when the user asks or when the output explicitly includes a setup view beyond thesis status.
24. Apply scoring only if the user asks or if the output explicitly includes setup evaluation. Do not produce a Global Research Score by default.
25. Produce output using `skills/stock-analysis/thesis/OUTPUT.md` and shared output rules.
26. Before writing, follow the global command-generated artifact save-order rule in `rules/ARTIFACTS.md`: draft internally, run required command-specific validation before first write, revise the draft if validation fails, save only after validation passes, verify the saved artifact, and show saved-path confirmation only after successful write.
27. Save the final clean Markdown only to `workspace/tickers/[ticker]/thesis.md`.
28. Before final response, perform a ticker-consistency finalization check: requested ticker/company, resolved issuer, report title, artifact path, saved-path line, source base, and action must all match the current command.
29. End with exactly one saved-path confirmation only after successful write.

Keep this command focused on thesis synthesis.

---

## Living Thesis Update Workflow

Use this workflow only when the user invokes:

`!thesis update [ticker/company]`

Update is a subcommand / living thesis workflow, not an output mode.

### 1. Load the current living thesis

Load the existing living thesis read-only first from:

`workspace/tickers/[ticker]/thesis.md`

If the file does not exist, stop and say:

```md
No baseline thesis exists yet for [ticker]. Run !thesis [ticker] first.
```

Do not build a new thesis from scratch during update mode unless the user changes the command to `!thesis [ticker]`.

### 2. Extract prior thesis structure

From the existing thesis, extract:

- prior thesis summary,
- thesis pillars,
- unproven assumptions,
- catalysts,
- monitoring points,
- risks and thesis breakers,
- what to verify next,
- source basis,
- prior thesis direction/status if available,
- prior generated or updated date, if available.

### 3. Review supporting artifacts and new evidence

Review available same-ticker artifacts when useful as secondary synthesis inputs only:

- `research.md`
- `financials.md`
- `risk.md`
- `earnings.md`
- `updates.md`
- `full.md`

Then retrieve or review new primary evidence since the prior thesis date when available:

- latest Form 10-Q,
- latest Form 10-K,
- material 8-Ks,
- earnings release if material,
- investor presentation if material,
- acquisition filing if material,
- financing/debt filing if material,
- transcript or other company source if material.

### 4. Compare new evidence to the living thesis

Separate:

- old thesis,
- new evidence,
- interpretation,
- unproven assumptions.

For the overall update direction, use exactly one local workflow label:

- `Strengthened`
- `Mostly Unchanged`
- `Weakened`
- `Under Review`
- `Broken`

For each thesis pillar, use exactly one local workflow label:

- `Strengthened`
- `Unchanged`
- `Weakened`
- `Not Yet Testable`
- `Broken`

Definitions:

- `Strengthened`: new reported evidence supports the pillar more than prior evidence did.
- `Unchanged`: new evidence does not materially change the pillar.
- `Weakened`: new evidence makes the pillar less supported, but not broken.
- `Not Yet Testable`: no new reported evidence directly tests the pillar.
- `Broken`: new evidence directly contradicts a required pillar or triggers a thesis-breaker.

Update direction labels and pillar status labels are local update workflow labels only. They are not Setup Classifications and must not become a second global classification system.

### 5. Produce a refreshed living thesis

The final output should be a clean updated thesis, not just a changelog.

Include `## Update Notes` near the top and then continue with the normal thesis structure.

### 6. Save the updated thesis

Overwrite only the same living thesis file after completing and validating the refreshed thesis:

`workspace/tickers/[ticker]/thesis.md`

Do not create:

- a new baseline when the baseline is missing,
- a separate `thesis-update.md`,
- timestamped thesis history by default,
- version files unless explicitly requested,
- a second thesis artifact,
- missing workspace artifacts,
- source manifest files,
- evidence ledger files,
- proof packets,
- schemas,
- fixture files.

Save only final clean Markdown and show saved-path confirmation only after successful write verification.

---

## No-Write Audit Rule

Use this rule for:

- `!thesis [ticker/company] -audit`
- `!thesis update [ticker/company] -audit`

`-audit` is no-write and overrides all artifact, compact artifact, update artifact, version, index, watchlist, manifest, ledger, proof-packet, schema, fixture, and downstream-command writes.

Audit mode must not:

- write `workspace/tickers/[ticker]/thesis.md`,
- write `workspace/tickers/[ticker]/thesis.compact.md`,
- write `workspace/tickers/[ticker]/thesis-update.md`,
- create timestamped thesis history,
- create version files,
- create ticker folders,
- create artifacts,
- update indexes,
- mutate watchlists,
- auto-run downstream commands,
- create schemas,
- create proof packets,
- create source manifests,
- create evidence ledgers,
- create fixture files,
- claim `Saved to:`.

Audit mode may:

- resolve ticker/company in memory,
- retrieve/read sources in memory,
- inspect existing `thesis.md` status read-only,
- inspect same-ticker workspace artifacts read-only,
- summarize source/filing basis,
- summarize existing thesis status,
- summarize thesis coverage,
- summarize update readiness when update audit is used,
- summarize missing evidence,
- summarize source limitations,
- summarize output safety,
- summarize artifact status,
- recommend next step.

New-thesis audit should follow the audit output contract in `OUTPUT.md` and write nothing.

Update audit must inspect existing `thesis.md` read-only when present. It must not overwrite `thesis.md`, create a baseline thesis if missing, create `thesis-update.md`, create timestamped history, or write anything. If no baseline exists, return Blocked or Partial and include:

```md
No baseline thesis exists yet for [ticker]. Run !thesis [ticker] first.
```

If no-write cannot be guaranteed, stop before source gathering and return:

```md
Audit Result: Blocked

Could not guarantee no-write behavior for !thesis [ticker] -audit, so source gathering was not started.

Would have checked:
- source basis
- existing thesis status, if any
- thesis coverage
- missing evidence
- source limitations
- output safety
- artifact status

Required before audit can run:
- patch SKILL.md and OUTPUT.md to make -audit override all artifact, compact artifact, update artifact, version, index, watchlist, manifest, ledger, proof-packet, schema, fixture, and downstream-command writes.

No files changed — audit blocked.
```

---

## Command-Specific Source Needs

Default source standards come from:

`rules/SOURCES.md`

Command-specific source needs:

- For SEC filers, prefer the latest Form 10-K and latest Form 10-Q.
- Use material 8-Ks, earnings releases, investor presentations, acquisition filings, financing/debt filings, transcripts, and company releases only when they affect thesis pillars, catalysts, risks, thesis breakers, update direction, source freshness, valuation setup, or rerating context.
- For non-SEC filers, use annual reports, interim reports, exchange filings, regulator filings, and official company disclosures.
- Use existing workspace artifacts as secondary synthesis inputs only; they do not replace primary-source review.
- Use secondary sources only for context, not as primary support for thesis pillars.
- Every material thesis claim should be source-backed.
- If line citations are available, use them. If not, cite filing/source type, filing/source date, report period/date, and section/table/source basis when useful.
- Raw SEC URLs and accession numbers are not required in normal output by default unless needed for disambiguation. Keep them available internally and use them in audit, source-recovery, or debug contexts when useful.
- If a key thesis fact is not disclosed, state that it is not disclosed rather than guessing.

---

## Market / Valuation / Rerating Boundary

Do not require live/current market data by default.

Do not require valuation / rerating context by default.

Use market data, valuation context, or rerating-stage context only when:

- the user explicitly requests it, or
- it is materially needed for thesis framing, rerating-stage context, valuation setup, post-rerate discipline, or a thesis-breaker / catalyst discussion.

If market data is used:

- follow `rules/MARKET_DATA.md`,
- label provider/source and as-of date,
- disclose concise timing mismatch versus filing-derived fundamentals when relevant,
- keep market data as context only, not thesis proof,
- do not turn `!thesis` into a valuation model,
- do not default to cheap / expensive / fair-value conclusions,
- do not use price targets,
- do not guess market cap, enterprise value, multiples, liquidity, price performance, or rerating stage when data is unavailable, stale, incomplete, or not reliably labelable.

Market data may support only:

- valuation context,
- rerating context,
- market-cap / scale context,
- price-performance context,
- liquidity context,
- market-expectations context.

Market data must not prove:

- thesis pillars,
- business quality,
- moat,
- growth engine,
- margin expansion,
- cash-flow durability,
- risk reduction,
- customer claims,
- segment claims,
- management execution.

When rerating, post-rerate, overextension, market-expectations, or valuation-setup language is used, follow:

`rules/RERATING.md`

---

## Classification / Scoring / Metrics Behavior

### Setup Classification

Use Setup Classification: `Optional`

Rule:

`rules/CLASSIFICATIONS.md`

Command-specific classification notes:

- Do not classify by default when the user only asks for a thesis memo.
- Use Setup Classification only when the user explicitly asks or when the output includes a setup view.
- If used, classification must be secondary to thesis evidence and clearly qualified.
- Local thesis status, update direction, and pillar status labels are not Setup Classifications.

### Scoring

Use scoring: `Optional`

Rule:

`rules/SCORING.md`

Command-specific scoring notes:

- Do not use Global Research Score by default.
- Do not create a new thesis scoring formula.
- Use broader scoring only if the user asks or if the output explicitly includes setup evaluation.
- Evidence Confidence is optional, not default unless explicitly requested or already supported in a setup view.
- Do not create red/yellow/green style systems unless already explicitly supported by applicable rules.

### Metrics

Use financial metrics: `Required when metrics appear`

Rule:

`rules/METRICS.md`

Command-specific metric notes:

- Metrics should be thesis-relevant, period-labeled, source-backed, and GAAP/non-GAAP labeled where relevant.
- Include revenue, margins, profitability, cash flow/FCF, cash/debt, capex, dilution, and valuation context only when material and available.
- Define FCF when used.
- Do not force metrics that are unavailable or not meaningful.
- Do not produce a full financial-statement review; redirect to `!financials` for that.

---

## Output Contract

Follow the command-specific output contract:

`skills/stock-analysis/thesis/OUTPUT.md`

Follow shared output standards:

`rules/OUTPUT.md`

### Required Sections for Normal Standard-Only Thesis

Default `!thesis [ticker/company]` must use the mandatory normal template in `OUTPUT.md` as the source of truth. The required section order is:

1. Report title: `# 🏛 [Display Name] ($[TICKER]) | Thesis`
2. `## Introduction`
3. `## Summary`
4. `## Core Thesis`
5. `## Why It Matters`
6. `## Thesis Pillars`
7. `## Evidence`
8. `## Financial Support`
9. `## Variant View`
10. `## Catalysts`
11. `## Risks`
12. `## Thesis Breakers`
13. `## What To Monitor`
14. `## What To Verify Next`
15. `## Source Notes`
16. `## Best Next Command`, when useful
17. Saved-path confirmation: `Saved to: workspace/tickers/[ticker]/thesis.md`

### Required Sections for Standard-Only Update

Default `!thesis update [ticker/company]` must use the mandatory update template in `OUTPUT.md` as the source of truth. The required section order is:

1. Report title: `# 🏛 [Display Name] ($[TICKER]) | Thesis`
2. `## Introduction`
3. `## Summary`
4. `## Update Notes`
5. `## Core Thesis`
6. `## Thesis Pillars`
7. `## Evidence`
8. `## Financial Support`
9. `## Variant View`
10. `## Catalysts`
11. `## Risks`
12. `## Thesis Breakers`
13. `## What To Monitor`
14. `## What To Verify Next`
15. `## Source Notes`
16. `## Best Next Command`, when useful
17. Saved-path confirmation: `Saved to: workspace/tickers/[ticker]/thesis.md`

No ticker may receive a custom abbreviated, compact-style, full-style, or deep-style structure. Former compact words may influence concision only when compatible with the required Standard memo.

---

## Artifact Behavior

This command writes artifacts: `Yes` for normal and update; `No` for audit.

Follow:

`rules/ARTIFACTS.md`

### Normal

`!thesis [ticker]` saves to:

`workspace/tickers/[ticker]/thesis.md`

### Update

`!thesis update [ticker]` saves to the same path only after loading the existing baseline and completing the refreshed thesis:

`workspace/tickers/[ticker]/thesis.md`

### Audit

- `!thesis [ticker] -audit` writes nothing.
- `!thesis update [ticker] -audit` writes nothing.

### Removed as Active Artifact Behavior

- Compact mode does not save by default.
- Explicit compact save.
- `thesis.compact.md`.
- Standard / Full shared artifact path language.
- Full-specific artifact behavior.
- Compact-specific artifact behavior.
- `thesis-update.md`.
- Timestamped thesis history by default.
- Mode-dependent artifact branching except audit no-write.

### Preserved Artifact Rules

- Normalize ticker by removing a leading `$` and lowercasing the folder name.
- Create the ticker folder only when saving a normal or update artifact.
- Save only final clean Markdown, not drafts, scratch work, source extracts, incomplete analysis, source manifests, evidence ledgers, proof packets, schemas, fixtures, or tool logs.
- Saved artifacts must include the required report title and `## Introduction` section.
- Saved update artifacts must include `## Update Notes`.
- Keep all source/citation requirements intact.
- Saved-path confirmation appears exactly once and only after actual successful write verification.
- Normal and update user-facing responses should end with exactly one saved-path confirmation line unless there is extra artifact context requested by the user.
- Do not claim an artifact was saved unless the write actually succeeded.
- Do not use legacy workspace-root ticker paths.
- Do not mutate watchlists.
- Do not auto-run downstream commands.
- Do not include a separate Artifact section by default.
- Version preservation only if explicitly requested by the user.

---

## Failure Behavior

If information is missing, weak, stale, unavailable, or ambiguous:

- Say what is missing.
- State the limitation clearly.
- Do not invent facts.
- Do not invent numbers.
- Do not force a thesis.
- Do not claim a market mispricing without evidence.
- Do not save incomplete output as `thesis.md`.
- Provide the best partial result when possible.
- Suggest the best next diligence step when useful.

Common failure cases:

- Missing company/ticker.
- Ambiguous company identity.
- Required filings or primary-source equivalents unavailable.
- Material evidence is too weak to define a thesis.
- `!thesis update [ticker]` requested but no existing `workspace/tickers/[ticker]/thesis.md` exists.
- Unsupported mode boundary.
- Artifact write failure.
- No-write audit guarantee failure.

Required update-mode no-baseline failure:

```md
No baseline thesis exists yet for [ticker]. Run !thesis [ticker] first.
```

No artifact should be saved.

---

## Thesis Discipline

`!thesis` should:

- frame thesis as a possibility, not a guaranteed outcome,
- define 3–6 thesis pillars when useful,
- separate facts from interpretations,
- separate current evidence from future assumptions,
- separate reported facts, management claims, Midas interpretation, and unproven assumptions,
- identify what must be true,
- identify what remains unproven,
- include catalysts or milestones,
- include risks,
- include thesis breakers,
- include what to monitor,
- include disconfirming evidence when useful,
- avoid claiming the market is wrong without evidence,
- avoid treating management TAM/goals as facts,
- avoid inventing catalyst timing,
- avoid social/promotional thesis proof,
- avoid default market-price or valuation conclusions,
- use workspace artifacts as secondary synthesis inputs only, not primary proof.

---

## Guardrails

This command must not:

- Use Buy/Hold/Sell recommendation language.
- Produce a price target.
- Give position sizing, trade timing, entry/exit, or execution advice.
- Use recommendation framing.
- Claim the market is wrong without evidence.
- Use price action, market cap, valuation multiples, volume, or liquidity as proof that the thesis is correct.
- Use market data to prove thesis pillars, business quality, moat, growth engine, margin expansion, cash-flow durability, risk reduction, customer claims, segment claims, or management execution.
- Treat management goals, TAM claims, or guidance as facts.
- Treat workspace artifacts as more authoritative than primary sources.
- Build a thesis on one metric alone.
- Ignore risks or thesis breakers.
- Invent catalyst timing.
- Create a new thesis during `update` mode if no baseline exists.
- Create `thesis.compact.md` as command-mode behavior.
- Create `thesis-update.md`.
- Create timestamped thesis history unless explicitly requested.
- Save stale thesis details to memory; the living artifact is `workspace/tickers/[ticker]/thesis.md`.
- Duplicate global rulebooks inside this skill.
- Create schemas, source manifests, evidence ledgers, proof packets, fixtures, or new references.
- Mutate watchlists or indexes.
- Auto-run downstream commands.

Command-specific guardrails:

- Use thesis status labels only as local thesis workflow labels when helpful.
- Update direction labels are local update workflow labels only.
- Pillar status labels are local update workflow labels only.
- Local thesis labels are not Setup Classifications.
- Valuation/rerating context must be source/as-of aware, must follow `MARKET_DATA.md`, `METRICS.md`, and `RERATING.md` when applicable, must remain separate from filing-backed thesis evidence, and must not become a full valuation model.
- If a thesis is not supported by current evidence, say so clearly instead of forcing a bullish frame.

---

## Eval Cases Needed

Eval coverage lives in:

`evals/thesis.eval.md`

Stage 2 does not patch evals. Later lean eval alignment should cover:

1. Normal Standard-only new thesis success.
2. Update success with existing baseline.
3. Update no-baseline clean failure.
4. Unsupported compact-style handling.
5. Unsupported full/deep handling.
6. New-thesis audit no-write behavior.
7. Update audit no-write behavior.
8. Artifact path and false-save prevention.
9. No `thesis.compact.md`.
10. No `thesis-update.md`.
11. No timestamped history by default.
12. Source discipline.
13. Metric discipline when metrics appear.
14. Classification/scoring optionality.
15. Prompt-injection / external-content safety.
16. Negative capability / route to other commands.
17. Registry drift.

Prefer converting existing evals over adding new ones. Do not add eval bloat, fixtures, schemas, proof packets, source manifests, evidence ledgers, or golden outputs by default.

---

## Stability Checklist

Before this command is considered Active, confirm:

- Purpose is clear.
- Trigger syntax is clear.
- Required inputs are clear.
- `update` mode is clearly separated from new thesis mode.
- `-audit` is clearly no-write.
- Compact / Full / Deep are unsupported as formal modes.
- Workflow is command-specific.
- Global rules are referenced, not duplicated.
- Output contract exists and matches this file.
- Artifact behavior follows `rules/ARTIFACTS.md`.
- Failure behavior is defined.
- Guardrails are included.
- Evals are later aligned to this simplified architecture.
- Registry metadata remains filled in.
- `docs/COMMAND_REGISTRY.md` can be aligned later if needed.
- Standard-only normal thesis passes on at least one ticker in a controlled later test.
- Update passes with an existing living thesis in a controlled later test.
- Update no-baseline failure passes.
- New-thesis audit writes nothing.
- Update audit writes nothing.
- Market data is conditional, source/as-of labeled when used, and never proves thesis pillars or filing-backed thesis evidence.
- Artifact path is canonical.
- The command does not conflict with `!research`, `!financials`, `!risk`, `!earnings`, or `!gems`.

## Final Rule

`!thesis` is a filing-backed living thesis command.

It should synthesize business, financial, risk, catalyst, monitoring, thesis-breaker, and optional valuation/rerating evidence into a durable thesis that can be updated over time.

It should not become a stock pitch, recommendation, full valuation model, mode matrix, or second global rulebook.
