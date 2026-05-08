# KiCad Engine Architecture

Date: 2026-05-02

## Architecture Goal

KiCad Engine is a repo-structured control layer around the user's installed KiCad application. It gives AI coding agents a predictable way to inspect, reason about, automate, verify, and document KiCad work while preserving KiCad as the canonical design tool.

The architecture is local-first, CLI/API-first, evidence-driven, and safe by default.

## Repo Control Plane

The repo itself is the first control plane. It tells agents what they may read, what they may edit, where outputs go, and what gates must pass before any KiCad design or fabrication claim is trusted.

Primary areas:

- `AGENTS.md`: root operating rules for AI agents.
- `00_CODEX_START`: startup files, control-plane definitions, indexes, active project pointer, product vision, and architecture.
- `01_MEMORY`: durable design decisions, preferences, and constraints.
- `02_HISTORY`: session logs, command logs, reviews, ERC/DRC reports, fabrication reviews, and product audits.
- `03_TOOLS`: scripts, tool docs, local tool repos, isolated environments, tool logs, and platform-specific automation roots.
- `04_KICAD_PROJECTS`: active projects, templates, archived samples, and project-local docs.
- `05_OUTPUTS`: generated reports and review/export outputs.
- `06_DATASHEETS`: component datasheets and reference documents.
- `99_BACKUPS`: backups before automated edits.

The repo control plane should remain plain text where possible so Codex, Claude, and other agents can consume it without proprietary integrations.

## KiCad App Integration

KiCad Engine uses the user's installed KiCad app. It should not modify KiCad installation files.

Integration points:

- `kicad-cli` for ERC, DRC, exports, and deterministic command-line workflows.
- KiCad Python and `pcbnew` APIs for board inspection, validation, and controlled automation where available.
- KiBot for repeatable project checks, exports, and release automation.
- KiCad source files as canonical project state, stored under the active project path.
- KiCad GUI discovery only when the CLI/API layer cannot answer a needed question.

The engine must record the KiCad version used for checks because KiCad file formats, library behavior, ERC/DRC rules, and exporters can drift between versions.

## CLI/API First Approach

Default order:

1. Read-only file inspection.
2. Local deterministic tools such as `kicad-cli`, KiBot, `pcbnew`, parsers, and validators.
3. MCP analysis tools in safe/read-only profiles.
4. Windows GUI discovery and screenshots.
5. Windows GUI control only after explicit approval and discovery evidence.
6. Linux/headless/CI workflows only in an explicitly selected environment.

CLI/API-first workflows are preferred because they are repeatable, scriptable, logged, and less likely to corrupt project state than GUI automation.

## Safe GUI Discovery

GUI tooling is a secondary control plane for cases where KiCad's visual state matters or when the CLI/API cannot expose the needed information.

Allowed discovery actions:

- List KiCad processes and windows.
- Confirm process names such as `kicad.exe`, `eeschema.exe`, and `pcbnew.exe`.
- Capture screenshots.
- Inspect UIA/Win32 trees where useful.
- Save logs and screenshots under `03_TOOLS/windows/logs`.

Restricted by default:

- No random clicks.
- No random typing.
- No coordinate control without current screenshots and window-size verification.
- No hotkeys, saves, closes, or project modifications without explicit approval.
- No GUI control against production project sources until active project and backup gates are complete.

## Datasheet Database

Current state: `06_DATASHEETS` stores datasheet PDFs and reference documents. It does not yet provide a full datasheet database.

Target architecture:

- A manifest for each datasheet with manufacturer, part number, document title, revision, publication date when known, source URL, access date, local path, and copyright/license notes.
- Mapping from project components to datasheet records.
- Extracted requirement facts with source references, such as voltage limits, package dimensions, recommended circuits, thermal data, pin descriptions, antenna clearances, and layout requirements.
- Review status fields: unreviewed, reviewed, project-approved, obsolete, superseded, or blocked.
- No blind redistribution of copyrighted datasheets in public releases unless licensing is clear.

The datasheet database should support evidence-backed AI review, not free-form assumptions.

## Component Database

Target component records should include:

- Manufacturer and manufacturer part number.
- Lifecycle and sourcing status.
- Preferred distributor links or internal sourcing notes.
- Electrical limits and operating conditions.
- Package and footprint candidates.
- Symbol candidate.
- Verified symbol-footprint-pin mapping status.
- Datasheet record linkage.
- Known alternates and substitutes.
- Avoid/approved status and reason.
- Project usage history.

The component database should distinguish observed parts from approved preferred parts. A part seen in a reference design is not automatically a verified part.

## Symbol And Footprint Knowledge

KiCad Engine needs a durable knowledge layer for symbols and footprints because AI PCB errors often happen at this boundary.

Required knowledge:

- Symbol name and library origin.
- Footprint name and library origin.
- Pin mapping between symbol pins, footprint pads, and datasheet pins.
- Pin 1, polarity, and orientation evidence.
- Package dimensions, courtyard, paste, mask, drill, and assembly assumptions.
- 3D model availability.
- Connector mating part, keying, cable orientation, and board-edge orientation.
- Review status and reviewer/date.

