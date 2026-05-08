# Placement Readiness Scoring Commands

Date: `2026-05-08`

## Commands Run

```powershell
python 03_TOOLS/scripts/memory_maintenance/check_maintenance_due.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE
Get-Content 14_LAYOUT_AUTOMATION/AUTO_PLACEMENT_ENGINE.md
Get-Content 14_LAYOUT_AUTOMATION/PLACEMENT_CONSTRAINTS_SCHEMA.md
Get-Content 14_LAYOUT_AUTOMATION/PLACEMENT_DRC_PRECHECK_RULES.md
Get-Content 14_LAYOUT_AUTOMATION/FIXED_MECHANICAL_PLACEMENT_RULES.md
Get-Content 14_LAYOUT_AUTOMATION/POWER_PATH_PLACEMENT_RULES.md
Get-Content 14_LAYOUT_AUTOMATION/USB_PLACEMENT_RULES.md
Get-Content 14_LAYOUT_AUTOMATION/RF_ANTENNA_PLACEMENT_RULES.md
Get-Content 14_LAYOUT_AUTOMATION/scripts/*.py
python 14_LAYOUT_AUTOMATION/scripts/extract_kicad_pcb_to_routing_schema.py 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_pcb %TEMP%/esp32_csi_live_schema_probe.json
& 'C:\Program Files\KiCad\9.0\bin\python.exe' -
python -m py_compile 14_LAYOUT_AUTOMATION/scripts/_placement_common.py 14_LAYOUT_AUTOMATION/scripts/score_placement_readiness.py 14_LAYOUT_AUTOMATION/scripts/detect_*.py
Copy-Item 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_pcb %TEMP%/kicad_engine_placement_readiness/ESP32_CSI_WIFI_NODE_copy.kicad_pcb
python 14_LAYOUT_AUTOMATION/scripts/score_placement_readiness.py %TEMP%/kicad_engine_placement_readiness/ESP32_CSI_WIFI_NODE_copy.kicad_pcb %TEMP%/kicad_engine_placement_readiness/PLACEMENT_READINESS_SCORECARD.json --markdown 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/PLACEMENT_READINESS_SCORECARD.md
git status -sb
git rev-parse HEAD
```
