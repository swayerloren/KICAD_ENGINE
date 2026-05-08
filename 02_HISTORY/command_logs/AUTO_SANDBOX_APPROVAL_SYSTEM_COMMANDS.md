# Auto Sandbox Approval System Commands

Date: `2026-05-07`

Workdir: `C:\Users\LJ\GitHub\KICAD_ENGINE`

## Commands Run

```powershell
python 03_TOOLS/scripts/memory_maintenance/increment_prompt_counter.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --apply
python 03_TOOLS/scripts/memory_maintenance/check_maintenance_due.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE
Get-FileHash '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb','04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch','04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pro' | ForEach-Object { "$($_.Path)|$($_.Hash)" }
Get-Content AGENTS.md
Get-Content README_GPT.md
Get-Content 'FOR CHAT GPT.MD'
Get-Content 00_CODEX_START\START_HERE.md
Get-Content 34_PCB_LAYOUT_SANDBOX\README.md
Get-Content 34_PCB_LAYOUT_SANDBOX\PCB_VARIANT_WORKFLOW.md
Get-Content 34_PCB_LAYOUT_SANDBOX\VARIANT_SCORING_RULES.md
Get-Content 34_PCB_LAYOUT_SANDBOX\HUMAN_REVIEW_GATE.md
Get-Content 09_ACCURACY_ENGINE\workflows\CREATE_PCB_WORKFLOW.md
Get-Content 09_ACCURACY_ENGINE\workflows\SCHEMATIC_TO_PCB_GATE_WORKFLOW.md
Get-Content 09_ACCURACY_ENGINE\checklists\FULL_PIPELINE_GATE_CHECKLIST.md
Get-Content 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\PCB_LAYOUT_SANDBOX_GATE_STATUS.md
Get-Content 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\memory\CURRENT_BLOCKERS.md
Get-Content 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\memory\CURRENT_PROJECT_STATE.md
Get-Content 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\layout_sandbox\SELECTED_LAYOUT_PLAN.md
Get-Content 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\layout_sandbox\VARIANT_COMPARISON_SCORECARD.md
Select-String -Path 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\FOOTPRINT_PACKAGE_GATE_REPORT.md -Pattern 'Gate result|blank footprint|High-risk|assigned|safe candidate|verified|human review|required' -Context 1,1
Select-String -Path 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\SCHEMATIC_TO_PCB_GATE_STATUS.md -Pattern 'Gate result|PCB layout sandbox|PASS|BLOCKED|FAIL' -Context 1,1
rg -n "LJ approved|LJ approval|selected layout plan" AGENTS.md README_GPT.md 'FOR CHAT GPT.MD' '00_CODEX_START\START_HERE.md' '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\PCB_LAYOUT_SANDBOX_GATE_STATUS.md' '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\memory\CURRENT_BLOCKERS.md' '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\memory\CURRENT_PROJECT_STATE.md'
python 03_TOOLS/scripts/indexing/build_repo_index.py
python 03_TOOLS/scripts/indexing/build_memory_index.py
python 03_TOOLS/scripts/indexing/build_history_index.py
python 03_TOOLS/scripts/ai_quality/build_ai_quality_index.py
python 03_TOOLS/scripts/indexing/build_known_problems.py
Get-FileHash '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb','04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch','04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pro' | ForEach-Object { "$($_.Path)|$($_.Hash)" }
```

## Notes

- One `rg` command used an invalid quoted glob path for `34_PCB_LAYOUT_SANDBOX\*.md`; this is recorded separately in `02_HISTORY/failed_attempts/AUTO_SANDBOX_APPROVAL_RG_GLOB_SEARCH_ERROR.md`.
- Index rebuild commands and the final KiCad file-hash check were rerun after late closeout edits so the generated indexes include the final command log and corrected project auto-block status.
- Final file-hash recheck matched the initial no-design-file baseline for the active project's `.kicad_pcb`, `.kicad_sch`, and `.kicad_pro`.
