# Politician Tracker Intelligence Contract

Stage: Active politician intelligence contract for `!track` politician mode.

This contract governs politician and senior-public-official disclosure triage for `!track`. It does not create a new command, does not change watchlist paths, and does not override global MIDAS source, scoring, classification, output, or artifact rules.

## Authority Boundaries

This contract owns the command-local intelligence logic for `!track` politician mode:

- Source scope, the source reconciliation ladder, and the P0 promotion source contract.
- Disclosure mechanics, managed-account / blind-trust treatment, and issuer / security identity resolution.
- The politician candidate gate, ranked-lead evidence pack, five P0 promotion gates, ranked-lead minimum bar, and Best Stock Leads promotion verdict.
- The internal triage model, Best Stock Leads ranking, politician candidate cards, and demotion / lower-signal handling.
- Command-local guardrail application for politician mode, without weakening global guardrails.

This contract does not own:

- Output templates or visible section shapes, which belong in the tracker `OUTPUT.md`; the Output Relationship section defers there.
- Trigger syntax, routing, inputs, workflow, or fund-manager mode, which belong in `SKILL.md` and `contracts/fund-manager.md`.
- Artifact paths or write mechanics, except by reference to the active artifact authorities.
- Watchlist or roster mutation, including `data/tracker_watchlist.json` handling defined in `SKILL.md`.
- Registry status or eval cases.
- Global source, metric, scoring, classification, output, artifact, or copy-trading guardrail definitions.

Follow `/home/jordan/.hermes/profiles/midas/rules/CONTRACT_AUTHORITY.md` when deciding whether future additions belong here, in `SKILL.md`, in `OUTPUT.md`, in evals, in docs, in schemas, or in shared global rules. Tracked activity framing follows the no-copy-trading rule in `rules/GLOBAL.md`; this contract applies that rule and must not weaken it.

## Purpose

Politician `!track` is a policy/event disclosure triage tool that ranks company-level research leads based on jurisdiction, regulation, procurement, timing, disclosure strength, and noise discount.

It should answer:

> Which disclosed politician or senior-public-official transactions are useful enough to become MIDAS research leads?

It should not answer:

- What should the user copy?
- What should the user buy?
- Which politician has the best trading returns?
- Whether a disclosure proves non-public information, wrongdoing, or intent.

Tracked politician activity is a research lead only. It is never a buy/sell/hold instruction, copy-trading signal, price target, position-sizing input, allegation of misconduct, or claim of privileged information.

## Source Scope

For politicians, members of Congress, and senior public officials, use official or clearly labeled disclosure sources when available:

- House financial disclosures.
- Senate financial disclosures.
- Periodic Transaction Reports.
- Official member pages.
- Office of Government Ethics public financial disclosure reports for presidents, vice presidents, cabinet officials, nominees, appointees, and other executive-branch filers.
- OGE Form 278e / annual public financial disclosure reports for executive-branch holdings and background.
- OGE Form 278-T / Periodic Transaction Reports for executive-branch transaction activity.
- White House disclosure pages when they host the same OGE PDFs.
- Quiver Quantitative or Capitol Trades as convenience sources for congressional disclosures, with source-dependent caveats.

Politicians and executive-branch officials do not file SEC forms for personal trades. SEC filings may still be useful for company research after a ticker becomes a research lead, but they are not the politician trade source.

## Source Reconciliation Ladder

When politician or senior-public-official disclosure sources conflict, use this reconciliation order:

1. Official disclosure PDF or official filing page.
2. Official House, Senate, or OGE disclosure index metadata.
3. Official amended or corrected disclosure, if applicable.
4. Reputable disclosure tracker, used only as a discovery aid.
5. Secondary reporting, used only as context.

If official and convenience sources disagree on transaction date, owner, ticker, amount range, instrument, action type, filing date, amendment status, notification date, report ID, or disclosure count, prefer the official source or mark the row `Needs verification`.

When a convenience tracker groups or displays rows under a date that differs from the official PTR filing/notification date, keep the fields separate. Use the official PTR/report ID, official transaction date, and official notification/filing date for disclosure mechanics; label the tracker date as tracker-specific grouped/display metadata only if it is used.

Do not aggregate transaction volume, counts, value ranges, or totals across trackers unless methodology is clear, consistent, and source-labeled.

Use convenience sources to find leads faster, not to override official disclosure mechanics.

## Promotion Source Contract — P0

Before a politician disclosure can enter visible `Best Stock Leads`, the promotion must satisfy a source contract:

- Official or primary disclosure sources may support promotion. For congressional filers, this means official House or Senate disclosure records, official PTR PDFs, official disclosure index metadata, or official amended/corrected disclosures. Official member, committee, agency, company, contract, procurement, grant, regulatory, budget, or court sources may support role, catalyst, and company-materiality claims.
- Convenience sources such as Quiver Quantitative, Capitol Trades, Congress Stock Tracker, scraped tables, newsletters, articles, or social posts may discover rows, speed reconciliation, or provide context, but they cannot promote a ticker to `Best Stock Leads` by themselves.
- Each promotion candidate must capture internally: source ID, source type, source date or access date, disclosure/filing/report ID when available, person/entity match, ticker/security match, transaction date, disclosure/filing date, owner/control field when available, and source limitations.
- If an official/primary source is unavailable, blocked, stale, contradictory, or incomplete, the candidate must be labeled with the limitation and demoted unless another official/primary source independently supports the promotion thesis.
- OGE and executive-branch references already present in this contract remain available for existing scope context, but this patch does not expand OGE behavior. Treat new OGE / executive-branch handling beyond existing language as out of scope until separately approved.

The source contract is internal by default. Standard output should reflect only the necessary caveat through existing output fields and must not add new visible sections unless the user asks for audit/source detail.

## Disclosure Mechanics

Politician-mode triage must account for disclosure mechanics before treating a transaction as a research lead:

- Disclosures can be delayed.
- Transaction value ranges may be broad.
- Public trackers can disagree on counts, trade volume, dates, owners, and methodology.
- Reported owner may be the politician, spouse, dependent, trust, managed account, or other disclosed owner when available.
- Disclosures do not prove current ownership, cost basis, intent, future trading, or alpha.
- Convenience parsers are useful for discovery but should not override official disclosure context when official records are available.

Use `Unknown`, `Not disclosed`, `Not verified in this run`, or `Needs verification` when a field cannot be confirmed. Do not invent missing trades, holdings, transaction dates, values, sectors, owners, or sources.

## Managed Account / Blind Trust Treatment

When a disclosure indicates a managed account, blind trust, third-party adviser, spouse, dependent, or trust ownership, treat control and intent as unclear.

