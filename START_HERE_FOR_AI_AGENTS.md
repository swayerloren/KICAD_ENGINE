# Start Here For AI Agents

This is the short first-read routing file for Codex, Claude, and similar agents working in `KICAD_ENGINE`.

This file does not replace `AGENTS.md`. It routes agents to the right deeper rules so future prompts do not need to list every `READ FIRST` file.

The old `knowledge_scrape/` source folder has been retired and removed from the
live repo workflow. If it appears in older records, treat it as migration
history only, not as a routing destination.

Future prompts may simply say:

`Read START_HERE_FOR_AI_AGENTS.md and route yourself to the correct project/task files.`

The agent must then follow `AGENTS.md`, use `00_CODEX_START/TASK_ROUTER.md`, and read the task-specific files required for the current work.

## Mandatory Minimal Startup

Read these first:

1. `START_HERE_FOR_AI_AGENTS.md`
2. `AGENTS.md`
3. `FOR CHAT GPT.MD`
4. `00_CODEX_START/AI_AGENT_FAST_CONTEXT.md`
5. `00_CODEX_START/TASK_ROUTER.md`

Then follow `AGENTS.md` for the full startup chain before touching KiCad project files or making engineering claims.

Also read `.prompts/README.md` and the task-specific prompt from `.prompts/codex` or `.prompts/claude` when the user is using the prompt pack.

## Hard Rule

If a user prompt asks for schematic, PCB, fabrication, memory/history, or
open-source tool work and does not list read-first files, Codex must use
`00_CODEX_START/TASK_ROUTER.md` to determine the required docs automatically.

Do not ask the user for a longer startup list when the router can derive the correct one.

## Router Files

Use these files together:

- `00_CODEX_START/TASK_ROUTER.md`
- `00_CODEX_START/TASK_TYPE_TO_REQUIRED_DOCS.md`
- `00_CODEX_START/TASK_TYPE_TO_ALLOWED_ACTIONS.md`
- `00_CODEX_START/TASK_TYPE_TO_BLOCKERS.md`
- `00_CODEX_START/TASK_TYPE_TO_OUTPUTS.md`
- `00_CODEX_START/TASK_TYPE_TO_KNOWLEDGE_MAP.md`
- `00_CODEX_START/TASK_TYPE_TO_TOOL_MAP.md`
- `00_CODEX_START/TASK_TYPE_TO_RULE_MAP.md`
- `00_CODEX_START/KICAD_ENGINE_CRITICAL_PATH.md`
- `00_CODEX_START/AI_AGENT_FAST_CONTEXT.md`

## Supported Routes

The router currently covers:

- `SCHEMATIC_CREATE_OR_REPAIR`
- `SCHEMATIC_VISUAL_CLEANUP`
- `NATIVE_ANNOTATION`
- `FOOTPRINT_PACKAGE_GATE`
- `PCB_UPDATE_FROM_SCHEMATIC`
- `PCB_PRELAYOUT_VARIANT_PLANNING`
- `PCB_PLACEMENT`
- `CONNECTOR_ORIENTATION_AUDIT`
- `PCB_ROUTING`
- `TRACE_GEOMETRY_AUDIT`
- `PCB_COPPER_ZONES`
- `FAB_EXPORT`
- `MEMORY_MAINTENANCE`
- `OPEN_SOURCE_TOOL_USE`

`OPEN_SOURCE_TOOL_USE` routes directly into
`03_TOOLS/open_source_integrations/` for optional-tool registry, install
policy, portability policy, attribution rules, and dry-run verification
wrappers.

Open-source KiCad sample-intake and reference-learning work must now also use:

- `32_OPEN_KICAD_SAMPLE_INTAKE/README.md`
- `32_OPEN_KICAD_SAMPLE_INTAKE/SAMPLE_INTAKE_WORKFLOW.md`
- `32_OPEN_KICAD_SAMPLE_INTAKE/SAMPLE_LICENSE_RULES.md`
- `32_OPEN_KICAD_SAMPLE_INTAKE/SAMPLE_NORMALIZATION_RULES.md`
- `32_OPEN_KICAD_SAMPLE_INTAKE/SAMPLE_QUALITY_SCORECARD.md`
- `32_OPEN_KICAD_SAMPLE_INTAKE/SAMPLE_DO_NOT_COPY_RULES.md`
- `07_REFERENCE_DESIGNS/README.md`
- `07_REFERENCE_DESIGNS/SCHEMATIC_STYLE_EXAMPLES.md`
- `07_REFERENCE_DESIGNS/PCB_LAYOUT_STYLE_EXAMPLES.md`
- `03_TOOLS/scripts/sample_intake/`

