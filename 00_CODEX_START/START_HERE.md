# Start Here

This is the first startup instruction file after the root `AGENTS.md`.

This repo is designed to be opened locally in VS Code after a normal `git clone` or GitHub `Download ZIP` extraction. The startup flow assumes the AI agent begins at the repo root and reads the local repo docs before touching KiCad files. Extra external GitHub repositories are optional helpers only; they are not required for first use unless a specific workflow explicitly calls for them.

## Required Startup Sequence
Codex and Claude must complete this production startup sequence before touching KiCad project files:

1. Read root `AGENTS.md`.
2. Read root `README_GPT.md`.
3. Read root `FOR CHAT GPT.MD`.
4. Read `00_CODEX_START/START_HERE.md`.
5. Read `00_CODEX_START/KICAD_PHASE_ORDER.md` for any KiCad project or pipeline work.
6. Read `00_CODEX_START/SESSION_START_CHECKLIST.md`.
7. Read `00_CODEX_START/STRUCTURE_STANDARD.md`.
8. Read `00_CODEX_START/FOLDER_ROUTING_RULES.md`.
9. Read `00_CODEX_START/PATH_PORTABILITY_RULES.md`.
10. Read `00_CODEX_START/CURRENT_KNOWN_PROBLEMS.md`.
11. Read `00_CODEX_START/MEMORY_INDEX.md`.
12. Read `00_CODEX_START/HISTORY_INDEX.md`.
13. Read `00_CODEX_START/PROMPT_COUNTER_RULES.md`.
14. If working on a project, read the active project memory and history before inspecting or editing project files.

Then read task-specific files such as `CONTROL_PLANES.md`, `TOOL_INDEX.md`, `PROJECT_INDEX.md`, `CURRENT_PROJECT.md`, accuracy-engine files, component-database files, library-factory rules, or installer/release docs as needed.

For active project work, check the project prompt counter before engineering work:

`python 03_TOOLS/scripts/memory_maintenance/check_maintenance_due.py --project <ACTIVE_PROJECT_PATH>`

If maintenance is due, block new engineering work until the maintenance cycle runs and the counter is reset:

`python 03_TOOLS/scripts/maintenance/run_maintenance_cycle.py --project <ACTIVE_PROJECT_PATH>`

Before meaningful work begins, declare exactly one task type using the execution-contract layer:

- `DOCS_ONLY`
- `AUDIT_ONLY`
- `LIVE_STATE_RECONCILE`
- `PLACEMENT_EDIT_REQUIRED`
- `ROUTING_EDIT_REQUIRED`
- `PCB_EDIT_REQUIRED`
- `GITHUB_DOCS_ONLY`

Execution-contract files:

- `03_TOOLS/scripts/execution_contract/README.md`
- `03_TOOLS/scripts/execution_contract/task_contract.schema.json`
- `03_TOOLS/scripts/execution_contract/validate_task_contract.py`
- `03_TOOLS/scripts/execution_contract/enforce_edit_required.py`

Live-state authority files:

- `03_TOOLS/scripts/project_state/live_state_authority.py`
- `03_TOOLS/scripts/project_state/validate_live_state_before_gate.py`
- `03_TOOLS/scripts/project_state/live_state_gate_wrapper.py`

If the task type is `PLACEMENT_EDIT_REQUIRED`, `ROUTING_EDIT_REQUIRED`, or `PCB_EDIT_REQUIRED`, the session must prove the required engineering artifact change before closeout or explicitly fail with `EDIT_REQUIRED_FAILED_NO_ENGINEERING_ARTIFACT_CHANGE`.

For supplier, distributor, stock, pricing, SKU, lifecycle, sourcing, or supplier datasheet-link work, also read:

- `../28_SUPPLIER_INGESTION/SOURCE_POLICY.md`
- `../28_SUPPLIER_INGESTION/API_KEY_HANDLING.md`
- `../28_SUPPLIER_INGESTION/SUPPLIER_CONNECTOR_STANDARD.md`
- The relevant connector folder under `../28_SUPPLIER_INGESTION/connectors/`

For installed KiCad footprint inventory, footprint gap, supplier SKU to footprint, package drawing, or footprint-confidence work, also read:

- `../29_FOOTPRINT_GAP_ANALYSIS/README.md`
- `../29_FOOTPRINT_GAP_ANALYSIS/INDEX.md`
- `../30_SUPPLIER_FOOTPRINT_MATCHES/README.md`
- `../30_SUPPLIER_FOOTPRINT_MATCHES/MATCH_SCHEMA.md`
- `../30_SUPPLIER_FOOTPRINT_MATCHES/MATCH_CONFIDENCE_RULES.md`
- `../30_SUPPLIER_FOOTPRINT_MATCHES/HUMAN_REVIEW_REQUIRED_RULES.md`

For Playwright-assisted supplier, datasheet, part-number, vendor, public KiCad library, or footprint-source research, also read:

- `../31_PLAYWRIGHT_RESEARCH_PIPELINE/SOURCE_POLICY.md`
- `../31_PLAYWRIGHT_RESEARCH_PIPELINE/TERMS_AND_RATE_LIMIT_RULES.md`
- `../31_PLAYWRIGHT_RESEARCH_PIPELINE/PLAYWRIGHT_USAGE_RULES.md`
- The relevant profile under `../31_PLAYWRIGHT_RESEARCH_PIPELINE/source_profiles/`

For open KiCad sample project discovery, intake, license screening, import, normalization, review, or benchmark promotion, also read:

- `../32_OPEN_KICAD_SAMPLE_INTAKE/README.md`
- `../32_OPEN_KICAD_SAMPLE_INTAKE/SOURCE_SELECTION_RULES.md`
- `../32_OPEN_KICAD_SAMPLE_INTAKE/LICENSE_SCREENING_RULES.md`
- `../32_OPEN_KICAD_SAMPLE_INTAKE/SAMPLE_IMPORT_WORKFLOW.md`
- `../32_OPEN_KICAD_SAMPLE_INTAKE/SAMPLE_REVIEW_WORKFLOW.md`
- `../32_OPEN_KICAD_SAMPLE_INTAKE/SAMPLE_PROMOTION_RULES.md`

For KiCad GUI/native schematic actions, annotation, GUI save, GUI ERC, Eeschema screenshots, or disputes between CLI/file evidence and what LJ sees in KiCad, also read:

- `../33_KICAD_GUI_AUTOMATION/README.md`
- `../33_KICAD_GUI_AUTOMATION/KICAD_GUI_AUTOMATION_RULES.md`
- `../33_KICAD_GUI_AUTOMATION/KICAD_WINDOW_STATE_RULES.md`
- `../33_KICAD_GUI_AUTOMATION/KICAD_NATIVE_ANNOTATION_WORKFLOW.md`
- `../33_KICAD_GUI_AUTOMATION/KICAD_NATIVE_ANNOTATION_SUCCESS_RECORD.md`
- `../33_KICAD_GUI_AUTOMATION/KICAD_ANNOTATION_DO_AND_DO_NOT.md`
- `../33_KICAD_GUI_AUTOMATION/KICAD_GUI_SAFETY_GATES.md`
- `../03_TOOLS/kicad/KICAD_NATIVE_ACTIONS_NOT_SUPPORTED_BY_CLI.md`

For KiCad project work that moves from schematic review into PCB update, placement, routing, verification, or NOT_FINAL fabrication export, also read:

- `KICAD_PIPELINE_STARTUP_RULES.md`
- `KICAD_PHASE_ORDER.md`
- `../34_PCB_LAYOUT_SANDBOX/README.md`
- `../34_PCB_LAYOUT_SANDBOX/PCB_LAYOUT_SANDBOX_RULES.md`
- `../34_PCB_LAYOUT_SANDBOX/PCB_VARIANT_WORKFLOW.md`
- `../34_PCB_LAYOUT_SANDBOX/PCB_WORK_AUTO_START_RULES.md`
- The active project's `reports/PCB_LAYOUT_SANDBOX_GATE_STATUS.md`
- `../09_ACCURACY_ENGINE/workflows/FULL_KICAD_PROJECT_PIPELINE.md`
- `../09_ACCURACY_ENGINE/workflows/AUTO_PCB_START_WORKFLOW.md`
- `../09_ACCURACY_ENGINE/workflows/MANDATORY_KICAD_PHASE_GATE.md`
- `../09_ACCURACY_ENGINE/checklists/AUTO_PCB_START_CHECKLIST.md`
- `../09_ACCURACY_ENGINE/checklists/FULL_PIPELINE_GATE_CHECKLIST.md`
- `../09_ACCURACY_ENGINE/checklists/PCB_PHASE_GATE_CHECKLIST.md`
- `../09_ACCURACY_ENGINE/verification_rules/NO_PHASE_SKIPPING_RULES.md`
- The matching prompt under `../.prompts/kicad_pipeline/`

