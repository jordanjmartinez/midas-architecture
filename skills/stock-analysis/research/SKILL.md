---
name: research
description: Filing-backed business-model research for a public company or ticker. Use for !research [ticker/company], /research [ticker/company], or natural-language company research requests.
version: 2.0.0
author: Midas / Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [stocks, equity-research, sec-filings, business-model, company-research]
    related_skills: [financials, thesis, risk, full]
---

# MIDAS Command Skill — !research

## Command References

- `references/source-extraction.md` — SEC filing extraction, SEC HTML/XBRL, citation recovery, and not-disclosed discipline.
- `references/entity-resolution.md` — ambiguous ticker, issuer identity, successor/redomiciliation, and legal entity transitions.
- `references/artifact-safety.md` — normal artifact overwrite/readback safety, context reanchor, and audit no-write boundary.
- `references/non-us-and-fpi.md` — FPI, non-U.S. issuer, 20-F/6-K/local-report handling, and non-U.S. disclosure limitations.
- `references/sector-edge-cases.md` — compact reusable business-model extraction cues for niche sectors.

## Command

`!research`

## Registry Metadata

Command: `!research`
Aliases: `/research`, `research`
Category: `Company Research`
Status: `Active`
Skill Path: `skills/stock-analysis/research/SKILL.md`
Output Path: `skills/stock-analysis/research/OUTPUT.md`
Eval File: `evals/research.eval.md`
Uses Classification: `Optional`
Uses Scoring: `Optional`
Uses Metrics: `Optional`
Writes Artifacts: `Yes`
Primary Global Rules: `GLOBAL.md, COMMAND_INTERFACE.md, SOURCES.md, CLASSIFICATIONS.md, SCORING.md, METRICS.md, OUTPUT.md, ARTIFACTS.md`

## Purpose

`!research` produces a filing-backed business-model research note for a public company or ticker. It helps the user understand what the company does, how it makes money, what the filings disclose about customers, segments, geography, recurrence, pricing power, cyclicality, recent business trends, and business-model risks before deciding which deeper diligence command to run next.

---

## When To Use

Use this command when:

- The user asks `!research [ticker/company]`, `/research [ticker/company]`, or naturally asks to research a company or ticker.
- The user needs a plain-English, filing-backed business-model view.
- The user wants to understand revenue mechanics, customers, end markets, geography, recurrence, pricing power, cyclicality, and key filing-backed business risks.

Do not use this command when:

- The user primarily wants financial statement analysis. Use `!financials` instead.
- The user wants bull/base/bear cases. Use `!thesis` instead.
- The user wants downside pressure-testing. Use `!risk` instead.
- The user wants a complete research packet with valuation, scoring, and classification. Run `!financials`, `!thesis`, and `!risk` alongside this research; the four core artifacts together form the complete packet.
- The user wants hidden-gem ranking or screening. Use `!gems` instead.
- The user asks only for current price, current market cap, volume, liquidity, quote data, or a market snapshot. Use `!market [ticker]` instead.

---

## Inputs

### Required Inputs

- Company name or ticker.

### Optional Inputs

- Source preference if the user provides a specific filing, report, transcript, or company document.
- Specific business-model focus such as customer concentration, geography, recurrence, pricing power, cyclicality, segments, end markets, business risks, or revenue mechanics.
- Optional audit flag: `-audit`.
- Explicit request for limited current-market context alongside business-model research, such as current market cap, price, volume, liquidity, or market snapshot context. Pure current-market snapshot requests should be routed to `!market [ticker]`.

Normal `!research [ticker]` always produces the one Standard filing-backed business-model report.

`-audit` is the only alternate mode.

### Input Clarification Rules

Ask for clarification only when ambiguity would materially change the company being researched.

If a ticker/company match is clear enough to proceed, state the identity assumption and proceed.

If multiple companies plausibly match the same ticker/name and the likely match is not clear, ask the user to clarify before analysis.

If a requested ticker cannot be verified and a clarification prompt has already been sent, do not proceed with a likely typo candidate or imply the user confirmed a substitute unless an explicit user response confirms it. Any tentative research gathered for a likely candidate must remain clearly labeled as tentative and must not be saved or presented as the requested ticker’s final report.