Default treatment:

- Demote if the trade lacks strong policy/event nexus and company materiality.
- Caveat heavily if the lead otherwise ranks.
- Do not infer personal intent, knowledge, direction, or control.
- Prefer `owner/control unclear` or `managed-account ambiguity` as the caveat.

A managed-account or blind-trust trade can still be a research lead only when the company-level policy/materiality evidence is independently strong.

## Issuer / Security Identity Resolution

Resolve the reported security before treating a politician disclosure as a company-level research lead. This gate prevents bad ticker mapping, wrong issuer mapping, ETF/fund confusion, ADR or share-class errors, merger/SPAC confusion, and option/security mismatch.

Identity resolution must start from the disclosure text as filed or parsed. Do not assume that a familiar ticker, company name, or convenience-source label represents direct common-stock exposure.

Check:

- Reported issuer or security name.
- Security type: common stock, ETF, mutual fund, closed-end fund, trust, option, bond, preferred, warrant, ADR, SPAC unit, fund, or other disclosed instrument.
- Ticker, CUSIP, exchange, share class, ADR/local ordinary distinction, or successor issuer when available.
- Whether the disclosed item is a direct company security, diversified fund exposure, derivative exposure, debt/security claim, or legacy/merged/SPAC entity.

Classify identity confidence internally as one of:

- `Resolved` — issuer, security type, and ticker/security mapping are supported by available source evidence.
- `Probable match` — mapping appears likely but one key field is missing or source-dependent.
- `Ambiguous` — multiple plausible issuers, tickers, security types, share classes, or successor entities exist.
- `Unresolved` — the disclosed security cannot be safely mapped in the run.
- `Excluded / fund or non-company security` — ETF, diversified fund, mutual fund, closed-end fund, trust, index exposure, or other non-company exposure unless holdings-level analysis is explicitly performed.

Rules:

- Do not map a disclosure to a ticker unless issuer/security identity is verified or clearly labeled as a probable match.
- Treat ETFs, mutual funds, closed-end funds, trusts, and index products as fund exposure, not direct company purchases.
- Treat options as derivative exposure; identify the underlying issuer separately from the option instrument and do not describe the transaction as a simple common-stock buy/sell.
- Distinguish ADRs from local ordinary shares and distinguish share classes when economics, voting rights, exchange, or ticker differs.
- Check for renames, mergers, acquisitions, delistings, ticker changes, SPAC units, warrants, and successor issuers before back-mapping stale tickers.
- Preserve historical issuer identity and current successor identity separately when a security has changed through merger, SPAC conversion, ticker change, or rename.
- If identity is `Ambiguous` or `Unresolved`, route the disclosure as a Verification Lead, demote it, or omit it. Do not give it ranked-lead treatment, company-level thesis treatment, or ticker artifact updates until the mapping is resolved.

## Politician Candidate Gate

A politician disclosure should not enter visible `Best Stock Leads` unless it has at least one of these:

- Policy / jurisdiction overlap.
- Executive authority overlap.
- Procurement exposure.
- Regulatory exposure.
- Timing around a relevant policy or event catalyst.
- Unusual company-specific trade.

If a disclosure is mechanically notable but fails this gate, keep it in `Lower-Signal Items`, demote it, or omit it depending on materiality. Do not create a second ranking list to preserve raw disclosure strength.

## Ranked Lead Evidence Pack — P0 Internal Gate

Before a politician disclosure can enter visible `Best Stock Leads`, create an internal evidence pack. The pack is not displayed by default, but the ranked-card language must be supportable from it.

Required evidence-pack fields:

- Official disclosure source or source limitation.
- Transaction date, filing/disclosure date, and disclosure lag.
- Issuer/security identity confidence.
- Owner/control status.
- Role and jurisdiction at the transaction date.
- Power Node / Influence Weighting category at the transaction date.
- Specific policy, procurement, regulatory, budget, enforcement, tariff, subsidy, grant, contract, or agency catalyst.
- Policy Event Tree stage and next public milestone when feasible.
- Official catalyst source when available.
- Company-materiality source showing why the catalyst could plausibly matter to the issuer, not merely the broad sector.
- Procurement / Grant Materiality Lane check when the thesis depends on government spending, procurement, grants, subsidies, reimbursement, or agency awards.
- Market Absorption / Next-Milestone Enforcement classification and remaining testable milestone/question.
- Main caveat that could demote the lead.

Evidence-ledger requirements:

- Every promoted ticker must map to one or more internal evidence IDs.
- Every evidence ID must map to one or more source IDs from the Promotion Source Contract.
- Every material promotion claim must be traceable to an evidence ID and source ID, including disclosure mechanics, issuer/security identity, owner/control, role/jurisdiction, catalyst, company materiality, independent cross-signal, market absorption, and caveat language.
- Inferred intent, inferred politician motive, alleged non-public information, suspected wrongdoing, current ownership after stale disclosure, future trading, or investment merit must not be ledgered as fact. If mentioned at all, it must be framed as unsupported, unknown, or prohibited inference.
- If a material claim cannot be ledgered, remove the claim, demote the candidate, or route it as a verification item rather than promoting it.

If the evidence pack is materially incomplete, route the candidate as a `Verification Lead`, demote it to `Lower-Signal Items`, or omit it. Do not promote a candidate to `Best Stock Leads` on politician fame, ticker fame, broad sector exposure, filing recency, or tracker popularity alone.

Keep the evidence pack internal in standard output. Surface only the compact implications through `Why it matters:`, `Why it is not a strong signal:`, `Why These Ranked`, and `Source Caveat` unless the user explicitly asks for detailed evidence, sources, or audit-style output.

## Five P0 Promotion Gates

Before a politician candidate can enter visible `Best Stock Leads`, it must explicitly clear all five internal P0 gates:

1. **Source Authority Gate:** official/primary sources support the disclosure mechanics and material promotion claims; convenience sources are not the sole basis for promotion; source IDs, source dates, disclosure/report IDs when available, person/entity match, and limitations are captured.
2. **Disclosure Signal Gate:** the transaction or disclosure is fresh, company-specific, mechanically significant, and not merely a sale, tiny trade, stale row, diversified product, ambiguous option, or tracker-display artifact.
3. **Person Relevance / Authority Gate:** the filer/person, role, jurisdiction, committee, office, executive authority, or policy/event relevance is verified at the transaction-date window and is not inferred from stale or later authority.
4. **Company Materiality / Researchability Gate:** the catalyst or disclosure creates a testable company-level MIDAS research question and there is source-backed evidence that the policy, procurement, regulatory, budget, agency, or event nexus could matter to the issuer.
5. **Integrity / Noise Discount Gate:** owner/control ambiguity, disclosure lag, source conflicts, market absorption, crowded/obvious ticker status, motive ambiguity, and non-public-information risk do not overwhelm the research signal.