Schematic-create, schematic-visual-cleanup, and schematic-to-PCB-readiness work
must now also use `34_SCHEMATIC_QUALITY_ENGINE/` plus
`03_TOOLS/scripts/schematic_quality/`.

Schematic-create and schematic-visual-cleanup work must now also use:

- `34_SCHEMATIC_QUALITY_ENGINE/SCHEMATIC_LAYOUT_ALGORITHM.md`
- `34_SCHEMATIC_QUALITY_ENGINE/FUNCTIONAL_BLOCK_TEMPLATES.md`
- `34_SCHEMATIC_QUALITY_ENGINE/LOCAL_WIRING_STYLE_GUIDE.md`
- `34_SCHEMATIC_QUALITY_ENGINE/VISUAL_READABILITY_SCORECARD.md`
- `03_TOOLS/scripts/schematic_layout/`

Native-annotation work must now also use:

- `33_KICAD_GUI_AUTOMATION/KICAD_AUTO_OPEN_PROJECT_WORKFLOW.md`
- `33_KICAD_GUI_AUTOMATION/KICAD_ANNOTATION_DO_AND_DO_NOT.md`
- `33_KICAD_GUI_AUTOMATION/KICAD_GUI_ACTION_MATRIX.md`
- `33_KICAD_GUI_AUTOMATION/scripts/windows/run_native_annotation_workflow.py`

Footprint/package gate work must now also use:

- `35_FOOTPRINT_PACKAGE_ENGINE/`
- `03_TOOLS/scripts/footprint_package/`
- active project `FOOTPRINT_LOCK.csv`
- `04_KICAD_PROJECTS/_templates/FOOTPRINT_LOCK_TEMPLATE.csv`

Real routed-board acceptance now also uses:

- `03_TOOLS/scripts/pcb_quality/`
- active project `reports/pcb_quality_gate/`
- the latest `PCB_QUALITY_GATE_REPORT.md`

Calculator and automation-result work must now also use:

- `10_KNOWLEDGE_BASE/calculators/`
- `03_TOOLS/calculators/`
- `09_ACCURACY_ENGINE/workflows/EDA_AUTOMATION_VERIFICATION_WORKFLOW.md`
- `09_ACCURACY_ENGINE/verification_rules/CALCULATOR_RESULT_EVIDENCE_RULES.md`
- `09_ACCURACY_ENGINE/verification_rules/AUTOMATION_TOOL_RESULT_VALIDATION_RULES.md`

Use the canonical startup maps, calculator surfaces, and automation-validation
files above as the normal routing path.

## Active Project Rule

For any project task:

1. Identify the active project from `00_CODEX_START\CURRENT_PROJECT.md`.
2. Read the active project memory.
3. Read active project `CURRENT_PROJECT_STATE.md` if present.
4. Read active project `CURRENT_BLOCKERS.md` if present.
5. Read active project `NEXT_ALLOWED_PHASE.md` if present.
6. Read active project reports relevant to the task.

Do not edit KiCad project files unless `AGENTS.md` edit gates are satisfied, the active project is confirmed, and the backup plan is confirmed. For real PCB edits, sandbox planning, prelayout gate evidence, and selected-variant justification must also be confirmed.

## Phase Gate Rule

Before any PCB pipeline phase, run or check:

`python 03_TOOLS\scripts\project_gate\check_phase_allowed.py --project <ACTIVE_PROJECT_PATH> --phase <PHASE>`

If the checker or evidence says `BLOCKED`, stop. Report the requested phase, blocking earlier phase, missing evidence, and next allowed phase. Do not create downstream blocked review reports unless LJ specifically asks for a blocker audit.

## Prelayout Gate Rule

Before real PCB placement or routing, run or review:

`python 03_TOOLS\scripts\pcb_prelayout\run_prelayout_gate.py --project <ACTIVE_PROJECT_PATH>`

Real PCB placement is blocked until the latest `reports\prelayout_engine\*\prelayout_gate_result.json` shows:

- `variant_count >= 3`
- `passing_variant_count >= 1`
- `placement_gate_status = PASS`

Real PCB routing is additionally blocked until the latest prelayout result also shows:

- `routing_gate_status = PASS`

After routing exists, final routing acceptance is additionally blocked until:

- `python 03_TOOLS/scripts/pcb_quality/run_pcb_quality_gate.py --project <ACTIVE_PROJECT_PATH>` returns `PASS_FINAL_ROUTING`

## Prompt Counter Rule

Before meaningful active-project repo work:

1. Increment the active project prompt counter.
2. Check whether maintenance is due.
3. If maintenance is due, run maintenance before engineering work:

`python 03_TOOLS\scripts\maintenance\run_maintenance_cycle.py --project <ACTIVE_PROJECT_PATH>`

