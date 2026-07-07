# MIDAS Setup Classifications

## Purpose

Setup Classification gives MIDAS a consistent way to describe what type of opportunity or research setup a public company represents.

These labels are research workflow classifications, not investment recommendations.

Do not use Buy/Hold/Sell language.

MIDAS classifications should help answer:

- What kind of setup is this?
- Why is it researchable?
- What style of diligence does it require?
- Is the setup clean, overextended, fragile, or incomplete?
- Should the name be prioritized, watched, or screened out?

## Research Foundation

This classification system is built around common institutional research concepts used by financial research firms, investment managers, and hedge-fund-style investors:

- Business quality
- Competitive advantage / moat
- Free cash flow
- Return on capital
- Balance-sheet strength
- Management quality
- Capital allocation
- Reinvestment runway
- Valuation / margin of safety
- Price versus value
- Information gap / variant view
- Catalyst path
- Risk of permanent impairment
- Fragility
- Evidence quality
- Crowding and rerating stage

MIDAS should not blindly copy any one investor’s framework.

The goal is to create a practical research-classification standard that works across commands and sectors.

## Classification Architecture

MIDAS uses two layers:

1. **Primary Setup Classification**
   - The main type of opportunity or research setup.
   - Use one primary classification unless the output explicitly allows a secondary classification.

2. **Setup Modifiers**
   - Optional tags that describe stage, risk, evidence quality, rerating status, or watchlist condition.
   - Modifiers should clarify the setup without replacing the primary classification.

Example:

`Setup Classification: Quality Compounder`

`Setup Modifiers: Well-Discovered; Awaiting Pullback`

Example:

`Setup Classification: Hidden-Gem Candidate`

`Setup Modifiers: Early Rerating; High-Fragility`

Example:

`Setup Classification: Deep Value / Mispricing Candidate`

`Setup Modifiers: Balance-Sheet Supported; Catalyst Needed`

## When To Use

Use Setup Classification when a command produces an evaluation, ranking, final view, research lead, setup summary, thesis review, risk view, or full research output.

Commands that should commonly use Setup Classification:

- `!gems`
- `!track`
- `!research`
- `!thesis`
- `!risk`

Commands that may omit Setup Classification when they are only summarizing raw data:

- `!financials`
- `!earnings`
- `!updates`

If a command is only presenting facts, filings, updates, or raw financial data without a setup view, classification is optional.

---

# Primary Setup Classifications

## Prime Research Candidate

Use when a stock has a strong overall balance of:

- Business quality
- Evidence-backed validation
- Credible information gap or differentiated angle
- Reasonable valuation or setup discipline
- Survivable risk
- Useful next-step research path

This label should be used selectively.

A company should not receive this classification just because it is interesting, small, cheap, popular, or attached to a strong theme.

A Prime Research Candidate does not mean Buy.

It means MIDAS believes the name deserves prioritized research under the current workflow.

## Hidden-Gem Candidate

Use when a stock appears meaningfully underdiscovered relative to the quality or relevance of the underlying business.

Evidence may include:

- Small/mid-cap or obscure company
- Boring or niche industry
- Low mainstream coverage
- Limited retail attention
- Less obvious beneficiary of a demand driver
- Underappreciated segment, asset, customer base, or backlog
- Filing-backed evidence that is not obvious from the market narrative

This label should be used heavily by `!gems`.

Do not use this label for obvious consensus winners, heavily promoted stocks, or companies already widely associated with the theme.

## Quality Compounder

Use when the company appears to have durable business quality and the ability to compound value over time.

Evidence may include:

- Strong return on capital
- Consistent free cash flow
- Durable margins
- Repeat or recurring demand
- Pricing power
- Competitive advantage
- Low or manageable leverage
- Long reinvestment runway
- Disciplined management
- High-quality capital allocation

A Quality Compounder can still be too expensive, too crowded, or too well-discovered.

Use setup modifiers to clarify that.

Example:

`Setup Classification: Quality Compounder`

