# !thesis Output Contract

## Command

Command: `!thesis`

Skill File: `skills/stock-analysis/thesis/SKILL.md`

Output File: `skills/stock-analysis/thesis/OUTPUT.md`

Registry Entry: `docs/COMMAND_REGISTRY.md`

Status: `Draft`

---

## Registry Consistency

This output contract should match the command’s Registry Metadata block in the command `SKILL.md` and the command row in:

`docs/COMMAND_REGISTRY.md`

Expected registry values:

- Command: `!thesis`
- Aliases: `/thesis`, `thesis`
- Category: `Thesis Analysis`
- Status: `Draft`
- Skill path: `skills/stock-analysis/thesis/SKILL.md`
- Output path: `skills/stock-analysis/thesis/OUTPUT.md`
- Eval file: `evals/thesis.eval.md`
- Classification: `Optional`
- Scoring: `Optional`
- Metrics: `Required`
- Artifacts: `Yes`

If this output file and the registry disagree, treat that as registry drift. Do not patch the registry unless that is explicitly in scope.

---

## Purpose

This file defines the command-specific output contract for `!thesis`.

`!thesis` output should present either:

- a Standard-only filing-backed long-term thesis memo,
- a Standard-only living thesis update, or
- a no-write audit of new-thesis or update readiness.

It should focus on core thesis, why it matters, thesis pillars, evidence, financial support, variant view, catalysts, risks, thesis breakers, monitoring points, verification gaps, concise source notes, and artifact behavior.

This file defines output shape only. Workflow belongs in `skills/stock-analysis/thesis/SKILL.md`. Source hierarchy belongs in `rules/SOURCES.md`. Metric definitions belong in `rules/METRICS.md`. Rerating discipline belongs in `rules/RERATING.md` when used. Artifact policy belongs in `rules/ARTIFACTS.md`.

---

## Global Output Inheritance

`!thesis` must follow:

- `/home/jordan/.hermes/profiles/midas/rules/GLOBAL.md`
- `/home/jordan/.hermes/profiles/midas/rules/COMMAND_INTERFACE.md`
- `/home/jordan/.hermes/profiles/midas/rules/SOURCES.md`
- `/home/jordan/.hermes/profiles/midas/rules/METRICS.md` when metrics appear.
- `/home/jordan/.hermes/profiles/midas/rules/MARKET_DATA.md` when market data appears.
- `/home/jordan/.hermes/profiles/midas/rules/RERATING.md` when rerating, post-rerate, overextension, market-expectations, or valuation-setup language appears.
- `/home/jordan/.hermes/profiles/midas/rules/OUTPUT.md`
- `/home/jordan/.hermes/profiles/midas/rules/ARTIFACTS.md`
- `/home/jordan/.hermes/profiles/midas/rules/CLASSIFICATIONS.md` when classification is used.
- `/home/jordan/.hermes/profiles/midas/rules/SCORING.md` when scoring is used.

Do not duplicate global rulebooks in this file.

---

## Output Philosophy

`!thesis` should read like a concise analyst thesis memo, not a worksheet, source dump, valuation model, or promotional pitch.

Good `!thesis` output is:

- thesis-led,
- filing-backed,
- clear about current evidence vs future requirements,
- clear about what is proven, unproven, and thesis-breaking,
- useful for monitoring future filings and disclosures,
- concise enough to read, but complete enough to be a durable living thesis,
- free of recommendation language.

Avoid:

- hype,
- Buy/Sell/Hold language,
- price targets,
- position sizing or trade advice,
- false precision,
- unsupported market-mispricing claims,
- default cheap / expensive / fair-value conclusions,
- price action, market cap, volume, liquidity, or valuation multiples presented as proof of thesis pillars,
- treating management goals or TAM claims as facts,
- long filing dumps,
- full financial-statement review that belongs in `!financials`,
- downside-only risk memo that belongs in `!risk`,
- complete packet synthesis output,
- false saved claims,
- watchlist mutation claims,
- downstream command auto-runs.

---

## Supported Output Modes

Supported:

- Normal: supported. This is the default Standard-only filing-backed thesis memo.
- Update: supported through `!thesis update [ticker]`. This is the Standard-only living-thesis refresh workflow.
- Audit: supported through `-audit`. This is no-write readiness output.

Default:

- Normal Standard-only filing-backed thesis memo.

Clarifications:

- Former compact words are style hints or boundary prompts, not modes.
- Former full/deep words route to better commands when appropriate, unless the user asks for a specific thesis component.
- `update` is a subcommand / living-thesis workflow, not an output mode.
- `-audit` is no-write and has separate audit output.
- Single-dash `-audit` is canonical.
- If the user uses `--audit`, return: `Use -audit for !thesis audit mode.`

---

## Required Title Format

Use:

```md
# 🏛 [TICKER] | [Company Name] Thesis
```

Example:

```md
# 🏛 HOOD | Robinhood Markets, Inc. Thesis
```

---

## Normal Standard-Only Output Shape

Every successful normal `!thesis [ticker]` response should include the Standard-only sections below unless the command cannot complete.

Required section order:

1. `# 🏛 [TICKER] | [Company Name] Thesis`
2. `## Introduction`
3. `## Summary`
4. `## Core Thesis`
5. `## Why It Matters`
6. `## Thesis Pillars`
7. `## Evidence`
8. `## Financial Support`
9. `## Variant View`
10. `## Catalysts`
11. `## Risks`
12. `## Thesis Breakers`
13. `## What To Monitor`
14. `## What To Verify Next`
15. `## Source Notes`
16. `## Best Next Command`, when useful
17. `Saved to: workspace/tickers/[ticker]/thesis.md`

Normal output must not collapse into a compact summary, completion receipt, artifact summary, or checklist.

### Normal Standard Template

```md
# 🏛 [TICKER] | [Company Name] Thesis

## Introduction
[2–4 sentence clean scope statement covering company name/ticker, source basis in plain English, thesis scope, and non-recommendation boundary. Do not display CIK, accession numbers, raw SEC URLs, primary document filenames, internal tool paths, source-recovery metadata, or long filing metadata blocks.]

## Summary
[Short conclusion-first summary of the thesis, biggest support, biggest unproven assumption, and main thesis breaker.]

## Core Thesis
[1–2 sentence long-term thesis framed as a possibility, not a guaranteed outcome.]

## Why It Matters
[Why this thesis could matter economically or strategically if evidence develops. Avoid claiming the market is wrong without evidence.]

## Thesis Pillars
1. [Pillar name]
   [What must be true, current evidence, what remains unproven, and what to monitor.]

2. [Pillar name]
   [Repeat for 3–6 pillars when useful.]

## Evidence
[Selective source-backed evidence supporting or weakening the thesis. Separate reported facts, management claims, MIDAS interpretation, and unproven assumptions.]

## Financial Support
[Conclusion-first discussion of whether financials support, weaken, or do not yet prove the thesis. Use only thesis-relevant metrics. Follow METRICS.md.]

## Variant View
[What may be underappreciated, misunderstood, not yet proven, or absent. Include information gap. If no clear variant view exists, say so.]

## Catalysts
[3–5 catalysts or validation milestones when material. Include timing only when disclosed or source-backed.]

## Risks
[Material risks that could weaken the thesis. Include disconfirming evidence here when useful.]

## Thesis Breakers
[Specific developments that would break or materially invalidate the thesis.]

## What To Monitor
[Short monitoring points tied to the thesis pillars, risks, catalysts, and financial support.]

## What To Verify Next
[Evidence gaps, missing disclosures, source limitations, or diligence steps needed next.]

## Source Notes
- [Filing type] — filed [date]; period ended [date]; used for [source basis].
- [Company release / earnings release] — dated [date]; used for [source basis], if material.
- [Investor presentation] — dated [date]; used for [source basis], if material.
- [Existing workspace artifact] — dated [date or unknown]; used as secondary synthesis input only, if used.

## Best Next Command
`!command TICKER` — Reason.

Saved to: workspace/tickers/[ticker]/thesis.md
```

---

## Update Output Shape

Every successful `!thesis update [ticker]` response should include the Standard-only update sections below unless the command cannot complete.

Required section order:

1. `# 🏛 [TICKER] | [Company Name] Thesis`
2. `## Introduction`
3. `## Summary`
4. `## Update Notes`
5. `## Core Thesis`
6. `## Thesis Pillars`
7. `## Evidence`
8. `## Financial Support`
9. `## Variant View`
10. `## Catalysts`
11. `## Risks`
12. `## Thesis Breakers`
13. `## What To Monitor`
14. `## What To Verify Next`
15. `## Source Notes`
16. `## Best Next Command`, when useful
17. `Saved to: workspace/tickers/[ticker]/thesis.md`

