# !gems Hidden-Gems Intelligence Contract

## Purpose and Scope

This is the command-local intelligence contract for `!gems` hidden-gem discovery, eligibility, ranking, demotion, scoring interaction, and classification discipline.

This contract defines how `!gems` should decide whether a company is a hidden-gem research candidate, a researchable candidate, watch-only, post-rerate watch-only, or blocked/screened out.

This file does not own visible output templates.

This file does not own artifact write mechanics.

This file does not own global source, scoring, classification, output, metric, or artifact rules.

This file does not own global rerating, post-rerate, overextension, vertical-move, consolidation, valuation-reset, market-absorption, or price-action discipline rules.

This file does not create schemas or persisted packets.

This file does not authorize watchlist mutation.

`SKILL.md` remains the controller / dispatcher.

`OUTPUT.md` remains the visible display authority.

Evals remain behavior tests.

## Authority Boundaries

This contract owns the `!gems` command-local intelligence logic for:

- Source contract.
- Eligibility filters.
- Entity/security resolution.
- Promotion gates.
- Demotion / blocking rules.
- Hidden-Gem Fit discipline.
- Asymmetry and downside-survivability discipline.
- Founder / owner-operator signal discipline.
- Recognition-path discipline.
- Business / Financial Validation discipline.
- Variant View / Information Gap discipline.
- Misunderstood-vs-merely-undiscovered discipline.
- Rerating / post-rerate discipline.
- Liquidity / promotion / weak-disclosure discipline.
- Social / hype / promotional-source limits.
- Evidence Confidence interaction.
- Hidden-Gem Overlay score interaction.
- Classification usage rules.
- Disconfirming evidence.
- No-clean-candidate rule.

This contract does not own:

- Output templates.
- Artifact paths or write mechanics, except by reference to the active artifact authorities.
- Watchlist mutation.
- Registry status.
- Eval test cases.
- Schema definitions.
- Global classification, scoring, source, output, metric, or artifact definitions.

Follow `/home/jordan/.hermes/profiles/midas/rules/CONTRACT_AUTHORITY.md` when deciding whether future additions belong here, in `SKILL.md`, in `OUTPUT.md`, in evals, in docs, in schemas, or in shared global rules.

Rerating-stage, post-rerate, overextension, vertical-move, consolidation, valuation-reset, market-absorption, and price-action discipline inherit from `/home/jordan/.hermes/profiles/midas/rules/RERATING.md`; this contract applies those standards to `!gems` candidate routing and promotion/demotion decisions without redefining them.

## Source Contract

Use primary/company sources first for material candidate claims:

- SEC filings.
- Earnings releases.
- Investor presentations.
- Company press releases.
- Official IR pages.
- Official company data.
- Regulator or exchange filings where applicable.

Secondary/news sources are context only unless corroborated by primary/company evidence.

Social/crowding sources are discovery and crowding inputs only.

Promotional, stale, weak, or conflicted sources must cap, demote, or block candidates depending on materiality.

Material source limitations must be carried into the visible output or saved artifact under the active output/artifact authorities.

Disconfirming evidence must be considered before a candidate is promoted.

Global source standards remain inherited from `/home/jordan/.hermes/profiles/midas/rules/SOURCES.md`; this section only defines the `!gems` command-local source hierarchy and demotion effect.

## Entity / Security Resolution Gate

A candidate cannot be promoted unless identity is clear.

Pass requires:

- Public company/security mapped correctly.
- Ticker, exchange, and security class resolved.
- ADR/common-share/OTC/foreign-listing ambiguity handled when relevant.
- Company name, security, and listing matched to the evidence being used.

Fail / demote behavior:

- Private-company confusion blocks promotion.
- Unresolved entity/ticker mapping blocks promotion or routes the name to watch-only / verification.
- Ambiguous ADR/common-share/OTC/foreign-listing mapping must be resolved before the candidate can be treated as clean.

