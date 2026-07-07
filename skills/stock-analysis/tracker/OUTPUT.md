# Tracker Output Templates

Use these templates for the `tracker` skill outputs.

`SKILL.md` controls command routing, source workflow, watchlist behavior, and high-level rules.
`OUTPUT.md` controls formatting, section order, field placement, and user-facing display shape.
Mode-specific intelligence contracts live under `contracts/`.

## Command

Command: `!track`

Skill File: `skills/stock-analysis/tracker/SKILL.md`

Output File: `skills/stock-analysis/tracker/OUTPUT.md`

Registry Entry: `docs/COMMAND_REGISTRY.md`

Status: `Active`

---

## Registry Consistency

This output contract should match the command’s Registry Metadata block in `skills/stock-analysis/tracker/SKILL.md` and the command row in `docs/COMMAND_REGISTRY.md`.

Expected metadata:

- Command: `!track`
- Aliases: `!show track`, `!track rm`
- Category: `Disclosure Tracking`
- Status: `Active`
- Skill path: `skills/stock-analysis/tracker/SKILL.md`
- Output path: `skills/stock-analysis/tracker/OUTPUT.md`
- Eval file: `evals/tracker.eval.md`
- Classification: `Required`
- Scoring: `Optional`
- Metrics: `Optional`
- Artifacts: `Optional`

If this output file and the registry disagree, treat that as registry drift.

---

For tracker candidate sections, keep candidate lists compact and usually limit ranked names to the most useful items.

For tracker candidate sections, use one final ranked section only, with the mode-specific title defined below.

- Fund-manager standard output uses `## Best Stock Leads` for the visible human-facing ranked section.
- Politician standard output uses `## Best Stock Leads`.

Do not use duplicate ranked sections in standard output. For fund managers, raw filing strength and practical research usefulness are internal Alpha Queue triage inputs, but the visible output label is `Best Stock Leads`. For politicians, raw disclosure strength and company-level research usefulness are internal triage inputs to Best Stock Leads.

For other tracker modes, follow the command-specific section names defined in this file.

Use a simple ranked list by default (`1.`, `2.`, `3.`). Medals are optional only when they improve readability and should only be used for candidates that are genuinely justified.

## Fund Manager Output

Use this format when the tracked person is classified as `Fund Manager`.

Fund-manager output follows these contracts:

- Intelligence / Alpha Queue triage: `contracts/fund-manager.md`
- Display support: `references/output-polish.md`

This file controls the visible fund-manager template: section order, candidate-card labels, conditional sections, and display placement. Detailed triage logic belongs in `contracts/fund-manager.md`.

Keep fund-manager output concise. Do not show empty sections. Normal Telegram output should not show a full `## Source Limits` section; source-limit logic is internal by default and should appear through `What Changed`, `Why it might not be a strong signal:`, `Source Caveat`, ranking, or demotion when relevant.

Fund-manager output must convert raw disclosure signals into one practical research queue:

- Internal filing lens: what changed in the disclosure?
- Internal research lens: which company-level names are useful enough to research today?
- Internal triage result: Alpha Queue
- Visible ranked result: `## Best Stock Leads`

Use `## Lower-Signal Items` only when there are material disclosures worth keeping visible but not worth ranking. Do not add a standalone `Ticker / Corporate-Action Mappings` section; show ticker or corporate-action mapping inline only when it materially affects the read.

Avoid fame-based promotional language by default. Do not show a routine `Signal Frame:` line in standard fund-manager output; keep that framing internal unless full/audit mode or the user asks for it.

Best next commands must route to Midas diligence commands such as `!research`, `!risk`, `!financials`, `!thesis`; do not use trading guidance and do not auto-run the command. For both fund-manager and politician standard output, place the best next command inside Best Stock Leads cards. If no ranked candidate exists, omit best-next-command wording and say no clean company-level tracker lead was found. Routing logic follows the shared workspace-aware Best Next Command standard in `rules/OUTPUT.md`, with artifact-state inputs from `rules/ARTIFACTS.md`; this file only controls the tracker-specific candidate-card display placement.

For raw Markdown templates and saved Markdown artifacts, section headings should use proper Markdown heading syntax. For Telegram/chat output, do not require literal `##` markers if the platform strips or renders Markdown; require visually clear section titles separated by blank lines. Never render a section heading immediately after a bullet list or paragraph without a blank line.

Default 13F caveat for `## Source Caveat`:

`Manager disclosures, especially 13F data, can be delayed, incomplete, hedged, or stale. They do not prove current ownership, cost basis, or intent. Treat this as a research lead only, not a copy-trading signal.`

