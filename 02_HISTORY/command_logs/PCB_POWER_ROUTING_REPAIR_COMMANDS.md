# PCB Power Routing Repair Commands

Date: `2026-05-09`

Project: `ESP32_CSI_WIFI_NODE`

## Commands Run

```powershell
rg -n "def iter_tracks|GetTracks\(|Tracks\(" 03_TOOLS\scripts\pcb_routing -S
Get-Content 03_TOOLS\scripts\pcb_routing\esp32_csi_power_routing_repair_20260509.py
```

```powershell
@'
import pcbnew
b = pcbnew.LoadBoard(...)
print(type(b.GetTracks()))
print(type(b.Tracks()))
'@ | & 'C:\Program Files\KiCad\9.0\bin\python.exe' -
```

```powershell
$trial = Join-Path $env:TEMP 'ESP32_CSI_power_trial_project_20260509c'
New-Item -ItemType Directory -Path $trial
Copy-Item 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb $trial
Copy-Item 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pro $trial
Copy-Item 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_prl $trial
```

```powershell
& 'C:\Program Files\KiCad\9.0\bin\python.exe' 03_TOOLS\scripts\pcb_routing\esp32_csi_power_routing_repair_20260509.py "$env:TEMP\ESP32_CSI_power_trial_project_20260509c\ESP32_CSI_WIFI_NODE.kicad_pcb" apply
kicad-cli pcb drc --format json --output "$env:TEMP\ESP32_CSI_power_trial_project_20260509c\trial_drc.json" "$env:TEMP\ESP32_CSI_power_trial_project_20260509c\ESP32_CSI_WIFI_NODE.kicad_pcb"
```

```powershell
git hash-object 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb
```

```powershell
& 'C:\Program Files\KiCad\9.0\bin\python.exe' 03_TOOLS\scripts\pcb_routing\esp32_csi_power_routing_repair_20260509.py 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb apply
kicad-cli pcb drc --format json --output 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\PCB_POWER_ROUTING_REPAIR_DRC.json 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb
git diff --stat -- 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch
git status --short -- 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch
git hash-object 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb
```

## Notes

- multiple copied-project trials were used while correcting the KiCad 9 SWIG track-iteration issue and the first live-pass DRC regressions
- final live result: `0 violations`, `17 unconnected items`
