# ESP32_CSI_WIFI_NODE NOT_FINAL Export Gate Commands

Date: `2026-05-10`

Project: `ESP32_CSI_WIFI_NODE`

## Commands Run

1. Startup/router/fab rule reads
   - `Get-Content -Raw "START_HERE_FOR_AI_AGENTS.md"`
   - `Get-Content -Raw "00_CODEX_START/TASK_ROUTER.md"`
   - `Get-Content -Raw "00_CODEX_START/TASK_TYPE_TO_REQUIRED_DOCS.md"`
   - `Get-Content -Raw "24_FAB_PROFILES/README.md"`
   - `Get-Content -Raw "17_RELEASE_BUILD/README.md"`
   - `Get-Content -Raw "09_ACCURACY_ENGINE/checklists/PCBA_EXPORT_GATE_CHECKLIST.md"`

2. Project gate-state reads
   - `Get-Content -Raw "04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/memory/PROMPT_COUNTER.md"`
   - `Get-Content -Raw "04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/FINAL_ROUTED_PCB_REVIEW.md"`
   - `Get-Content -Raw "04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/REMAINING_BEFORE_NOT_FINAL_EXPORT.md"`

3. Live hash and manufacturing-folder checks
   - `Get-Date -Format o`
   - `Get-FileHash "04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_pcb" -Algorithm SHA256 | Select-Object Hash`
   - `Get-FileHash "04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_sch" -Algorithm SHA256 | Select-Object Hash`
   - `Get-FileHash "04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_pro" -Algorithm SHA256 | Select-Object Hash`
   - `Test-Path "04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/manufacturing/rev_A"`
   - `Get-ChildItem "04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports" | Where-Object { $_.Name -like '*EXPORT*' -or $_.Name -like '*BOM_CPL*' -or $_.Name -like '*ORIENTATION_POLARITY*' } | Select-Object Name`

4. Contract validation
   - `python 03_TOOLS/scripts/execution_contract/validate_task_contract.py --contract 02_HISTORY/sessions/2026-05-10_esp32_csi_wifi_node_not_final_export_gate_task_contract.json`
   - `python 03_TOOLS/scripts/execution_contract/write_task_contract_report.py --contract 02_HISTORY/sessions/2026-05-10_esp32_csi_wifi_node_not_final_export_gate_task_contract.json --output 02_HISTORY/sessions/2026-05-10_esp32_csi_wifi_node_not_final_export_gate_task_contract_report.md`

5. Final KiCad diff check
   - `git diff --name-only -- "*.kicad_sch" "*.kicad_pcb" "*.kicad_pro"`
   - `git status --short --untracked-files=no -- "*.kicad_sch" "*.kicad_pcb" "*.kicad_pro"`

6. Index rebuilds
   - `python 03_TOOLS/scripts/indexing/build_memory_index.py --repo-root .`
   - `python 03_TOOLS/scripts/indexing/build_history_index.py --repo-root .`
   - `python 03_TOOLS/scripts/ai_quality/build_ai_quality_index.py --repo-root .`
   - `python 03_TOOLS/scripts/indexing/build_known_problems.py --repo-root .`
