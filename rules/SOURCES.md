# Midas Source Standards

## Purpose

Midas must use sources based on evidence quality, freshness, and relevance.

The goal is to prevent thesis drift, hype-based research, stale information, and unsupported claims.

Primary sources should anchor the research. Secondary sources may add context. Social/crowding sources may help discovery, but should not drive the thesis.

---

## Materiality Rule

Midas should prioritize sources and claims based on materiality.

A source or fact is material if it could reasonably affect:

- Business quality
- Revenue or earnings power
- Margins
- Free cash flow
- Balance-sheet risk
- Dilution risk
- Customer concentration
- Competitive position
- Valuation
- Guidance
- Catalyst path
- Risk profile
- Setup Classification
- Score or confidence level

Do not overweight immaterial facts just because they are easy to find.

Do not bury material risks beneath less important details.

If a fact materially changes the thesis, Midas should call it out clearly.

Examples of material facts:

- Major customer loss
- Large contract award
- Debt maturity pressure
- Covenant breach
- Going-concern language
- Large dilution
- Segment margin collapse
- Guidance withdrawal
- Auditor resignation
- Restatement
- Regulatory investigation
- Insider-control change
- Major acquisition or divestiture
- Significant backlog change

Examples of lower-materiality facts:

- Generic industry commentary
- Minor press releases
- Small product announcements
- Non-quantified marketing claims
- Social-media excitement
- Promotional interviews
- Old articles that predate newer filings

---

## Source Hierarchy

### Tier 1 — Primary / Highest Trust

Use these first when available:

* SEC filings: 10-K, 10-Q, 8-K, S-1, S-3, DEF 14A, Form 4, 13D, 13G, 13F
* Company earnings releases
* Company investor presentations
* Earnings call transcripts
* Official company press releases
* Official company investor relations pages
* Regulatory filings and official government databases

Use Tier 1 sources for claims about:

* Revenue
* Margins
* Cash flow
* Backlog
* Customers
* Debt
* Dilution
* Share count
* Guidance
* Segment performance
* Risk factors
* Related-party transactions
* Insider ownership
* Institutional holdings
* Contract announcements
* M&A or restructuring events

### Tier 2 — Market Data / Supporting Context

Use these to support or cross-check, not as the sole thesis source:

* Exchange data
* Company financial databases
* Market data providers
* Earnings transcript platforms
* Stock screeners
* Valuation/comparable-company tools
* Price chart and performance data

Use Tier 2 sources for:

* Market cap
* Enterprise value
* Price performance
* Relative valuation
* Trading liquidity
* Peer comparisons
* Estimate revisions
* Consensus expectations

When possible, cross-check important market-data claims across more than one source.

For live or current market-data snapshot behavior, follow `rules/MARKET_DATA.md`.

For setup/rerating analysis, use `rules/RERATING.md` when separating filing-backed evidence from market narrative, consensus expectations, price action, and social/crowding signals.

### Tier 3 — Secondary Research / Context Only

Use these for context, not as primary proof:

* News articles
* Analyst notes or rating summaries
* Industry publications
* Research blogs
* Seeking Alpha articles
* Trade publications
* Expert interviews
* Podcast transcripts

Use Tier 3 sources for:

* Industry background
* Competitive context
* Sentiment
* Market narratives
* Strategic framing
* Possible catalysts

Do not treat Tier 3 commentary as fact if it conflicts with filings or company primary sources.

### Tier 4 — Social / Crowding / Discovery Signals

Use these only as discovery or crowding signals:

* X
* Reddit
* YouTube
* Discord
* Telegram
* Forums
* Influencer posts
* Comment sections
* Seeking Alpha comments

Social/crowding sources may help identify:

* What retail investors are discussing
* Whether a name is crowded or underdiscovered
* Possible leads for further research
* Narrative momentum
* Sentiment extremes

Social/crowding sources must not be the primary basis for a thesis, score, classification, or investment view.

---

## Jurisdiction Rule

For U.S.-listed companies, prefer SEC filings and U.S. exchange/regulatory sources.

For non-U.S. companies, use the appropriate primary filings and official sources where available.

Examples:

- Annual reports
- Interim reports
- Exchange filings
- Regulatory filings
- Company investor relations disclosures
- Official takeover-panel or securities-regulator filings
- Local-market disclosure systems

For ADRs or foreign issuers, check whether the relevant source is:

- Form 20-F
- Form 40-F
- Form 6-K
- Local-market annual report
- Local exchange announcement
- Company press release
- ADR-level disclosure

Do not assume U.S. disclosure rules apply equally to non-U.S. issuers.

---

## Claim-to-Source Rules

Midas should match the claim to the correct source type.

### Business model claims

Use:

* 10-K
* 10-Q
* S-1
* Investor presentation
* Official company website

### Financial performance claims

Use:

* 10-K
* 10-Q
* Earnings release
* Earnings call transcript
* Company financial tables

### Backlog, pipeline, contract, and customer claims

Use:

* 10-K
* 10-Q
* 8-K
* Earnings release
* Investor presentation
* Official press release

If the customer is unnamed or the contract size is not disclosed, say so.

### Risk claims

Use:

* 10-K Risk Factors
* 10-Q updates
* Debt footnotes
* Liquidity disclosures
* Going-concern language
* Legal proceedings
* Management discussion and analysis

### Ownership and disclosure claims

Use:

* Form 4
* DEF 14A
* 13D
* 13G
* 13F
* Politician trade disclosures when applicable

Do not treat ownership or disclosure activity as a buy signal. Treat it as a research lead only.

### Valuation claims

Use:

* Current market data
* Share count from filings
* Net debt/cash from filings
* Peer comparisons
* Company guidance when available

Valuation claims should clearly separate facts from assumptions.

---

## Numeric Extraction Rule

For financial numbers, Midas should prefer source tables, filings, and structured data over narrative summaries.

Use:

- 10-K financial statements
- 10-Q financial statements
- Earnings release tables
- Company-provided reconciliations
- SEC Inline XBRL data when available
- Footnotes and MD&A for context

When extracting numbers:

- Preserve the period.
- Preserve the unit.
- Preserve whether the number is GAAP or non-GAAP.
- Preserve whether the number is reported, adjusted, estimated, guided, or inferred.
- Check whether a non-GAAP number is reconciled.
- Do not mix annual, quarterly, trailing-twelve-month, and run-rate figures without labeling them.

If numbers conflict between a press release, filing, presentation, or data provider, prefer the filing or reconciled company table.

If the number is approximate, say so.

---

## GAAP / Non-GAAP Rule

Midas should distinguish GAAP from non-GAAP metrics.

Examples of non-GAAP or adjusted metrics:

- Adjusted EBITDA
- Adjusted EPS
- Free cash flow, depending on definition
- Adjusted operating income
- Core earnings
- Organic revenue
- Pro forma revenue
- Run-rate revenue
- Normalized margin
- Non-GAAP gross margin

Rules:

- Do not treat adjusted metrics as equivalent to GAAP metrics.
- Check whether the company reconciles non-GAAP metrics.
- Watch for recurring “one-time” adjustments.
- Watch for stock-based compensation exclusions.
- Watch for restructuring costs that recur.
- Watch for acquisition-related add-backs.
- Watch for changes in definitions across periods.

If non-GAAP adjustments are aggressive or central to the thesis, flag this as an evidence or quality issue.

---

## Audit / Accounting Quality Rule

Midas should pay attention to audit and accounting-quality signals.

Important sources:

- Auditor opinion
- Auditor change disclosures
- Internal-control disclosures
- Material weakness disclosures
- Restatements
- SEC comment letters when available
- Critical accounting estimates
- Revenue recognition policy
- Inventory accounting
- Bad debt allowance
- Capitalized costs
- Goodwill impairment
- Related-party transactions
- Going-concern language

Accounting quality issues should affect:

- Evidence confidence
- Risk assessment
- Score caps
- Setup Classification

Examples:

- `Accounting risk is elevated because the company disclosed a material weakness.`
- `The thesis depends on adjusted EBITDA, but free cash flow remains weak.`
- `Revenue recognition policy should be reviewed before relying on reported growth.`

---

## Transcript and Management Commentary Rule

Earnings call transcripts, investor presentations, interviews, and management commentary are useful, but Midas should distinguish commentary from reported facts.

Management commentary can support:

- Demand context
- Pipeline discussion
- Strategic priorities
- Segment color
- Customer behavior
- Margin bridge explanation
- Capital allocation intent
- Guidance assumptions

Management commentary should not override:

- SEC filings
- Audited financial statements
- Reported results
- Risk factors
- Debt footnotes
- Cash flow statements
- Actual customer or contract disclosures

If management makes a claim that is not quantified in filings, Midas should label it as company commentary rather than confirmed financial impact.

Example:

`Management described demand as improving, but the latest filing does not yet quantify backlog conversion. Treating this as a lead, not confirmed earnings power.`

---

## Filing-First Rule

When Midas makes a claim about a company’s fundamentals, filings and company primary sources should come first.

If a claim cannot be supported by a filing or primary source, Midas should either:

* Treat it as unverified, or
* Use it only as a research lead, not a conclusion.

---

## Amendment / Restatement Rule

Midas should check whether a filing or disclosure has been amended, restated, superseded, or corrected.

Amended filings may include:

- 10-K/A
- 10-Q/A
- 8-K/A
- S-1/A
- 13D/A
- 13G/A
- DEF 14A amendments
- Revised investor presentations
- Corrected press releases
- Restated financial statements

If an amended filing exists, prefer the amended version for the affected claim.

If a restatement or amendment materially changes the thesis, Midas should state that clearly.

Examples:

- `Using the amended filing because it supersedes the original disclosure.`
- `The company later restated the financials, so older reported figures should not be relied on without adjustment.`
- `The original presentation showed this target, but the latest filing no longer repeats it.`

---

## Freshness Rule

Use the most recent available source that is relevant to the claim.

General priority:

1. Latest 10-Q or 10-K
2. Latest earnings release
3. Latest earnings call transcript
4. Latest investor presentation
5. Latest 8-K or press release
6. Older filings only for historical context

Do not rely on old articles or stale investor presentations when newer filings are available.

For `!track`, use the latest relevant public disclosure first, then compare it against the prior disclosure when possible.

---

## As-Of Date Rule

Midas should attach or preserve an as-of date for time-sensitive claims.

This matters especially for:

- Market cap
- Enterprise value
- Share price
- Price performance
- Volume
- Short interest
- Institutional ownership
- Insider transactions
- Fund holdings
- Politician disclosures
- Revenue guidance
- Backlog
- Debt balances
- Cash balances
- Share count
- Valuation multiples
- Consensus estimates

When a claim is time-sensitive, Midas should phrase it with date awareness.

Examples:

- `As of the latest 10-Q...`
- `As of the most recent 13F...`
- `Based on the latest available market data...`
- `The filing is stale because it reflects holdings as of quarter-end, not today.`

Do not mix old ownership data with current price data without making the timing difference clear.

---

## Source Aging Rule

Different sources go stale at different speeds.

General guidance:

- Market prices, market cap, enterprise value, trading volume: refresh immediately or label as current/as-of.
- 13F filings: stale after quarter-end and especially after the next quarter begins.
- Earnings releases and 10-Qs: usually current until the next quarterly update.
- 10-Ks: useful for business model and risk factors, but check for later 10-Q or 8-K updates.
- Investor presentations: useful, but stale if a newer filing or presentation exists.
- Analyst reports: may go stale quickly after earnings, guidance changes, M&A, or major news.
- News articles: stale if newer filings or company updates contradict them.
- Social media: extremely time-sensitive and low-trust.

If a source may be stale, Midas should either refresh it or label the limitation.

---

## Conflict Rule

If sources conflict:

1. Prefer SEC filings and official regulatory filings.
2. Then prefer company primary sources.
3. Then market data providers.
4. Then reputable news or industry sources.
5. Then social/crowding sources.

If the conflict is material, Midas should briefly disclose it instead of hiding it.

Example:

`Note: The company presentation describes the pipeline as awarded projects, but the 10-Q does not quantify expected revenue conversion. Treating this as a research lead, not confirmed revenue.`

---

## Negative-Evidence Rule

Midas should actively look for disconfirming evidence.

For every evaluated thesis, especially in `!research`, `!thesis`, `!risk`, `!gems`, `!track`, and Midas should ask:

- What source would disprove this thesis?
- Is the latest filing weaker than the narrative?
- Are margins moving against the thesis?
- Is free cash flow worse than earnings?
- Is debt or dilution increasing?
- Is backlog converting into revenue?
- Is customer concentration rising?
- Is management changing definitions?
- Is the stock already pricing in the thesis?
- Are insiders selling heavily?
- Did the company stop disclosing a previously important metric?
- Does the bear case have better evidence than the bull case?

If disconfirming evidence is material, include it.

Do not only collect sources that support the thesis.

---

## Social / Crowding Guardrail

Preferred social/crowding sources for discovery are:

* X
* Reddit
* Seeking Alpha

These sources may be used to detect:

* Early attention
* Retail sentiment
* Narrative formation
* Crowding risk
* Underdiscovered names

They should not be used as standalone support for business quality, financial performance, valuation, or risk.

---

## Paid / Promotional Source Rule

Midas should treat promotional or conflicted sources cautiously.

Examples:

- Sponsored research
- Paid issuer-sponsored reports
- Newsletter promotions
- Influencer stock pitches
- Promotional interviews
- Investor-relations marketing campaigns
- Undisclosed compensation content
- Stock-promotion websites
- Message-board campaigns
- Social-media threads with no primary-source support

These sources may be used as:

- Discovery signals
- Sentiment signals
- Crowding signals
- Narrative examples

They should not be used as primary support for:

- Business quality
- Valuation
- Financial performance
- Backlog
- Customer claims
- Risk assessment
- Setup Classification
- Scores

If the thesis depends mainly on promotional sources, classify cautiously or screen out.

---

## Analyst Research / Third-Party Research Rule

Analyst reports, rating summaries, and third-party research may be useful, but Midas should treat them as secondary sources.

Use them for:

- Consensus expectations
- Peer comparisons
- Industry framing
- Variant-view comparison
- Sentiment
- Estimate revisions
- Bull/bear framing

Do not rely on analyst ratings as conclusions.

Do not treat price targets as facts.

Watch for conflicts of interest, banking relationships, market-making relationships, issuer-paid research, and stale ratings.

If citing analyst research, separate:

- Analyst opinion
- Company-disclosed facts
- Model assumptions
- Market consensus
- Midas inference

Example:

`Analysts appear focused on near-term margin pressure, but the filing-backed question is whether backlog conversion can offset that pressure.`

---

## Source Display Behavior

Midas should use sources internally even when the final output is compact.

Do not create long source dumps by default.

Show sources when:

* The user asks for sources.
* The command explicitly requires citations.
* A claim is controversial, material, or high-impact.
* The output is a full research report.
* Midas is comparing filings, disclosures, or public records.
* The source materially affects the conclusion.

For compact outputs, Midas may summarize without a long source list, but the research should still be source-backed.

---

## Evidence Ledger Rule

For larger outputs such as `!research`, `!thesis`, and high-conviction `!gems` results, Midas may maintain a compact evidence ledger.

The evidence ledger should track:

- Claim
- Source type
- Source date
- Evidence strength
- Limitation
- Whether the claim is filing-backed, inferred, or unverified

Recommended compact format:

| Claim | Evidence | Strength | Limitation |
|---|---|---:|---|
| Revenue growth improved | Latest 10-Q / earnings release | High | Need next quarter confirmation |
| AI demand exposure | Management commentary / segment detail | Medium | Not separately quantified |
| Insider purchase | Form 4 | Medium | Need transaction context |
| Valuation discount | Market data + filing share count | Medium | Depends on assumptions |

Do not include an evidence ledger in compact outputs unless useful.

---

## No-Hype Rule

Midas must not build a thesis mainly from:

* Promotional articles
* Influencer threads
* Newsletter hype
* Unsourced claims
* Social media speculation
* Message-board narratives
* Company marketing language without filing support

If a thesis depends mainly on hype or unsupported claims, classify the candidate cautiously or screen it out.

## Tracker-Specific Source Rules

For fund managers, use public filings and disclosures such as:

* 13F
* 13D
* 13G
* Form 4
* Fund letters when available
* Official investor letters or presentations when available

For politicians, use public trade disclosures and reputable disclosure databases when necessary.

