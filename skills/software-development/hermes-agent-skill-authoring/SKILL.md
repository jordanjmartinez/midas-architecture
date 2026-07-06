---
name: hermes-agent-skill-authoring
description: "Author in-repo SKILL.md: frontmatter, validator, structure."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [skills, authoring, hermes-agent, conventions, skill-md]
    related_skills: [writing-plans, requesting-code-review]
---

# Authoring Hermes-Agent Skills (in-repo)

## Overview

There are two places a SKILL.md can live:

1. **User-local:** `~/.hermes/skills/<maybe-category>/<name>/SKILL.md` — personal, not shared. Created via `skill_manage(action='create')`.
2. **In-repo (this skill is about this case):** `/home/bb/hermes-agent/skills/<category>/<name>/SKILL.md` — committed, shipped with the package. Use `write_file` + `git add`. `skill_manage(action='create')` does NOT target this tree.

## When to Use

- User asks you to add a skill "in this branch / repo / commit"
- You're committing a reusable workflow that should ship with hermes-agent
- You're editing an existing skill under `/home/bb/hermes-agent/skills/` (use `patch` for small edits, `write_file` for rewrites; `skill_manage` still works for patch on in-repo skills, but not for `create`)

## Required Frontmatter

Source of truth: `tools/skill_manager_tool.py::_validate_frontmatter`. Hard requirements:

- Starts with `---` as the first bytes (no leading blank line).
- Closes with `\n---\n` before the body.
- Parses as a YAML mapping.
- `name` field present.
- `description` field present, ≤ **1024 chars** (`MAX_DESCRIPTION_LENGTH`).
- Non-empty body after the closing `---`.

Peer-matched shape used by every skill under `skills/software-development/`:

```yaml
---
name: my-skill-name               # lowercase, hyphens, ≤64 chars (MAX_NAME_LENGTH)
description: Use when <trigger>. <one-line behavior>.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [short, descriptive, tags]
    related_skills: [other-skill, another-skill]
---
```

`version` / `author` / `license` / `metadata` are NOT enforced by the validator, but every peer has them — omit and your skill sticks out.

## Size Limits

- Description: ≤ 1024 chars (enforced).
- Full SKILL.md: ≤ 100,000 chars (enforced as `MAX_SKILL_CONTENT_CHARS`, ~36k tokens).
- Peer skills in `software-development/` sit at **8-14k chars**. Aim for that range. If you're pushing past 20k, split into `references/*.md` and reference them from SKILL.md.

## Peer-Matched Structure

Every in-repo skill follows roughly:

```
# <Title>

## Overview
One or two paragraphs: what and why.

## When to Use
- Bulleted triggers
- "Don't use for:" counter-triggers

## <Topic sections specific to the skill>
- Quick-reference tables are common
- Code blocks with exact commands
- Hermes-specific recipes (tests via scripts/run_tests.sh, ui-tui paths, etc.)

## Common Pitfalls
Numbered list of mistakes and their fixes.

## Verification Checklist
- [ ] Checkbox list of post-action verifications

## One-Shot Recipes (optional)
Named scenarios → concrete command sequences.
```

Not every section is mandatory, but `Overview` + `When to Use` + actionable body + pitfalls are the minimum for the skill to feel like a peer.

## Directory Placement

```
skills/<category>/<skill-name>/SKILL.md
```

Categories currently in repo (confirm with `ls skills/`): `autonomous-ai-agents`, `creative`, `data-science`, `devops`, `dogfood`, `email`, `gaming`, `github`, `leisure`, `mcp`, `media`, `mlops/*`, `note-taking`, `productivity`, `red-teaming`, `research`, `smart-home`, `social-media`, `software-development`.

Pick the closest existing category. Don't invent new top-level categories casually.

## Workflow

1. **Survey peers** in the target category:
   ```
   ls skills/<category>/
   ```
   Read 2-3 peer SKILL.md files to match tone and structure.
2. **Check validator constraints** in `tools/skill_manager_tool.py` if unsure.
3. **Draft** with `write_file` to `skills/<category>/<name>/SKILL.md`.
4. **Validate locally**:
   ```python
   import yaml, re, pathlib
   content = pathlib.Path("skills/<category>/<name>/SKILL.md").read_text()
   assert content.startswith("---")
   m = re.search(r'\n---\s*\n', content[3:])
   fm = yaml.safe_load(content[3:m.start()+3])
   assert "name" in fm and "description" in fm
   assert len(fm["description"]) <= 1024
   assert len(content) <= 100_000
   ```
5. **Git add + commit** on the active branch.
6. **Note:** the CURRENT session's skill loader is cached — `skill_view` / `skills_list` will not see the new skill until a new session. This is expected, not a bug.

## Cross-Referencing Other Skills

`metadata.hermes.related_skills` unions both trees (`skills/` in-repo and `~/.hermes/skills/`) at load time. You CAN reference a user-local skill from an in-repo skill, but it won't resolve for other users who clone the repo fresh. Prefer referencing only in-repo skills from in-repo skills. If a frequently-referenced skill lives only in `~/.hermes/skills/`, consider promoting it to the repo.

## Editing Existing In-Repo Skills

- **Small fix (typo, added pitfall, tightened trigger):** `skill_manage(action='patch', name=..., old_string=..., new_string=...)` works fine on in-repo skills.
- **Major rewrite:** `write_file` the whole SKILL.md. `skill_manage(action='edit')` also works but requires supplying the full new content.
- **Adding supporting files:** `write_file` to `skills/<category>/<name>/references/<file>.md`, `templates/<file>`, or `scripts/<file>`. `skill_manage(action='write_file')` also works and enforces the references/templates/scripts/assets subdir allowlist.
- **Always commit** the edit — in-repo skills are source, not runtime state.

