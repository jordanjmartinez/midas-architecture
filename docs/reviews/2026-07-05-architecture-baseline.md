# Midas Architecture Baseline Review

Status: Approved as architecture baseline (Jordan, 2026-07-05)
Reviewer: Claude, external architecture and direction review
Repository: github.com/jordanjmartinez/midas-architecture
Reviewed at commit: `7aba818`
Suggested location: `docs/reviews/2026-07-05-architecture-baseline.md`

Scope reviewed: SOUL.md, AGENTS.md, all 11 files in `rules/`, docs (ARCHITECTURE.md,
COMMAND_REGISTRY.md), all 12 stock-analysis command skills (registry metadata, structure,
and one full-skill sample), the three command-local contracts, the maintenance skill,
templates, tools, and the eval suite.

---

## Authority Notice

This document is a findings tracker and design record. Per `rules/CONTRACT_AUTHORITY.md`,
docs must not contain hidden runtime rules. Nothing in this file is active Midas policy.
Every remediation listed here must be applied through the normal Contract Authority
process (Contract Authority Check, correct authority layer, eval coverage where relevant)
before it changes behavior.

## How To Use This File

Each finding has an ID, a priority, and a status. Statuses: `Open`, `In Progress`,
`Closed`, `Wont Fix`. When a finding is closed, record the closing commit hash in the
Notes column. Do not edit finding descriptions after baseline approval; append notes
instead, so the baseline stays a stable reference point.

---

## Verdict

The architecture is sound. The layering (identity, onboarding, global rules, command
skills, local contracts, evals) is coherent, the no-secondary-law doctrine in
CONTRACT_AUTHORITY.md is the right constitutional idea, and registry metadata discipline
is unusually good. The findings below are mostly cases where the newest and most powerful
components (intelligence contracts, maintenance skill, gems workspace tree) grew faster
than the constitution that governs them. Nothing requires redesign.

---

## Findings Index

| ID  | Priority | Area              | Title                                                        | Status | Notes |
|-----|----------|-------------------|--------------------------------------------------------------|--------|-------|
| 2.1 | P0       | Commands/Contracts| `contracts/` is an undefined authority layer                  | Closed | `3bdad7f` |
| 1.1 | P0       | Global            | Rule index divergence across four files                       | Closed | `3bdad7f` |
| 2.2 | P1       | Registry          | Maintenance skill exists but is unregistered                  | Closed | P1 fixes commit |
| 4.1 | P1       | Artifacts         | Gems workspace tree absent from ARTIFACTS canon               | Closed | P1 fixes commit; see note in status log |
| 1.2 | P1       | Global            | `schemas/` is a ghost layer                                   | In Progress | layer established; shape migrations pending |
| 1.3 | P1       | Global            | Two overlapping governance systems                            | Closed | P1 fixes commit |
| 2.3 | P2       | Commands          | `!full` lacks OUTPUT.md and eval coverage                     | Closed | P2: removed entirely; template preserved as promote seed; !promote registered Planned |
| 2.4 | P2       | Commands          | Legacy filing-backed skill claims Midas command triggers      | Closed | found post-baseline; routing note added in P2 fixes |
| 1.4 | P2       | Global            | RERATING.md is Draft but mandatory                            | Closed | P2 fixes commit |
| 4.2 | P2       | Artifacts         | Second data store not enumerated globally                     | Closed | P2 fixes commit |
| 6.1 | P2       | Evals             | Verify earnings/updates mode-routing eval coverage            | Closed | verified: no output modes; explicit declaration added |
| 6.2 | P2       | Evals             | No automated registry-sync check                             | Open   |       |
| 3.1 | P3       | Registry          | Category label mismatch for `!risk`                           | Closed | P3 hygiene commit |
| 3.2 | P3       | Docs              | BUILD_ORDER.md recommended but missing                        | Closed | P3 hygiene commit |
| 3.3 | P3       | Registry          | Aliases vs subcommands are conflated                          | Closed | P3 hygiene commit |
| 1.5 | P3       | Global            | Absolute-path portability                                     | Closed | P3 hygiene commit |
| 6.3 | P3       | Hygiene           | `__pycache__` committed; no .gitignore                        | Closed | P3 hygiene commit |
| 5.1 | Watch    | Rules             | Rerating concept spans three rule files                      | Open   |       |

