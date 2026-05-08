# ESP32_CSI_WIFI_NODE_LIVE_PCB_TRUTH_AUDIT_SESSION

Date: `2026-05-07`

## Summary

Ran a read-only live PCB truth audit on `ESP32_CSI_WIFI_NODE` and reconciled stale project reports against the actual `ESP32_CSI_WIFI_NODE.kicad_pcb` file.

## Result

- target PCB exists: `YES`
- PCB hash captured: `YES`
- PCB timestamp captured: `YES`
- live board parsed: `YES`
- board outline exists: `YES`
- footprints present: `YES`
- placement exists: `YES`
- routing exists: `YES_PARTIAL`
- KiCad design files edited: `NO`
- fabrication outputs generated: `NO`
- final classification: `PCB_EXISTS_PARTIAL_ROUTING_EXISTS_NEEDS_AUDIT`

## Key Live Facts

- SHA256: `0CFE639213D3B0A111F5D06E728A3F7F34B55674DC27312B00D39F80235B2844`
- Timestamp: `2026-05-07 16:28:37 -04:00`
- Board size: `60.0 mm x 95.0 mm`
- Footprints: `43`
- Mounting holes: `4`
- Tracks: `24`
- Vias: `2`
- Zones: `0`
- Detectable unrouted nets: `16`
- DRC result: `FAIL`
- DRC violations: `12`
- Unconnected items: `65`

## Reconciled Report Drift

The audit confirmed that several reports had become stale as factual status documents:

- `PCB_PLACEMENT_PASS_1_REPORT.md`
- `AUTO_PCB_START_REPORT.md`
- `PCB_LAYOUT_SANDBOX_GATE_STATUS.md`
- `CURRENT_PCB_PLACEMENT_REJECTION_REPORT.md`
- `PCB_INTELLIGENCE_BASED_PLACEMENT_REPAIR_REPORT.md`
- `PCB_INTELLIGENCE_BASED_DRC_REPORT.md`

New or refreshed live-state reports now document the actual board state without falsely promoting any blocked phase gates to `PASS`.

## Formal Gate State After Reconciliation

`check_phase_allowed.py` was rerun after the report updates.

- Phase 2: `BLOCKED`
- Phase 3: `BLOCKED`
- Phase 5: `BLOCKED`
- Phase 8: `BLOCKED`

Reason: the authoritative schematic-to-PCB gate is still exact `FAIL`, so the truth audit corrected live-state drift but did not override the formal phase workflow.

## Safety

No `.kicad_sch`, `.kicad_pcb`, `.kicad_pro`, symbol library, footprint library, or manufacturing output files were modified in this task.
