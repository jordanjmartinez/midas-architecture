# Fund-Manager Intelligence Contract

Stage: Active fund-manager intelligence contract for `!track`.

This is the active fund-manager intelligence contract for `!track`. Global Midas rules govern shared source, scoring, classification, output, and artifact standards. This contract governs fund-manager Alpha Queue triage.

This file defines how fund-manager disclosures are triaged into one internal final `Alpha Queue`. Standard visible output translates that queue into the human-readable `Best Stock Leads` section defined in `OUTPUT.md`. It does not alter politician mode or create a new command.

## Authority Boundaries

This contract owns the command-local intelligence logic for `!track` fund-manager mode:

- Core funnel, Alpha Queue gate, and the five P0 promotion gates.
- Best Stock Leads source contract and Evidence Ledger requirements.
- Disclosure-type signal matrix and filing entity / CIK / account-mapping hygiene.
- Manager archetype calibration, triage lenses, and the manager profile layer.
- Post-period fundamental event checks and event status labels.
- Source-limit handling, the false-positive library, and demotion rules.
- Eligible manager universe / cloneability, 13F completeness, thesis-linkage, qualified-consensus, and best-idea / active-tilt gates.
- Manager thesis lifecycle monitoring, 13D / 13G parsing, and event-path tracking.
- Liquidity / float / market-impact researchability gating and quantitative chase filters.
- The internal signal scorecard and ranking principle, and their interaction with Setup Classification and Scoring, without redefining global scoring or classification.
- The structured Alpha Queue candidate shape, held here until a `schemas/` home exists.

This contract does not own:

- Output templates or visible section shapes, which belong in the tracker `OUTPUT.md`.
- Trigger syntax, routing, inputs, workflow, or politician mode, which belong in `SKILL.md` and `contracts/politician.md`.
- Artifact paths or write mechanics, except by reference to the active artifact authorities.
- Watchlist or roster mutation, including `data/tracker_watchlist.json` handling defined in `SKILL.md`.
- Registry status or eval cases.
- Global source, metric, scoring, classification, output, artifact, or copy-trading guardrail definitions.

Follow `rules/CONTRACT_AUTHORITY.md` when deciding whether future additions belong here, in `SKILL.md`, in `OUTPUT.md`, in evals, in docs, in schemas, or in shared global rules. Tracked activity framing follows the no-copy-trading rule in `rules/GLOBAL.md`; this contract applies that rule and must not weaken it.

## Purpose

Fund-manager `!track` should answer:

> Which disclosed fund-manager moves are still useful enough to become Midas research leads today?

It should not answer:

- What were the biggest holdings?
- What should the user copy?
- What should the user buy?
- Which famous manager owns this?

Tracked fund-manager activity is a research lead only. It is never a buy/sell/hold instruction, copy-trading signal, price target, or position-sizing input.

## Visible Output Translation

Standard visible fund-manager output should use the thesis-style `Best Stock Leads` layout from `OUTPUT.md`. Keep `Signal Frame`, `Chase Filter`, `Signal type`, and other Alpha Queue mechanics internal by default unless full/audit mode or a user request requires them.

Avoid fame-based promotional language by default.

## Core Funnel

```text
Raw disclosed security
→ Qualified disclosure event
→ Candidate signal
→ Alpha Queue candidate
→ Final ranking or demotion
```

This funnel prevents raw holdings, large reported market values, or famous tickers from automatically becoming research leads.

## Alpha Queue Gate

A ticker may enter the Alpha Queue only when all gate items are satisfied:

1. **Company-level exposure:** The security is company-level common equity, clean company-linked exposure, or separately identified company event. Broad ETFs, index options, vague baskets, and unverified mappings do not qualify by default.
2. **Disclosure support:** The source supports the event type: latest 13F-HR, 13F/A, 13D/G, 13D/A or 13G/A, Form 4, fund letter, company filing, or official investor communication.
3. **Materiality:** The event is meaningful enough to be more than noise: new, increased, concentrated, repeated, activist-related, thesis-supported, or large enough relative to the disclosed portfolio to matter.
4. **Manager signal plausibility:** The signal fits the manager's known style or disclosed thesis, or the filing change is sufficiently unusual to merit research. Quant/index-like, factor, or ultra-diversified managers require a higher bar.
5. **Company-level research question:** There is a specific question Midas can research with `!research`, `!financials`, `!risk`, `!thesis`.
6. **Source caveats manageable:** Source limitations do not overwhelm the signal. If the source is too stale, ambiguous, amended without clarity, options-heavy, or unmappable, demote.
7. **Chase Filter acceptable:** Price/action/context does not require demotion. A strong filing signal can still fail as a current research lead if the market has already chased it vertically.
8. **Consensus quality clean:** Any ownership overlap is qualified independent accumulation rather than broad crowding, hedge-fund-hotel ownership, or social hype. Broad holder count alone does not validate a lead.

If any gate item fails, keep the ticker in lower-priority/context or omit it, with a specific reason when material.

## Best Stock Leads Source Contract — P0

Before a fund-manager candidate can enter visible `Best Stock Leads`, the promotion must satisfy a source contract:

- Official or primary sources may support promotion. Examples include SEC 13F-HR, 13F-HR/A, 13D, 13D/A, 13G, 13G/A, Form 4, company filings, official investor letters, and official firm communications when they directly support the disclosure event or thesis context.
- Convenience sources, scraped summaries, third-party holdings databases, social posts, newsletters, and media articles may discover candidates or assist with reconciliation, but they cannot promote a ticker to `Best Stock Leads` by themselves.
- Each promotion candidate must capture internally: source ID, source type, source date or access date, filing date, reporting period when applicable, accession number or disclosure/filing ID when available, filer/person/entity match, issuer/security match, CIK/CUSIP/ticker mapping when available, amendment status, and source limitations.
- Source limitations must be explicit internally: 13F delay, amendment risk, confidential treatment, incomplete information table, options ambiguity, shared discretion, account/entity mapping uncertainty, fund-letter non-ownership proof, stale data, or inconsistent issuer mapping.
- If an official/primary source is unavailable, blocked, stale, contradictory, incomplete, or not tied to the named manager/entity, the candidate must be demoted unless another official/primary source independently supports the promotion thesis.

The source contract is internal by default. Standard output should translate only material limitations through existing candidate caveats, `Lower-Signal Items`, or `Source Caveat`; it must not create new visible output fields or sections unless the user asks for audit/source detail.

## Evidence Ledger — P0

Every promoted fund-manager ticker must have an internal evidence ledger before visible `Best Stock Leads` placement:

- Every promoted ticker must map to one or more evidence IDs.
- Every evidence ID must map to one or more source IDs from the source contract.
- Every material promotion claim must be traceable to an evidence ID and source ID, including disclosure type, filing period/date, filer/entity match, position/change math, security identity, amendment status, source limitation, thesis/catalyst support, company-level research question, price/rerating context when used, and demotion/caveat reasoning.
- Inferred manager intent, current ownership after stale disclosure, undisclosed activity, future returns, investment attractiveness, or a fund manager's motive must not be ledgered as fact. If no primary source states the manager thesis, label the thesis as Midas inference or omit it.
- If a material claim cannot be ledgered, remove the claim, demote the candidate, or route it as a verification item rather than promoting it.

Keep the evidence ledger internal in standard output. Surface only compact implications through the existing `Why it matters:`, `Why it might not be a strong signal:`, `Why These Ranked`, `Lower-Signal Items`, and `Source Caveat` fields unless detailed/audit output is explicitly requested.

## Five P0 Promotion Gates

Before a fund-manager candidate can enter visible `Best Stock Leads`, it must explicitly clear all five internal P0 gates:

1. **Source Authority Gate:** official/primary sources support the disclosure event and material promotion claims; convenience sources are not the sole promotion basis; source IDs, source dates, filing/accession IDs when available, filer/entity match, and limitations are captured.
2. **Disclosure Signal Gate:** the event is company-level and meaningful: new, increased, concentrated, activist/event-related, repeated, thesis-supported, or otherwise material after position normalization. Broad ETFs, index/options baskets, stale rows, noise-sized positions, and ambiguous derivatives fail by default.
3. **Person Relevance / Authority Gate:** the named manager, adviser, fund, reporting entity, or beneficial owner is correctly mapped to the filing or disclosure, and the signal plausibly fits the manager/entity's strategy, authority, or disclosed role.
4. **Company Materiality / Researchability Gate:** the disclosure creates a testable company-level Midas research question and there is source-backed evidence that the position/change/event could matter to the issuer, setup, capital structure, governance, fundamentals, or rerating path.
5. **Integrity / Noise Discount Gate:** 13F delay, amendment/completeness risk, shared-discretion ambiguity, options/hedge ambiguity, stale or overextended price action, crowding, social hype, and source conflicts do not overwhelm the research signal.

If any P0 gate fails, the candidate cannot appear in visible `Best Stock Leads`. It may appear only as lower-signal context when useful, clearly caveated, and not framed as a promoted research lead.

## Disclosure Type Signal Matrix

Use the global source rules in `rules/SOURCES.md` for evidence hierarchy and citation discipline. This matrix is fund-manager-specific signal weighting for `!track` Alpha Queue triage; it does not replace global source standards.

Different disclosure types have different intelligence value. A 13D activist-style filing is not the same as a passive 13G, delayed 13F row, call option, or fund-letter mention.

Use this matrix internally when weighting fund-manager signals:

| Disclosure type | Default signal weight | Fund-manager `!track` interpretation |
|---|---:|---|
| `13D / 13D-A` | High | Event/intent-heavy. Often stronger evidence of company-level ownership, activism, influence, or strategic intent. Prioritize when it creates a clear research question. |
| `13G / 13G-A` | Medium | Ownership-relevant but often passive. Raise only when size, change, filing context, or company-specific setup is unusual. |
| `13F new common-stock position` | Medium | Useful but delayed. Requires position normalization, portfolio-weight context, and source-limit caveats before ranking. |
| `13F increase` | Medium | Meaningful only when real share-count increase, portfolio-weight increase, or concentration change supports added exposure. Do not rely on value increase alone. |
| `Options exposure` | Low-to-medium | Promote only when company-specific and direction is clean. Otherwise caveat or demote as possible hedge, factor exposure, downside protection, or portfolio construction. |
| `Fund letter` | Thesis context | Useful for understanding stated rationale, but not ownership proof, current-position proof, or standalone evidence of current attractiveness. |

Apply the matrix as source weighting, not as an automatic ranking outcome. A high-signal disclosure can still be demoted if it lacks a company-level research question, is stale, unmappable, crowded, overextended, or overwhelmed by source caveats. A medium-signal disclosure can rank if it is fresh, normalized, company-specific, and tied to a clear filing thesis.

## Filing Entity / CIK / Account-Mapping Hygiene

Verify the filing entity and security mapping before treating a fund-manager disclosure as a clean Alpha Queue signal.

Fund-manager disclosures can involve multiple advisers, related entities, amended filings, shared discretion, 13F-NT notices, fund-level disclosures, duplicated reporting, and corporate-action/ticker mapping issues. If the entity or account mapping is wrong, the entire signal can be wrong.

Before ranking or comparing positions, verify when available:

- Legal filer name.
- CIK.
- Accession number.
- Filing type.
- Original versus amended filing status.
- Manager-level versus fund-level disclosure.
- Shared-discretion or other-manager reporting.
- 13F-NT / notice-only filings.
- Ticker, CUSIP, issuer-name, and corporate-action mapping.

Hygiene rules:

- Do not combine related advisers, funds, or entities unless the filing relationship is verified.
- Do not treat a 13F-NT notice as a holdings table.
- Do not mix original and amended filing values without labeling the amendment status.
- Do not double-count shared-discretion or duplicated rows as separate conviction signals.
- Do not treat manager-level and fund-level disclosures as interchangeable unless the relationship and reporting scope are clear.
- Verify ticker/CUSIP/corporate-action continuity before treating old and current rows as one economic position history.
- If mapping is plausible but unverified, label it as a mapping uncertainty and demote or caveat the signal.

