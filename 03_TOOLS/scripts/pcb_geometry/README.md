# PCB Geometry Audit Tools

This folder contains the read-only PCB trace geometry audit surface for real KiCad boards.

## Purpose

KiCad DRC can prove spacing/connectivity classes, but it does not prove that routed copper is professionally shaped.

These tools exist to block false routing-acceptable claims when the board still has:

- right-angle corners
- acute-angle jogs
- zigzags or boxy perimeter routing
- excessive detour ratios
- long test-point stubs
- board-edge or RF-keepout crossings
- plane-splitting traces that can damage return paths

## Scripts

- `extract_tracks.py`
  - extracts the live board into a read-only geometry payload with real path branches, not only per-net segment buckets
- `audit_trace_angles.py`
  - detects 90-degree and acute-angle bends
- `audit_power_loop_geometry.py`
  - audits power-path detours, boxy loops, and return-path split risk
- `audit_usb_pair_geometry.py`
  - audits routed USB pair geometry for detours and ugly bends
- `audit_trace_quality.py`
  - runs the end-to-end geometry audit and writes the full report packet
- `render_trace_quality_overlays.py`
  - renders an SVG overlay for flagged geometry findings

## Canonical Workflow

```powershell
python 03_TOOLS\scripts\pcb_geometry\audit_trace_quality.py `
  --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE
```

Default output location:

- `04_KICAD_PROJECTS\active\<PROJECT>\reports\pcb_geometry\<timestamp>\`

Expected artifacts:

- `tracks.json`
- `trace_angles.json`
- `power_loop_geometry.json`
- `usb_pair_geometry.json`
- `trace_quality.json`
- `trace_quality_overlay.svg`

## Read-Only Guarantee

These scripts:

- read `.kicad_pcb` content
- write audit artifacts only
- do not route
- do not edit KiCad board or schematic source files

## Relationship To Existing Rules

This toolchain complements:

- `09_ACCURACY_ENGINE\pcb_rules\TRACE_ANGLE_ROUTING_RULES.md`
- `09_ACCURACY_ENGINE\pcb_rules\PCB_ROUTING_QUALITY_RULES.md`
- `09_ACCURACY_ENGINE\checklists\PCB_ROUTING_QUALITY_CHECKLIST.md`
- `14_LAYOUT_AUTOMATION\ROUTING_GEOMETRY_HARD_FAIL_RULES.md`

Routing is not acceptable just because DRC spacing is clean.