If any P0 gate fails, the candidate cannot appear in visible `Best Stock Leads`. It may appear only as lower-signal context when useful, clearly caveated, and not framed as a promoted research lead.


## Ranked Lead Minimum Bar — P0

A politician disclosure may enter visible `Best Stock Leads` only if all of the following are true or explicitly caveated without overwhelming the signal:

1. Issuer/security identity is `Resolved` or `Probable match`.
2. Transaction date and filing/disclosure date are known, or the timing limitation is explicit.
3. Owner/control status is known, or ambiguity is demoting rather than ignored.
4. Role/jurisdiction is assessed at the transaction date when relevant.
5. There is a specific policy/event/procurement/regulatory nexus.
6. The nexus appears financially material or testable at the company level.
7. At least one independent public cross-signal supports the research question.
8. Market absorption does not eliminate the usefulness of the lead.
9. The output can state a concrete `Why it matters:` and a concrete `Why it is not a strong signal:`.

If any of these fail, route the item to `Lower-Signal Items`, classify it internally as a `Verification Lead`, or omit it. Do not use visible `Best Stock Leads` placement to preserve candidates that cannot clear this minimum bar.

This gate can be satisfied by explicit caveats only when the caveats do not overwhelm the research signal. If the caveat is central to identity, timing, owner/control, materiality, market absorption, or the existence of a company-level research question, demote or omit the candidate rather than ranking it strongly.

## Best Stock Leads Promotion Verdict — P0 Hard Gate

Passing the Politician Candidate Gate only makes a disclosure eligible for review. It does not automatically make the disclosure rankable.

Before a candidate enters visible `Best Stock Leads`, assign an internal promotion verdict:

- `Cleared for Best Stock Leads`
- `Cleared with heavy caveat`
- `Verification Lead`
- `Lower-Signal Item`
- `Omit`

A candidate may enter visible `Best Stock Leads` only when the evidence supports all of the following:

1. Resolved or probable issuer/security identity.
2. Official or clearly reconciled disclosure source.
3. Transaction date, official notification/filing date, and disclosure lag.
4. Owner/control status or a clear owner/control caveat.
5. Role/jurisdiction assessed at the transaction date.
6. Specific policy, procurement, regulatory, budget, agency, or event nexus.
7. Company-level materiality support.
8. At least one independent public cross-signal.
9. Market absorption not obviously eliminating the research usefulness.

`Cleared for Best Stock Leads` requires the evidence to support the ranked-card language without central unresolved caveats.

`Cleared with heavy caveat` may enter visible `Best Stock Leads` only when the company-level research question remains strong, the caveat is explicit, and the caveat does not overwhelm issuer identity, source reconciliation, timing, owner/control, role-date jurisdiction, materiality, or market absorption.

If the candidate is interesting but fails company-materiality support, procurement/program support, role-date verification, market-absorption review, or source reconciliation, route it as `Verification Lead`, demote it to `Lower-Signal Items`, or omit it.

Do not promote a second or third name merely to fill the `Best Stock Leads` section. If only one candidate clears this hard gate, show one. If none clear it, say no clean politician stock lead was found.

Keep the promotion verdict internal in standard output. Surface only the compact implications through `Why it matters:`, `Why it is not a strong signal:`, `Why These Ranked`, `Lower-Signal Items`, and `Source Caveat` unless the user explicitly asks for detailed evidence, sources, or audit-style output.

## Internal Triage Model

Use these lenses internally to decide whether a politician disclosure deserves visible attention and how it ranks. Do not display these as default candidate-card labels unless the user explicitly asks for detailed scoring.

### 1. Policy / Event Nexus

This is the most important politician-specific lens.

Check:

- Committee jurisdiction.
- Executive authority.
- Agency relevance.
- Procurement / government-contract exposure.
- Regulation exposure.
- Legislative, regulatory, budget, tariff, enforcement, procurement, or policy-catalyst timing.
- Defense, energy, healthcare, banking, housing, infrastructure, semiconductors, cybersecurity, AI, tariffs, and other policy-sensitive sectors.

A strong nexus does not imply wrongdoing or intent. It means the disclosed company overlaps with a policy, jurisdiction, procurement, regulation, or event context worth researching.

### 2. Disclosure Signal Strength

Higher signal quality can come from:

- Purchase rather than sale, when the purchase is company-specific and fresh.
- Newly disclosed ticker.
- Large amount range.
- Repeat activity in the same ticker or sector.
- Options activity.
- Company-specific trade rather than ETF/diversified exposure.
- Timing around a relevant policy/event catalyst.
- Reported owner clarity: filer, spouse, trust, dependent, or managed account.

Lower signal quality can come from:

- Tiny trades.
- Old trades.
- Broad ETFs.
- Routine household mega-cap activity with no unusual pattern.
- Sales with no clear forward research signal.
- Disclosure rows that cannot be reconciled across sources.

### 3. Research Setup Quality

A politician disclosure is more useful to MIDAS when it creates a clear company-level research question that can be followed with `!research` or `!risk`.

Check:

- Is the policy exposure material to the company?
- Is there a clear company-level research question?
- Is it more than broad ETF exposure?
- Is it more than an obvious mega-cap household trade?
- Does the disclosure point to something MIDAS can actually research next?

Prefer leads where the next diligence step can test something concrete, such as government-contract exposure, regulatory sensitivity, procurement risk/opportunity, balance-sheet fragility, valuation/rerating setup, or business exposure to a policy/event catalyst.

### 4. Integrity / Noise Discount

Politician disclosures are noisy. Discount for:

- Reporting delay.
- Broad value ranges.
- Managed-account ambiguity.
- Spouse/trust/dependent ambiguity.
- No evidence of intent.
- Mixed academic alpha evidence.
- Risk of implying wrongdoing.
- ETF / diversified exposure.
- No clear jurisdiction link.

A high raw disclosure signal can still be a weak research lead if the disclosure is stale, owner-ambiguous, too diversified, has no company-level question, or lacks policy/event nexus.

### 5. Anomaly Trigger Index — P0 Internal Lens

Use the Anomaly Trigger Index to detect politician disclosures that look meaningfully unusual relative to normal disclosure noise. This is an internal research-triage score only. It is not an allegation engine, copy-trading signal, legal conclusion, or claim of non-public information.

Score internally from 0-30 across six buckets. Do not show numeric anomaly scores in standard output unless the user explicitly asks for detailed or audit-style output.

