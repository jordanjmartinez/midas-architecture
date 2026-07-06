# !gems Output Contract

## Purpose

`!gems` returns a concise hidden-gem candidate list. It is a discovery and prioritization command, not a full research report, recommendation, trading command, price-target command, or watchlist mutation command.

Use this file for command-specific presentation. Do not duplicate the full global rules here. Apply these shared standards by reference:

- `/home/jordan/.hermes/profiles/midas/rules/OUTPUT.md` for general MIDAS output style and market-data display.
- `/home/jordan/.hermes/profiles/midas/rules/SOURCES.md` for source discipline.
- `/home/jordan/.hermes/profiles/midas/rules/CLASSIFICATIONS.md` for approved setup classifications and modifiers.
- `/home/jordan/.hermes/profiles/midas/rules/SCORING.md` for Hidden-Gem Overlay and Evidence Confidence behavior.
- `/home/jordan/.hermes/profiles/midas/rules/RERATING.md` for rerating, post-rerate, overextension, vertical-move, consolidation, valuation-reset, market-absorption, and price-action discipline.
- `references/artifact-index.md` for command-local artifact/index mechanics and `/home/jordan/.hermes/profiles/midas/rules/ARTIFACTS.md` for global artifact standards.
- `/home/jordan/.hermes/profiles/midas/rules/METRICS.md` when financial, valuation, market-cap, enterprise-value, liquidity, or price-performance metrics appear.

## Output Modes

### Broad Mode

Use for `!gems` with no theme. Return a concise general candidate list, normally up to 5 candidates, and save to the broad gems artifact path defined by `SKILL.md` / `references/artifact-index.md`.

### Theme Mode

Use for `!gems [theme]`. Return a concise candidate list for the normalized theme, normally up to 5 candidates, and save to the theme artifact path defined by `SKILL.md` / `references/artifact-index.md`.

### Theme/Subtheme Mode

Use for `!gems [theme] [subtheme]`. Return a concise candidate list for the normalized theme/subtheme, normally up to 5 candidates, and save to the theme/subtheme artifact path defined by `SKILL.md` / `references/artifact-index.md`.

### No-Clean-Candidate Mode

Use when the screen produces no clean hidden-gem candidates. Do not force candidate picks when evidence is weak, setups are overextended, names are social-only, or primary-source validation is insufficient.

## Default Output

Use this shape for normal successful chat output. Keep it concise, Telegram-readable, and thesis-first. Normal output should make candidates feel like research leads, not label or score dumps.

```md
# 💎 Hidden Gems | [Theme/Subtheme]

Summary:
[1–3 sentences explaining whether a clean hidden gem was found, whether names are only researchable or watch-only, and the main caveat. Do not force a gem and do not use recommendation framing.]

## [Hidden-Gem Candidates or Researchable Leads]

[Use `## Hidden-Gem Candidates` only when candidates actually clear clean hidden-gem gates. Use `## Researchable Leads` when candidates are researchable but not clean hidden gems. Use exactly one of these headings.]

1. [TICKER] | [Company]

Why it matters:
[Short business/setup reason.]

Evidence:
[Primary/company evidence or clear source-backed reason it surfaced.]

Founder-led:
[Yes / No / Unknown — source-backed person/status and source type when known.]

Why it might not be clean:
[Main fragility, rerating issue, weak evidence, crowding, obviousness, missing information gap, source limitation, unresolved entity/security ambiguity, or promotional/social-source dependence.]

Best next command:
`!research TICKER`

## Watch Only

- [TICKER] | [Company] — [short reason.]

Not included: [TICKER] — [short reason, only when there is a specific user-facing reason to mention a screened-out name.]

## Source Note

[Compact caveat about primary/company sources, discovery inputs, market-data/rerating limitations, and social/crowding not being used as thesis proof.]

Saved to: workspace/gems/[actual-path].md
Updated index: workspace/gems/index.md
```

Do not force every section if it would add clutter. The candidate list, Source Note, and artifact confirmation should remain readable first. Do not add source-gathering workflow, candidate-screening workflow, scoring calculation workflow, artifact-writing procedure, command routing, schemas, or proof-packet language to normal output.

Title and opening rules:

- Use `# 💎 Hidden Gems | [Theme]` as the visible chat title.
- Do not use `MIDAS Gems` as the visible report title.
- Use a pipe separator, not an em dash.
- Keep the theme Title Case when possible.
- Place the short `Summary:` directly under the title.
- Use the visible `Summary:` label in normal `!gems` chat output.
- Keep the summary short; do not expand it into a full report.
- The summary should state whether a clean hidden gem was found, whether names are only researchable or watch-only, the main caveat, and the no-recommendation boundary when needed.

