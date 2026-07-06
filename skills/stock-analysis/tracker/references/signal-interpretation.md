# Tracker Signal Interpretation

This is command-local support for !track. It does not replace GLOBAL.md, SOURCES.md, CLASSIFICATIONS.md, SCORING.md, OUTPUT.md, ARTIFACTS.md, or tracker contracts.

## Authority boundary

References do not own intelligence logic. `contracts/fund-manager.md` and `contracts/politician.md` own mode-specific intelligence logic. SCORING.md owns scoring standards. CLASSIFICATIONS.md owns setup classifications.

## Tracker lead standard

A tracker lead is a research lead only, not an investment recommendation. A disclosure can be interesting and still fail as a company-level thesis.

Useful tracker leads usually have:

- A verified disclosure or filing signal.
- A clear person/fund relevance basis.
- A company-level research question.
- Enough source quality to distinguish fact from inference.
- A reason to research the company beyond famous-owner, politician-trade, or social proof.

Do not automatically promote a ticker because a fund manager, politician, insider, or institution disclosed activity.

## Separate fact, inference, and thesis

- Disclosed fact: what the filing or disclosure actually says.
- Tracker inference: what the change may suggest, with cautious language.
- Company thesis: still unproven until researched through company filings and fundamentals.

Use language such as `may suggest`, `appears consistent with`, `points toward`, and `worth researching`. Avoid `buy`, `bullish proof`, `they know something`, or `copy this trade`.

## Fund-manager signal cues

When data allows, compare current vs prior filing by issuer/security/class/put-call:

- New position.
- Meaningful increase or reduction.
- Exit.
- Concentration or portfolio-weight change.
- Smaller/mid-cap position becoming material.
- Fresh 13D/G or related ownership signal.
- Common-equity signal vs options/hedge ambiguity.

Position size alone should not decide rank. A smaller position can be a better research lead if it is fresher, more company-specific, less crowded, or more tied to the filing thesis.

## Politician/public-official signal cues

Politician disclosures are often useful when they show:

- Newly disclosed or repeated activity.
- Large reported ranges relative to the filer pattern.
- Policy-sensitive or jurisdiction-relevant sectors.
- Committee, executive, procurement, regulatory, or event-window relevance.
- Unusual small/mid-cap or undercovered company-level activity.

Avoid implying wrongdoing, non-public information, or intent unless independent evidence supports it.

## Demotion and noise cues

Move to lower-signal context, caveat, or omit when the signal is:

- Broad ETF, index, basket, hedge, or ambiguous options exposure.
- Tiny, stale, unchanged, or old relative to the current question.
- A famous mega-cap with no new research angle.
- Post-rerate, crowded, or already vertically moved when price context materially weakens current research usefulness.
- Source-weak, convenience-source-only, identity-ambiguous, or failed under the active mode contract.

## Ranking discipline

- Prioritize research usefulness, evidence quality, freshness, and company specificity over fame or disclosed size alone.
- Compare the top candidates against the rest of the filing/disclosure: why these, why not the others?
- Do not create a second visible ranking system. OUTPUT.md controls display, while contracts control promotion logic.
- Best next commands are suggestions only and must not be auto-run.
