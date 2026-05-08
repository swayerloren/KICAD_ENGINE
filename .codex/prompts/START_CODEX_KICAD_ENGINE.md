# Start Codex KiCad Engine

Use this prompt at the beginning of every KiCad engineering workspace session.

## Required Behavior
You are in the KiCad engineering workspace. Before touching any KiCad project file, complete the startup check below.

## Startup Check
1. Detect and state the workspace root.
2. Read root `AGENTS.md`.
3. Read every file in `00_CODEX_START/` in the order required by `AGENTS.md`:
   - `00_CODEX_START/START_HERE.md`
   - `00_CODEX_START/SESSION_START_CHECKLIST.md`
   - `00_CODEX_START/WORKFLOW_RULES.md`
   - `00_CODEX_START/SAFETY_RULES.md`
   - `00_CODEX_START/REPO_MAP.md`
   - `00_CODEX_START/TOOL_INDEX.md`
   - `00_CODEX_START/MEMORY_INDEX.md`
   - `00_CODEX_START/HISTORY_INDEX.md`
   - `00_CODEX_START/PROJECT_INDEX.md`
   - `00_CODEX_START/CURRENT_PROJECT.md`
4. Detect and state the active project from `00_CODEX_START/CURRENT_PROJECT.md`.
5. Load relevant memory from `01_MEMORY/`.
6. Load relevant history from `02_HISTORY/`.
7. List installed and missing tools by inspecting the local workspace and system PATH. Do not install anything.
8. State the verification plan for the requested task.

## Refusal Gate
Refuse to edit `.kicad_sch`, `.kicad_pcb`, `.kicad_pro`, symbol libraries, footprint libraries, or manufacturing outputs until the startup check is complete and an active project is identified.

## Deferred Setup
Do not install tools, clone repositories, or configure MCP unless the user explicitly asks in a later task.