Section-title rules:

- Use exactly one normal lead-section heading: `## Hidden-Gem Candidates` or `## Researchable Leads`.
- Use `## Hidden-Gem Candidates` only when candidates actually clear clean hidden-gem gates.
- Use `## Researchable Leads` when candidates are researchable but not clean hidden gems.
- Do not use `## Best Candidates / Researchable Leads`.
- Use `## Watch Only` for names worth monitoring but not strong enough for the main researchable section.
- Do not pair Watch Only with Screened Out in the normal section title.
- Screened-out names should generally be omitted from normal output unless there is a specific user-facing reason to mention them.
- If a screened-out name is mentioned in normal output, use a short plain-English note such as `Not included: [TICKER] — [short reason].`
- Do not make `Screened Out` a normal-output section heading unless explicitly required by the user or audit mode.
- If no clean gem exists, say so in the `Summary:` and do not force a clean-gem section.

## Candidate List Rules

- Show 1–5 candidates by default.
- Do not pad the list if fewer clean candidates exist.
- Rank by hidden-gem quality, not just business quality, theme exposure, market cap, market excitement, or recent stock momentum.
- Do not produce full company reports per candidate.
- Do not use overwide tables by default.
- Do not turn candidate cards into metric dumps, source dumps, or label-heavy field dumps.
- Keep detailed source notes, score breakdowns, screened-out reasoning, and full supporting detail in the saved artifact unless the user asks for more in chat.

## Concise Candidate Format

Preferred chat format:

```md
1. [TICKER] | [Company]

Why it matters:
[Short business/setup reason.]

Evidence:
[Primary/company evidence or clear source-backed reason it surfaced.]

Founder-led:
[Yes / No / Unknown — source-backed person/status and source type when known.]

Why it might not be clean:
[Main fragility, rerating issue, weak evidence, crowding, obviousness, missing information gap, source limitation, unresolved entity/security ambiguity, or promotional/social-source dependence.]

Best next command:
`!research TICKER`
```

Use this thesis-first order by default:

- `[TICKER] | [Company]`
- `Why it matters:`
- `Evidence:`
- `Founder-led:` for main candidates; include when relevant and source-supported elsewhere
- `Why it might not be clean:`
- `Best next command:`

Avoid default cards that repeatedly foreground labels such as `Category`, `Score`, `Main risk`, `Monitor`, `Thesis impact`, `Setup / Confidence`, `Hidden-Gem Overlay`, `Confidence`, or `Setup Classification`. Use plain-English synthesis and section placement to communicate candidate status in normal output.

## Founder-Led Display

Include `Founder-led:` in normal candidate cards for main candidates when source-backed or after a reasonable source-backed check returns unclear status.

Acceptable values:

- `Founder-led: Yes — [Name], founder/CEO, based on [source type].`
- `Founder-led: Yes — [Name], founder/executive chair, based on [source type].`
- `Founder-led: No — [Name], current CEO; founder no longer appears to lead day-to-day operations, based on [source type].`
- `Founder-led: Unknown from reviewed sources.`

Rules:

- `Unknown from reviewed sources` may be used only after a reasonable source-backed check.
- Do not default to `Unknown from reviewed sources` without checking.
- Do not infer founder-led status from social media, vibes, market narrative, ticker popularity, or unsourced web snippets.
- Founder-led status is supporting context only, not thesis proof and not a promotion gate by itself.
- Omit the line only if it would add clutter and founder/operator status is not relevant to the setup; do not omit it to avoid doing the source-backed check for main candidates.
- If included, use primary/company sources where available, such as proxy statements, company leadership pages, filings, or official biographies.

## Scoring Display

In normal `!gems` output, do not show Hidden-Gem Overlay scores by default. Scores are internal, audit-only, artifact-level, or user-requested unless the user explicitly asks for score detail.

When a user explicitly asks for score detail, user-facing chat display should use:

```md
Hidden-Gem Overlay: [score]/25
```

or, when extra clarity is useful:

```md
Hidden-Gem Overlay Score: [score]/25
```