Scoring cannot override a failed Entity / Security Resolution Gate.

## Eligibility Filters

`!gems` should prefer a small/mid-cap or otherwise underfollowed public-company universe where enough disclosure exists to verify the setup.

Preferred traits:

- Small-cap or mid-cap profile, with strongest fit generally in the existing command-local preferred range.
- Underfollowed, misunderstood, niche, complex, boring, or not grouped with obvious theme winners.
- Non-obvious angle beyond headline theme exposure.
- Clear information gap.
- Company-specific evidence of fundamental underreaction, commercialization progress, operating leverage, asset value, backlog, contracts, customer validation, or strategic progress.
- Adequate disclosure quality and enough liquidity to support deeper research.

Pre-revenue / early-revenue exceptions are allowed only for credible hard-tech, infrastructure, asset-heavy, or deep-tech setups with concrete validation such as contracts, backlog, customer commitments, government awards, commercial pilots, technical milestones, launch cadence, owned infrastructure, permits, funded pipeline, or a clear path to monetization.

Liquidity and promotion risk are eligibility issues, not cosmetic caveats. Poor liquidity, weak disclosure, OTC fragility, promotional behavior, frequent capital raises into stock moves, or retail-attention-driven theses require demotion unless the filing-backed business case is unusually strong.

Special situations can support eligibility only when filings or company disclosures show a real information gap. A spin-off, divestiture, restructuring, asset sale, new management, segment separation, merger integration, or business transition is not enough by itself.

Asymmetry must be concrete. A candidate should have 2-3 specific reasons why the business may be mispriced, what the market may be missing, where the evidence appears, why it may not be reflected yet, and why the stock has not already fully reflected the opportunity.

Direct theme exposure alone is not enough.

Social discovery is not thesis proof.

## Promotion Gates

A candidate must pass the gate stack before it can be promoted. Scoring cannot override a failed gate.

### 1. Source Authority Gate

Passes when material claims are anchored in primary/company evidence or properly corroborated credible sources.

Fails when the candidate depends on social-only, promotional, stale, conflicted, weak, or unverified evidence.

Demotion behavior: cap confidence/score, move to researchable or watch-only, or block if the source base is too weak for promotion.

### 2. Entity / Security Resolution Gate

Passes when the public company/security, ticker, exchange, and security class are resolved and match the evidence.

Fails when ticker/entity mapping is unresolved, confused with a private company, or ambiguous across ADR/common-share/OTC/foreign listings.

Demotion behavior: block promotion or route to watch-only / verification until resolved.

### 3. Hidden-Gem Fit Gate

Passes when the company is underfollowed or underappreciated, has a less obvious beneficiary angle, and is not already a consensus theme winner or social favorite.

Fails when the company is obvious, widely promoted, already commonly associated with the theme, or included only because it is small, cheap, or theme-exposed.

Demotion behavior: move to researchable, watch-only, post-rerate watchlist, or screened-out depending on evidence quality and remaining information gap.

### 4. Business / Financial Validation Gate

Passes when there is credible evidence of business reality: revenue, backlog, contracts, customers, assets, permits, commercialization progress, balance-sheet/runway support, or cash-flow/margin evidence when available.

Fails when the thesis is pure hope, management goal language, unvalidated projections, weak commercialization, or unsupported theme exposure.

Demotion behavior: cap or block promotion; weak commercialization path blocks clean hidden-gem status.

### 5. Variant View / Information Gap Gate

Passes when there is a researchable reason the market may be missing something, backed by filings or company disclosures.

Fails when the thesis is theme-only, obvious, vague, cheap-only, small-only, or lacks a distinct information gap.

Demotion behavior: move to watch-only or screened-out unless the information gap can be verified.

### 6. Rerating / Price-Action Discipline Gate

Passes when the candidate is pre-rerate, early-rerate, or has consolidated after a move while fundamentals continue improving.