---

## Detailed Findings

### 2.1 (P0) `contracts/` is an undefined authority layer

Evidence: CONTRACT_AUTHORITY.md defines these layers: rules, SKILL.md, OUTPUT.md, evals,
docs, templates, schemas, references, references/archive. It never defines `contracts/`.
Meanwhile `tracker/contracts/fund-manager.md` (107KB, largest file in Midas),
`tracker/contracts/politician.md` (60KB), and `gems/contracts/hidden-gems.md` (26KB) hold
about 194KB of the densest behavioral law in the system. The gems contract self-remedies
with an explicit Authority Boundaries section (owns / does not own) and path deferrals to
CONTRACT_AUTHORITY and RERATING. The two tracker contracts contain neither an Authority
Boundaries section nor any reference to CONTRACT_AUTHORITY (verified by grep).

Impact: the constitution written to prevent hidden rulebooks does not govern the largest
rulebooks in the system. Tracker contracts can drift into global law with no boundary.

Fix: add a `contracts/` layer definition to CONTRACT_AUTHORITY.md (allowed and prohibited
content, required Authority Boundaries header, required global-rule deferral), then
retrofit fund-manager.md and politician.md with gems-style Authority Boundaries blocks.

### 1.1 (P0) Rule index divergence across four files

Evidence: `rules/` contains 11 files. SOUL.md lists 6. AGENTS.md read order lists 6 plus
conditional CONTRACT_AUTHORITY. GLOBAL.md Shared Rule Library lists 9 and omits
METRICS.md, the largest rule file (42KB), which GLOBAL itself cites elsewhere.
ARCHITECTURE.md Current Rule Files lists 7 (missing COMMAND_INTERFACE,
CONTRACT_AUTHORITY, MARKET_DATA, RERATING).

Impact: four indexes, four different answers; a single-source-of-truth violation of the
system's own doctrine. An agent following any one index misses real law.

Fix: make GLOBAL.md's Shared Rule Library the single canonical index, complete it, and
convert SOUL.md, AGENTS.md, and ARCHITECTURE.md to pointers at that index.

### 2.2 (P1) Maintenance skill exists but is unregistered

Evidence: `skills/maintenance/` is a full command system (SKILL.md v2.0.0 plus
MAINTENANCE.md, PLAN.md, OUTPUT.md, active/archived references) with eval coverage at
`evals/maintenance.eval.md`. It has no row in COMMAND_REGISTRY.md. The registry's own
freshness rule declares the registry stale when a skill exists without a row. It also
introduces two contract file types (MAINTENANCE.md, PLAN.md) not defined in
CONTRACT_AUTHORITY, and GLOBAL's promotion gate flags skills whose purpose is managing
other skills.

Impact: `!commands` is registry-bound and therefore cannot surface the most powerful
skill in the system; the approval trail (status, category) is missing.

Fix: add a registry row (category System / Utility), record status, and either define
MAINTENANCE.md/PLAN.md as part of the `contracts/` layer work in 2.1 or fold their
authority statement into the layer definitions.

### 4.1 (P1) Gems workspace tree absent from ARTIFACTS canon

Evidence: ARTIFACTS.md's Canonical Workspace Structure defines tickers/, trackers/,
watchlists/, reports/. The live workspace uses a heavily populated
`workspace/gems/[sector]/[theme].md` tree with an index.md (ai, cybersecurity, defense,
energy, memory, networking, robotics, space). That tree is defined only in gems
command-local files. The only gems mention in ARTIFACTS is a sample report filename.

Impact: canonical workspace shape is global law by the system's own doctrine; a whole
artifact tree exists as hidden local law.

Fix: add the gems tree to the Canonical Workspace Structure block in ARTIFACTS.md; keep
write mechanics local to the gems command.

### 1.2 (P1) `schemas/` is a ghost layer

Evidence: eight files reference `schemas/` as an authority layer (AGENTS.md folder map,
CONTRACT_AUTHORITY layer definitions, GLOBAL approved locations, ARCHITECTURE Layer 8).
The folder does not exist. Schema-like content lives elsewhere: a structured Alpha Queue
candidate schema inside the fund-manager contract, and watchlist JSON schema notes in wl
references.