`Setup Modifiers: Well-Discovered; Valuation Sensitive`

## Deep Value / Mispricing Candidate

Use when the market appears to be pricing in excessive pessimism relative to the company’s assets, earnings power, cash flow, survivability, or strategic value.

Evidence may include:

- Discount to conservative intrinsic value
- Discount to NAV or asset value
- Discount to liquidation or replacement value
- Earnings power not reflected in current valuation
- Strong balance sheet despite weak market perception
- Temporary controversy or cyclical pressure
- Market narrative that appears more negative than the filing-backed facts

Do not use this label just because a stock is down.

A Deep Value / Mispricing Candidate requires evidence of potential value support.

## Turnaround / Inflection Candidate

Use when a company may be improving after a weak period.

Evidence may include:

- Revenue stabilization
- Margin improvement
- Free cash flow improvement
- Balance-sheet repair
- Cost discipline
- Backlog conversion
- Demand recovery
- Management execution
- Operational restructuring
- Improved guidance
- Better unit economics
- Reduced losses or narrowing cash burn

This label requires signs of improvement.

Do not score hope as evidence.

## Special Situation / Event-Driven Candidate

Use when the setup depends on a specific identifiable event, transaction, or catalyst.

Examples:

- Spin-off
- Asset sale
- Restructuring
- Contract award
- Litigation outcome
- Regulatory decision
- Merger/acquisition
- Bankruptcy emergence
- Strategic review
- Index inclusion
- Major financing event
- Tender offer
- Liquidation
- Capital return event
- Tax, legal, or ownership structure change

The catalyst should be specific enough to research.

Do not use this label for vague “something might happen” speculation.

## Cyclical Recovery Candidate

Use when the setup depends mainly on recovery from a depressed cycle.

Evidence may include:

- Industry downturn nearing normalization
- Order recovery
- Volume recovery
- Pricing stabilization
- Inventory normalization
- End-market recovery
- Operating leverage from trough conditions
- Improved demand indicators
- Balance sheet strong enough to survive the cycle

This classification is distinct from Turnaround / Inflection.

A cyclical recovery may happen because the industry cycle improves, even if management is not executing a dramatic internal fix.

## Tracker Lead Candidate

Use when a name is surfaced primarily through a disclosure, filing, ownership change, insider transaction, 13F, 13D, 13G, Form 4, fund letter, or public trade disclosure.

This classification is mainly for `!track`.

Tracked activity should be treated as:

- A research lead
- A disclosure change
- A clue for diligence
- A possible signal of attention or ownership change

Tracked activity is not a buy/sell signal.

Do not classify a stock as attractive only because a famous investor, politician, insider, or institution owns it.

A Tracker Lead Candidate should usually receive another classification after deeper research.

Example:

`Setup Classification: Tracker Lead Candidate`

`Setup Modifiers: Needs Fundamental Research; Not a Copy-Trade Signal`

## Speculative / High-Fragility Candidate

Use when upside may exist, but the thesis can break easily.

Fragility may come from:

- Customer concentration
- Weak balance sheet
- Dilution risk
- Liquidity risk
- Cash burn
- Execution risk
- Commodity exposure
- Regulatory risk
- Dependence on one catalyst
- Unproven demand
- Very small scale
- Poor governance
- Key-person risk
- Promotional source base
- Missing primary-source support

This label should make fragility clear without automatically dismissing the idea.

A speculative idea can still be researchable if the upside path and risks are clearly labeled.

## Watchlist / Awaiting Better Setup

Use when the company or thesis is interesting, but the current setup is not clean enough to prioritize.

Reasons may include:

- Sharp recent price move
- Overextended valuation
- Lack of consolidation
- Unclear entry discipline
- Evidence still incomplete
- Catalyst timing unclear
- Market already pricing in part of the thesis
- Need for another filing or earnings update
- Risk/reward not yet clear enough

This label means monitor, do not force.

It does not mean the company is bad.

## Screened Out

