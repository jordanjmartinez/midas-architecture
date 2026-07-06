# MIDAS Global Artifact Eval

## Purpose

This eval file protects shared artifact behavior governed by `/home/jordan/.hermes/profiles/midas/rules/ARTIFACTS.md`.

It is command-agnostic. Command-specific eval files should still test their own artifact paths, output sections, validation gates, and source-preservation requirements.

---

## artifact-global-save-order-001 — Validate Before First Artifact Write

Type: `Artifact / Regression`
Priority: `P0`
Status: `Draft`
Mode: `Command-generated artifact`

### Purpose

Verify that any MIDAS command that generates a research artifact validates the complete draft before the first artifact write, rather than saving an invalid artifact and patching it afterward as cleanup.

### User Input

`![artifact-writing-command] [ticker/company]`

### Context / Fixtures

Use any command-generated Markdown artifact fixture where the first draft contains validation failures such as missing required sections, prohibited language, incorrect path, mixed labels, source omissions, or saved-path confirmation placement errors.

### Expected Behavior

The command should draft internally, run required command-specific validation, revise the draft before saving if validation fails, save only after validation passes, verify the saved path/content, and show the saved-path confirmation only after a successful write.

### Must Include

- Complete internal artifact draft before first write.
- Command-specific validation before first artifact write.
- Revision before saving when validation fails.
- Successful write verification before saved-path confirmation.
- Accurate create/update/append/replace wording.

### Must Not Include

- A just-created artifact written before required validation passes.
- Post-save patching used as normal cleanup for validation failures in the just-created artifact.
- Saved-path confirmation before successful write verification.
- False save claim.
- Invalid artifact treated as passed because it was later patched.

### Relevant Rules

- `rules/ARTIFACTS.md`
- Command-specific `SKILL.md`
- Command-specific `OUTPUT.md`

### Pass Criteria

Passes only if the command validates before the first artifact write and any validation failure is corrected before saving.

### Fail Criteria

Fails if the command writes a just-created artifact first and then patches it afterward to clean validation failures, even if the final saved artifact is clean.

---

## artifact-global-user-requested-edit-002 — Explicit Edits Remain Allowed

Type: `Artifact / Guardrail`
Priority: `P1`
Status: `Draft`
Mode: `Explicit edit/update`

### Purpose

Ensure the save-order rule does not block transparent user-requested edits, updates, appends, replacements, or corrections.

### User Input

`Update the saved artifact to fix [specific user-requested change].`

### Expected Behavior

MIDAS may edit, update, append, replace, or correct the existing artifact when the user explicitly asks or when a separate maintenance task requires it, but the response should label the action accurately.

### Must Include

- Accurate action label such as `Updated`, `Edited`, `Appended to`, `Replaced`, or equivalent.
- No claim that the edit was part of the original pre-save validation pass.
- Scope limited to the requested edit/update.

### Must Not Include

- Hidden post-save cleanup represented as a clean initial artifact-generation pass.
- Unlabeled correction to a just-created artifact that failed validation.

### Pass Criteria

Passes if explicit edits remain transparent and accurately labeled while normal command generation still validates before first save.