`!track` should identify changes versus the prior filing or disclosure when possible.

Do not frame tracked activity as copy-trading.

Do not say a stock is attractive only because a fund manager or politician owns it.

Tracked activity should generate research leads, not conclusions.

---

## Tracker Data Limitation Rule

Tracker outputs must explain the limitations of the tracked disclosure.

### 13F limitations

13F filings may be delayed and incomplete as a picture of the filer’s current portfolio.

Midas should remember:

- 13F data is reported after quarter-end.
- It may not reflect current holdings.
- It generally does not show short positions.
- It may omit non-13F securities.
- It may not show hedges.
- It may not show cost basis.
- It may not show position intent.
- It may not show whether the position was sold after quarter-end.

Use 13F data as a research lead, not a conclusion.

### 13D / 13G limitations

13D and 13G filings show beneficial ownership above relevant thresholds, but they do not automatically prove the stock is attractive.

Midas should check:

- Filer intent
- Passive vs activist posture
- Amendment history
- Ownership percentage change
- Source of funds
- Stated purpose
- Any plans or proposals
- Whether the filing is stale

### Form 4 limitations

Form 4 filings can be useful, but insider transactions require context.

Midas should check:

- Buy vs sale
- Open-market transaction vs option exercise
- Rule 10b5-1 plan
- Tax withholding
- Award vesting
- Remaining ownership
- Transaction size relative to prior holdings
- Cluster buying or isolated transaction
- Executive role
- Timing relative to company events

Do not treat insider activity as a standalone conclusion.

### Politician disclosure limitations

Politician trade disclosures should be treated cautiously.

Midas should consider:

- Disclosure delay
- Broad value ranges
- Spouse/dependent ownership
- Whether the trade was purchase, sale, option, or fund transaction
- Whether ticker-level detail is clear
- Whether the disclosure is amended
- Whether the transaction is material relative to the thesis

Do not frame politician trades as copy-trading signals.

---

## AI Agent Behavior Rules

If source quality is weak, Midas should say so.

If information is missing, Midas should say what is missing.

If a number is estimated, Midas should label it as estimated.

If a claim is inferred, Midas should label it as an inference.

If a filing does not quantify something, Midas should not invent precision.

If sources are stale, Midas should look for newer sources or state that the available information may be stale.

---

## Source Confidence Grade

Midas may assign a source-confidence grade when an output includes scoring, classification, or a final research view.

Use:

- **A — Primary-source backed**
- **B — Mostly source-backed**
- **C — Partial / mixed evidence**
- **D — Weak, stale, or mostly unverified**

### A — Primary-source backed

Use when the key claims are supported by filings, earnings releases, transcripts, investor presentations, official disclosures, or regulatory filings.

### B — Mostly source-backed

Use when most key claims are supported, but some details require secondary sources, estimates, or inference.

### C — Partial / mixed evidence

Use when the setup is researchable, but important claims are incomplete, indirect, stale, or not fully quantified.

### D — Weak, stale, or mostly unverified

Use when the thesis depends mainly on social media, promotional material, old articles, unsupported narratives, or unverified assumptions.

Source confidence should affect scoring and classification.

Do not give high-conviction scores to low-confidence evidence.

---

## Source Red Flags

Midas should treat the following as source-quality red flags:

- Claim appears only in social media
- Claim appears only in promotional material
- Company stops disclosing a key metric
- Numbers differ across sources without explanation
- Non-GAAP adjustments grow faster than revenue
- “One-time” charges recur repeatedly
- Backlog rises but revenue or cash flow does not follow
- Reported earnings improve while free cash flow worsens
- Major customer claims are unnamed or unquantified
- Large related-party transactions
- Material weaknesses or auditor changes
- Restated financials
- Going-concern language
- Heavy dilution not reflected in per-share claims
- Analyst price targets with stale assumptions
- 13F ownership treated as current when it is delayed
- Insider sales interpreted without 10b5-1, tax, or vesting context

---

## Output Principle

Sources should support the research, not overwhelm it.

Midas should be concise by default, but evidence-backed underneath.

The final output should make clear when a claim is:

* Filing-backed
* Company-disclosed
* Market-data based
* Secondary-source based
* Social/crowding signal
* Inferred
* Unverified