#### 5.1 Jurisdiction Precision — 0-5

- 0 = no relevant role or jurisdiction.
- 1 = broad sector relevance only.
- 2 = committee or agency overlap.
- 3 = subcommittee, program, regulator, or agency overlap.
- 4 = chair/ranking member, appropriator, leadership, or agency authority with direct relevance.
- 5 = direct power node over a named program, budget line, rulemaking, procurement stream, enforcement area, approval path, or regulated market.

#### 5.2 Company Materiality — 0-5

- 0 = no company-level materiality.
- 1 = broad thematic exposure only.
- 2 = disclosed but minor segment/customer/program exposure.
- 3 = meaningful revenue, backlog, cost, margin, approval, contract, or regulatory exposure.
- 4 = major segment, customer, program, reimbursement, subsidy, approval, or procurement exposure.
- 5 = company thesis depends materially on the relevant government action, contract, regulation, subsidy, tariff, approval, or enforcement path.

#### 5.3 Trade Abnormality vs Filer Baseline — 0-5

- 0 = routine for filer.
- 1 = slightly unusual size, ticker, or sector.
- 2 = new ticker or uncommon sector for filer.
- 3 = first-time company-specific trade or unusually large amount range versus filer history.
- 4 = repeat buys, sector cluster, or concentrated exposure outside normal pattern.
- 5 = first-time or concentrated company-specific options/common-stock activity in an undercovered policy-sensitive company.

#### 5.4 Timing / Catalyst Proximity — 0-5

- 0 = stale or no event date.
- 1 = post-event or already widely absorbed.
- 2 = loose window, 46-90 days, with active policy process.
- 3 = standard window, 15-45 days, around a relevant public event.
- 4 = tight window, 0-14 days, around a relevant public event.
- 5 = tight pre-event window before a specific named catalyst such as contract award, final rule, hearing, vote, budget language, enforcement action, agency approval, tariff decision, grant/subsidy award, or procurement milestone.

#### 5.5 Instrument / Aggressiveness — 0-5

- 0 = ETF, fund, tiny trade, or routine diversified exposure.
- 1 = small common-stock trade.
- 2 = meaningful common-stock purchase.
- 3 = large common-stock purchase or repeated purchases.
- 4 = options, short-dated derivative exposure, or unusually concentrated position.
- 5 = options or concentrated exposure paired with strong timing, jurisdiction, and materiality.

#### 5.6 Cross-Signal Support — 0-5

- 0 = no independent public support.
- 1 = only broad news or theme support.
- 2 = company filing supports general exposure.
- 3 = official policy, agency, procurement, regulatory, or company source supports the research question.
- 4 = multiple independent public signals align.
- 5 = disclosure timing, role/jurisdiction, company materiality, and official policy/procurement/regulatory/company records all point to the same company-specific question.

Internal interpretation:

- 0-7 = Low anomaly / likely noise.
- 8-13 = Moderate anomaly / researchable only if company materiality is present.
- 14-20 = High anomaly / eligible for Best Stock Leads only if the Ranked Lead Minimum Bar and false-positive gates pass.
- 21-30 = Exceptional anomaly / priority verification and research lead, not an allegation.

Use the Anomaly Trigger Index to help rank, demote, or omit candidates. A high Anomaly Trigger Index cannot override issuer identity, owner/control, source quality, company materiality, market absorption, the Ranked Lead Minimum Bar, or false-positive suppression gates.

Keep the score internal in standard output. Surface only the practical implication through existing fields such as `Why it matters:`, `Why it is not a strong signal:`, `Why These Ranked`, `Source Caveat`, or `Best next command:` unless the user explicitly asks for detailed evidence or audit-style output.

Do not use anomaly scoring to imply that the politician has non-public information, acted improperly, coordinated with anyone, or that a trade is suspicious without evidence.


### 6. No Single-Factor Suspicion Rule — P0 Guardrail

Do not treat any single anomaly factor as enough to promote a politician disclosure. Single-factor matches may support verification, caveats, or `Lower-Signal Items`, but they are not enough by themselves for visible `Best Stock Leads`.

The following are not sufficient by themselves:

- Committee member buys a company in the same broad sector.
- Famous politician buys famous ticker.
- Recent disclosure date without transaction-date context.
- Large reported amount range without filer-history comparison.
- Late or amended disclosure without evidence of what changed.
- Spouse, dependent, trust, or managed-account trade without owner/control clarity.
- Trade near a public event without company-materiality support.
- Multiple politicians buying the same broad sector through ETFs or mega-cap household names.

A disclosure becomes a high-anomaly research lead only when multiple public factors align, such as transaction-date role/jurisdiction, company-level materiality, abnormal trade behavior, event-window timing, instrument/size significance, and independent public cross-signal support.

Use this guardrail with the Anomaly Trigger Index, Ranked Lead Minimum Bar, issuer/security identity rules, owner/control checks, market absorption gate, and false-positive suppression. Do not imply suspicion, causality, intent, non-public information, coordination, wrongdoing, recommendation, or copy-trading value from any single factor.

### 7. Filer-History Baseline

A trade is only `unusual` if it differs meaningfully from that filer's normal disclosed pattern. Before treating a disclosure as anomalous, compare it against the filer's available history when feasible.

Check baseline behavior across:

- Normal ticker and issuer behavior.
- Normal sector and theme exposure.
- Typical transaction value ranges.
- Reported owner patterns, including filer, spouse, dependent, trust, or managed account.
- Instrument type, including common stock, options, ETFs, funds, bonds, or other disclosed securities.
- Trade frequency and clustering patterns.
- Managed-account or third-party-advised account patterns.
- Prior late, amended, corrected, or source-disputed disclosures.

Use the baseline to separate a genuinely unusual company-specific disclosure from routine household or managed-account activity. A disclosure that matches the filer's normal pattern may still be relevant, but it should need stronger policy/event nexus and company-materiality support before ranking in Best Stock Leads.

If the filer-history baseline is unavailable, incomplete, or source-dependent, say so internally and avoid overclaiming anomaly. Prefer cautious language such as `appears unusual based on available disclosures` or demote when the baseline is too weak.

### 8. Transaction-Date vs Filing-Date Normalization

For every politician ranked stock lead, normalize timing before ranking or describing the disclosure. Distinguish:

- Transaction date — when the disclosed transaction occurred.
- Filing/disclosure date — when the transaction was publicly filed or disclosed.
- Disclosure lag — time between transaction date and filing/disclosure date, when both dates are available.
- Event date — the relevant policy, regulatory, procurement, budget, enforcement, committee, earnings, contract, or company-specific event date, when a specific event is part of the thesis.
- Timing classification — `Pre-event`, `Same-window`, `Post-event`, `Stale`, or `No clear event date`.

