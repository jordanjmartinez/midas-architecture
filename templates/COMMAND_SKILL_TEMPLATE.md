# MIDAS Command Skill Template

## Command

`![command]`

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

## Purpose

[One short paragraph explaining what this command does.]

This section should answer:

- What problem does this command solve?
- What kind of research workflow does it support?
- What should the user expect from it?

Keep this concise.

Do not include global philosophy here.

---

## When To Use

Use this command when:

- [condition]
- [condition]
- [condition]

Do not use this command when:

- [condition]
- [condition]
- [condition]

If another command is better for a situation, name it.

Example:

```md
Do not use this command for a full company report. Use `!full` instead.
```

---

## Inputs

### Required Inputs

- [ticker / company / person / theme / filing / date range / other]

### Optional Inputs

- [time period]
- [output depth]
- [source preference]
- [watchlist behavior]
- [artifact behavior]
- [comparison target]
- [theme]
- [other]

### Input Clarification Rules

Ask for clarification only when missing information would materially change the result.

If the request is clear enough to proceed, proceed.

If a ticker/company/person is ambiguous, clarify or make the ambiguity explicit.

---

## Aliases

Supported aliases:

- `![alias]`
- `![alias]`

If there are no aliases, write:

```md
No aliases currently defined.
```

---

## Global Rules

This command must follow:

- `/home/jordan/.hermes/profiles/midas/rules/GLOBAL.md`
- `/home/jordan/.hermes/profiles/midas/rules/SOURCES.md`
- `/home/jordan/.hermes/profiles/midas/rules/OUTPUT.md`

Use when applicable:

- `/home/jordan/.hermes/profiles/midas/rules/CLASSIFICATIONS.md`
- `/home/jordan/.hermes/profiles/midas/rules/SCORING.md`
- `/home/jordan/.hermes/profiles/midas/rules/METRICS.md`
- `/home/jordan/.hermes/profiles/midas/rules/ARTIFACTS.md` when this command writes artifacts

Do not duplicate global rule content inside this command.

Reference global rules instead.

Before adding behavior that may apply beyond this command, check `/home/jordan/.hermes/profiles/midas/rules/CONTRACT_AUTHORITY.md`. Command skills should define command-specific deltas, not hidden global law.

---

## Workflow

Follow this command-specific workflow:

1. Parse the user request.
2. Identify the target entity or topic.
3. Determine whether the command has enough input to proceed.
4. Gather required evidence using the source standards.
5. Apply the command-specific analysis.
6. Use metrics if appropriate.
7. Apply Setup Classification if appropriate.
8. Apply scoring if appropriate.
9. Identify material risks, limitations, or disconfirming evidence.
10. Produce the output using shared and command-specific output standards.
11. Create, update, append, or skip artifacts according to this command’s artifact rules and `/home/jordan/.hermes/profiles/midas/rules/ARTIFACTS.md`.
12. Suggest the best next command only when useful.

Keep the workflow specific to this command.

Do not turn this section into a copy of global rules.

---

## Command-Specific Source Needs

Default source standards come from:

`/home/jordan/.hermes/profiles/midas/rules/SOURCES.md`

Command-specific source needs:

- [source/tool need]
- [source/tool need]
- [source/tool need]

Examples:

```md
For `!track`, use the latest relevant disclosure first and compare against the prior disclosure when possible.
```

```md
For `!financials`, use filings, earnings releases, and company financial tables before secondary sources.
```

If this command has no special source needs beyond `SOURCES.md`, write:

```md
No command-specific source needs beyond the global source standards.
```

---

## Classification / Scoring / Metrics Behavior

### Setup Classification

Use Setup Classification:

- Required / Optional / Not used

Rule:

```md
Use `/home/jordan/.hermes/profiles/midas/rules/CLASSIFICATIONS.md`.
```

Command-specific classification notes:

- [note]
- [note]

### Scoring

Use scoring:

- Required / Optional / Not used

Rule:

```md
Use `/home/jordan/.hermes/profiles/midas/rules/SCORING.md`.
```

Command-specific scoring notes:

- [note]
- [note]

### Metrics

Use financial metrics:

- Required / Optional / Not used

Rule:

```md
Use `/home/jordan/.hermes/profiles/midas/rules/METRICS.md`.
```

Command-specific metric notes:

- [note]
- [note]

---

## Output Contract

Follow the shared output standards:

`/home/jordan/.hermes/profiles/midas/rules/OUTPUT.md`

### Required Sections

- Bottom Line
- [section]
- [section]
- [section]

### Optional Sections

- Setup Classification
- Setup Modifiers
- Score
- Evidence Confidence
- Source Note
- Key Risk
- What Would Change the View
- Best Next Command
- Artifact Path

### Output Depth

Default output depth:

- Compact / Standard / Full

Use compact output unless the command or user request requires more detail.

Do not create giant reports for commands that are meant to be quick.

---

## Artifact Behavior

If this command writes artifacts, follow:

`/home/jordan/.hermes/profiles/midas/rules/ARTIFACTS.md`

This command writes artifacts:

- Yes / No / Optional

### Creates

- [path or none]

### Updates

- [path or none]

### Appends

- [path or none]

### Replace Behavior

- [replace rule]

### Artifact Rules

- Define command-specific artifact behavior here.
- Do not duplicate the full global artifact policy.
- Use canonical paths from `/home/jordan/.hermes/profiles/midas/rules/ARTIFACTS.md`.
- If no artifact is written, do not pretend one was created.

If this command does not write artifacts by default, write:

```md
This command does not write artifacts by default.
```

---

## Failure Behavior

If information is missing, weak, stale, or unavailable:

- Say what is missing.
- State the limitation clearly.
- Do not invent facts.
- Do not invent numbers.
- Do not force a conclusion.
- Provide the best partial result when possible.
- Suggest the best next diligence step when useful.

Useful phrases:

```md
Could not verify:
```

```md
Missing information:
```

```md
Source limitation:
```

```md
Partial result:
```

```md
Best next step:
```

---

## Guardrails

This command must not:

- Use Buy/Hold/Sell recommendation language.
- Treat tracked ownership or disclosures as copy-trading signals.
- Treat social media as thesis proof.
- Present unverified claims as facts.
- Hide material risks.
- Invent metrics or unsupported precision.
- Ignore stale data.
- Ignore source limitations.
- Overwrite important files unless the command explicitly requires it.
- Duplicate global rules inside this skill.

Command-specific guardrails:

- [guardrail]
- [guardrail]

---

## Eval Cases Needed

Every major command should eventually have evals.

At minimum, create evals for:

1. Normal success case
2. Weak or missing evidence case
3. Guardrail case

Additional useful evals:

- Ambiguous input case
- Stale data case
- Overextended/rerated setup case
- High-fragility setup case
- Raw-data-only output case
- Artifact creation/update case
- Source conflict case

Eval files should live in:

```bash
/home/jordan/.hermes/profiles/midas/evals/
```

---

## Stability Checklist

Before this command is considered stable, confirm:

- Purpose is clear.
- Trigger syntax is clear.
- Required inputs are clear.
- Workflow is command-specific.
- Global rules are referenced, not duplicated.
- Output contract is defined.
- Artifact behavior is defined.
- Failure behavior is defined.
- Guardrails are included.
- Evals exist or are planned.
- Command registry metadata is filled in.
- `docs/COMMAND_REGISTRY.md` is updated when the command is created, renamed, deprecated, or materially changed.
- The command does not conflict with other commands.

## Final Rule

A command skill should be an interface contract.

It should define what the command does and how it behaves.

It should not become a second global rulebook.
