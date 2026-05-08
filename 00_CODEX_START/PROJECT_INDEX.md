# Project Index

KiCad projects belong in:

`04_KICAD_PROJECTS\active`

Standard project templates belong in:

`04_KICAD_PROJECTS\templates`

## Current State
- No active project is selected unless `CURRENT_PROJECT.md` says otherwise.
- Do not edit KiCad project files when the active project is `NONE`.
- Standard project template system created on 2026-04-30.
- Final setup audit completed on 2026-04-30 with readiness score 88/100: `02_HISTORY\design_reviews\KICAD_ENGINE_FINAL_SETUP_AUDIT.md`.
- Real projects should be created only after requirements intake using `.codex\prompts\CREATE_REAL_KICAD_PROJECT_FROM_REQUIREMENTS.md`.
- Current checkout root is user-local and may vary by machine. Use repo-relative paths whenever possible, and use `00_CODEX_START\PATH_PORTABILITY_RULES.md` before acting on any absolute historical path.

## Project Record Fields
For each active project, record:
- Project name.
- Project path.
- Status.
- Board purpose.
- KiCad version.
- Important electrical constraints.
- Important mechanical constraints.
- Fabrication constraints.
- Related project memory file.
- Latest review or verification report.

## Project Work Rule
Before touching project files:

1. Confirm the target path is inside the active project path listed in `CURRENT_PROJECT.md`.
2. Read the active project's `memory/` folder for durable decisions, component decisions, footprint decisions, datasheet decisions, user corrections, agent mistakes, open design risks, and project quality gates.
3. Read the active project's `history/` folder for recent sessions, command logs, failed attempts, issue logs, verification runs, user corrections, AI self-reviews, scorecards, claim/evidence matrices, uncertainty logs, hallucination-risk logs, and quality-gate failures.
4. Create or confirm a backup before KiCad project edits.
5. Keep new project-specific lessons in project memory/history unless they are reusable across projects.

## Standard Template System
- Standard template folder: `04_KICAD_PROJECTS\templates\STANDARD_KICAD_PROJECT_TEMPLATE`
- README template: `04_KICAD_PROJECTS\templates\STANDARD_PROJECT_README_TEMPLATE.md`
- AGENTS template: `04_KICAD_PROJECTS\templates\STANDARD_PROJECT_AGENTS_TEMPLATE.md`
- Creation guide: `04_KICAD_PROJECTS\templates\PROJECT_CREATION_GUIDE.md`
- Real project requirements template: `04_KICAD_PROJECTS\templates\REAL_PROJECT_REQUIREMENTS_TEMPLATE.md`
- Finished PCB review checklist: `04_KICAD_PROJECTS\templates\FINISHED_PCB_REVIEW_CHECKLIST.md`
- Reference project folder standard: `04_KICAD_PROJECTS\templates\REFERENCE_PROJECT_FOLDER_STANDARD.md`
- Real project intake prompt: `.codex\prompts\CREATE_REAL_KICAD_PROJECT_FROM_REQUIREMENTS.md`
- Creation script: `03_TOOLS\scripts\new_kicad_project_workspace.ps1`
- Script behavior: creates projects under `04_KICAD_PROJECTS\active`, creates project memory/history folders, updates this index, and does not update `CURRENT_PROJECT.md`.

## Finished PCB Reference Library

Finished PCB references may exist in a user-local folder:

`99_01 Finished PCBs`

This folder is not present in every checkout. If it is missing, treat finished PCB references as historical records only. Do not edit finished PCB source files, manufacturing outputs, backups, PDFs, STL files, BOMs, or pick-and-place files directly. If edits or experiments are needed, copy the reference into an approved review workspace first.

### Finished Reference: COMMAND LINK

- Reference path: `99_01 Finished PCBs\COMMAND LINK`
- Status: FINISHED_FIVERR_VERIFIED_REFERENCE_INDEXED_READ_ONLY
- Indexed: 2026-04-30
- Source files observed: `COMMAND LINK DRAFT.kicad_pro`, `COMMAND LINK DRAFT.kicad_sch`, `COMMAND LINK DRAFT.kicad_pcb`, `COMMAND LINK DRAFT.kicad_prl`
- Output/reference files observed: `COMMAND LINK BOM.csv`, `COMMAND LINK DRAFT.pdf`, `COMMAND LINK DRAFT.stl`, `Fabrication files`, `Fabrication files.zip`, `pick and place file`, `pick and place file.zip`
- Backup/cache files observed: `COMMAND LINK DRAFT.kicad_sch-bak`, `COMMAND LINK DRAFT-backups`, `fp-info-cache`
- Inventory report: `02_HISTORY\design_reviews\COMMAND_LINK_FINISHED_PCB_INVENTORY.md`
- Review rule: create reports only unless LJ explicitly requests a copied review workspace.
- Review copy: `04_KICAD_PROJECTS\active\COMMAND_LINK_VERIFIED_REFERENCE`
- Review copy status: COPIED_REFERENCE_READ_ONLY_NOT_ACTIVE_REVISION