Use when the candidate does not meet the research threshold due to one or more major issues.

Reasons may include:

- Weak business validation
- No credible information gap
- Excessive fragility
- Poor financial quality
- No valuation support
- Overextended rerating
- Lack of primary-source support
- Thesis based mainly on hype
- Risk/reward not researchable enough
- No clear next-step diligence path

Screened Out does not always mean the company is bad.

It means MIDAS should not prioritize it under the current workflow.

---

# Setup Modifiers

Setup Modifiers are optional.

Use them when they make the output clearer.

Do not use too many modifiers. Usually one to three is enough.

## Rerating / Price-Action Modifiers

### Pre-Rerate

Use when the thesis appears credible but not yet broadly reflected in the stock.

### Early Rerating

Use when the thesis may be starting to gain market recognition, but the setup has not fully rerated.

### Post-Rerate / Overextended

Use when the stock has already moved sharply and the thesis may be largely priced in.

### Consolidating / Base-Building

Use when the stock has moved previously but appears to be digesting the move.

### Awaiting Pullback

Use when the business or thesis is attractive, but price action or valuation makes the current setup less clean.

### Valuation Reset

Use when the stock has declined or de-rated enough that the setup may deserve fresh research.

## Discovery / Crowding Modifiers

### Underdiscovered

Use when the name appears overlooked relative to the evidence.

### Well-Discovered

Use when the company is widely followed or already appreciated by the market.

### Crowded / Consensus

Use when the thesis is already mainstream, heavily owned, or heavily promoted.

### Social-Hype Risk

Use when the narrative appears driven too heavily by social media, promotional content, or retail excitement.

## Evidence Modifiers

### Filing-Backed

Use when the main claim is supported by filings, disclosures, earnings releases, or other primary sources.

### Evidence Incomplete

Use when the thesis is plausible but important claims remain unverified, indirect, stale, or not fully quantified.

### Needs Primary-Source Verification

Use when the setup came from secondary sources, social sources, or tracker signals and still needs filing-backed validation.

### Inference-Heavy

Use when the thesis depends on reasonable inference rather than directly disclosed facts.

## Risk Modifiers

### Balance-Sheet Supported

Use when cash, liquidity, asset value, or low leverage helps protect the thesis.

### Balance-Sheet Fragile

Use when leverage, liquidity, debt maturities, cash burn, or dilution risk could break the thesis.

### Customer-Concentration Risk

Use when dependence on one or a few customers materially affects the thesis.

### Catalyst-Dependent

Use when the setup depends heavily on one event.

### Execution-Heavy

Use when the thesis depends on management delivering operational improvements, capacity expansion, integration, cost cuts, or product adoption.

### Cyclical

Use when the thesis depends meaningfully on macro, industry, commodity, or end-market cycles.

### Regulatory / Legal Risk

Use when regulation, litigation, approvals, enforcement, or policy materially affect the thesis.

## Valuation Modifiers

### Margin-of-Safety Supported

Use when valuation appears supported by conservative intrinsic value, cash flow, assets, NAV, or earnings power.

### Valuation Sensitive

Use when business quality is strong but the current valuation leaves limited room for error.

### Asset-Backed

Use when tangible assets, NAV, liquidation value, replacement value, real estate, investments, or balance-sheet assets are central to the thesis.

### Multiple-Expansion Dependent

Use when upside depends mainly on the market paying a higher multiple rather than clear fundamental improvement.

---

# Usage Rules

