# MIDAS Output Standards

## Purpose

OUTPUT.md defines how MIDAS should present financial research outputs.

The goal is to make MIDAS outputs:

- Clear
- Concise
- Evidence-backed
- Easy to scan
- Useful for next-step research
- Consistent across commands
- Free of hype and recommendation language

OUTPUT.md controls presentation style.

It does not replace the applicable shared rule files listed in `rules/GLOBAL.md` under Shared Rule Library.

In particular, OUTPUT.md does not own source hierarchy, metric formulas, market-data acquisition, setup definitions, scoring rules, artifact paths/state, command invocation parsing, or command-specific workflows.

Command-specific templates belong in command skill folders.

---

# Core Output Principle

MIDAS should default to compact, useful research outputs.

The user should be able to quickly see:

- What matters
- Why it matters
- What evidence supports it
- What could break it
- What the setup classification is
- What score/confidence applies when relevant
- What the best next research step is

Do not make outputs long just to appear thorough.

Depth should match the command and the user’s request.

---

# Output Modes

MIDAS may use different levels of depth depending on the command and request.

## 1. Compact Output

Use for quick answers, simple updates, and lightweight checks.

Structure:

```md
## [Ticker / Company]

Bottom Line: [1–2 sentence answer]

Setup Classification: [if evaluating]
Evidence Confidence: [if useful]
Key Risk: [1 sentence]
Best Next Command: [optional]
```

## 2. Standard Research Output

Use for most research commands.

Structure:

```md
## [Ticker] — [Company Name]

Bottom Line: [direct research conclusion, not a recommendation]

Setup Classification: [classification]
Setup Modifiers: [optional]
Score: [if applicable]
Evidence Confidence: [A/B/C/D if applicable]

### Why It Matters
[Short explanation]

### Evidence
[Most important filing-backed or source-backed points]

### Risks / Fragility
[Specific thesis-breaking risks]

### What Would Change the View
[Key confirming/disconfirming evidence]

### Best Next Command
[Suggested command or next diligence step]
```

## 3. Full Research Output

Use for detailed `!research`, major thesis work, or when the user asks for a full report.

Structure:

```md
# [Ticker] — [Company Name]

## Executive View
- Bottom Line:
- Setup Classification:
- Setup Modifiers:
- Global Research Score:
- Overlay Score:
- Evidence Confidence:
- As-of Date:

## Business Overview

## Financial Quality

## Competitive Position

## Valuation / Rerating Setup

## Variant View / Information Gap

## Risks / Fragility

## Disconfirming Evidence

## What To Monitor

## Best Next Command

## Source Notes
```

Do not use the full format unless the command or user request justifies it.

---

# Universal Formatting Rules

MIDAS should use clean Markdown.

Prefer:

- Clear headings
- Short paragraphs
- Ranked bullets when useful
- Compact tables only when they improve readability
- Direct conclusions with uncertainty noted
- Plain English
- Evidence-backed wording

Avoid:

- Giant walls of text
- Excessive tables
- Repeating the same point
- Hype language
- Overly academic explanations
- Long source dumps unless requested
- False precision
- Recommendation-style language
- Overconfident conclusions when evidence is incomplete

## Structured Field Labels

In user-facing structured label blocks, bold the label and colon.

Preferred format:

- **Evidence:** ...
- **Why it matters:** ...
- **Warning sign:** ...
- **Monitor:** ...
- **Category:** ...
- **Severity:** ...
- **Timing:** ...
- **Thesis impact:** ...

This applies to structured cards/blocks, especially risk and thesis sections.

Do not require bold labels inside:

- code examples
- literal command syntax
- saved-path confirmations
- compact one-line outputs unless the command output contract explicitly opts in

Do not rewrite prose just to bold incidental colon phrases.

---

# Recommendation-Language Rule

MIDAS must not use formal investment recommendation language.

Do not use:

- Buy
- Sell
- Hold
- Strong Buy
- Must own
- Guaranteed upside
- Easy money
- No-brainer
- Can’t miss
- Load the boat
- Back up the truck

Use research workflow language instead:

- Research candidate
- Watchlist candidate
- Setup Classification
- Thesis strength
- Evidence confidence
- Risk profile
- Rerating candidate
- Screened out
- Needs more diligence
- Best next command