Do not use legacy score labels in user-facing chat output. General scoring standards are governed by `/home/jordan/.hermes/profiles/midas/rules/SCORING.md`; command-local Hidden-Gem Overlay behavior, score caps, and promotion/demotion logic are governed by `contracts/hidden-gems.md`.

Score display rules:

- Do not show `Hidden-Gem Overlay: [score]/25` in normal candidate cards by default.
- Do not show scores as the visible reason a candidate appears in normal output.
- Use `/25`; do not convert to percentages, `/10`, decimals, or star ratings.
- Include Evidence Confidence when a score is displayed.
- Keep score secondary to the thesis/evidence/fragility explanation whenever it is user-requested or audit-only.
- Evidence Confidence should be at least as prominent as the raw score.
- Do not place score before `Why it matters:` or `Evidence:`.
- Score may be omitted for screened-out candidates unless it materially clarifies the demotion.
- For weak-evidence names, use plain wording such as `Score withheld because primary-source validation is incomplete.` when score detail is requested.
- Apply score caps and downgrades when evidence is weak, social-only, promotional, overextended, fragile, or valuation support is missing.
- Do not present a score as a recommendation.
- Do not make score appear to be the reason for promotion.
- Do not allow famous investor ownership, influencer attention, social hype, or market excitement to justify a high score by itself.
- Optional Global Research Score should not appear by default; include it only when explicitly justified by the command context and evidence base.

## Classification Display

In normal `!gems` output, do not show setup classification labels by default in each candidate card. Communicate candidate status through prose and section placement:

- `## Hidden-Gem Candidates` means candidates cleared clean hidden-gem gates.
- `## Researchable Leads` means candidates are interesting enough for deeper work but not clean hidden gems.
- `## Watch Only` means names are worth monitoring but not strong enough for the main researchable section.

Use approved classifications and modifiers from `/home/jordan/.hermes/profiles/midas/rules/CLASSIFICATIONS.md`, with rerating/post-rerate modifiers and discipline inherited from `/home/jordan/.hermes/profiles/midas/rules/RERATING.md`. Do not invent recommendation-like labels.

Classification labels may still appear in audit mode, saved artifacts, or user-requested score/classification detail. When explicitly requested, acceptable display patterns include:

```md
Setup / Confidence: Hidden-Gem Candidate | Confidence: B | Hidden-Gem Overlay: [score]/25
```

```md
Setup / Confidence: Hidden-Gem Candidate; Early Rerating | Confidence: B | Hidden-Gem Overlay: [score]/25
```

```md
Setup / Confidence: Watchlist / Awaiting Better Setup; Post-Rerate / Overextended | Confidence: C | Hidden-Gem Overlay: [score]/25
```

Use modifiers selectively. Do not overload the chat response with long modifier chains.

Display headings such as `Hidden-Gem Candidates`, `Researchable Leads`, and `Watch Only`, plus audit bucket names such as `Promoted hidden-gem candidates`, `Researchable candidates`, `Lower-signal / watch-only`, and `Post-rerate watch-only`, are candidate-decision buckets or section headings, not official Setup Classification labels and do not imply watchlist mutation.

## Evidence Confidence Display

In normal `!gems` output, do not show Evidence Confidence grades by default in candidate cards. Evidence Confidence may appear in audit mode, saved artifacts, or when the user explicitly asks for score/classification detail. When a candidate is scored or ranked in those contexts, show:

```md
Confidence: [A/B/C/D]
```

Use `/home/jordan/.hermes/profiles/midas/rules/SCORING.md` for Evidence Confidence definitions.

General display expectations:

- `A` or `B` requires meaningful primary-source or company-source support.
- `C` is appropriate for partial, mixed, incomplete, or inference-heavy evidence.
- `D` is appropriate for weak, stale, promotional, social-only, or mostly unverified evidence.
- Low confidence should cap or downgrade score and classification.
- Do not hide weak confidence behind exciting language.
- If the evidence base is weak enough that a score would imply false precision, withhold the score and explain the evidence limitation in prose when score detail is requested.

## Source Note Behavior

`!gems` may use discovery signals, but material candidate claims should be anchored in primary or company-source evidence when available.

Chat Source Notes should be compact. They should explain the evidence base and limitations without becoming a citation dump.

Preferred examples:

```md
Source Note: Candidates were ranked from primary/company disclosures where available, with market and social/crowding signals treated as supporting context only.
```

