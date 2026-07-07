# Midas Rerating / Setup Standards

## Status

Active

Promoted from Draft on 2026-07-05. This file was already binding in practice: `rules/GLOBAL.md` requires rerating reasoning to follow it and the gems contract formally inherits from it.

## Purpose

Define Midas standards for stock setup, expectations, rerating stage, and valuation/rerating risk.

This file should help Midas separate:

- business quality,
- financial quality,
- setup / expectations / rerating quality,
- valuation/rerating risk,
- evidence versus market narrative.

This file is a shared conceptual rule. It is not a command workflow, scoring rubric, classification list, valuation model, market-data provider spec, chart-pattern system, or trading rulebook.

## Core Distinction

Define these layers:

1. Business Quality

- What the business is.
- How it makes money.
- Durability, competition, customers, recurrence, pricing power, cyclicality.
- Primary command input: `!research`.

2. Financial Quality

- Revenue, margins, profitability, cash flow, balance sheet, dilution, accounting quality, metric quality.
- Primary command input: `!financials`.

3. Setup / Rerating Quality

- Whether expectations, valuation, evidence, market recognition, and catalyst path create a researchable stock setup.
- A strong business can still be a weak setup if expectations are already high.
- A weak current business can still have a powerful but fragile rerating setup if expectations are changing before filings confirm improvement.

4. Rerating Risk

- The risk that expectations have moved faster than evidence.
- The risk that valuation, market narrative, or price action already discounts future execution that filings have not yet proven.

## Key Principle

Strong fundamentals do not automatically create a clean stock setup.

Weak current fundamentals do not automatically prevent a stock from rerating.

Rerating analysis compares:

- what filings prove today,
- what management claims,
- what the market appears to be underwriting,
- what price/volume/sector behavior may be signaling,
- what evidence is still missing,
- what could validate or break the setup.

Rerating analysis is research prioritization, not investment advice.

## Evidence Versus Market Narrative

Define evidence categories:

- Filing-backed evidence:
  SEC filings, annual/interim reports, audited financial statements, official disclosures.
  Highest trust for business and financial claims.

- Company-disclosed narrative:
  Management commentary, investor presentations, earnings calls, press releases.
  Useful but should be separated from reported facts.

- Market-data context:
  Price, market cap, volume, relative strength, liquidity, valuation multiples, price performance.
  Can support rerating context, valuation context, overextension, crowding, or market recognition.
  Cannot prove revenue, margins, cash flow, customer demand, balance-sheet quality, business quality, or thesis validity.

- Consensus / expectations context:
  Analyst estimates, estimate revisions, valuation expectations, peer comparisons.
  Useful for understanding what the market may be underwriting.
  Not filing-backed proof.

- Social / crowding narrative:
  X, Reddit, YouTube, forums, influencer content, newsletter hype.
  Discovery/crowding signal only.
  Not thesis proof.

- Price action:
  Can show market recognition, overextension, consolidation, or possible narrative shift.
  Cannot prove fundamentals.

## Rerating Stage Framework

Define the following stages as setup interpretation, not recommendations:

- Pre-Rerate
  Evidence may be improving, but market recognition appears limited.

- Early Rerating
  Market recognition appears to be starting, but evidence and valuation still need discipline.

- Mid-Rerate / Evidence-Building
  Price and narrative have moved, and filings are beginning to confirm part of the story.

- Post-Rerate / Overextended
  The stock has already moved sharply or expectations appear high relative to filing-backed proof.

- Consolidating / Base-Building
  A prior move is being digested; next evidence may matter more than narrative.

- Valuation Reset
  The stock has de-rated or declined enough that setup quality may deserve fresh review.

- Hype Spike / Narrative-Heavy Move
  Price or attention has moved mainly on theme, social excitement, or weakly verified narrative.

- Failed Rerating / Narrative Unwind
  Market expectations previously rose but filings, guidance, cash flow, margins, or execution failed to confirm the setup.

## Setup Quality Questions

When a command evaluates setup or rerating, Midas should ask:

- What has changed?
- What is the market likely starting to underwrite?
- Is the new narrative filing-backed, management-commentary-backed, inferred, market-data-backed, or social/crowding-driven?
- Are filings confirming the narrative?
- Is price action ahead of evidence?
- Is valuation support visible?
- Is the idea already crowded or well-discovered?
- What evidence would validate the setup?
- What evidence would break the setup?
- Is the setup clean, fragile, overextended, resetting, or not yet researchable?

## Positive Rerating Setup Indicators

Potential positives include:

- Expectations appear low, stale, or backward-looking.
- Filings are improving before the market narrative fully catches up.
- Revenue, margins, backlog, cash flow, or balance sheet are inflecting.
- A segment, asset, customer base, or product line appears underappreciated.
- A catalyst path exists and is evidence-backed.
- Market recognition is early rather than fully crowded.
- The stock is consolidating after initial recognition rather than moving vertically without proof.
- Valuation or margin-of-safety support is at least frameable.

## Market Absorption / Recognition Check

When a command evaluates setup, rerating, catalyst quality, or stock prioritization, check whether the market appears to have already absorbed the relevant signal.

Market absorption means price, volume, valuation, consensus, media attention, sector narrative, or crowding may already reflect the disclosure, filing detail, policy/event catalyst, guidance change, contract award, or thesis evidence being considered.

Check:

- Did the price, volume, valuation multiple, or relative-strength move occur before the current research signal?
- Did the move occur after the signal but before the current analysis, suggesting recognition may already be underway or complete?
- Has consensus, media coverage, social/crowding attention, or peer valuation already shifted toward the thesis?
- Is the stock consolidating after recognition, still underrecognized, or post-rerate / overextended?
- Is the remaining research question still company-specific and evidence-testable, or mostly a stale market narrative?

