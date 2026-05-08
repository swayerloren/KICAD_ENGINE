# ESP32_CSI_WIFI_NODE Intelligence-Based Placement Repair Commands

Date: 2026-05-07

## Commands Run

```powershell
& 'C:\Program Files\KiCad\9.0\bin\python.exe' '03_TOOLS\scripts\kicad_pcb_intelligence\repair_esp32_csi_wifi_node_placement.py'
```

Result: first run exposed a KiCad Python API ordering issue; script was patched to place footprints before redrawing Edge.Cuts.

```powershell
& 'C:\Program Files\KiCad\9.0\bin\python.exe' '03_TOOLS\scripts\kicad_pcb_intelligence\repair_esp32_csi_wifi_node_placement.py'
```

Result: placement saved. Final board outline reported by script: `55.0 x 90.0 mm`. Footprints placed: `43`.

```powershell
kicad-cli pcb drc --schematic-parity --severity-all --format report --output 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\PCB_INTELLIGENCE_BASED_DRC_REPORT.rpt 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb
```

Result: `18` DRC violations, `78` unconnected items, `0` schematic parity issues.

```powershell
kicad-cli pcb export svg --mode-single --page-size-mode 2 --exclude-drawing-sheet --layers F.Cu,F.Mask,F.Silkscreen,F.Courtyard,F.Fab,Edge.Cuts --output 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\pcb_visual\intelligence_based_placement_top.svg 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb
```

Result: top SVG exported.

```powershell
kicad-cli pcb export svg --mode-single --mirror --page-size-mode 2 --exclude-drawing-sheet --layers B.Cu,B.Mask,B.Silkscreen,B.Courtyard,B.Fab,Edge.Cuts --output 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\pcb_visual\intelligence_based_placement_bottom.svg 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb
```

Result: bottom SVG exported.

```powershell
kicad-cli pcb render --side top --width 1800 --height 2400 --background opaque --quality basic --output 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\pcb_visual\intelligence_based_placement_3d_top.png 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb
```

Result: top 3D PNG exported.

## Safety Notes

- No routing was performed.
- No zones were created.
- No fabrication outputs were generated.
