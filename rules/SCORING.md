# MIDAS Scoring Standards

## Purpose

MIDAS scoring is used to prioritize research, compare candidates, and support setup classification.

Scores are not investment recommendations.

Scores should help answer:

- Is this worth researching further?
- What kind of setup is this?
- What is strong?
- What is weak?
- What evidence supports the view?
- What could break the thesis?
- Is the market already pricing in the thesis?

Scoring should not replace judgment, source review, valuation work, or risk review.

## Architecture Overview

MIDAS uses a four-layer scoring architecture:

1. **Global Research Score**
   - A broad 100-point score that can work across most public-company research.

2. **Setup Overlay Score**
   - Optional smaller scores for specific workflows such as hidden gems, tracker leads, turnarounds, deep value, or special situations.

3. **Evidence Confidence Grade**
   - A separate confidence grade based on source quality, freshness, and verification.

4. **Score Caps / Gates**
   - Rules that prevent weak, hype-driven, fragile, or poorly sourced ideas from scoring too high.

Scoring should connect to:

`/home/jordan/.hermes/profiles/midas/rules/CLASSIFICATIONS.md`

Scoring must follow:

`/home/jordan/.hermes/profiles/midas/rules/SOURCES.md`

---

# 1. Global Research Score

Use the Global Research Score when MIDAS gives a final research view on a stock.

Total score: **100 points**

The score has eight pillars:

1. Business Quality / Economics — 15 points
2. Competitive Position / Moat — 15 points
3. Financial Strength / Cash Conversion — 10 points
4. Management / Capital Allocation / Governance — 10 points
5. Reinvestment Runway / Growth Quality — 10 points
6. Valuation / Margin of Safety — 15 points
7. Variant View / Information Gap / Catalyst Path — 15 points
8. Risk / Fragility / Downside Protection — 10 points

Higher score = stronger research setup.

A high score does not mean Buy.

A low score does not always mean the company is bad. It may mean the setup is not attractive, not differentiated, too fragile, too expensive, too discovered, or not supported by enough evidence.

---

## Pillar 1: Business Quality / Economics — 15 points

Measures whether the company is a real, durable, economically attractive operating business.

Consider:

- Revenue quality
- Recurring or repeat demand
- Profitability
- Gross margin / operating margin profile
- Free cash flow generation
- Return on invested capital
- Return on equity
- Unit economics
- Cash conversion
- Customer demand
- Backlog or contract validation
- Segment quality
- Cyclicality of core business
- Simplicity and understandability

Scoring guide:

- **13–15** — High-quality business with strong economics, durable demand, attractive returns, and clear operating validation.
- **10–12** — Good business with real validation, but some cyclicality, margin limits, or missing detail.
- **7–9** — Mixed quality; real business, but economics are average, volatile, or not yet proven.
- **4–6** — Weak or early-stage business with limited proof of durable economics.
- **0–3** — Little to no credible business quality validation.

---

## Pillar 2: Competitive Position / Moat — 15 points

Measures whether the company has a defensible position.

Consider:

- Sustainable competitive advantage
- Barriers to entry
- Pricing power
- Switching costs
- Network effects
- Scale advantages
- Cost advantage
- Brand strength
- Regulatory or licensing advantage
- Customer relationships
- Intellectual property
- Differentiation
- Industry structure
- Competitive intensity
- Threat of disruption

Scoring guide:

- **13–15** — Strong moat or durable competitive position with evidence of pricing power, barriers, or structural advantage.
- **10–12** — Good competitive position, but moat is narrower or less proven.
- **7–9** — Some differentiation, but competition could pressure returns.
- **4–6** — Weak competitive advantage or highly competitive market.
- **0–3** — No clear moat or defensibility.

---

## Pillar 3: Financial Strength / Cash Conversion — 10 points

Measures whether the company has the financial durability to survive and execute.

Consider:

- Balance sheet strength
- Net debt / leverage
- Liquidity
- Interest coverage
- Free cash flow
- Working capital needs
- Capital intensity
- Dilution risk
- Debt maturity schedule
- Ability to self-fund growth
- Cash burn
- Accounting quality
- Earnings quality

