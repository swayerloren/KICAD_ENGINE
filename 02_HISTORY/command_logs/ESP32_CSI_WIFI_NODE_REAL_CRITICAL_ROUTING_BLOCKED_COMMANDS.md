# ESP32_CSI_WIFI_NODE Real Critical Routing Blocked Commands

Date: `2026-05-07`

## Commands

```powershell
Get-Content -Raw AGENTS.md
Get-Content -Raw README_GPT.md
Get-Content -Raw 'FOR CHAT GPT.MD'
Get-Content -Raw '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\COPIED_BOARD_CRITICAL_ROUTING_REHEARSAL_REPORT.md'
Get-Content -Raw '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\REAL_PCB_ROUTING_PLAN.md'
Get-Content -Raw '14_LAYOUT_AUTOMATION\REAL_PROJECT_ROUTING_WORKFLOW.md'
Get-Content -Raw '14_LAYOUT_AUTOMATION\REAL_PROJECT_TRACE_BY_TRACE_REVIEW.md'
Get-Content -Raw '14_LAYOUT_AUTOMATION\REAL_PROJECT_ROUTING_STOP_CONDITIONS.md'
python 03_TOOLS/scripts/project_gate/check_phase_allowed.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --phase 8
python 03_TOOLS/scripts/memory_maintenance/check_maintenance_due.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE
Get-Content -Raw '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\memory\PROJECT_MEMORY.md'
```

## Key Results

- `COPIED_BOARD_CRITICAL_ROUTING_REHEARSAL_REPORT.md`: missing
- `REAL_PCB_ROUTING_PLAN.md`: `ROUTING_BLOCKED`
- Phase gate: `PHASE_GATE_RESULT: BLOCKED`
- Prompt counter: `0`, maintenance not due