Update output must be a refreshed clean thesis, not just a changelog. It must load the existing baseline first and overwrite only `workspace/tickers/[ticker]/thesis.md` after completing the refreshed thesis.

### Update Template

```md
# 🏛 [TICKER] | [Company Name] Thesis

## Introduction
[2–4 sentence clean scope statement covering company name/ticker, living-thesis refresh scope, source basis in plain English, prior thesis review, and non-recommendation boundary. Do not display CIK, accession numbers, raw SEC URLs, primary document filenames, internal tool paths, source-recovery metadata, or long filing metadata blocks.]

## Summary
[Short conclusion-first summary of whether the thesis strengthened, stayed mostly unchanged, weakened, moved under review, or broke.]

## Update Notes
- Previous thesis reviewed: Yes
- Previous thesis date: [date or unknown]
- New sources reviewed: [concise list]
- Thesis direction: [Strengthened / Mostly Unchanged / Weakened / Under Review / Broken]
- Reason: [short source-backed explanation]

## Core Thesis
[Current refreshed long-term thesis framed as a possibility, not a guaranteed outcome.]

## Thesis Pillars
1. [Pillar name] — Status: [Strengthened / Unchanged / Weakened / Not Yet Testable / Broken]
   [Prior thesis requirement, new evidence, interpretation, unproven assumption, and monitor.]

2. [Pillar name] — Status: [Strengthened / Unchanged / Weakened / Not Yet Testable / Broken]
   [Repeat for existing or refreshed pillars.]

## Evidence
[New and prior evidence synthesis. Separate old thesis, new evidence, interpretation, and unproven assumptions.]

## Financial Support
[Whether updated financial evidence supports, weakens, or does not yet prove the thesis. Follow METRICS.md when metrics appear.]

## Variant View
[Updated information gap or variant view.]

## Catalysts
[Updated catalysts or validation milestones.]

## Risks
[Updated risks and disconfirming evidence.]

## Thesis Breakers
[Updated thesis-breaking conditions.]

## What To Monitor
[Updated monitoring points.]

## What To Verify Next
[Evidence gaps, missing disclosures, source limitations, or diligence steps needed next.]

## Source Notes
- [Filing type] — filed [date]; period ended [date]; used for [source basis].
- [Company release / earnings release] — dated [date]; used for [source basis], if material.
- [Investor presentation] — dated [date]; used for [source basis], if material.
- [Existing workspace artifact] — dated [date or unknown]; used as secondary synthesis input only, if used.

## Best Next Command
`!command TICKER` — Reason.

Saved to: workspace/tickers/[ticker]/thesis.md
```

### Update Workflow Labels

Overall thesis direction labels:

- `Strengthened`
- `Mostly Unchanged`
- `Weakened`
- `Under Review`
- `Broken`

Pillar status labels:

- `Strengthened`
- `Unchanged`
- `Weakened`
- `Not Yet Testable`
- `Broken`

These are local update workflow labels. They are not Setup Classifications and should not be promoted into a second global classification system.

---

## Source Notes

Normal Source Notes should be concise.

Do not require CIK, raw SEC URLs, or accession numbers by default unless needed for disambiguation.

Preferred normal Source Notes format:

```md
## Source Notes
- [Filing type] — filed [date]; period ended [date]; used for [source basis].
- [Company release / earnings release] — dated [date]; used for [source basis].
- [Investor presentation] — dated [date]; used for [source basis], if material.
- [Existing workspace artifact] — dated [date or unknown]; used as secondary synthesis input only, if used.
```

Accession numbers and URLs may remain internal and may appear in audit, source-recovery, or debug contexts when useful.

Normal Source Notes should preserve:

- filing/source type,
- filing/source date,
- period or report date,
- source basis,
- source freshness,
- missing disclosures,
- source limitations,
- calculated metric labeling when relevant,
- explicit distinction between primary sources and workspace-artifact synthesis inputs.

Source limitations should usually live in `## Source Notes` and `## What To Verify Next`, not as a separate required top-level section.

