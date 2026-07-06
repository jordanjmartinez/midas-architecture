# !thesis Update Workflow Support

This is command-local support for !thesis. It does not replace GLOBAL.md, SOURCES.md, METRICS.md, OUTPUT.md, ARTIFACTS.md, CLASSIFICATIONS.md, SCORING.md, or RERATING.md.

## Purpose

Use this reference to keep `!thesis update` clearly scoped as a living-thesis refresh, not an output mode or separate artifact workflow.

SKILL.md owns parser and workflow behavior. OUTPUT.md owns the visible update template and section order. ARTIFACTS.md owns global artifact standards.

## Update is a subcommand

`!thesis update [ticker]` is a subcommand / living-thesis workflow.

It is not:

- an output depth,
- Compact mode,
- Full mode,
- Deep mode,
- a changelog-only response,
- a separate update artifact workflow.

## Baseline requirement

Before gathering update evidence, load the existing living thesis read-only from:

`workspace/tickers/[ticker]/thesis.md`

If it does not exist, stop and say exactly:

```md
No baseline thesis exists yet for [ticker]. Run !thesis [ticker] first.
```

Do not create a baseline thesis during update mode unless the user changes the command to normal `!thesis [ticker]`.

## Update comparison discipline

Compare new evidence against the prior living thesis.

Separate:

- old thesis,
- new evidence,
- interpretation,
- unproven assumptions.

Review prior thesis pillars, catalysts, monitoring points, risks, thesis breakers, and prior source basis when available.

## Local update labels

Overall update direction uses one local workflow label:

- `Strengthened`
- `Mostly Unchanged`
- `Weakened`
- `Under Review`
- `Broken`

Each thesis pillar may use one local workflow label:

- `Strengthened`
- `Unchanged`
- `Weakened`
- `Not Yet Testable`
- `Broken`

These are local update workflow labels only. They are not Setup Classifications and must not become a second global classification system.

## Save behavior

After the refreshed thesis is complete and validated, update overwrites only:

`workspace/tickers/[ticker]/thesis.md`

Do not create:

- a new baseline when the baseline is missing,
- `thesis-update.md`,
- timestamped history by default,
- version files unless explicitly requested,
- a second thesis artifact,
- source manifests,
- evidence ledgers,
- proof packets,
- schemas,
- fixture files.

Saved-path confirmation appears only after successful write verification.

## Update audit no-write boundary

`!thesis update [ticker] -audit` reads the baseline thesis status and update readiness without writing anything.

If no baseline exists, it must not create one. It should include the no-baseline message and write nothing.