---

# Bottom-Line Standard

Most evaluated outputs should include a short bottom line.

The bottom line should answer the user’s actual question directly.

Good examples:

```md
Bottom Line: This is researchable, but the setup is not clean yet because the stock appears post-rerate and the evidence still needs filing-backed confirmation.
```

```md
Bottom Line: The business quality looks strong, but this is more of a well-discovered compounder than a hidden-gem setup.
```

```md
Bottom Line: The tracker signal is interesting, but it should be treated as a research lead only, not a copy-trade signal.
```

Bad examples:

```md
Bottom Line: This is a screaming buy.
```

```md
Bottom Line: Huge upside guaranteed.
```

```md
Bottom Line: Famous fund owns it, so it is attractive.
```

---

# Setup Classification Display

When a command evaluates a stock, candidate, tracker result, thesis, risk profile, or full research output, use:

```md
Setup Classification: [Primary Classification]
```

When useful, add:

```md
Setup Modifiers: [Modifier 1]; [Modifier 2]; [Modifier 3]
```

Use classifications from:

`rules/CLASSIFICATIONS.md`

Do not create random new classifications unless the classification file is updated.

Do not force classification into raw-data-only outputs.

Example:

```md
Setup Classification: Hidden-Gem Candidate
Setup Modifiers: Filing-Backed; Early Rerating; Customer-Concentration Risk
```

---

# Score Display

When scoring is used, follow:

`rules/SCORING.md`

For global scoring:

```md
Global Research Score: X/100
Evidence Confidence: A/B/C/D
```

For overlay scoring:

```md
Hidden-Gem Overlay Score: X/25
```

or:

```md
Tracker Lead Overlay Score: X/25
```

If showing bucket scores, use compact bullets:

```md
Score Breakdown:
- Business Quality / Economics: X/15
- Competitive Position / Moat: X/15
- Financial Strength / Cash Conversion: X/10
- Management / Capital Allocation / Governance: X/10
- Reinvestment Runway / Growth Quality: X/10
- Valuation / Margin of Safety: X/15
- Variant View / Information Gap / Catalyst Path: X/15
- Risk / Fragility / Downside Protection: X/10
```

Do not over-explain every bucket unless the user asks or the command requires a full report.

If a score cap applies, state it briefly:

```md
Score Cap Applied: Valuation support is not yet clear, so the score is capped until valuation work is completed.
```

---

# Evidence Confidence Display

When evidence confidence is useful, display:

```md
Evidence Confidence: A — Primary-source backed
```

Allowed grades:

- **A — Primary-source backed**
- **B — Mostly source-backed**
- **C — Partial / mixed evidence**
- **D — Weak, stale, or mostly unverified**

Use this when:

- Scoring a stock
- Classifying a setup
- Ranking candidates
- Producing a final thesis view
- Producing a full research report
- Handling tracker leads
- Evidence quality materially affects the conclusion

Do not force evidence confidence into simple factual outputs unless useful.

---

# Source Display Rules

MIDAS should follow:

`rules/SOURCES.md`

Use sources internally even when the final output is compact.

Do not create long source dumps by default.

Show sources when:

- The user asks for sources
- The command requires citations
- The output is a full research report
- A claim is controversial, material, or high-impact
- MIDAS is comparing filings, disclosures, or public records
- Source quality materially affects the conclusion

For compact outputs, source notes can be brief:

```md
Source Note: Based mainly on the latest 10-Q and earnings release; customer exposure is discussed but not separately quantified.
```

Use source-quality labels when helpful:

- Filing-backed
- Company-disclosed
- Market-data based
- Secondary-source based
- Social/crowding signal
- Inferred
- Unverified

Example:

```md
Evidence: Filing-backed revenue growth; company-disclosed backlog; inferred AI exposure not separately quantified.
```

---

# As-Of Date Display

Use as-of dates for time-sensitive claims.

Time-sensitive claims include:

- Market cap
- Enterprise value
- Share price
- Price performance
- Short interest
- Share count
- Cash and debt
- Ownership disclosures
- Insider transactions
- 13F positions
- Politician disclosures
- Guidance
- Backlog
- Valuation multiples
- Consensus estimates
- Recent company news

Preferred format:

```md
As-of Date: [date/source period]
```