---

## Aliases

Supported aliases:

- `/research`
- `research`
- Natural-language company research requests.

---

## Parser / Routing Behavior

Normal routing:

- `!research [ticker]` → produce the one Standard filing-backed business-model report.
- `!research [ticker] -audit` → run no-write audit mode.

Audit flag:

- Single-dash `-audit` is canonical.
- If the user uses `--audit`, return this short correction and do not run the command:

```md
Use `-audit` for `!research` audit mode.
```

Former compact-style words such as `compact`, `quick`, `brief`, `short`, `concise`, and `summary` are not output modes for `!research`.

- Treat them as style hints only when compatible with the Standard report.
- If the request conflicts with required Standard output, use this boundary message:

```md
`!research` now uses one Standard filing-backed business-model report. I can keep the sections concise, but the command still preserves source visibility and saves the canonical research artifact.
```

Former full/deep-style words such as `full`, `deep`, `detailed`, `expanded`, `deep-dive`, and `deepdive` are not output modes for `!research`.

- If the request asks for a full packet, recommend completing `!financials [ticker]`, `!thesis [ticker]`, and `!risk [ticker]`.
- If the request asks for thesis work, recommend `!thesis [ticker]`.
- If the request asks for financial statements or metric quality, recommend `!financials [ticker]`.
- If the request asks for downside or thesis-breaking risk, recommend `!risk [ticker]`.
- If the request is a specific business-model focus, keep it inside normal `!research`.

Do not auto-run downstream commands.

---

## Global Rules

This command must follow:

- `rules/GLOBAL.md`
- `rules/COMMAND_INTERFACE.md`
- `rules/SOURCES.md`
- `rules/OUTPUT.md`
- `rules/ARTIFACTS.md`

Use when applicable:

- `rules/CLASSIFICATIONS.md`
- `rules/SCORING.md`
- `rules/METRICS.md`
- `rules/MARKET_DATA.md` only for explicit current-market context or market-data boundary discipline.

Do not duplicate global rule content inside this command. Reference global rules instead.

---

## Workflow

Reference: `references/source-extraction.md` covers SEC filing extraction, SEC HTML/XBRL parsing, citation recovery, table reconstruction, calculated-ratio labeling, and not-disclosed discipline.

Reference: `references/entity-resolution.md` covers ambiguous tickers, issuer identity checks, successor/redomiciliation situations, and legal entity transitions.

Reference: `references/artifact-safety.md` covers normal artifact overwrite/readback safety, context reanchor after compaction or interruption, and the `-audit` no-write boundary.

Reference: `references/non-us-and-fpi.md` covers foreign private issuers, non-U.S. issuers, Form 20-F / Form 6-K / local-report handling, and non-U.S. disclosure limitations.

Reference: `references/sector-edge-cases.md` covers compact reusable business-model extraction cues for niche sectors such as consumer brands, freemium apps, and fabless/power semiconductor transition stories.

Follow this command-specific workflow:

1. Parse the request and identify the target company or ticker.
2. Determine whether the request is normal `!research [ticker]` or no-write audit mode `!research [ticker] -audit`.
3. If the request uses `--audit`, return `Use -audit for !research audit mode.` and stop.
4. If there was context compaction, an interrupted prior command, or any recent work on a different ticker, explicitly re-anchor on the latest active user request before doing more work: command type, ticker/company, output artifact path, and report type must all match the current request. Do not continue a stale ticker or stale command type from tool output, restored todo state, prior artifact content, or pre-compaction assistant drafts. If any anchor mismatches, hard-stop, reset the plan, and execute the latest active user command instead.
5. Resolve company identity before analysis: legal name, ticker, exchange if available, SEC CIK if applicable, and whether it is an SEC filer.
6. If the issuer is newly redomiciled, renamed, reorganized, or a successor issuer, reconcile the current public-company identity with predecessor operating-company filings before analysis; cite the relevant 8-K or filing that explains the transition.
7. Decide whether the input is clear enough to proceed; clarify only if ambiguity changes the target company.
8. Determine whether the user requested pure current-market data or business-model research plus current-market context. For pure current price, current market cap, volume, liquidity, quote, or market snapshot requests, route to `!market [ticker]` instead of turning `!research` into a market-data command; do not generate a business-model report and do not create or update `workspace/tickers/[ticker]/research.md`.
9. For no-write audit mode, follow the No-Write Audit Rule below before any source gathering.
10. Gather primary evidence under `rules/SOURCES.md`.
11. For SEC filers, identify the most recent 10-K and most recent 10-Q when available; record form type, filing date, report period, accession number, and source basis for internal traceability. Normal Source Notes should not display accession numbers by default. Include accession numbers only when the user asks for detailed filing identifiers, audit/debug/source-recovery context makes them useful, or multiple same-form filings on similar dates would otherwise be ambiguous. Include raw URLs only if the user asks for source links, a non-standard source cannot be clearly identified by filing metadata, or audit/debug/source-recovery context makes the URL useful.
12. For non-SEC filers, identify the closest primary-source equivalents such as annual reports, interim reports, exchange filings, regulator filings, or official company disclosures.
13. Extract evidence relevant to business model, segment/revenue categories, customers, end markets, geography, revenue recognition, recurrence, contracts, backlog/RPO, pricing pressure or pricing power, cyclicality, seasonality, recent business trends, and business risks.
14. If the user asked for business-model research plus explicit current-market context, keep any market data separate, labeled, and non-evidentiary for business-model conclusions under the Market Data Boundary section.
15. Separate filing-backed facts from interpretation.
16. Explicitly state when important facts are not disclosed in the reviewed sources.
17. Use only lightweight business-performance metrics when they support the business-model discussion; do not turn the output into `!financials`.
18. When deriving business-model percentages from filing tables (for example segment revenue mix, recognition mix, backlog mix, or year-over-year segment growth), calculate them with a tool, not mental math; label them as calculated from filing values and keep them clearly secondary to the business-model explanation.
19. Apply Setup Classification only when the response includes a setup view or final research view; do not force classification into a factual business-model explanation.
20. Apply scoring only if the user asks for a score or the output explicitly includes setup evaluation; if full scoring is needed, apply it per `rules/SCORING.md` on explicit request.
21. Produce the response using `skills/stock-analysis/research/OUTPUT.md` plus global output rules.
22. Save the final clean Markdown artifact after the final output is complete and verified for normal `!research [ticker]` only.
23. If a prior `!research` run was interrupted and the user issues a new command, do not silently resume the old ticker or imply completion. Briefly state what, if anything, was completed for the interrupted run, then execute the new command. Do not save an artifact for the interrupted ticker unless its final output was actually completed and verified.
24. Before overwriting `workspace/tickers/[ticker]/research.md`, read or otherwise inspect the existing file when the tool reports potential sibling/user modification, unusual customization, or other overwrite risk. If the existing file was read with offset/limit pagination or the write tool warns that only a partial view was inspected, re-read the complete file before overwriting or create a versioned backup if full inspection is impractical. Preserve the command’s default replace behavior for normal generated artifacts, but avoid blindly overwriting a file that may contain newer user/sibling work.
25. End normal successful responses with the required saved-path confirmation only after the artifact was actually written.

Keep this command focused on business-model research.

---

## No-Write Audit Rule

`!research [ticker] -audit` is the only alternate mode.

Audit mode must not:

- write `workspace/tickers/[ticker]/research.md`
- write `workspace/tickers/[ticker]/research.compact.md`
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

- resolve ticker/company identity in memory
- retrieve/read sources in memory
- inspect existing artifact status read-only
- summarize source/filing basis
- summarize business-model coverage
- summarize missing evidence
- summarize source limitations
- summarize output safety
- summarize artifact status
- recommend the next step

If no-write cannot be guaranteed, stop before source gathering and return:

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

## Command-Specific Source Needs

Default source standards come from:

`rules/SOURCES.md`

Command-specific source needs:

- For SEC filers, prefer the latest Form 10-K and latest Form 10-Q.
- Use 8-Ks, S-1s, 20-Fs, 40-Fs, proxies, exhibits, investor presentations, earnings releases, or transcripts only when useful for current business context or when 10-K/10-Q coverage is insufficient.
- For non-SEC filers, use annual reports, interim reports, exchange filings, regulator filings, and official company disclosures.
- Use secondary sources only for context, not as the primary basis for business-model claims.
- Every material factual claim should be citation-backed.
- If line citations are available, use them.
- If line citations are unavailable, cite filing name, filing date, report period/date, and section/table/source basis. Keep accession numbers available internally, but do not require or display them in normal Source Notes by default; include them only when the user asks for detailed filing identifiers, audit/debug/source-recovery context makes them useful, or multiple same-form filings on similar dates would otherwise be ambiguous. Do not include raw SEC URLs in normal Source Notes by default; include URLs only if the user explicitly asks for links, a non-standard source cannot be clearly identified by filing metadata, or audit/debug/source-recovery context makes the URL useful.

SEC access implementation note:

- Use a compliant descriptive SEC User-Agent when retrieving SEC data.
- If a SEC request fails due to headers or response format, retry with a compliant client/header pattern before treating the filing as unavailable.
- Do not expose personal contact details in skill output or stored artifacts.

## Market Data Boundary

`!research` is filing-backed business-model research by default. It should not fetch or display live/current market-data snapshots by default.

If the user asks only for current price, current market cap, volume, liquidity, quote data, or a market snapshot, route to:

```md
!market [ticker]
```

If the user asks for business-model research plus current market context, `!research` may include market data only as clearly labeled Tier 2 market context under `rules/MARKET_DATA.md`.

When market data is truly needed inside `!research`:

- Use the canonical helper directly under `MARKET_DATA.md`.
- Do not call or parse `!market` user-facing output text.
- Do not duplicate provider fallback logic inside `!research`; follow `MARKET_DATA.md` and use the canonical helper output.
- Label provider/source, as-of timestamp, timezone when available, limitations, and timing mismatch versus filing-derived inputs.
- Keep market data separate from filing-backed business-model conclusions.

Market data may support only limited current-market context, such as:

- current price context
- market-cap / scale context
- volume / liquidity context
- price-performance context
- market snapshot context

Market data must not prove or alter conclusions about:

- business model
- revenue mechanics
- customer claims
- geography
- recurrence
- pricing power
- cyclicality
- segment mix
- business quality
- moat
- business-model risks
- filing-backed conclusions

---

## Classification / Scoring / Metrics Behavior

### Setup Classification

Use Setup Classification:

- Optional

Rule:

```md
Use `rules/CLASSIFICATIONS.md`.
```

Command-specific classification notes:

- Use classification only when the response produces a setup view or final research view.
- Do not classify a purely factual business-model explanation.
- If classification is used, keep it secondary to the business-model evidence and clearly qualify confidence.

### Scoring

Use scoring:

- Optional

Rule:

```md
Use `rules/SCORING.md`.
```

Command-specific scoring notes:

- Do not score by default.
- Use scoring only if the user asks for a score or if the output explicitly includes setup evaluation.
- If the user wants full scoring, apply it per `rules/SCORING.md` on explicit request.

### Metrics

Use financial metrics:

- Optional

Rule:

```md
Use `rules/METRICS.md`.
```

Command-specific metric notes:

- Use lightweight business-performance metrics only when they support the business-model discussion.
- Examples include revenue trend, segment revenue, revenue category mix, backlog/RPO, customer concentration, geography, retention, or other disclosed operating metrics.
- Do not produce a full margin, cash-flow, balance-sheet, valuation, or shareholder-return review; redirect to `!financials` for that.

---

## Output Contract

Follow the shared output standards:

`rules/OUTPUT.md`

Follow the command-specific output contract:

`skills/stock-analysis/research/OUTPUT.md`

### Required Normal Sections

Normal `!research [ticker]` has one Standard-only output shape. Required sections must appear in this order:

- Report title, formatted as `# 📜 [TICKER] | [Company Name] Business Analysis`
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

`Source Notes` is required and must appear after `What To Verify Next` and before `Best Next Command`, when useful. Normal Source Notes should be concise: filing type, filing date, report period/date, and source-basis description; do not include accession numbers or raw SEC URLs by default.

