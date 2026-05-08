# KiCad Agent Operating Manual Session

Date: 2026-05-02

## Purpose

Create agent-facing KiCad usage guidance for Codex, Claude, and similar VS Code-based agents.

## Required Context Read

- `AGENTS.md`
- `README.md`
- `00_CODEX_START/KICAD_ENGINE_ARCHITECTURE.md`
- `02_HISTORY/design_reviews/KICAD_INSTALLED_APP_DEEP_AUDIT.md`
- `03_TOOLS/kicad_app_intelligence/KICAD_9_WINDOWS_PATH_MAP.md`
- `03_TOOLS/kicad_app_intelligence/KICAD_CLI_COMMANDS_REFERENCE.md`
- `03_TOOLS/kicad_app_intelligence/KICAD_LIBRARY_DISCOVERY_GUIDE.md`

## Files Created

- `00_CODEX_START/KICAD_AGENT_OPERATING_MANUAL.md`
- `00_CODEX_START/KICAD_SAFE_AUTOMATION_RULES.md`
- `03_TOOLS/kicad_app_intelligence/KICAD_AGENT_TASK_MAP.md`

## Files Updated

- `README_GPT.md`
- `FOR CHAT GPT.MD`
- `00_CODEX_START/TOOL_INDEX.md`

## Backups Created

- `99_BACKUPS/pre_codex_edits/agent_operating_manual_docs_20260502_160550`
- `99_BACKUPS/pre_codex_edits/tool_index_agent_docs_20260502_161014`

## Safety Notes

- No KiCad project source files were edited.
- No installed KiCad files were edited.
- No tools were installed.
- No datasheets were downloaded.
- Work was documentation and agent guidance only.

## Result

The new documentation defines safe task selection for direct parsing, `kicad-cli`, `pcbnew` Python, GUI screenshots, and GUI automation avoidance. It also maps common KiCad engineering requests to guarded workflows with ERC, DRC, BOM, footprint, datasheet, fabrication, and board-house review gates.
