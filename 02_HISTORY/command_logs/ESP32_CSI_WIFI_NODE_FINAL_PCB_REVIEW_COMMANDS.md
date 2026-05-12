# ESP32_CSI_WIFI_NODE Final PCB Review Commands

Date: `2026-05-10`

Project: `ESP32_CSI_WIFI_NODE`

## Commands Run

1. Report and history discovery
   - `Get-ChildItem -Force "04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports" | Where-Object { $_.Name -like 'FINAL*' -or $_.Name -like 'LJ_FINAL*' -or $_.Name -like 'REMAINING_BEFORE*' } | Select-Object Name,Length,LastWriteTime`
   - `Get-ChildItem -Force "04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/_verification/pcb_visual" | Where-Object { $_.Name -like 'FINAL*' } | Select-Object Name,Length,LastWriteTime`
   - `Get-ChildItem -Force "02_HISTORY/sessions" | Where-Object { $_.Name -like '*FINAL*PCB*REVIEW*' } | Select-Object Name,LastWriteTime`
   - `Get-ChildItem -Force "02_HISTORY/command_logs" | Where-Object { $_.Name -like '*FINAL*PCB*REVIEW*' } | Select-Object Name,LastWriteTime`

2. Contract and closeout support discovery
   - `rg -n "execution_contract|task contract|VALID_TASK_CONTRACT" 03_TOOLS 02_HISTORY 00_CODEX_START -g "*.md" -g "*.py"`
   - `Get-Content -Raw "03_TOOLS/scripts/execution_contract/README.md"`
   - `Get-Content -Raw "02_HISTORY/sessions/2026-05-10_real_routing_apply_from_rehearsal_block_task_contract.json"`

3. Live evidence reads
   - `Get-Content -Raw "04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/memory/CURRENT_BLOCKERS.md"`
   - `Get-Content -Raw "04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/memory/PROJECT_MEMORY.md"`
   - `Get-Content -Raw "01_MEMORY/DESIGN_RULES_MEMORY.md"`
   - `Get-Content -Raw "FOR CHAT GPT.MD"`
   - `Get-Content -Raw "04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/pcb_quality_gate/20260510_quality_gate_creation_v2/pcb_quality_gate_result.json"`
   - `Get-Content -Raw "04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/mechanical_orientation/20260510_usb_c_orientation_audit.json"`
   - `Get-Content -Raw "04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/mechanical_orientation/20260510_barrel_jack_orientation_audit.json"`
   - `Get-Content -Raw "04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/mechanical_orientation/20260510_esp32_antenna_orientation_audit.json"`
   - `Get-Content -Raw "04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/SCHEMATIC_ERC_AFTER_VISUAL_CLEANUP.md"`
   - `Get-Content -Raw "04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/SCHEMATIC_READY_FOR_PCB_UPDATE_GATE.md"`

4. Hash checks
   - `Get-FileHash "04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_pcb" -Algorithm SHA256 | Select-Object Hash,Path`
   - `Get-FileHash "04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_sch" -Algorithm SHA256 | Select-Object Hash,Path`
   - `Get-FileHash "04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_pro" -Algorithm SHA256 | Select-Object Hash,Path`

5. Contract validation and report
   - `python 03_TOOLS/scripts/execution_contract/validate_task_contract.py --contract 02_HISTORY/sessions/2026-05-10_esp32_csi_wifi_node_final_pcb_review_task_contract.json`
   - `python 03_TOOLS/scripts/execution_contract/write_task_contract_report.py --contract 02_HISTORY/sessions/2026-05-10_esp32_csi_wifi_node_final_pcb_review_task_contract.json --output 02_HISTORY/sessions/2026-05-10_esp32_csi_wifi_node_final_pcb_review_task_contract_report.md`

6. Final KiCad diff check
   - `git diff --name-only -- "*.kicad_sch" "*.kicad_pcb" "*.kicad_pro"`
   - `git status --short --untracked-files=no -- "*.kicad_sch" "*.kicad_pcb" "*.kicad_pro"`

7. Index rebuilds
   - `python 03_TOOLS/scripts/indexing/build_memory_index.py --repo-root .`
   - `python 03_TOOLS/scripts/indexing/build_history_index.py --repo-root .`
   - `python 03_TOOLS/scripts/ai_quality/build_ai_quality_index.py --repo-root .`
   - `python 03_TOOLS/scripts/indexing/build_known_problems.py --repo-root .`

## Key Results

- Task contract validated as `VALID_TASK_CONTRACT`.
- Live KiCad hashes stayed:
  - PCB `ACA326C7B7C96AA67FED119E8DF54BDEBF80148C6B5F34F998780137C2BA1DD1`
  - SCH `A82DD63FBD226227F777677D6EF5491BC9EAF27411A369C13A24C014F82F24E6`
  - PRO `CE1853F7614F591B5AF042ECBCF17ACC3BEB3D97091540B7B913D949900532D5`
- `git diff` still shows the schematic as dirty from earlier work, but its hash
  did not change during this audit.
