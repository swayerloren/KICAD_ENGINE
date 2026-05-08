# Codex Startup Control Planes Synced

Date: 2026-04-30
Workspace: `C:\Users\LJ\KICAD_ENGINE`

## Goal

Synchronize Codex startup/control-plane documentation so future agents understand the `03_TOOLS` common/windows/linux structure, legacy path compatibility, and tool selection rules.

## Backups Created

Backups were written to `99_BACKUPS\pre_codex_edits` before editing:

- `START_HERE_BACKUP_20260430_185010.md`
- `SESSION_START_CHECKLIST_BACKUP_20260430_185010.md`
- `WORKFLOW_RULES_BACKUP_20260430_185010.md`
- `SAFETY_RULES_BACKUP_20260430_185010.md`
- `TOOL_INDEX_BACKUP_20260430_185010.md`
- `REPO_MAP_BACKUP_20260430_185010.md`
- `AGENTS_BACKUP_20260430_185010.md`
- `README_GPT_BACKUP_20260430_185010.md`
- `FOR_CHAT_GPT_BACKUP_20260430_185010.MD`

## Files Updated

- `AGENTS.md`
- `00_CODEX_START\START_HERE.md`
- `00_CODEX_START\SESSION_START_CHECKLIST.md`
- `00_CODEX_START\WORKFLOW_RULES.md`
- `00_CODEX_START\SAFETY_RULES.md`
- `00_CODEX_START\TOOL_INDEX.md`
- `00_CODEX_START\REPO_MAP.md`
- `README_GPT.md`
- `FOR CHAT GPT.MD`

## File Created

- `00_CODEX_START\CONTROL_PLANES.md`

## Rules Added Or Synchronized

- `CONTROL_PLANES.md` is now part of the required startup read order in `AGENTS.md`.
- `START_HERE.md` now includes explicit platform tool roots, legacy path compatibility, tool selection order, GUI automation safety, and Linux/headless safety.
- `SESSION_START_CHECKLIST.md` now requires a control-plane check at session start.
- `WORKFLOW_RULES.md` now includes common-first workflow, GUI-discovery-before-GUI-control workflow, Linux/headless workflow, path migration rule, and ChatGPT handoff update rule.
- `SAFETY_RULES.md` now includes stricter GUI automation, repository migration, finished PCB reference, and Linux/headless safety rules.
- `TOOL_INDEX.md` now includes explicit sections for legacy tool paths, common root, Windows GUI root, installed Windows GUI packages, Windows helper repos, Linux/headless root, Linux docs/scripts, MCP status, and verification script status.
- `REPO_MAP.md` now identifies the legacy, common, Windows, and Linux repo roots and records that current common repos remain in the legacy root until migration is approved.
- `README_GPT.md` and `FOR CHAT GPT.MD` were updated so future ChatGPT/Codex sessions know the platform split, startup order, GUI false-positive warning, and legacy-path rule.

## Safety Notes

- No KiCad project files were modified.
- No GUI automation was run.
- No tools were installed.
- No repos were moved, pulled, built, or edited.
- MCP permissions were not changed.

## Conflicts Or Notes

- Existing startup docs already had a control-plane model. This session expanded and centralized it rather than changing the intended behavior.
- `README_GPT.md` previously still said KiCad GUI discovery had not run against KiCad; that was updated to the current state: the first read-only run was safe but matched a VS Code false positive.
- The false-positive GUI discovery issue remains a known blocker before any GUI control task.

## Recommended Next Prompt

```text
You are in:
C:\Users\LJ\KICAD_ENGINE

Goal:
Fix the Windows KiCad GUI discovery scripts so they only treat confirmed KiCad processes as high-confidence candidates.

Rules:
- Do NOT click.
- Do NOT type.
- Do NOT send hotkeys.
- Do NOT open/save/modify KiCad projects.
- Do NOT run GUI control.
- Update docs/history after fixing.

Focus:
- Prefer process names kicad.exe, eeschema.exe, pcbnew.exe.
- Treat title-only matches such as KICAD_ENGINE in VS Code as low-confidence or exclude them.
- Rerun passive discovery only after the script fix.
```
