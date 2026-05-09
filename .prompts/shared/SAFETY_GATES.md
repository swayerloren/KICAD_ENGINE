# Shared Safety Gates

Use this standard in every KiCad Engine prompt.

## Files To Read First

Read these before touching KiCad project files:

1. `AGENTS.md`
2. `00_CODEX_START/START_HERE.md`
3. `00_CODEX_START/SESSION_START_CHECKLIST.md`
4. `00_CODEX_START/WORKFLOW_RULES.md`
5. `00_CODEX_START/SAFETY_RULES.md`
6. `00_CODEX_START/CONTROL_PLANES.md`
7. `00_CODEX_START/PATH_PORTABILITY_RULES.md`
8. `00_CODEX_START/REPO_MAP.md`
9. `00_CODEX_START/TOOL_INDEX.md`
10. `00_CODEX_START/MEMORY_INDEX.md`
11. `00_CODEX_START/HISTORY_INDEX.md`
12. `00_CODEX_START/PROJECT_INDEX.md`
13. `00_CODEX_START/CURRENT_PROJECT.md`

Then read relevant memory and history for the target project or task.

## Do Not Modify

Do not modify:

- Installed KiCad folders under `C:\Program Files\KiCad`.
- User-global KiCad config under `%APPDATA%\kicad`.
- KiCad project source files unless the active project gate is satisfied.
- `.kicad_pro`, `.kicad_sch`, `.kicad_pcb`, `.kicad_sym`, `.kicad_mod`.
- `sym-lib-table`, `fp-lib-table`, `design-block-lib-table`.
- Gerber, drill, pick-and-place, or manufacturing outputs unless the prompt explicitly asks for review-only export.
- Secrets, API keys, tokens, credentials, or license keys.

## Required Before Edits

Before any KiCad source edit:

1. Confirm active project name.
2. Confirm active project path.
3. Confirm files likely to change.
4. Confirm target files are inside the active project folder.
5. Create or confirm backup in `99_BACKUPS/pre_codex_edits`.
6. State rollback plan.
7. State verification plan.
8. Record what happened in `02_HISTORY`.

## Required Verification

- After schematic edits: run ERC or explain why ERC could not run.
- After PCB edits: run DRC or explain why DRC could not run.
- For footprint choices: verify exact package drawing.
- For connector choices: verify pin numbering, orientation, mating connector, and mechanical drawing.
- For polarity-sensitive parts: verify orientation and silkscreen.
- For RF paths: verify stackup, controlled impedance, keepout, antenna, and matching network.
- For manufacturing outputs: use `NOT_FINAL` unless the full verification gate is complete and user-approved.

## Report Language

Use precise status language:

- `READ_ONLY_INSPECTION`
- `REPORT_GENERATED`
- `PASS_BY_KICAD_CLI`
- `FAILED_OR_VIOLATIONS_REPORTED`
- `EXPORTED_REQUIRES_REVIEW`
- `EXPORTED_NOT_FINAL`
- `HUMAN_REVIEW_REQUIRED`
- `FAB_READY_BY_USER_APPROVAL`

Never collapse one passing check into full approval.

Historical reports, generated indexes, and archived review packets may contain old absolute machine paths. Use repo-relative paths and live discovery for current work.
