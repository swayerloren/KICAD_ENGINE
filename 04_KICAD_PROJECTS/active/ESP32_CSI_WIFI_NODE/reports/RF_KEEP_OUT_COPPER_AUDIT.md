# RF Keep-Out Copper Audit

Status: `NOT_RUN_BLOCKED`

Generated: `2026-05-07`

Project: `ESP32_CSI_WIFI_NODE`

## Result

No RF keepout copper audit could be performed on new copper because no copper zones were created.

## Existing RF Keepout Rule

`pcb_intelligence\ESP32_RF_KEEP_OUT_PLAN.md` states:

- `U2` must remain near the top edge with antenna/U.FL/RF keepout facing the top edge.
- No copper, traces, vias, test pads, mounting holes, or components are allowed in the RF keepout.
- Reports state `RF_Module:ESP32-S3-WROOM-1` footprint/keepout bbox is approximately `48 mm` wide, wider than the `38 mm` board.
- This requires LJ explicit acceptance or board/footprint repair before routing.

## Copper Decision

Because the RF keepout/footprint risk remains unresolved and zone creation is blocked, no F.Cu or B.Cu copper was added.

RF keepout result: `COPPER_NOT_CREATED_KEEP_OUT_RISK_UNRESOLVED`

Final PCB audit may begin: `NO`

