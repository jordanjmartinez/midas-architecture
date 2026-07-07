# Midas Command Interface Rules

## Purpose

`COMMAND_INTERFACE.md` defines shared command invocation and output-mode resolution behavior for Midas commands.

Its job is to keep command parsing consistent without forcing every command `SKILL.md` to duplicate the same mode-alias and default-mode rules.

This file governs:

- command invocation basics
- command aliases versus mode words
- default output-mode selection
- compact and full mode trigger words
- ticker/company argument handling
- mode-conflict handling
- where command-specific exceptions should live
- eval coverage for shared interface behavior

This file does not define:

- source hierarchy
- metric formulas
- setup classifications
- scoring rubrics
- artifact paths
- command workflows
- report section order
- command-specific output templates
- command-specific research logic

Use those files instead:

- Source standards: `rules/SOURCES.md`
- Metric standards: `rules/METRICS.md`
- Setup classifications: `rules/CLASSIFICATIONS.md`
- Scoring standards: `rules/SCORING.md`
- Output standards: `rules/OUTPUT.md`
- Artifact standards: `rules/ARTIFACTS.md`
- Command workflows: `skills/**/SKILL.md`
- Command-local output contracts: `skills/**/OUTPUT.md`

---

## Relationship to Other Rules

`COMMAND_INTERFACE.md` is a shared rule file.

It sits beside other global Midas rule files and should be referenced from `rules/GLOBAL.md`.

Command-specific skills should inherit this file rather than duplicating it.

Command-specific `OUTPUT.md` files should define output shape, not command parsing doctrine.

If this file conflicts with system/developer/runtime instructions, those higher-priority instructions win.

If this file conflicts with a command-specific exception that is explicitly documented in that command's `SKILL.md` and `OUTPUT.md`, the documented command exception may apply for that command only.

Undocumented exceptions should be treated as drift.

---

## Core Interface Principle

A command should interpret the user's requested target before interpreting output-mode words.

For ticker/company commands, the first ticker/company argument after the command is the security identifier unless the command explicitly defines a different input grammar.

Output mode should be inferred only from explicit mode words or flags outside the target identifier.

Do not infer output mode from:

- ticker text
- company name text
- uppercase words
- market cap
- popularity
- source availability
- filing complexity
- prior examples
- prior outputs
- current workspace artifacts
- command history

---

## Command Aliases vs Mode Words

Command aliases and mode words are different.

### Command aliases

Command aliases are alternate ways to invoke a command.

Examples:

```md
!research
/research
research
```

Command aliases are command-specific and should be declared in that command's `SKILL.md`, registry metadata, and evals.

Do not add command aliases only for uniformity.

### Mode words

Mode words modify the output depth of a command that supports output modes.

Examples:

```md
compact
quick
full
deep
```

Mode words are not command aliases.

Shared mode-word behavior belongs here, not duplicated in every command skill.

---

## Supported Shared Output Modes

Midas research and analysis commands may support three shared output modes:

| Mode | Meaning |
|---|---|
| Compact | Short triage or snapshot output |
| Standard | Default research-quality output |
| Full | Expanded deep-dive output |

Not every command must support all three modes.

Each command's `SKILL.md` and command-local `OUTPUT.md` should declare which modes are supported.

If a command does not support a requested mode, it should use the closest supported mode when safe or explain the unsupported mode briefly.

---

## Default Mode Rule

For Midas research and analysis commands that support output modes, Standard mode is the default.

Plain command usage should therefore use Standard mode unless the user explicitly requests another supported mode.

Examples:

```md
!research TICKER        -> Standard
!financials TICKER     -> Standard
```

Compact mode should not be selected merely because the answer could be short.

Full mode should not be selected merely because the company is complex.

Utility or menu-style commands may define a different default only if that exception is explicit in the command's `SKILL.md` and command-local `OUTPUT.md`.

---

## Compact Mode Trigger Words

Compact mode requires explicit user wording or an explicit command flag outside the target identifier.

Shared compact-mode words include:

```md
compact
quick
brief
short
summary
concise
```

Examples:

```md
!research TICKER compact      -> Compact
!research TICKER quick        -> Compact
!financials TICKER brief      -> Compact
!financials TICKER summary    -> Compact
```

A command may support additional compact-mode words only if documented in that command's `SKILL.md`, command-local `OUTPUT.md`, and evals.

---

## Full Mode Trigger Words

Full mode requires explicit user wording or an explicit command flag outside the target identifier.

Shared full-mode words include:

```md
full
deep
detailed
expanded
deep-dive
deepdive
```

Examples:

```md
!research TICKER full         -> Full
!research TICKER detailed     -> Full
!financials TICKER deep       -> Full
!financials TICKER expanded   -> Full
```