Before starting the requested phase, run:

`python 03_TOOLS/scripts/project_state/validate_live_state_before_gate.py --project <ACTIVE_PROJECT_PATH>`

Then run:

`python 03_TOOLS/scripts/project_gate/check_phase_allowed.py --project <ACTIVE_PROJECT_PATH> --phase <PHASE>`

`LIVE_PROJECT_STATE.json` is the top authority for phase, placement, routing, and closeout status claims. Reports without source hashes are weak, and stale `NO_PCB`, `0 footprints`, or `no routing` claims cannot overrule live KiCad file evidence.

The phase checker now routes through the live-state authority wrapper, rebuilds or reads fresh `reports/LIVE_PROJECT_STATE.json`, reruns stale-report detection, and prints whether each blocker came from `LIVE_FILE_EVIDENCE`, `FRESH_GATE_REPORT`, `STALE_REPORT_IGNORED`, `TASK_CONTRACT_FAILURE`, or `HUMAN_REVIEW_REQUIRED`.

If the result is `BLOCKED`, stop and report the missing prerequisite. Do not create future-phase blocked review reports unless LJ specifically asked for a blocker audit.

## Session Rule
If the active project is `NONE`, Codex may organize instructions, memory, history, indexes, and workspace documentation, but must not edit KiCad project files.

## Path Portability Rule

Read `PATH_PORTABILITY_RULES.md` before resolving local paths. The current workspace path is `C:\Users\LJ\GitHub\KICAD_ENGINE`. Historical records may still mention an older non-GitHub checkout path; do not use older paths for edits or script writes unless the user explicitly directs work in that location and the path exists.

## Structure Routing Rule

Before creating, moving, or reorganizing repo files, Codex must read:

- `STRUCTURE_STANDARD.md`
- `FOLDER_ROUTING_RULES.md`
- `REPO_STRUCTURE_INDEX.md`

Use those files to choose the narrowest correct folder, preserve existing implementation roots such as `installer/`, `setup/`, and `docs/`, and avoid moving user work without an explicit migration task.

## Learning Loop Rule
At the end of every meaningful session, Codex must follow `SESSION_CLOSEOUT_CHECKLIST.md`.

Required closeout behavior:

1. Write a session log.
2. Write command logs if commands were run.
3. Write failed-attempt records if anything failed.
4. Write user-correction records if the user says something did not work, was wrong, or needs to be redone.
5. Create an AI self-review.
6. Create an AI response scorecard.
7. Create a claim/evidence matrix for major engineering claims.
8. Create an uncertainty log for anything not verified.
9. Create hallucination-risk log if any claim was guessed, inferred, or weakly sourced.
10. Create/update open issues for unresolved risks.
11. Update project memory only with durable project-specific lessons.
12. Update global memory only with reusable lessons.
13. Rebuild repository, memory, history, AI-quality, and known-problem indexes.
14. Rebuild `CURRENT_KNOWN_PROBLEMS.md`.
15. Update `FOR CHAT GPT.MD` if repo structure, workflow, tool status, active project status, known blockers, or scoring rules changed.

Primary indexing scripts:

- `03_TOOLS/scripts/indexing/build_repo_index.py`
- `03_TOOLS/scripts/indexing/build_memory_index.py`
- `03_TOOLS/scripts/indexing/build_history_index.py`
- `03_TOOLS/scripts/indexing/build_known_problems.py`

Prompt counter scripts:

- `03_TOOLS/scripts/memory_maintenance/increment_prompt_counter.py`
- `03_TOOLS/scripts/memory_maintenance/check_maintenance_due.py`
- `03_TOOLS/scripts/memory_maintenance/reset_prompt_counter_after_maintenance.py`
- `03_TOOLS/scripts/maintenance/run_maintenance_cycle.py`