The counter is a maintenance trigger only. It does not replace session logs, command logs, project memory, or project history.

## Evidence Hierarchy Rule

Use the strongest available evidence:

1. KiCad GUI and screenshot evidence beats Codex report text.
2. KiCad ERC and DRC evidence beats generated summaries.
3. Parsed design files beat generic documentation.
4. Codex summaries are not proof.

Do not claim `PASS`, `READY`, `PROVEN`, or manufacturing readiness unless the required evidence exists and supports the claim.

## Workspace Boundaries

- Use `01_MEMORY\` for durable design decisions.
- Use `02_HISTORY\` for sessions, command logs, design reviews, verification reports, and audit results.
- Use `03_TOOLS\` for scripts and external tool support.
- Use `03_TOOLS\open_source_integrations\` for optional third-party tool
  profiles, install policy, attribution notes, and verification wrappers.
- Use `04_KICAD_PROJECTS\` only for KiCad projects.
- Use `04_KICAD_PROJECTS\_templates\` for project-level lock, checklist, and
  gate-report templates.
- Use `05_OUTPUTS\` for generated review and export outputs.
- Use `06_DATASHEETS\` for datasheet metadata, summaries, and permitted local references.
- Use `07_REFERENCE_DESIGNS\` for human-made reference-style comparison rules
  and link-first learning notes derived from reviewed open-source examples.
- Use `08_COMPONENT_DATABASE\` for structured component intelligence.
- Use `09_ACCURACY_ENGINE\` for strict schematic, PCB, verification, and release-package rules.
- Use `10_KNOWLEDGE_BASE\` for reusable circuit blocks, design patterns, checklists, common mistakes, manufacturing package rules, and AI stop/verify guidance.
- Use `11_LIBRARY_FACTORY\` for symbol, footprint, package mapping, project-local library, and basic read-only library QA standards.
- Use `12_REFERENCE_DESIGN_LIBRARY\` for public-source reference design links, summaries, license records, and verification notes.
- Use `13_PART_INGESTION\` for new-part datasheet/source ingestion, structured stubs, extraction rules, and AI summaries.
- Use `14_LAYOUT_AUTOMATION\` for realistic placement/routing assistance plans, constraint extraction, FreeRouting integration planning, and human layout review gates.
- Use `15_BENCHMARKS\` for benchmark methodology, task definitions, scoring rubrics, and real run results.
- Use `32_OPEN_KICAD_SAMPLE_INTAKE\` for controlled intake, normalization,
  licensing, scoring, and metric extraction for open-source KiCad sample
  projects.
- Use `33_PCB_PRELAYOUT_ENGINE\` for reusable PCB digital-twin, variant-planning, projected-route, and pre-placement/pre-routing gate rules.
- Use `34_SCHEMATIC_QUALITY_ENGINE\` for schematic readability, annotation,
  footprint-readiness, visual-audit, and schematic-to-PCB gate rules.
- Use `35_FOOTPRINT_PACKAGE_ENGINE\` for footprint assignment proof, package
  evidence, lock-file rules, and footprint/package gate logic.
- Use `34_PCB_LAYOUT_SANDBOX\` for reusable sandbox rules, selected-variant reasoning, and pre-PCB-edit workflow gates.
- Use `99_BACKUPS\` for backups before automated edits.

## Do Not Modify Without Approval

Do not edit:

- `.kicad_sch`
- `.kicad_pcb`
- `.kicad_pro`
- `.kicad_sym`
- `.kicad_mod`
- `sym-lib-table`
- `fp-lib-table`
- Gerber, drill, pick-and-place, STEP, or other fabrication outputs
- Installed KiCad application files
- User-global KiCad library tables
- Secrets, credentials, tokens, or private license material

Before any KiCad source edit, confirm the active project, target files, backup path, rollback plan, verification plan, and history log path.

## Control Plane Order

Use the safest control plane that can complete the task:

1. Direct file inspection, repo scripts, `kicad-cli`, `pcbnew` Python, and other CLI/API paths.
2. GUI screenshots for discovery only when CLI/file inspection is insufficient.
3. GUI automation only after explicit user approval, screenshots, window verification, backup, and a rollback plan.

For native schematic annotation, the safe GUI path is:

- dry-run first
- live only with `--live`
- annotation only with `--allow-annotation`
- save only with `--allow-save`
- GUI ERC only with `--allow-gui-erc`

## End-of-Work Rule

At closeout:

1. Write session logs and command logs when commands were run.
2. Update project memory and current state when status changes.
3. Update blockers and resolved blockers when risks change.
4. Rebuild indexes if required by the workflow.
5. State what changed, what was verified, what was not verified, and whether any KiCad project files changed.
6. Make no fake `PASS` claims.
