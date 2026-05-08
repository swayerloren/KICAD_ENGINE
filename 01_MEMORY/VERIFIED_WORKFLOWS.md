# Verified Workflows

Repo-wide workflows that have been tested enough to reuse with reasonable confidence.

Do not add a workflow here because it sounds correct. Add it only after it has evidence in `02_HISTORY/workflow_runs/`, `02_HISTORY/command_logs/`, or a project `history/workflow_runs/` folder.

## Verification Levels

- `UNVERIFIED`: Planned but not tested.
- `SMOKE_TESTED`: Ran on a disposable or non-production example.
- `PROJECT_TESTED`: Ran on an approved project with backup and logs.
- `USER_CONFIRMED`: User confirmed the workflow result.

## Workflow Record Format

```text
ID:
Name:
Status:
Scope:
Inputs:
Outputs:
Safe boundaries:
Required prechecks:
Required postchecks:
Evidence:
Known limits:
```

## Current Verified Workflows

ID: `MCU_DATASHEET_TREE_STUB_GENERATION`
Name: Conservative microcontroller family datasheet-tree stub generation.
Status: `SMOKE_TESTED`
Scope: Global datasheet library tooling; ran against 48 MCU family/vendor folders under `06_DATASHEETS/01_MICROCONTROLLERS`.
Inputs: Vendor, family, representative part, and output folder values passed to `03_TOOLS/scripts/datasheet_tree/create_microcontroller_family_content.py`.
Outputs: AI-readable family overviews, part records, schematic notes, PCB layout notes, boot/debug notes, power/clock notes, package/footprint notes, source-link stubs, needs-review backlogs, generation JSON, summary, and audit report.
Safe boundaries: Offline only; no PDF downloads; no web scraping; no KiCad design file edits; no `--force`; `--overwrite-weak` replaces only obvious boilerplate placeholders.
Required prechecks: Read `AGENTS.md`, the generator, and the target datasheet tree; dry-run before write; use `UNKNOWN_REQUIRES_SOURCE` for unknowns.
Required postchecks: Run Python syntax validation, coverage check expected generated files, inspect remaining weak folders, and rebuild indexes.
Evidence: `02_HISTORY/workflow_runs/MCU_DATASHEET_TREE_STUB_GENERATION_WORKFLOW.md`; `02_HISTORY/design_reviews/MCU_DATASHEET_TREE_UPGRADE_REPORT.md`; `05_OUTPUTS/datasheet_tree/MCU_TREE_COMPLETION_SUMMARY.md`.
Known limits: Stub generation is not datasheet research, symbol approval, footprint approval, or schematic/PCB approval.

ID: `SCHEMATIC_ANNOTATION_COMPLETENESS_CHECKERS`
Name: Read-only schematic annotation, completeness, BOM-lock, and review-marker screening before PCB gate.
Status: `SMOKE_TESTED`
Scope: Global KiCad Engine tooling; tested against `ESP32_CSI_WIFI_NODE` schematic without editing KiCad design files.
Inputs: `.kicad_sch`, optional BOM lock/ready-parts file, optional project root.
Outputs: Markdown and JSON reports under a caller-selected report folder.
Safe boundaries: Read-only input parsing; writes only explicit report paths; no PCB update, routing, footprint assignment, or KiCad design-file modification.
Required prechecks: Confirm active project path if using project files; do not treat report output as engineering approval.
Required postchecks: Carry any `FAIL` into the schematic-to-PCB gate and project issue logs.
Evidence: `02_HISTORY/workflow_runs/SCHEMATIC_ANNOTATION_COMPLETENESS_CHECKER_SMOKE_TEST.md`; `02_HISTORY/command_logs/SCHEMATIC_ANNOTATION_COMPLETENESS_CHECKERS_COMMANDS.md`.
Known limits: Heuristic BOM parsing; no exact footprint, pinout, connector orientation, ERC/DRC, or fabrication approval.