## AI Quality Startup Rule

Before making KiCad engineering claims, read:

- `AI_SELF_REVIEW_RULES.md`
- `AI_TRUTHFULNESS_SCORING.md`
- `AI_HALLUCINATION_RISK_RULES.md`
- `AI_RESPONSE_QUALITY_GATE.md`
- `AI_EVIDENCE_REQUIREMENTS.md`
- `AI_UNCERTAINTY_DISCLOSURE_RULES.md`
- `AI_ENGINEERING_CLAIM_RULES.md`
- `AI_CLOSEOUT_SCORECARD_RULES.md`
- `CURRENT_KNOWN_PROBLEMS.md`
- `../26_AGENT_QUALITY/AI_SELF_REVIEW_RULES.md`
- `../26_AGENT_QUALITY/AI_TRUTHFULNESS_SCORING.md`
- `../26_AGENT_QUALITY/AI_HALLUCINATION_RISK_RULES.md`
- `../26_AGENT_QUALITY/AI_RESPONSE_QUALITY_GATE.md`
- `../26_AGENT_QUALITY/AI_EVIDENCE_REQUIREMENTS.md`

For every meaningful session that makes engineering claims, Codex/Claude must create:

- AI self-review.
- AI response scorecard.
- Claim/evidence matrix.
- Uncertainty log.

Create a hallucination-risk log when any claim was inferred, guessed, weakly sourced, or contradicted.

## Schematic To PCB Gate Rule

Before any PCB update from schematic, PCB creation, placement, routing, copper-zone work, or PCB manufacturing-style output, Codex/Claude must read:

- `../34_PCB_LAYOUT_SANDBOX/README.md`
- `../34_PCB_LAYOUT_SANDBOX/PCB_LAYOUT_SANDBOX_RULES.md`
- `../34_PCB_LAYOUT_SANDBOX/PCB_VARIANT_WORKFLOW.md`
- `../09_ACCURACY_ENGINE/workflows/SCHEMATIC_TO_PCB_GATE_WORKFLOW.md`
- `../09_ACCURACY_ENGINE/checklists/SCHEMATIC_READY_FOR_PCB_CHECKLIST.md`
- `../09_ACCURACY_ENGINE/checklists/PCB_UPDATE_FROM_SCHEMATIC_CHECKLIST.md`
- `../09_ACCURACY_ENGINE/verification_rules/SCHEMATIC_TO_PCB_BLOCKERS.md`
- `../09_ACCURACY_ENGINE/verification_rules/NEEDS_REVIEW_BLOCKER_RULES.md`
- The active project's `reports/SCHEMATIC_TO_PCB_GATE_STATUS.md`
- The active project's `reports/PCB_LAYOUT_SANDBOX_GATE_STATUS.md`

Agents must not update PCB from schematic, import schematic changes into PCB, place parts, route traces, create zones, or generate PCB manufacturing outputs unless the active project's `SCHEMATIC_TO_PCB_GATE_STATUS.md` exists and is exactly `PASS`, and the active project's `PCB_LAYOUT_SANDBOX_GATE_STATUS.md` exists and is exactly `PASS`.

If the sandbox status is `AUTO_APPROVED_FOR_PCB_WORK` and the `AUTO_PCB_START_WORKFLOW.md` preconditions pass, Codex/Claude may automatically continue only through PCB sync, real `.kicad_pcb` creation/update, board outline, fixed-mechanical placement, grouped placement, DRC, and placement visual evidence. If any auto-start precondition fails, stop with `AUTO_PCB_START_BLOCKED`.

Agents must not edit a real `.kicad_pcb` until an active-project sandbox report set exists with at least three variants, a variant scorecard, a selected layout plan, connector-orientation planning, antenna-keepout planning, board-shape/dimension planning, routing-feasibility evidence, and sandbox auto-approval status `AUTO_APPROVED_FOR_PCB_WORK`.

For `ESP32_CSI_WIFI_NODE`, the current gate file is `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/SCHEMATIC_TO_PCB_GATE_STATUS.md`.

## Native Annotation Rule

For schematic annotation tasks, Codex/Claude must use KiCad-native annotation through verified GUI automation or stop and instruct LJ to run KiCad's native annotation manually:

`Tools -> Annotate Schematic -> Re-annotate all symbols -> Save -> Run ERC`

Raw `.kicad_sch` text edits, regex scans, and saved-file reference tables are not sufficient proof that the KiCad GUI/native annotation state is clean. If Eeschema's title begins with `*`, treat it as `UNSAVED_GUI_STATE` and do not save or annotate through automation without explicit LJ approval and a backup.

The authoritative annotation gate requires all of these before annotation is considered clean:

1. KiCad native `Annotate Schematic` applied through verified GUI automation or LJ-confirmed manual action.
2. Schematic saved from KiCad GUI.
3. GUI ERC shows 0 violations when safely automatable.
4. `kicad-cli` ERC passes after GUI save.
5. Saved schematic scan shows 0 unresolved `?` references.
6. Duplicate-reference scan passes.

The 2026-05-06 `ESP32_CSI_WIFI_NODE` run is the current success model: `../33_KICAD_GUI_AUTOMATION/KICAD_NATIVE_ANNOTATION_SUCCESS_RECORD.md`. After native annotation passes, visual cleanup is allowed only as a separate task, and PCB update remains blocked until the full schematic-to-PCB gate is exactly `PASS`.

## Full KiCad Pipeline Rule

Future KiCad projects must follow the reusable 17-stage pipeline in `.prompts/kicad_pipeline/` and `../09_ACCURACY_ENGINE/workflows/FULL_KICAD_PROJECT_PIPELINE.md` unless the user explicitly approves an exception.

The mandatory phase order in `KICAD_PHASE_ORDER.md` is a hard gate on top of the 17-stage prompt pack. Missing `.kicad_pcb` blocks every phase after PCB creation/update. Missing `PCB_SYNC_STATUS.md`, DRC evidence, or no-unrouted-net proof blocks JLCPCB, production, export, upload feedback, and signoff tasks. Reports do not replace design artifacts or evidence.

Pipeline exceptions must be logged with:

- Affected gate number and name.
- User approval evidence.
- Reason for the exception.
- Risk classification.
- `HUMAN_REVIEW_REQUIRED`.
- Follow-up issue or blocker path.

Agents must not treat a later-stage report as permission to bypass an earlier gate. The stage result must match the exact required status in `../09_ACCURACY_ENGINE/checklists/FULL_PIPELINE_GATE_CHECKLIST.md`.

## Deferred Setup
Do not install tools, clone repositories, or configure MCP servers during startup.

## First Action Checklist
- Confirm the workspace root.
- Confirm the active project.
- Confirm the task mode.
- Confirm whether KiCad files are in scope.
- Confirm `CONTROL_PLANES.md` has been read before selecting tools.
- Confirm `STRUCTURE_STANDARD.md`, `FOLDER_ROUTING_RULES.md`, and `REPO_STRUCTURE_INDEX.md` have been read before changing repo structure.
- If KiCad files are in scope, verify that backups and a rollback plan exist before edits.
- If real PCB edits are in scope, verify that the PCB Layout Sandbox reports exist, that one selected variant is justified, that sandbox auto-approval status `AUTO_APPROVED_FOR_PCB_WORK` is recorded in `PCB_LAYOUT_SANDBOX_GATE_STATUS.md`, and that the `AUTO_PCB_START_WORKFLOW.md` preconditions pass before any real board edit starts.
- If PCB work is in scope, verify that both `SCHEMATIC_TO_PCB_GATE_STATUS.md` and `PCB_LAYOUT_SANDBOX_GATE_STATUS.md` are exactly `PASS` before any PCB update, placement, routing, zone, or manufacturing-output action.
- If KiCad pipeline work is in scope, choose the correct `.prompts/kicad_pipeline/NN_*.md` prompt and verify all earlier gates before acting.
- If supplier ingestion is in scope, use official APIs first, user-provided CSV exports second, and manual source-link records third. Do not scrape supplier websites or store credentials.
- If Playwright research is in scope, default to `DRY_RUN`, require explicit `--live` for browser execution, stop on login/CAPTCHA/blocking/unclear terms, and keep captured data `UNVERIFIED` until official-source or human review.
- If open KiCad sample intake is in scope, default scripts to `DRY_RUN`, record source URL/license/attribution before import, preserve `imported_originals` read-only, create a normalized copy before analysis or repair, and exclude samples from public payloads unless license status is `PUBLIC_BUNDLE_ALLOWED`.

