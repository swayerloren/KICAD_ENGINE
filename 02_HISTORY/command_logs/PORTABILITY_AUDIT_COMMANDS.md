# Portability Audit Commands

Record kind: `workflow_run`
Status: `UNVERIFIED`
Created: `2026-05-08T18:31:00`
Scope: `global`
Project: `N/A`

## Summary

Major commands used for the portability audit and hardening pass.

## Details

- `git status --ignored`
- `git fetch origin`
- `git status`
- `git branch --show-current`
- `git remote -v`
- `git rev-parse HEAD`
- `git rev-parse origin/main`
- `git log --oneline --decorate -n 10`
- `git check-ignore -v 03_TOOLS/node_envs/kicanvas 03_TOOLS/python_envs/kibot 03_TOOLS/repos/KiBot 03_TOOLS/tool_logs/KICAD_ENGINE_HEALTH_CHECK.md 99_BACKUPS/pre_codex_edits 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/routing_rehearsals/scratch.txt`
- `git ls-files 03_TOOLS/node_envs 03_TOOLS/python_envs 03_TOOLS/repos 03_TOOLS/tool_logs 99_BACKUPS 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/routing_work 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/routing_rehearsals`
- `git ls-tree -r origin/main --name-only | findstr /i "03_TOOLS node_envs python_envs repos tool_logs 99_BACKUPS routing_work routing_rehearsals"`
- `rg -n "C:\\Users\\LJ|C:/Users/LJ" ...` across targeted docs/scripts
- `python -m py_compile 03_TOOLS/scripts/ai_quality/ai_quality_common.py 03_TOOLS/scripts/memory_history/memory_history_common.py 03_TOOLS/scripts/maintenance/prompt_counter.py 03_TOOLS/scripts/memory_maintenance/check_maintenance_due.py 03_TOOLS/windows/scripts/window_discovery/discover_windows.py 03_TOOLS/windows/scripts/screenshots/take_screenshot.py 03_TOOLS/windows/scripts/kicad_window_filter.py`
- PowerShell folder-size/file-count inventory commands for:
  - `03_TOOLS/node_envs`
  - `03_TOOLS/python_envs`
  - `03_TOOLS/repos`
  - `03_TOOLS/tool_logs`
  - `99_BACKUPS`
  - `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/routing_work`
  - `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/routing_rehearsals`

## Source Or Evidence

Command outputs were used to populate:

- `05_OUTPUTS/release_readiness/PORTABILITY_AUDIT_REPORT.md`
- `05_OUTPUTS/release_readiness/LOCAL_VS_GITHUB_SYNC_REPORT.md`

## Verification Status

Mark this record `USER_CONFIRMED` or `VERIFIED_WORKFLOW` only after human confirmation or repeatable evidence exists.

## Secret Check

No secrets should be stored in this record.
