# MIDAS Command Registry

## Purpose

COMMAND_REGISTRY.md is the human-readable index of MIDAS commands.

It answers:

- What commands exist?
- What does each command do?
- Where does each command live?
- What aliases are supported?
- Which commands use classification, scoring, metrics, or artifacts?
- Which commands have eval coverage?
- Which commands are planned, draft, active, or deprecated?

This file is not a command skill.

This file is not a global runtime rule.

This file should not contain full command workflows.

Full command behavior belongs in each command’s `SKILL.md`.

---

# Registry Freshness Rule

The command registry must be updated whenever a command is:

- Created
- Renamed
- Deprecated
- Given a new alias
- Moved to a new folder
- Changed to use scoring/classification/metrics
- Changed to create or update artifacts
- Changed in ways that affect `rules/ARTIFACTS.md` compliance
- Given new eval coverage
- Materially changed in purpose or output behavior

Every command skill should include a **Registry Metadata** block.

The registry should mirror those metadata blocks.

If a command exists in `skills/` but is missing from this registry, the registry is stale.

If a command appears in this registry but no matching skill exists, the registry is stale.

---

# Status Labels

Use these statuses:

## Planned

The command is intended but not built yet.

## Draft

The command exists but is not stable.

Usually missing one or more of:

- Complete workflow
- Output file
- Eval coverage
- Artifact behavior
- Registry metadata

## Active

The command is usable and has a defined skill workflow.

Active does not necessarily mean perfect.

## Deprecated

The command should no longer be used.

Deprecated commands should point to the replacement command when possible.

---

# Aliases vs Subcommands

Aliases are alternate top-level triggers for the same command. Subcommands and argument forms (for example `!wl rm` or `!track rm`) are not aliases; they are documented in the command `SKILL.md`.

# Command Categories

Recommended categories:

- Command Menu
- Stock Discovery
- Disclosure Tracking
- Company Research
- Financial Analysis
- Thesis Analysis
- Risk Analysis
- Full Report
- Earnings / Updates
- Watchlist / Artifacts
- System / Utility

---

# Registry Table

| Command | Aliases | Category | Status | Purpose | Skill Path | Output Path | Eval File | Classification | Scoring | Metrics | Artifacts |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `!commands` | None | Command Menu | Active | Show available MIDAS commands and when to use each one. | `skills/stock-analysis/commands/SKILL.md` | `skills/stock-analysis/commands/OUTPUT.md` | `evals/commands.eval.md` | Not used | Not used | Not used | No |
| `!gems` | None | Stock Discovery | Draft | Find and rank underdiscovered research candidates. | `skills/stock-analysis/gems/SKILL.md` | `skills/stock-analysis/gems/OUTPUT.md` | `evals/gems.eval.md` | Required | Required | Optional | Yes |
| `!track` | `!show track` | Disclosure Tracking | Active | Analyze politician or fund-manager disclosures and surface research leads. | `skills/stock-analysis/tracker/SKILL.md` | `skills/stock-analysis/tracker/OUTPUT.md` | `evals/tracker.eval.md` | Required | Optional | Optional | Optional |
| `!research` | `/research`, `research` | Company Research | Active | Produce filing-backed business-model research for a company or ticker, covering monetization, segments, customers, geography, recurrence, pricing power, cyclicality, recent business trends, and key filing-backed risks. | `skills/stock-analysis/research/SKILL.md` | `skills/stock-analysis/research/OUTPUT.md` | `evals/research.eval.md` | Optional | Optional | Optional | Yes |
| `!financials` | None | Financial Analysis | Active | Review financial statements, margins, cash flow, balance sheet, dilution, capital returns, GAAP/non-GAAP quality, source limitations, and metric-quality red flags. | `skills/stock-analysis/financials/SKILL.md` | `skills/stock-analysis/financials/OUTPUT.md` | `evals/financials.eval.md` | Optional | Optional | Required | Yes |
| `!thesis` | `/thesis`, `thesis` | Thesis Analysis | Draft | Build or update a filing-backed long-term investment thesis for a public company, covering thesis pillars, variant view, business and financial evidence, valuation/rerating context, catalysts, monitoring rules, thesis-breaking risks, strongest bear case, and living-thesis update behavior. | `skills/stock-analysis/thesis/SKILL.md` | `skills/stock-analysis/thesis/OUTPUT.md` | `evals/thesis.eval.md` | Optional | Optional | Required | Yes |
| `!risk` | `/risk`, `risk` | Risk Analysis | Draft | Produce filing-backed risk assessments that identify material thesis-breaking risks, warning signs, financial fragility, valuation/rerating risk, bear case, and risk-reduction evidence. | `skills/stock-analysis/risk/SKILL.md` | `skills/stock-analysis/risk/OUTPUT.md` | `evals/risk.eval.md` | Optional | Optional | Required | Yes |
| `!promote` | `/promote` | Full Report | Draft | Promote a ticker's completed research set to the Pathos Library: eligible when `research.md`, `financials.md`, `thesis.md`, and `risk.md` exist and are fresh; synthesizes the handoff packet, registers it via `library/tools/register_packet.py`, and records the promotion in the workspace. Governed by `library/LIBRARY.md`. Replaces the removed `!full`. | `skills/stock-analysis/promote/SKILL.md` | `skills/stock-analysis/promote/OUTPUT.md` | `evals/promote.eval.md` | Required | Required | Optional | Yes |
| `!earnings` | `/earnings`, `earnings review` | Earnings / Updates | Active | Review latest-quarter earnings, guidance, financial changes, thesis impact, risk update, and next-quarter watch metrics. | `skills/stock-analysis/earnings/SKILL.md` | `skills/stock-analysis/earnings/OUTPUT.md` | `evals/earnings.eval.md` | Optional | Not used | Required | Yes |
| `!updates` | None | Earnings / Updates | Active | Summarize recent material company updates and separate material changes from noise. | `skills/stock-analysis/updates/SKILL.md` | `skills/stock-analysis/updates/OUTPUT.md` | `evals/updates.eval.md` | Optional | Not used | Optional | Yes |
| `!wl` | `!watchlist`, `!list` | Watchlist / Artifacts | Active | Manage the persistent MIDAS stock watchlist and run short watchlist update checks. Subcommands (`add`, `rm`, `show`, `updates`) work under any alias and are defined in the SKILL. | `skills/stock-analysis/wl/SKILL.md` | `skills/stock-analysis/wl/OUTPUT.md` | `evals/wl.eval.md` | Not used | Not used | Optional | Yes |
| `!market` | None | System / Utility | Active | Return a compact read-only live market-data snapshot for a ticker with price, market cap when available, change, volume/exchange when available, source, as-of timestamp, and compact limitations; full/debug modes are explicit only; no artifacts, classification, scoring, recommendations, price targets, sizing, or trade advice. | `skills/stock-analysis/market/SKILL.md` | `skills/stock-analysis/market/OUTPUT.md` | `evals/market.eval.md` | Not used | Not used | Optional | No |
| `maintenance` | None | System / Utility | Active | Govern MIDAS profile maintenance: audits, refactors, registry/eval/rule cleanup, staged plans with approval gates, exact-scope edits, and verification. Skill trigger; no `!` command syntax. Edits MIDAS profile files under its maintenance contracts; does not write workspace research artifacts. | `skills/maintenance/SKILL.md` | `skills/maintenance/OUTPUT.md` | `evals/maintenance.eval.md` | Not used | Not used | Not used | No |

