# Contract Authority Placement Notes

Archived historical note. This file preserves context from a prior maintenance cleanup and is not active routing law. The reusable template-change lesson is handled by `references/active/template-change-discipline.md`; the canonical authority rule lives in `/home/jordan/.hermes/profiles/midas/rules/CONTRACT_AUTHORITY.md`.

Use this reference for MIDAS maintenance work that could add, move, expand, or deduplicate rules, command contracts, output contracts, templates, docs, eval requirements, or references.

## Session lesson

When tightening MIDAS maintenance architecture, avoid turning every downstream template into a copy of the global authority rule.

Prefer this layering:

1. `rules/CONTRACT_AUTHORITY.md` owns the canonical rule and required check.
2. `skills/maintenance/PLAN.md` carries the full Contract Authority Check in staged maintenance planning.
3. `skills/maintenance/MAINTENANCE.md` carries only a short pointer to the global rule.
4. `AGENTS.md` may include a conditional read-order pointer so agents see the rule before broad MIDAS edits.
5. Command templates should receive at most a short pointer when the risk is command-local secondary law; do not paste the full check into every template.

## Decision pattern

Before patching templates or command files, ask whether the proposed language adds necessary guidance or just ceremony.

- If the behavior is already enforced by the maintenance plan, skip downstream duplication.
- If command authors need a local reminder, add one short sentence near the relevant section.
- If the issue applies to all MIDAS maintenance, prefer `AGENTS.md` or `rules/` over command templates.

## Preferred wording for command skill templates

Use a short pointer such as:

```md
Before adding behavior that may apply beyond this command, check `/home/jordan/.hermes/profiles/midas/rules/CONTRACT_AUTHORITY.md`. Command skills should define command-specific deltas, not hidden global law.
```

Do not add the full Contract Authority Check block to command templates unless repeated drift proves it necessary.
