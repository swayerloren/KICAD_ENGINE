# ESP32_CSI_WIFI_NODE Bottom Edge Connector Repair Session

Status: `ACTIVE_BLOCKER`

Generated: `2026-05-07T12:56:21-04:00`

Project: `ESP32_CSI_WIFI_NODE`

## Summary

Performed placement-only connector repair after LJ correction that J1 and J2 must be on the bottom edge and face down/off-board unless impossible.

## Actions

- Incremented prompt counter to `2`; maintenance not due.
- Created backup under `99_BACKUPS/pre_codex_edits`.
- Added and ran `03_TOOLS/scripts/kicad_pcb_intelligence/repair_esp32_csi_wifi_node_bottom_edge_connectors.py`.
- Set board outline to `60.0 mm x 95.0 mm`.
- Placed J2 USB-C at the bottom edge.
- Attempted and placed J1 barrel jack at the bottom-left edge.
- Moved test pads to a right-side service row.
- Adjusted USB and power support clusters.
- Ran KiCad DRC.
- Exported top/bottom SVG and 3D PNG review images.

## Result

`BLOCKED_BY_MECHANICAL_OR_FOOTPRINT_RISK`

J2 orientation is proven. J1 bottom-edge 2D placement is proven, but J1 3D orientation proof is blocked because the installed KiCad model library lacks the referenced barrel jack STEP model.