---

# Command Metadata Standard

Every command `SKILL.md` should include this metadata block near the top:

```md
## Registry Metadata

Command: `![command]`
Aliases: `[aliases or "None"]`
Category: `[category]`
Status: `Planned / Draft / Active / Deprecated`
Skill Path: `[path to SKILL.md]`
Output Path: `[path to OUTPUT.md or "None"]`
Eval File: `[path to eval file or "Not created yet"]`
Uses Classification: `Required / Optional / Not used`
Uses Scoring: `Required / Optional / Not used`
Uses Metrics: `Required / Optional / Not used`
Writes Artifacts: `Yes / No / Optional`
Primary Global Rules: `[GLOBAL.md, SOURCES.md, OUTPUT.md, ARTIFACTS.md if artifacts are written, etc.]`
```

The registry table should mirror this metadata.

---

# Registry Update Checklist

When creating or changing a command, update:

- Command `SKILL.md`
- Command `OUTPUT.md` if applicable
- Command eval file if applicable
- This registry row
- Any aliases
- Status
- Artifact behavior
- Classification/scoring/metrics usage

If a command is only planned, mark it as `Planned`.

If the skill exists but evals are missing, mark it as `Draft`.

If the command is usable with a defined workflow, mark it as `Active`.

If the command is replaced, mark it as `Deprecated` and name the replacement.

---

# Drift Checks

Before calling the registry current, check:

- Every command listed here has a matching skill path or is clearly marked `Planned`.
- Every built command in `skills/` appears in this registry.
- Every active command has a clear purpose.
- Every active command has a status.
- Every active command lists whether it uses classification, scoring, metrics, or artifacts.
- Every active command lists an eval file or clearly says the eval is not created yet.
- Deprecated commands point to replacements when possible.

If any of these fail, the registry is stale.

---

# Future Automation

Later, MIDAS may add a script that scans command `SKILL.md` metadata blocks and regenerates this registry automatically.

Possible future path:

`scripts/update_command_registry.py`

Until that exists, the registry must be updated manually whenever command metadata changes.

Do not let this registry drift from the actual `skills/` folder.

---

# Relationship to `!commands`

The `!commands` skill should use this registry as the command index.

`!commands` should not invent commands that are not listed here.

`!commands` should not show deprecated commands unless the user asks for deprecated or legacy commands.

When the registry changes, `!commands` output should be reviewed.

---

# Relationship to Evals

Each active command should eventually have an eval file.

Eval files live in:

`evals/`

Command eval status should be reflected in the registry.

A command without eval coverage can still be usable, but should usually remain `Draft` until evals exist.

---

# Relationship to Architecture

This registry should follow the architecture described in:

`docs/ARCHITECTURE.md`

Architecture defines where things belong.

This registry indexes the commands that exist inside that architecture.

Artifact-writing commands should follow `rules/ARTIFACTS.md`, and their `Writes Artifacts` metadata should match the command skill, output contract, and eval file.

---

# Final Rule

The command registry should make command discovery easier.

It should not become a second command system.

Command workflows belong in `skills/`.

The registry is an index, not the command logic.