---

## Market / Valuation / Rerating Output Boundary

Do not require live/current market data by default.

Do not require valuation / rerating context by default.

Use market data, valuation context, or rerating-stage context only when:

- the user explicitly requests it, or
- it is materially needed for thesis framing, rerating-stage context, valuation setup, post-rerate discipline, or a thesis-breaker / catalyst discussion.

If market data is used:

- label provider/source and as-of date,
- make clear that market data is context only, not thesis proof,
- keep it bounded and placed inside the most relevant section, usually `## Financial Support`, `## Variant View`, `## Catalysts`, `## Risks`, or `## What To Verify Next`,
- follow `MARKET_DATA.md`, `METRICS.md`, and `RERATING.md` when applicable,
- avoid default cheap / expensive / fair-value conclusions,
- avoid price targets,
- avoid full valuation models by default,
- do not guess unavailable market cap, enterprise value, multiples, liquidity, price performance, or rerating stage.

Do not use market data to prove thesis pillars, business quality, moat, growth durability, margin expansion, cash-flow durability, risk reduction, customer claims, segment claims, or management execution.

---

## Audit Output

Audit output is no-write. It must not include:

- raw source dump,
- hidden reasoning,
- scratch work,
- tool logs,
- internal prompts,
- giant filing excerpts,
- saved-path confirmation,
- artifact write claims.

Audit output must not write files, create folders, create artifacts, update indexes, mutate watchlists, auto-run downstream commands, create schemas, create proof packets, create source manifests, create evidence ledgers, or create fixture files.

### New-Thesis Audit Output

Use this output only for:

`!thesis [ticker] -audit`

```md
# [TICKER] | !thesis Audit

Audit Result: Pass / Partial / Blocked

## Source / Filing Basis
[Latest annual/interim basis, source availability, freshness, and whether source basis appears sufficient for a new thesis.]

## Existing Artifact Status
[Whether `workspace/tickers/[ticker]/thesis.md` exists, read-only status, and any artifact-path concerns.]

## Standard Output Contract Check
[Whether the expected output can satisfy the Standard-only section/order/save-path contract.]

## Thesis Coverage
[Whether core thesis, thesis pillars, evidence, financial support, variant view, catalysts, risks, thesis breakers, monitors, verification gaps, and source notes appear supportable.]

## Missing Evidence
[Missing filings, missing disclosures, weak source areas, or unproven thesis requirements.]

## Source Limitations
[Source freshness, unavailable data, citation limits, or primary-source gaps.]

## Output Safety
[Recommendation, valuation, market-data, metric-labeling, source, and unsupported-claim risks.]

## Artifact / Write Boundary
[Confirmation that audit wrote nothing, created no artifacts/folders, and made no saved-path claim.]

## Recommended Next Step
[One concise next step. Do not auto-run it.]

No files changed — audit mode was read-only.
```

### Update Audit Output

Use this output only for:

`!thesis update [ticker] -audit`

```md
# [TICKER] | !thesis Update Audit

Audit Result: Pass / Partial / Blocked

## Existing Thesis Status
[Whether `workspace/tickers/[ticker]/thesis.md` exists and can be reviewed read-only. If missing, include: `No baseline thesis exists yet for [ticker]. Run !thesis [ticker] first.`]

## Source / Filing Basis
[Latest annual/interim basis, new source availability, freshness, and whether source basis appears sufficient for update review.]

## Update Readiness
[Whether the baseline and new evidence are sufficient to compare prior thesis pillars against new evidence.]

## Pillar Coverage
[Whether prior thesis pillars can be identified and tested; note any missing or ambiguous pillars.]

## Missing Evidence
[Missing filings, missing disclosures, weak source areas, or untested update requirements.]

## Source Limitations
[Source freshness, unavailable data, citation limits, or primary-source gaps.]

## Output Safety
[Recommendation, valuation, market-data, metric-labeling, source, and unsupported-claim risks.]

## Artifact / Write Boundary
[Confirmation that audit wrote nothing, created no artifacts/folders, did not overwrite thesis.md, and made no saved-path claim.]

## Recommended Next Step
[One concise next step. Do not auto-run it.]

No files changed — audit mode was read-only.
```

### Blocked Audit Fallback

If no-write cannot be guaranteed, stop before source gathering and return:

```md
Audit Result: Blocked

Could not guarantee no-write behavior for !thesis [ticker] -audit, so source gathering was not started.

Would have checked:
- source basis
- existing thesis status, if any
- thesis coverage
- missing evidence
- source limitations
- output safety
- artifact status

Required before audit can run:
- patch SKILL.md and OUTPUT.md to make -audit override all artifact, compact artifact, update artifact, version, index, watchlist, manifest, ledger, proof-packet, schema, fixture, and downstream-command writes.

No files changed — audit blocked.
```

For update audit with no baseline, return Blocked or Partial depending command semantics, include the no-baseline message, and write nothing.

---

## Removed / Replaced Default Sections

The following are not default top-level sections in the simplified Standard-only `!thesis` contract:

- `## Bottom Line`
- `## Sources Used`
- `## Variant View / Information Gap`
- `## Catalysts and Monitoring`
- `## Risk and Failure Points`
- `## Thesis Strength / Weakness Rules`
- `## Final Thesis Status`
- `## Source Limitations`
- `## Evidence Ledger`
- `## Pillar Evidence Audit`
- `## Bull / Base / Bear Case`
- `## Disconfirming Evidence`
- `## Monitoring Dashboard`
- `## Open Questions`
- `## Valuation / Rerating Context` as a default top-level section
- `## Market Data Limitations` as a default top-level section

Do not remove the underlying concepts:

- Information gap belongs inside `## Variant View`.
- Monitoring belongs inside `## What To Monitor`.
- Failure points belong inside `## Thesis Breakers`.
- Disconfirming evidence belongs inside `## Risks`, `## Thesis Breakers`, or `## What To Verify Next`.
- Source limitations belong inside `## Source Notes` and `## What To Verify Next`.
- Bull/base/bear thinking may appear inside `## Variant View` or `## Thesis Pillars` when useful, but not as a default slash heading.
- Valuation/rerating context may appear only when explicitly requested or materially needed, usually inside `## Financial Support`, `## Variant View`, `## Catalysts`, `## Risks`, or `## What To Verify Next`.

---

## Best Next Command

Best Next Command is optional in normal and update output and should be context-aware. When included, it must appear as a standalone report-style section after `## Source Notes` and before the final saved-path confirmation line.

Required format:

```md
## Best Next Command

`!command TICKER` — Reason.
```

Rules:

- Use `## Best Next Command` as the section heading.
- Insert one blank line after the heading.
- Use command-first format with the command wrapped in backticks.
- The reason after the dash should begin with a capital letter and end with a period when sentence-style.
- Do not recommend a next command when it would be noisy or unnecessary.
- Do not auto-run the next command.
- The saved-path confirmation must remain the final line after Best Next Command when a save occurs.

---

## Artifact Behavior

Writes artifacts: `Yes` for normal and update; `No` for audit.

Artifact behavior follows:

`/home/jordan/.hermes/profiles/midas/rules/ARTIFACTS.md`

Default artifact behavior:

- Normal `!thesis [ticker]` saves by default when complete.
- Update `!thesis update [ticker]` saves by default when complete and overwrites the same living thesis after loading the existing baseline.
- Audit writes nothing.

Artifact locations:

- Normal: `workspace/tickers/[ticker]/thesis.md`
- Update: `workspace/tickers/[ticker]/thesis.md`
- Audit: no artifact

When normal or update artifact is written, output should include exactly one saved-path confirmation, and in normal user-facing output it must be the final line:

```md
Saved to: workspace/tickers/[ticker]/thesis.md
```

Do not claim an artifact was written unless it was actually created or overwritten successfully.

Do not use old artifact paths that place ticker folders directly under the workspace root.

Do not save incomplete output as `thesis.md`.

Do not create:

- `thesis.compact.md`,
- `thesis-update.md`,
- timestamped thesis history by default,
- version files unless explicitly requested,
- source manifest files,
- evidence ledger files,
- proof packets,
- schemas,
- fixture files,
- missing workspace artifacts.

Do not update indexes, mutate watchlists, or auto-run downstream commands.

Do not include a separate Artifact section by default.

---

## Pre-Save Validation

Before saving `workspace/tickers/[ticker]/thesis.md`, hard-stop and do not save if any validation fails:

- Required normal or update sections are missing or out of order.
- The output contains compact-style, full-style, or deep-style replacement structure instead of the required Standard-only sections.
- `!thesis update` output lacks `## Update Notes`.
- `!thesis update` was requested but no existing living thesis was loaded.
- Update output has thesis pillars without required pillar status labels.
- Material thesis claims are not tied to filing/source support in the relevant section, not just a generic source list.
- Metrics appear without period/source/definition labels required by `METRICS.md`.
- Market data is used by default without explicit request or material need.
- Market data is used to prove thesis pillars or filing-backed thesis evidence.
- Market data is included without provider/source and as-of date when those details are required.
- The output turns market context into a full valuation model, price target, Buy/Sell/Hold view, position-sizing view, entry/exit view, trade-timing view, unsupported cheap/expensive/fair-value conclusion, or proof that the thesis is correct.
- `## Best Next Command`, when included, does not appear after `## Source Notes` and before the final saved-path confirmation line.
- The saved-path confirmation is not the final line after a successful write.
- The output contains Buy/Sell/Hold language, a price target, position sizing, or trade execution advice.
- The output contains false saved claims, watchlist mutation claims, or downstream command auto-run claims.
- The output contains hidden reasoning, scratch work, tool logs, internal prompts, source dumps, proof-packet language, source-manifest language, evidence-ledger language, schema references, or fixture references as generated artifacts.

If validation fails, return failure output and do not claim a save.

---

## Classification / Scoring Display

Setup Classification:

- Optional only.
- Include only if the user explicitly asks or if the output includes a setup view.
- If included, follow `CLASSIFICATIONS.md`.

Global Research Score:

- Not default.
- Do not create a new thesis score formula.
- If scoring is explicitly requested, follow `SCORING.md`.

Evidence Confidence:

- Optional.
- More appropriate for audit or explicit request than default normal output.
- Do not add as a default label unless clearly justified by requested setup view or supported command behavior.

Thesis status / update labels:

- Thesis status labels may remain local thesis workflow labels when useful.
- Update direction labels are local update workflow labels only.
- Pillar status labels are local update workflow labels only.
- None of these local labels are Setup Classifications.
- Do not create new classification labels.
- Do not create red/yellow/green systems unless already explicitly supported.

---

## Output Guardrails

Normal, update, and audit output must avoid:

- Buy/Sell/Hold language,
- price targets,
- position sizing,
- trade advice,
- recommendation framing,
- default cheap/expensive/fair-value conclusions,
- unsupported valuation conclusions,
- full valuation model by default,
- false saved claims,
- watchlist mutation claims,
- downstream command auto-runs,
- unsupported thesis claims,
- guaranteed outcome language,
- unlabeled metrics,
- stale market data presented as current,
- raw source dumps,
- hidden reasoning,
- scratch work,
- tool logs,
- internal prompts,
- giant filing excerpts.

Do not change:

- registry status,
- evals,
- references,
- global rules,
- source hierarchy,
- metric definitions,
- classification/scoring optionality,
- artifact paths except removing compact/update-version artifacts from active default behavior.

---

## Failure Output

If update mode has no baseline thesis, return:

```md
No baseline thesis exists yet for [ticker]. Run !thesis [ticker] first.
```

Do not create a baseline thesis.

Do not write anything.

If no-write audit cannot be guaranteed, use the Blocked Audit Fallback and do not gather sources.

If required source evidence is unavailable, say what is missing, state the limitation, and do not force a thesis or claim a save unless a complete valid artifact was actually written.

---

## Final Line Rules

Normal successful save:

```md
Saved to: workspace/tickers/[ticker]/thesis.md
```

Update successful save:

```md
Saved to: workspace/tickers/[ticker]/thesis.md
```

Audit:

```md
No files changed — audit mode was read-only.
```

Blocked audit:

```md
No files changed — audit blocked.
```

The saved-path confirmation appears only after successful write verification and exactly once at the end of normal/update output.

## Final Rule

`!thesis` output is Standard-only for normal thesis construction and living-thesis updates, with no-write audit as the only alternate display contract.

It should be thesis-led, filing-backed, concise, skeptical, source-visible, and artifact-disciplined.

It should not become a mode matrix, stock pitch, recommendation, full valuation model, source dump, proof-packet workflow, or second global classification/scoring system.