When filing-entity or account mapping is uncertain, keep the candidate out of the Alpha Queue unless another clean disclosure independently supports the company-level signal.

## Manager Archetype Calibration

Classify the filer before evaluating the stock-level signal.

The same disclosed position can mean different things depending on the manager's strategy, concentration, turnover, and domain expertise. A new 3% portfolio position from a concentrated fundamental manager may be a real signal. A new 0.03% position from a diversified quant or index-like institution may be noise. An activist 13D is different from a multi-strategy hedge fund option overlay. A sector specialist's move inside their domain deserves more attention than a random small position in a broad portfolio.

Use the manager archetype to calibrate the burden of proof for Alpha Queue inclusion:

| Manager archetype | Calibration guidance |
|---|---|
| `concentrated fundamental` | Higher signal when a position is new, increased, or meaningful as a portfolio weight. Treat company-level allocation decisions as more informative when the portfolio is focused. |
| `sector specialist` | Higher signal for moves inside the manager's domain expertise. Require more caution for off-domain positions unless the filing thesis is clear. |
| `activist/event-driven` | Higher signal when paired with 13D/13D-A, governance, strategic, restructuring, merger, financing, or event-driven evidence. Focus on the company-level event question. |
| `quality compounder` | Higher signal when a new or increased position fits durable growth, returns, moat, margin, or long-duration quality themes. Still check valuation and crowding. |
| `deep value/distressed` | Higher signal when the position fits balance-sheet repair, asset value, restructuring, bankruptcy emergence, cyclical trough, or mispricing evidence. Emphasize risk and solvency checks. |
| `multi-strategy/trading-oriented` | Medium-to-lower signal by default. Require clearer evidence that the position is company-specific rather than hedge, event trade, relative-value exposure, or portfolio overlay. |
| `quant/factor/systematic` | Lower signal by default. Small positions, broad factor baskets, and high-position-count portfolios need a higher bar before becoming Alpha Queue leads. |
| `passive/index-like` | Low signal by default. Do not rank positions unless there is a separate company-level disclosure, ownership threshold, governance event, or unusual change. |
| `unknown` | Use cautious default calibration. Do not over-rank based on manager fame; rely more heavily on disclosure type, normalization, source cleanliness, and company-level research question. |

Archetype classification should be evidence-based and may use firm descriptions, strategy disclosures, fund letters, portfolio concentration, number of disclosed positions, turnover pattern, historical filings, and known investment style. If uncertain, classify as `unknown` rather than guessing.

Do not display the archetype as a routine output field in standard tracker output unless it materially explains the ranking or demotion. Use it internally to calibrate signal strength, source caveats, and Alpha Queue priority.

## Fund-Manager Triage Lenses

Use these lenses internally to decide whether a disclosure becomes an Alpha Queue candidate and how it ranks.

### 1. Manager Edge Fit

Higher quality:

- Specialist or concentrated manager with clear company-level exposure.
- Fundamental manager with a position that fits a disclosed thesis.
- Activist or 13D-style disclosure with a clear company event question.

Lower quality:

- Very broad, quant-like, index-like, or factor-style portfolio with many small positions.
- Manager fame without a company-specific signal.
- Position exists only because it is a mega-cap or index constituent.

### 2. Conviction & Change

Prioritize newness, increased shares/value, portfolio-weight change, concentration, and repeated accumulation over raw reported market value. A smaller new or sharply increased position may rank above a larger stale mega-cap holding.

Use filing-to-filing language:

- `new 13F entry`
- `increased vs prior 13F`
- `reduced vs prior 13F`
- `exited vs prior 13F`
- `notable disclosed options exposure`
- `13D / activist-style signal`

Avoid implying real-time trades or current ownership when a delayed filing is the only evidence.

### 3. Position Normalization

Normalize 13F positions before using them for Alpha Queue ranking.

A 13F position can look larger because the stock price moved, not because the manager bought more shares. A position can also look important in absolute dollars while remaining tiny inside a large disclosed portfolio.

The key distinction is:

- `manager owns a lot`
- versus `manager appears to have made a meaningful company-level allocation decision`

Use normalized position analysis to avoid over-ranking mega-caps, price-appreciated holdings, and large-but-stale legacy positions.

When current and prior 13F data are available, prioritize these normalized signals:

- Share-count change, not value change alone.
- Portfolio-weight change, not current market value alone.
- Current position weight relative to total disclosed portfolio.
- Change from tiny to meaningful portfolio weight.
- New position size relative to portfolio, not just absolute dollars.
- Concentration change versus the manager's own portfolio.

Treat value change carefully:

- A value increase with flat or lower share count may mostly reflect price appreciation, not added exposure.
- A large current value may be stale if share count and portfolio weight did not materially increase.
- A mega-cap holding may dominate dollars while revealing little about fresh company-level allocation.

Do not describe a position as a conviction increase unless the filing supports it through share-count increase, portfolio-weight increase, new-position materiality, concentration change, or related disclosure evidence.

Demote or caveat positions when:

- Reported value increased but shares were flat or down.
- The position is large in dollars but small as a percentage of portfolio.
- The position is a long-held legacy holding with no meaningful change.
- The apparent importance comes mainly from market-price appreciation.
- The position is a mega-cap or consensus name without unusual normalized change.

Rank higher when normalization shows:

- New or increased exposure that is meaningful relative to portfolio size.
- A small or mid-cap position becoming a real portfolio allocation.
- A clear increase in portfolio weight, not just market value.
- A manager-specific concentration decision.
- A company-level allocation signal tied to the filing thesis.

### 4. Disclosure Cleanliness

Higher quality:

- Clean common-stock 13F row with current/prior comparison.
- 13D/G or amendment clearly tied to a company-level ownership/event question.
- Fund letter supports thesis context and is labeled as thesis context, not current-ownership proof.

Lower quality / demotion candidates:

- Options-only signal without directional clarity.
- Puts/calls that may be hedges, factor exposure, or portfolio construction.
- Unverified ticker/corporate-action mapping.
- Amended filing mixed with original values without labeling.
- Related-disclosure evidence blended into 13F holdings.

### 5. Company-Level Research Setup

Prefer undercovered or misunderstood companies with a concrete research question: business quality, balance-sheet risk, unit economics, customer concentration, contract durability, regulatory setup, valuation/rerating, or thesis fragility.

Demote stale legacy holdings, broad ETFs, tiny/noisy positions, obvious mega-caps with no unusual change, and names with no clear company-level question.

### 6. Timing / Crowding / Chase Filter

Internal labels:

- `Pass`
- `Watch`
- `Demote`

Before final ranking, check price context when available: move since report-period end, move since filing date, and 1M / 3M / 6M / 1Y  context when useful. Use this as timing/rerating context only, not proof of business quality.

Internal guide:

- **Pass:** Disclosure signal remains timely enough; no obvious vertical post-period/post-filing rerate or crowding problem based on available context.
- **Watch:** Signal is interesting but price/action/attention may already be processing it; candidate may need consolidation, valuation review, or updated company work before promotion.
- **Demote:** Stock already had a major vertical move, broad crowding/hedge-fund-hotel/social-hype risk overwhelms the signal, or current research usefulness is materially weaker than the filing signal.

A high-quality filing signal may still be lower-priority if the internal Chase Filter is `Watch` or `Demote`. Keep normal output compact by translating the issue into `Why it might not be a strong signal:` or `Lower-Signal Items` rather than showing a routine `Chase Filter:` field.

## Post-Period Fundamental Event Check

Before final Alpha Queue ranking, check whether material company-specific events after the 13F report-period end or disclosure date strengthen, weaken, invalidate, or reframe the filing signal.

A fund-manager disclosure can be stale or less useful if the company changed materially after the relevant reporting period. The purpose of this check is to decide whether the disclosed move is still useful enough to become a Midas research lead today.

Check for material post-period events when available and relevant:

- Latest earnings, 10-Q, or 10-K.
- Material 8-Ks.
- Guidance changes.
- Dilution or financing.
- Debt maturity, refinancing, covenant, liquidity, or going-concern events.
- M&A, strategic review, divestiture, or asset sale.
- Customer, contract, backlog, or award developments.
- Regulatory or legal updates.
- Management changes.

Use post-period events to adjust ranking, caveats, and demotions:

- If post-period events strengthen or clarify the filing thesis, the candidate may remain or improve as a research lead.
- If post-period events weaken, invalidate, or materially reframe the filing thesis, demote, caveat, or move the name to lower-priority/context.
- If post-period information is missing but the signal depends on current fundamentals, label that as an information gap rather than assuming the setup remains intact.

Do not treat post-period company events as proof of manager intent. Separate filing-backed evidence from later company evidence.

## Source Limits Handling

Source-limit logic is mandatory internally but should not become routine Telegram bloat.

Default behavior:

- Do **not** add a standalone `Source Limits` section in normal output.
- Apply source limits through ranking, caveats, demotions, and candidate-card `Why it might not be a strong signal:` wording when relevant.
- Show a standalone source-limit section only in full/audit mode, when explicitly requested, or when the limitations are unusually complex and necessary for user understanding.

Common internal source limits:

- 13F filings are delayed and do not prove current ownership.
- 13F filings omit shorts and many asset classes.
- 13F cost basis and post-period exits are unknown.
- Options exposure may be hedging, factor exposure, downside protection, or portfolio construction.
- Investor letters can explain thesis context but do not prove current attractiveness or current ownership.
- Amendments must be labeled and not mixed with original filings without explanation.
- Ticker/corporate-action mappings must be verified during the run.

Candidate-card caveat examples:

- `Key caveat: 13F data is delayed and does not prove current ownership.`
- `Key caveat: options exposure is ambiguous and may reflect hedging rather than company-level conviction.`
- `Key caveat: strong filing signal, but Chase Filter is Watch after a sharp post-period rerate.`
- `Key caveat: ticker mapping needs verification before treating this as a continuous position.`

## False-Positive Library

Use these recurring false-positive patterns to protect the Alpha Queue from common fund-manager tracker mistakes.

These are not automatic exclusions. If a false-positive pattern appears, demote or caveat the candidate unless clean contrary evidence shows the signal is fresh, normalized, company-specific, and tied to a clear research question.

Common false positives:

| False-positive pattern | Why it can mislead | Default treatment |
|---|---|---|
| Mega-cap held by everyone | Large dollar value may reflect index weight, consensus ownership, or portfolio ballast rather than a fresh manager-specific decision. | Demote unless the filing shows unusual normalized change, activist/event evidence, or a clear thesis shift. |
| Market-value increase caused by price appreciation | Reported value may rise even when shares are flat or down. | Do not treat as conviction increase without share-count, portfolio-weight, or concentration increase. |
| Tiny quant/factor/systematic position | Small rows in broad portfolios may be model exposure or factor noise. | Demote unless position size/change is unusual for that manager or tied to a clear company-level thesis. |
| Options-only exposure | Options can reflect hedging, downside protection, factor exposure, or portfolio construction rather than clean equity conviction. | Low-to-medium signal; promote only if company-specific and direction is clean. |
| Merger-arb position mistaken for conviction | Event-spread exposure may not indicate long-term business-quality view. | Treat as event context unless the disclosure supports a durable company-level research question. |
| Spin-off, CUSIP, ticker, or issuer-name artifact mistaken for a new buy | Corporate actions can create apparent new rows, exits, or ticker changes without a new allocation decision. | Verify mapping before ranking; demote/caveat if continuity is uncertain. |
| Fund-letter thesis with no matching exposure | A letter can explain views without proving current ownership or current attractiveness. | Use as thesis context only; do not rank without matching clean exposure or separate disclosure support. |
| Passive 13G mistaken for activist intent | 13G often reflects passive ownership and does not imply control intent. | Medium signal at most; do not frame as activist/event-driven without 13D-style or other event evidence. |