Use this normalization to avoid false timing claims. Do not imply a trade was timely, predictive, or connected to an event unless the transaction date, filing date, disclosure lag, and event context support that framing.

Treat stale disclosures, long disclosure lags, missing event dates, or source-disagreement on dates as ranking caveats. A disclosure can still be a useful research lead when stale, but the output must make the timing limitation clear.

In standard output, keep this timing work compact and include it through existing Best Stock Leads fields when material. Do not add new visible timing fields to politician candidate cards unless `OUTPUT.md` is explicitly updated.


### 9. Direct Jurisdiction Overlap Ladder — P0 Internal Lens

When a politician trades a company in a sector connected to the filer's official role, classify the overlap level internally. This lens prevents broad role/sector adjacency from being treated as direct jurisdiction or named-catalyst authority.

Internal ladder:

- `No overlap` — no meaningful connection between role and issuer.
- `Broad sector overlap` — filer has broad exposure to the sector but no direct committee, agency, budget, procurement, or regulatory nexus.
- `Committee overlap` — filer sits on a committee with jurisdiction over the sector.
- `Subcommittee / program overlap` — filer sits on a subcommittee or role tied to a specific agency, market, program, procurement stream, or regulatory area that affects the company.
- `Power-node overlap` — filer is chair, ranking member, leadership, appropriator, budget/authorization lead, agency head, cabinet official, or other power node with direct influence over the relevant area.
- `Named catalyst overlap` — filer role overlaps with a specific bill, amendment, hearing, markup, rulemaking, contract, grant, subsidy, enforcement action, approval, tariff, waiver, or budget line tied to the issuer.

Do not promote `Broad sector overlap` alone. A stronger overlap classification can improve ranking only when paired with transaction-date role verification, company materiality, timing/event context, and independent public cross-signal evidence.

Keep this ladder internal in standard output. Surface only the practical implication through existing fields such as `Why it matters:`, `Why it is not a strong signal:`, `Why These Ranked`, `Source Caveat`, or `Best next command:` unless the user explicitly asks for detailed evidence or audit-style output.

Do not imply causality, intent, non-public information, wrongdoing, recommendation, or copy-trading value from jurisdiction overlap. Jurisdiction overlap is a research-prioritization input only.

### 10. Role-at-Transaction-Date Jurisdiction Mapping

For every politician ranked stock lead, assess jurisdiction using the filer's role at the transaction date when feasible, not only the filer's current role. Current committee, office, agency, leadership, or public-official role may differ from the role held when the transaction occurred, and that difference can materially change anomaly detection.

Check historical role context as of the transaction date:

- Committee and subcommittee assignments.
- Chamber, office, leadership role, caucus role, or public-official position.
- Executive-branch authority, agency jurisdiction, cabinet role, nominee/appointee status, or transition window when relevant.
- Whether the filer had jurisdiction over the relevant sector, agency, procurement stream, regulation, budget item, tariff, subsidy, enforcement action, or policy event at that time.

Separate current role from transaction-date role:

- Current role may appear in `Current Role` output.
- Internal anomaly detection and policy/event nexus should use transaction-date role when available.
- If the filer joined a relevant committee or office after the transaction, do not treat that later jurisdiction as transaction-date nexus.
- If the filer left a relevant committee or office before the transaction, do not treat stale jurisdiction as active nexus unless residual influence is specifically supported.
- For nominees, appointees, presidents, vice presidents, cabinet officials, and senior executive-branch filers, distinguish pre-office, confirmation, transition, in-office, and post-office windows.

Classify role-date confidence internally as one of:

- `Role verified at transaction date`.
- `Role likely but not verified`.
- `Current-role only`.
- `Role unknown at transaction date`.

If only current-role evidence is available, caveat the policy/event nexus and do not let current-role overlap alone drive a high anomaly rank. A transaction is a stronger anomaly candidate when the transaction-date role overlaps with the relevant jurisdiction or policy/event context; it is weaker when the claimed jurisdiction exists only after the transaction date.

Do not imply causality, intent, non-public information, wrongdoing, or recommendation from a verified role/date overlap. It remains a research-triage input only.

### 11. Power Node / Influence Weighting — Internal Lens

When evaluating policy/event nexus, classify the filer's power node at the transaction date. This lens distinguishes generic jurisdiction from roles with greater agenda-setting, information-flow, appropriations, executive, procurement, or local-project relevance.

Classify the power node internally as one of:

- `Top leadership` — Speaker, majority/minority leader, whip, conference/caucus chair, or Senate/House party leadership.
- `Committee power` — chair, ranking member, subcommittee chair, or subcommittee ranking member with direct jurisdiction.
- `Appropriations / budget power` — appropriations, budget, authorization, defense, infrastructure, healthcare, energy, financial services, or other spending-relevant role.
- `Agency/executive authority` — president, vice president, cabinet official, agency head, senior appointee, nominee, or transition official with relevant authority.
- `District/state nexus` — issuer headquarters, major facility, project, employer, military base, grant recipient, or government contract in the filer's district/state.
- `Generic member` — no specific power node beyond general legislative status.
- `Unverified / unknown power node` — role or relevant authority cannot be verified at the transaction date.

Do not treat generic committee membership and leadership, committee power, appropriations authority, agency authority, or district/state nexus as equal. A verified power node may increase ranking confidence only when issuer identity, transaction timing, company materiality, and official policy, procurement, regulatory, budget, enforcement, agency, grant, subsidy, contract, or catalyst evidence also support the lead.

Generic membership alone should not promote a candidate to Best Stock Leads. If the relevant power node cannot be verified at the transaction date, caveat the policy/event nexus and route the candidate as a Verification Lead, demote it to `Lower-Signal Items`, or omit it when the missing authority evidence materially weakens the case.

Keep this lens internal in standard output. Surface only the practical implication through existing fields such as `Why it matters:`, `Why it is not a strong signal:`, `Why These Ranked`, or `Source Caveat` unless the user explicitly asks for detailed evidence or audit-style output.

Do not imply causality, intent, non-public information, wrongdoing, or recommendation from a verified power node. Power-node status is a research-prioritization input only.

### 12. Late/Amended Disclosure Handling

Late, amended, corrected, or source-disputed disclosures are source-quality and disclosure-mechanics flags first. They are not automatic Best Stock Leads items.

Do not promote a disclosure merely because it was late, amended, corrected, revised, or disputed across sources. First treat the issue as a quality caveat and verify what changed: transaction date, filing/disclosure date, owner, ticker/issuer, amount range, instrument type, amendment reason, and whether the amendment affects the research question.

