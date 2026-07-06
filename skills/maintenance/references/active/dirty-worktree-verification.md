# Dirty-Worktree Verification

Use this playbook when verifying MIDAS maintenance work in a profile that already has unrelated dirty or untracked files.

## Principle

A dirty profile does not mean every dirty file was changed by the current task.

Do not revert, clean, or explain unrelated dirt unless the user asks.

## Workflow

1. Identify the files touched by the current task.
2. Verify those files directly with targeted reads or scoped diffs.
3. If useful and allowed, run scoped status checks for the in-scope paths only.
4. Distinguish current-task changes from pre-existing dirty files when possible.
5. Report unrelated dirty state as a caveat, not as task evidence.
6. Do not claim full-profile cleanliness unless a full-profile check was approved and performed.

## Useful Scoped Checks

Use scoped checks such as:

```bash
git -C /home/jordan/.hermes/profiles/midas status --short -- path/to/scope
```

Prefer targeted file reads when the user requested narrow verification.

## Boundaries

Do not run broad discovery if the user restricted scope.

Do not remove untracked files unless cleanup is explicitly approved.

Do not run stock commands, create workspace artifacts, or mutate data files during verification-only work.

## Reporting Language

Use:

- `not verified within scope`
- `pre-existing dirty state caveat`
- `scoped status only`
- `no files outside the approved scope were edited by this task`

Avoid:

- `the repo is clean` unless verified
- `only these files changed` unless broad enough status/diff checks support it
- implying unrelated dirty files were caused by the current task