Show a separate `## Source Limits` section only when full/audit mode is requested, source limitations are unusually complex, multiple disclosure types are being reconciled, the user asks for source limitations, or an eval/audit specifically tests source-limit display.

`## Lower-Signal Items` is for material disclosures that did not enter Best Stock Leads: mega-cap context, broad ETFs, stale holdings, ambiguous options/hedges, reductions/exits, unverified ticker mappings, post-rerate names, or tiny/noisy positions. Each visible item should state a specific reason. Avoid generic wording such as `less interesting`.

For fund-manager candidates, keep Chase Filter discipline internal by default; reflect price-context checks in `Why it might not be a strong signal:` when relevant. Check movement since the filing report-period end and since the filing date before treating a strong filing signal as a fresh current research lead. Keep this compact: translate internal `Pass` / `Watch` / `Demote` into plain-English limitation wording only when timing/rerating context changes the read. Do not create a new section or repeat broad 13F caveats for every candidate.

Runtime tracker output must not print unresolved placeholders such as `[date]`, `[period]`, `[value]`, `[count]`, `[share/value change]`, or `[Concise summary...]`. These placeholders are allowed only inside examples or template documentation clearly labeled as examples. Runtime output must fill the value, omit the field, or say `Not verified in this run`, `Not disclosed`, or `Needs verification`, depending on the situation.

Runtime tracker output must not print conditional verification instructions as if they are facts. For ticker or corporate-action mapping, report the verified mapping inline when verified; if plausible but unverified, say ticker mapping needs verification before treating it as one economic position history. If mapping is not verified, do not rank the name in Best Stock Leads on the basis of that mapping.

```md
🧿 Tracking Fund Manager | [Person Name]

## Summary

[Plain-English bottom line. Say what the latest disclosure suggests, whether it produced clean company-level stock leads, and the main limitation.]

## What Changed

• Latest filing: [13F / 13D / 13G / Form 4 / investor letter / other]
• Filing date: [date or Unknown]
• Reporting period: [period or Unknown]
• Latest disclosed value: [Answer or Unknown]
• Notable change: [plain-English position or portfolio change]
• Important read-through: [why this does or does not create useful stock leads]

## Best Stock Leads

1. [Display Name] ($[TICKER])

Why it matters:
[Why this is a useful company-level research lead based on the manager disclosure.]

Why it might not be a strong signal:
[Main limitation: 13F delay, options/hedge ambiguity, stale timing, crowded trade, post-rerate, valuation sensitivity, mapping uncertainty, or unclear intent.]

Best next command:
`![research/risk/financials/thesis/full] [ticker]`

2. [Display Name] ($[TICKER])

Why it matters:
[Answer]

Why it might not be a strong signal:
[Answer]

Best next command:
`![research/risk/financials/thesis/full] [ticker]`

3. [Display Name] ($[TICKER])

Why it matters:
[Answer]

Why it might not be a strong signal:
[Answer]

Best next command:
`![research/risk/financials/thesis/full] [ticker]`

## Why These Ranked

[Explain why these names beat the rest of the disclosure. Keep Alpha Queue / Chase Filter / signal-type logic internal; translate it into plain English.]

## Lower-Signal Items

• [Ticker or exposure] — [specific reason it did not make Best Stock Leads]

## Source Caveat

Manager disclosures, especially 13F data, can be delayed, incomplete, hedged, or stale. They do not prove current ownership, cost basis, or intent. Treat this as a research lead only, not a copy-trading signal.
```

Candidate entries in visible fund-manager `Best Stock Leads` should usually use:

- `[Display Name] ($[TICKER])`
- `Why it matters:`
- `Why it might not be a strong signal:`
- `Best next command:`

Keep internal Alpha Queue labels such as `Signal type:`, `Capital-allocation signal:`, `Chase Filter:`, and `Key caveat:` hidden by default in standard output.

Keep `Setup Classification:` and `Setup Modifiers:` internal by default for standard fund-manager output. When shown, use `rules/CLASSIFICATIONS.md`; do not define or invent classifications in this file.

Approved internal Chase Filter values are:

- `Pass`
- `Watch`
- `Demote`

Chase Filter should separate filing signal strength from current research attractiveness:

- `Pass` — no obvious post-period or post-filing rerate/crowding issue based on available price context.
- `Watch` — filing signal is real, but price action, attention, valuation, or crowding may already be processing the thesis; the name may need consolidation or updated valuation work.
- `Demote` — filing signal may still be material, but the stock appears post-rerate/overextended enough that it should usually move to `Lower-Signal Items` rather than rank as a fresh Best Stock Leads candidate.

