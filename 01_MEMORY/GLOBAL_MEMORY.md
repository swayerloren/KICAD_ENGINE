# Global Memory

Durable workspace-wide rules for AI-assisted KiCad engineering.

## Workspace Purpose
- This workspace is for AI-assisted KiCad design, review, verification, and fabrication prep.
- Codex should operate from `KICAD_ENGINE` unless working inside a specific project.
- Preserve clean separation between tools, projects, memory, history, outputs, datasheets, and backups.

## Trust And Verification
- Never trust AI-only review for fabrication.
- Always verify with KiCad ERC/DRC and visual review.
- Manufacturing output is not final until ERC, DRC, BOM, footprint, netlist, datasheet, and visual review are complete.
- Treat missing or blocked verification as a release blocker, not a minor note.

## Workspace Separation
- Tools and tool repositories belong in `03_TOOLS/`.
- Active projects belong in `04_KICAD_PROJECTS/active/`.
- Durable decisions belong in `01_MEMORY/`.
- Session notes, command logs, reviews, and reports belong in `02_HISTORY/`.
- Generated outputs belong in `05_OUTPUTS/` or approved project output folders.
- Datasheets belong in `06_DATASHEETS/` or approved project datasheet folders.
- Backups before edits belong in `99_BACKUPS/pre_codex_edits/`.

## Current Durable State
- Workspace bootstrapped.
- No active project selected unless `00_CODEX_START/CURRENT_PROJECT.md` says otherwise.
- No external repositories installed by bootstrap.
- No MCP tools configured by bootstrap.
- Do not install tools, clone repositories, or configure MCP unless explicitly requested.
