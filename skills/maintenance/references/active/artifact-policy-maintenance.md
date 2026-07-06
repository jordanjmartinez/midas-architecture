# Artifact Policy Maintenance

Use this playbook when maintaining MIDAS artifact standards, workspace conventions, save-path rules, or artifact-related command behavior.

## Authority Split

- `rules/ARTIFACTS.md` — shared artifact policy and workspace conventions
- command `SKILL.md` — command-specific artifact workflow
- command `OUTPUT.md` — displayed save-path and artifact reporting shape
- evals — regression coverage for artifact behavior
- `workspace/` — generated artifacts, not policy

## Workflow

1. Inspect the in-scope artifact policy or command files.
2. Decide whether the behavior is shared or command-specific.
3. Put shared behavior in `rules/ARTIFACTS.md`.
4. Put command-specific workflow in command `SKILL.md`.
5. Put visible artifact reporting shape in command `OUTPUT.md`.
6. Patch evals only if eval maintenance is in scope.
7. Verify no generated research artifacts were created unless explicitly requested.

## Boundaries

Do not write under `workspace/tickers/` during maintenance unless artifact generation is explicitly in scope.

Do not mutate watchlists or data files while changing artifact policy.

Do not run stock commands just to test save-path wording unless runtime validation is approved.

## Verification

Report whether workspace artifacts changed.

If no workspace check was allowed, say `not verified within scope` instead of implying cleanliness.

## Pitfalls

- Do not put global artifact policy inside one command folder.
- Do not duplicate `rules/ARTIFACTS.md` into command contracts.
- Do not save artifacts before validating output shape when the policy requires pre-save validation.
- Do not expose internal workspace-state details in user-facing reasons unless the output contract requires it.