```md
Source Note: Evidence is incomplete for several names; social or promotional signals were not treated as thesis proof.
```

Rules:

- Social/crowding sources can help discovery, but must not prove the thesis.
- Promotional sources, influencer mentions, famous-investor ownership, or market excitement are not proof.
- Underdiscovered status should not be assumed without evidence.
- Market data, if displayed, must follow `/home/jordan/.hermes/profiles/midas/rules/OUTPUT.md` `Market-Data Display Rule`.
- Full source detail belongs in the saved artifact when needed for auditability.

## Rerating / Valuation Display

`!gems` should show rerating and valuation discipline without turning chat into a valuation report.

Use concise language such as:

- `pre-rerate`
- `early rerating`
- `post-rerate / overextended`
- `consolidating`
- `awaiting pullback`
- `valuation reset`
- `valuation support unverified`

A hidden gem should not be rewarded just because it already had a vertical move. If a candidate is post-rerate or overextended, the card should make that clear in plain English; internal scoring/classification should reflect it.

If valuation support is not verified, say so plainly. Do not invent valuation support or imply a stock is cheap without evidence.

## Watch Only

Use this section only when useful. Keep it short. Use Watch Only for names worth monitoring but not strong enough for the main researchable section.

Preferred shape when company name is known:

```md
## Watch Only

- TICKER | Company Name — Reason sentence.
```

Preferred shape when company name is not known:

```md
## Watch Only

- TICKER | Reason sentence.
```

Screened-out names should generally be omitted from normal output unless there is a specific user-facing reason to mention them. If mentioned, use:

```md
Not included: TICKER — Reason sentence.
```

Rules:

- Use the pipe separator after the ticker.
- Prefer company name when known: `TICKER | Company Name — Reason`.
- If the company name is not known, use: `TICKER | Reason`.
- Do not insert `watch-only` after the pipe.
- Capitalize the first letter of the reason sentence after the pipe or em dash.
- Keep each watch-only note one sentence.
- Do not make `Screened Out` a normal-output section heading unless explicitly required by the user or audit mode.
- Do not include long mini-reports or default scores for screened-out names.
- Do not imply watch-only names were added to the watchlist.
- Do not use watch-only status as a buy/sell/hold signal.

## Artifact / Index Display

Preserve the current `!gems` artifact and index behavior from `SKILL.md`, `references/artifact-index.md`, and `/home/jordan/.hermes/profiles/midas/rules/ARTIFACTS.md`.

The user-facing reply should show these lines only if the actions actually happen:

```md
Saved to: workspace/gems/[actual-path].md
Updated index: workspace/gems/index.md
```

Rules:

- Do not claim a save unless the artifact was written.
- Do not claim an index update unless the index was updated.
- Use the actual canonical path written.
- Do not expose internal artifact plumbing unless needed to explain a save/update/failure condition.
- Do not imply watchlist mutation.
- Do not auto-add gems to the watchlist.
- Do not treat watchlist status as a buy/sell signal.

## Watchlist Boundary

`!gems` does not mutate the watchlist by default.

Allowed:

```md
Best next command: `!wl add TICKER`
```

only if the user explicitly asks for watchlist-oriented next steps or if it is clearly framed as an optional manual action.

Preferred default:

```md
Best next command: `!research TICKER`
```

Never say or imply that a candidate was added to `data/midas_watchlist.json` unless the user explicitly requested that separate action and it actually happened.

## Failure / No-Candidate Behavior

If the command cannot complete, use:

```md
Unable to complete: [specific issue]

Reason: [why the screen could not run or why required evidence was unavailable.]

Best next step: [adjust theme, broaden/narrow scan, or research a specific ticker.]
```

For no clean candidates, use:

```md
# 💎 Hidden Gems | [Theme]

Summary:
No clean hidden-gem candidates surfaced under the current screen. [Short explanation — weak evidence, overextended setups, social-only signals, insufficient primary-source validation, no clean information gap, or similar.]

## Watch Only

- [TICKER] | [Company] — [optional concise reason if useful.]

Best next step: [adjust screen or run research on a specific ticker.]

Saved to: workspace/gems/[actual-path].md
Updated index: workspace/gems/index.md
```

Only show `Saved to:` and `Updated index:` if those actions actually happened.

Do not force candidate picks when evidence is weak.

## Best Next Command Behavior

Use command-first next steps.