When a false-positive pattern dominates, move the name to lower-priority/context with a specific reason or omit it if it has no company-level research value.

## Demotion Rules

Demote to lower-priority/context when any of these dominate:

- Mega-cap or consensus name with no unusual change.
- Largest holding only because of market value.
- Broad ETF or index exposure.
- Options-heavy or hedge-like exposure without a clean company-level signal.
- Tiny/noisy position with no research question.
- Stale legacy holding with no meaningful change.
- 13F lag overwhelms timeliness.
- Chase Filter is `Demote`.
- Amendment or related disclosure cannot be cleanly reconciled.
- Ticker/company mapping is plausible but unverified.

Demotion language should be specific, not generic.

## Structured Alpha Queue Candidate Schema

Create one internal Alpha Queue Candidate object for each material fund-manager disclosure candidate before applying the Formal Internal Signal Scorecard or final ranking. The object makes ranking, audit mode, artifact saving, and eval coverage reproducible.

The schema is internal by default. Standard visible output should not print the object or expose raw schema fields unless full/audit mode, artifact export, or an explicit user request requires it. Normal output should translate the object into the thesis-style `Best Stock Leads`, `Why These Ranked`, `Lower-Signal Items`, and `Source Caveat` sections defined in `OUTPUT.md`.

Use `Unknown` when a required fact cannot be verified. Use `Not applicable` when the field does not apply to the security or disclosure type. Do not invent missing shares, values, dates, tickers, CUSIPs, weights, ranks, scores, statuses, or sources.

Required internal object:

```yaml
alpha_queue_candidate:
  candidate_id: string
  ticker: string | Unknown | Not applicable
  normalized_ticker: string | Unknown | Not applicable
  issuer_name: string | Unknown
  raw_issuer_name: string | Unknown
  cusip: string | Unknown | Not applicable
  security_type: common_stock | call_option | put_option | adr | preferred | note | warrant | etf | index | other | Unknown
  put_call: Put | Call | Not applicable | Unknown
  source_type: 13F-HR | 13F-HR/A | 13F-NT | 13D | 13D/A | 13G | 13G/A | Form 4 | fund_letter | company_filing | official_investor_communication | other
  accession_number: string | Unknown | Not applicable
  filing_date: YYYY-MM-DD | Unknown
  report_period_end: YYYY-MM-DD | Unknown | Not applicable
  filing_amendment_status: Original | Amended | Notice only | Unknown
  filing_completeness:
    public_13f_complete: Yes | No | Unknown | Not applicable
    confidential_treatment_requested: Yes | No | Unknown | Not applicable
    public_summary_indicates_omissions: Yes | No | Unknown | Not applicable
    confidential_release_detected: Yes | No | Unknown | Not applicable
    omitted_holdings_risk: Low | Medium | High | Unknown | Not applicable
    completeness_caveat: string | None
  event_type: new_position | increased_position | reduced_position | exited_position | unchanged_legacy_holding | options_exposure | activist_or_ownership_signal | fund_letter_thesis_context | related_disclosure | other | Unknown
  manager_name: string | Unknown
  manager_cik: string | Unknown | Not applicable
  manager_archetype: concentrated_fundamental | sector_specialist | activist_event_driven | quality_compounder | deep_value_distressed | multi_strategy_trading | quant_factor_systematic | passive_index_like | unknown
  archetype_confidence: High | Medium | Low
  manager_eligibility:
    manager_universe_status: Eligible | Watch | Excluded | Unknown
    cloneability_grade: High | Medium | Low | Unknown
    average_holding_period: Long | Medium | Short | Unknown
    turnover_pattern: Low | Medium | High | Unknown
    position_count_band: Concentrated | Moderate | Diversified | Very diversified | Unknown
    filing_lag_pattern: Early | Normal | Late | Unknown
    public_thesis_availability: Frequent | Occasional | Rare | None | Unknown
    strategy_purity: High | Medium | Low | Unknown
    exclusion_reason: string | None
  discretion_type: Sole | Shared | Other | Unknown | Not applicable
  current_shares: number | Unknown | Not applicable
  prior_shares: number | Unknown | Not applicable
  share_delta_pct: number | Unknown | Not applicable
  current_reported_value: number | Unknown | Not applicable
  prior_reported_value: number | Unknown | Not applicable
  current_portfolio_weight: number | Unknown | Not applicable
  prior_portfolio_weight: number | Unknown | Not applicable
  portfolio_weight_delta_bps: number | Unknown | Not applicable
  position_rank_current: number | Unknown | Not applicable
  position_rank_prior: number | Unknown | Not applicable
  thesis_linkage:
    filing_backed_signal: string
    inferred_manager_hypothesis: string | Unknown
    explicit_manager_thesis_source: 13D Item 4 | fund_letter | investor_presentation | official_investor_communication | company_filing | none | Unknown
    variant_view: string | Unknown
    company_research_question: string
    disconfirming_evidence_to_check: list[string]
    best_next_command: !research | !financials | !risk | !thesis | None
  consensus_quality:
    qualified_manager_count: number | Unknown
    qualified_manager_add_count: number | Unknown
    qualified_manager_best_idea_count: number | Unknown
    broad_13f_holder_count: number | Unknown
    hedge_fund_hotel_risk: Low | Medium | High | Unknown
    social_hype_risk: Low | Medium | High | Unknown
    consensus_type: Qualified independent accumulation | Broad crowding | Mixed | Unknown
    qualified_consensus_basis: string | Unknown
  best_idea_signal:
    manager_position_percentile: number | Unknown | Not applicable
    top_3_position: Yes | No | Unknown | Not applicable
    top_5_position: Yes | No | Unknown | Not applicable
    top_10_position: Yes | No | Unknown | Not applicable
    top_quartile_position: Yes | No | Unknown | Not applicable
    active_weight_vs_benchmark: number | Unknown | Not applicable
    active_weight_percentile: number | Unknown | Not applicable
    best_idea_status: Top idea | Top 5 | Top 10 | Top quartile | Routine | Unknown | Not applicable
  mapping_confidence: High | Medium | Low
  source_confidence: A | B | C | D
  post_period_event_status: Supports | Neutral | Weakens | Invalidates | Unknown
  ownership_event_parser: object | Not applicable | Unknown
  activist_event_path:
    event_stage: Initial filing | Demand made | Company response | Cooperation agreement | Board seat | Proxy fight | Strategic review | Sale process | Capital return | Litigation | Reduced stake | Exited | Unknown | Not applicable
    next_required_proof: string | Unknown | Not applicable
    company_response_status: Supportive | Opposed | Settlement | No response | Unknown | Not applicable
    event_path_alive: Yes | No | Unclear | Not applicable
    event_path_staleness: Fresh | Aging | Stale | Unknown | Not applicable
    last_event_path_source: string | Unknown | Not applicable
    last_event_path_date: YYYY-MM-DD | Unknown | Not applicable
    event_path_caveat: string | None
  liquidity_researchability:
    market_cap_band: Mega | Large | Mid | Small | Micro | Unknown | Not applicable
    avg_dollar_volume_30d: number | Unknown | Not applicable
    free_float: number | Unknown | Not applicable
    float_ownership_pressure: Low | Medium | High | Unknown | Not applicable
    post_filing_volume_spike: Yes | No | Unknown | Not applicable
    bid_ask_spread_risk: Low | Medium | High | Unknown | Not applicable
    liquidity_researchability_status: Clean | Watch | Demote | Unknown | Not applicable
    liquidity_caveat: string | None
    market_impact_research_question: string | Unknown | Not applicable
  manager_thesis_lifecycle:
    lifecycle_stage: New | Accumulating | Thesis stated | Confirmed by company evidence | Holding steady | Reduced | Exited | Thesis stale | Unknown | Not applicable
    quarters_held: number | Unknown | Not applicable
    consecutive_adds: number | Unknown | Not applicable
    consecutive_reductions: number | Unknown | Not applicable
    last_manager_thesis_mention_date: YYYY-MM-DD | Unknown | Not applicable
    last_company_evidence_update: YYYY-MM-DD | Unknown | Not applicable
    thesis_lifecycle_implication: Rank | Watch | Demote | Omit | Unknown | Not applicable
    lifecycle_caveat: string | None
    next_lifecycle_proof: string | Unknown | Not applicable
  price_move_since_report_period_end_pct: number | Unknown | Not applicable
  price_move_since_filing_pct: number | Unknown | Not applicable
  price_move_since_filing_trading_days: number | Unknown | Not applicable
  price_context_1m_3m_6m_1y: string | Unknown | Not applicable
  volume_or_attention_spike: Yes | No | Unknown | Not applicable
  updated_company_evidence_after_move: Supports | Neutral | Weakens | None found | Unknown | Not applicable
  chase_filter: Pass | Watch | Demote
  false_positive_flags: list[string]
  data_gaps: list[string]
  signal_score: number | Unknown
  score_cap: number | None | Unknown
  alpha_queue_status: Rank | Watch | Demote | Omit
  demotion_reason: string | None
  ranking_rationale: string | Unknown
  best_next_command: !research | !financials | !risk | !thesis | None
  source_citations: list[string]
```

Schema rules:

- `candidate_id` should be stable within the run and should not depend only on ticker when issuer/ticker mapping is uncertain. Prefer a composite such as manager CIK, accession number, source type, CUSIP or raw issuer name, security type, and put/call where available.
- `ticker` is the displayed ticker only when verified. `normalized_ticker` is the current mapped ticker when a corporate action, renamed issuer, ADR mapping, or old security title is verified. If mapping is plausible but unverified, keep mapping confidence Low and do not silently promote.
- `raw_issuer_name` should preserve the exact filing-table issuer name when available. `issuer_name` should be the cleaned company/issuer name used for analysis.
- `security_type` and `put_call` must preserve options rows distinctly from common equity.
- `source_type`, `accession_number`, `filing_date`, `report_period_end`, and `filing_amendment_status` should make delayed filings, amendments, and 13F-NT notice-only cases explicit.
- `filing_completeness` is required for 13F-HR and 13F-HR/A candidates and otherwise `Not applicable` unless a related 13F completeness issue affects the candidate. It should identify confidential treatment, public-summary omissions, confidential releases, omitted-holdings risk, and any completeness caveat. Use `Unknown` rather than assuming the public 13F is complete.
- `manager_archetype` and `archetype_confidence` should be evidence-based. Use `unknown` and Low confidence rather than guessing.
- `manager_eligibility` is the run-level snapshot of the Eligible Manager Universe / Cloneability Gate. It should be derived from the Manager Profile when available, refreshed when stale, and set to `Unknown` rather than guessed when manager-level evidence is insufficient.
- `discretion_type` should identify shared-discretion or other-manager reporting when available so positions are not double-counted as separate conviction signals.
- Share, value, portfolio-weight, and rank fields should use current versus prior filing comparisons when available. Do not treat value change alone as conviction change.
- `thesis_linkage` is required for any candidate eligible for visible Best Stock Leads. It should separate the filing-backed signal from Midas inference, identify any explicit manager-thesis source, state the variant view or `Unknown`, define a company-level research question, list disconfirming evidence to check, and route to the best next command only when a specific diligence gap exists.
- `consensus_quality` is required when consensus/crowding is material to ranking, demotion, or caveats. It should distinguish qualified independent accumulation by eligibility-cleared or properly excepted managers from broad 13F ownership, hedge-fund-hotel risk, or social hype. Use `Unknown` rather than treating broad holder counts as qualified consensus.
- `best_idea_signal` should identify whether the candidate is one of the manager's likely best disclosed ideas or merely a routine portfolio row. Use position rank, portfolio-weight percentile, top-3/top-5/top-10/top-quartile flags, benchmark-relative active weight when available, and manager profile context. Use `Unknown` when the portfolio universe, benchmark, or position-rank data cannot be verified; do not invent benchmark weights or percentiles.
- `source_confidence` follows the Evidence Confidence Grade standard from `rules/SCORING.md`; `source_citations` should store concise source handles internally and raw links only when needed for audit/artifact support.
- `post_period_event_status` should summarize whether later company events support, weaken, invalidate, or leave neutral the disclosure signal. Do not treat later events as proof of manager intent.
- `ownership_event_parser` is required for material 13D, 13D/A, 13G, or 13G/A candidates and otherwise `Not applicable`. It should contain the internal 13D / 13G Intelligence Parser object.
- `activist_event_path` is required for material 13D or 13D/A activist/event-path candidates and otherwise `Not applicable`. It should track whether the event path is live, stale, settled, opposed, reduced, exited, or awaiting a specific next proof point. A 13D should not stay highly ranked after a major post-filing move unless the event path is still live, the next proof point is clear, and no later evidence shows stake reduction, exit, failed process, or stale implementation.
- `liquidity_researchability` is required when liquidity, float, market cap, spread risk, post-filing volume reaction, or market-impact distortion is material to ranking, demotion, or caveats. It should separate fundamental/company interest from practical fresh-tracker-lead researchability. Use `Unknown` rather than treating missing liquidity data as clean.
- `manager_thesis_lifecycle` is required when prior filings, consecutive changes, manager thesis sources, 13D escalation, reductions/exits, or post-period company evidence are material to ranking. It should track whether the manager idea appears new, accumulating, thesis-stated, company-confirmed, steady, reduced, exited, stale, or unknown. Use `Unknown` rather than treating a one-quarter snapshot as lifecycle evidence.
- Price-move, price-context, volume/attention, and updated-company-evidence fields feed the Quantitative Chase Filter Thresholds. Use `Unknown` when market data or event context is unavailable and `Not applicable` only when the candidate has no public equity price context.
- `false_positive_flags` should capture traps from the False-Positive Library, such as `mega_cap_consensus`, `broad_crowding`, `hedge_fund_hotel`, `social_hype`, `stale_activist_event_path`, `activist_exit_or_reduction`, `liquidity_distorted_after_disclosure`, `low_float_market_impact`, `one_quarter_snapshot_overranked`, `stale_manager_thesis`, `manager_exit_or_reduction`, `price_appreciation_only`, `tiny_quant_position`, `ambiguous_options`, `merger_arb`, `ticker_mapping_uncertain`, `fund_letter_without_matching_exposure`, or `passive_13g_not_activist`.
- `data_gaps` should list missing information that could change ranking, such as missing prior filing, missing multi-quarter lifecycle history, missing manager thesis source/date, missing price context, missing liquidity/float/spread context, unverified CUSIP mapping, missing amended filing comparison, unavailable post-period company events, unresolved activist next proof point/event-path status, unresolved thesis-linkage question/disconfirming checks, unresolved consensus/crowding quality, or unresolved 13F completeness/confidential-treatment status.
- `signal_score` and `score_cap` come from the Formal Internal Signal Scorecard. The capped score governs Alpha Queue eligibility.
- `alpha_queue_status` controls final handling: `Rank` for visible Best Stock Leads eligibility, `Watch` for interesting but not clean enough, `Demote` for lower-signal/context, and `Omit` for non-researchable or immaterial items.
- `demotion_reason` is required when `alpha_queue_status` is `Watch`, `Demote`, or `Omit`.
- `best_next_command` should be `None` unless the candidate is a clean company-level research lead with a specific diligence gap. Follow shared best-next-command routing from `rules/OUTPUT.md` and artifact-state inputs from `rules/ARTIFACTS.md`.

The schema is a data discipline layer, not an output requirement and not an automatic ranking engine. A structurally complete candidate can still be demoted if the signal is stale, crowded, unmappable, options-heavy, not company-specific, or lacks a clear Midas research question.

## Manager Profile Layer

Maintain an internal Manager Profile when enough public evidence exists to calibrate a fund manager's disclosure signal across runs. The profile should feed `manager_archetype`, `archetype_confidence`, manager-edge scoring, false-positive detection, and Alpha Queue burden of proof.

The Manager Profile is internal by default. Do not show it in standard tracker output unless full/audit mode, artifact export, or an explicit user request requires it. Do not use it for copy-trading, performance marketing, buy/sell framing, or claims that a manager's historical ownership predicts future returns.

Profile data should be source-backed or clearly labeled as inferred. Use `Unknown` when a field cannot be verified and `Not applicable` when a field does not apply. If profile evidence is stale, weak, or inconsistent with the latest filing, current disclosure evidence controls.

Recommended internal object:

```yaml
manager_profile:
  manager_name: string | Unknown
  cik: string | Unknown | Not applicable
  known_strategy: string | Unknown
  archetype: concentrated_fundamental | sector_specialist | activist_event_driven | quality_compounder | deep_value_distressed | multi_strategy_trading | quant_factor_systematic | passive_index_like | unknown
  archetype_confidence: High | Medium | Low
  average_position_count: number | Unknown | Not applicable
  top_10_concentration: number | Unknown | Not applicable
  median_position_weight: number | Unknown | Not applicable
  typical_turnover: Low | Medium | High | Unknown
  manager_eligibility:
    manager_universe_status: Eligible | Watch | Excluded | Unknown
    cloneability_grade: High | Medium | Low | Unknown
    average_holding_period: Long | Medium | Short | Unknown
    turnover_pattern: Low | Medium | High | Unknown
    position_count_band: Concentrated | Moderate | Diversified | Very diversified | Unknown
    filing_lag_pattern: Early | Normal | Late | Unknown
    public_thesis_availability: Frequent | Occasional | Rare | None | Unknown
    strategy_purity: High | Medium | Low | Unknown
    exclusion_reason: string | None
  sector_specialty: list[string]
  activist_history: Yes | No | Mixed | Unknown
  13D_frequency: Frequent | Occasional | Rare | None | Unknown
  13F_signal_quality_history: High | Medium | Low | Mixed | Unknown
  common_false_positive_patterns: list[string]
  prior_Midas_leads: list[string]
  prior_lead_quality_notes: string | Unknown
  profile_status: New | Established | Stale | Needs Review
  profile_confidence: High | Medium | Low
  style_drift_flags: list[string]
  notes_on_signal_interpretation: string | Unknown
  data_gaps: list[string]
  last_updated: YYYY-MM-DD | Unknown
  source_citations: list[string]
```

Profile rules:

- Build or refresh the profile from public evidence such as firm strategy disclosures, investor letters, historical 13F concentration, number of positions, turnover, 13D/13G frequency, Form 4/related disclosures when relevant, sector exposure, and prior Midas tracker notes when available.
- `prior_Midas_leads` and `prior_lead_quality_notes` measure research usefulness only. They must not become performance claims, copy-trading claims, or proof that future disclosed positions will work.
- `average_position_count`, `top_10_concentration`, `median_position_weight`, and `typical_turnover` should calibrate materiality. A routine small position from a broad quant manager should face a higher bar than a new meaningful position from a concentrated fundamental manager.
- `manager_eligibility` stores the reusable manager-level eligibility view. It should be evidence-backed by historical holding period, turnover, position count, filing lag, thesis availability, and strategy purity. Refresh it when the manager's strategy, disclosure behavior, or profile evidence changes.
- `sector_specialty`, `activist_history`, and `13D_frequency` should calibrate whether a disclosure is inside the manager's plausible edge. Do not infer activism from a passive 13G or manager reputation alone.
- `common_false_positive_patterns` should carry recurring manager-specific traps, such as tiny quant baskets, options overlays, merger-arb/event-spread positions, passive ownership filings, stale legacy holdings, or price-appreciation-only changes.
- `profile_status` should become `Stale` or `Needs Review` when the manager's strategy, portfolio structure, personnel, mandate, or disclosure pattern appears to have changed.
- `style_drift_flags` should identify evidence that the current filing may not fit the historical profile, such as sudden concentration change, new sector focus, activist filing by a historically passive filer, or large options exposure by a manager usually focused on common equity.
- The profile informs ranking but does not override candidate-level evidence. A strong manager profile cannot rescue an unmappable, stale, non-company-specific, or source-weak candidate.
- When profile evidence is unavailable, use `unknown` archetype with Low confidence and rely more heavily on disclosure type, source cleanliness, position normalization, company-level setup, and Chase Filter.

## Eligible Manager Universe / Cloneability Gate

Use this hard pre-ranking gate to decide whether a manager is eligible to produce high-priority Alpha Queue leads from 13F-only evidence. This is P0 fund-manager tracker discipline because serious 13F research depends on the manager universe: long-term, concentrated, lower-turnover, thesis-driven managers produce cleaner public-disclosure research signals than high-turnover, multi-strategy, quant, passive, or disclosure-noisy filers.

The gate is about public-disclosure signal quality and cloneability of the filing evidence, not copy-trading. `Cloneability` means the manager's public disclosures are more likely to contain durable, researchable, company-level signal. It does not mean Midas should copy holdings, forecast manager returns, or treat manager ownership as a recommendation.

Required internal object is embedded in both `manager_profile.manager_eligibility` and the run-level `alpha_queue_candidate.manager_eligibility` snapshot:

```yaml
manager_eligibility:
  manager_universe_status: Eligible | Watch | Excluded | Unknown
  cloneability_grade: High | Medium | Low | Unknown
  average_holding_period: Long | Medium | Short | Unknown
  turnover_pattern: Low | Medium | High | Unknown
  position_count_band: Concentrated | Moderate | Diversified | Very diversified | Unknown
  filing_lag_pattern: Early | Normal | Late | Unknown
  public_thesis_availability: Frequent | Occasional | Rare | None | Unknown
  strategy_purity: High | Medium | Low | Unknown
  exclusion_reason: string | None
```

Universe-status rules:

- `Eligible`: the manager's public disclosures appear usable for high-priority Alpha Queue leads when candidate-level evidence also clears source cleanliness, position normalization, best-idea/active-tilt gate, company-level setup, post-period checks, Chase Filter, and scorecard caps.
- `Watch`: the manager may produce research leads, but 13F-only candidates require stronger evidence, usually top-quartile-or-better best-idea status, unusual normalized change, repeated accumulation, explicit thesis context, or unusually clean undercovered company-level setup.
- `Excluded`: the manager should not produce top Alpha Queue candidates from 13F-only evidence by default. Routine rows from high-turnover, passive/index-like, quant/factor, very diversified, multi-strategy/trading-oriented, or disclosure-noisy managers should be demoted, watched, or omitted unless separate clean company-level evidence exists.
- `Unknown`: do not guess eligibility. Unknown manager eligibility should block top Alpha Queue promotion from 13F-only evidence by default until enough manager-profile evidence is gathered. Unknown is not a permanent exclusion; it can be upgraded after source-backed profile work.

Exception rule:

An `Excluded` or `Unknown` manager should not produce a top Alpha Queue candidate from 13F-only exposure unless there is separate clean company-level evidence or unusually strong normalized change. Acceptable exceptions include:

- Fresh 13D or 13D/A with parsed Item 4 substance.
- Form 4 or other ownership evidence that is directly company-specific and source-clean.
- Fund letter or official investor communication with matched disclosed exposure.
- Unusually large normalized share or portfolio-weight increase.
- Move from immaterial to meaningful allocation.
- Concentrated position that is clearly atypical for that filer.
- Verified company-specific event setup.
- Repeated accumulation across filings.
- Clean undercovered company-level setup with strong source confidence.

Gate rules:

- Apply manager eligibility before best-idea/active-tilt scoring and before final Alpha Queue ranking.
- A top-5 position from an `Excluded` or `Unknown` manager does not automatically outrank a lower-ranked but cleaner signal from an `Eligible` manager.
- Famous-manager status is not eligibility. A famous filer with high turnover, very diversified holdings, low strategy purity, or poor source cleanliness can be `Watch`, `Excluded`, or `Unknown`.
- `cloneability_grade` should be based on public-disclosure usefulness: holding period, turnover, concentration, filing timeliness, strategy purity, repeatability of thesis signals, and availability of source-backed thesis context.
- `average_holding_period`, `turnover_pattern`, `position_count_band`, and `filing_lag_pattern` should use historical 13F comparisons when practical. Use `Unknown` when insufficient data is available.
- `public_thesis_availability` should reflect whether investor letters, official communications, conference materials, or other source-clean thesis context is publicly available. It should not substitute for current position evidence.
- `strategy_purity` should distinguish focused fundamental or specialist strategies from blended, trading-oriented, multi-strategy, passive/index-like, or factor/systematic books.
- Standard output should not show the raw `manager_eligibility` object by default. Translate it into plain English only when material, such as demoting a candidate because the manager is broad, high-turnover, passive/index-like, or not yet eligibility-verified.
- The gate feeds score caps, manager-edge scoring, `alpha_queue_status`, `demotion_reason`, and final Alpha Queue ranking.

## 13F Completeness / Confidential Treatment Gate

Use this source-integrity gate for every material 13F-HR or 13F-HR/A candidate before best-idea/active-tilt scoring and final Alpha Queue ranking. This is P0 fund-manager tracker discipline because confidential treatment or omitted holdings can make the public 13F table incomplete, and the omitted positions may be the most information-sensitive positions in the manager's portfolio.

This gate is distinct from ordinary 13F delay. Delay is timing risk; confidential treatment and omissions are public-disclosure completeness risk. Both can weaken a filing signal, but they should be tested separately.

Required internal object is embedded in `alpha_queue_candidate.filing_completeness`:

```yaml
filing_completeness:
  public_13f_complete: Yes | No | Unknown | Not applicable
  confidential_treatment_requested: Yes | No | Unknown | Not applicable
  public_summary_indicates_omissions: Yes | No | Unknown | Not applicable
  confidential_release_detected: Yes | No | Unknown | Not applicable
  omitted_holdings_risk: Low | Medium | High | Unknown | Not applicable
  completeness_caveat: string | None
```

Completeness-risk rules:

- Do not assume the public 13F is complete when completeness cannot be verified. Use `Unknown` rather than `Yes`.
- `Low` omitted-holdings risk means there is no indication of omitted confidential holdings after checking available filing metadata, public summary information, and amendments/release history when practical.
- `Medium` omitted-holdings risk means completeness cannot be verified, metadata is ambiguous, or public summary information leaves a material gap.
- `High` omitted-holdings risk means confidential treatment is requested or indicated, the public summary suggests omissions, an amended/released filing later reveals previously confidential holdings, or other source evidence shows the public table was incomplete.
- A later confidential release should be treated as a separate source event, not silently merged into the original public 13F without labeling.
- If confidential treatment is indicated, public 13F completeness is uncertain, public summary data indicates omissions, or omitted-holdings risk is Medium/High, reduce `source_confidence` when material.
- If the candidate still ranks despite Medium/High omitted-holdings risk, carry a visible caveat in standard output using existing candidate caveat fields rather than exposing the raw object.
- If the lead depends mainly on visible 13F rank, concentration, portfolio-weight interpretation, or best-idea status, uncertain or incomplete public 13F data should cap the score, Watch/Demote the candidate, or require a stronger supporting disclosure.
- Ranking may still be allowed when another clean company-level disclosure supports the lead, such as 13D/13D-A, 13G/13G-A when properly parsed, Form 4, company filing naming the holder, official investor communication, fund letter with matched exposure, later confidential release that clarifies the omitted position, or unusually strong normalized change in the public filing with caveat.
- Do not automatically penalize every filing from a manager that has ever requested confidential treatment. Apply the gate filing-specifically unless there is evidence of a recurring manager-level completeness pattern.
- Standard output should not show the raw `filing_completeness` object by default. Translate material completeness issues into plain-English caveats such as incomplete public 13F risk, confidential-treatment indication, or omitted-holdings risk.
- The gate feeds source confidence, source-cleanliness scoring, score caps, `alpha_queue_status`, `demotion_reason`, visible caveat logic, and final Alpha Queue ranking.

## Thesis Linkage / Variant-View Extraction Gate

Use this gate for every candidate before Best Stock Leads promotion. This is P0 fund-manager tracker discipline because the Alpha Queue should be a research queue of testable company-level hypotheses, not a smarter-looking holdings list. The central question is not only "what did the manager disclose?" but "what company-level question might this disclosure point Midas toward, and what evidence would disconfirm it?"

This gate separates filing-backed evidence from Midas inference. A filing may prove a disclosed position, ownership event, size, rank, change, filing date, and source type. It does not by itself prove manager intent, current ownership, future returns, company quality, mispricing, or attractiveness. If no explicit manager-thesis source exists, describe the hypothesis as Midas inference, not as the manager's stated thesis.

Required internal object is embedded in `alpha_queue_candidate.thesis_linkage`:

```yaml
thesis_linkage:
  filing_backed_signal: string
  inferred_manager_hypothesis: string | Unknown
  explicit_manager_thesis_source: 13D Item 4 | fund_letter | investor_presentation | official_investor_communication | company_filing | none | Unknown
  variant_view: string | Unknown
  company_research_question: string
  disconfirming_evidence_to_check: list[string]
  best_next_command: !research | !financials | !risk | !thesis | None
```

Gate rules:

- `filing_backed_signal` must state only what the source evidence supports, such as disclosed new position, increased share count, ownership percentage, Item 4 language, matched fund-letter exposure, or corrected/amended filing evidence.
- `inferred_manager_hypothesis` may state what Midas thinks the manager might be underwriting, but must be labeled as inference unless backed by `explicit_manager_thesis_source`.
- `explicit_manager_thesis_source` should be `none` when there is no manager-stated thesis source; do not upgrade inference into stated intent.
- `variant_view` should identify the plausible research angle versus consensus or obvious surface narrative when available. `Unknown` is allowed, but weakens Alpha Queue attractiveness unless the company research question and disconfirming checks are strong.
- `company_research_question` must be a specific filing-aware company-level question, not a promotional conclusion. It should point to a business-model, financial-quality, risk, scenario, or full-packet diligence need.
- `disconfirming_evidence_to_check` must list concrete evidence that could break or weaken the hypothesis, such as customer loss, margin compression, dilution, leverage stress, stale ownership, segment slowdown, regulatory overhang, valuation/rerating, or lack of disclosed recurrence.
- If `company_research_question` is missing, vague, or not company-level, the candidate should not appear in Best Stock Leads.
- If `disconfirming_evidence_to_check` is missing or empty, the candidate should not appear in Best Stock Leads.
- If `filing_backed_signal` is vague, promotional, or mixes inference with evidence, Watch/Demote the candidate until the evidence/inference split is fixed.
- A candidate can still appear in Watch, Lower-Signal Items, Disclosure Tape, or be omitted when thesis linkage is incomplete.
- Standard output should not show the raw `thesis_linkage` object by default. Translate it into a concise lead rationale, research question, and visible caveat only when useful.

Command-routing rules:

- The thesis-linkage gate routes to `!research` only when the company-level question is primarily about business-model identity, revenue mechanics, customers/end markets, geography, recurrence, pricing power, cyclicality, or basic filing-backed company understanding.
- Use `!financials` when the gap is margin quality, cash conversion, leverage, dilution, valuation basics, or financial durability.
- Use `!risk` when the gap is downside fragility, financing/refinancing, execution, regulatory/legal, concentration, options ambiguity, activist/event risk, or post-rerate risk.
- Use `!thesis` when enough base research exists and the next step is scenario framing or explicit variant-view construction.
- Recommend `!research` first when multiple gaps require broad coverage, then the remaining core commands as needed.
- Use `None` when there is no clean researchable company-level next step.
- Follow shared best-next-command routing from `rules/OUTPUT.md` and artifact-state inputs from `rules/ARTIFACTS.md`; do not embed the `!research` workflow or force `!research` as the default.
- The gate feeds company-level setup, manager-edge interpretation, signal score, score caps, `alpha_queue_status`, `demotion_reason`, and final Alpha Queue ranking.

## Qualified Consensus vs Broad Crowding Gate

Use this gate when multiple managers, broad 13F ownership, hedge-fund-hotel risk, or social attention could affect ranking. This is P0 fund-manager tracker discipline because serious ownership research distinguishes qualified independent accumulation from generic crowding. Consensus is useful only when it comes from the right manager set and clean position behavior; broad ownership by everyone is not the same signal.

This gate modifies the Chase Filter rather than replacing it. Vertical moves, crowded trades, and overextended setups still matter, but high-quality independent accumulation by long-term, concentrated, source-clean managers can improve a lead's research priority when the company-level thesis linkage is also strong.

Required internal object is embedded in `alpha_queue_candidate.consensus_quality`:

```yaml
consensus_quality:
  qualified_manager_count: number | Unknown
  qualified_manager_add_count: number | Unknown
  qualified_manager_best_idea_count: number | Unknown
  broad_13f_holder_count: number | Unknown
  hedge_fund_hotel_risk: Low | Medium | High | Unknown
  social_hype_risk: Low | Medium | High | Unknown
  consensus_type: Qualified independent accumulation | Broad crowding | Mixed | Unknown
  qualified_consensus_basis: string | Unknown
```

Consensus-quality rules:

- `qualified_manager_count` should count only eligibility-cleared managers or properly excepted managers whose strategy, holding period, concentration, source cleanliness, and position behavior make their disclosures relevant to the Alpha Queue. Do not count all filers indiscriminately.
- `qualified_manager_add_count` should count qualified managers with clean new positions, meaningful increases, repeated accumulation, or other normalized add behavior. Do not treat price-appreciation-only value increases as adds.
- `qualified_manager_best_idea_count` should count qualified managers where the position appears top-quartile-or-better, unusually active, or otherwise best-idea-like under the Best-Idea / Active-Tilt Gate.
- `broad_13f_holder_count` is context, not validation. Broad ownership alone should not improve ranking and may lower discovery quality.
- `hedge_fund_hotel_risk` should rise when the name is widely owned across many hedge funds, event funds, fast-money funds, or consensus books such that incremental ownership signal is likely crowded or already discovered.
- `social_hype_risk` should rise when the name is heavily promoted, narrative-saturated, or attention-spiking on social/promotional channels. Social hype is never thesis evidence by itself.
- `Qualified independent accumulation` can improve ranking only when the managers are source-clean, eligibility-cleared or properly excepted, independent enough to avoid circular copying, and the adds/weights are meaningful.
- `Broad crowding` should increase crowding risk, reduce discovery score, and usually Watch/Demote the candidate unless thesis linkage and company evidence are unusually strong.
- `Mixed` requires a visible caveat when material: qualified accumulation may exist, but broad crowding, hedge-fund-hotel risk, or social hype limits discovery quality.
- `Unknown` should not be used as a positive ranking factor. If consensus quality cannot be assessed, leave the candidate to stand on its own filing, manager, thesis-linkage, source-cleanliness, and Chase Filter evidence.
- Mega-cap consensus, index-like ownership, quant baskets, passive holder counts, and famous-manager overlap do not equal qualified consensus.
- Do not frame qualified consensus as a buy/sell recommendation, expected-return claim, or instruction to copy a manager cluster. It only changes research-priority confidence.
- Standard output should not show the raw `consensus_quality` object by default. Translate material consensus/crowding findings into plain English such as "qualified independent accumulation," "broad crowding," "hedge-fund-hotel risk," or "social-hype caveat."
- The gate feeds discovery score, Chase Filter, source-cleanliness interpretation, company-level setup, false-positive flags, score caps, `alpha_queue_status`, `demotion_reason`, and final Alpha Queue ranking.

