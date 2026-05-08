# KiCad Engine

KiCad Engine is a local-first AI-assisted workflow for building, reviewing, validating, and preparing KiCad schematic and PCB projects. It gives Codex, Claude, and similar VS Code agents a strict operating environment so they can help with real engineering work without pretending to replace KiCad, ERC/DRC, or human review.

This repo is intended to be downloaded or cloned locally, opened in VS Code, and used as the working toolkit for AI-assisted KiCad engineering.

## Status

- Repository status: `PRIVATE / INTERNAL / EXPERIMENTAL`
- Public release status: `NOT_PUBLIC_RELEASE_READY`
- Active project: [`04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE`](04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/README.md)
- Active PCB warning: `ESP32_CSI_WIFI_NODE is not fabrication-ready.`

## What This Repo Is

KiCad Engine is a structured workspace for:

- creating and editing KiCad schematics and PCB layouts
- guiding AI agents with explicit engineering rules before they touch design files
- reviewing symbols, footprints, nets, placement, routing, and board constraints
- enforcing routing quality rules such as no right angles, no acute angles, and no sloppy manufacturing geometry
- running or documenting ERC, DRC, routing audits, and visual review steps
- preparing `NOT_FINAL` fabrication deliverables such as Gerbers, drill files, BOMs, and CPL / pick-and-place outputs
- supporting manufacturing workflows for JLCPCB and PCBWay after verification gates pass

## What This Repo Is Not

KiCad Engine is not:

- a replacement for KiCad itself
- a claim that AI can safely autoroute boards without supervision
- a guarantee that every generated report matches the live board unless the live-state checks confirm it
- a fabrication approval system by itself
- a promise that the active project is complete, production-ready, or order-ready

Human review in KiCad is still required before exporting manufacturing files or ordering boards.

## Why This Exists

AI coding agents are good at repeatable file operations, rule enforcement, scripted audits, and producing structured documentation. They are bad at silently making safe engineering decisions without constraints.

This repo exists to close that gap by giving the agent:

- startup rules
- project gates
- routing-quality rules
- placement-readiness rules
- memory and history requirements
- live-state reconciliation
- export checklists
- manufacturing constraints

The result should be small, auditable engineering changes instead of random edits, stale reports, or messy PCB routing.

## Download ZIP / Local VS Code Use

You can use KiCad Engine without setting up any extra GitHub repositories first.

1. On GitHub, click `Code -> Download ZIP`.
2. Extract the ZIP locally.
3. Open the extracted `KICAD_ENGINE` folder in VS Code.
4. Open Codex, Claude, or another AI coding agent inside that VS Code workspace.
5. Start the agent from the repo root and give it this starter prompt:

```text
You are working inside the KICAD_ENGINE repo. First read README.md, CURRENT_STATUS.md, WORKFLOWS_INDEX.md, TOOLS_INDEX.md, and 00_CODEX_START/START_HERE.md. Follow the repo rules before editing any KiCad files. Do not edit schematic or PCB files until you understand the active project, the live project state, the task type, and the validation requirements.
```

For local GUI review or live design editing, KiCad itself still must be installed on the local machine. The repo gives the rules, workflows, prompts, validation scripts, and project structure around KiCad; it does not replace the KiCad application.

## How The Workflow Works

1. A human opens the repo in VS Code and identifies the active project.
2. The AI agent starts from the repo root and reads the startup docs and current project status before touching KiCad files.
3. The agent inspects the real KiCad files and current reports instead of relying on stale Markdown.
4. Before any schematic or PCB edit, the workflow requires backups, scope confirmation, and the correct phase gate.
5. After edits, the workflow requires evidence such as ERC/DRC, geometry audit results, hash changes, and visual review artifacts.
6. Manufacturing outputs are treated as `NOT_FINAL` until the validation and human review gates are complete.

Important hardening layers now in this repo:

- task-type execution contracts
- live-project-state authority over stale reports
- edit-required hash-delta enforcement
- hard-fail routing geometry checks
- placement readiness scoring
- staged routing runner and no-progress detection

## What Is Included

This repo includes:

- KiCad project structure under `04_KICAD_PROJECTS/`
- AI agent startup instructions and repo operating rules
- schematic workflows, checks, and gate guidance
- PCB placement workflows and readiness scoring
- PCB routing rules and staged routing workflows
- 45-degree / no-acute-angle routing enforcement
- live project state tools and live-state-first phase gating
- stale report detection and gate reconciliation
- task execution contracts for docs, audits, placement, routing, and PCB-edit work
- routing geometry checks and hard-fail geometry reporting
- staged routing runner and no-progress detector logic
- JLCPCB and PCBWay export guidance
- optional GitHub / Codespaces / devcontainer setup for repo tooling