Scoring guide:

- **9–10** — Strong balance sheet, good liquidity, strong cash conversion, low financial fragility.
- **7–8** — Manageable balance sheet and cash profile.
- **5–6** — Some financial pressure, but not immediately thesis-breaking.
- **3–4** — High leverage, weak liquidity, poor cash conversion, or dilution risk.
- **0–2** — Severe solvency, liquidity, or financing risk.

---

## Pillar 4: Management / Capital Allocation / Governance — 10 points

Measures whether leadership appears capable, aligned, and disciplined.

Consider:

- Track record
- Capital allocation history
- Reinvestment discipline
- M&A discipline
- Share repurchases / dilution history
- Insider ownership
- Incentive alignment
- Governance quality
- Transparency
- Related-party transactions
- Credibility of guidance
- Willingness to communicate risks clearly
- Shareholder friendliness
- Operational execution

Scoring guide:

- **9–10** — Strong management, aligned incentives, good governance, disciplined capital allocation.
- **7–8** — Generally credible management with some limitations.
- **5–6** — Mixed record or limited evidence.
- **3–4** — Questionable execution, weak alignment, or capital allocation concerns.
- **0–2** — Serious governance, credibility, dilution, or related-party concerns.

---

## Pillar 5: Reinvestment Runway / Growth Quality — 10 points

Measures whether growth can create value rather than consume capital.

Consider:

- Addressable market
- Organic growth runway
- Incremental returns on capital
- Return on incremental invested capital
- Ability to reinvest free cash flow
- Operating leverage
- Margin expansion potential
- Durable demand drivers
- Backlog conversion
- New product/service adoption
- Growth funded internally vs externally
- Whether growth improves or weakens economics

Scoring guide:

- **9–10** — Long runway with attractive incremental returns and evidence that growth creates value.
- **7–8** — Good growth runway, but some uncertainty around reinvestment returns.
- **5–6** — Growth exists, but quality or capital intensity is mixed.
- **3–4** — Growth is low-quality, expensive, cyclical, or dependent on external financing.
- **0–2** — No clear growth runway or growth appears value-destructive.

---

## Pillar 6: Valuation / Margin of Safety — 15 points

Measures the relationship between price and value.

Consider:

- Intrinsic value estimate
- Price versus fair value
- Free cash flow yield
- Earnings yield
- EV/EBITDA
- EV/EBIT
- EV/Sales when appropriate
- Price/book or NAV where appropriate
- Replacement value / liquidation value where appropriate
- Sum-of-the-parts value
- Peer valuation
- Historical valuation range
- Margin of safety
- Valuation versus growth and risk
- Whether the stock already prices in the thesis

Scoring guide:

- **13–15** — Clear valuation support, meaningful margin of safety, or strong price-versus-value gap.
- **10–12** — Reasonable valuation with some upside support.
- **7–9** — Fair valuation; upside depends on execution or rerating.
- **4–6** — Expensive, thin margin of safety, or valuation hard to justify.
- **0–3** — No credible valuation support or obvious overvaluation.

Important:

Valuation should be matched to the business type.

Use present-value/DCF logic when cash flows are forecastable.

Use multiples when peers are relevant.

Use asset/NAV methods for asset-heavy, financial, real estate, holding company, or deep-value situations.

Use sum-of-the-parts when segments have materially different economics.

Do not force one valuation method onto every company.

---

## Pillar 7: Variant View / Information Gap / Catalyst Path — 15 points

Measures whether there is a credible reason the market may be missing something.

Consider:

- Non-consensus insight
- Filing detail not reflected in narrative
- Misunderstood segment
- Hidden asset
- Margin inflection
- Backlog conversion
- Delayed financial impact
- Underappreciated operating leverage
- Balance sheet repair
- Management change
- Industry transition
- Special situation
- Temporary controversy
- Crowd pessimism or neglect
- Clear catalyst path
- Rerating mechanism
- Evidence that expectations are too low

Scoring guide:

- **13–15** — Strong, evidence-backed variant view with a clear reason the market may be wrong.
- **10–12** — Credible information gap or catalyst path, but some uncertainty.
- **7–9** — Possible gap, but not clearly differentiated.
- **4–6** — Weak, obvious, or mostly narrative-driven gap.
- **0–3** — No real information gap or catalyst path.

Important:

This pillar should not reward hype.

A real variant view should be researchable, evidence-backed, and connected to future fundamentals, valuation, or risk perception.

---

## Pillar 8: Risk / Fragility / Downside Protection — 10 points

Measures how easily the thesis can break.

Consider:

- Customer concentration
- Supplier concentration
- Key-person risk
- Execution risk
- Regulatory risk
- Commodity risk
- Cyclicality
- Technology disruption
- Litigation risk
- Accounting risk
- Liquidity risk
- Financing risk
- Margin pressure
- Valuation risk
- Permanent capital impairment risk
- Downside scenario
- Whether the balance sheet gives the company time

Higher score = lower fragility.

Scoring guide:

- **9–10** — Risks are manageable, survivable, and unlikely to break the thesis quickly.
- **7–8** — Meaningful risks, but company has enough durability and evidence support.
- **5–6** — Risk is material and must be monitored.
- **3–4** — Fragile setup; several risks could break the thesis.
- **0–2** — Thesis is structurally fragile, unresearchable, or highly vulnerable to permanent impairment.

---

# 2. Evidence Confidence Grade

Every scored output should include an evidence confidence grade.

This is separate from the numeric score.

Use:

- **A — Primary-source backed**
- **B — Mostly source-backed**
- **C — Partial / mixed evidence**
- **D — Weak, stale, or mostly unverified**

## A — Primary-source backed

Use when the thesis is supported by:

- SEC filings
- Company filings
- Earnings releases
- Earnings call transcripts
- Investor presentations
- Official company press releases
- Regulatory filings
- Public disclosure documents

## B — Mostly source-backed

Use when most key claims are supported, but some details rely on secondary sources, estimates, or inference.

## C — Partial / mixed evidence

Use when the company is researchable, but important claims are incomplete, indirect, stale, or not fully quantified.

## D — Weak, stale, or mostly unverified

Use when the thesis depends mainly on social media, promotional material, old articles, unsupported narratives, or unverified assumptions.

Evidence confidence should affect score caps.

Do not give a high conviction score to a low evidence idea.

---

# 3. Score Interpretation

Use this guide for the Global Research Score:

- **85–100** — Exceptional research candidate
- **75–84** — Strong research candidate
- **65–74** — Researchable / watchlist candidate
- **50–64** — Incomplete, speculative, or needs more diligence
- **Below 50** — Weak setup / likely screened out

These ranges are guidance, not automatic conclusions.

Classification still requires judgment.

A company can be high quality but not a good setup if valuation is stretched or the idea is already well discovered.

A company can be speculative but still researchable if the information gap is strong and the risks are clearly labeled.

---

# 4. Setup Overlay Scores

Use setup overlays when a command needs a specialized score.

Setup overlays should not replace the Global Research Score.

They should answer a narrower question.

Examples:

- Hidden-Gem Overlay
- Tracker Lead Overlay
- Deep Value Overlay
- Turnaround Overlay
- Special Situation Overlay
- Quality Compounder Overlay

A command may use:

- Global Research Score only
- Setup Overlay only
- Both, when useful

Keep overlays concise.

---

## Hidden-Gem Overlay Score

Use for:

- `!gems`
- underdiscovered screens
- small/mid-cap discovery
- thematic hidden-gem searches
- tracker leads that may be overlooked

Total score: **25 points**

Five buckets, 0–5 each:

1. Business Quality / Validation
2. Underdiscovered / Non-Consensus Status
3. Information Gap / Mispricing Driver
4. Valuation / Rerating Setup
5. Risk / Fragility / Evidence Quality

### 1. Business Quality / Validation

Measures whether the company is real, operating, and supported by evidence.

Score high for revenue, customers, contracts, backlog, profitability, free cash flow, operating progress, filing-backed demand, and credible execution.