Promote a late or amended disclosure only when it also has:

- Company-specific exposure.
- Policy/event nexus.
- Company materiality.
- A clear research question.
- Timing or cross-signal evidence that remains relevant after accounting for the disclosure lag or amendment.

If lateness or amendment history is consistent with the filer's baseline or appears administrative, demote or caveat it rather than treating it as unusual. Do not imply concealment, intent, wrongdoing, or non-public information from a late or amended disclosure without evidence.

### 13. Event-Window Rules

Use consistent timing windows when comparing transaction dates to event dates. This makes timing anomaly detection repeatable across politician tracker runs.

Classify event-window proximity as:

- `Tight window:` 0-14 days.
- `Standard window:` 15-45 days.
- `Loose window:` 46-90 days.
- `Stale:` beyond 90 days unless the policy process remains active.

Policy processes may remain active beyond 90 days when there is ongoing rulemaking, procurement, budget negotiation, permitting, licensing, litigation, enforcement, agency approval, tariff review, subsidy implementation, or contract-award activity.

Use the event window internally for anomaly detection, timing caveats, demotion, and Best Stock Leads ranking. Timing proximity alone must not imply causality, intent, non-public information, wrongdoing, or a recommendation.

Event-window strength still requires policy/event nexus and Company-Materiality support before it can become a strong Best Stock Leads reason.

### 14. Policy Event Tree — Internal Stage Classifier

For every ranked politician lead with policy/event nexus, identify the stage of the relevant public policy, agency, enforcement, procurement, grant, subsidy, contract, or budget path when feasible. This classifier answers where the catalyst sits in the public event path, not merely whether the trade was near an event.

Classify the catalyst stage internally as one of:

- `Legislative idea / early bill`.
- `Committee referral`.
- `Hearing / testimony`.
- `Markup / amendment`.
- `Committee vote`.
- `Floor vote / passage`.
- `Conference / reconciliation`.
- `Signed law / enacted budget`.
- `Agency proposed rule / NPRM`.
- `Comment period / docket activity`.
- `Final rule`.
- `Effective / compliance date`.
- `Agency guidance / waiver / approval`.
- `Enforcement / investigation / settlement`.
- `Procurement forecast`.
- `RFP / solicitation`.
- `Contract award`.
- `Grant / subsidy award`.
- `Bid protest / litigation`.
- `No clear public catalyst stage`.

Use the event-stage classification as a P0 ranking input. A lead ranks higher when the stage creates a concrete, testable company-level research question and a visible next public milestone, such as a final rule, effective date, live procurement deadline, contract award, agency approval, grant/subsidy award, enforcement settlement, or enacted budget implementation.

A lead ranks lower when the catalyst is early, vague, stale, only thematic, or lacks a visible next milestone. Trades near bill introduction, committee referral, or broad sector policy chatter generally need stronger company-materiality evidence before they can enter Best Stock Leads.

When stage evidence is unavailable or source-dependent, classify it as `No clear public catalyst stage`, caveat the policy/event nexus, and route the candidate as a Verification Lead, demote it to `Lower-Signal Items`, or omit it if the missing stage materially weakens the research case.

Keep this classifier internal in standard output. Surface only the practical implication through existing fields such as `Why it matters:`, `Why it is not a strong signal:`, `Why These Ranked`, or `Source Caveat` unless the user explicitly asks for detailed evidence or audit-style output.

Do not imply causality, intent, non-public information, wrongdoing, or recommendation from a mature event stage. Event-stage maturity is a research-prioritization input only.


### 15. Procurement / Grant Materiality Lane — P0 Hard Gate

For companies where the politician lead depends on government spending, procurement, grants, subsidies, reimbursement, or agency awards, check official spending/procurement sources before ranking the lead strongly. This lane is especially important for defense, infrastructure, energy, healthcare, aerospace, cybersecurity, AI/data-center, telecom, and government-services names.

Use official and company sources such as:

- USAspending for federal awards, grants, contracts, loans, and assistance.
- SAM.gov / FPDS-linked contract award and opportunity data.
- Agency award announcements.
- Company filings for government-customer exposure, backlog, contract concentration, program risk, reimbursement exposure, or funding exposure.
- 8-Ks, earnings releases, investor presentations, or official company releases for material awards.

A procurement/grant lead should not rank highly unless it creates a testable company-level question, such as:

- Is the disclosed company a direct awardee or major subcontractor?
- Is the relevant agency/program financially material to revenue, backlog, margins, cash flow, or valuation?
- Is there a visible upcoming RFP, award, renewal, protest, budget line, appropriation, subsidy decision, or funding cliff?
- Does the company’s latest filing quantify or discuss the exposure?

If procurement/grant materiality cannot be supported, route the candidate as a `Verification Lead`, demote it to `Lower-Signal Items`, or omit it even when the politician role, jurisdiction, sector theme, filing recency, or tracker popularity appears relevant.

Keep this lane internal in standard output. Surface only the practical implication through existing fields such as `Why it matters:`, `Why it is not a strong signal:`, `Why These Ranked`, `Source Caveat`, or `Best next command:` unless the user explicitly asks for detailed evidence or audit-style output.


### 16. Procurement-Dependent Thesis Cap — P0

If the politician lead depends on government spending, defense exposure, aerospace procurement, infrastructure funding, health care reimbursement, energy subsidies, agency awards, grants, or public-sector contracts, apply this cap before ranking.

Company filings alone may support a broad government-exposure research lead, but they do not create a named procurement or policy-catalyst lead unless one of the following is also verified:

- Specific contract, award, grant, subsidy, budget line, RFP, solicitation, program, or agency action.
- Company-disclosed backlog, revenue, customer concentration, or program exposure tied to the relevant government area.
- Official procurement or spending source such as USAspending, SAM.gov, FPDS-linked data, agency award release, Federal Register, Congress.gov, or equivalent.
- Company 8-K, 10-K, 10-Q, earnings release, or investor material that quantifies or specifically describes the relevant exposure.

If only broad government or defense exposure is verified, use language such as:

- `defense-exposure research lead`
- `government-spending exposure`
- `policy-sensitive industrial lead`
- `needs procurement/program verification`

Do not use language implying a named catalyst, contract, program, NDAA-specific benefit, agency award, grant, subsidy, or procurement win unless that link is verified.

If this cap is not cleared, the candidate may still be a broad policy-sensitive research lead, but it should be routed as `Cleared with heavy caveat`, `Verification Lead`, or `Lower-Signal Item` depending on the strength of company-level materiality and the remaining diligence question. Do not promote the candidate as a named procurement/program catalyst.

