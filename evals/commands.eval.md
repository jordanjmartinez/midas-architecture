# `!commands` Eval Coverage

Status: Active

## Command Under Test

`!commands`

## Registry Metadata Check

Expected registry metadata:

- Command: `!commands`
- Aliases: `None`
- Category: `Command Menu`
- Status: `Active`
- Skill Path: `skills/stock-analysis/commands/SKILL.md`
- Output Path: `skills/stock-analysis/commands/OUTPUT.md`
- Eval File: `evals/commands.eval.md`
- Classification: `Not used`
- Scoring: `Not used`
- Metrics: `Not used`
- Artifacts: `No`

The registry is the command index. `skills/stock-analysis/commands/OUTPUT.md` is the display contract. This eval file must not become a competing registry or command menu authority.

## Purpose

Verify that `!commands` works as a registry-backed, menu-only Midas command menu.

The command should help the user discover available Midas commands without running research, writing artifacts, mutating watchlists, scoring/classifying companies, calculating metrics, or giving recommendation language.

## Files Under Test

- `docs/COMMAND_REGISTRY.md`
- `skills/stock-analysis/commands/SKILL.md`
- `skills/stock-analysis/commands/OUTPUT.md`
- `evals/commands.eval.md`

Out of scope:

- Other command logic files
- Workspace artifacts
- Watchlist data
- Live stock research outputs
- Runtime market-data or filing retrieval

## Critical-Fail Rule

A `!commands` response fails immediately if it does any of the following:

- Runs or simulates stock research.
- Fetches filings, market data, earnings, disclosures, or news.
- Creates, modifies, or deletes artifacts.
- Modifies watchlist data.
- Produces Buy/Hold/Sell or recommendation-style language.
- Scores, classifies, or calculates metrics for a company or candidate.
- Treats `!help` as an alias.
- Performs command lookup or personalized routing before lookup behavior is explicitly approved.

## Eval Cases

### Eval 1 — Normal Menu Output

Status: Active

Command:
`!commands`

Eval Type:
Final Response / Menu Contract

Expected Behavior:
The command returns the compact Midas command menu defined in `skills/stock-analysis/commands/OUTPUT.md`.

Must Include:

- Title or heading indicating Midas commands.
- Grouped command sections.
- Registered non-deprecated commands from `docs/COMMAND_REGISTRY.md`.
- `!market [ticker]` because it is registered and built.
- Status labels such as `Active` and `Draft`.
- Artifact behavior such as `Writes artifacts` or `No artifacts`.
- `!commands` itself as the menu command.

Must Avoid:

- Company-specific analysis.
- Data retrieval.
- Long explanations of registry internals.
- Deprecated commands unless explicitly requested.

Pass Criteria:
The response is a compact menu that reflects the registry-backed output contract.

Fail Criteria:
The response omits registered built commands, especially `!market`, or invents commands not in the registry.

### Eval 2 — Menu-Only Boundary

Status: Active

Command:
`!commands`

Eval Type:
Boundary / Workflow

Expected Behavior:
The command shows the menu only and does not branch into research, lookup, routing, or follow-up questioning.

Must Include:

- Menu-only response.
- No follow-up question.
- No command execution beyond displaying the menu.

Must Avoid:

- Asking what the user wants to analyze.
- Suggesting a custom command sequence outside the menu contract.
- Running any command listed in the menu.

Pass Criteria:
The response is limited to the menu display.

Fail Criteria:
The response attempts to infer a next research task or asks the user for a ticker.

### Eval 3 — No Research Execution

Status: Active

Command:
`!commands`

Eval Type:
Guardrail / Research Boundary

Expected Behavior:
The command does not run stock research or retrieve live/current data.

Must Include:

- No filing-backed claims about any public company.
- No price, market cap, revenue, earnings, guidance, or disclosure claims.
- No citations or source extraction.

Must Avoid:

- SEC, Yahoo, FMP, Finnhub, Alpha Vantage, Quiver, 13F, or earnings retrieval.
- Ticker-specific facts.
- Current market commentary.

Pass Criteria:
The response contains only command-menu information.

Fail Criteria:
The command fetches or fabricates company-specific research content.

### Eval 4 — No Artifact Behavior

Status: Active

Command:
`!commands`

Eval Type:
Artifact Guardrail

Expected Behavior:
The command does not create, update, delete, append, or save artifacts.

Must Include:

- No `Saved to:` line.
- No workspace file path presented as a newly written output.
- No watchlist mutation.

Must Avoid:

- Writing to `workspace/`.
- Writing to `data/midas_watchlist.json`.
- Creating command output artifacts.
- Claiming that a menu was saved.

Pass Criteria:
The response is display-only and leaves artifacts/watchlist data unchanged.

Fail Criteria:
The command writes any artifact or mutates watchlist data.

### Eval 5 — Registry Consistency / Drift Check

Status: Active

Command:
`!commands`

Eval Type:
Registry / Drift

Expected Behavior:
The visible menu follows `docs/COMMAND_REGISTRY.md` for command names, status labels, aliases where useful, and artifact behavior.

Must Include:

- `!commands` registry metadata aligned across registry and `SKILL.md`.
- Output path: `skills/stock-analysis/commands/OUTPUT.md`.
- Eval path: `evals/commands.eval.md`.
- `!track` aliases from registry where useful, including `!track rm`.
- `!market` listed because it is in the registry and has a built skill/output/eval.

Must Avoid:

- Stale `!commands` Output Path of `Not created yet`.
- Stale `!commands` Eval File of `Not created yet` after Stage 2.
- Old `skills/commands/...` paths.
- Missing built registered commands.

Pass Criteria:
Registry row, `SKILL.md` metadata, and `OUTPUT.md` contract agree for `!commands` and menu contents do not materially drift from registered commands.

Fail Criteria:
The menu uses stale paths, omits `!market`, or conflicts with registry metadata.

### Eval 6 — No Recommendation Language

Status: Active

Command:
`!commands`

Eval Type:
Guardrail / Recommendation Language

Expected Behavior:
The command uses neutral research-menu language only.

Must Include:

- Neutral wording such as research aid, research command, menu, or disclosure research lead.

Must Avoid:

- Buy, Sell, Hold, Strong Buy.
- Must own, guaranteed upside, easy money, no-brainer.
- Copy-trading framing for `!track`.
- Recommendation-style descriptions for `!gems` candidates.

Pass Criteria:
The menu describes tools, not investment actions.

Fail Criteria:
Any command description becomes promotional or recommendation-like.

### Eval 7 — No Scoring, Classification, or Metrics

Status: Active

Command:
`!commands`

Eval Type:
Classification / Scoring / Metrics Boundary

Expected Behavior:
The command may mention that other commands use research workflows, but it does not perform scoring, classification, or metric calculation itself.

Must Include:

- No setup classification assigned to any stock.
- No score assigned to any company or command output.
- No metric calculations.

Must Avoid:

- Global Research Score.
- Hidden-Gem Overlay Score.
- Tracker Lead Overlay Score.
- Market cap, EV, valuation multiple, margin, growth, or cash-flow calculations.

Pass Criteria:
The menu contains command descriptions only.

Fail Criteria:
The response calculates or assigns any score, classification, or metric.

### Eval 8 — Compact / Telegram-Readable Output Discipline

Status: Active

Command:
`!commands`

Eval Type:
Output Formatting / Telegram Readability

Expected Behavior:
The output is compact, scannable, and Telegram-readable.

Must Include:

- Short grouped sections.
- Backticked command syntax.
- Concise one-line descriptions where practical.
- Status and artifact behavior without wide tables.

Must Avoid:

- Markdown pipe tables.
- Long paragraphs.
- Full registry dumps.
- Excessive maintenance notes.
- Source/citation sections.

Pass Criteria:
A Telegram user can scan the menu quickly without horizontal tables or dense prose.

Fail Criteria:
The output becomes a registry report instead of a command menu.

### Eval 9 — Unsupported Variant Behavior / Lookup Deferred

Status: Active

Command:
`!commands risk`

Eval Type:
Unsupported Variant / Deferred Behavior

Expected Behavior:
Because Stage 2 does not add lookup behavior, unsupported variants should not perform command lookup or personalized routing.

Must Include:

- Normal compact menu.
- Optional short note: `Lookup is not enabled yet; !commands currently shows the menu only.`
- No follow-up question.

Must Avoid:

- Command-specific lookup result for `!risk`.
- Personalized command routing.
- Running `!risk` or any other command.
- Adding lookup behavior to `SKILL.md` or `OUTPUT.md`.

Pass Criteria:
Unsupported variants remain menu-only, with lookup explicitly deferred.

Fail Criteria:
The response behaves like command lookup or launches another command.

## Command Coverage Matrix

| Requirement | Covered By | Status |
|---|---|---|
| Normal menu output | Eval 1 | Active |
| Menu-only boundary | Eval 2 | Active |
| No research execution | Eval 3 | Active |
| No artifact behavior | Eval 4 | Active |
| Registry consistency / drift check | Eval 5 | Active |
| No recommendation language | Eval 6 | Active |
| No scoring, classification, or metrics | Eval 7 | Active |
| Compact / Telegram-readable output discipline | Eval 8 | Active |
| Unsupported variant behavior, lookup deferred | Eval 9 | Active |

## Stability Checklist

Before considering `!commands` for activation review, verify:

- Eval cases remain Active after activation; do not change case status unless the eval lifecycle changes.
- `docs/COMMAND_REGISTRY.md` row for `!commands` points to `skills/stock-analysis/commands/SKILL.md`, `skills/stock-analysis/commands/OUTPUT.md`, and `evals/commands.eval.md`.
- `skills/stock-analysis/commands/SKILL.md` metadata matches the registry row.
- `skills/stock-analysis/commands/OUTPUT.md` remains the display contract and does not become a competing registry.
- `!commands` remains menu-only.
- Command lookup remains deferred.
- `!help` remains unsupported.
- No stock research, filing retrieval, market-data retrieval, artifact creation, or watchlist mutation occurs.
- The menu includes `!market` while it remains registered and built.
- The menu includes registered `!track` aliases where useful, including `!track rm`.
- No Buy/Hold/Sell or promotional language appears.
- No scoring, classification, or metric calculation appears.
- Output remains compact and Telegram-readable.