## What Is Not Included

This repo does not include:

- the KiCad application installer
- guaranteed automatic schematic or PCB completion
- fabrication approval without human review
- vendor ordering automation
- secrets, credentials, or embedded private tokens

## Using Codex Or Claude With This Repo

1. Open the repo in VS Code from the repository root.
2. Start Codex, Claude, or another AI coding agent from the repo root, not from a random subfolder.
3. Tell the agent to first read [`00_CODEX_START/START_HERE.md`](00_CODEX_START/START_HERE.md), [`README.md`](README.md), [`CURRENT_STATUS.md`](CURRENT_STATUS.md), [`WORKFLOWS_INDEX.md`](WORKFLOWS_INDEX.md), and [`TOOLS_INDEX.md`](TOOLS_INDEX.md) before editing anything.
4. The AI should inspect the real KiCad project files before changing them.
5. The AI should make small, auditable changes instead of broad unreviewed rewrites.
6. The AI should run or document ERC/DRC checks, routing audits, and visual review steps after engineering changes.
7. The AI should never fabricate, export, or order boards without human review and explicit verification evidence.

Recommended starting links:

- humans: [`START_HERE.md`](START_HERE.md), [`CURRENT_STATUS.md`](CURRENT_STATUS.md), [`PROJECTS_INDEX.md`](PROJECTS_INDEX.md)
- AI agents: [`AGENTS.md`](AGENTS.md), [`README_GPT.md`](README_GPT.md), [FOR CHAT GPT.MD](<FOR CHAT GPT.MD>), [`00_CODEX_START/START_HERE.md`](00_CODEX_START/START_HERE.md)

## KiCad Workflow Overview

The intended workflow is:

1. define the active project and target files
2. inspect schematic, PCB, reports, and current blockers
3. back up the project before edits
4. make small schematic, footprint, placement, or routing changes in the correct phase
5. run or document ERC/DRC plus geometry and manufacturability checks
6. review BOM, CPL, and fabrication outputs only after the board state is ready
7. perform human visual review in KiCad before release or ordering

For the current live project, the authoritative state comes from:

- [`CURRENT_STATUS.md`](CURRENT_STATUS.md)
- [`04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/memory/CURRENT_PROJECT_STATE.md`](04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/memory/CURRENT_PROJECT_STATE.md)
- [`04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/memory/CURRENT_BLOCKERS.md`](04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/memory/CURRENT_BLOCKERS.md)

## PCB Routing Rules

These rules are central to the repo and should be treated as hard engineering constraints, not suggestions:

- Avoid 90-degree trace bends.
- Prefer 45-degree bends or smooth intentional routing.
- Absolutely avoid acute angles sharper than 90 degrees.
- Avoid acid traps and manufacturing-unfriendly trace geometry.
- Keep routing clean, inspectable, and DRC-safe.
- High-speed and sensitive traces should use smooth, deliberate routing with the shortest sane path.
- Do not let AI randomly autoroute messy traces without validation.
- If routing geometry is ugly, jagged, over-angled, or impossible to inspect, the routing pass should fail even if a raw DRC snapshot is otherwise quiet.

See also:

- [`14_LAYOUT_AUTOMATION/TRACE_PLANNING_RULES.md`](14_LAYOUT_AUTOMATION/TRACE_PLANNING_RULES.md)
- [`14_LAYOUT_AUTOMATION/TRACE_BY_TRACE_VERIFICATION_RULES.md`](14_LAYOUT_AUTOMATION/TRACE_BY_TRACE_VERIFICATION_RULES.md)
- [`14_LAYOUT_AUTOMATION/ROUTING_GEOMETRY_HARD_FAIL_RULES.md`](14_LAYOUT_AUTOMATION/ROUTING_GEOMETRY_HARD_FAIL_RULES.md)
- [`14_LAYOUT_AUTOMATION/REAL_PROJECT_ROUTING_STOP_CONDITIONS.md`](14_LAYOUT_AUTOMATION/REAL_PROJECT_ROUTING_STOP_CONDITIONS.md)

## Manufacturing / Export Workflow

This repo supports preparing fabrication packages for:

- JLCPCB
- PCBWay

Typical outputs may include:

- Gerbers
- drill files
- BOM
- CPL / pick-and-place files

Those outputs should only be produced after:

- schematic and PCB state are current
- ERC/DRC is run and reviewed
- remaining unconnected items are classified and resolved or explicitly accepted
- footprint and polarity checks are complete
- BOM/CPL readiness is reviewed
- human visual review is complete