## Best-Idea / Active-Tilt Gate

Use this gate internally to decide whether a disclosed name is likely one of the manager's best ideas or merely a portfolio row. This is P0 fund-manager tracker discipline because broad all-holdings data is much noisier than concentrated, active-tilt, high-conviction holdings. Midas should not promote routine disclosed holdings as if they were high-conviction manager signals.

The gate measures disclosure-signal quality only. It is not a buy/sell recommendation, expected-return claim, manager-performance claim, or instruction to copy a manager's portfolio. Best-idea status means the position is more relevant as a research lead, not that the stock is attractive today.

Required internal object is embedded in `alpha_queue_candidate.best_idea_signal`:

```yaml
best_idea_signal:
  manager_position_percentile: number | Unknown | Not applicable
  top_3_position: Yes | No | Unknown | Not applicable
  top_5_position: Yes | No | Unknown | Not applicable
  top_10_position: Yes | No | Unknown | Not applicable
  top_quartile_position: Yes | No | Unknown | Not applicable
  active_weight_vs_benchmark: number | Unknown | Not applicable
  active_weight_percentile: number | Unknown | Not applicable
  best_idea_status: Top idea | Top 5 | Top 10 | Top quartile | Routine | Unknown | Not applicable
```

Gate rules:

- For 13F-only candidates, a high Alpha Queue rank usually requires `best_idea_status` of `Top quartile` or better unless there is a strong event signal, explicit thesis context, or unusual repeat accumulation.
- `Top idea`, `Top 5`, `Top 10`, and `Top quartile` should be based on current disclosed portfolio rank, portfolio-weight percentile, manager concentration, and when available benchmark-relative active weight. Do not rely on raw dollar value alone.
- `Routine` means the row appears ordinary for that manager: not high-ranked, not top quartile, not unusually active versus benchmark, not newly meaningful, and not supported by a separate event or thesis signal.
- `Unknown` is acceptable when the portfolio universe, benchmark, or current/prior rank cannot be verified. Unknown best-idea status should raise the burden of proof for 13F-only promotion rather than silently passing.
- Active weight is useful only when a relevant benchmark or peer baseline is available. If no defensible benchmark exists, set active-weight fields to `Unknown` or `Not applicable`; do not invent benchmark weights.
- A non-top-quartile 13F-only position can still rank if other evidence is strong: fresh 13D/13G/Form 4 signal, explicit fund-letter thesis context, unusual repeat accumulation, a move from tiny to meaningful allocation, verified company-specific event setup, or clear undercovered research asymmetry.
- A top position can still be demoted by stale filing data, post-period evidence that weakens the signal, Chase Filter, weak company-level setup, unresolved ticker mapping, options ambiguity, source weakness, crowding, or lack of a specific diligence question.
- For broad quant, passive/index-like, multi-strategy, or highly diversified managers, require stronger best-idea/active-tilt evidence before promoting 13F-only positions. A large reported row in a broad portfolio is not automatically a best idea.
- For concentrated fundamental, sector-specialist, or activist/event-driven managers, best-idea status may carry more signal when it fits the Manager Profile and the disclosure is source-clean.
- Standard output should not show the raw `best_idea_signal` object by default. Translate it into plain English only when material, such as noting that a candidate appears to be a top disclosed position or demoting a name because it appears to be routine portfolio exposure.
- The gate feeds Conviction / Change, Manager Edge / Relevance, score caps, `alpha_queue_status`, `demotion_reason`, and final Alpha Queue ranking.

## Manager Thesis Lifecycle Monitoring

Use this lifecycle layer to track whether a manager's idea appears to be born, reinforced, paused, reduced, contradicted, stale, or exited over time. This is P0 fund-manager tracker discipline because a one-quarter snapshot is not enough to judge the research value of a disclosed idea.

The lifecycle layer is internal by default. Standard output should not show the raw `manager_thesis_lifecycle` object unless full/audit mode, artifact export, or an explicit user request requires it. Translate material lifecycle conclusions into plain English through `Why it matters:`, `Why it might not be a strong signal:`, `Lower-Signal Items`, rank order, or candidate caveats.

Required internal object is embedded in `alpha_queue_candidate.manager_thesis_lifecycle` when material:

```yaml
manager_thesis_lifecycle:
  lifecycle_stage: New | Accumulating | Thesis stated | Confirmed by company evidence | Holding steady | Reduced | Exited | Thesis stale | Unknown
  quarters_held: number | Unknown
  consecutive_adds: number | Unknown
  consecutive_reductions: number | Unknown
  last_manager_thesis_mention_date: YYYY-MM-DD | Unknown | Not applicable
  last_company_evidence_update: YYYY-MM-DD | Unknown
  thesis_lifecycle_implication: Rank | Watch | Demote | Omit
  lifecycle_caveat: string | None
  next_lifecycle_proof: string | Unknown
```

Lifecycle rules:

- A one-quarter new position should usually rank below repeat accumulation or a matched thesis disclosure unless the new position is already a top active idea, unusually large for that manager, tied to a live event, supported by explicit manager-thesis evidence, or has an unusually strong company-level research question with clean source context.
- `New` means newly disclosed in the reviewed source period. It is a fresh signal, but not automatically a durable manager thesis.
- `Accumulating` requires source-backed repeated adds, portfolio-weight increases, or position becoming more meaningful across multiple filings or related disclosures. Do not infer accumulation from market-value appreciation alone.
- `Thesis stated` requires an explicit manager source such as a fund letter, investor presentation, interview, public thesis note, or 13D Item 4 language. Midas inference alone does not qualify.
- `Confirmed by company evidence` means later company filings, earnings, contract wins, regulatory milestones, financing, settlement, or other company-level evidence supports the research question. It does not mean the stock is a buy or that the manager thesis is proven.
- `Holding steady` means the position appears maintained without material add/reduction. It can support context but is usually weaker than fresh accumulation, explicit thesis, or live event escalation.
- `Reduced` and `Exited` usually Watch/Demote/Omit as forward tracker leads unless the reduction/exit itself creates a useful research question or separate fresh company-level evidence keeps the setup relevant.
- `Thesis stale` applies when the last manager thesis mention is old, no follow-through appears in filings, company evidence has moved on, or the original event/research premise no longer has a current proof point.
- `Unknown` is not positive. If multi-quarter history, thesis-source date, or exit/reduction status cannot be checked and the lifecycle matters, caveat, cap, Watch, or Demote rather than treating the candidate as clean.
- `quarters_held`, `consecutive_adds`, and `consecutive_reductions` should use comparable source periods when available. Use `Unknown` if prior filings are missing, incomparable, confidential-treatment-limited, or affected by unresolved ticker/CUSIP mapping.
- `last_manager_thesis_mention_date` should be `Not applicable` when no explicit manager-thesis source exists; do not invent dates from Midas inference.
- `last_company_evidence_update` should reference the latest material company evidence checked when it affects lifecycle status. Use `Unknown` if material company evidence could not be checked.
- `thesis_lifecycle_implication` feeds final Alpha Queue treatment: `Rank` for clean lifecycle-supported leads, `Watch` for interesting but incomplete lifecycle evidence, `Demote` for reduced/stale/one-quarter-only weak leads, and `Omit` for exited or non-researchable items.
- `lifecycle_caveat` is required when lifecycle status is `Reduced`, `Exited`, `Thesis stale`, `Unknown`, or otherwise materially limits ranking.
- `next_lifecycle_proof` should identify what would advance or re-open the setup, such as another add in the next 13F, an updated fund-letter thesis, 13D escalation, company evidence confirming the research question, or evidence that a reduction/exit is complete.
- Do not imply the manager still owns a position beyond the latest verified disclosure.
- Do not treat price appreciation as lifecycle confirmation. Price action can affect Chase Filter but does not prove manager thesis development.

Scorecard integration:

- Conviction / Change should improve for repeat accumulation, top-active-position status, position becoming meaningfully larger, 13D escalation, matched thesis disclosure, or company evidence that supports the research question.
- Disclosure Quality improves when lifecycle evidence comes from clean comparable filings, amendments, related disclosures, fund letters, or explicit manager sources.
- Manager Edge / Relevance improves when the lifecycle fits the manager's known strategy, holding period, sector edge, activist/event-driven pattern, or public thesis history.
- Company-Level Setup improves only when lifecycle evidence maps to a current company-specific research question and disconfirming checks.
- Source Cleanliness / Data Integrity declines when prior filings, amendment history, confidential-treatment context, thesis dates, mapping, or exit/reduction status are unresolved.
- Chase Filter / Rerating Context should still penalize already-processed, stale, or post-rerate lifecycle signals.

## 13D / 13G Intelligence Parser

Use formal 13D / 13G parsing for any material Schedule 13D, 13D/A, 13G, or 13G/A signal before applying the Formal Internal Signal Scorecard or final Alpha Queue ranking. The parser prevents oversimplifying a 13D as automatically activist/bullish or a 13G as automatically meaningless/passive.

This parser is internal by default. Do not show the full parser object in standard tracker output unless full/audit mode, artifact export, or an explicit user request requires it. In normal output, translate the parser into plain English inside `Why it matters:`, `Why it might not be a strong signal:`, `Lower-Signal Items`, and candidate-level best-next-command routing.

Recommended internal object:

```yaml
ownership_event_parser:
  source_type: 13D | 13D/A | 13G | 13G/A | Unknown
  accession_number: string | Unknown
  filing_date: YYYY-MM-DD | Unknown
  event_date: YYYY-MM-DD | Unknown | Not applicable
  amendment_number: number | Unknown | Not applicable
  beneficial_ownership_pct: number | Unknown
  ownership_change_pct: number | Unknown | Not applicable
  purpose_of_transaction: string | Unknown
  source_of_funds: string | Unknown | Not applicable
  item_4_plan_or_proposal: string | Unknown | Not applicable
  board_governance_language: Present | Absent | Unknown
  strategic_review_sale_merger_language: Present | Absent | Unknown
  capital_allocation_proposal: Present | Absent | Unknown
  financing_or_debt_language: Present | Absent | Unknown
  litigation_or_regulatory_hook: Present | Absent | Unknown
  group_members: list[string]
  derivative_or_swap_exposure: Present | Absent | Unknown
  standstill_or_cooperation_agreement: Present | Absent | Unknown
  prior_13d_g_relationship: New | Existing | Prior Passive 13G | Prior Activist 13D | Unknown | Not applicable
  event_type: Governance pressure | Board representation | Strategic review / sale process | Capital allocation pressure | Restructuring / operational pressure | Merger / acquisition / tender | Financing / recapitalization | Passive ownership disclosure with no clear event path | Mixed / unclear | Unknown
  event_type_confidence: High | Medium | Low
  parser_summary: string | Unknown
  alpha_queue_implication: Rank | Watch | Demote | Omit | Unknown
  data_gaps: list[string]
  source_citations: list[string]
```

Parser rules:

