# ESP32_CSI_WIFI_NODE_REAL_PCB_UPDATE_FROM_SCHEMATIC_COMMANDS

Date: `2026-05-07`

## Commands Run

```powershell
python 03_TOOLS/scripts/memory_maintenance/check_maintenance_due.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE
```

```powershell
Test-Path 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_pro
Test-Path 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_sch
Test-Path 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_pcb
```

```powershell
Get-Content 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/SCHEMATIC_TO_PCB_GATE_STATUS.md -Raw
Get-Content 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/PCB_LAYOUT_SANDBOX_GATE_STATUS.md -Raw
Get-Content 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/layout_sandbox/AUTO_APPROVAL_REPORT.md -Raw
```

```powershell
python 03_TOOLS/scripts/project_gate/check_phase_allowed.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --phase 2
```

```powershell
Get-FileHash 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_pcb -Algorithm SHA256
Get-Item 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_pcb | Select-Object FullName, LastWriteTime
```