### 2. Underdiscovered / Non-Consensus Status

Measures whether the company is overlooked, niche, boring, small/mid-cap, less followed than peers, or outside the obvious consensus trade.

Do not give full credit to names already widely discussed, heavily promoted, or crowded.

### 3. Information Gap / Mispricing Driver

Measures whether there is a credible reason the market may be missing something.

Examples:

- Misunderstood segment
- Hidden asset
- Backlog conversion
- Margin inflection
- Delayed financial impact
- Industry transition
- New demand driver
- Misread risk profile
- Temporary controversy
- Filing detail not reflected in narrative

### 4. Valuation / Rerating Setup

Measures whether the stock still has a clean setup.

Consider:

- Price versus value
- Margin of safety
- Rerating stage
- Recent vertical move
- Consolidation
- Valuation reset
- Whether thesis is already priced in
- Whether price action is disconnected from fundamentals

### 5. Risk / Fragility / Evidence Quality

Measures how easily the thesis can break and whether the evidence is strong enough.

Higher score = lower fragility and stronger evidence.

---

## Hidden-Gem Overlay Interpretation

- **21–25** — Exceptional hidden-gem candidate
- **18–20** — Strong hidden-gem candidate
- **15–17** — Researchable / watchlist candidate
- **12–14** — Speculative or incomplete setup
- **Below 12** — Weak hidden-gem setup / likely screened out

---

## Tracker Lead Overlay Score

Use for:

- `!track`
- 13F/13D/13G/Form 4 tracking
- politician trade disclosures
- fund manager disclosure changes
- insider or institutional research leads

Total score: **25 points**

Five buckets, 0–5 each:

1. Disclosure Signal Quality
2. Business / Thesis Quality
3. Change Significance
4. Research Gap / Underfollowed Angle
5. Risk / Crowding / Copy-Trading Fragility

Important:

Tracked activity is a research lead, not a buy/sell signal.

Do not score a stock highly only because a famous investor, fund, insider, or politician owns it.

---

## Deep Value Overlay Score

Use when a setup is primarily valuation-driven.

Total score: **25 points**

Five buckets, 0–5 each:

1. Asset / Earnings Power Support
2. Balance Sheet Survivability
3. Discount to Intrinsic Value / NAV / Liquidation Value
4. Catalyst or Mean-Reversion Path
5. Value Trap Risk

Higher score = stronger deep value setup.

Do not label something deep value just because the stock is down.

---

## Turnaround Overlay Score

Use when a company may be improving after a weak period.

Total score: **25 points**

Five buckets, 0–5 each:

1. Evidence of Stabilization
2. Margin / Cash Flow Inflection
3. Balance Sheet Repair
4. Management Execution / Operational Fix
5. Downside Survivability

Higher score = stronger turnaround setup.

Do not score hope as evidence.

---

## Special Situation Overlay Score

Use when the thesis depends on a specific event.

Total score: **25 points**

Five buckets, 0–5 each:

1. Catalyst Specificity
2. Probability / Evidence Support
3. Value Creation Potential
4. Timing / Path Clarity
5. Deal / Legal / Regulatory / Financing Risk

Higher score = stronger special situation setup.

Do not use this overlay unless the catalyst is specific enough to research.

---

## Quality Compounder Overlay Score

Use when the company is high quality but may not be hidden.

Total score: **25 points**

Five buckets, 0–5 each:

1. Durable Business Quality
2. Moat / Competitive Advantage
3. Reinvestment Runway
4. Management / Capital Allocation
5. Valuation Discipline

Higher score = stronger compounder setup.

A strong compounder can still be too expensive or too well-discovered.

---

# 5. Score Caps and Gates

Use caps to keep scores honest.

Caps are judgment tools, not mechanical rules.

Explain briefly when a cap affects the score.

## Evidence Caps

- If there is no primary-source support, Global Research Score should usually be capped at **70**.
- If the thesis is mostly social-media driven, Global Research Score should usually be capped at **55**.
- If key claims are unverified, use Evidence Confidence Grade C or D.
- If sources are stale, reduce confidence and consider a cap.