Impact: a layer that exists only on paper trains agents to ignore the map; structured
shapes accumulate in the wrong layers.

Fix: either create `schemas/` and migrate structured shapes into it, or remove the layer
from all constitutional references. Decide once; apply everywhere.

### 1.3 (P1) Two overlapping governance systems

Evidence: CONTRACT_AUTHORITY.md (placement decision tree, Contract Authority Check) and
GLOBAL.md's Auto-Created File Promotion Gate (Guard Agent questions, promotion criteria,
status labels) cover the same territory with different vocabularies. The gate is roughly
half of GLOBAL.md.

Impact: parallel governance texts drift apart over time; GLOBAL stops being a control
layer and becomes a second constitution.

Fix: merge the promotion gate into CONTRACT_AUTHORITY.md (or a single GOVERNANCE.md) and
leave a pointer in GLOBAL.md.

### 2.3 (P2) `!full` lacks OUTPUT.md and eval coverage

Evidence: registry and skill metadata agree: Draft status, classification/scoring/metrics
all Required, writes `full.md`, Output Path and Eval File both "Not created yet".

Impact: the command that synthesizes every subsystem has no output contract and no
regression coverage; it is the most likely surface for drift to appear first.

Fix: either complete OUTPUT.md and an eval next, or add an explicit confirm-before-run
gate to its SKILL.md while Draft.

### 1.4 (P2) RERATING.md is Draft but mandatory

Evidence: RERATING.md declares Status: Draft. GLOBAL.md states rerating reasoning must
follow it, and the gems contract formally inherits from it.

Impact: a must-follow Draft is a contradiction an agent can resolve in either direction.

Fix: promote RERATING.md to Active, or soften GLOBAL's language to advisory until it
stabilizes.

### 4.2 (P2) Second data store not enumerated globally