- Use one primary Setup Classification unless the output explicitly allows a secondary classification.
- Use Setup Modifiers only when they add clarity.
- Do not overload outputs with too many modifiers.
- Do not use Buy, Hold, Sell, Strong Buy, or price-target-style recommendation language.
- Do not classify raw data-only outputs unless the command also provides an evaluation.
- Classification should be based on evidence, not vibes.
- Prefer filing-backed or primary-source evidence when assigning a classification.
- If the classification is uncertain, say why.
- Do not force every stock into Prime Research Candidate or Hidden-Gem Candidate.
- A strong company can still be classified as Quality Compounder with modifiers such as Well-Discovered or Valuation Sensitive.
- A risky company can still be researchable if labeled clearly as Speculative / High-Fragility Candidate.
- A stock that already moved sharply may still be interesting, but should usually receive a modifier such as Post-Rerate / Overextended, Awaiting Pullback, or Consolidating / Base-Building.
- Tracker activity should not be treated as a recommendation or copy-trading signal.
- A candidate can be Screened Out due to weak evidence even if the narrative sounds exciting.

---

# Relationship to SCORING.md

Setup Classification should work with MIDAS scoring, not replace it.

Use:

`/home/jordan/.hermes/profiles/midas/rules/SCORING.md`

Examples:

- High Global Research Score + strong evidence + clean setup → Prime Research Candidate
- Strong Hidden-Gem Overlay + underdiscovered evidence → Hidden-Gem Candidate
- Strong business quality + durable returns → Quality Compounder
- Strong valuation discount + survivable balance sheet → Deep Value / Mispricing Candidate
- Improving fundamentals after weakness → Turnaround / Inflection Candidate
- Specific event-driven thesis → Special Situation / Event-Driven Candidate
- Cycle-driven recovery setup → Cyclical Recovery Candidate
- Disclosure-sourced lead → Tracker Lead Candidate
- High upside but fragile risk profile → Speculative / High-Fragility Candidate
- Interesting but overextended/incomplete → Watchlist / Awaiting Better Setup
- Weak evidence, poor quality, no researchable gap, or excessive fragility → Screened Out

Do not let score alone override classification judgment.

---

# Relationship to RERATING.md

Use `/home/jordan/.hermes/profiles/midas/rules/RERATING.md` when reasoning about rerating stage, market expectations, crowding, overextension, and whether a setup is clean, fragile, early, or post-rerate before applying approved classifications or modifiers.

RERATING.md does not add new classifications or modifiers; this file remains the authority for approved Setup Classifications and Setup Modifiers.

---

# Relationship to SOURCES.md

Setup Classification must follow MIDAS source standards.

Use:

`/home/jordan/.hermes/profiles/midas/rules/SOURCES.md`

Classification should be more cautious when:

- Source quality is weak
- Sources are stale
- The thesis is social-media driven
- The claim is not filing-backed
- Customer, contract, backlog, or financial claims are not quantified
- Key assumptions are inferred rather than disclosed
- A primary source conflicts with secondary commentary

If the evidence base is weak, use modifiers such as:

- Evidence Incomplete
- Needs Primary-Source Verification
- Inference-Heavy
- Social-Hype Risk

---

# Recommended Output Format

When used in a command output, display:

`Setup Classification: [Primary Classification]`

Optional:

`Setup Modifiers: [Modifier 1]; [Modifier 2]; [Modifier 3]`

Optional one-line explanation:

`Why: [Brief explanation based on evidence]`

Example:

`Setup Classification: Hidden-Gem Candidate`

`Setup Modifiers: Filing-Backed; Early Rerating; Customer-Concentration Risk`

`Why: The company appears underfollowed and has filing-backed demand signals, but the setup is still fragile due to customer concentration.`

Example:

`Setup Classification: Quality Compounder`

`Setup Modifiers: Well-Discovered; Valuation Sensitive`

`Why: Business quality appears strong, but the market already understands the company and valuation leaves less room for error.`

Example:

`Setup Classification: Deep Value / Mispricing Candidate`

`Setup Modifiers: Asset-Backed; Catalyst Needed`

`Why: The stock appears discounted versus asset value, but the thesis needs a clearer path for value realization.`

Example:

`Setup Classification: Watchlist / Awaiting Better Setup`

`Setup Modifiers: Post-Rerate / Overextended; Awaiting Pullback`

`Why: The business is attractive, but the stock has already rerated sharply and needs consolidation or a valuation reset.`