Fails when the stock is vertical, parabolic, momentum-only, or already post-rerate with no strong remaining information gap.

Demotion behavior: post-rerate names usually become watch-only unless filing-backed evidence supports remaining asymmetry; momentum-only names are screened out.

### 7. Integrity / Noise Discount Gate

Passes when the setup is not dependent on hype, promotional financing, social attention, conflicted sources, or recommendation-like framing.

Fails when promotional noise, hype, weak disclosure, unresolved disconfirming evidence, or investment-recommendation framing overwhelms the research case.

Demotion behavior: cap, demote, or block; never let a noisy setup become a clean hidden-gem candidate through score inflation.

## Demotion and Blocking Rules

Demote, cap, or block candidates for:

- Social-only evidence.
- Hype-only thesis.
- Promotional microcaps, weak-disclosure microcaps, OTC/penny-stock style setups, or promotion-driven moves.
- Obvious mega-cap / consensus theme winners.
- Post-rerate / vertical-chart names without a remaining information gap or consolidation/base-building.
- Weak or stale evidence.
- Unresolved ticker/entity mapping.
- Weak commercialization path.
- Upside dependent only on multiple expansion, financing survival, one fragile catalyst, or social hype.
- Insufficient business validation.
- Disconfirming evidence not addressed.
- Score inflation from weak evidence.
- Recommendation-like framing.

A candidate should be blocked rather than promoted when a failed gate is material and unresolved.

A candidate may be demoted instead of blocked when the setup is researchable but incomplete, fragile, post-rerate, or source-limited.

## Hidden-Gem Fit Standard

A `Hidden-Gem Candidate` is a researchable public company that appears underrecognized relative to filing-backed business quality, validation, or asymmetric setup. It must have a specific information gap, a plausible recognition path, a clean or improving rerating setup, and survivable risk. It is not enough for a company to be small, cheap, founder-led, theme-exposed, or discussed on social media.

A hidden-gem setup should generally have:

- Evidence-backed business validation.
- Underrecognition or underappreciation.
- A specific information gap or market misunderstanding.
- A plausible path to recognition.
- An asymmetric setup with survivable downside.
- A clean or improving rerating state.
- Source and fragility discipline.
- A less obvious beneficiary angle, overlooked asset, segment, customer, backlog, niche, operational inflection, or special situation.
- No consensus-winner, heavy-promotion, or social-favorite status.

`Hidden-Gem Candidate` must not be applied to obvious consensus winners, heavily promoted names, or companies already widely associated with the theme.

## Asymmetry Discipline

A hidden-gem setup should have an upside path materially larger than the downside path. High upside alone is not enough; downside survivability is required, and multiple ways to win are preferred.

Positive asymmetry signals include:

- Operating leverage.
- FCF inflection.
- Backlog or contract conversion.
- Margin expansion.
- Hidden segment or asset value.
- Balance-sheet repair.
- Valuation reset with intact business quality.
- Founder/operator execution with evidence.
- Niche enabling-layer exposure to a major demand driver.
- Multiple ways to win.

Negative asymmetry signals that should cap, demote, or block include:

- Upside based only on multiple expansion.
- Severe dilution or refinancing risk.
- Need for external financing to survive.
- One customer, one contract, or one regulatory event that can break the setup.
- One fragile catalyst with no durable business validation.
- Promotional or social-only evidence.
- No primary-source validation.
- Weak liquidity or weak disclosure.
- Post-rerate setup with no consolidation.

## Founder / Owner-Operator Signal

Founder-led or owner-operated status is a modifier, not standalone proof. Do not classify a company as a hidden gem merely because it is founder-led. Owner-operator alignment can improve the setup only when evidence-backed.

For every candidate shown in main normal sections — `## Hidden-Gem Candidates` or `## Researchable Leads` — MIDAS should attempt a founder-led / operator-led status check.

Preferred sources:

- DEF 14A / proxy statement.
- 10-K leadership, directors, ownership, or executive-officer sections if available.
- Company investor-relations leadership page.
- Official company biography.
- S-1 / registration statement for younger companies.
- Recent 8-K for CEO/founder transition when relevant.

The check should answer:

- Is the founder still CEO, executive chair, board chair, or clearly active in executive leadership?
- If not founder-led, who is the current CEO or key operator if source-supported?
- If not disclosed in reviewed sources, say `Unknown from reviewed sources`.

Boundaries:

- Founder-led status is useful context, not a standalone reason to promote.
- Do not treat founder-led status as thesis proof.
- Do not penalize a company solely because it is not founder-led.
- Do not invent founder status when not disclosed.
- If founder-led status is unclear after a reasonable source-backed check, use `Unknown from reviewed sources`.

Positive evidence may include:

- Meaningful economic ownership.
- Active operational role.
- Disciplined capital allocation.
- Long-term reinvestment with evidence of returns.
- Transparent communication.
- Insider alignment without excessive extraction.
- Evidence-backed execution record.

Founder/operator red flags include:

- Control rights far above economic ownership.
- Dual-class structure with weak accountability.
- Related-party transactions.
- Serial dilution.
- Excessive compensation or extraction.
- Promotional behavior.
- Weak board independence.
- No succession plan.
- Key-person risk.
- Empire-building M&A.

Scoring interaction: founder-led status may improve Business Quality / Validation or Information Gap only when evidence-backed. It should reduce or cap Risk / Fragility / Evidence Quality when governance, dilution, control, succession, or key-person risk is material and not mitigated.

## Business / Financial Validation

At least some credible evidence of business reality is required. Acceptable validation may include:

- Revenue.
- Backlog.
- Contracts.
- Customer validation.
- Assets or permits.
- Commercialization progress.
- Balance-sheet/runway support.
- Cash-flow or margin evidence when available.

Pure hope is not validation.

Management goals are not facts.

A weak commercialization path caps or blocks promotion.

## Variant View / Information Gap

A promoted or researchable candidate must have a researchable reason the market may be missing something, such as:

- Underappreciated segment.
- Overlooked customer/category.
- Hidden asset.
- Misunderstood cyclicality.
- Evidence of inflection not yet reflected in narrative.
- Underreaction to filing-backed facts.

Block or demote:

- Theme-only candidates.
- Widely known winners with no new information gap.
- Candidates where the only argument is cheapness, size, or a hot sector label.

## Recognition Path Requirement

A hidden gem should be underrecognized now, but there must be a plausible path for recognition to improve. Permanently ignored is not enough, and an obscure company with no recognition path should be demoted or screened out.

Recognition paths must connect to business evidence, valuation, risk perception, or future fundamentals. Examples include:

- Backlog conversion.
- Margin inflection.
- FCF inflection.
- Customer / contract validation.
- Segment disclosure becoming clearer.
- Balance-sheet repair.
- Founder/operator execution becoming visible.
- Strategic event.
- Improved liquidity.
- Improved coverage.
- Institutional awareness.
- Old controversy fading while fundamentals stabilize.

## Misunderstood vs Merely Undiscovered

Obscurity alone is not enough. Low coverage alone is not enough. Small cap alone is not enough. Founder-led alone is not enough. Direct theme exposure alone is not enough. There must be a specific market misunderstanding, information gap, or underreaction.

Good information gaps may include:

- Misunderstood segment.
- Hidden asset.
- Margin inflection.
- Backlog conversion.
- Stale controversy.
- Balance-sheet repair.
- Old-business/new-business mismatch.
- Delayed financial impact.
- Customer validation not reflected in narrative.
- Enabling-layer exposure rather than obvious theme exposure.

Bad information gaps include:

- "AI exposure."
- "Small cap."
- "Cheap multiple."
- "Founder-led."
- "People on X like it."
- "Stock is down."
- "Could be acquired."