# Platform Tool Roots

KiCad Engine now uses three tool/control roots under `03_TOOLS`:

1. `common`

   Purpose: OS-neutral KiCad project intelligence and deterministic automation.

   Use for:
   - `kicad-cli`
   - KiBot
   - `pcbnew` scripts
   - MCP analysis tools
   - BOM/Gerber/PNP parsers
   - File validators
   - InteractiveHtmlBom
   - PcbDraw
   - KiCanvas

2. `windows`

   Purpose: Windows desktop GUI hands/eyes for KiCad.

   Use for:
   - pywinauto
   - PyAutoGUI
   - OpenCV image matching
   - Screenshots
   - Window discovery
   - FlaUI/FlaUInspect
   - AutoHotkey
   - SikuliX

3. `linux`

   Purpose: Linux/headless/CI automation and repeatable validation.

   Use for:
   - Linux `kicad-cli`
   - KiBot
   - Xvfb
   - xdotool
   - wmctrl
   - ydotool
   - dogtail
   - Docker/headless validation

# Legacy Path Compatibility

The existing legacy paths remain valid until a separate migration is explicitly approved:

- `03_TOOLS\repos`
- `03_TOOLS\scripts`
- `03_TOOLS\python_envs`
- `03_TOOLS\node_envs`
- `03_TOOLS\tool_logs`

Do not move current repos or scripts unless a migration prompt specifically approves it.

# Tool Selection Rule

For any KiCad task, Codex must choose the safest control plane in this order:

1. Read-only file/project inspection.
2. Common project-intelligence tools:
   - `kicad-cli`
   - KiBot
   - `pcbnew`
   - MCP analysis tools
   - validators/parsers
3. Windows GUI discovery:
   - window listing
   - UI tree inspection
   - screenshots
4. Windows GUI control:
   - pywinauto
   - AutoHotkey
   - PyAutoGUI
   - SikuliX
5. Linux/headless validation:
   - Linux `kicad-cli`
   - KiBot
   - Xvfb
   - Docker
6. Design edits only after:
   - active project confirmed
   - backup completed
   - edit scope stated
   - rollback plan stated
   - verification plan stated

# GUI Automation Safety

Codex must not randomly click or type in KiCad.

Before any GUI control:

1. Confirm active project.
2. Confirm whether original or copied project is open.
3. Run window discovery.
4. Capture screenshot.
5. Prefer UIA/Win32 element-based control over coordinates.
6. If coordinate/image control is needed, verify window size, screenshot, target location, and risk.
7. Never use GUI automation on the original finished PCB folder.
8. Never save through GUI automation unless explicitly approved.
9. Log screenshots and actions.

# Linux / Headless Safety

Linux/headless scripts must:

- be read-only by default
- not use `sudo` inside scripts
- not delete project files
- not generate final manufacturing outputs unless verify-before-fab is explicitly approved
- write logs
- fail safely if tools are missing

# ChatGPT Handoff Maintenance Rule

Codex must update:

`FOR CHAT GPT.MD`

whenever any of the following changes:

- folder structure
- `AGENTS.md`
- `00_CODEX_START` files
- `README_GPT.md`
- memory system
- history system
- learning loop rules
- issue tracking rules
- user correction capture rules
- AI truthfulness/scoring rules
- AI quality gate rules
- current known problems
- tool repos
- installed tools
- MCP configuration
- verification scripts
- project templates
- active project index
- finished PCB reference library
- review workflow
- KiCad Engine health status
- known blockers
- setup readiness score

`FOR CHAT GPT.MD` must always include:

1. current repo purpose
2. current folder map
3. current tool status
4. current MCP status
5. current active project
6. current finished PCB reference projects
7. current warnings/blockers
8. latest important history files
9. exact instructions for ChatGPT/Codex before doing future work
10. path to `README_GPT.md` for full context

Codex must not leave `README_GPT.md` and `FOR CHAT GPT.MD` out of sync.

If Codex changes repo structure or workflows, it must update both files.

If Codex only changes a KiCad project but not the engine structure, it should update project memory/history and only update `FOR CHAT GPT.MD` if the change affects future ChatGPT context.
