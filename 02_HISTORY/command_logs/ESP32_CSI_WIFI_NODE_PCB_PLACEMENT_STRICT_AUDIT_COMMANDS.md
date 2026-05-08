# ESP32_CSI_WIFI_NODE PCB Placement Strict Audit Commands

Date: 2026-05-07

## Commands Run

```powershell
Get-ChildItem '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\PCB_PLACEMENT_REAL_LAYOUT_REPORT.md','04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\PCB_PLACEMENT_DRC_REPORT.md','04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\PCB_PLACEMENT_ORIENTATION_RISK_REPORT.md' -ErrorAction SilentlyContinue
```

Result: Only `PCB_PLACEMENT_ORIENTATION_RISK_REPORT.md` existed.

```powershell
Get-Content '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\PCB_PLACEMENT_DRC_REPORT.rpt' -TotalCount 120
```

Result: Latest DRC report was available and showed 26 DRC violations, 78 unconnected items, and 0 schematic parity issues.

```powershell
& 'C:\Program Files\KiCad\9.0\bin\python.exe' -
```

Result: Read-only KiCad Python inspection confirmed board outline bbox `(0.0,0.0)` to `(100.0,65.0)`, 43 footprints, mounting holes at the requested coordinates, and no footprints far outside/away from the board.

```powershell
Select-String -Path '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\PCB_PLACEMENT_DRC_REPORT.rpt' -Pattern '^\[([^\]]+)\]'
```

Result: DRC categories were `unconnected_items: 78`, `drill_out_of_range: 12`, `silk_over_copper: 9`, and `silk_overlap: 5`.

```powershell
& 'C:\Program Files\Google\Chrome\Application\chrome.exe' --headless --disable-gpu --window-size=1600,1100 --screenshot=... placement_real_layout_top.svg
& 'C:\Program Files\Google\Chrome\Application\chrome.exe' --headless --disable-gpu --window-size=1600,1100 --screenshot=... placement_real_layout_bottom.svg
```

Result: Created PNG review images from the existing KiCad SVG visual exports for audit viewing.

## KiCad Design File Edits

None during this audit session.