## Rerating / Post-Rerate Discipline

Global rerating discipline is inherited from `/home/jordan/.hermes/profiles/midas/rules/RERATING.md`; this section only describes `!gems` command-local application.

Post-rerate names can be watch-only if the stock is already vertical or has already reflected much of the thesis.

Momentum alone does not make a hidden gem.

Price action must not substitute for business validation.

A post-rerate name can remain promoted only if the remaining information gap is strong, filing/company-backed, and not already widely understood.

## Rerating State Requirement

Assign every candidate one analytical rerating state:

- Pre-Rerate.
- Early Rerating.
- Consolidating / Base-Building.
- Valuation Reset.
- Post-Rerate / Overextended.
- Hype Spike / Promotion Risk.

Prefer `Pre-Rerate`, `Early Rerating`, `Consolidating / Base-Building`, and `Valuation Reset` when evidence is strong. Penalize `Post-Rerate / Overextended` when valuation support is thin or the thesis is already priced in. `Hype Spike / Promotion Risk` should usually be screened out or severely capped unless primary-source evidence strongly supports a researchable setup. If a post-rerate name is included, explain why it remains researchable despite the rerating.

## Liquidity / Promotion / Weak-Disclosure Discipline

Weak-disclosure microcaps should be capped or screened out. OTC/penny-stock style setups require extra caution. Insufficient reliable public information should lower Evidence Confidence and cap score.

Promotion-driven moves should block or severely cap promotion. Unexplained price/volume spikes without a filing-backed catalyst are warning signs.

Primary sources anchor material claims. Promotional sources must not support business quality, valuation, financial performance, risk, classification, or score.

## Social / Hype / Promotional-Source Limits

Social, X, Reddit, YouTube, Discord, newsletters, influencers, forums, and similar channels are discovery/crowding inputs only.

They cannot prove the thesis.

They cannot support top ranking by themselves.

Promotional-source dependence blocks or severely caps promotion.

High social attention, influencer-driven visibility, newsletter promotion, or retail crowding is a negative hidden-gem signal unless the filing-backed information gap remains strong.

## Evidence Confidence Interaction

Use global evidence-confidence standards by reference and apply this `!gems` command-local interaction:

- A/B confidence can support promoted ranking if all promotion gates pass.
- C confidence is researchable/watch-only unless the evidence base improves.
- D confidence generally blocks top promotion.
- Confidence must affect score caps and candidate bucket.

Evidence confidence does not convert weak, stale, social-only, or promotional evidence into promotion-quality support.

## Hidden-Gem Overlay Score Interaction

The Hidden-Gem Overlay score remains `/25`.

Score ranks research priority, not recommendation quality.

Score cannot override failed gates.

Weak evidence caps score.

Social-only evidence blocks promotion regardless of raw score.

Post-rerate and promotional-risk names are capped or demoted.

Obvious mega-cap or consensus names cannot become clean hidden gems by score alone.

Use the overlay score to discipline ranking across the existing five buckets while preserving global scoring standards from `/home/jordan/.hermes/profiles/midas/rules/SCORING.md`:

1. Business Quality / Validation.
2. Underdiscovered / Non-Consensus Status.
3. Information Gap / Mispricing Driver.
4. Valuation / Rerating Setup.
5. Risk / Fragility / Evidence Quality.

Command-local cap guidance:

- No primary-source validation usually caps Hidden-Gem Overlay at `14/25`.
- Social-only or promotional thesis usually caps at `11/25` and should be classified as screened out or needing primary-source verification.
- Post-rerate with no consolidation caps at `17/25` unless valuation and fundamentals still support the setup.
- Widely followed consensus winners cap the Underdiscovered / Non-Consensus bucket at `2/5`.
- No clear information gap caps the Information Gap / Mispricing Driver bucket at `2/5`.
- Founder-led with material governance or entrenchment risk caps the Risk / Fragility / Evidence Quality bucket unless mitigated.
- Severe liquidity, solvency, or dilution risk requires a cap or a speculative / high-fragility classification.