- Treat form type as the starting point, not the conclusion. A 13D is not automatically a clean activist campaign; a 13G is not automatically irrelevant.
- For 13D / 13D/A, parse Item 4 substance before assigning an event type. Generic reservation-of-rights language should not be treated as a concrete plan by itself.
- For 13G / 13G/A, identify whether the filing is a passive ownership disclosure, qualified institutional disclosure, or other non-activist ownership signal when available. Do not infer governance pressure without supporting language or related filings.
- `beneficial_ownership_pct` should use the disclosed percentage and issuer share-count basis when available. If the basis is unclear or stale, label the gap.
- `ownership_change_pct` should compare against the prior 13D/13G relationship when available. Do not infer change when only the current filing is available.
- `purpose_of_transaction`, `source_of_funds`, and Item 4 content should drive event interpretation more than filer reputation.
- `board_governance_language`, `strategic_review_sale_merger_language`, `capital_allocation_proposal`, `financing_or_debt_language`, and `litigation_or_regulatory_hook` should be marked `Present` only when the filing or cited agreement includes concrete language. Use `Unknown` when the source was not parsed deeply enough.
- `group_members` should preserve named group members and reporting persons when disclosed. Do not collapse a group filing into a single manager conviction signal without noting group structure.
- `derivative_or_swap_exposure` should distinguish economic exposure from direct common-share ownership. Derivatives, swaps, options, or other synthetic exposure require caveats and may reduce source cleanliness or conviction/change scoring.
- `standstill_or_cooperation_agreement` should identify whether the filing includes a cooperation agreement, standstill, settlement, board appointment agreement, voting agreement, or similar governance contract. These can increase event specificity but may also limit escalation.
- `amendment_number` and `prior_13d_g_relationship` should identify whether the filing is a fresh ownership/event signal, a continuation, a passive-to-activist transition, an activist-to-passive transition, or a mechanical amendment.
- `event_type` should classify the dominant event path. Use `Mixed / unclear` when several possible paths exist without enough specificity.
- A high-signal 13D can still be demoted by Chase Filter, weak company-level setup, stale amendment content, derivative-heavy exposure, unresolved issuer mapping, or lack of a clear diligence question.
- A 13G can still become a useful research lead when the ownership signal is fresh, large, source-clean, company-specific, undercovered, and tied to a clear Midas research question.
- Missing facts must be `Unknown` or `Not applicable`. Do not invent percentages, group members, amendment numbers, plans, proposals, agreements, event dates, or prior relationships.

Scorecard integration:

- Disclosure Quality should improve when the ownership event is fresh, source-clean, directly company-specific, and clearly parsed.
- Conviction / Change should improve when beneficial ownership or the filing relationship changed materially and can be compared to prior 13D/13G evidence.
- Manager Edge / Relevance should improve when the event type fits the Manager Profile, such as a known activist filing a concrete governance proposal.
- Company-Level Setup should improve when the event creates a clear research question: sale process, board fight, capital allocation pressure, financing/recap risk, operational turnaround, litigation/regulatory catalyst, or ownership overhang.
- Source Cleanliness should decline when exposure is derivative-heavy, group structure is unclear, amendment content is stale, the source chain is weak, or issuer/security mapping is unresolved.
- Chase Filter should still check whether the 13D/13G event has already been priced in through a vertical post-filing move or crowded public attention.

## 13D Event-Path Implementation Tracker

Use this tracker for material 13D and 13D/A activist/event-path candidates after parsing Item 4 and related agreements, and before final Chase Filter, scorecard, and Alpha Queue ranking. A 13D is path-dependent: the research value depends on whether the event path is progressing, stalled, settled, opposed, reduced, exited, or already priced in.

This tracker is internal by default. Standard output should not show the raw `activist_event_path` object unless full/audit mode, artifact export, or an explicit user request requires it. Translate material findings into plain English through `Why it matters:`, `Why it might not be a strong signal:`, `Lower-Signal Items`, and candidate-level best-next-command routing.

Required internal object is embedded in `alpha_queue_candidate.activist_event_path`:

```yaml
activist_event_path:
  event_stage: Initial filing | Demand made | Company response | Cooperation agreement | Board seat | Proxy fight | Strategic review | Sale process | Capital return | Litigation | Reduced stake | Exited | Unknown
  next_required_proof: string
  company_response_status: Supportive | Opposed | Settlement | No response | Unknown
  event_path_alive: Yes | No | Unclear
  event_path_staleness: Fresh | Aging | Stale | Unknown
  last_event_path_source: string | Unknown
  last_event_path_date: YYYY-MM-DD | Unknown
  event_path_caveat: string | None
```

Event-path rules:

- A 13D should not remain highly ranked after a major post-filing move unless `event_path_alive` is `Yes`, `next_required_proof` is specific, the path is not stale, and no later evidence shows reduced stake, exit, failed process, or thesis invalidation.
- `event_stage` should be based on the latest source-backed step, not only the initial 13D filing. Check later 13D/A, 8-Ks, company releases, proxy materials, cooperation agreements, settlement terms, litigation filings, sale-process updates, financing disclosures, and Form 4/ownership changes when material.
- `next_required_proof` must identify the next evidence item that would confirm progress: board appointment, settlement terms, proxy materials, sale-process update, bidder interest, transaction announcement, capital-return authorization, financing close, litigation milestone, company response, or updated ownership disclosure. Use `Unknown` only when the next proof point cannot be identified.
- `company_response_status` should separate activist demand from company response. Do not infer company support from activist language or price movement.
- `event_path_alive: Yes` requires a current source-supported path or unresolved implementation milestone. `No` applies when the activist exited/reduced materially, the campaign ended, the sale/review/settlement path failed, or the original event premise no longer exists. `Unclear` should not be used as a strong positive ranking factor.
- `event_path_staleness` should use the latest event-path source date and materiality. Fresh paths can support ranking; Aging paths require caveat; Stale paths usually Watch/Demote unless a separate fresh disclosure reopens the setup.
- `event_stage: Reduced stake` or `Exited` usually blocks treating the original 13D as a current positive activist lead unless a separate new catalyst exists.
- `company_response_status: Opposed` can keep the event path live, but risk rises and `!risk` may be the better next command.
- `company_response_status: Settlement` or `event_stage: Cooperation agreement` can support ranking only when implementation proof points remain; otherwise the filing reaction may already be priced.
- `event_stage: Strategic review` or `Sale process` requires explicit next proof: process update, board action, bidder interest, transaction announcement, financing, regulatory step, or termination.
- Do not treat price reaction as proof that the activist thesis is valid, progressing, or still alive.
- If `event_path_alive` is `No`, `event_path_staleness` is `Stale`, or `next_required_proof` is missing/Unknown after a major post-filing move, cap, Watch/Demote, move to Lower-Signal Items, or omit from Best Stock Leads depending on remaining company-level research value.
- The gate feeds thesis linkage, post-period event status, Chase Filter, Company-Level Setup, Source Cleanliness, score caps, `alpha_queue_status`, `demotion_reason`, and final Alpha Queue ranking.

Scorecard integration:

- Disclosure Quality improves when later event-path sources are fresh, official, and specific.
- Conviction / Change improves when the activist maintains or increases stake through implementation milestones; it weakens when the activist reduces or exits.
- Manager Edge / Relevance improves when the path fits the manager's activist/event-driven profile and historical edge.
- Company-Level Setup improves when the event path creates a clear research question and next proof point.
- Source Cleanliness declines when the path depends on stale Item 4 language, unverified media reports, unclear group structure, or missing latest company response.
- Chase Filter should penalize major post-filing moves unless the event path remains live with a specific next proof point.

## Post-Period Event Status Labels

Use these labels internally after checking material post-period company evidence. The goal is to prevent stale or contradicted filing signals from ranking too cleanly. This is a company-evidence freshness layer, not a buy/sell judgment and not proof of manager intent.

Post-period review should check, when available and material:

- latest earnings releases, 10-Q, 10-K, and 8-Ks;
- guidance, outlook changes, margin/cash-flow updates, and management commentary;
- dilution, equity offerings, convertible issuance, financing, refinancing, covenant, liquidity, or debt events;
- M&A, tender offers, strategic review updates, asset sales, spin-offs, restructurings, or bankruptcy events;
- customer wins/losses, contract awards, cancellations, backlog changes, or concentration events;
- regulatory, legal, litigation, investigation, approval, denial, or compliance updates;
- management, board, auditor, control, or governance changes; and
- later related 13D/13G/Form 4/fund-letter/company disclosures when they directly affect the filing signal.

Allowed `post_period_event_status` values:

| Status | Meaning | Default Alpha Queue treatment |
|---|---|---|
| Supports | Later company evidence strengthens, confirms, or clarifies the filing signal. | Can support ranking or soften Chase Filter concerns, but still requires source-clean company-level research setup. |
| Neutral | No material company-level update found, or updates do not materially change the filing read. | Candidate may rank if other Alpha Queue evidence is strong. |
| Weakens | Later company evidence makes the filing signal less attractive as a current research lead. | Must show a caveat or be demoted/capped; do not present as a clean fresh lead. |
| Invalidates | Later company evidence directly contradicts the filing thesis or removes the event path/research premise. | Usually Demote/Omit unless a clearly updated, source-backed thesis exists. |
| Unknown | Post-period evidence could not be checked or source access was insufficient. | Must show a caveat or be demoted/capped; do not treat as clean. |

Application rules:

- `Supports` requires specific later company evidence, not just favorable price action, manager reputation, or market narrative.
- `Neutral` means no material post-period company evidence changed the read; it does not mean diligence is complete.
- `Weakens` includes later evidence such as guidance cuts, margin deterioration, dilution, financing stress, contract loss, regulatory setback, litigation escalation, failed transaction path, or management/governance instability that makes the original filing signal less useful today.
- `Invalidates` requires direct contradiction of the filing thesis, such as a terminated sale process after a sale-process thesis, failed financing after a financing-resolution thesis, delisting/bankruptcy path that breaks the ordinary-equity setup, or company disclosure showing the assumed event path no longer exists.
- `Unknown` is not a neutral result. If post-period evidence could not be checked, the candidate must carry a caveat, score cap, `Watch`/`Demote` treatment, or lower ranking depending on materiality.
- If status is `Weakens`, `Invalidates`, or `Unknown`, the candidate must show a visible caveat in standard output or be demoted to `Lower-Signal Items`, `Watch`, `Demote`, or `Omit` internally. Do not leave it as an uncaveated Best Stock Leads candidate.
- Post-period status feeds `post_period_event_status`, `updated_company_evidence_after_move`, `chase_filter`, `score_cap`, `alpha_queue_status`, `demotion_reason`, and the Formal Internal Signal Scorecard.
- Keep raw status labels internal by default. In standard output, translate material status into plain-English wording through `Why it might not be a strong signal:`, `Lower-Signal Items`, or ranking rationale.

## Liquidity / Float / Market-Impact Researchability Gate

Use this gate when liquidity, float, market cap, spread risk, post-filing volume reaction, or market-impact distortion is material to whether a disclosed idea remains a clean fresh tracker lead. This is a researchability and disclosure-distortion check, not a company-quality judgment and not a buy/sell/timing instruction.

Illiquid names can carry stronger information signals, but they can also be more vulnerable to front-running, copycat reaction, spread widening, float squeeze/overhang, and post-disclosure price distortion. Confidential-treatment-sensitive or later-revealed holdings deserve extra care when the position appears illiquid or low-float.

This gate is internal by default. Standard output should not show the raw `liquidity_researchability` object unless full/audit mode, artifact export, or an explicit user request requires it. Translate material findings into plain English through `Why it might not be a strong signal:`, `Lower-Signal Items`, rank demotion, or candidate caveats.

Required internal object is embedded in `alpha_queue_candidate.liquidity_researchability` when material:

```yaml
liquidity_researchability:
  market_cap_band: Mega | Large | Mid | Small | Micro | Unknown
  avg_dollar_volume_30d: number | Unknown
  free_float: number | Unknown
  float_ownership_pressure: Low | Medium | High | Unknown
  post_filing_volume_spike: Yes | No | Unknown
  bid_ask_spread_risk: Low | Medium | High | Unknown
  liquidity_researchability_status: Clean | Watch | Demote | Unknown
  liquidity_caveat: string | None
  market_impact_research_question: string | Unknown
```

Gate rules:

- A candidate can be fundamentally interesting but should be demoted as a fresh tracker lead if liquidity is too poor and the post-filing reaction already distorted the setup.
- Low liquidity does not automatically make a company bad. It can increase information value while reducing clean current researchability after disclosure publication.
- `market_cap_band`, `avg_dollar_volume_30d`, `free_float`, and `bid_ask_spread_risk` should be source-backed when available. Use `Unknown` when unavailable; do not treat missing liquidity data as `Clean`.
- `float_ownership_pressure` should capture whether disclosed holders, qualified-consensus overlap, activist/group ownership, insider ownership, or other known ownership concentration creates low-float pressure or overhang risk. Use `Unknown` when float ownership cannot be checked.
- `post_filing_volume_spike` should identify whether filing publication appears to have changed trading volume materially. Do not infer business validation from a volume spike.
- `liquidity_researchability_status: Clean` requires no obvious liquidity/float/spread/post-filing-distortion issue that changes fresh-lead usefulness.
- `Watch` applies when liquidity is thin, spread risk is elevated, float pressure is meaningful, or a post-filing reaction requires caution but does not invalidate the research question.
- `Demote` applies when liquidity is poor, float pressure/spread risk is high, and post-filing price or volume reaction appears to have distorted the setup enough that the candidate is no longer a clean fresh tracker lead.
- `liquidity_caveat` is required when status is `Watch`, `Demote`, or `Unknown` and liquidity materially affects ranking.
- `market_impact_research_question` should ask whether the disclosure itself distorted the setup, such as: `Did the 13F/13D publication create enough buying pressure to distort current researchability?`
- Micro-cap, illiquid, distressed, merger-arb, and event-driven situations require extra caution. Do not let noisy low-liquidity price action alone determine ranking, but do not ignore market-impact risk either.
- If `avg_dollar_volume_30d`, `free_float`, or spread risk is `Unknown`, keep the uncertainty visible internally and caveat/demote when material rather than pretending liquidity was checked.
- If float ownership pressure is `High`, require a caveat and consider a cap unless separate fresh company-level evidence keeps the research gap open.
- Qualified independent accumulation can improve signal quality, but high float pressure or market-impact distortion can still reduce fresh-lead researchability.
- Broad crowding, social hype, and hedge-fund-hotel ownership can worsen liquidity/market-impact treatment even if market cap is not small.
- The gate feeds Chase Filter, 13F completeness/confidential-treatment caution, Qualified Consensus vs Broad Crowding, Source Cleanliness, Company-Level Setup, score caps, `alpha_queue_status`, `demotion_reason`, and final Alpha Queue ranking.

Scorecard integration:

- Disclosure Quality can improve when liquidity context is fresh and source-backed, and should weaken when market-impact risk cannot be checked in a liquidity-sensitive setup.
- Conviction / Change should not be boosted solely because a position is large relative to a tiny float; normalize for practical float pressure and disclosure distortion.
- Company-Level Setup can remain strong even when liquidity researchability is weak, but fresh tracker-lead ranking should be capped or caveated.
- Source Cleanliness / Data Integrity declines when float, dollar volume, spread, or post-filing volume reaction data is missing in a liquidity-sensitive candidate.
- Chase Filter / Rerating Context should penalize post-filing price/volume distortion, spread widening, and copycat/crowded reaction when material.

## Quantitative Chase Filter Thresholds

Use these defaults internally when price data is available to make the Chase Filter more consistent. The thresholds are starting points, not rigid automatic decisions. They should discipline Alpha Queue ranking without turning market price action into a filing-backed business-quality judgment.

The Chase Filter evaluates whether the disclosure signal remains useful as a fresh Midas research lead today. A Chase Filter demotion is not a view that the company is bad. It means the filing signal is less useful as a fresh Midas research lead today. A strong company can still be a poor setup if the market has already priced in most of the thesis.

Standard visible output should not show raw `Pass`, `Watch`, or `Demote` labels by default. Translate the result into plain-English caveats in `Why it might not be a strong signal:`, `Lower-Signal Items`, or rank order when material.

Default Chase Filter states:

| State | Default triggers | Default treatment |
|---|---|---|
| Pass | Price move since filing is modest; stock has consolidated after the initial disclosure reaction; or valuation/fundamental work still shows a researchable gap. | Candidate can remain eligible for Alpha Queue ranking if disclosure quality, source cleanliness, and company-level setup are strong. |
| Watch | +20-35% move since filing without updated company evidence; +35-60% move since report-period end; major volume spike or narrative attention after disclosure; interesting signal but valuation needs immediate review. | Usually cap or caveat the candidate, require valuation/fundamental review, and consider `Watch` status or lower ranking unless other evidence keeps the setup fresh. |
| Demote | >60% move since report-period end with no new fundamental support; >40% move since filing within 30 trading days; stock is already widely promoted or consensus-owned; post-period company event materially weakens the thesis. | Usually move to Lower-Signal Items, `Watch`, or `Demote`; do not promote as a fresh Best Stock Leads candidate unless updated company evidence clearly reopens the research gap. |

Application rules:

- Calculate price move from both the filing report-period end and filing date when available. Also review 1M / 3M / 6M / 1Y context when useful and readily available.
- If price data is unavailable, set relevant price fields to `Unknown` and avoid pretending the Chase Filter was computed. Do not force a Pass just because data is missing.
- Treat thresholds as asymmetric guardrails. Crossing a Watch or Demote threshold does not automatically mean the company is unattractive; it means the filing signal may be stale, crowded, or less actionable as a research lead.
- Updated company evidence can override or soften a price-move penalty when it provides fundamental support for the move, such as a new filing, earnings acceleration, financing resolution, contract award, regulatory approval, activist settlement, or other company-specific evidence.
- Post-period company evidence that weakens or invalidates the filing thesis should push toward Watch or Demote even if price action is not extreme.
- Consolidation after an initial disclosure reaction can move a candidate from Watch toward Pass when the company-level research gap remains real.
- Major volume spikes, broad social-media promotion, crowded narrative attention, or obvious consensus ownership should push toward Watch or Demote even if the price move is below the numerical thresholds.
- For illiquid, micro-cap, distressed, merger-arb, or event-driven situations, use the thresholds carefully and emphasize source quality, liquidity, event path, and company-level risk. Do not let a noisy low-liquidity move alone determine ranking.
- The Chase Filter feeds the `chase_filter`, `score_cap`, `alpha_queue_status`, `demotion_reason`, and the Chase Filter / Rerating Context bucket in the Formal Internal Signal Scorecard.

## Formal Internal Signal Scorecard

Use this scorecard internally to make Alpha Queue ranking more consistent and computable. It scores the quality of the fund-manager disclosure as a Midas research lead, not expected return, buy/sell attractiveness, current ownership, or portfolio suitability.

Standard visible output should not show the numeric scorecard by default. Show it only in full/audit mode or when the user explicitly asks for scoring detail. In normal output, translate the scorecard into rank order, `Why it matters:`, `Why it might not be a strong signal:`, `Lower-Signal Items`, and candidate-level best-next-command routing.

Total score: **100 points**

| Bucket | Points | What it measures |
|---|---:|---|
| Disclosure Quality | 20 | Filing/disclosure type, freshness, common equity versus options, clean issuer/ticker/CUSIP mapping, amendment status, and source confidence. |
| Conviction / Change | 20 | New position, share-count increase, portfolio-weight increase, concentration change, position becoming meaningful, repeated accumulation, or fresh 13D/13G/Form 4 ownership signal. |
| Manager Edge / Relevance | 15 | Fit with manager archetype, sector/domain edge, concentration, strategy relevance, activist/event-driven relevance, or disclosed thesis fit. |
| Company-Level Setup | 20 | Clear research question, undercovered or misunderstood company, non-obvious thesis, company-specific rather than basket exposure, and useful setup classification context. |
| Source Cleanliness / Data Integrity | 10 | Correct filer/CIK/accession/account scope, no double-counting, related disclosures labeled, corporate actions verified, and source chain clean enough to support ranking. |
| Chase Filter / Rerating Context | 15 | Price move since period end and filing date, 1M/3M/6M context when useful, crowding, vertical-move risk, post-rerate risk, valuation sensitivity, and whether the signal remains researchable today. |

Internal interpretation:

- **80-100:** Strong Alpha Queue candidate; eligible for visible `Best Stock Leads` if no hard cap applies.
- **65-79:** Researchable candidate; rank only if differentiated or directly tied to the filing thesis.
- **50-64:** Context or lower-signal candidate unless the company-level research question is unusually strong.
- **Below 50:** Usually screen out or mention only as context when material.

Scoring discipline:

- Treat the score as a ranking aid, not an automatic decision rule.
- Keep filing signal strength separate from current research attractiveness.
- A high score requires both disclosure support and a company-level research question.
- Do not let manager fame, position size, ticker popularity, or social-media interest substitute for evidence.
- If a hard cap applies, the capped score governs Alpha Queue eligibility even when raw bucket points are higher.

Hard caps:

| Condition | Maximum internal score | Default treatment |
|---|---:|---|
| Broad ETF, index exposure, or vague basket | 40 | Screen out from company-level Best Stock Leads by default. |
| Ambiguous options-only or hedge-like exposure | 55 | Demote unless clean company-specific direction and research question are supported. |
| Stale unchanged legacy holding | 50 | Lower-priority/context unless another fresh disclosure supports the signal. |
| Ticker, issuer, CUSIP, or corporate-action mapping unresolved | 60 | Label mapping uncertainty; do not silently promote. |
| No clear company-level research question | 55 | Do not rank in Best Stock Leads by default. |
| One-quarter new position with no repeat accumulation, no stated thesis, no top-active-position evidence, and no live event | 70 | Usually rank below repeat accumulation or matched thesis disclosure unless the company-level research question is unusually strong. |
| Reduced or exited position with no fresh company-level research question | 55 | Do not rank as a positive Best Stock Leads candidate; use context or omit unless the reduction/exit itself creates a research question. |
| Thesis stale or contradicted by company evidence | 60 | Demote unless new evidence reopens the setup. |
| Major vertical post-period or post-filing move with no consolidation | 70 | Usually Watch/Demote through Chase Filter; explain timing/rerating caveat. |
| 13D event path stale, unclear, reduced/exited, or missing next proof after major move | 65 | Do not rank as a clean activist Best Stock Leads candidate unless separate fresh company-level evidence reopens the setup. |
| Illiquid / micro-cap candidate with poor dollar volume and distorted post-filing reaction | 65 | Fundamentally interesting but usually Watch/Demote as a fresh tracker lead unless separate fresh evidence reopens the setup. |
| Illiquid candidate with unresolved ticker/float/liquidity data and major post-filing move | 60 | Do not rank as a clean Best Stock Leads candidate until liquidity and market-impact risk are checked. |
| Weak, stale, conflicted, or low-confidence source chain | 65 | Demote or caveat until source cleanliness improves. |
| Manager archetype is quant/factor/passive and the position is small or routine | 60 | Require unusual change or separate company-specific evidence before promotion. |

Use the scorecard after the Alpha Queue Gate and before final ranking. If a candidate fails a gate item, do not rescue it with a high numeric score; keep it in lower-priority/context or omit it. If a lower raw score candidate ranks above a higher raw filing-signal candidate, the reason should be company-level research attractiveness, cleaner source quality, better Chase Filter outcome, or stronger fit with the filing thesis.

## Ranking Principle

Final ranking should combine the Formal Internal Signal Scorecard with disclosure signal quality, conviction/change, manager edge fit, company-level research setup, source cleanliness, and Chase Filter judgment.

Do not rank by current reported market value alone. Do not rank by manager fame alone. Do not rank by ticker popularity alone.

## Relationship to Setup Classification and Scoring

Tracked activity can help identify a research candidate, but it should not by itself create a high company score.

Use `rules/CLASSIFICATIONS.md` and `rules/SCORING.md` when classification or scoring is required.

Do not create source-specific global classes inside this contract.