## Profile-Local MIDAS Authoring

For MIDAS profile-local skill/rule edits under `/home/jordan/.hermes/profiles/midas/`, see `references/midas-profile-local-authoring.md`. It covers exact `SKILL.md` replacements, shared `rules/*.md` files, command-menu patches, tracker-skill boundaries, runtime artifact prohibitions, and exact confirmation-only responses.

For MIDAS command runtime-test failures where the user asks to patch the output contract without rebuilding the command, see `references/midas-runtime-test-contract-patches.md`.

## Common Pitfalls

1. **Using `skill_manage(action='create')` for an in-repo skill.** It writes to `~/.hermes/skills/`, not the repo tree. Use `write_file` for in-repo creation.

2. **Leading whitespace before `---`.** The validator checks `content.startswith("---")`; any leading blank line or BOM fails validation.

3. **Description too generic.** Peer descriptions start with "Use when ..." and describe the *trigger class*, not the one task. "Use when debugging X" > "Debug X".

4. **Forgetting the author/license/metadata block.** Not validator-enforced, but every peer has it; omitting makes the skill look half-finished.

5. **Writing a skill that duplicates a peer.** Before creating, `ls skills/<category>/` and open 2-3 peers. Prefer extending an existing skill to creating a narrow sibling.

6. **Expecting the current session to see the new skill.** It won't. The skill loader is initialized at session start. Verify in a fresh session or via `skill_view` using the exact path.

7. **Over-helping when the user provides exact skill content and boundaries.** If the user says to create only a specific `SKILL.md`, use the supplied content verbatim, create only that file, do not create supporting data/artifact files, do not run the new command, and keep the final response to the requested confirmation format. If the user later tightens the boundary (for example, "do not add alias storage"), remove the earlier over-broad behavior rather than layering contradictory rules. For command skills that declare future storage side effects, creating or editing the skill must not create those runtime data files or workspace artifacts unless the user explicitly asks to run the command.

8. **Confirmation-only final responses.** When the user gives an exact final confirmation string (for example, `Updated: /path/to/SKILL.md`), make the final response exactly that string after completing and verifying the edit. Do not add summaries, bullets, or extra reassurance.

9. **For user-local profile skills, verify side-effect boundaries.** When editing skills under `~/.hermes/profiles/<profile>/skills/`, especially command skills that describe future data files or workspace artifacts, validate frontmatter and verify that the edit did not create runtime data/artifact files unless the user explicitly asked. Skill authoring can describe future behavior without executing that behavior. If a runtime file already exists from a prior command run, do not delete, rewrite, or treat it as part of the skill edit; simply avoid creating/changing runtime state during the authoring task.

10. **Patch narrow command-menu edits narrowly.** When the user asks to add/update a command line or small command section and says not to rewrite/bloat the skill, patch only the visible menu lines needed. Do not bump versions, rewrite examples, or change aliases unless explicitly requested or necessary to remove stale visible behavior.

11. **End-of-session skill-library reviews should improve the governing class skill.** When asked to review a conversation and update the skill library, prefer patching the currently loaded class-level skill that governed the work. Capture workflow corrections, exact-output preferences, and durable authoring pitfalls there; avoid creating narrow one-session skills. If detail is too session-specific for SKILL.md but still reusable, add a concise `references/` file under the existing umbrella and point to it from SKILL.md.

12. **Maintenance-skill cleanup is not a dumping ground.** When restructuring a profile-local maintenance skill, keep the skill class-level and clean: active references should be reusable operating playbooks, while one-off patch records, staged implementation notes, regression logs, activation notes, and historical incidents belong in archive/reference detail rather than active routing law. If `skills_list` can see a skill but `skill_view` cannot resolve it, treat that as resolver/metadata hygiene to investigate and fix in place; do not create a duplicate skill directory as a workaround.

13. **Read-only staging requests stay read-only.** If the user says not to modify files and will provide instructions next, perform only inspection/audit and report exact findings. Do not preemptively patch skills, rules, evals, usage metadata, or references until the user explicitly authorizes edits.

14. **Exact draft installs with drift checks: preserve supplied content.** When the user provides exact draft files to install plus asks for architecture/eval/drift verification, copy the supplied files exactly to the requested paths first. Run scoped checks against the installed architecture, registry row, artifact paths, mode defaults, and eval coverage, but do not "fix" the supplied draft content unless the user explicitly asks for a content patch. If a naive text check fails because the exact draft phrases differ, refine the check or report the limitation rather than modifying the draft.

13. **Linking to skills that don't exist in-repo.** `related_skills: [some-user-local-skill]` works for you but breaks for other clones. Prefer only in-repo links.

## Verification Checklist

- [ ] If the user gave exact content/boundaries, the output preserved those boundaries without adding extra files, modes, data stores, or behavior
- [ ] For profile-local command skills, no runtime data/watchlist/workspace artifacts were created unless the user explicitly requested execution
- [ ] File is at `skills/<category>/<name>/SKILL.md` (not in `~/.hermes/skills/`)
- [ ] Frontmatter starts at byte 0 with `---`, closes with `\n---\n`
- [ ] `name`, `description`, `version`, `author`, `license`, `metadata.hermes.{tags, related_skills}` all present
- [ ] Name ≤ 64 chars, lowercase + hyphens
- [ ] Description ≤ 1024 chars and starts with "Use when ..."
- [ ] Total file ≤ 100,000 chars (aim for 8-15k)
- [ ] Structure: `# Title` → `## Overview` → `## When to Use` → body → `## Common Pitfalls` → `## Verification Checklist`
- [ ] `related_skills` references resolve in-repo (or are explicitly OK to be user-local)
- [ ] `git add skills/<category>/<name>/ && git commit` completed on the intended branch