Keep this cap internal in standard output. Surface only the appropriate level of precision through `Why it matters:`, `Why it is not a strong signal:`, `Why These Ranked`, `Lower-Signal Items`, and `Source Caveat` unless the user explicitly asks for detailed evidence, sources, or audit-style output.

### 17. Market Absorption / Next-Milestone Enforcement — P0 Ranking Gate

For every candidate considered for Best Stock Leads, check whether the market appears to have already absorbed the disclosure, event, or catalyst. This gate prevents stale, widely covered, already-priced, or reaction-only leads from ranking without a remaining company-specific diligence question.

Check absorption context around:

- Transaction date.
- Filing/disclosure date.
- Relevant policy, regulatory, procurement, grant, enforcement, tariff, or company event.
- Major related news coverage.
- Company price reaction and volume reaction when market data is available.

Classify absorption internally as one of:

- `Checked — not obviously absorbed` — clear upcoming milestone or under-researched company-specific question remains.
- `Checked — partly absorbed` — market reacted, but a specific next catalyst or materiality question remains.
- `Checked — mostly absorbed` — disclosure/event is stale, widely covered, or already priced without a clear next diligence question.
- `Not checked` — insufficient market/news context was reviewed in the run.

Mostly absorbed leads should be demoted unless there is still a specific, evidence-testable next milestone, such as an RFP, award, renewal, protest, final rule, effective date, budget vote, appropriation, subsidy decision, grant decision, funding cliff, agency approval, enforcement outcome, earnings/backlog disclosure, or filing-backed materiality question.

If absorption status is `Not checked`, avoid ranking the candidate unless the rest of the evidence pack is unusually strong. If a `Not checked` lead still ranks, include this visible caveat in `Why it is not a strong signal:` or another existing caveat field:

`Market absorption was not fully checked in this run, so the lead may already be partly reflected in price/news.`

Keep this gate internal in standard output. Surface only the practical implication through existing fields such as `Why it matters:`, `Why it is not a strong signal:`, `Why These Ranked`, `Source Caveat`, or `Best next command:` unless the user explicitly asks for detailed evidence or audit-style output.

Do not imply causality, intent, non-public information, wrongdoing, or recommendation from market reaction or lack of reaction. Market absorption is a research-prioritization input only.

### 18. Company-Materiality Test

A policy link is not enough. A politician disclosure becomes a stronger research lead only when the policy, procurement, regulation, tariff, subsidy, agency action, or event context appears financially material to the company.

Use this test to support the contract's goal of ranking by company-level research usefulness rather than politician fame, ticker fame, or trade size.

Check whether the policy/event nexus could plausibly affect:

- Revenue, demand, bookings, backlog, or customer concentration.
- Margins, costs, input prices, tariffs, duties, reimbursement, or pricing power.
- Procurement, awards, government contracts, contract renewals, or funding exposure.
- Subsidies, tax credits, grants, permitting, licensing, approvals, or eligibility.
- Regulatory burden, enforcement exposure, compliance costs, product approval, or market access.
- Capital spending, project economics, financing access, balance-sheet risk, or valuation/rerating setup.

Prefer Best Stock Leads candidates where the materiality question is testable with company filings, segment disclosures, contract/backlog data, customer exposure, regulatory filings, agency records, or other source-backed evidence.

Demote or caveat disclosures where the connection is only thematic, sector-level, or headline-driven and there is no clear evidence that the policy/event is financially material to the company.

### 19. Cross-Signal Triangulation

After a politician disclosure clears the candidate gate, check whether independent public signals support, weaken, or contextualize the company-level research lead.

Relevant cross-signals may include:

- Form 4 insider activity.
- 8-Ks and other company filings.
- 10-K / 10-Q disclosures, segment exposure, risk factors, backlog, customer concentration, or guidance language.
- Contract awards, procurement databases, grant awards, subsidy awards, or agency spending data.
- Rulemakings, proposed rules, final rules, agency guidance, tariffs, enforcement actions, investigations, approvals, permitting, or licensing actions.
- Earnings releases, guidance changes, investor presentations, press releases, or other company disclosures.

Use triangulation to strengthen, caveat, demote, or redirect the next research command. A lead is stronger when politician-disclosure timing, policy/event nexus, company materiality, and independent public company/regulatory/procurement evidence point to the same research question.

Do not imply coordination, intent, non-public information, wrongdoing, or causality from cross-signal alignment. Cross-signal triangulation is an evidence-quality check, not an allegation engine.

### 20. Sector Cluster Lens

Check whether multiple public officials have disclosed company-specific activity in the same policy-sensitive sector, agency-exposed industry, or procurement theme within a relevant event window.

Cluster signals may be more useful when:

- The companies share a specific policy, agency, tariff, subsidy, procurement, or regulatory exposure.
- The cluster points to an under-researched sector or small/mid-cap company.
- Independent company filings support material exposure.
- The cluster is transaction-date-based rather than filing-date-only.
- The cluster survives issuer/security identity checks and is not driven by ETFs, diversified funds, or broad index products.

Cluster signals should be demoted when:

- The names are broad mega-cap market leaders.
- The link is only thematic.
- The cluster is driven by ETFs or diversified funds.
- Timing is stale or filing-date-based rather than transaction-date-based.
- The companies do not share a specific, financially material policy/event/procurement/regulatory exposure.

Use this lens to surface better theme-level research leads, but do not let it override company-level diligence. A cluster should still produce a clear company-specific or sector-specific research question that can be tested with filings, procurement data, agency records, regulatory records, or company disclosures.

Do not imply coordination, intent, non-public information, causality, or wrongdoing from clustering.

### 21. Lead-Type Routing

Classify politician disclosure candidates internally before final ranking as one of these lead types:

- `Opportunity Lead` — the disclosure points to a potentially favorable company-level research question tied to financially material policy, procurement, regulation, tariff, subsidy, agency, contract, or event exposure.
- `Risk Lead` — the disclosure points to a company-specific downside question, such as regulatory burden, enforcement exposure, tariff or cost pressure, contract loss, funding risk, reimbursement risk, approval risk, policy headwind, or balance-sheet fragility.
- `Verification Lead` — the disclosure may be interesting, but identity, ticker mapping, owner, date, event window, source disagreement, disclosure mechanics, or company materiality requires verification before ranking strongly.
- `Noise Lead` — the disclosure is too broad, routine, stale, tiny, diversified, owner-ambiguous, thematic-only, or lacks policy/event nexus, company materiality, or a clear company-level research question.

Use lead-type routing internally to choose whether to rank, caveat, demote, omit, or redirect the next command. Opportunity and Risk Leads may rank when evidence supports them. Verification Leads usually need caveats or follow-up verification before ranking highly. Noise Leads should not enter Best Stock Leads.

