# Skill Library Curation Playbook

Use this when maintaining Midas skills after a session or after restructuring a maintenance skill.

## Core rule

Midas skills should be class-level operating contracts, not session logs. Preserve lessons, but do not promote every patch note, regression, activation, or incident into active routing law.

When the user explicitly constrains available tools for a skill-library review, obey that constraint first. If only memory and skill-management tools are allowed, do not inspect the filesystem, run commands, or verify with unrelated tools; use `skill_view`, `skills_list`, `skill_manage`, and memory only.

## Update preference order

1. Patch the skill that was loaded or governed the work.
2. If that skill is protected or not the right class, patch an existing umbrella skill.
3. Add a concise support file under `references/`, `templates/`, or `scripts/` only when the detail is reusable.
4. Create a new skill only for a durable class of work, never for one incident, PR, feature codename, error string, or today's audit.

## Active vs archive distinction

Active references are reusable operating playbooks:
- repeatable maintenance procedures
- verification/eval recipes
- routing rules that should affect future behavior
- durable pitfalls and constraints

Archive references are retained context, not active instructions:
- one-off patch records
- staged migration notes
- historical incidents
- implementation transcripts
- regression records that no longer describe current behavior

If a historical note still matters, extract the reusable rule into an active playbook and leave the original in archive.

## Maintenance skill hygiene

- Keep `SKILL.md` compact and rich enough to route the class of work.
- Put durable procedure in `MAINTENANCE.md` and user-facing/reporting expectations in `OUTPUT.md`.
- Keep `references/README.md` as the manifest that explains active vs archive.
- Do not bulk-link old reference folders after a migration.
- Do not recreate deleted legacy maintenance skill trees just because historical references once existed.

## Review checklist

Before finishing a maintenance-skill update, verify:
- the skill remains class-level rather than incident-level
- active references are small and reusable
- archive files are not linked as mandatory instructions
- stale legacy paths are marked deprecated or absent
- evals/contracts match the post-migration architecture
