# Claude Prompt: Start Session

You are Claude working from VS Code in:

`C:\Users\LJ\GitHub\KICAD_ENGINE`

## Read First

Read these files before doing any work:

1. `AGENTS.md`
2. `00_CODEX_START/START_HERE.md`
3. `00_CODEX_START/SESSION_START_CHECKLIST.md`
4. `00_CODEX_START/WORKFLOW_RULES.md`
5. `00_CODEX_START/SAFETY_RULES.md`
6. `00_CODEX_START/CONTROL_PLANES.md`
7. `00_CODEX_START/REPO_MAP.md`
8. `00_CODEX_START/TOOL_INDEX.md`
9. `00_CODEX_START/MEMORY_INDEX.md`
10. `00_CODEX_START/HISTORY_INDEX.md`
11. `00_CODEX_START/PROJECT_INDEX.md`
12. `00_CODEX_START/CURRENT_PROJECT.md`
13. `.prompts/shared/SAFETY_GATES.md`

## Goal

Start a safe KiCad engineering session and establish the current repo, project, memory, history, and verification context.

## Universal Requirements

- Do not modify KiCad project files until the active project, target files, backup path, verification plan, and rollback plan are confirmed.
- Require a backup before any edit to schematic, PCB, symbol, footprint, project, or fabrication-output files.
- Record meaningful work in `02_HISTORY/`, including commands run and verification results.
- Produce verification reports when checks are run or explain why they could not be run.
- Do not fabricate datasheet claims, electrical limits, lifecycle status, or package data.
- Do not select or approve footprints unless the exact package and manufacturer drawing have been verified.
- Label all generated manufacturing-style outputs `NOT_FINAL` until ERC, DRC, BOM, footprint, datasheet, and visual review gates pass.

## Session Work

1. Confirm the current working directory.
2. Summarize the active project status from `CURRENT_PROJECT.md`.
3. Identify relevant memory and history files to read for the requested task.
4. State whether the requested task is documentation-only, read-only inspection, project editing, or output generation.
5. Choose the safest control plane: CLI/API first, direct file parsing when safe, GUI discovery only when needed.

## Do Not Modify

- KiCad project source files unless startup and backup gates pass.
- Installed KiCad application folders.
- User global KiCad library tables.
- Datasheet PDFs or redistributed vendor documents without permission review.
- Secrets, credentials, tokens, or private license files.

## Output

Provide a concise session-start summary with:

- Current repo path.
- Active project status.
- Relevant memory/history to inspect next.
- Safety gates required before edits.
- Proposed next action.
