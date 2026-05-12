# Task Router

## Purpose

This file is the automatic routing layer for Codex, Claude, and similar agents
working in `KICAD_ENGINE`.

Use it when the user asks for schematic, PCB, GUI, routing, fabrication,
memory/history, or open-source tool work and does not provide a long `READ
FIRST` list.

The retired `knowledge_scrape/` source tree is not part of this routing path.
If it appears in older reports, treat it as migration provenance only.

This router does not replace `AGENTS.md`. It decides which deeper rules must be
read after startup.

## Hard Rule

If a user prompt asks for schematic, PCB, fabrication, memory/history, or
open-source tool work and does not list read-first files, Codex must use this
router to determine the required docs automatically.

Do not ask the user to paste a giant startup list when the required path can be
derived from this file plus the companion task tables.

## First Reads

Read these first:

1. `START_HERE_FOR_AI_AGENTS.md`
2. `AGENTS.md`
3. `FOR CHAT GPT.MD`
4. `00_CODEX_START/AI_AGENT_FAST_CONTEXT.md`
5. `00_CODEX_START/CURRENT_PROJECT.md`

Then follow `AGENTS.md` and the route-specific docs below.

## Router Procedure

1. Classify the request into exactly one primary route from the table below.
2. If the request spans multiple phases, choose the earliest blocked phase
   first. Do not jump to a later phase.
3. Read:
   - `00_CODEX_START/TASK_TYPE_TO_REQUIRED_DOCS.md`
   - `00_CODEX_START/TASK_TYPE_TO_ALLOWED_ACTIONS.md`
   - `00_CODEX_START/TASK_TYPE_TO_BLOCKERS.md`
   - `00_CODEX_START/TASK_TYPE_TO_OUTPUTS.md`
   - `00_CODEX_START/TASK_TYPE_TO_KNOWLEDGE_MAP.md`
   - `00_CODEX_START/TASK_TYPE_TO_TOOL_MAP.md`
   - `00_CODEX_START/TASK_TYPE_TO_RULE_MAP.md`
4. Read the active project memory, history, and reports required by that route.
5. Check prompt-counter and maintenance rules before meaningful work.
6. Declare exactly one execution-contract task type for the run. Router task
   routes are workflow categories; they do not replace execution-contract task
   types such as `DOCS_ONLY` or `ROUTING_EDIT_REQUIRED`.
7. Choose the safest control plane. Prefer CLI/API/file inspection before GUI.

## Task Route Picker

| Route | Use This Route When The User Asks To |
| --- | --- |
| `SCHEMATIC_CREATE_OR_REPAIR` | create, repair, refactor, or electrically fix a schematic under the schematic quality engine |
| `SCHEMATIC_VISUAL_CLEANUP` | improve schematic readability, overlap cleanup, or close-up visual review under the schematic quality engine |
| `NATIVE_ANNOTATION` | annotate references in KiCad GUI or prove annotation state |
| `FOOTPRINT_PACKAGE_GATE` | assign, verify, or audit footprints/packages |
| `PCB_UPDATE_FROM_SCHEMATIC` | sync/update/create PCB from schematic |
| `PCB_PRELAYOUT_VARIANT_PLANNING` | extract a PCB digital twin, generate variants, project routes, or score placement/routing candidates |
| `PCB_PLACEMENT` | place components on a real board or evaluate placement readiness |
| `CONNECTOR_ORIENTATION_AUDIT` | prove connector mouth direction, mating face, body side, pin side, or antenna keepout orientation |
| `PCB_ROUTING` | route real traces, copied-board rehearsals, or routing-stage audits |
| `TRACE_GEOMETRY_AUDIT` | judge whether existing routing geometry is acceptable |
| `PCB_COPPER_ZONES` | create, refill, or review copper pours/zones |
| `FAB_EXPORT` | generate or approve fabrication/export packages |
| `MEMORY_MAINTENANCE` | update memory/history, run maintenance, rebuild indexes, or close out a session |
| `OPEN_SOURCE_TOOL_USE` | use optional external KiCad-adjacent tools, local wrappers, tool-evaluation docs, sample projects, or browser-assisted research rules |

