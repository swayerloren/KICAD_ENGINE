# PCB ESP Routing And Via Repair Commands

Date: `2026-05-09`

## Key commands

```powershell
git status --short
```

```powershell
Get-Content AGENTS.md -TotalCount 220
Get-Content 00_CODEX_START\START_HERE.md -TotalCount 220
Get-Content 00_CODEX_START\KICAD_PHASE_ORDER.md -TotalCount 220
Get-Content 00_CODEX_START\CURRENT_PROJECT.md -TotalCount 220
```

```powershell
Get-Content 03_TOOLS\scripts\pcb_routing\esp32_csi_esp_routing_via_repair_20260509.py
Get-Content 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\memory\PROMPT_COUNTER.md
Get-Content 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\history\quality_gate_failures\2026-05-09_esp_routing_via_user_override_exception.md
```

```powershell
Copy-Item 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\backups\ESP32_CSI_WIFI_NODE_esp_routing_20260509_150640.kicad_pcb $env:TEMP\ESP32_CSI_esp_trial_project_20260509*\ESP32_CSI_WIFI_NODE.kicad_pcb
```

```powershell
& 'C:\Program Files\KiCad\9.0\bin\python.exe' 03_TOOLS\scripts\pcb_routing\esp32_csi_esp_routing_via_repair_20260509.py <trial_board> apply
kicad-cli pcb drc --format json --output <trial_drc.json> <trial_board>
```

```powershell
Copy-Item 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\backups\ESP32_CSI_WIFI_NODE_esp_routing_20260509_150640.kicad_pcb 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb -Force
& 'C:\Program Files\KiCad\9.0\bin\python.exe' 03_TOOLS\scripts\pcb_routing\esp32_csi_esp_routing_via_repair_20260509.py 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb apply
kicad-cli pcb drc --format json --output 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\PCB_ESP_ROUTING_AND_VIA_REPAIR_DRC.json 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb
```

```powershell
git diff --stat
git diff --name-only -- '*.kicad_sch'
```

## Outcome summary

- Accepted copied-board-proven subset only
- Live DRC result: `0` violations, `13` unconnected items
- No `.kicad_sch` changes detected
