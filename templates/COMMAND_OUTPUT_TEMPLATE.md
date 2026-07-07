# COMMAND_OUTPUT_TEMPLATE.md

Template for building command-specific `OUTPUT.md` files in Midas.

Use this when creating a command-specific output contract:

`[path to command OUTPUT.md]`

Examples:

- `skills/commands/OUTPUT.md`
- `skills/stock-analysis/gems/OUTPUT.md`
- `skills/stock-analysis/research/OUTPUT.md`

This template standardizes command output without duplicating global output rules.

---

## Command

Command: `![command]`

Skill File: `[path to command SKILL.md]`

Output File: `[path to command OUTPUT.md]`

Registry Entry: `docs/COMMAND_REGISTRY.md`

Status: `[Draft / Active / Deprecated]`

---

## Registry Consistency

This output contract should match the command’s Registry Metadata block in the command `SKILL.md` and the command row in:

`docs/COMMAND_REGISTRY.md`

Check:

- Command name
- Skill path
- Output path
- Status
- Classification usage
- Scoring usage
- Metrics usage
- Artifact behavior

If this output file says a command uses classification, scoring, metrics, or artifacts, the command `SKILL.md` and `docs/COMMAND_REGISTRY.md` should say the same.

If this output file and the registry disagree, treat that as registry drift.

---

## Purpose

This file defines the command-specific output contract for `![command]`.

It explains:

- What the command should return
- Which output modes it supports
- Which sections are required, optional, or prohibited
- How artifacts, scores, classifications, sources, and failures should appear for this command

This file should not redefine global output standards.

---

## Output / Workflow Boundary

This file defines output shape only.

Workflow steps belong in the command’s `SKILL.md`.

Do not add source-gathering workflow, scoring workflow, research workflow, metric-calculation workflow, or artifact-writing procedure here unless it is strictly about how the result appears in the output.

This file should answer:

- What sections should appear?
- Which sections are required, optional, or prohibited?
- Which output modes are supported?
- How should scores, classifications, metrics, sources, risks, failures, and artifacts be displayed?

This file should not answer:

- How sources are gathered
- How candidates are screened
- How scores are calculated
- How metrics are computed
- How artifacts are written
- How the command routes or executes

---

## Global Output Inheritance

`![command]` must follow the global Midas output rules in:

- `rules/GLOBAL.md`
- `rules/OUTPUT.md`

Depending on command behavior, it may also inherit from:

- `rules/SOURCES.md`
- `rules/CLASSIFICATIONS.md`
- `rules/SCORING.md`
- `rules/METRICS.md`
- `rules/ARTIFACTS.md` when the command writes artifacts

If this file conflicts with a global rule file, the global rule file wins unless the exception is explicitly documented here.

---

## Output Philosophy

`![command]` output should be:

- Useful before it is exhaustive
- Evidence-aware
- Clear about uncertainty
- Compact by default unless the user asks for depth
- Structured enough to scan quickly
- Specific about the next best action

Avoid:

- Hype
- False precision
- Unsupported conviction
- Long generic market commentary
- Repeating global rule language
- Dumping raw data without interpretation

---

## Supported Output Modes

`![command]` supports the following output modes:

| Mode | Supported? | Use Case |
|---|---:|---|
| Compact | `[Yes / No]` | Fast answer, triage, menu, or quick status |
| Standard | `[Yes / No]` | Default research-quality response |
| Full | `[Yes / No]` | Deep-dive output with expanded evidence, risks, and artifacts |

Default mode:

`[Compact / Standard / Full]`

Mode selection should follow `rules/OUTPUT.md`.

## Unsupported Mode Behavior

If the user asks for an unsupported output mode:

- Use the closest supported mode when safe, or
- Explain that the mode is not supported for this command.

Example:

`Full mode is not supported for !commands. Showing compact command menu instead.`

Do not pretend to support an output mode that this command does not support.

---

## Required Top-Level Output Contract

Every successful `![command]` response should include the following sections unless the command is intentionally minimal.

Do not show empty sections.

If a section is not applicable, omit it unless the command contract requires a clear `Not applicable` statement.

Do not leave placeholder text in active command outputs.

### 1. Bottom Line

A brief answer first.

For research commands, this should state the practical conclusion.

For utility commands, this should state what the command did or what the user can do next.

Format:

`Bottom Line: [1-3 sentence conclusion]`

---

### 2. Command Result

The main result of the command.

This section should be renamed when a more specific label improves clarity.

Examples:

- `Command Menu`
- `Research Summary`
- `Candidate List`
- `Tracking Update`
- `Financial Snapshot`
- `Risk Review`
- `Thesis Summary`
- `Earnings Review`

Required content:

`[Define what this command must show here.]`

Optional content:

`[Define what this command may show here.]`

Do not include:

`[Define what this command must never show here.]`

---

### 3. Evidence / Source Notes

