# GITHUB_REPO_INDEXING_COMMANDS

Date: `2026-05-08`

## Commands Run In The Tightening Pass

```powershell
Get-Content AGENTS.md
Get-Content README.md
Get-Content README_GPT.md
Get-Content '.\FOR CHAT GPT.MD'
Get-Content 00_CODEX_START\START_HERE.md
Get-Content 00_CODEX_START\CURRENT_PROJECT.md
Get-Content 00_CODEX_START\PROJECT_INDEX.md
Get-Content .gitignore
Get-Content 05_OUTPUTS\release_readiness\GITHUB_PUSH_REPORT.md
Get-Content 05_OUTPUTS\release_readiness\GITHUB_PUSH_PLAN.md
Get-Content 05_OUTPUTS\release_readiness\GITHUB_PUSH_SECURITY_SCAN.md
Get-Content 05_OUTPUTS\release_readiness\GITHUB_PUSH_FILE_INCLUDE_EXCLUDE_AUDIT.md
Get-Content 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\memory\CURRENT_PROJECT_STATE.md
Get-Content 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\memory\CURRENT_BLOCKERS.md
Get-Content 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\FINAL_PCB_VISUAL_REVIEW_PACKET.md
Get-Content 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\LJ_FINAL_PCB_REVIEW_CHECKLIST.md
Get-Content 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\PCB_FINAL_UNCONNECTED_ITEMS_REVIEW.md
git status --short --branch
python 03_TOOLS\scripts\memory_maintenance\check_maintenance_due.py --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE
Get-Content REPO_INDEX.md
Get-Content FOLDER_MAP.md
Get-Content PROJECTS_INDEX.md
Get-Content TOOLS_INDEX.md
Get-Content WORKFLOWS_INDEX.md
Get-Content CURRENT_STATUS.md
Get-Content PUBLIC_RELEASE_STATUS.md
Get-Content 00_CODEX_START\GITHUB_NAVIGATION.md
git diff --stat
python 03_TOOLS\scripts\memory_history\build_memory_index.py
python 03_TOOLS\scripts\memory_history\build_history_index.py
python 03_TOOLS\scripts\ai_quality\build_ai_quality_index.py
python 03_TOOLS\scripts\ai_quality\build_current_known_problems.py
python 03_TOOLS\scripts\memory_maintenance\increment_prompt_counter.py --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE --apply
python 03_TOOLS\scripts\maintenance\run_maintenance_cycle.py --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE
```

## Notes

- The task reused and tightened the previously created GitHub-facing index layer instead of rebuilding it from scratch.
