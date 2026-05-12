# AI Agent Fast Context

## Purpose

This is the short startup cheat sheet for future Codex and Claude sessions.

If the user says `Read START_HERE_FOR_AI_AGENTS.md and route yourself
correctly`, this file is part of the immediate follow-up.

## Fast Start

1. Read `START_HERE_FOR_AI_AGENTS.md`.
2. Read `AGENTS.md`.
3. Read `FOR CHAT GPT.MD`.
4. Read `00_CODEX_START/TASK_ROUTER.md`.
5. Read `00_CODEX_START/CURRENT_PROJECT.md`.
6. Use `TASK_TYPE_TO_REQUIRED_DOCS.md`,
   `TASK_TYPE_TO_ALLOWED_ACTIONS.md`,
   `TASK_TYPE_TO_BLOCKERS.md`, and `TASK_TYPE_TO_OUTPUTS.md`.
7. Use `TASK_TYPE_TO_KNOWLEDGE_MAP.md`,
   `TASK_TYPE_TO_TOOL_MAP.md`, and `TASK_TYPE_TO_RULE_MAP.md`.

## Hard Truths

- If a schematic, PCB, or fab prompt does not list read-first files, use
  `TASK_ROUTER.md`. Do not wait for the user to paste a giant list.
- Use the canonical startup maps in `00_CODEX_START/` and the mirror retrieval
  maps in `10_KNOWLEDGE_BASE/retrieval_indexes/`.
- Raw `.kicad_sch` text edits are not annotation proof.
- Real PCB placement is blocked until the latest prelayout result proves at
  least three variants, at least one passing variant, and
  `placement_gate_status = PASS`.
- Real PCB routing is additionally blocked until that same prelayout result
  proves `routing_gate_status = PASS`.
- Connector orientation is not proven by XY position or rotation alone.
- Routing is not acceptable on DRC alone. The trace-geometry audit must also
  pass.
- Copper zones come after routing is substantially complete.
- Fabrication-style outputs stay `NOT_FINAL` unless the full gate passes and LJ
  explicitly approves final status.

## Route Shortcuts

- schematic create/repair -> `SCHEMATIC_CREATE_OR_REPAIR`
- schematic readability/overlap cleanup -> `SCHEMATIC_VISUAL_CLEANUP`
- native KiCad annotation -> `NATIVE_ANNOTATION`
- footprint/package assignment -> `FOOTPRINT_PACKAGE_GATE`
- PCB update from schematic -> `PCB_UPDATE_FROM_SCHEMATIC`
- prelayout digital twin / variants -> `PCB_PRELAYOUT_VARIANT_PLANNING`
- PCB placement -> `PCB_PLACEMENT`
- connector direction proof -> `CONNECTOR_ORIENTATION_AUDIT`
- PCB routing -> `PCB_ROUTING`
- trace quality audit -> `TRACE_GEOMETRY_AUDIT`
- copper pours -> `PCB_COPPER_ZONES`
- fabrication outputs -> `FAB_EXPORT`
- memory/history/index refresh -> `MEMORY_MAINTENANCE`
- local tool or open-source workflow use -> `OPEN_SOURCE_TOOL_USE`
- formula-sizing or calculator help -> `OPEN_SOURCE_TOOL_USE`, then
  `10_KNOWLEDGE_BASE/calculators/`

## Control Plane Reminder

Use the safest control plane that can finish the task:

1. file inspection, repo scripts, CLI, API, `kicad-cli`, `pcbnew` Python
2. GUI screenshots for discovery only when needed
3. GUI automation only under the explicit `33_KICAD_GUI_AUTOMATION` gates

Calculator rule:

- calculator output is an aid only until the source/formula is recorded and an
  independent check exists
