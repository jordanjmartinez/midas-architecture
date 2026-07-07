# MIDAS Agent Guide

## Purpose

MIDAS is a financial research agent for public-company research, tracking, classification, scoring, and research artifact management.

This file is the first file an AI/coding agent should read before modifying MIDAS.

## Read Order

Before editing commands or behavior, read:

1. `rules/GLOBAL.md` first. Its Shared Rule Library section is the canonical index of all shared rule files.
2. Every rule file listed in that index, prioritizing the ones relevant to the edit.
3. `rules/CONTRACT_AUTHORITY.md` in full when adding, moving, expanding, or deduplicating rules, contracts, references, templates, docs, eval requirements, or command-local instructions

When editing a specific command, also read that command’s skill folder.

## Folder Map
All paths are relative to the MIDAS profile root.

- `rules/` = shared MIDAS-wide standards
- `skills/` = command-specific workflows
- `templates/` = reusable templates for building commands
- `docs/` = architecture, command registry, build plans
- `evals/` = regression tests and golden examples
- `schemas/` = artifact and data-shape conventions
- `workspace/` = generated research artifacts

## Editing Principles

- Do not duplicate global rules inside command skills.
- Skills should reference global rules.
- Keep command workflows inside `skills/`.
- Keep shared standards inside `rules/`.
- Use templates when creating new commands.
- Do not overwrite important files unless the user requested replacement.
- Prefer clean replacement over appending duplicate versions.
- Summarize changes after editing.

## Command-Building Process

When creating or upgrading a command:

1. Define the command purpose.
2. Define trigger syntax and aliases.
3. Define required inputs.
4. Define workflow steps.
5. Define sources/tools needed.
6. Define output shape.
7. Define artifacts created or updated.
8. Define failure behavior.
9. Add eval examples.
10. Check the command against global rules.

## Safety and Research Guardrails

MIDAS must follow:

- No Buy/Hold/Sell recommendation language
- No copy-trading framing
- Filing-first evidence discipline
- Source freshness and as-of-date discipline
- Setup Classification rules
- Scoring rules
- Metric-definition rules
- Concise output rules
- File/artifact discipline

## Final Rule

When modifying MIDAS, preserve architecture first.

A command should be useful, testable, source-aware, and easy to maintain.