Use this section only if the command uses external evidence, filings, market data, company documents, or user-provided documents.

Follow:

- `rules/SOURCES.md`
- `rules/OUTPUT.md`

Required source behavior:

`[Describe command-specific source expectations.]`

Example source note language:

`Evidence base: [primary filings / company materials / market data / secondary context / user-provided material] as of [date].`

If the command does not gather evidence, state:

`This command does not perform source gathering.`

---

### 4. Classification Behavior

Use this section only if the command applies setup classification.

Follow:

- `rules/CLASSIFICATIONS.md`

Classification usage:

`[Required / Optional / Not used]`

If used, output should include:

`Setup Classification: [classification]`

Optional:

`Setup Modifiers: [modifier 1], [modifier 2]`

Command-specific classification notes:

`[Explain any command-specific classification constraints.]`

If classification is not used, state:

`This command does not classify setups.`

---

### 5. Scoring Behavior

Use this section only if the command applies Midas scoring.

Follow:

- `rules/SCORING.md`

Scoring usage:

`[Required / Optional / Not used]`

If used, output should include:

`Global Research Score: [score]/100`

Optional overlay score:

`[Overlay Name]: [score]/25`

Evidence confidence:

`Evidence Confidence: [A / B / C / D]`

Command-specific scoring notes:

`[Explain whether this command produces full scores, preliminary scores, overlay scores, or no score.]`

If scoring is not used, state:

`This command does not score companies or setups.`

---

### 6. Metrics Behavior

Use this section only if the command displays, calculates, compares, or interprets financial metrics.

Follow:

- `rules/METRICS.md`
- `rules/ARTIFACTS.md` when the command writes artifacts

Metrics usage:

`[Required / Optional / Not used]`

Required metrics:

`[List required metrics, or "None"]`

Optional metrics:

`[List optional metrics, or "None"]`

Metric constraints:

`[Describe command-specific metric requirements, such as period, source, GAAP/non-GAAP handling, or freshness.]`

If metrics are not used, state:

`This command does not calculate or interpret financial metrics.`

---

### 7. Risks / Caveats

Use this section when the command could influence investment judgment.

Required risk behavior:

`[Define minimum risks or caveats this command must include.]`

For research commands, include at least:

- Key downside risk
- Evidence limitation
- What could disconfirm the setup

For utility-only commands, this section may be omitted.

---

### 8. Best Next Command

When useful, end with the next most logical Midas command.

Format:

`Best next command: ![command] [reason]`

Examples:

- `Best next command: !research to build a full company view.`
- `Best next command: !financials to verify valuation and cash conversion.`
- `Best next command: !risk to pressure-test the thesis.`
- `Best next command: !track to add this company to the watchlist.`

Do not recommend a next command when it would be noisy or unnecessary.

---

## Compact Output Contract

Use compact mode when the user wants speed, navigation, triage, or a short answer.

Compact output should include:

1. `Bottom Line`
2. `[Primary compact section for this command]`
3. `Best Next Command`, if useful

Compact output should not include:

- Full scoring detail
- Long source discussion
- Full metric tables
- Expanded thesis/risk sections
- Large artifact summaries

Command-specific compact structure:

### Compact Format

`Bottom Line: [short result]`

`[Section Name]: [compact content]`

`Best next command: [optional]`

---

## Standard Output Contract

Use standard mode as the default for most research and workflow commands.

Standard output should include:

1. `Bottom Line`
2. Main command result
3. Evidence/source note, if applicable
4. Classification, if applicable
5. Score, if applicable
6. Key risks or caveats, if applicable
7. Best next command, if useful

Command-specific standard structure:

### Standard Format

#### Bottom Line

`[1-3 sentence conclusion]`

#### [Main Section Name]

`[Primary command output]`

#### Evidence Notes

`[Sources, freshness, evidence quality, or "Not applicable"]`

#### Classification

`[Required only if used]`

#### Scores

`[Required only if used]`

#### Risks / Caveats

`[Required when investment judgment is involved]`

#### Best Next Command

`[Optional]`

---

## Full Output Contract

Use full mode when the user asks for a deep dive, complete artifact, full research view, or detailed audit trail.

Full output may include:

1. `Bottom Line`
2. Main command result
3. Expanded evidence base
4. Classification and modifiers
5. Full scoring detail
6. Relevant metrics
7. Risks and disconfirming evidence
8. Open questions
9. Artifact path, if written
10. Best next command

Command-specific full structure:

### Full Format

#### Bottom Line

`[Clear conclusion]`

#### [Main Section Name]

`[Expanded command result]`

#### Evidence Base

`[Primary sources, secondary context, freshness, conflicts, missing evidence]`

#### Setup Classification

`[Classification and modifiers, if used]`

#### Scoring

`[Global score, overlay score, evidence confidence, score caps/gates, if used]`

#### Metrics

`[Relevant metrics, formulas, periods, source notes, if used]`