Evidence: ARTIFACTS.md names `data/midas_watchlist.json` as the watchlist source of
truth. `data/tracker_watchlist.json` (person/manager roster) is defined only inside
tracker SKILL.md. ARTIFACTS phrasing is also conditional ("If the existing source of
truth is...") where it should be declarative.

Impact: nothing at the global layer knows `data/` holds two stores; a future command can
collide with the roster file.

Fix: add a short Data Stores enumeration to ARTIFACTS.md listing both files and their
owning commands; make the source-of-truth statement declarative.

### 6.1 (P2) Verify earnings/updates mode-routing eval coverage

Evidence: COMMAND_INTERFACE.md requires mode-routing evals for commands that support
output modes. Grep found mode-routing coverage in research, financials, thesis, risk, and
market evals only. Earnings and updates did not appear.

Impact: unverified; may be a real gap or may reflect commands that do not support modes.

Fix: confirm whether earnings and updates SKILLs declare mode support; if yes, add the
minimum mode-routing evals; if no, note the exception explicitly per COMMAND_INTERFACE.

### 6.2 (P2) No automated registry-sync check

Evidence: COMMAND_REGISTRY.md sketches future automation
(`scripts/update_command_registry.py`) but nothing checks skills against the registry
today. Finding 2.2 is the live proof.

Fix: build a minimal check mode that parses each skill's Registry Metadata block and
diffs it against the registry table; run it as an eval.

### 3.1 (P3) Category label mismatch for `!risk`

Registry row uses "Risk Assessment"; the defined category list says "Risk Analysis".
Align to the defined list.

### 3.2 (P3) BUILD_ORDER.md recommended but missing

ARCHITECTURE.md recommends `docs/BUILD_ORDER.md`; only `docs/plans/` exists. Create it or
remove the recommendation.

### 3.3 (P3) Aliases vs subcommands are conflated

Tracker lists `!show track` and `!track rm` as aliases; wl mixes true aliases
(`!watchlist`, `!list`) with subcommands (`!wl rm`, `!wl updates`). Consider a separate
Invocations or Subcommands field in the metadata standard.

### 1.5 (P3) Absolute-path portability

367 references to `/home/jordan/...` across 55 files. Functional on the current machine;
brittle for migration, renames, or mirrors. Consider a profile-root-relative convention.

### 6.3 (P3) `__pycache__` committed; no .gitignore

`__pycache__` directories are committed under evals/, tools/, and
skills/stock-analysis/market/scripts/. Add a .gitignore covering `__pycache__/`,
`*.pyc`, and runtime state.

### 5.1 (Watch) Rerating concept spans three rule files

RERATING.md (framework), CLASSIFICATIONS.md (rerating modifiers), and SCORING.md
(valuation pillar) all touch rerating. Consistent today. Ensure RERATING's Relationship
to Other Rules section names the other two explicitly so a future edit cannot silently
fork the concept.

---

## Strengths To Preserve

These are working as designed and should not be casually refactored:

- Registry metadata blocks mirroring the registry table (verified across all 12 commands).
- The pointer pattern in command skills: rule references by path, guardrails as short
  command-specific deltas (research SKILL.md is the reference example).
- COMMAND_INTERFACE mode-conflict handling: hard fail, no artifact written, exact
  failure format.
- The gems contract's Authority Boundaries section; it is the template for finding 2.1.
- ARTIFACTS.md create/update/append/replace semantics, required headers, and the
  prompt-injection rule for external content.
- MARKET_DATA's canonical read-only helper (tools/market_data_snapshot.py) with key
  safety, matching the contract exactly.
- The Self-Improvement Write Gate in GLOBAL.md: the agent may not change its own
  architecture without explicit user approval.
- Eval doctrine: evals may test contracts but must not create them.

## Remediation Order

1. P0 pair first: 2.1 (contracts layer plus tracker retrofits) and 1.1 (canonical rule
   index). These two close the largest constitutional gaps.
2. P1 set: 2.2, 4.1, 1.2, 1.3.
3. P2 set: 2.3, 1.4, 4.2, 6.1, 6.2.
4. P3 set: batchable in a single hygiene commit.

Every change routes through the Contract Authority Check and receives eval coverage where
it prevents a regression, per existing Midas doctrine.

---

Baseline recorded 2026-07-05. Reviewed at commit `7aba818`. Findings above are frozen;
progress is tracked in the Status and Notes columns only.

Status log:

- 2026-07-05: 2.1 and 1.1 closed at `3bdad7f` (P0 fixes). 2.2, 4.1, and 1.3
  closed in the P1 fixes commit. 1.2 moved to In Progress: schemas/ layer
  established via schemas/README.md; shape migrations remain pending. Note on
  4.1: the live gems tree is theme/subtheme with general.md defaults, per the
  gems artifact-index reference; ARTIFACTS mirrors that structure, not the
  sector/theme wording in the original finding.

- 2026-07-05 (P2, revised): 2.3 closed by full removal rather than deferral,
  per Jordan's harness-tightening decision. The !full skill folder is deleted;
  its synthesis template, the rules/OUTPUT.md !full section, and the
  evals/README.md !full section are preserved in
  docs/plans/2026-07-05-promote-command-seed.md. !promote is registered as
  Planned in the registry, replacing the !full row. All 117 live-surface
  references were removed or rewritten (enumeration drops, suggestion rewrites
  to the four-command path, eval routing updates); dated historical reference
  files were left untouched as records. New finding 2.4 closed via a Midas
  Routing Note in the legacy filing-backed skill. 1.4 closed: RERATING
  promoted to Active. 4.2 closed: both data stores enumerated in ARTIFACTS.
  6.1 closed: earnings and updates declare no output modes. Remaining open:
  6.2 and the P3 batch.

- 2026-07-05 (P3): hygiene batch. 3.1 closed: !risk category aligned to Risk
  Analysis. 3.2 closed: BUILD_ORDER.md references removed from ARCHITECTURE
  (the build order already lives inline there; a second file would duplicate
  it). 3.3 closed: Aliases columns now hold true top-level aliases only;
  subcommands moved to a Subcommands line in the wl and tracker metadata
  blocks, with an Aliases vs Subcommands definition added to the registry.
  1.5 closed: all profile-prefixed absolute paths converted to
  profile-root-relative, with a path convention note in GLOBAL and AGENTS;
  smoke-test one command after applying. 6.3 closed: .gitignore added,
  committed __pycache__ removed. Remaining open: 1.2 (schema migrations) and
  6.2 (registry-sync check).
