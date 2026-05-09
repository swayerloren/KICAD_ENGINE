# KiCad Engine

AI-assisted KiCad workflow engine for using Codex or Claude inside VS Code with your existing KiCad app.

![KiCad](https://img.shields.io/badge/KiCad-local_app-blue)
![VS Code](https://img.shields.io/badge/VS%20Code-workspace-007ACC)
![Codex ready](https://img.shields.io/badge/Codex-ready-111111)
![Claude ready](https://img.shields.io/badge/Claude-ready-CC785C)
![PCB workflow](https://img.shields.io/badge/PCB-workflow-2E8B57)
![JLCPCB / PCBWay](https://img.shields.io/badge/JLCPCB%20%2F%20PCBWay-supported-0A7E3B)
![Experimental](https://img.shields.io/badge/status-experimental-orange)

KiCad Engine is a repo you can download, open in VS Code, and give to Codex or Claude so the AI agent has structured rules, prompts, tools, and workflows for working on KiCad schematic and PCB projects. It is designed for people who already like KiCad and want AI assistance without switching to Flux or another paid PCB design platform.

The repo is the AI-agent operating system for KiCad work. It gives the agent a repeatable workspace, startup rules, task contracts, validation gates, and project structure so it can help with real KiCad projects without depending on hidden local folders or improvised workflow assumptions.

## Fast Start: ZIP -> VS Code -> One Prompt

1. Download the repo ZIP from GitHub.
2. Extract it.
3. Open the `KICAD_ENGINE` folder in VS Code.
4. Open Codex or Claude in that workspace.
5. Paste this prompt:

```text
You are working inside the KICAD_ENGINE repo. Before doing any work, read README.md, ONE_PROMPT_START.md if present, CURRENT_STATUS.md, WORKFLOWS_INDEX.md, TOOLS_INDEX.md, 03_TOOLS/TOOLS_INDEX.md, EXTERNAL_DEPENDENCIES.md, and 00_CODEX_START/START_HERE.md. Run python health_check.py --no-write if available. Use portable repo docs and live discovery scripts as tool truth. Treat 00_CODEX_START/TOOL_INDEX.md as machine-specific inventory only. Use repo-relative paths only. Do not assume the original author's local paths. Detect the local KiCad install if needed. Do not edit KiCad schematic or PCB files until you identify the active project, task type, live project state, and validation requirements. For PCB/routing work, obey the routing rules: no 90-degree bends, no acute angles, no ugly zig-zag traces, no bad pad-entry geometry, and no fabrication outputs without human review. Summarize the current repo/project status and ask what task to run next.
```

Useful follow-up docs:

- [ONE_PROMPT_START.md](ONE_PROMPT_START.md)
- [DOWNLOAD_ZIP_START_HERE.md](DOWNLOAD_ZIP_START_HERE.md)
- [START_HERE.md](START_HERE.md)
- [CURRENT_STATUS.md](CURRENT_STATUS.md)
- [PROJECTS_INDEX.md](PROJECTS_INDEX.md)
- [WORKFLOWS_INDEX.md](WORKFLOWS_INDEX.md)
- [TOOLS_INDEX.md](TOOLS_INDEX.md)
- [03_TOOLS/TOOLS_INDEX.md](03_TOOLS/TOOLS_INDEX.md)
- [EXTERNAL_DEPENDENCIES.md](EXTERNAL_DEPENDENCIES.md)
- [LOCAL_SETUP_REQUIREMENTS.md](LOCAL_SETUP_REQUIREMENTS.md)
- [docs/HEALTH_CHECK.md](docs/HEALTH_CHECK.md)

## What KiCad Engine Is

KiCad Engine is an AI-agent rule and workflow engine for KiCad work.

- It helps Codex and Claude work in a predictable, auditable way.
- It gives AI agents project structure, task contracts, routing rules, DRC/ERC expectations, manufacturing checklists, and validation workflows.
- It is designed to work with the user's existing local KiCad installation.
- It supports project creation, review, cleanup, validation, documentation, and release-prep workflows around KiCad projects.
- It helps the AI agent operate inside a real repo instead of improvising from memory.

## What KiCad Engine Is Not

- It is not a replacement for KiCad.
- It is not an automatic perfect PCB designer.
- It is not a guarantee of fabrication-ready boards.
- It is not a cloud SaaS PCB tool.

## How It Works

- The AI agent reads `00_CODEX_START/` before doing project work.
- The AI agent follows task contracts so docs-only, audit-only, and edit-required work are separated clearly.
- The AI agent works inside `04_KICAD_PROJECTS/` for real project context.
- The AI agent uses tools in `03_TOOLS/` and workflows in `09_ACCURACY_ENGINE/` and `14_LAYOUT_AUTOMATION/`.
- The AI agent produces auditable changes, reports, DRC/ERC results, live-state summaries, and visual-review records instead of making silent broad edits.

## Project Workspace

`04_KICAD_PROJECTS/active`

- current working KiCad projects

`04_KICAD_PROJECTS/archive`

- older, reference, demo, or historical KiCad projects

`04_KICAD_PROJECTS/templates`

- starting templates for new projects

## Using Your Own KiCad Project

1. Create a new folder under `04_KICAD_PROJECTS/active`.
2. Put or create your KiCad project files there.
3. Ask Codex or Claude to read `00_CODEX_START/` and create, review, or organize the project.
4. Use the repo's workflow gates, routing rules, validation scripts, and report structure as the operating framework for that project.

## Routing Rules

- avoid 90-degree bends
- prefer 45-degree bends or smooth curves
- acute angles are not allowed
- no ugly zig-zag routing
- no bad pad-entry geometry
- no antenna keepout violations
- no blind autoroute without audit
- DRC quiet does not mean visually or professionally acceptable

## Manufacturing Support

KiCad Engine includes workflow support for manufacturing preparation and review around:

- JLCPCB
- PCBWay
- Gerbers
- drill files
- BOM
- CPL / pick-and-place

Fabrication outputs still require human review before anything is treated as order-ready.

## Repo Map

| Folder | Purpose |
| --- | --- |
| `00_CODEX_START` | AI startup instructions |
| `03_TOOLS` | scripts and tool helpers |
| `04_KICAD_PROJECTS` | KiCad project workspace |
| `09_ACCURACY_ENGINE` | validation and gates |
| `14_LAYOUT_AUTOMATION` | placement/routing logic |
| `24_FAB_PROFILES` | fab/export profiles |
| `34_PCB_LAYOUT_SANDBOX` | planning and variants |
| `docs` | user/developer docs |

## Current Example Project

The repo currently includes `ESP32_CSI_WIFI_NODE` as an active example workspace. It is there to demonstrate how KiCad Engine organizes and reviews a live project. It is not the identity of the repo, and it is not fabrication-ready unless that project's own reports say so.

## Requirements

Required:

- VS Code or equivalent editor
- Codex or Claude access
- KiCad installed locally for schematic/PCB GUI work

Recommended:

- Python
- Git

Optional:

- GitHub CLI
- Codespaces
- FreeRouting or KiBot if configured

## Safety Notice

Human KiCad review is required before ordering PCBs.