Use this check to distinguish:

- `Unabsorbed / underrecognized` — evidence exists but market recognition appears limited.
- `Partially absorbed` — market recognition has started, but the setup may still be researchable if evidence and valuation remain disciplined.
- `Mostly absorbed` — the market appears to have priced much of the signal; require stronger valuation support or a new evidence gap.
- `Overabsorbed / hype-heavy` — price or attention appears ahead of filing-backed proof; treat rerating risk as elevated.

Market absorption should affect setup quality, rerating risk, candidate ranking, and best-next diligence. It must not become a buy/sell/hold signal, entry/exit timing rule, or claim that price action proves fundamentals.

## Negative / Fragile Rerating Indicators

Potential negatives include:

- Vertical move without filing confirmation.
- Narrative mainly social/promotional.
- Multiple expansion without fundamental improvement.
- Market already underwriting execution perfection.
- Valuation support is thin or impossible to frame.
- Financial quality is weak and survivability depends on dilution or financing.
- Customer, contract, regulatory, commodity, liquidity, or supply-chain concentration can break the thesis.
- Management claims are not visible in reported results.
- Revenue growth does not convert into margins, cash flow, or balance-sheet improvement.
- Strong price action is being treated as proof of thesis validity.

## Command Usage

Use RERATING.md heavily when commands evaluate setup, expectations, valuation/rerating risk, or stock prioritization:

- `!gems`
  High relevance. Use for hidden-gem, underdiscovered, rerating, crowding, and post-rerate discipline.

- `!thesis`
  High relevance. Use for expectations, variant view, valuation/rerating setup, what must become true, and what is priced in.

- `!risk`
  High relevance. Use for valuation/rerating risk, setup fragility, and expectations outrunning evidence.

  High relevance. Use to integrate business quality, financial quality, setup quality, rerating risk, classification, scoring, and evidence confidence.

Limited default use:

- `!research`
  Use as a business-model evidence input. Do not make stock setup or rerating conclusions by default unless the user explicitly asks for a setup view.

- `!financials`
  Use as a financial-quality evidence input. Do not make stock setup or rerating conclusions by default unless the user explicitly asks for setup, valuation, or rerating context.

- `!market`
  If present, market data can supply price/volume/liquidity/valuation context only. It should not classify, score, recommend, or prove fundamentals.

## Guardrails

Rerating analysis must not produce:

- Buy/Sell/Hold calls.
- Price targets.
- Entry or exit levels.
- Position sizing.
- Trade timing instructions.
- “Breakout buy” language.
- “Wait for pullback then buy” language.
- Claims that chart patterns guarantee outcomes.
- Claims that price action proves fundamentals.
- Claims that social hype proves thesis validity.

Preferred language:

- Setup appears cleaner / less clean.
- Rerating risk is elevated.
- Evidence supports / does not yet support the market narrative.
- Filing-backed evidence is not yet sufficient.
- Market appears to be underwriting [future outcome], but this remains unproven.
- Best next diligence step.

## Future Chart / Technical-Analysis Boundary

A future chart-analysis agent, chart command, or technical-analysis layer may analyze technical structure, support/resistance, trend, volume, momentum, and timing context.
Midas may use chart/market behavior only as separate market-context evidence when explicitly relevant.

Chart or technical signals must not determine Midas business quality, financial quality, thesis validity, source confidence, or filing-backed setup classification by themselves.

Midas setup classification should remain evidence-aware and filing-first.

## Relationship to Other Rules

- `rules/GLOBAL.md`
  Global operating principles and high-level rerating discipline.

- `rules/CLASSIFICATIONS.md`
  Owns approved setup classifications and modifiers.

- `rules/SCORING.md`
  Owns scoring pillars, overlays, score caps, and gates.

- `rules/SOURCES.md`
  Owns evidence hierarchy and source confidence.

- `rules/MARKET_DATA.md`
  Owns live/current market-data rules, provider behavior, and market-data boundaries.

- `rules/METRICS.md`
  Owns financial formulas, valuation-multiple formulas, period labels, and metric discipline.

- Command `SKILL.md`
  Owns when a command applies RERATING.md.

- Command `OUTPUT.md`
  Owns how rerating/setup analysis appears in that command’s output.

## Stage Plan / Drift Control

Stage 1 — Shared Rule Install

- Create `rules/RERATING.md` as Draft.
- Add short pointers only in shared rule files.
- Do not patch command skills yet.
- Do not patch command output contracts yet.
- Do not patch evals yet.

Stage 2 — Command Integration

- When building/refactoring `!risk`, add RERATING.md to the command and include valuation/rerating risk behavior.
- When building/refactoring `!thesis`, add expectations/rerating setup behavior.
- When refactoring `!gems`, add hidden-gem/rerating-stage discipline.
- When building the planned packet-synthesis command (see the promote seed in `docs/plans/`), integrate setup quality as a separate layer.
- Do not wire `!research` or default `!financials` into setup/rerating conclusions unless explicitly requested.

Stage 3 — Eval Coverage

- Add evals for:
  - strong company / weak setup,
  - weak company / fragile rerating setup,
  - price action is not proof,
  - social narrative is not proof,
  - rerating risk in `!risk`,
  - expectations/rerating setup in `!thesis`,
  - hidden-gem post-rerate discipline in `!gems`,
  - separation of business quality, financial quality, setup quality, and evidence confidence in packet-level synthesis.

Stage 4 — Possible Future Command

- Consider `!setup [ticker]` only after `!risk`, `!thesis`, and `!gems` behavior is stable.
- Prefer `!setup` over `!rerate` because it is broader and less prediction-sounding.
