# Exact-Scope Edits

Use this playbook when the user approves specific Midas maintenance edits or gives exact target files.

## Principle

Patch only what was approved. Do not convert a narrow edit into a nearby cleanup pass.

## Steps

1. Confirm the requested scope and target files.
2. Inspect each target file before editing.
3. Identify the smallest coherent change.
4. Patch only approved files.
5. Avoid adjacent cleanups unless required for the requested edit to work.
6. Verify the changed files directly.
7. Report changed files, inspected files, and explicit non-actions.

## Boundaries

Do not modify unless explicitly in scope:

- command behavior
- eval status
- registry status
- workspace artifacts
- watchlists or data files
- unrelated command contracts
- old interrupted work from a prior scope

## Verification

Report:

- files changed
- files inspected
- whether files outside scope changed
- whether commands/evals were run
- whether workspace artifacts changed
- whether watchlists/data files changed
- whether status labels changed
- whether secrets/API keys were printed or written

## Pitfalls

- Do not broaden scope because nearby files look related.
- Do not duplicate shared rules into command-local files.
- Do not claim full-profile cleanliness unless checked.
- Do not run stock commands as a shortcut for contract verification.
