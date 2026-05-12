# Schematic Quality Engine Follow-Up Items

Date: `2026-05-10`
Status: `OPEN`

## Open Items

- Clear KiCad-native annotation proof for `ESP32_CSI_WIFI_NODE`; current gate
  still reports `FAIL_NOT_GUI_VERIFIED`.
- Replace visible `NEEDS_REVIEW` values on `D3`, `U1`, and `J2` with reviewed
  final values before claiming PCB-update readiness.
- Resolve visible text-placement issues around the `U2` `+3V3` area and rerun
  the schematic-quality gate.
- Complete human close-up schematic review; automated crop generation alone is
  not enough.
- Consider future refinement of text-overlap geometry using richer symbol shape
  extraction, while keeping the current heuristic audit read-only and
  conservative.
