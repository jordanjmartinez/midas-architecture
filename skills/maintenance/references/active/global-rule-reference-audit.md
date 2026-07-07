# Global Rule Reference Audit Playbook

Use this when the user asks for a read-only audit of Midas global rules, rule references, pointer accuracy, bloat, or spiderweb risk.

## Purpose

Map whether global rule files are referenced accurately and whether any rule, template, doc, eval, command skill, or reference file has become a hidden secondary rulebook.

## Read-only audit steps

1. Confirm the task is read-only unless the user explicitly approves patches.
2. Inventory `rules/*.md` and note each rule's role, size, and apparent authority layer.
3. Scan references across `AGENTS.md`, `SOUL.md`, `rules/`, `skills/`, `templates/`, `docs/`, `evals/`, and `schemas/`.
4. Separate reference volume from reference quality:
   - high reference count can be healthy for true global standards such as output, sources, metrics, or artifacts;
   - spiderweb risk appears when many files restate policy bodies, point to stale moved files, or create command-local secondary law.
5. Check command metadata for `Primary Global Rules` consistency, but do not force every command to inherit every global rule.
6. Check maintenance references for the active/archive boundary. Root-level or broadly linked references should be classified as active playbooks or archived context.
7. Report findings with prioritized cleanup stages, not opportunistic edits.

## What to flag

- Broken or nonexistent rule references.
- Stale sample deferral notices that enumerate old rule sets instead of pointing to the current shared rule library.
- Command skills missing relevant runtime global rules, especially `COMMAND_INTERFACE.md` for bang-command parsing and `ARTIFACTS.md` for artifact-writing commands.
- Global rules that contain historical migration detail better reduced to a short active pointer.
- Templates or docs that duplicate policy bodies rather than pointing to authoritative rule files.
- Maintenance references linked as active law even though they are session-specific historical notes.

## What not to do

- Do not add `CONTRACT_AUTHORITY.md` to every command's runtime `Primary Global Rules`; it governs maintenance/editing authority, not normal stock-command execution.
- Do not split large global rules solely because they are large. `OUTPUT.md`, `ARTIFACTS.md`, and `METRICS.md` may be large because they legitimately own cross-command standards.
- Do not patch during a read-only audit. Provide staged recommendations and wait for approval.

## Report shape

Include:

- scope inspected;
- global rule inventory;
- high-level bottom line;
- reference-count summary by rule;
- specific stale/broken/bloated pointer findings with file paths;
- prioritized next stages;
- explicit statement that no files were modified.