Until then, outputs should be treated as `NOT_FINAL`.

## Folder Structure

High-level map:

- `00_CODEX_START/` - startup rules, status files, navigation, phase gates
- `01_MEMORY/` - durable memory and reusable lessons
- `02_HISTORY/` - session logs, command logs, issues, failed attempts, AI-quality artifacts
- `03_TOOLS/` - scripts for maintenance, live-state checks, gating, routing helpers, and automation
- `04_KICAD_PROJECTS/` - active, template, and archived KiCad projects
- `05_OUTPUTS/` - release-readiness outputs, dashboards, and generated summaries
- `09_ACCURACY_ENGINE/` - verification rules, checklists, and anti-hallucination controls
- `14_LAYOUT_AUTOMATION/` - placement/routing rules, scorecards, staged runner logic
- `34_PCB_LAYOUT_SANDBOX/` - layout-variant and pre-edit sandbox workflow
- `99_BACKUPS/` - local-only backups before AI edits, intentionally excluded from Git

You do not need to install extra GitHub repos just to get started locally with the core documentation, prompts, checks, and workflow logic in this repo. Optional external helpers should only be used when a specific documented workflow calls for them.

See:

- [`FOLDER_MAP.md`](FOLDER_MAP.md)
- [`REPO_INDEX.md`](REPO_INDEX.md)
- [`TOOLS_INDEX.md`](TOOLS_INDEX.md)
- [`WORKFLOWS_INDEX.md`](WORKFLOWS_INDEX.md)

## Current Board / Project Status

Active project:

- path: `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE`
- KiCad project: `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_pro`
- KiCad PCB: `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_pcb`

Latest known live PCB state:

- PCB exists
- partial routing exists
- `43` footprints
- `74` tracks
- `32` vias
- `2` zones
- DRC has `0` rule violations and `17` unconnected items
- explicit unrouted nets still include `/DM_C`, `/DM_E`, `/DP_C`, and `/DP_E`

Remaining blockers must always be verified from the live reports before any new engineering claim. Current references:

- [`CURRENT_STATUS.md`](CURRENT_STATUS.md)
- [`04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/FINAL_PCB_VISUAL_REVIEW_PACKET.md`](04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/FINAL_PCB_VISUAL_REVIEW_PACKET.md)
- [`04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/LJ_FINAL_PCB_REVIEW_CHECKLIST.md`](04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/LJ_FINAL_PCB_REVIEW_CHECKLIST.md)
- [`04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/PCB_FINAL_UNCONNECTED_ITEMS_REVIEW.md`](04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/PCB_FINAL_UNCONNECTED_ITEMS_REVIEW.md)

## How To Give Prompts To Codex / Claude

Good prompts in this repo should include:

- the active project path
- the exact target files
- whether the task is docs-only, audit-only, or edit-required
- hard constraints such as `do not edit schematic`, `do not route USB yet`, or `do not generate manufacturing outputs`
- the verification you expect after changes

Good prompt pattern:

```text
You are working in C:\Users\LJ\GitHub\KICAD_ENGINE.
Active project: C:\Users\LJ\GitHub\KICAD_ENGINE\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE
Task type: ROUTING_EDIT_REQUIRED
Read README.md, CURRENT_STATUS.md, and the relevant routing rules first.
Inspect the live .kicad_pcb before editing.
Make only the smallest clean change needed.
Run or document DRC after edits.
Do not generate fabrication outputs.
```

## Example AI Agent Prompts

### 1. Review the KiCad project and summarize the schematic / PCB status

```text
You are working in C:\Users\LJ\GitHub\KICAD_ENGINE.
Read README.md, CURRENT_STATUS.md, AGENTS.md, and the active project reports first.
Inspect the live KiCad project under 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE.
Summarize the current schematic state, PCB state, DRC/ERC evidence, remaining blockers, and next recommended engineering step.
Do not edit design files.
```

### 2. Improve routing while obeying 45-degree / no-acute-angle rules

```text
You are working in C:\Users\LJ\GitHub\KICAD_ENGINE.
Task type: ROUTING_EDIT_REQUIRED.
Read the routing workflow, stop conditions, and geometry hard-fail rules first.
Inspect the live PCB and only repair traces that clearly violate the 45-degree / no-acute-angle routing rules.
Do not route unrelated nets. Run DRC and the routing geometry audit after any PCB edit.
```

### 3. Audit the board for DRC / manufacturing risks

