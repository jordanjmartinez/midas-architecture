# Midas Maintenance Output Contract

Use this output contract when reporting Midas maintenance work, audits, staged changes, verification, or migration status.

Default style:

- concise
- exact-scope
- evidence-backed
- plain English
- no hype
- no unnecessary implementation diary

## Standard Maintenance Report

Use this shape after a completed maintenance task:

```md
Done.

Changed:
- [path] — [what changed]

Inspected:
- [path] — [why inspected]

Verification:
- Files outside scope changed: [yes/no/not verified within scope]
- Commands/evals run: [none/list]
- Workspace artifacts changed: [yes/no/not verified within scope]
- Watchlists/data files changed: [yes/no/not verified within scope]
- Status labels changed: [yes/no]
- Secrets/API keys printed or written: no

Limitations:
- [only if relevant]
```

## Read-Only Audit Report

Use this shape when no edits were requested:

```md
Read-only audit complete.

Findings:
- present — [item]
- missing — [item]
- drift — [item]
- blocked — [item]
- not verified within scope — [item]

Inspected:
- [path]

No files were modified.
```

## Staged Work Report

Use this shape when the user requested one stage of a larger migration:

```md
## Stage [N] Complete — [Name]

Changed:
- [file]: [what changed]

Inspected:
- [file]: [why inspected]

Verified:
- [check]: [result]

Not changed:
- [explicitly excluded file/scope]
- [explicitly excluded file/scope]

Commands/evals run:
- [none / exact command]

Workspace/watchlist/artifacts:
- [none / exact change]

Status changes:
- [none / exact change]

Limitations:
- [anything not verified]

Next proposed stage:
Stage [N+1] — [name]

Awaiting approval:
Approve Stage [N+1] to continue.
```

## Scope Language

Be explicit about scope boundaries.

Say:

- `not in scope`
- `not verified within scope`
- `deferred by design`
- `no stock commands were run`
- `no workspace artifacts were created`

Avoid implying full-profile cleanliness unless actually verified.

## Prohibited Output Drift

Do not present maintenance work as stock research.

Do not include buy/sell/hold language.

Do not claim runtime command validation if only file-contract checks were performed.

Do not claim no unrelated files changed unless that was checked.

Do not include secrets, API keys, or raw credentials.