Use current market data only as timing/rerating context, not as filing-backed proof of business quality. If price data is unavailable or unreliable, do not invent it; use `Watch` or a caveat only when the missing timing evidence materially affects confidence.

`Signal type:` is an internal triage label by default and should remain source-backed and mechanical enough to describe what the disclosure showed when used in full/audit mode. Good examples:

- `New high-conviction position`
- `Increased common-equity exposure`
- `13D / activist-style signal`
- `Fund-letter supported setup`
- `Amended filing signal`
- `Options-heavy signal`

Do not use promotional signal types or invented source-specific classes such as `Smart Money Candidate`, `Whale Buy`, or `Famous Manager Pick`.

Aschenbrenner-style fund-manager Best Stock Leads skeleton:

```md
🧿 Tracking Fund Manager | Leopold Aschenbrenner

## Summary

The filing appears consistent with a hedged AI-infrastructure / semiconductor-cycle book. The cleaner stock leads are company-level common-equity or separate-filing signals that remain researchable after options ambiguity, ticker mapping, and rerating checks.

## What Changed

• Latest filing: 13F-HR
• Filing date: Not verified in this example
• Reporting period: Not verified in this example
• Latest disclosed value: Not verified in this example
• Notable change: Common-equity and options-heavy AI-infrastructure / semiconductor exposure require separation before ranking.
• Important read-through: The useful leads are not automatically the largest reported option notionals; cleaner company-level signals rank higher when they create a specific diligence question.

## Best Stock Leads

1. KEEL | Keel Infrastructure

Why it matters:
Cleaner practical tracker lead because the common-equity signal is less obvious, partly hidden by ticker/corporate-action complexity, and may be underprocessed versus already-rerated AI-infrastructure names.

Why it might not be a strong signal:
Ticker mapping must be verified in the run, and 13F timing does not prove current ownership or intent.

Best next command:
`!risk KEEL`

## Why These Ranked

The visible ranking favors clean company-level common-equity leads over larger but ambiguous options exposure or already well-discovered AI-infrastructure names.

## Lower-Signal Items

• SNDK / IREN / APLD — strong filing signals, but lower priority if already well-discovered or post-rerate.
• SMH/NVDA/ORCL/AVGO/AMD/MU/TSM/ASML puts — options exposure may represent hedging, factor exposure, downside protection, or portfolio construction rather than company-specific directional intent.
• NBIS — handle as a separate 13G/13D/Form 4 or other related disclosure only if verified; do not mix into the reviewed 13F table.

## Source Caveat

Manager disclosures, especially 13F data, can be delayed, incomplete, hedged, or stale. They do not prove current ownership, cost basis, or intent. Treat this as a research lead only, not a copy-trading signal.
```

## Politician Output

Use this format when the tracked person is classified as `Politician`.

Politician output follows `contracts/politician.md` for intelligence logic and this file for section order, candidate-card labels, and display placement.

Politician mode is a disclosure triage tool. Standard politician output must use one visible ranked stock-leads section only: `## Best Stock Leads`. Do not show duplicate ranked sections.

Best next commands must appear inside politician stock-lead cards only when a clean company-level ticker lead exists. If no stock lead exists, omit best-next-command wording and say no clean politician stock lead was found.

Politician stock-lead cards intentionally differ from fund-manager cards. Do not use fund-manager-only fields such as `Capital-allocation signal:` or `Chase Filter:` in politician cards.

Standard politician output should not show a routine mode/contract transparency line. Put the person type in the title instead, using `🧿 Tracking Politician | [Person Name]` or `🧿 Tracking Fund Manager | [Person Name]`.

Do not add separate visible standard-output sections or labels such as `Mode:`, `Contract used:`, `Ranking basis:`, or `Tracker roster: added [Person]`. Ranking basis and contract routing are internal unless the user explicitly asks for audit/debug detail. Watchlist add/update receipts should not appear in the main tracker report body; show them only when the command is specifically roster-management output, when a save/update fails, or when the user explicitly asks.

When no candidate enters `Best Stock Leads`, omit `## Why These Ranked`. Use the `Best Stock Leads` section itself to say no clean politician stock lead was found, then use `Lower-Signal Items` only for material context.

