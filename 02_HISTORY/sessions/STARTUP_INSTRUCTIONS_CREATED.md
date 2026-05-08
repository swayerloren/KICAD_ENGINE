# Startup Instructions Created

Date: 2026-04-30

## Summary
Updated the root `AGENTS.md` and all `00_CODEX_START` instruction files with strict Codex startup rules for KiCad engineering work.

## Files Updated
- `AGENTS.md`
- `00_CODEX_START\START_HERE.md`
- `00_CODEX_START\SESSION_START_CHECKLIST.md`
- `00_CODEX_START\WORKFLOW_RULES.md`
- `00_CODEX_START\SAFETY_RULES.md`
- `00_CODEX_START\REPO_MAP.md`
- `00_CODEX_START\TOOL_INDEX.md`
- `00_CODEX_START\MEMORY_INDEX.md`
- `00_CODEX_START\HISTORY_INDEX.md`
- `00_CODEX_START\PROJECT_INDEX.md`
- `00_CODEX_START\CURRENT_PROJECT.md`

## Rules Captured
- Codex must read `AGENTS.md` first, then `00_CODEX_START` files in the required order.
- Codex must identify the active project and review relevant memory/history before touching KiCad files.
- Protected KiCad files require an identified active project, backups, a verification plan, and a rollback plan before edits.
- Schematic changes require ERC or an explanation.
- PCB changes require DRC or an explanation.
- Manufacturing output is not final until ERC, DRC, BOM, footprint, netlist, datasheet, and visual review are complete.
- Durable decisions belong in `01_MEMORY`; commands and results belong in `02_HISTORY`.
- Secrets and credentials must not be stored in memory or history.

## Tooling
No tools were installed.
No repositories were cloned.
No MCP configuration was performed.