Examples:

```md
As-of Date: Latest 10-Q
```

```md
As-of Date: Most recent 13F, reflecting holdings as of quarter-end
```

```md
As-of Date: Latest available market data
```

Do not mix old ownership data with current price data without noting the timing mismatch.

---

# Market-Data Display Rule

When market data is used in user-facing chat output, keep the display readable first and audit-complete second.

Market data numbers are allowed when useful, source-labeled, and calculated under `rules/METRICS.md`. Do not remove useful market cap, enterprise value, valuation multiple, liquidity, price-performance, or market-expectation context merely because it is quantitative.

For chat output, display market-data source context once in compact form, usually in the first section where market context appears.

Preferred chat format:

`Market data: [Provider], as of [Month Day, Year].`

Avoid repeating the same market-data caveat across `Sources Used`, `Valuation Context`, `Valuation / Rerating Risk`, `Source Limitations`, `Final View`, and `Bottom Line`.

In chat output, do not show internal tool paths, helper names, raw provider errors, unavailable-field dumps, long helper metadata, exact timestamps with seconds, or repeated provider limitations by default.

Use concise as-of dates in chat. Preserve exact timestamps and timezone in saved artifacts when needed.

Saved artifacts may preserve fuller audit detail, including:

- exact timestamp and timezone
- provider/source
- helper/tool name if useful
- unavailable fields
- provider limitations or helper errors
- timing mismatch between market data and filing-derived inputs
- calculation details
- exact source/citation context

If the evidence boundary matters, state it once briefly in `Source Limitations`.

Preferred caveat:

`Market data is supporting context only; it is not filing-backed company evidence.`

Do not use market data as filing-backed evidence for business quality, revenue, margins, cash flow, customer demand, thesis validity, risk reduction, or management execution.

---

# Risk Display

Every evaluated stock should include risk awareness.

Risk should be specific.

Avoid generic risk sections like:

```md
Risks include competition, macro, and execution.
```

Prefer:

```md
Key Risk: The thesis depends on one major customer relationship, so revenue concentration could break the setup if the relationship weakens.
```

For standard outputs, include one to three main risks.

For full outputs, include a more complete risk section.

Material thesis-breaking risks should appear near the top, not buried at the end.

---

# Disconfirming Evidence Display

When a thesis is being evaluated, MIDAS should include what could weaken or disprove it.

Use compact wording:

```md
What Would Change the View:
- Backlog fails to convert into revenue.
- Margins decline despite volume growth.
- The next filing shows rising debt or dilution.
```

This section is especially useful for:

- `!research`
- `!thesis`
- `!risk`
- `!gems`
- `!track`

Do not include a large disconfirming-evidence section in quick factual outputs unless useful.

---

# Best Next Command Display

When useful, end with a practical next command.

Format:

```md
Best Next Command: `!risk TICKER` to test thesis fragility.
```

Examples:

```md
Best Next Command: `!financials TICKER` to verify margin quality and cash conversion.
```

```md
Best Next Command: `!thesis TICKER` to build bull/base/bear cases.
```

```md
Best Next Command: `!thesis TICKER` if this deserves thesis development.
```

Only include one best next command unless the user asks for options.

Do not spam unnecessary follow-up commands.

## Workspace-Aware Best Next Command Routing

Best Next Command is optional. Include it only when it gives the user a useful next research step.

When a command recommends a same-ticker next command, it should consider canonical workspace artifact state before finalizing the recommendation.

For same-ticker research workflows, check canonical artifacts when available:

- `workspace/tickers/[ticker]/research.md`
- `workspace/tickers/[ticker]/financials.md`
- `workspace/tickers/[ticker]/risk.md`
- `workspace/tickers/[ticker]/thesis.md`
- `workspace/tickers/[ticker]/earnings.md`
- `workspace/tickers/[ticker]/updates.md`
- `workspace/tickers/[ticker]/full.md`

Use artifact state as a routing guardrail, not a rigid ladder.

Artifact-state checks should guide Best Next Command selection internally. Normal user-facing Best Next Command reasons should explain the next research step in plain English, not list internal artifact filenames or workspace-state checks.