#### Risks and Disconfirming Evidence

`[Key risks, what would break the thesis, what needs verification]`

#### Open Questions

`[Unresolved research items]`

#### Artifact

`[Artifact path or "No artifact written"]`

#### Best Next Command

`[Optional]`

---

## Artifact Behavior

Artifact display and failure behavior should follow:

`rules/ARTIFACTS.md`

Writes artifacts:

`[Yes / No / Optional]`

Default artifact behavior:

`[Describe whether artifacts are written automatically, only on request, or never.]`

Artifact location:

`[command-specific workspace path]`

Examples:

- `workspace/tickers/[TICKER]/research.md`
- `workspace/tickers/[TICKER]/financials.md`
- `workspace/tickers/[TICKER]/risk.md`
- `workspace/trackers/[tracker-name].md`
- `workspace/watchlists/[watchlist-name].md`
- `workspace/reports/[report-name].md`

Artifact types:

`[Markdown / CSV / JSON / tracker entry / research note / other]`

When an artifact is written, output should include:

`Artifact: [path]`

When no artifact is written, output should either omit the artifact section or state:

`No artifact written.`

Do not claim an artifact was written unless it was actually created.

Do not duplicate the full artifact policy here; define only command-specific output behavior.

---

## Failure Output Contract

Use failure output when the command cannot complete its intended task.

Common failure cases:

- Missing ticker/company/input
- Insufficient source evidence
- Conflicting evidence
- Unsupported command mode
- Data too stale
- Metric cannot be calculated
- No matching companies or candidates found
- Artifact write failure

Failure output should include:

1. What failed
2. Why it failed
3. What evidence or input is missing
4. Best next step

Failure format:

### Failure Format

`Unable to complete: [specific failure]`

`Reason: [clear explanation]`

`Missing or needed: [input/evidence/data]`

`Best next step: [command or user action]`

Do not fabricate results to avoid a failure state.

---

## Command-Specific Required Sections

The following sections are required for `![command]`:

- `[Section 1]`
- `[Section 2]`
- `[Section 3]`

The following sections are optional:

- `[Section 1]`
- `[Section 2]`
- `[Section 3]`

The following sections are prohibited:

- `[Section 1]`
- `[Section 2]`
- `[Section 3]`

---

## Command-Specific Table Standards

Use tables only when they improve scanability.

Required tables:

`[List required tables, or "None"]`

Optional tables:

`[List optional tables, or "None"]`

Table rules:

- Keep tables compact
- Do not include decorative columns
- Do not show unavailable metrics as if known
- Use `N/A` only when the reason is obvious or explained
- Include period/date context when metrics are shown

---

## Command-Specific Language Standards

Preferred language:

`[Define tone or phrasing specific to this command.]`

Avoid:

`[Define phrases, claims, or behaviors to avoid.]`

Required disclaimers or caveats:

`[Only include if truly command-specific. Do not duplicate global disclaimers.]`

---

## Examples Needed

Each command-specific `OUTPUT.md` should eventually include or reference examples for:

- Normal success case
- Weak or incomplete evidence case
- Failure case
- Artifact-writing case, if applicable

Example coverage may live in the command eval file instead of this file.

Eval file:

`evals/[command].eval.md`

The eval file should test that this output contract is followed.

---

## Placeholder Cleanup Rule

Before a command-specific `OUTPUT.md` is marked Active, all template placeholders should be replaced or removed.

Do not leave unresolved placeholders such as:

- `[Define what this command must show here.]`
- `[Section 1]`
- `[Yes / No]`
- `[Required / Optional / Not used]`
- `[command-specific workspace path]`

A Draft output file may contain placeholders.

An Active output file should not.

---

## Stability Checklist

Before marking this output contract Active, confirm:

- [ ] It references global output rules instead of duplicating them
- [ ] It defines compact, standard, and/or full output behavior
- [ ] It clearly states whether classification is used
- [ ] It clearly states whether scoring is used
- [ ] It clearly states whether metrics are used
- [ ] It clearly states whether artifacts are written
- [ ] It defines failure behavior
- [ ] It avoids command workflow instructions that belong in `SKILL.md`
- [ ] It avoids source hierarchy rules that belong in `rules/SOURCES.md`
- [ ] It avoids scoring rubric details that belong in `rules/SCORING.md`
- [ ] It avoids metric formulas that belong in `rules/METRICS.md`
- [ ] Skill and output paths are command-specific, not generic `skills/[command]/...` placeholders
- [ ] Registry metadata matches `docs/COMMAND_REGISTRY.md`
- [ ] Unsupported output mode behavior is defined
- [ ] Empty sections are omitted unless explicitly required
- [ ] Artifact paths use command-specific workspace paths, not generic placeholders
- [ ] All template placeholders have been replaced or removed before marking Active
- [ ] This file defines output shape only and does not duplicate command workflow logic
- [ ] It is concise enough to serve as an interface contract
