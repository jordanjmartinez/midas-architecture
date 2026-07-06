# MIDAS Schemas

## Purpose

`schemas/` is the authority layer for structured data and artifact shapes, as
defined in `/home/jordan/.hermes/profiles/midas/rules/CONTRACT_AUTHORITY.md`.

Allowed here:

- JSON schemas
- table schemas
- artifact data-shape contracts
- machine-readable output shapes

Not allowed here:

- prose workflow rules (those belong in skills or rules)
- output display templates (command `OUTPUT.md`)
- command intelligence logic (command `contracts/`)

## Conventions

- One shape per file.
- Filenames: `[domain]-[shape].md` for prose-specified shapes, or
  `[domain]-[shape].schema.json` for JSON Schema files.
- Every schema file states which command or data store owns the shape and which
  file consumes it.
- A schema placed here does not change runtime behavior by itself. It becomes
  active only when the owning contract, skill, or rule points to it. Per the
  no-secondary-law rule, schemas describe structure; they do not create policy.

## Known Migration Candidates

Structured shapes currently living in other layers that should migrate here,
each as its own approved change:

- Alpha Queue candidate shape, currently embedded in
  `skills/stock-analysis/tracker/contracts/fund-manager.md` (its Authority
  Boundaries section notes it is held there until this layer hosts it).
- `data/midas_watchlist.json` shape, currently described in
  `skills/stock-analysis/wl/references/`.
- `data/tracker_watchlist.json` roster shape, currently described in
  `skills/stock-analysis/tracker/SKILL.md`.

Migrating a shape means: create the schema file here, point the owning file at
it, and remove the duplicated definition, following the Contract Authority
Check. Do not migrate shapes as a side effect of unrelated edits.