Preferred default:

```md
Best next command: `!research TICKER`
```

Other next commands may be used only when they fit the candidate’s information gap:

- `!financials TICKER` for financial-statement quality or balance-sheet questions.
- `!risk TICKER` for risk-first diligence.
- `!thesis TICKER` only after enough evidence exists to frame a thesis.
- `!wl add TICKER` only as an optional manual action, not as an automatic command.

Do not run the next command unless the user explicitly asks.

## No-Recommendation Guardrails

`!gems` output must not:

- use Buy/Sell/Hold language
- provide price targets
- suggest position sizing
- give trade advice
- call candidates recommendations
- treat social media as proof
- treat a famous investor or influencer mention as proof
- treat market excitement as evidence
- produce full reports per candidate by default
- auto-add candidates to the watchlist
- imply watchlist status is a recommendation

Use language such as:

- `candidate`
- `research candidate`
- `watch-only candidate`
- `screened out`
- `worth deeper research`
- `best next diligence step`

Avoid language such as:

- `buy`
- `sell`
- `hold`
- `strong buy`
- `price target`
- `entry`
- `exit`
- `position size`
- `trade setup`
- `recommendation`


## Optional Audit Output

Use this section only when the user invokes canonical `-audit` mode:

- `!gems -audit`
- `!gems [theme] -audit`
- `!gems [theme] / [subtheme] -audit`

Do not use `--audit` as the canonical trigger. If the user invokes `--audit`, use the short correction: `Use -audit for !gems audit mode.`

Audit output is a no-write runtime verification summary. Normal `!gems` output remains unchanged. Audit output must not become a raw source dump, hidden reasoning, scratch work, tool log, internal prompt dump, giant full research report, or normal saved artifact.

Audit output may include an optional `Candidate Pool / Discovery Provenance` section to show where candidate tickers entered the pool before validation. This provenance section is audit-only and must not appear in normal `!gems` output, which can keep the compact `Source Note`.

Discovery provenance rules:

- Discovery remains flexible; do not create a static universe, hard-code a candidate pool, or restrict discovery to the labels below.
- Use exactly one of these controlled discovery-source labels when the provenance section is shown: `User theme/subtheme text`, `Prior MIDAS artifact/index`, `Filing/company keyword hit`, `Company business-segment match`, `Market-data/screener result`, `Secondary/news context`, `Manual theme adjacency`, `Social/crowding discovery`, `Model/general knowledge`, or `Unknown`.
- Discovery labels are not proof labels, classifications, recommendations, source hierarchy changes, or scoring changes.
- A discovery source can seed a candidate; a validation source must support material claims.
- Prior MIDAS artifacts are prior context, not fresh proof.
- Social/crowding can help discovery but cannot prove a thesis.
- Market data supports rerating, price-action, liquidity, valuation, or screen context; it does not validate the business by itself.
- When market data is used for rerating context, identify the provider/source name and retrieval date or as-of date, and label it context-only. Example: `Yahoo Finance chart data, retrieved 2026-06-20; used only for price-performance context.`
- Every ticker shown in `Candidate Decisions` must also appear in `Candidate Pool / Discovery Provenance` when that section is used.
- If provenance is unclear for a shown candidate, use: `Discovery source: Unknown`; `Validation source: Not materially validated in this audit`; `Rerating source: Not checked` unless a provider/date was used; and `Provenance confidence: Low`.
- `Unknown` discovery source is allowed, but should lower provenance confidence.
- Provenance is in-memory only in audit mode: do not create artifacts, index updates, folders, watchlist mutations, source manifest files, evidence ledger files, proof packets, schemas, or other persisted provenance records.

Audit output may include:

```md
# Gems Audit | [Theme or General]

## Verification Summary
- Mode: [Broad audit / Theme audit / Theme/Subtheme audit]
- Audit purpose: runtime verification only
- Normal output impact: none
- No-write guarantee: [confirmed / blocked]

## Source Contract Used
- Command-local intelligence: `contracts/hidden-gems.md`
- Output display: `OUTPUT.md`
- Artifact/index mechanics: `references/artifact-index.md`
- Inherited standards: global `SOURCES.md`, `SCORING.md`, `CLASSIFICATIONS.md`, `RERATING.md`, `OUTPUT.md`, `ARTIFACTS.md`, and applicable metric rules

## Source / Evidence Summary
- Primary/company evidence: [summary or limitation]
- Secondary/news evidence: [context only]
- Social/crowding evidence: [discovery only, if used]
- Promotional/stale/weak-source limits: [caps/demotions applied]
- Disconfirming evidence considered: [yes/no + short note]

## Candidate Pool / Discovery Provenance
- Ticker: [TICKER]
- Discovery source: [one allowed discovery-source label]
- Validation source: [primary/company or other source class used to support material claims, or limitation]
- Rerating source: [provider/source name + retrieval/as-of date + context-only purpose, or `Not checked`]
- Output role: [promoted hidden-gem candidate / researchable candidate / watch-only / post-rerate watch-only / blocked or screened-out]
- Provenance confidence: [High / Medium / Low + short reason]

## Promotion Gate Results
- Source Authority Gate: [pass/fail/cap + reason]
- Entity / Security Resolution Gate: [pass/fail/cap + reason]
- Hidden-Gem Fit Gate: [pass/fail/cap + reason]
- Business / Financial Validation Gate: [pass/fail/cap + reason]
- Variant View / Information Gap Gate: [pass/fail/cap + reason]
- Rerating / Price-Action Discipline Gate: [pass/fail/cap + reason]
- Integrity / Noise Discount Gate: [pass/fail/cap + reason]

## Scoring / Evidence Confidence Summary
- Hidden-Gem Overlay: [score]/25 or [not scored]
- Evidence Confidence: [A/B/C/D]
- Score caps triggered: [short note]
- Gate override check: scoring did not override failed gates

## Candidate Decisions
- Promoted hidden-gem candidates: [names or none]
- Researchable candidates: [names or none]
- Lower-signal / watch-only: [names or none]
- Post-rerate watch-only: [names or none]
- Blocked / screened-out: [names or none + reason]

## Output Safety Check
- no Buy/Sell/Hold
- no price targets
- no sizing
- no trade advice
- no recommendation framing
- no social proof treated as thesis proof
- no score/classification framed as a recommendation
- no downstream commands auto-run

## Artifact / Index Status
artifact_write_requested: false
artifact_write_performed: false
index_update_requested: false
index_update_performed: false
watchlist_write_requested: false
watchlist_write_performed: false
downstream_command_requested: false
downstream_command_performed: false

No artifact path was created.
No index was updated.
No watchlist was modified.
No saved/index confirmation applies in audit mode.
```

If audit execution is blocked because no-write safety cannot be guaranteed, return a blocked audit result instead of gathering sources or promoting candidates.

Audit output must avoid Buy/Sell/Hold, price targets, sizing, trade advice, recommendation framing, social proof as thesis proof, and score/classification as recommendation.

## Saved Artifact Expectations

The saved artifact can be more detailed than chat. It may include:

- candidate universe notes
- screened-out names
- source detail
- scoring rationale
- rerating / valuation notes
- duplicate/cross-theme handling
- detailed information gaps
- detailed risks
- index update context

The chat response should summarize the artifact, not paste it.

## Final Verification Before Replying

Before finalizing a `!gems` response, verify:

- The response is concise and candidate-oriented.
- The candidate list has 1–5 names by default, or fewer if fewer clean candidates exist.
- No full company reports appear in chat by default.
- Normal candidate cards do not show `Setup / Confidence`, `Hidden-Gem Overlay`, Evidence Confidence grades, or Setup Classification labels by default.
- If the user explicitly asks for scores, candidate scoring uses `Hidden-Gem Overlay` or `Hidden-Gem Overlay Score` and includes Evidence Confidence.
- If the user explicitly asks for classifications or audit mode is active, setup classifications come from the approved global classification system.
- Normal output uses `Summary:`, one lead heading from `## Hidden-Gem Candidates` or `## Researchable Leads`, and `## Watch Only` when a watch-only section is useful.
- Founder-led status is included only when relevant and source-supported, or shown as unknown from reviewed sources when appropriate.
- Rerating/valuation status is not ignored for overextended names.
- Social/crowding/promotion signals are not treated as thesis proof.
- Market data, if present, follows the global Market-Data Display Rule.
- `Saved to:` appears only if the artifact was actually written; never show it in audit mode.
- `Updated index:` appears only if the index was actually updated; never show it in audit mode.
- No watchlist mutation is implied.
- No Buy/Sell/Hold, price target, position sizing, trade advice, or recommendation framing appears.