A command may support additional full-mode words only if documented in that command's `SKILL.md`, command-local `OUTPUT.md`, and evals.

---

## Target-Identifier Precedence

For ticker/company commands, the first ticker/company argument after the command should be treated as the target identifier before mode words are evaluated.

Ticker-like words must not be treated as mode selectors when they occupy the target position.

Examples:

```md
!financials NOW       -> Standard mode for ticker/company `NOW`
!financials DEEP      -> Standard mode for ticker/company `DEEP`
!research DEEP        -> Standard mode for ticker/company `DEEP`
!financials DEEP full -> Full mode for ticker/company `DEEP`
!research DEEP quick  -> Compact mode for ticker/company `DEEP`
```

These examples are parser examples only. They are not ticker recommendations and do not create ticker-specific command behavior.

---

## Output Mode Conflict Rule

Midas commands use these broad output modes:

- Standard: default complete command output.
- Compact: short summary / quick triage output.
- Full: expanded report output.

Compact-mode words include:

- `compact`
- `quick`
- `brief`
- `short`
- `summary`
- `concise`

Full-mode words include:

- `full`
- `deep`
- `detailed`
- `expanded`
- `deep-dive`
- `deepdive`

If explicit Compact-mode and Full-mode words both appear in the same command invocation, treat the request as a mode conflict.

Examples:

```md
!risk HOOD full summary
!financials RKLB full brief
!research AAPL deep concise
```

Required behavior:

- Do not silently choose one mode.
- Do not run the command.
- Do not create, update, replace, or append any artifact.
- Do not save `research.md`, `financials.md`, `risk.md`, or any compact artifact.
- Return a clean conflict failure.

Required failure format:

```md
Unable to complete: conflicting output modes.

Reason: `[full-token]` asks for an expanded report, while `[compact-token]` asks for compact output.

Choose one:
- `![command] [ticker] full`
- `![command] [ticker] compact`

No artifact saved.
```

Invariant:

```md
Full mode means expanded report output.
Compact mode is the summary path.
Do not create “full summary” behavior.
If the user asks for both Full and Compact/Summary behavior in the same command, fail with a mode-conflict message.
```

---

## Command Skill Requirements

A command `SKILL.md` should declare only command-specific interface facts:

```md
Aliases: [command aliases or None]
Supported Output Modes: [Compact / Standard / Full / subset]
Default Mode: Standard
Shared Mode Behavior: Inherits `rules/COMMAND_INTERFACE.md`
Command-Specific Mode Exceptions: [None or documented exception]
```

Do not paste the full shared mode-word list into every command `SKILL.md` unless there is a command-specific reason.

Do not let `SKILL.md` become a second global rulebook.

---

## Command Output Contract Requirements

A command-local `OUTPUT.md` should define output shape for each supported mode.

It may state that Standard is the default for that command, but it should not redefine the full shared parser doctrine.

Command-local `OUTPUT.md` files should focus on:

- Compact output structure
- Standard output structure
- Full output structure
- required section order
- source display behavior
- metric display behavior
- score/classification display behavior when applicable
- artifact display wording
- failure output shape

They should not define source-gathering workflows, metric formulas, scoring rubrics, artifact policy, or global command-interface parsing.

---

## Eval Requirements

Commands that support output modes should include eval coverage for shared interface behavior.

Minimum mode-routing evals should test:

- plain command usage selects Standard mode
- explicit compact-mode words select Compact mode
- explicit full-mode words select Full mode
- ticker-like target words are not treated as mode words
- mode conflicts fail clearly
- artifact behavior matches the selected mode

For ticker/company commands, include at least one eval where the target identifier is also an ordinary English word or mode-like word.

Eval examples:

```md
![command] TICKER          -> Standard
![command] TICKER compact  -> Compact
![command] TICKER quick    -> Compact
![command] TICKER full     -> Full
![command] TICKER deep     -> Full
![command] DEEP            -> Standard for target `DEEP`
![command] DEEP full       -> Full for target `DEEP`
```

Evals should test behavior, not copy this file verbatim.

---

## Drift Signals

Treat the following as command-interface drift:

- Plain research/analysis command returns Compact mode without explicit compact wording.
- A ticker-like word in target position is interpreted as a mode.
- Compact output overwrites a Standard/Full canonical artifact by default.
- Full output is selected from company complexity rather than explicit user wording.
- A command skill duplicates the full shared mode doctrine instead of referencing this file.
- A command-local `OUTPUT.md` defines parser behavior instead of output shape.
- Command `SKILL.md`, command-local `OUTPUT.md`, registry metadata, and evals disagree about supported modes or aliases.

---

## Final Rule

`COMMAND_INTERFACE.md` standardizes how Midas interprets command invocation and output modes.

It should make command behavior consistent without taking over command workflows or output templates.
