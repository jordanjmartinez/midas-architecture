# Command Lifecycle

Use this playbook when creating, refactoring, validating, or activating a MIDAS command.

## Authority Split

Check the command against these layers:

- command `SKILL.md` — routing, workflow, inputs, source needs, artifacts, failure behavior, guardrails
- command `OUTPUT.md` — visible output shape and display contract
- command eval file — regression and behavior checks
- `docs/COMMAND_REGISTRY.md` — command metadata, aliases, status, artifact behavior
- shared `rules/` — cross-command standards

## Workflow

1. Inspect the command folder and registry metadata.
2. Check whether `SKILL.md`, `OUTPUT.md`, and eval coverage exist.
3. Identify drift between routing, output contract, evals, registry, and status.
4. Patch only approved lifecycle stage files.
5. Preserve `Draft` unless the user explicitly approves promotion and validation supports it.
6. Verify status, aliases, artifact behavior, and guardrails only within approved scope.

## Activation Discipline

Do not promote a command as a side effect of cleanup.

Activation requires explicit user approval and evidence that the relevant validation stage passed.

Runtime validation is separate from file-contract cleanup.

## Boundaries

Do not run the stock command unless the user explicitly asks for runtime validation.

Do not create workspace artifacts, mutate watchlists, or call live providers during architecture-only work.

## Pitfalls

- Do not let `SKILL.md` become a monolithic prompt.
- Do not put display-contract details only in evals.
- Do not leave registry metadata stale after approved lifecycle changes.
- Do not treat historical reference files as current command law.
