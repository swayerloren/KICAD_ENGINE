# Start Router Upgrade Audit

Date: `2026-05-10`

## Scope

Upgrade the repo startup and prompt-router layer so future Codex/Claude
sessions can derive the correct schematic, PCB, GUI, routing, fab,
memory/history, and open-source-tool docs from `START_HERE_FOR_AI_AGENTS.md`
without the user pasting large manual `READ FIRST` lists.

## Files Created

- `00_CODEX_START/TASK_ROUTER.md`
- `00_CODEX_START/TASK_TYPE_TO_REQUIRED_DOCS.md`
- `00_CODEX_START/TASK_TYPE_TO_ALLOWED_ACTIONS.md`
- `00_CODEX_START/TASK_TYPE_TO_BLOCKERS.md`
- `00_CODEX_START/TASK_TYPE_TO_OUTPUTS.md`
- `00_CODEX_START/KICAD_ENGINE_CRITICAL_PATH.md`
- `00_CODEX_START/AI_AGENT_FAST_CONTEXT.md`

## Files Updated

- `START_HERE_FOR_AI_AGENTS.md`
- `AGENTS.md`
- `README_GPT.md`
- `FOR CHAT GPT.MD`
- `.prompts/README.md`
- `.prompts/codex/00_START_SESSION.md`
- `.prompts/claude/00_START_SESSION.md`
- `01_MEMORY/DESIGN_RULES_MEMORY.md`

## Supported Task Routes

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

## Validation

1. `START_HERE_FOR_AI_AGENTS.md` points to `00_CODEX_START/TASK_ROUTER.md`.
2. Every main task route appears in:
   - `TASK_TYPE_TO_REQUIRED_DOCS.md`
   - `TASK_TYPE_TO_ALLOWED_ACTIONS.md`
   - `TASK_TYPE_TO_BLOCKERS.md`
   - `TASK_TYPE_TO_OUTPUTS.md`
3. `git diff --name-only -- '*.kicad_sch' '*.kicad_pcb'` returned no paths.
4. Prompt-counter maintenance triggered during this task when the active-project
   counter reached `5`; the required maintenance cycle ran and reset the counter
   to `0`.
5. `02_HISTORY/sessions/2026-05-10_start_router_upgrade_task_contract.json`
   validated as `VALID_TASK_CONTRACT`.
6. Standard repo, memory, history, AI-quality, and known-problem indexes were
   rebuilt after the router upgrade.

## Key Routing Outcome

The new front-door behavior is now:

1. Read `START_HERE_FOR_AI_AGENTS.md`.
2. Read `AGENTS.md`.
3. Read `FOR CHAT GPT.MD`.
4. Read `00_CODEX_START/AI_AGENT_FAST_CONTEXT.md`.
5. Use `00_CODEX_START/TASK_ROUTER.md` and companion task-type tables.

This removes the need for users to paste large repeated startup lists for
common schematic, placement, routing, or fab tasks.

## Compatibility Note

The router explicitly resolves the historical `03_TOOLS/scripts/pcb_quality`
name to the current routing-quality gate under `03_TOOLS/scripts/pcb_geometry/`
when the older folder is absent.

## KiCad File Status

No `.kicad_sch` or `.kicad_pcb` files were changed by this router-upgrade task.