## Business Quality Caps

- If business validation is weak, Global Research Score should usually be capped at **65**.
- If the company has no clear revenue, customer, product, or operating proof, cap at **55** unless the command is explicitly screening early-stage/speculative setups.

## Valuation Caps

- If valuation support is missing or impossible to frame, Global Research Score should usually be capped at **75**.
- If valuation appears stretched and the thesis is already consensus, cap at **70**.
- If the setup depends entirely on multiple expansion, cap unless there is strong evidence of fundamental value growth.

## Rerating Caps

- If the stock has already had a vertical move with no consolidation, cap the Hidden-Gem Overlay at **17/25**.
- If the stock is post-rerate and valuation support is thin, classify cautiously.
- A strong company can still be a poor setup after a major rerating.

## Fragility Caps

- If the company has severe liquidity, solvency, or dilution risk, Global Research Score should usually be capped at **60** unless the command is explicitly focused on distressed or special situations.
- If one customer, one contract, one regulatory event, or one financing event can break the thesis, cap the relevant score and label fragility clearly.

## Crowding / Discovery Caps

- If the company is widely followed and already a consensus winner, the Hidden-Gem Overlay’s Underdiscovered bucket should usually be capped at **2/5**.
- If the thesis is already heavily promoted on social media, reduce Underdiscovered and Information Gap scores.

---

# 6. Relationship to Setup Classification

Scoring should inform Setup Classification, not mechanically dictate it.

Use:

`/home/jordan/.hermes/profiles/midas/rules/CLASSIFICATIONS.md`

Examples:

- High Global Score + strong hidden-gem overlay → Prime Hidden-Gem Candidate
- Strong business + high quality score + widely discovered → Quality Compounder, Not Hidden
- Good company + stretched valuation or post-rerate setup → Watchlist / Awaiting Pullback
- High upside + weak balance sheet or concentration risk → Speculative / High-Fragility Candidate
- Strong asset/earnings support + pessimistic pricing → Deep Value / Mispricing Candidate
- Improving fundamentals after weak period → Turnaround / Inflection Candidate
- Specific event-driven setup → Special Situation Candidate
- Weak evidence, poor quality, excessive fragility, or no researchable gap → Screened Out

Do not let the score alone override classification judgment.

---

# 7. Relationship to RERATING.md

Use `/home/jordan/.hermes/profiles/midas/rules/RERATING.md` when interpreting valuation/rerating setup, variant-view strength, information gap, crowding, and rerating caps.

RERATING.md does not add new scoring buckets, rubrics, caps, or gates; this file remains the authority for MIDAS scoring.

---

# 8. Output Format

When using the Global Research Score, display:

`Global Research Score: X/100`

Then, when helpful:

- Business Quality / Economics: X/15
- Competitive Position / Moat: X/15
- Financial Strength / Cash Conversion: X/10
- Management / Capital Allocation / Governance: X/10
- Reinvestment Runway / Growth Quality: X/10
- Valuation / Margin of Safety: X/15
- Variant View / Information Gap / Catalyst Path: X/15
- Risk / Fragility / Downside Protection: X/10

Also display:

`Evidence Confidence: A/B/C/D`

And when applicable:

`Setup Classification: [Approved Classification]`

For hidden-gem or tracker workflows, optionally include:

`Hidden-Gem Overlay Score: X/25`

or:

`Tracker Lead Overlay Score: X/25`

Keep explanations concise.

Do not over-explain every bucket unless the command requires a full report.

---

# 9. Command Usage

## Commands that commonly use Global Research Score

- `!research`
- `!thesis`
- `!risk`

## Commands that commonly use Setup Overlay Scores

- `!gems`
- `!track`
- special situation workflows
- turnaround workflows
- deep value workflows

## Commands that may omit scoring

- `!financials`
- `!earnings`
- `!updates`

These may omit scoring when they only summarize facts, filings, or raw financial data.

If they produce a final setup view, they may include scoring.

---

# 10. Final Rule

Scoring is a research-prioritization tool.

It is not a recommendation.

A score should help decide what deserves more diligence, not what to buy.
