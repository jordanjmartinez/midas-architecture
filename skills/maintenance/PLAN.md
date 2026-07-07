# Midas Maintenance Plan Contract

## Purpose

PLAN.md defines how Midas proposes, approves, executes, verifies, reports, and stops staged maintenance work.

The goal is to prevent:

- scope drift
- hidden follow-on work
- completion of later stages without approval
- accidental command activation
- accidental runtime validation
- unwanted workspace, watchlist, artifact, registry, eval, backup, commit, or push changes
- old todos continuing after the user changes scope

This file is an active maintenance contract.

It is not an archived reference note.

## Core Rule

A staged plan is a contract.

Midas may execute only the currently approved stage.

Approval for Stage N does not authorize Stage N+1.

After completing a stage, Midas must stop, report what happened, and wait for explicit user approval before continuing.

Do not continue into the next stage because it is obvious, small, adjacent, already planned, convenient, or likely desired.

Required flow:

proposal → approval → execution → verification → stop → next approval

## When To Use This Contract

Use this contract for any maintenance task involving:

- multiple files
- multiple authority layers
- command creation
- command refactor
- command activation
- eval creation or promotion
- registry cleanup
- shared-rule installs
- output-contract changes
- reference-folder migration
- archive cleanup
- workspace or artifact-policy changes
- watchlist/data-file changes
- runtime validation
- backup, commit, or push steps

If the user asks only for a one-file exact patch, PLAN.md may be unnecessary unless the task naturally has stages.

## Planning-Only Requests

If the user asks for a plan, direction, proposal, audit, sequencing, or recommendation, do not edit files.

Return the plan only.

Do not start Stage 1 unless the user explicitly asks to implement it.

Examples of planning-only requests:

- “What should we do?”
- “Give me the direction.”
- “Design the stages.”
- “What files should exist?”
- “Do not implement yet.”
- “Just the plan.”

## Required Plan Format

When proposing staged maintenance work, use this format:

```md
## Proposed Staged Plan

Scope:
[What the plan covers.]

Non-goals:
[What the plan does not cover.]

Contract Authority Check:
- Existing global authority checked: [files]
- Existing command authority checked: [files]
- Proposed new or changed behavior: [summary]
- Applies to: [one command / multiple commands / global]
- Correct home: [rules / SKILL.md / OUTPUT.md / evals / docs / templates / schemas / references / archive]
- Reason: [why]
- Duplication risk: [none / possible / confirmed]
- Action: [point to existing rule / create global rule / create command-local rule / archive / defer]

Approval model:
Each stage requires explicit approval. Approval for one stage does not authorize the next stage.

### Stage 1 — [Name]

Goal:
[One clear outcome.]

Files in scope:
- [path]
- [path]

Allowed actions:
- [action]
- [action]

Prohibited actions:
- [action]
- [action]

Verification:
- [check]
- [check]

Stop condition:
Stop after reporting Stage 1 results. Do not start Stage 2 without approval.

### Stage 2 — [Name]

[Repeat the same structure.]
```

## Hard-Stop Stages

Some stages always require separate explicit approval, even if the user says to approve the whole plan.

Hard-stop stages include:

- status promotion from Draft to Active
- command activation
- live runtime validation
- stock command runs
- workspace artifact creation or mutation
- watchlist or data-file mutation
- deleting files
- moving or archiving large reference folders
- backup, commit, push, or deployment
- changes outside the Midas profile
- changes involving secrets, API keys, credentials, cron, plugins, or automation

For hard-stop stages, stop and ask for approval using clear wording:

```md
Stage [N] requires separate approval because it involves [reason].

Approve Stage [N]?
```

## Execution Rules

When executing an approved stage:

- Re-read the approved stage before editing.
- Stay inside the files and actions listed for that stage.
- Do not patch files from later stages.
- Do not perform “while I’m here” cleanup.
- Do not run live commands unless the approved stage explicitly allows it.
- Do not create or mutate workspace artifacts unless the approved stage explicitly allows it.
- Do not change registry, eval, or status metadata unless the approved stage explicitly allows it.
- If new work is discovered, propose it as a future stage.
- Verify only the approved stage’s scope unless broader verification is approved.
- Stop after the stage report.

## Discovery During a Stage

If Midas discovers that the approved stage requires extra work outside the approved scope, it must stop or narrow the work.

Use this report shape:

```md
Blocked / scope expansion needed:
[What was discovered.]

Why it is outside the approved stage:
[Reason.]

Proposed next stage or revised scope:
[New proposed stage.]

Awaiting approval before continuing.
```

## Stage Completion Report

After each stage, Midas must report in this format:

```md
## Stage [N] Complete — [Name]

Changed:
- [file]: [what changed]

Inspected:
- [file]: [why inspected]

Verified:
- [check]: [result]

Not changed:
- [explicitly excluded file/scope]
- [explicitly excluded file/scope]

Commands/evals run:
- [none / exact command]

Workspace/watchlist/artifacts:
- [none / exact change]

Status changes:
- [none / exact change]

Limitations:
- [anything not verified]

Next proposed stage:
Stage [N+1] — [name]

Awaiting approval:
Approve Stage [N+1] to continue.
```

## Prohibited Completion Behavior

Midas must not say or do any of the following unless explicitly approved:

- “I also completed Stage 2.”
- “I went ahead and did the next stage.”
- “I cleaned up the related files too.”
- “I promoted the command since validation looked good.”
- “I ran a live smoke test to verify it.”
- “I archived the rest of the references.”
- “I updated the registry while I was there.”
- “I committed and pushed the changes.”
- “I finished the remaining stages.”

These are stage-boundary violations.

## Plan Drift Rule

The approved plan is not permanent permission.

If the user changes direction, pauses, narrows scope, or says not to implement, Midas must discard stale pending stages and re-anchor on the latest user message.

After interruption or context compaction, treat old todos as background only.

The latest user instruction controls the next action.

## Read-Only Stage Rule

If a stage is labeled read-only:

- do not edit files
- do not patch files
- do not create artifacts
- do not run commands that write files
- do not promote statuses
- do not update registries
- do not create missing files even if gaps are obvious

A read-only stage ends with findings only.

## Patch Stage Rule

If a stage is labeled patch or implementation:

- patch only approved files
- preserve exact-scope boundaries
- avoid adjacent cleanup
- report all changed files
- verify scoped diffs
- do not run live stock commands unless explicitly approved

## Validation Stage Rule

Validation stages must define whether they are:

- static validation
- fixture/mock validation
- read-only runtime validation
- live runtime validation

Live runtime validation is a hard-stop stage.

Do not convert static or fixture validation into live validation.

Do not run stock commands as a maintenance shortcut unless explicitly approved.

## Activation Stage Rule

Activation is always a separate hard-stop stage.

Before activation, Midas must clearly report:

- current status
- files that will change
- eval status
- registry status
- whether runtime validation was performed
- what will not change

Activation patches should be status-only unless the user explicitly approves behavior changes.

Do not combine activation with behavior edits.

## Reference Migration Rule

Reference-folder migration should be staged separately:

1. create new contract structure
2. add pointers
3. classify active vs archive
4. move or distill active playbooks
5. archive historical notes
6. add eval coverage

Do not bulk-move, delete, or relink historical references in the same stage as creating the new maintenance contract unless the user explicitly approves that combined scope.

Archived means not active routing law.

Archived does not mean deleted.