## Project: SAMPLE_KICAD_TEST_PROJECT
- Project path: `04_KICAD_PROJECTS\archive\SAMPLE_KICAD_TEST_PROJECT`
- Status: ARCHIVED_SAMPLE_PIPELINE_TEST_COMPLETE_NOT_FAB_READY
- Board purpose: Harmless sample/test project for verification script pipeline testing.
- KiCad version: 9.0.7 sample fixture.
- Important electrical constraints: None; not a production design.
- Important mechanical constraints: None; not a production design.
- Fabrication constraints: Do not fabricate; outputs are not final.
- Related project memory file: `01_MEMORY\projects\SAMPLE_KICAD_TEST_PROJECT\PROJECT_MEMORY.md`
- Latest review or verification report: `02_HISTORY\erc_drc_reports\SAMPLE_KICAD_TEST_PROJECT_VERIFICATION.md`
- Project history folder: `02_HISTORY\project_history\SAMPLE_KICAD_TEST_PROJECT`

## Project: CLEAN_KICAD_PASSING_SAMPLE
- Project path: `04_KICAD_PROJECTS\archive\CLEAN_KICAD_PASSING_SAMPLE`
- Status: ARCHIVED_SAMPLE_SUCCESS_PATH_VALIDATED_NOT_FAB_READY
- Board purpose: Disposable clean KiCad sample used to validate the successful verification pipeline path.
- KiCad version: 9.0 installed demo fixture `test_pads_inside_pads`.
- Important electrical constraints: Not a production design; ERC passed with 0 messages, 0 errors, and 0 warnings.
- Important mechanical constraints: Not a production design; DRC passed with 0 violations, 0 unconnected pads, and 0 footprint errors.
- Fabrication constraints: Do not fabricate; generated Gerber, drill, and STEP outputs are automation test artifacts in `NOT_FINAL` folders.
- Related project memory file: `01_MEMORY\projects\CLEAN_KICAD_PASSING_SAMPLE\PROJECT_MEMORY.md`
- Latest review or verification report: `02_HISTORY\erc_drc_reports\CLEAN_KICAD_PASSING_SAMPLE_VERIFICATION.md`
- Project history folder: `02_HISTORY\project_history\CLEAN_KICAD_PASSING_SAMPLE`

## Project: COMMAND_LINK_VERIFIED_REFERENCE
- Project path: `04_KICAD_PROJECTS\active\COMMAND_LINK_VERIFIED_REFERENCE`
- Status: COPIED_FINISHED_REFERENCE_READ_ONLY_NOT_FAB_READY
- Board purpose: Review and learning copy of the finished Fiverr-verified `COMMAND LINK` PCB reference.
- KiCad version: Source files copied from `99_01 Finished PCBs\COMMAND LINK`; do not edit originals.
- Important electrical constraints: Preserve as reference until reviewed; no design changes in this copy.
- Important mechanical constraints: Preserve as reference until reviewed; PDF/STL copied from source.
- Fabrication constraints: Do not fabricate from this copy; copied fabrication outputs are reference artifacts only.
- Related project memory file: `01_MEMORY\projects\COMMAND_LINK_VERIFIED_REFERENCE\PROJECT_MEMORY.md`
- Latest review or verification report: `02_HISTORY\design_reviews\COMMAND_LINK_READ_ONLY_REVIEW.md`
- Project history folder: `02_HISTORY\project_history\COMMAND_LINK_VERIFIED_REFERENCE`
- Source finished reference: `99_01 Finished PCBs\COMMAND LINK`
- Local project AGENTS: `04_KICAD_PROJECTS\active\COMMAND_LINK_VERIFIED_REFERENCE\AGENTS.md`
- Latest ERC/DRC report: `02_HISTORY\erc_drc_reports\COMMAND_LINK_ERC_DRC_REVIEW.md`

## Project: ESP32_CSI_WIFI_NODE
- Project path: `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE`
- Status: ACTIVE_DESIGN_PROJECT_LIVE_PCB_EXISTS_PARTIAL_ROUTING_BLOCKED
- Board purpose: Complete custom compact ESP32-S3 CSI WiFi sensing/experimentation node PCB; not a carrier board and not a development-board plug-in PCB.
- KiCad version: KiCad 9.0.7 project with live schematic and PCB artifacts present.
- Important electrical constraints: External certified 5 V DC wall supply; 5.5 mm x 2.1 mm center-positive barrel jack; input fuse/polyfuse; reverse-polarity protection; 5 V TVS; bulk input capacitor; 3.3 V regulator; ESP32-S3-WROOM-1U module; USB-C programming/debug; USB ESD; BOOT and RESET/EN buttons; power/status indication; 5 V/3.3 V/GND test pads; no 120 VAC.
- Important mechanical constraints: Compact rectangular board; four mounting holes near corners; barrel jack and USB-C face enclosure wall; external antenna pigtail/SMA clearance for 3D printed enclosure.
- Fabrication constraints: Active design only, not fab-ready; live PCB exists with `60 mm x 95 mm` outline, `43` footprints, and partial Stage 1/2 routing, but routing remains blocked by formal gate failure, `12` `U2 pad 41` drill-rule violations, `65` unconnected items, and `16` detectable unrouted nets. Outputs remain `NOT_FINAL`.
- Related project memory file: `01_MEMORY\projects\ESP32_CSI_WIFI_NODE\PROJECT_MEMORY.md`
- Latest review or verification report: `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\LIVE_PCB_TRUTH_AUDIT.md`
- Project history folder: `02_HISTORY\project_history\ESP32_CSI_WIFI_NODE`
