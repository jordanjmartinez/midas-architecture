# Template Change Discipline

Use this reference during MIDAS maintenance when a proposed stage would patch command templates or scaffolding.

## Core rule

Do not add maintenance-only checks, planning ceremony, or authority-audit blocks to command templates by default.

Templates should stay reusable for command authors. They should not become maintenance brain dumps or second global rulebooks.

Before adding maintenance/authority language to a command template, first assess whether the existing template already covers the behavior. If the change is merely a helpful reminder, explain the benefit and downside to the user and prefer a one-line pointer over a full checklist or policy block.

## Decision process

Before patching templates:

1. Inspect the relevant template files read-only.
2. Check whether existing template language already prevents the failure mode.
3. Prefer no template change when the template already says to:
   - reference global rules,
   - avoid duplicating global rule content,
   - keep command files from becoming second global rulebooks,
   - keep output files from redefining global output standards,
   - test architecture boundaries in evals.
4. If reinforcement is still needed, add the smallest reusable pointer possible.
5. Do not paste the full Contract Authority Check into command scaffolds unless the user explicitly approves that heavier template contract.

## Practical recommendation

For contract-authority work, the default home is maintenance planning:

- `skills/maintenance/PLAN.md` should require the Contract Authority Check for staged maintenance work.
- `rules/CONTRACT_AUTHORITY.md` should own the canonical rule.
- Command templates should usually only contain short anti-duplication language and pointers to global rules.

## Pitfall

Do not assume every useful maintenance check belongs in future command templates. If the check governs the maintainer's workflow rather than the command author's output, keep it in the maintenance skill or maintenance plan contract.