ID: `SCHEMATIC_VISUAL_AUTOCROP`
Name: Read-only schematic full-page export and automatic close-up crop generation.
Status: `SMOKE_TESTED`
Scope: Global KiCad Engine visual verification tooling; tested against `ESP32_CSI_WIFI_NODE` without editing KiCad design files.
Inputs: `.kicad_sch`, installed `kicad-cli`, project visual block config or default generated config.
Outputs: Full-page SVG/PDF/PNG when renderer is available, crop SVG/PNG files, `reports/CLOSE_UP_REVIEW.md`, and JSON summary.
Safe boundaries: Read-only KiCad export; writes only `_verification/schematic_visual` and `reports/CLOSE_UP_REVIEW.md`; no GUI control and no KiCad source edits.
Required prechecks: Confirm project root and schematic path; do not use default block coordinates as proof of correct crop alignment.
Required postchecks: Carry any `FAIL`, `WARN`, or `VISUAL_REVIEW_INCOMPLETE` result into the schematic-to-PCB gate.
Evidence: `02_HISTORY/workflow_runs/SCHEMATIC_VISUAL_AUTOCROP_ACTIVE_PROJECT_SMOKE_TEST.md`; `02_HISTORY/command_logs/AUTOMATIC_SCHEMATIC_CLOSEUP_CROPS_COMMANDS.md`.
Known limits: SVG text parsing is not OCR; default normalized crops may need tuning; visual review does not prove ERC, DRC, footprint correctness, connector orientation, or fabrication readiness.

ID: `MEMORY_HISTORY_CURRENT_TRUTH_MAINTENANCE`
Name: Dry-run-first memory/history current-truth compilation.
Status: `PROJECT_TESTED`
Scope: Existing `01_MEMORY`, `02_HISTORY`, `09_ACCURACY_ENGINE`, and `ESP32_CSI_WIFI_NODE` project memory/history maintenance.
Inputs: Existing markdown memory/history/report files and project evidence paths.
Outputs: Project current-state, blocker, resolved-blocker, superseded-report, false-pass, next-phase, and project-memory index markdown files.
Safe boundaries: Default dry-run; `--apply` required for writes; writes only markdown/index/status files; never edits KiCad design files; never deletes history.
Required prechecks: Read memory/history maintenance rules and verify the active repo root.
Required postchecks: Syntax-check scripts, run dry-run, run apply, rebuild indexes, and confirm no `.kicad_*` files changed.
Evidence: `03_TOOLS/scripts/memory_maintenance/`; `05_OUTPUTS/release_readiness/MEMORY_HISTORY_MAINTENANCE_VALIDATION_REPORT.md`.
Known limits: The scanner is heuristic; unresolved dates and ambiguous false-pass records may require human review.

ID: `PCB_VISUAL_REVIEW_PACKET_FROM_LIVE_RENDERS`
Name: Fresh full-board PCB render plus deterministic crop review-packet generation.
Status: `PROJECT_TESTED`
Scope: `ESP32_CSI_WIFI_NODE` live-board visual review packaging without editing KiCad design files.
Inputs: Active-project `.kicad_pcb`, `kicad-cli pcb render`, fresh DRC run, and project review reports.
Outputs: Full-board top and bottom PNGs, region close-up PNGs, visual manifest markdown, LJ checklist markdown, and session/command closeout records.
Safe boundaries: Read-only KiCad render and DRC commands only; writes only image assets, markdown reports, and history/AI-quality records; no schematic, PCB, or manufacturing-output edits.
Required prechecks: Confirm active project path and live PCB hash; confirm the task is a review-packet task, not a fabrication-output task.
Required postchecks: Spot-check the generated crops, refresh live-state references, run a fresh DRC check, and explicitly separate packet readiness from board electrical completeness.
Evidence: `02_HISTORY/sessions/ESP32_CSI_WIFI_NODE_FINAL_PCB_VISUAL_REVIEW_PACKAGE_SESSION.md`; `02_HISTORY/command_logs/ESP32_CSI_WIFI_NODE_FINAL_PCB_VISUAL_REVIEW_PACKAGE_COMMANDS.md`; `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/_verification/pcb_visual/FINAL_PCB_REVIEW_PACKAGE.md`.
Known limits: Direct camera-pivot close-ups can misframe top-down review targets; deterministic crops from fresh full-board renders are safer for exact region review.
