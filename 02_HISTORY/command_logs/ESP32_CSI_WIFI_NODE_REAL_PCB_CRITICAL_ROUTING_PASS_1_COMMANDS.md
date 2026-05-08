# ESP32_CSI_WIFI_NODE Real PCB Critical Routing Pass 1 Commands

## Key Commands

```powershell
Get-FileHash 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb -Algorithm SHA256
```

```powershell
python 03_TOOLS\scripts\project_gate\check_phase_allowed.py --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE --phase 8
python 03_TOOLS\scripts\memory_maintenance\check_maintenance_due.py --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE
```

```powershell
python -m py_compile 03_TOOLS\scripts\pcb_routing\esp32_csi_critical_route_pass_1.py
```

```powershell
& 'C:\Program Files\KiCad\9.0\bin\python.exe' 03_TOOLS\scripts\pcb_routing\esp32_csi_critical_route_pass_1.py <copied-board>
kicad-cli pcb drc --format json --severity-all --units mm --output <trial>\trial_drc.json <copied-board>
```

Copied-board rehearsal summary:

- `trial_apply` -> `92` violations, `29` unconnected
- `trial_apply_v2` -> `23` violations, `34` unconnected
- `trial_apply_v3` -> `2` violations, `48` unconnected
- `trial_apply_v4` -> `3` violations, `48` unconnected
- `trial_apply_v5` -> `0` violations, `49` unconnected

```powershell
& 'C:\Program Files\KiCad\9.0\bin\python.exe' 03_TOOLS\scripts\pcb_routing\esp32_csi_critical_route_pass_1.py 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb
```

Live apply result:

- `TRACKS_ADDED=16`
- `VIAS_ADDED=23`
- nets touched live: `+3V3`, `GND`

```powershell
kicad-cli pcb drc --format json --severity-all --units mm --output 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\REAL_PCB_CRITICAL_ROUTING_PASS_1_DRC.json 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb
```

Live DRC result:

- `0` violations
- `49` unconnected items

```powershell
kicad-cli pcb export svg --mode-single --page-size-mode 2 --exclude-drawing-sheet --layers F.Cu,F.Mask,F.SilkS,F.Fab,Edge.Cuts --output 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\pcb_visual\real_pcb_critical_routing_pass_1_top.svg 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb
kicad-cli pcb export svg --mode-single --page-size-mode 2 --exclude-drawing-sheet --mirror --layers B.Cu,B.Mask,B.SilkS,B.Fab,Edge.Cuts --output 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\pcb_visual\real_pcb_critical_routing_pass_1_bottom.svg 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb
& 'C:\Program Files\Inkscape\bin\inkscape.exe' 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\pcb_visual\real_pcb_critical_routing_pass_1_top.svg --export-type=png --export-width=2400 --export-filename=04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\pcb_visual\real_pcb_critical_routing_pass_1_top.png
& 'C:\Program Files\Inkscape\bin\inkscape.exe' 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\pcb_visual\real_pcb_critical_routing_pass_1_bottom.svg --export-type=png --export-width=2400 --export-filename=04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\pcb_visual\real_pcb_critical_routing_pass_1_bottom.png
```