## Precedence Rules

Apply these rules before acting:

1. `NATIVE_ANNOTATION` outranks raw text-based annotation ideas. Raw
   `.kicad_sch` edits are never annotation proof.
2. `FOOTPRINT_PACKAGE_GATE` must pass before `PCB_UPDATE_FROM_SCHEMATIC`.
3. `PCB_PRELAYOUT_VARIANT_PLANNING` must pass before real `PCB_PLACEMENT` or
   real `PCB_ROUTING`.
4. `CONNECTOR_ORIENTATION_AUDIT` is mandatory support evidence for
   `PCB_PLACEMENT`, `PCB_ROUTING`, `PCB_COPPER_ZONES`, and `FAB_EXPORT`.
5. `TRACE_GEOMETRY_AUDIT` is mandatory support evidence for `PCB_ROUTING`,
   `PCB_COPPER_ZONES`, and `FAB_EXPORT`. DRC alone is not routing-quality proof.
6. `PCB_COPPER_ZONES` comes after routing is substantially complete.
7. `FAB_EXPORT` comes after final schematic, placement, routing, orientation,
   BOM/CPL, polarity, DRC, and visual gates.
8. If a later route is requested too early, stop and reroute to the earliest
   blocking phase or provide a blocker audit if the user explicitly asked for
   one.

## Route Notes

- When schematic create/repair, readability cleanup, or schematic-to-PCB gate
  work is requested, read `34_SCHEMATIC_QUALITY_ENGINE/` and
  `03_TOOLS/scripts/schematic_quality/` in addition to the existing schematic
  rules and annotation gates.
- When native KiCad annotation is requested, read
  `33_KICAD_GUI_AUTOMATION/KICAD_AUTO_OPEN_PROJECT_WORKFLOW.md`,
  `KICAD_ANNOTATION_DO_AND_DO_NOT.md`, and `KICAD_GUI_ACTION_MATRIX.md` in
  addition to the native annotation workflow and safety gates. Closed-state
  recovery must go through the dry-run-first auto-open path; raw text edits are
  never annotation proof.
- When footprint or package assignment work is requested, read
  `35_FOOTPRINT_PACKAGE_ENGINE/`, `03_TOOLS/scripts/footprint_package/`, the
  active project's `FOOTPRINT_LOCK.csv` when present, and the project template
  files under `04_KICAD_PROJECTS/_templates/`.
- For startup routing, knowledge lookup, and tool/rule selection, use the
  canonical `00_CODEX_START/TASK_TYPE_TO_*_MAP.md` files and the mirror copies
  under `10_KNOWLEDGE_BASE/retrieval_indexes/`. Historical migration
  provenance belongs in repo history and release-readiness reports; it is not
  part of the live routing path.
- If the prompt says `pcb_quality` but the folder
  `03_TOOLS/scripts/pcb_quality/` does not exist, use the current routing
  quality gate under `03_TOOLS/scripts/pcb_geometry/`.
- If the prompt says `Read START_HERE_FOR_AI_AGENTS.md and route yourself
  correctly`, do not wait for more instructions. Use this file.
- If the active project reports conflict with live KiCad files, follow the
  live-state authority rules before trusting stale reports.

## Related Files

- `00_CODEX_START/TASK_TYPE_TO_REQUIRED_DOCS.md`
- `00_CODEX_START/TASK_TYPE_TO_ALLOWED_ACTIONS.md`
- `00_CODEX_START/TASK_TYPE_TO_BLOCKERS.md`
- `00_CODEX_START/TASK_TYPE_TO_OUTPUTS.md`
- `00_CODEX_START/TASK_TYPE_TO_KNOWLEDGE_MAP.md`
- `00_CODEX_START/TASK_TYPE_TO_TOOL_MAP.md`
- `00_CODEX_START/TASK_TYPE_TO_RULE_MAP.md`
- `00_CODEX_START/KICAD_ENGINE_CRITICAL_PATH.md`
- `00_CODEX_START/AI_AGENT_FAST_CONTEXT.md`