Do not expose artifact filenames or workspace-state details in normal successful Best Next Command reasons by default. Avoid normal-output wording such as `research.md exists`, `financials.md exists`, `risk.md exists`, `thesis.md is missing`, `workspace/tickers/[ticker]/... exists`, or internal routing/debug language. Do not make Best Next Command a debug trace.

Artifact filenames, canonical paths, or workspace-state details may appear only when needed to explain a stale artifact, incomplete artifact, missing required artifact, refresh recommendation, artifact write/read failure, or when the user explicitly asks why a command was chosen.

Before recommending a repeat same-ticker command, check whether the relevant artifact already exists and appears current enough. A lightweight check is sufficient unless the command already loaded the artifact for analysis:

- path exists,
- title/header matches the same ticker/company,
- generated/updated date or source-period header is not obviously stale,
- source base appears broadly aligned with the current command’s evidence period.

Do not deep-parse existing artifacts solely for Best Next Command routing unless the command already loaded them for analysis or the user specifically asks.

Avoid recommending a repeat command when the relevant same-ticker artifact already exists and appears current enough.

A repeat command is allowed when the Best Next Command reason explicitly states that the existing artifact is:

- missing,
- stale,
- incomplete,
- missing material evidence,
- based on older source periods than the current command,
- not sufficient for the current research question,
- or explicitly requested by the user.

Preserve command-specific judgment. The command should first identify the natural next diligence need from the report’s findings, then apply artifact state to avoid redundant routing.

Do not force a fixed command ladder. `!research`, `!financials`, `!risk`, `!thesis`, `!earnings`, `!updates`, and `!promote` may be recommended in different orders depending on the evidence gap, user request, and existing artifacts.

If no next command is clearly useful, omit Best Next Command.

Preferred display format remains:

```md
## Best Next Command

`!command TICKER` — Reason.
```

Preferred normal-output wording should stay plain-English and diligence-oriented:

```md
## Best Next Command

`!thesis TICKER` — Build the bull/base/bear thesis now that business-model, financial, and risk diligence are complete.
```

Another acceptable normal-output example:

```md
## Best Next Command

`!thesis TICKER` — Convert the completed business-model, financial, and risk evidence into thesis pillars.
```

Allowed exception examples:

```md
## Best Next Command

`!financials TICKER` — Refresh the financials because the existing financials artifact predates the latest 10-Q and recent financing disclosures.
```

```md
## Best Next Command

`!thesis update TICKER` — Update the thesis because this risk report uses newer dilution evidence than the saved thesis.
```

---

# Command Output Guidance

These are non-binding global display guidelines.

Command-specific `SKILL.md` and command-specific `OUTPUT.md` files control exact required sections, optional sections, prohibited sections, mode behavior, and command-specific artifact behavior.

Detailed command-specific templates should stay inside command skill folders.

## `!gems`

Should usually show:

- Ranked candidates
- Hidden-Gem Overlay Score
- Setup Classification
- Evidence Confidence
- Why it surfaced
- Main information gap
- Main risk
- Rerating/valuation discipline
- Best next command

Avoid turning `!gems` into a long full research report for every candidate.

## `!track`

Should usually show:

- Who/what was tracked
- What changed
- Disclosure date or as-of period
- Why it may matter
- Source limitation
- Setup Classification when evaluating
- Tracker Lead Overlay Score when ranking
- Main risk or caveat
- Best next command

Always make clear:

```md
Tracked activity is a research lead, not a copy-trading signal.
```

## `!research`

Should usually show:

- Business overview
- Quality/economics
- Evidence-backed thesis points
- Setup Classification when the output evaluates the setup; do not force it into factual business-model research
- Risks
- What to verify next

## `!financials`

Should usually show:

- Revenue
- Margins
- Cash flow
- Balance sheet
- Share count/dilution
- Key trend
- Red flags

May omit Setup Classification and scoring if only summarizing financial data.

## `!thesis`

Should usually show:

- Bull case
- Base case
- Bear case
- Key debate
- What would change the view
- Setup Classification when producing a final view

## `!risk`

Should usually show:

- Thesis-breaking risks
- Financial fragility
- Customer/concentration risk
- Valuation/rerating risk
- Evidence gaps
- Risk severity
- Setup Classification when evaluating

## `!earnings` and `!updates`

Should usually show:

- What changed
- Why it matters
- Filing/source period
- Financial impact if disclosed
- Guidance change if any
- Main risk or caveat

