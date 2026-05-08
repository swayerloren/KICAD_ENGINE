# Platform Tool Roots Created

Date: 2026-04-30

## Scope

Created a platform-aware tool structure for common KiCad tools, Windows GUI automation tools, and Linux/headless automation tools.

This was a structure, documentation, index, and migration-plan update only.

## Safety Notes

- No existing repos were moved.
- No existing scripts were moved.
- No Python virtual environment paths were changed.
- No Node environment paths were changed.
- No tools were installed.
- No third-party repo files were edited.
- No KiCad project files were modified.
- No manufacturing files were generated.

## Folders Created

- `03_TOOLS\common`
- `03_TOOLS\common\repos`
- `03_TOOLS\common\scripts`
- `03_TOOLS\common\docs`
- `03_TOOLS\windows`
- `03_TOOLS\windows\repos`
- `03_TOOLS\windows\scripts`
- `03_TOOLS\windows\scripts\pywinauto`
- `03_TOOLS\windows\scripts\pyautogui`
- `03_TOOLS\windows\scripts\ahk`
- `03_TOOLS\windows\scripts\screenshots`
- `03_TOOLS\windows\scripts\window_discovery`
- `03_TOOLS\windows\docs`
- `03_TOOLS\windows\logs`
- `03_TOOLS\linux`
- `03_TOOLS\linux\repos`
- `03_TOOLS\linux\scripts`
- `03_TOOLS\linux\scripts\xdotool`
- `03_TOOLS\linux\scripts\wmctrl`
- `03_TOOLS\linux\scripts\ydotool`
- `03_TOOLS\linux\scripts\dogtail`
- `03_TOOLS\linux\scripts\xvfb`
- `03_TOOLS\linux\scripts\screenshots`
- `03_TOOLS\linux\scripts\appimage_control`
- `03_TOOLS\linux\docs`
- `03_TOOLS\linux\logs`

## Docs Created

- `03_TOOLS\TOOL_PLATFORM_STRATEGY.md`
- `03_TOOLS\common\README.md`
- `03_TOOLS\windows\README.md`
- `03_TOOLS\linux\README.md`
- `03_TOOLS\tool_logs\PLATFORM_TOOL_STRUCTURE_CREATED.md`
- `03_TOOLS\tool_logs\TOOL_MIGRATION_PLAN.md`

## Files Updated

- `00_CODEX_START\TOOL_INDEX.md`
- `README_GPT.md`
- `FOR CHAT GPT.MD`

## Backups Created

- `99_BACKUPS\pre_codex_edits\TOOL_INDEX_BACKUP_20260430_181639.md`
- `99_BACKUPS\pre_codex_edits\README_GPT_BACKUP_20260430_181639.md`
- `99_BACKUPS\pre_codex_edits\FOR CHAT GPT_BACKUP_20260430_181639.MD`

## Migration Risk Summary

Migration is deferred because current docs, scripts, logs, installed environments, and MCP configuration reference legacy paths. The highest breakage risk is `kicad-happy`, because usage guidance invokes analyzer scripts directly from `03_TOOLS\repos\kicad-happy`. MCP and installed CLI tools mostly run from `03_TOOLS\python_envs`, but their docs and logs still reference source repo paths.

## Next Recommended Prompt

Audit references to `03_TOOLS\repos` and create a repo-by-repo migration checklist without moving files.
