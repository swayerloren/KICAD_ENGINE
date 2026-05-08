# Current Status

## Repo Identity

- Repo name: `KiCad Engine`
- Repo role: general AI-assisted KiCad workflow engine
- Main use: local VS Code + Codex or Claude + local KiCad
- Repo status: `PRIVATE / EXPERIMENTAL / NOT_PUBLIC_RELEASE_READY`

This repo is not only the `ESP32_CSI_WIFI_NODE` board. That project is just the current example/current active project inside the larger KiCad Engine workspace.

## Workspace Model

- `04_KICAD_PROJECTS/active` is for current working KiCad projects
- `04_KICAD_PROJECTS/archive` is for older, reference, or historical projects
- `04_KICAD_PROJECTS/templates` is for new-project starting points
- `03_TOOLS` contains scripts and helpers used by the workflow engine
- `00_CODEX_START` contains the startup rules the AI agent should read first

## Repo Capability Snapshot

- ZIP-download and local-clone onboarding docs exist
- one-prompt startup docs exist
- KiCad discovery and health-check scripts exist
- task-contract, live-state, and validation workflows are included
- routing rules and manufacturing-review workflows are included

## Current Example Project

- Current active example project: `ESP32_CSI_WIFI_NODE`
- Path: `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE`
- Role in repo: current example/work-in-progress project only
- Fabrication-ready: `NO`

Current example-project notes:

- a live PCB exists
- placement exists
- partial routing exists
- unresolved connectivity and review work remain
- human KiCad review is still required before fabrication-style claims

## Current Repo Limitations

- KiCad Engine is not a replacement for KiCad
- it does not guarantee perfect schematic or PCB results
- fabrication outputs still require human review
- optional helper tools may exist, but they are not required for the baseline ZIP -> VS Code -> prompt workflow

## Recommended Start

If you are new to the repo:

1. Read [README.md](README.md).
2. Read [ONE_PROMPT_START.md](ONE_PROMPT_START.md) if present.
3. Read [WORKFLOWS_INDEX.md](WORKFLOWS_INDEX.md) and [TOOLS_INDEX.md](TOOLS_INDEX.md).
4. Use the current active project as an example, or create your own project under `04_KICAD_PROJECTS/active`.
