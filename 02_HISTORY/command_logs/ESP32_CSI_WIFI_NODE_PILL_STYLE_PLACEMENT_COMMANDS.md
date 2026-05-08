# ESP32_CSI_WIFI_NODE Pill-Style Placement Command Log

Date: 2026-05-07

## Commands / Tooling Used

```powershell
Get-Content AGENTS.md
Get-Content README_GPT.md
Get-Content 'FOR CHAT GPT.MD'
Get-Content reports/PCB_SELECTED_DEV_BOARD_LAYOUT_SPEC.md
Get-Content reports/CURRENT_PCB_PLACEMENT_REJECTION_REPORT.md
Get-Content reports/PCB_SYNC_STATUS.md
```

Purpose: required startup and project evidence reads.

```powershell
Copy-Item ... 99_BACKUPS/pre_codex_edits/20260507_110816_ESP32_CSI_WIFI_NODE_pre_pill_style_placement
```

Purpose: pre-edit backup.

```powershell
Get-Process -Name kicad | Where-Object { $_.MainWindowTitle -like '*ESP32_CSI_WIFI_NODE*' } | ForEach-Object { $_.CloseMainWindow() }
```

Purpose: close KiCad main window after backup to avoid GUI overwrite during file-based placement.

```powershell
& 'C:\Program Files\KiCad\9.0\bin\python.exe' -
```

Purpose: KiCad `pcbnew` Python API placement edits. Used to reset Edge.Cuts to `38 x 80 mm`, move footprints, reduce reference text, and save the PCB. No routing or zones were created.

```powershell
& 'C:\Program Files\KiCad\9.0\bin\kicad-cli.exe' pcb drc --schematic-parity --severity-all --format report --output reports/PCB_PILL_STYLE_DRC_REPORT.rpt kicad/ESP32_CSI_WIFI_NODE.kicad_pcb
```

Purpose: DRC after placement. Final console result: `Found 73 violations`, `Found 78 unconnected items`, `Found 0 schematic parity issues`.

```powershell
& 'C:\Program Files\KiCad\9.0\bin\kicad-cli.exe' pcb export svg ...
```

Purpose: top/bottom PCB review SVG exports.

```powershell
& 'C:\Program Files\Google\Chrome\Application\chrome.exe' --headless --screenshot=...
```

Purpose: converted SVG review images to PNG for visual inspection.

```powershell
& 'C:\Program Files\KiCad\9.0\bin\kicad-cli.exe' pcb render --output _verification/pcb_visual/pill_style_placement_3d_top.png ...
```

Purpose: 3D review PNG export. This is not STEP and not a manufacturing output.

## KiCad Design File Edits

Edited:

- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_pcb`

Not edited:

- Schematic files
- Project file
- Libraries
- Manufacturing outputs

## Routing / Zones / Fabrication

- Routed traces: `NO`
- Created zones: `NO`
- Exported Gerbers/drills/BOM/CPL/STEP: `NO`
