# Copper Pour Request Blocked Commands

Date: `2026-05-10`
Project: `ESP32_CSI_WIFI_NODE`

## Commands Run

- `python 03_TOOLS/scripts/maintenance/run_maintenance_cycle.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE`
- `python 03_TOOLS/scripts/memory_maintenance/increment_prompt_counter.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --apply`
- `python 03_TOOLS/scripts/memory_maintenance/check_maintenance_due.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE`
- `Get-Content START_HERE_FOR_AI_AGENTS.md`
- `Get-Content 00_CODEX_START/TASK_ROUTER.md`
- `Get-Content 00_CODEX_START/TASK_TYPE_TO_REQUIRED_DOCS.md`
- `Get-Content 00_CODEX_START/TASK_TYPE_TO_BLOCKERS.md`
- `Get-Content 00_CODEX_START/PROMPT_COUNTER_RULES.md`
- `Get-Content 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/REAL_PCB_STAGED_ROUTING_REPORT.md`
- `Get-Content 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/pcb_intelligence/COPPER_ZONE_STRATEGY.md`
- `Get-Content 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/pcb_intelligence/ESP32_RF_KEEP_OUT_PLAN.md`
- `Get-Content 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/pcb_intelligence/VIA_AND_LAYER_STRATEGY.md`
- `Get-Content 34_PCB_LAYOUT_SANDBOX/RF_ANTENNA_KEEP_OUT_RULES.md`
- parsed `reports/pcb_quality_gate/20260510_quality_gate_creation_v2/pcb_quality_gate_result.json`
- `Get-FileHash 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_pcb -Algorithm SHA256`
- `Get-FileHash 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_sch -Algorithm SHA256`
- `Get-FileHash 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_pro -Algorithm SHA256`
- `git diff --name-only -- '*.kicad_sch' '*.kicad_pcb' '*.kicad_pro'`

## Important Results

- maintenance completed first and reset the prompt counter
- the live staged-routing report still says `REAL_ROUTING_BLOCKED`
- no copper-pour edit path was allowed to start