```md
🧿 Tracking Politician | [Person Name]

## Current Role

[Role, party, chamber, state]

## Summary

[Plain-English bottom line. Say whether the latest disclosure is a clean stock-trade signal, portfolio context, or no company-level lead. If there are useful leads, summarize the theme and the main limitation.]

## What Changed

• Newest filing: [filing type or Unknown]
• Filing date: [date or Unknown]
• Filing ID: [filing ID or Unknown]
• Latest PTR found: [date/status or Unknown]
• Latest PTR transaction: [transaction summary or Unknown]
• Important read-through: [why the latest activity is or is not a public-equity stock lead]

## Best Stock Leads

1. [Display Name] ($[TICKER])

Why it matters:
[Why this is a useful company-level research lead based on the disclosure pattern.]

Why it is not a strong signal:
[Main limitation: broad policy link, stale timing, owner ambiguity, routine mega-cap exposure, source disagreement, weak event nexus, or no direct intent evidence.]

Best next command:
`![research/risk/full] [ticker]`

2. [Display Name] ($[TICKER])

Why it matters:
[Answer]

Why it is not a strong signal:
[Answer]

Best next command:
`![research/risk/full] [ticker]`

3. [Display Name] ($[TICKER])

Why it matters:
[Answer]

Why it is not a strong signal:
[Answer]

Best next command:
`![research/risk/full] [ticker]`

## Why These Ranked

[Explain why the ranked leads beat the rest of the disclosure. Tie the explanation to fresh company-level purchases, same-theme clustering, larger disclosed ranges, cleaner policy sensitivity, unusual company-specific activity, or other candidate-gate factors from `contracts/politician.md`.]

## Lower-Signal Items

• [Ticker or disclosure] — [specific reason it did not make Best Stock Leads, such as broad ETF, routine mega-cap exposure, stale transaction, owner ambiguity, no clear policy/event nexus, sale with no clear forward research signal, or no clear company-level research question]

## Source Caveat

Politician trade disclosures can be delayed, source-dependent, and value ranges may be broad. They do not prove current ownership, intent, cost basis, or future trading. Treat this as a research lead only.
```

Politician candidate entries in `Best Stock Leads` should use:

- `[Display Name] ($[TICKER])`
- `Why it matters:`
- `Why it is not a strong signal:`
- `Best next command:`

Allowed standard politician signal types remain internal triage labels unless full/audit mode requires them:

- `Purchase`
- `Sale`
- `Option`
- `Disclosure update`

A politician trade should not enter `Best Stock Leads` unless it has at least one candidate-gate factor from `contracts/politician.md`: policy/jurisdiction overlap, executive authority overlap, procurement exposure, regulatory exposure, timing around a relevant policy/event catalyst, or unusual company-specific trade.

## Optional Audit Output

Use this template only when the user invokes the explicit audit trigger: `-audit`. Do not use `--audit` as the canonical trigger.

This section aligns audit display with the internal proof-packet scaffold from `SKILL.md`. It does not change normal `!track` output, standard politician cards, standard fund-manager cards, candidate labels, or normal section order. Audit output is optional, verification-oriented, and may be more verbose than standard output. It must not be framed as an investment recommendation, copy-trading instruction, allegation of wrongdoing, claim of intent, or claim of non-public information.

Audit output may summarize proof-packet state, but it must hide by default:

- Raw URLs, unless the user explicitly asks for links.
- Raw source dumps or full filing/source text.
- Scratch work.
- Hidden reasoning.
- Tool logs.
- Internal prompts.
- Unrelated dirty-tree or project status.

Audit output must label missing evidence as missing, not inferred. Convenience-source-only evidence must be labeled insufficient for `Best Stock Leads` promotion. Failed P0 gates must visibly block `Best Stock Leads` promotion and route the candidate to lower-signal, rejected, blocked, or omitted audit treatment according to the active mode contract.

Do not add scoring, valuation fields, price targets, recommendations, portfolio fields, schemas, persisted proof packets, artifact writes, or watchlist writes through audit output.

