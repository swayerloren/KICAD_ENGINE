# ESP32_CSI_WIFI_NODE_REAL_PCB_ROUTING_PLAN_BLOCKER_AUDIT_COMMANDS

Date: `2026-05-07`

## Commands Run

```powershell
python 03_TOOLS/scripts/memory_maintenance/check_maintenance_due.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE
python 03_TOOLS/scripts/project_gate/check_phase_allowed.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --phase 8
```

```powershell
Get-Content 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/PCB_PLACEMENT_PASS_1_REPORT.md -Raw
Test-Path 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/PCB_PLACEMENT_ORIENTATION_REVIEW.md
Get-Content 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/SCHEMATIC_TO_PCB_GATE_STATUS.md -Raw
Get-Content 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/PCB_LAYOUT_SANDBOX_GATE_STATUS.md -Raw
```

```powershell
python 14_LAYOUT_AUTOMATION/scripts/extract_kicad_pcb_to_routing_schema.py 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_pcb 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/REAL_PCB_ROUTING_SCHEMA.json --markdown 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/REAL_PCB_ROUTING_SCHEMA.md
```

```powershell
python 14_LAYOUT_AUTOMATION/scripts/run_real_board_routing_audit.py 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_pcb 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/real_board_routing_audit --report-json 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/real_board_routing_audit_summary.json --report-markdown 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/real_board_routing_audit_summary.md
```
