# Staged Contract Authority Checks

This is an active maintenance playbook. It supports staged MIDAS maintenance work and does not replace `/home/jordan/.hermes/profiles/midas/rules/CONTRACT_AUTHORITY.md` or `skills/maintenance/PLAN.md`.

Use this reference when maintaining MIDAS profile contracts, command templates, or reference-library structure.

Lesson captured from maintenance-contract cleanup:

- Before adding or expanding command-local instructions, perform a Contract Authority Check.
- Put the check in the staged plan, not only in the final report, so rule placement is decided before patching.
- If the behavior is already global, add a short pointer from the local contract instead of duplicating the policy body.
- For maintenance plans, include the check before the approval model so the user approves both scope and authority placement.
- Stop at the approved stage boundary; do not roll template updates, evals, activation, or reference moves into the same stage unless explicitly approved.

Minimal plan-template block:

```md
Contract Authority Check:
- Existing global authority checked: [files]
- Existing command authority checked: [files]
- Proposed new or changed behavior: [summary]
- Applies to: [one command / multiple commands / global]
- Correct home: [rules / SKILL.md / OUTPUT.md / evals / docs / templates / schemas / references / archive]
- Reason: [why]
- Duplication risk: [none / possible / confirmed]
- Action: [point to existing rule / create global rule / create command-local rule / archive / defer]
```
