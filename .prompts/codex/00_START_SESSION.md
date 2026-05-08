# Codex Prompt: Start KiCad Engine Session

You are working in your local `KICAD_ENGINE` repo root from VS Code.

## Read First

Read:

1. `AGENTS.md`
2. `.prompts/shared/SAFETY_GATES.md`
3. `00_CODEX_START/START_HERE.md`
4. `00_CODEX_START/SESSION_START_CHECKLIST.md`
5. `00_CODEX_START/WORKFLOW_RULES.md`
6. `00_CODEX_START/SAFETY_RULES.md`
7. `00_CODEX_START/CONTROL_PLANES.md`
8. `00_CODEX_START/TOOL_INDEX.md`
9. `00_CODEX_START/CURRENT_PROJECT.md`

Then read relevant `01_MEMORY` and `02_HISTORY` entries for the current task.

## Task

Start a safe KiCad Engine session. Summarize:

- Active project name and path.
- Current task mode.
- Whether KiCad project source edits are allowed.
- Relevant tools and scripts.
- Relevant memory/history.
- Required backup and verification gates.

## Restrictions

- Do not edit KiCad project files.
- Do not modify installed KiCad files or user-global KiCad config.
- Do not install tools.
- Do not make datasheet or footprint claims without source evidence.

## Output

Return a concise session readiness summary and recommended next action. If any KiCad source edit is requested later, require backup, rollback, ERC/DRC, history log, and verification report.

## Universal Safety Requirements

- Require active project confirmation, backup, rollback plan, verification plan, and history log before any KiCad source edit.
- Do not fabricate datasheet claims, electrical limits, lifecycle status, package data, or verification status.
- Do not select or approve a footprint unless the exact part package and manufacturer drawing have been verified.
- Label every generated manufacturing-style output `NOT_FINAL` until ERC, DRC, BOM, footprint, datasheet, and visual review gates pass.
