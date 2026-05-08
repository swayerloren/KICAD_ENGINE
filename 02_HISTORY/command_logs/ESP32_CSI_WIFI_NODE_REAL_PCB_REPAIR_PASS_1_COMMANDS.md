# ESP32_CSI_WIFI_NODE_REAL_PCB_REPAIR_PASS_1_COMMANDS

Date: `2026-05-08`

## Commands

```powershell
python 03_TOOLS\scripts\memory_maintenance\check_maintenance_due.py --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE
```

```powershell
Get-Item 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb | Select-Object FullName, Length, LastWriteTime
Get-FileHash 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb -Algorithm SHA256
python 03_TOOLS\scripts\project_gate\check_phase_allowed.py --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE --phase 2
python 03_TOOLS\scripts\project_gate\check_phase_allowed.py --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE --phase 3
```

```powershell
Copy-Item 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb 99_BACKUPS\pre_codex_edits\20260508_065905_ESP32_CSI_WIFI_NODE_real_pcb_repair_pass_1
Copy-Item 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pro 99_BACKUPS\pre_codex_edits\20260508_065905_ESP32_CSI_WIFI_NODE_real_pcb_repair_pass_1
```

```powershell
& 'C:\Program Files\KiCad\9.0\bin\python.exe' -
```

Inline KiCad Python result:

- loaded the real board
- confirmed `U2` exposed-pad thermal-via drill is `0.20 mm`
- added `REAL_PCB_REPAIR_PASS_1_GND_F`
- added `REAL_PCB_REPAIR_PASS_1_GND_B`
- refilled zones
- saved the live `.kicad_pcb`

```powershell
kicad-cli pcb drc --format json --severity-all --units mm --output 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\REAL_PCB_REPAIR_PASS_1_DRC.json 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb
python 03_TOOLS\scripts\project_state\build_live_project_state.py --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE --apply
python 03_TOOLS\scripts\project_gate\check_phase_allowed.py --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE --phase 8
```

```powershell
kicad-cli pcb export svg --mode-single --page-size-mode 2 --exclude-drawing-sheet --layers F.Cu,F.Mask,F.SilkS,F.Fab,Edge.Cuts --output 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\pcb_visual\real_pcb_repair_pass_1_top.svg 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb
kicad-cli pcb export svg --mode-single --page-size-mode 2 --exclude-drawing-sheet --mirror --layers B.Cu,B.Mask,B.SilkS,B.Fab,Edge.Cuts --output 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\pcb_visual\real_pcb_repair_pass_1_bottom.svg 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb
& 'C:\Program Files\Inkscape\bin\inkscape.exe' 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\pcb_visual\real_pcb_repair_pass_1_top.svg --export-type=png --export-width=2400 --export-filename=04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\pcb_visual\real_pcb_repair_pass_1_top.png
& 'C:\Program Files\Inkscape\bin\inkscape.exe' 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\pcb_visual\real_pcb_repair_pass_1_bottom.svg --export-type=png --export-width=2400 --export-filename=04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\pcb_visual\real_pcb_repair_pass_1_bottom.png
```

## Notable Output

- before PCB hash: `0CFE639213D3B0A111F5D06E728A3F7F34B55674DC27312B00D39F80235B2844`
- after PCB hash: `1944B6DDFA7B233B8C231F5441D68B827FA3416B5C0B58A3004DE5C63C797FAC`
- DRC after repair: `0` violations, `65` unconnected items
- routing phase 8 remains `BLOCKED`