```text
You are working in C:\Users\LJ\GitHub\KICAD_ENGINE.
Task type: AUDIT_ONLY.
Inspect the active KiCad PCB, current reports, and manufacturing-readiness docs.
List DRC status, unrouted nets, unconnected items, routing geometry risks, footprint risks, and fabrication blockers.
Do not edit the design files.
```

### 4. Prepare JLCPCB export files

```text
You are working in C:\Users\LJ\GitHub\KICAD_ENGINE.
Read the active project status, fabrication gates, and export workflow first.
Confirm whether the board is actually ready for JLCPCB export.
If it is not ready, stop and list exact blockers.
If it is ready, prepare the JLCPCB export package and document Gerber, drill, BOM, and CPL evidence.
Do not claim fabrication-ready unless the validation gates are satisfied.
```

### 5. Prepare PCBWay export files

```text
You are working in C:\Users\LJ\GitHub\KICAD_ENGINE.
Read the active project status, fabrication gates, and export workflow first.
Confirm whether the board is actually ready for PCBWay export.
If it is not ready, stop and list exact blockers.
If it is ready, prepare the PCBWay export package and document Gerber, drill, BOM, and pick-and-place evidence.
Do not claim fabrication-ready unless the validation gates are satisfied.
```

### 6. Add or update a schematic block

```text
You are working in C:\Users\LJ\GitHub\KICAD_ENGINE.
This is a schematic-edit task. Do not touch the PCB unless the request explicitly includes a PCB update workflow.
Read the schematic workflow, symbol/footprint checks, and active project memory first.
Inspect the current .kicad_sch and explain the exact block to add or modify before editing.
After edits, run or document ERC and update the project reports.
```

### 7. Review BOM / CPL readiness

```text
You are working in C:\Users\LJ\GitHub\KICAD_ENGINE.
Task type: AUDIT_ONLY.
Inspect the active project BOM-related reports, footprint assignments, manufacturer part data, and placement state.
Summarize BOM readiness, CPL readiness, missing fields, polarity/orientation risks, and blockers for JLCPCB or PCBWay assembly export.
Do not edit the design files unless explicitly instructed.
```

## Safety / Validation Rules Before Fabrication

Before any board is treated as ready for fabrication:

- verify the active project and target files
- create a backup before design edits
- inspect the live KiCad files, not just historical Markdown
- run or document ERC for schematic changes
- run or document DRC for PCB changes
- confirm unrouted nets and unconnected items are resolved or explicitly classified
- confirm routing geometry passes the repo's hard-fail checks
- review BOM and CPL / pick-and-place readiness
- perform human visual review inside KiCad before ordering boards

If any of those are missing, the board should be treated as not ready.

The active example board is not fabrication-ready unless the final live checks, remaining blockers, and human review explicitly say otherwise.

## What Is Excluded By `.gitignore`

The repo intentionally excludes local-only or risky files such as:

- backups under `99_BACKUPS/`
- copied-board routing rehearsal folders
- raw imported sample originals
- caches, lock files, temp files, and local logs
- `.env` files, local credentials, private config, and obvious secret material
- large local-only artifacts and manufacturing-style binaries unless explicitly approved

See [`.gitignore`](.gitignore) and [`PUBLIC_RELEASE_STATUS.md`](PUBLIC_RELEASE_STATUS.md).

## Supported Manufacturing Targets

Current manufacturing/export workflow support is aimed at:

- JLCPCB
- PCBWay

Support means the repo is structured to help generate and review the files those vendors usually require. It does not mean every active project is already approved for manufacture.

## Roadmap

- keep hardening the execution contract so edit-required tasks cannot close with report-only output
- finish live-state-first gating across routing, placement, closeout, and release checks
- improve USB / high-speed routing assistance and geometry visualization
- expand BOM, CPL, and manufacturing-export review helpers
- grow example projects, checklists, and validation fixtures
- complete repo hygiene and licensing work required before public release

## Related Docs

- [`START_HERE.md`](START_HERE.md)
- [`CURRENT_STATUS.md`](CURRENT_STATUS.md)
- [`PROJECTS_INDEX.md`](PROJECTS_INDEX.md)
- [`TOOLS_INDEX.md`](TOOLS_INDEX.md)
- [`WORKFLOWS_INDEX.md`](WORKFLOWS_INDEX.md)
- [`PUBLIC_RELEASE_STATUS.md`](PUBLIC_RELEASE_STATUS.md)
- [`.github/README.md`](.github/README.md)

## License

This repository is MIT-licensed, but vendor documents, reference designs, and third-party materials may carry their own attribution or redistribution rules.