The engine should support statuses such as `UNVERIFIED`, `DATASHEET_MATCHED`, `FOOTPRINT_GEOMETRY_VERIFIED`, `PIN_MAPPING_VERIFIED`, `PROJECT_APPROVED`, and `DO_NOT_USE`.

## Project Templates

Project templates under `04_KICAD_PROJECTS/templates` define safe defaults for new workspaces.

Expected project structure:

- `kicad`: KiCad source files.
- `datasheets`: project-local datasheet copies or references.
- `bom`: BOM outputs and BOM review artifacts.
- `fabrication`: fabrication exports, marked not final unless verified.
- `renders`: visual renders and screenshots.
- `reports`: ERC, DRC, reviews, and release notes.
- `notes`: working engineering notes.
- `scripts`: project-local scripts only when needed.
- `memory`: project-local durable context.
- `history`: project-local session and command history.

Templates should remain conservative and should not create real schematic or PCB source files until the user confirms requirements and edit gates.

## Verification Scripts

Existing verification scripts live under `03_TOOLS/scripts`.

Current script roles:

- `find_kicad_project_files.ps1`: project inventory.
- `backup_kicad_project.ps1`: pre-edit backups.
- `run_erc.ps1`: schematic ERC.
- `run_drc.ps1`: PCB DRC.
- `export_bom.ps1`: BOM export.
- `export_gerbers.ps1`: Gerber export into review folders.
- `export_drill.ps1`: drill export into review folders.
- `export_step.ps1`: STEP export into review folders.
- `full_verify_project.ps1`: gated verification pipeline.
- `kicad_engine_health_check.ps1`: workspace health check.
- `new_kicad_project_workspace.ps1`: standard project workspace creation.

Target improvements:

- Machine-readable report manifests.
- Stable exit-code contract.
- Regression fixtures for pass, fail, and blocked cases.
- Explicit KiCad version capture in every report.
- Component, datasheet, footprint, and connector review gates in addition to ERC/DRC.
- Public CI-safe checks that do not require private designs or checked-in virtual environments.

## Release Installer Plan

Current state: no top-level setup, installer, or release folder exists. `05_OUTPUTS/release_packages` exists as an output location, but there is no public installer or release workflow yet.

Target plan:

1. Keep the public repo source-only by default. Do not check in local virtual environments, downloaded package caches, or cloned third-party repos as the normal release mechanism.
2. Provide a dry-run setup checker that detects KiCad, `kicad-cli`, Python, Node, Git, and optional tools without installing anything.
3. Provide optional, clearly separated install scripts for Windows and Linux that require explicit user action.
4. Keep tool installs isolated under `03_TOOLS/python_envs` and `03_TOOLS/node_envs`.
5. Provide a release packaging script that creates a local archive without secrets, private projects, copyrighted datasheets without permission, or generated final fabrication outputs.
6. Add a public sample project and validation command set.
7. Add versioned release notes and a public compatibility matrix for KiCad versions.

The installer should bootstrap the engine around the user's installed KiCad app, not install or replace KiCad unless a future separate installer explicitly supports that.

## AI-Agent Prompt System

Current prompt system:

- `.codex/prompts` contains Codex-oriented startup, project creation, review, install, and verify-before-fab prompts.
- `AGENTS.md` and `00_CODEX_START` define mandatory behavior for Codex and similar agents.
- `README_GPT.md` and `FOR CHAT GPT.MD` provide longer and shorter handoff context.

Target prompt system:

- Agent-neutral prompt contracts for Codex, Claude, and similar VS Code-based agents.
- Optional `.claude` and `.vscode` integration files when they are intentionally added.
- Prompt templates for review-only work, proposed edits, backup creation, ERC/DRC, BOM review, footprint review, datasheet review, release audit, and issue triage.
- A clear authority model for read-only, propose-only, edit-with-backup, and release-review modes.
- Test prompts against sample projects to verify agents refuse unsafe edits and preserve `NOT_FINAL` output labels.

## Data Flow

Normal safe flow:

1. Agent reads `AGENTS.md` and startup files.
2. Agent confirms active project and task mode.
3. Agent reads relevant memory and history.
4. Agent inventories project files without editing.
5. Agent creates or confirms backups before protected edits.
6. Agent performs requested planning, review, or edits within the active project boundary.
7. Agent runs appropriate ERC, DRC, BOM, footprint, datasheet, connector, and visual checks.
8. Agent writes reports to history and outputs to approved folders.
9. Agent leaves manufacturing-style outputs marked `NOT_FINAL` until the full verification gate passes.

## Authority Model

- Read-only: inspection, summaries, reports, and planning.
- Propose-only: patch plans, review comments, and change recommendations without modifying protected files.
- Edit-with-backup: protected file edits only after active project, backup, verification plan, and rollback plan are confirmed.
- Output-review: generated BOM, Gerber, drill, STEP, PDF, SVG, and review files marked `NOT_FINAL`.
- Release-candidate: all automated checks pass and human review items are explicitly tracked.
- Final-release: only after required human confirmation and full verification evidence.

By default, agents operate at read-only or documentation authority until the user explicitly requests a higher-authority action.
