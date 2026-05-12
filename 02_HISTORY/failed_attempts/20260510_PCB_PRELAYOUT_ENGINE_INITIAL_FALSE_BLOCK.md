# Failed Attempt - PCB Prelayout Engine Initial False Block

Date: `2026-05-10`

## Attempt

Ran the first dry-run of:

```powershell
python 03_TOOLS\scripts\pcb_prelayout\run_prelayout_gate.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE
```

against the live `ESP32_CSI_WIFI_NODE` board.

## Result

- The first pass produced `0` passing variants.
- The engine was over-blocking because:
  - synthetic `UNCONNECTED-*` nets were still being treated like required route targets
  - projected-route anchors were too courtyard-driven
  - outside-board and overlap heuristics were too strict for edge connectors and non-critical pairs

## Resolution

- Ignored synthetic `UNCONNECTED-*` nets in route projection.
- Switched projected-route anchors to component placement centers instead of oversized courtyard geometry.
- Tightened hard-fail overlap handling so it focuses on real critical pairs.
- Reran the gate successfully.

## Final Outcome

The corrected run produced `3` variants, `1` passing variant, and a blocked routing gate for the correct live-board reason: `13` unconnected items and `3` detectable unrouted nets.