```md
Tracking Audit | [Person / Fund Name]

## Verification Summary

[Maps to `run_metadata` and `subject_resolution`.]

• Mode: [Politician / Public Official / Fund Manager / Unknown]
• Subject: [resolved person/fund name]
• Source contract used: [politician/public-official mode or fund-manager mode]
• Audit purpose: verification of sources, evidence, P0 gates, decisions, and output safety only.
• Normal output impact: none; standard `!track` output remains unchanged.

## Source Contract Used

[Maps to the selected mode contract.]

• Mode contract: [contracts/politician.md or contracts/fund-manager.md]
• Mode label: [politician/public-official or fund-manager]
• Promotion authority: promotion remains governed by the active mode contract.
• Contract application status: [Applied / Partial / Blocked / Unknown]

## Source Manifest Summary

[Maps to `source_manifest`. Do not show raw URLs or source dumps by default.]

• Source IDs reviewed: [S1, S2, S3 or None]
• Source types: [official disclosure / primary filing / convenience mirror / external / unknown]
• Authority levels: [official / primary / convenience / external / unknown]
• Official / primary sources: [count and concise labels]
• Convenience / external sources: [count and concise labels; discovery or cross-check only]
• Timing / as-of fields: [filing date, disclosure date, transaction date, report period, or Unknown]
• Source limitations: [as-of delay, missing official source, convenience-only, conflict, or None]
• Amendment status: [original / amended / unknown / not relevant]

## Evidence Ledger Summary

[Maps to `evidence_ledger`. Missing evidence must be shown as missing/unknown, not inferred.]

• Evidence IDs reviewed: [E1, E2, E3 or None]
• Evidence-to-source mapping: [E1 → S1/S2; E2 → S3; or Missing]
• Candidate tickers / securities: [tickers or securities]
• Claim summaries: [concise claim per candidate]
• Evidence quality: [official/primary / convenience-only / mixed / insufficient / unknown]
• Evidence limitations: [as-of caveat, missing official evidence, instrument ambiguity, source conflict, or None]
• Missing evidence: [specific missing item or None]

## P0 Gate Results

[Maps to `p0_gate_results`. Best Stock Leads is blocked unless all five required P0 gates pass.]

### [Display Name / Security Name] ($[TICKER])

• Source Authority Gate: [Pass / Fail / Partial / Unknown] — [blocker reason if relevant]
• Disclosure Signal Gate: [Pass / Fail / Partial / Unknown] — [blocker reason if relevant]
• Person Relevance / Authority Gate: [Pass / Fail / Partial / Unknown] — [blocker reason if relevant]
• Company Materiality / Researchability Gate: [Pass / Fail / Partial / Unknown] — [blocker reason if relevant]
• Integrity / Noise Discount Gate: [Pass / Fail / Partial / Unknown] — [blocker reason if relevant]
• Best Stock Leads eligibility: [Cleared only if all five pass / Blocked / Lower-signal only / Omit]
• Main blocker: [specific blocker or None]

## Promotion / Demotion Decisions

[Maps to `candidate_decisions`.]

• Promoted to Best Stock Leads: [ticker list or None]
• Lower-signal: [ticker/security list and concise reason]
• Rejected: [ticker/security list and concise reason]
• Blocked: [ticker/security list and blocker]
• Omitted: [ticker/security list and concise reason]
• Best Stock Leads eligibility: [per candidate]
• Primary decision reason: [concise reason]
• Required caveats: [source/as-of/instrument/researchability caveats]
• Best next command: [suggested command or None; suggestion only, not auto-run]

## Output Safety Check

[Maps to `output_safety_check`.]

• No Buy/Sell/Hold language: [Pass / Fail]
• No price-target language: [Pass / Fail]
• No copy-trading framing: [Pass / Fail]
• No current-ownership/current-intent overclaim: [Pass / Fail]
• No wrongdoing / intent / non-public-information implication: [Pass / Fail]
• No external content treated as instruction authority: [Pass / Fail]
• No convenience-source-only promotion: [Pass / Fail / Not applicable]
• No failed-P0 promotion: [Pass / Fail / Not applicable]
• No false artifact/watchlist claim: [Pass / Fail / Not applicable]

## Artifact Status

[Maps to `artifact_watchlist_status`. Show only if relevant. If no artifact/watchlist write was requested, performed, or failed, omit this section.]

• Artifact requested: [Yes / No]
• Artifact written: [Yes / No]
• Watchlist write requested: [Yes / No]
• Watchlist modified: [Yes / No]
• Persistence claim allowed: [Yes / No]
• Persistence status summary: [concise status]
• Persistence caveat: promotion does not imply artifact creation, watchlist mutation, tracking activation, saving, appending, updating, or persistence.
```

## Tracker Show Output

Use this format for `!track show`.

```md
Midas Tracker Watchlist

Politicians:
- [Name]

Fund Managers:
- [Name]
```

If no tracker watchlist exists, use:

```md
No tracker watchlist found yet. Add someone with `!track [person name]`.
```

## Tracker Remove Output

Use this format for `!track remove [person name]`.

If removed:

```md
Removed [Person Name] from watchlist.
```

If not found:

```md
[Person Name] was not found in watchlist.
```

Do not delete saved artifacts unless the user explicitly asks.
