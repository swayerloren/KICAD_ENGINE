# GitHub README Workflow Rewrite Commands

## Commands Run

```powershell
python 03_TOOLS\scripts\maintenance\run_maintenance_cycle.py --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE
Get-Content -Raw README.md
Get-Content -Raw .github\README.md
Get-Content -Raw CURRENT_STATUS.md
Get-Content -Raw 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\memory\CURRENT_PROJECT_STATE.md
Get-Content -Raw 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\memory\CURRENT_BLOCKERS.md
Get-Content -Raw 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\FINAL_PCB_VISUAL_REVIEW_PACKET.md
Get-Content -Raw 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\LJ_FINAL_PCB_REVIEW_CHECKLIST.md
Get-Content -Raw 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\PCB_FINAL_UNCONNECTED_ITEMS_REVIEW.md
git status --short
git branch --show-current
Get-Content -Raw .gitignore
Get-ChildItem -Name
rg -n "PROMPT_COUNTER" 03_TOOLS 00_CODEX_START 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE -g "*.py" -g "*.md"
rg -n "build_current_known_problems|build_memory_index|build_history_index|AI_QUALITY_INDEX|CURRENT_KNOWN_PROBLEMS" 03_TOOLS -g "*.py" -g "*.md"
python 03_TOOLS\scripts\memory_maintenance\increment_prompt_counter.py --help
git diff --stat -- README.md .github\README.md
python -  # markdown-link validation helper
Get-Content "FOR CHAT GPT.MD" -TotalCount 60
python 03_TOOLS\scripts\memory_maintenance\increment_prompt_counter.py --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE --reason "GitHub README workflow rewrite session" --apply
python 03_TOOLS\scripts\indexing\build_memory_index.py --repo-root .
python 03_TOOLS\scripts\indexing\build_history_index.py --repo-root .
python 03_TOOLS\scripts\ai_quality\build_ai_quality_index.py --repo-root .
python 03_TOOLS\scripts\ai_quality\build_current_known_problems.py --repo-root .
git status --short
```

## Notes

- Manual file edits were applied with `apply_patch`, not shell redirection.
- No KiCad design files were opened for editing.
