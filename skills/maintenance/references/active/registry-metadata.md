# Registry Metadata

Use this playbook when maintaining `docs/COMMAND_REGISTRY.md` or command-local registry metadata blocks.

## Purpose

Registry metadata should describe command availability, aliases, status, artifact behavior, output contract presence, and eval coverage without redefining the command.

## Checks

For each in-scope command, compare:

- command folder exists
- `SKILL.md` status/metadata
- `OUTPUT.md` presence and status language
- eval file presence and status language
- aliases and trigger syntax
- artifact behavior
- guardrails and command category
- `docs/COMMAND_REGISTRY.md` row or section

## Patch Rules

1. Inspect the registry and command-local metadata before editing.
2. Normalize only the approved rows/blocks.
3. Preserve `Draft` unless activation is explicitly approved.
4. Mark missing files honestly, e.g. `Not created yet`.
5. Do not create missing command files unless that is in scope.
6. Do not change command behavior through registry wording.

## Verification

Report whether registry metadata matches the in-scope command files.

If the profile is dirty, distinguish current registry changes from unrelated existing dirt.

## Pitfalls

- Do not use the registry as the source of detailed workflow law.
- Do not hide behavior changes in registry copy.
- Do not promote status labels during metadata cleanup.
- Do not inspect every command if the user requested one command or one row.
