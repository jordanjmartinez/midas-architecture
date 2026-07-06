# Eval Maintenance

Use this playbook when creating, editing, reviewing, or activating MIDAS eval files.

## Purpose

Evals protect command contracts from regressions. They should test behavior, output expectations, artifact behavior, status discipline, and guardrails without becoming the only place a rule exists.

## Workflow

1. Inspect the in-scope command `SKILL.md`, `OUTPUT.md`, and registry metadata.
2. Identify the behavior or contract the eval should protect.
3. Add or patch only the approved eval file.
4. Use fixture/mock validation when the task does not require live data.
5. Keep eval status aligned with the command lifecycle stage.
6. Add manual run log entries only when an actual approved run occurred.
7. Verify the eval references current command names, aliases, paths, and status language.

## Coverage Targets

As applicable, cover:

- normal output
- compact/standard/full mode differences
- failure behavior
- artifact behavior
- watchlist/data mutation boundaries
- source or provider limits
- guardrails and prohibited language
- registry/status drift

## Boundaries

Do not activate evals unless explicitly approved.

Do not run live stock commands unless runtime validation is in scope.

Do not create workspace artifacts or mutate watchlists while doing fixture-only eval work.

## Pitfalls

- Do not add eval assertions for stale output templates.
- Do not use evals to introduce new behavior not present in SKILL/OUTPUT/rules.
- Do not mark coverage Active without validation evidence.
- Do not confuse fixture validation with live runtime validation.
