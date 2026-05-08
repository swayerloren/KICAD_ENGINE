# Start Here For AI Agents

This is the short first-read routing file for Codex, Claude, and similar agents working in `KICAD_ENGINE`.

This file does not replace `AGENTS.md`. It routes agents to the right deeper rules so future prompts do not need to list every `READ FIRST` file.

Future prompts may simply say:

`Read START_HERE_FOR_AI_AGENTS.md and route yourself to the correct project/task files.`

The agent must then use the Task Router below, follow `AGENTS.md`, and read the task-specific files required for the current work.

## Mandatory Minimal Startup

Read these first:

1. `START_HERE_FOR_AI_AGENTS.md`
2. `AGENTS.md`
3. `FOR CHAT GPT.MD`

Then follow `AGENTS.md` for the full startup chain before touching KiCad project files or making engineering claims.

Also read `.prompts/README.md` and the task-specific prompt from `.prompts/codex` or `.prompts/claude` when the user is using the prompt pack.

## Task Router

Use this table after the mandatory minimal startup. Read the listed folders/files plus the active project memory, history, and reports relevant to the requested task.

| If the task is | Read / check |
| --- | --- |
| Schematic work | `09_ACCURACY_ENGINE\schematic_rules\`; `09_ACCURACY_ENGINE\verification_rules\`; `03_TOOLS\scripts\kicad_schematic_checks\`; active project reports and memory |
| Schematic annotation | `33_KICAD_GUI_AUTOMATION\`; `03_TOOLS\kicad\KICAD_NATIVE_ACTIONS_NOT_SUPPORTED_BY_CLI.md`; never use raw `.kicad_sch` text edits as proof |
| PCB update from schematic | `00_CODEX_START\KICAD_PHASE_ORDER.md`; `09_ACCURACY_ENGINE\workflows\MANDATORY_KICAD_PHASE_GATE.md`; `09_ACCURACY_ENGINE\verification_rules\NO_PHASE_SKIPPING_RULES.md`; `34_PCB_LAYOUT_SANDBOX\`; active project `reports\SCHEMATIC_TO_PCB_GATE_STATUS.md`; active project sandbox variant reports; active project `reports\PCB_SYNC_STATUS.md` when present |
| PCB placement | `09_ACCURACY_ENGINE\pcb_rules\`; `09_ACCURACY_ENGINE\checklists\PILL_STYLE_PLACEMENT_CHECKLIST.md`; `34_PCB_LAYOUT_SANDBOX\`; `04_KICAD_PROJECTS\active\<PROJECT>\pcb_intelligence\`; `14_LAYOUT_AUTOMATION\`; active project placement reports and sandbox variant reports |
| Connector orientation | `09_ACCURACY_ENGINE\pcb_rules\CONNECTOR_EDGE_ORIENTATION_RULES.md`; `09_ACCURACY_ENGINE\pcb_rules\PCB_MECHANICAL_CLEARANCE_RULES.md`; active project connector proof reports; 3D and screenshot evidence required when available |
| Routing | Run/check the phase gate first; `34_PCB_LAYOUT_SANDBOX\`; active project selected sandbox variant; active project `pcb_intelligence\`; `CRITICAL_NET_ROUTING_RULES.md`; `POWER_TREE_AND_RETURN_PATHS.md`; `USB_ROUTING_PLAN.md`; `VIA_AND_LAYER_STRATEGY.md`; `COPPER_ZONE_STRATEGY.md`; LJ placement approval required |
| Copper pour / zones | `COPPER_ZONE_STRATEGY.md`; `ESP32_RF_KEEP_OUT_PLAN.md`; `VIA_AND_LAYER_STRATEGY.md`; GND, thermal, and zone priority rules; placement and routing gates must pass |
| JLCPCB / export / production | `24_FAB_PROFILES\`; `24_FAB_PROFILES\UNIVERSAL_PCBA_PACKAGE_RULES.md`; `24_FAB_PROFILES\JLCPCB\README.md`; `24_FAB_PROFILES\PCBWAY\README.md`; `17_RELEASE_BUILD\`; `09_ACCURACY_ENGINE\checklists\PCBA_EXPORT_GATE_CHECKLIST.md`; phase gate; DRC and no-unrouted proof; `NOT_FINAL` rules; run validators before claiming package readiness |
| Memory / history cleanup | `01_MEMORY\`; `02_HISTORY\`; `03_TOOLS\scripts\memory_maintenance\`; `09_ACCURACY_ENGINE\workflows\MEMORY_HISTORY_MAINTENANCE_WORKFLOW.md` |

If a row points to a filename without a directory, resolve it from the active project first, then from the relevant rule folder named in that row.

## Active Project Rule

For any project task:

1. Identify the active project from `00_CODEX_START\CURRENT_PROJECT.md`.
2. Read the active project memory.
3. Read active project `CURRENT_PROJECT_STATE.md` if present.
4. Read active project `CURRENT_BLOCKERS.md` if present.
5. Read active project `NEXT_ALLOWED_PHASE.md` if present.
6. Read active project reports relevant to the task.

Do not edit KiCad project files unless `AGENTS.md` edit gates are satisfied, the active project is confirmed, and the backup plan is confirmed. For real PCB edits, sandbox planning and selected-variant justification must also be confirmed.

## Phase Gate Rule

Before any PCB pipeline phase, run or check:

`python 03_TOOLS\scripts\project_gate\check_phase_allowed.py --project <ACTIVE_PROJECT_PATH> --phase <PHASE>`

If the checker or evidence says `BLOCKED`, stop. Report the requested phase, blocking earlier phase, missing evidence, and next allowed phase. Do not create downstream blocked review reports unless LJ specifically asks for a blocker audit.

## Prompt Counter Rule

Before meaningful active-project repo work:

1. Increment the active project prompt counter.
2. Check whether maintenance is due.
3. If maintenance is due, run maintenance before engineering work:

`python 03_TOOLS\scripts\memory_maintenance\run_memory_maintenance.py --project <ACTIVE_PROJECT_PATH> --apply`

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
- Use `04_KICAD_PROJECTS\` only for KiCad projects.
- Use `05_OUTPUTS\` for generated review and export outputs.
- Use `06_DATASHEETS\` for datasheet metadata, summaries, and permitted local references.
- Use `08_COMPONENT_DATABASE\` for structured component intelligence.
- Use `09_ACCURACY_ENGINE\` for strict schematic, PCB, verification, and release-package rules.
- Use `10_KNOWLEDGE_BASE\` for reusable circuit blocks, design patterns, checklists, common mistakes, manufacturing package rules, and AI stop/verify guidance.
- Use `11_LIBRARY_FACTORY\` for symbol, footprint, package mapping, project-local library, and basic read-only library QA standards.
- Use `12_REFERENCE_DESIGN_LIBRARY\` for public-source reference design links, summaries, license records, and verification notes.
- Use `13_PART_INGESTION\` for new-part datasheet/source ingestion, structured stubs, extraction rules, and AI summaries.
- Use `14_LAYOUT_AUTOMATION\` for realistic placement/routing assistance plans, constraint extraction, FreeRouting integration planning, and human layout review gates.
- Use `15_BENCHMARKS\` for benchmark methodology, task definitions, scoring rubrics, and real run results.
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

## End-of-Work Rule

At closeout:

1. Write session logs and command logs when commands were run.
2. Update project memory and current state when status changes.
3. Update blockers and resolved blockers when risks change.
4. Rebuild indexes if required by the workflow.
5. State what changed, what was verified, what was not verified, and whether any KiCad project files changed.
6. Make no fake `PASS` claims.