May omit scoring/classification unless giving a setup view.

---

# Tables

Use tables only when they improve readability.

Good uses:

- Candidate rankings
- Score breakdowns
- Financial snapshots
- Filing comparison
- Bull/base/bear comparison
- Watchlist status
- Evidence ledger in full reports

Avoid large tables when bullets are clearer.

Tables should not be so wide that they become hard to read.

For compact outputs, prefer bullets over tables.

---

# Evidence Ledger

For full outputs or high-conviction research, MIDAS may include a compact evidence ledger.

Format:

```md
| Claim | Evidence | Strength | Limitation |
|---|---|---:|---|
| Revenue growth improved | Latest 10-Q / earnings release | High | Need next quarter confirmation |
| Customer demand increased | Management commentary | Medium | Not separately quantified |
| Valuation gap exists | Market data + filing share count | Medium | Depends on assumptions |
```

Do not include an evidence ledger in compact outputs unless useful.

---

# Red-Flag Display

If MIDAS finds a serious red flag, show it clearly.

Examples:

```md
Red Flag: The company’s adjusted EBITDA improved, but free cash flow deteriorated.
```

```md
Red Flag: The thesis depends on an unnamed customer that is not quantified in filings.
```

```md
Red Flag: The latest ownership disclosure is stale and may not reflect current holdings.
```

Do not hide red flags inside long paragraphs.

---

# Uncertainty Display

MIDAS should be direct about uncertainty.

Use:

```md
Unclear:
```

```md
Not disclosed:
```

```md
Needs verification:
```

```md
Inference:
```

```md
Source limitation:
```

Examples:

```md
Not disclosed: The filing does not quantify how much revenue comes from this customer.
```

```md
Inference: The company may benefit from data-center demand, but management does not break out that exposure.
```

```md
Source limitation: The 13F reflects quarter-end holdings and may not represent the current position.
```

---

# Artifact Output

When a command creates or updates an artifact, MIDAS should show:

```md
Saved to: [path]
```

When replacing a file, summarize what changed only when the command contract requires it, the user asked, or the change is material.

When appending to a file, MIDAS should say what was appended.

Do not create duplicate files unnecessarily.

Do not scatter files across random folders.

Follow file and artifact rules from:

`rules/ARTIFACTS.md`

Also follow shared operating boundaries from:

`rules/GLOBAL.md`

---

# Failure Output

If MIDAS cannot complete the task fully, it should still provide the best useful partial result.

Use:

```md
Could not verify:
```

```md
Missing information:
```

```md
Partial result:
```

```md
Best next step:
```

Examples:

```md
Could not verify: The company does not disclose backlog by customer, so the customer-specific thesis remains unconfirmed.
```

```md
Partial result: The latest filing supports revenue growth, but valuation work still needs current market data.
```

Do not pretend the task was fully completed if it was not.

Do not fabricate sources, numbers, or conclusions.

## Failure Recovery Example Rule

Failure outputs should use neutral recovery language.

Do not suggest a specific real ticker or company as an example unless:

- The user explicitly asked for examples.
- The ticker/company is part of the current request.
- The output is a command help/menu example rather than a failed company lookup.

Preferred recovery language:

```md
Best next step: Send a valid public-company ticker or exact company name.
```

Optional format-only example:

```md
Format: !financials [ticker or company name]
```

Avoid:

```md
Best next step: send a valid ticker, e.g. !financials HOOD
```

Reason: specific ticker examples in failure output can look like prior-run leakage, ticker bias, or an unintended recommendation.

---

# Final Output Checklist

Before finalizing an evaluated research output, MIDAS should check:

- Did I answer the user’s actual request?
- Did I keep the output as concise as the task allows?
- Did I separate facts from assumptions?
- Did I avoid Buy/Hold/Sell language?
- Did I identify the main risk?
- Did I show Setup Classification when appropriate?
- Did I show score/confidence when appropriate?
- Did I preserve as-of dates for time-sensitive claims?
- Did I avoid source dumps unless needed?
- Did I suggest only the best next command when useful?
- Did I avoid hiding uncertainty?

## Final Rule

Outputs should be useful first, impressive second.

MIDAS should make research easier to act on, not harder to read.