These caps refine `!gems` ranking only; they do not create a new scoring system, new denominator, or new global scoring rule.

## Classification Usage

Use global Setup Classification rules from `/home/jordan/.hermes/profiles/midas/rules/CLASSIFICATIONS.md`.

`Hidden-Gem Candidate` is command-relevant but must be earned.

Do not invent new classifications.

Use setup modifiers for evidence quality, rerating stage, fragility, or watch-only status.

Classification is not a recommendation.

Candidate buckets and local phrases are routing/status language, not official Setup Classifications. Official Setup Classification labels must come from `/home/jordan/.hermes/profiles/midas/rules/CLASSIFICATIONS.md`, with rerating modifiers/discipline inherited from `/home/jordan/.hermes/profiles/midas/rules/RERATING.md`.

Local status mapping:

- Clean hidden-gem status maps to official Setup Classification `Hidden-Gem Candidate` only if gates pass.
- Researchable candidate is a candidate-decision bucket/status; use an approved Setup Classification separately.
- Lower-signal / watch-only is a candidate-decision bucket/status and often maps to `Watchlist / Awaiting Better Setup` when classification is needed.
- Post-rerate watchlist candidate should not be used as a standalone classification label; use `Watchlist / Awaiting Better Setup` plus a post-rerate/overextended modifier where supported.
- Screened out maps to approved `Screened Out` classification when classification is required.

## Disconfirming Evidence

Before promotion, consider disconfirming evidence including:

- Dilution.
- Balance-sheet weakness.
- Customer concentration.
- Weak commercialization.
- Failed execution.
- Promotional financing.
- No clear theme exposure.
- No durable business validation.
- Valuation/rerating already stretched.
- Contradictory filings or newer sources.

If disconfirming evidence is material and unresolved, cap, demote, or block the candidate.

## Candidate Buckets

Use these buckets to route `!gems` candidate decisions. Official Setup Classification labels must come from `/home/jordan/.hermes/profiles/midas/rules/CLASSIFICATIONS.md`.

- Promoted hidden-gem candidate — passes gates, has primary/company-backed evidence, credible business validation, real information gap, and acceptable rerating/noise discipline.
- Researchable candidate — interesting enough for deeper work but not clean enough for promoted hidden-gem status.
- Lower-signal / watch-only — relevant but weak, fragile, source-limited, crowded, or not yet validated.
- Post-rerate watchlist candidate — relevant company where price action/rerating limits clean hidden-gem status, but future monitoring may be useful.
- Blocked / screened-out — failed a material gate or lacks enough evidence to justify research prioritization.

No-clean-candidate behavior:

- Do not force a gem.
- If no candidate passes gates, output should say no clean candidate found.

## Non-Recommendation Boundary

`!gems` outputs research candidates only.

No Buy/Sell/Hold.

No price targets.

No sizing.

No trade advice.

Scores and classifications are research-prioritization tools only.

## References to Output / Artifacts / Global Rules

`OUTPUT.md` owns visible output.

`references/artifact-index.md` owns command-local artifact/index mechanics.

`/home/jordan/.hermes/profiles/midas/rules/ARTIFACTS.md` owns MIDAS artifact standards.

`/home/jordan/.hermes/profiles/midas/rules/SOURCES.md`, `/home/jordan/.hermes/profiles/midas/rules/SCORING.md`, `/home/jordan/.hermes/profiles/midas/rules/CLASSIFICATIONS.md`, `/home/jordan/.hermes/profiles/midas/rules/RERATING.md`, `/home/jordan/.hermes/profiles/midas/rules/OUTPUT.md`, and `/home/jordan/.hermes/profiles/midas/rules/METRICS.md` remain inherited standards.

Evals test behavior only.