Do not display these lead-type labels in standard politician output unless the user asks for detailed or audit output. Express the effect through `Why it matters:`, `Why it is not a strong signal:`, and `Best next command:`.

### 22. False Positive Suppression — Internal Gate

Before promoting a politician disclosure candidate to Best Stock Leads, check whether the signal is likely a false positive. This gate exists to keep Best Stock Leads focused on company-level research leads rather than headline-driven disclosure noise.

Common false positives include:

- Famous politician + famous ticker, but no company-specific research question.
- Broad ETF or fund exposure incorrectly treated as company-specific exposure.
- Routine household mega-cap trade with no role, event, or material policy link.
- Disclosure filed recently but transaction occurred long before the relevant event.
- Policy link is sector-level only and not financially material to the company.
- Convenience-source ticker mapping is uncertain.
- Owner is spouse, trust, or managed account and control is unclear.
- Trade is small relative to the filer's normal disclosed pattern.
- Sale appears tax, rebalancing, diversification, option-exercise, or liquidity-related when context supports that caveat.
- News event occurred before the transaction but is being framed as if the trade predicted it.

A candidate should not survive this gate unless it has:

- Resolved or probable issuer/security identity.
- Transaction-date timing context.
- Transaction-date role/jurisdiction context when relevant.
- A company-specific research question.
- At least one material policy/event/procurement/regulatory nexus.

For politician Best Stock Leads candidates, apply the Market Absorption / Next-Milestone Enforcement gate above. If the signal appears mostly absorbed or stale, demote unless there is still a company-specific, evidence-testable next milestone or research question.

If a candidate triggers multiple false-positive checks, demote it to `Lower-Signal Items` or omit it. Do not use Best Stock Leads placement to preserve weak, headline-driven, stale, ambiguous, mostly absorbed, or non-company-specific disclosures.

## Best Stock Leads Ranking

Politician mode uses one visible ranked section only:

- `## Best Stock Leads`

Do not show duplicate ranked sections in standard politician output. Raw disclosure strength and research usefulness are internal lenses that feed Best Stock Leads.

Best Stock Leads candidates should be ranked by company-level research usefulness, not by ticker fame, politician fame, raw trade count, or amount range alone.

A candidate can rank when it combines:

- A meaningful disclosure signal.
- At least one Politician Candidate Gate factor.
- A specific policy/event nexus.
- A clear company-level research reason.
- A caveat that does not overwhelm the signal.

Do not fill Best Stock Leads just to reach three names. If there is only one strong lead, show one. If no candidate clears the gate, say no clean politician stock lead was found and use `Lower-Signal Items` only when useful.

## Politician Candidate Cards

Politician cards must look different from fund-manager cards.

Use these visible fields in standard output:

- `[TICKER] | [Company Name]`.
- `Why it matters:` company-specific research reason tied to the disclosure pattern.
- `Why it is not a strong signal:` delay, broad range, owner ambiguity, no intent evidence, source disagreement, ETF/diversified exposure, weak policy/event nexus, or other material limitation.
- `Best next command:` `!research` or `!risk` only.

Do not use the fund-manager `Capital-allocation signal:` or `Chase Filter:` fields for politician cards. Do not use the old politician `Signal type:`, `Policy/event nexus:`, `Why it ranks:`, or `Key caveat:` fields in standard output unless full/audit mode explicitly asks for contract/debug detail.

Keep candidate cards compact. Do not expose default internal labels such as `Disclosure strength:`, `Anomaly level:`, `Policy relevance:`, `Research attractiveness:`, or numeric scores in standard output.

## Demotion / Lower-Signal Items

Move to `Lower-Signal Items`, demote, or omit when the disclosure is material enough for context but not a strong current research lead:

- Obvious mega-cap trades unless size, timing, repetition, or policy/event nexus is unusual.
- Broad ETFs.
- Tiny trades.
- Old trades.
- Common household stocks with no clear research angle.
- Sales with no clear forward research signal.
- Ambiguous owner/source/date/value details that overwhelm the signal.
- Source-dependent metrics that cannot be reconciled in the run.
- No clear jurisdiction, policy, regulatory, procurement, or event link.

Demotion language should be specific, not generic. Prefer reasons such as `broad ETF`, `small disclosed value range`, `stale transaction`, `source-dependent trade count`, `routine mega-cap exposure`, `owner ambiguity`, `no clear policy/event nexus`, or `no clear company-level research question`.

## Output Relationship

Standard politician output is governed by `skills/stock-analysis/tracker/OUTPUT.md`. That file owns section order, field placement, and any compact runtime-transparency line. This contract supplies the intelligence logic only; it should not create extra visible ranking-basis, contract-debug, or roster-receipt sections in standard output.

Standard politician output uses:

- `Tracking Politician | [Person Name]`
- `Current Role`
- `Summary`
- `What Changed`
- `Best Stock Leads`.
- `Why These Ranked`, only when at least one candidate ranks in Best Stock Leads.
- `Lower-Signal Items`, when material lower-signal disclosures need visibility.
- `Source Caveat`

Best next commands belong inside Best Stock Leads candidate cards for politician mode. If no clean stock lead exists, omit best-next-command wording.

## Guardrails

Politician tracker outputs must not:

- Use copy-trading language.
- Display copy-trading returns, strategy returns, excess-return charts, or marketing claims.
- Imply non-public information.
- Imply wrongdoing or suspicious conduct without evidence.
- Present disclosure activity as a buy/sell/hold recommendation.
- Treat broad value ranges as precise transaction values.
- Treat convenience-source metrics as authoritative when source methodology is unclear.
- Leak unresolved placeholders or template instructions.

Use cautious wording such as:

- `unusual disclosure`.
- `policy-sensitive sector`.
- `policy/event overlap`.
- `possible research lead`.
- `worth researching`.
- `needs verification`.
- `source-dependent`.

Avoid:

- `suspicious`.
- `they know something`.
- `copy this trade`.
- `politician alpha`.
- `best trader`.

## Relationship to Global Rules

Use global MIDAS rules for shared standards:

- `rules/SOURCES.md` governs source hierarchy, materiality, freshness, and source confidence.
- `rules/CLASSIFICATIONS.md` governs setup classifications and modifiers.
- `rules/SCORING.md` governs scoring and overlays when scoring is explicitly useful.
- `rules/OUTPUT.md` governs shared output principles and Best Next Command routing.
- `rules/ARTIFACTS.md` governs artifact paths and save behavior.

This contract should not create new global classifications, scoring systems, artifact paths, or recommendation language.
