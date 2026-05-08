# PCB Pill-Style Mechanical Conflicts

Project: `ESP32_CSI_WIFI_NODE`

Date: 2026-05-07

Scope: Mechanical placement conflicts after 38 mm x 80 mm pill-style reset.

## Conflicts

| Item | Conflict | Severity | Required decision |
|---|---|---:|---|
| `U2` footprint/keepout | Current `RF_Module:ESP32-S3-WROOM-1` footprint bbox is approximately `48 mm` wide, wider than the `38 mm` board. Module body is centered, but footprint/keepout/courtyard extends beyond side edges. | `HIGH` | Confirm correct ESP32-S3-WROOM-1U footprint/keepout or choose wider board. |
| Mounting holes | Four corner M2.5 holes do not fit cleanly with U2 keepout and compact board density. `MH3/MH4` were moved below the keepout for review. | `HIGH` | Accept moved mid-board holes, switch to 2-hole strategy, or widen board. |
| `J1` barrel jack | Barrel jack is large for a 38 mm pill board and consumes lower-left side area. | `HIGH` | Accept side barrel jack, switch to wider Option C, or approve replacement with smaller power input. |
| `J2` USB-C | Connector intentionally overhangs bottom edge; DRC reports copper-edge clearance issues. | `MEDIUM` | Confirm footprint edge alignment and accepted overhang. |
| Test pads | Bottom test row fits visually but is close to USB support/connector area. | `MEDIUM` | Confirm test pad row location and USB D+/D- stub policy before routing. |
| Silkscreen | Dense compact placement creates silkscreen overlap/clipping warnings. | `MEDIUM` | Cleanup references/labels after LJ accepts placement concept. |
| U2 drill rule | U2 pad 41 holes are 0.20 mm while current board setup minimum drill is 0.30 mm. | `HIGH` | Confirm fab capability or repair footprint/rule before final DRC. |

## J1 Status

`J1` is placed on the board, not parked outside.

Status: `J1_SIDE_PLACEMENT_REQUIRES_MECHANICAL_REVIEW`

## Mounting-Hole Status

Current status: `FOUR_HOLE_FOOTPRINTS_PRESENT_BUT_NOT_CORNER_CLEAN`

Recommended next decision:

- Use Option A only if LJ accepts moved `MH3/MH4`, or
- switch to 2-hole mounting, or
- switch to wider Option C if four real corner holes and barrel jack are mandatory.

## Routing Gate

Routing must remain blocked until LJ reviews and accepts the mechanical conflicts.

## 2026-05-07 Placement Repair Attempt

Repair status: `NOT_APPLIED_PHASE_GATE_BLOCKED`

The requested placement/mechanical cleanup was blocked before PCB edits because the read-only Phase 5 gate reported:

`PHASE_GATE_RESULT: BLOCKED`

Primary blocker:

- `reports/SCHEMATIC_TO_PCB_GATE_STATUS.md` still reports `Gate result: FAIL` and `PCB update allowed: NO`.

Conflicting later evidence:

- `reports/PCB_SYNC_STATUS.md` reports `Status: PCB_SYNCED`.
- The target `.kicad_pcb` exists.

Current mechanical conflicts remain unchanged until the gate inconsistency is resolved and a real placement repair pass is allowed.