### Standard Finalization / Display Check

Before finalizing a normal `!research` response:

- Confirm the user-facing response contains the required Standard-only sections.
- Confirm the response is not merely a completion summary.
- Confirm the saved artifact and user-facing response materially match in structure and conclusion.
- Confirm Best Next Command, when included, uses `## Best Next Command`, then a blank line, then `` `!command TICKER` — Reason. ``
- Confirm the reason after the dash starts with a capital letter.
- Confirm the Best Next Command body does not repeat `Best next command:` or `Best Next Command:` under the heading.
- Confirm the final saved-path line uses:

```md
Saved to: workspace/tickers/[ticker]/research.md
```

- Confirm the saved-path line appears exactly once and is the final line.
- If the drafted response only says the command is complete, gives key filing-backed points, or uses `Saved artifact:`, hard-stop and regenerate the complete Standard-only response.

### Optional Sections

- Setup Classification
- Setup Modifiers
- Evidence Confidence
- Artifact section only when there is extra artifact context beyond a normal save confirmation, such as multiple files, versioning, path changes, save failure, or an explicit user request for artifact details.

### Supported Modes

- Normal: supported. This is the default Standard-only business-model report.
- Audit: supported only through `-audit` and writes nothing.

Unsupported modes:

- Compact mode.
- Full mode.
- Deep mode.

---

## Artifact Behavior

This command writes artifacts:

- Normal `!research [ticker]`: Yes.
- Audit `!research [ticker] -audit`: No.

Follow the global artifact standards:

`rules/ARTIFACTS.md`

### Creates / Updates

Normal `!research [ticker]`:

- `workspace/tickers/[ticker]/research.md`

Audit `!research [ticker] -audit`:

- Writes nothing.

### Replace Behavior

- Normal `!research [ticker]` may overwrite the prior `research.md` for the same normalized lowercase ticker unless the user explicitly asks to preserve versions.
- Audit mode must not create, update, overwrite, or append to any artifact.

### Command-Specific Rules

- Normalize ticker by removing a leading `$` and lowercasing the folder name.
- If the ticker folder does not exist, create it only when saving a normal artifact.
- Save only the clean final Markdown output after analysis is complete and verified.
- Use the required artifact header from `rules/ARTIFACTS.md`, with Analysis Type set to `Business Analysis`.
- Saved normal artifacts must include the required report title and `Introduction` section; if a metadata header is present, the visible report body immediately after the header must begin with `# 📜 [TICKER] | [Company Name] Business Analysis`, then `## Introduction`, then `## Summary`.
- Artifact header pitfall: do not add an extra ad-hoc H1 such as `# Company (TICKER) — Business Analysis` before the canonical visible report title. Use the required `ARTIFACTS.md` metadata/header pattern if needed, then begin the visible body directly with the canonical `# 📜 [TICKER] | [Company Name] Business Analysis` title.
- Normal user-facing responses must not include a separate Artifact section by default. End with exactly one saved-path confirmation line only after the artifact was actually written:

```md
Saved to: workspace/tickers/[ticker]/research.md
```

- Only include a separate Artifact section if there is extra artifact context beyond a normal save confirmation, such as multiple artifacts created, a versioned artifact preserved, the artifact path changed, a save failed, or the user explicitly asked for artifact details. Otherwise use only the final saved-path confirmation line.
- Do not claim an artifact was written unless it was actually created or updated.
- Do not mutate watchlists while saving research artifacts.
- Do not auto-run downstream commands.

---

## Failure Behavior

If information is missing, weak, stale, unavailable, or ambiguous:

- Say what is missing.
- State the limitation clearly.
- Do not invent facts.
- Do not invent numbers.
- Do not force a conclusion about moat, pricing power, recurrence, customer concentration, cyclicality, or geography.
- Provide the best partial result when possible.
- Suggest the best next diligence step when useful.

Useful phrases:

```md
Could not verify:
```

```md
Missing information:
```

```md
Source limitation:
```

```md
Partial result:
```

```md
Best next step:
```

---

## Guardrails

This command must not:

- Use Buy/Hold/Sell recommendation language.
- Treat tracked ownership or disclosures as copy-trading signals.
- Treat social media as thesis proof.
- Present unverified claims as facts.
- Hide material risks.
- Invent metrics or unsupported precision.
- Ignore stale data.
- Ignore source limitations.
- Overwrite important files outside its artifact contract.
- Duplicate global rules inside this skill.

Command-specific guardrails:

- Do not present a full valuation model or price target.
- When refusing buy/sell/price-target requests, provide research framing only. Do not use `I'd classify it as` or similar classification phrasing unless using an approved Setup Classification from `rules/CLASSIFICATIONS.md` and explicitly outputting `Setup Classification: [approved classification]`.
- For non-classification framing, use `Business-model characterization: ...` instead of `I'd classify it as: ...`.
- Do not perform a full financial statement analysis; redirect to `!financials`.
- Do not build bull/base/bear cases unless the user explicitly asks and the scope is redirected to `!thesis`.
- Do not turn the company into a hidden-gem ranking or screen.
- Do not call revenue recurring unless reviewed filings support that conclusion.
- Do not assert pricing power, cyclicality, moat, customer concentration, segment mix, geography, or contract structure unless source-backed.
- Do not fetch live/current market data by default for plain `!research [ticker]`.
- Do not use market data to prove or alter business-model conclusions, revenue mechanics, customer claims, geography, recurrence, pricing power, cyclicality, segment mix, business quality, moat, business-model risks, or other filing-backed conclusions.
- Do not treat price action, market cap, volume, liquidity, or rerating as proof of business quality or business-model risk.
- Do not turn `!research` into a current quote, market snapshot, valuation, price-action, or trading command.
- Do not call or parse `!market` user-facing output text.
- Do not duplicate provider fallback logic inside `!research`; follow `MARKET_DATA.md` and use the canonical helper output.

---

## Eval Cases Needed

Eval file:

```bash
evals/research.eval.md
```

Required eval coverage:

1. Normal successful `!research TICKER` case.
2. Weak or missing evidence case.
3. Guardrail / clean failure case.
4. Registry metadata / registry drift case.
5. Source discipline case.
6. Negative capability case proving `!research` does not become `!financials`, `!thesis`.
7. Artifact behavior case.
8. Prompt-injection / external-content safety case for filings, PDFs, HTML, documents, or transcripts.
9. Market-data boundary case proving Standard `!research [ticker]` does not fetch live market data by default.
10. Current market snapshot redirect case proving pure current price / market cap / volume / liquidity requests route to `!market [ticker]`.
11. Market-context separation case proving explicit market context is labeled as Tier 2 context and does not support business-model conclusions.
12. No `!market` output parsing case.
13. No valuation, recommendation, trading, or price-action thesis-proof drift case.

---

## Active Readiness / Monitoring Checklist

Active readiness is satisfied when:

- Purpose is clear.
- Trigger syntax is clear.
- Required inputs are clear.
- Workflow is command-specific.
- Global rules are referenced, not duplicated.
- Output contract is defined.
- Artifact behavior is defined.
- Failure behavior is defined.
- Guardrails are included.
- Evals exist or are planned.
- Command registry metadata is filled in.
- `docs/COMMAND_REGISTRY.md` is updated when the command is created, renamed, deprecated, or materially changed.
- Normal Standard-only output passes.
- `-audit` no-write behavior passes.
- Artifact behavior is verified.
- Filing-backed source discipline passes on more than one normal ticker.
- The command does not conflict with `!financials`, `!thesis`, `!risk`, or `!gems`.

Carried-forward monitoring items do not block Active status when normal tested tickers pass:

- Runtime-heavy tickers with slow filing retrieval or unusually large filings.
- Weak/missing-evidence fixtures.
- Clean-failure fixtures.
- Prompt-injection fixtures.
- Future unsupported-inference regressions.
- Buy/price-target guardrail spot checks.

## Final Rule

`!research` is a filing-backed business-model research command.

It should make the company understandable before deeper financial analysis, thesis construction, risk pressure-testing, or full scoring.

It should not become a second global rulebook or a full report command.
