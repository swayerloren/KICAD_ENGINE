# LJ J1/J2 Connector Review Checklist

Status: `ACTIVE_EVIDENCE`

Generated: `2026-05-07T13:50:00-04:00`

Project: `ESP32_CSI_WIFI_NODE`

## Review Summary

Final audit classification: `J2_READY_J1_BLOCKED_REPLACEMENT_REQUIRED`

Routing remains blocked.

## Checklist

| Item | Audit Status | LJ Review |
|---|---|---|
| J2 is on bottom edge | `PROVEN` | Confirm visually. |
| J2 USB-C opening faces down/off-board | `PROVEN` | Confirm using 3D front/close-up images. |
| J2 PCB-edge line aligns to bottom Edge.Cuts | `PROVEN` | Confirm footprint `PCB Edge` line at bottom edge in KiCad if desired. |
| J2 pads are on-board | `PROVEN` | No action unless footprint choice is rejected. |
| J2 body overhang looks correct | `PROVEN_FOR_REVIEW` | Confirm physical connector exposure is acceptable. |
| J1 is not side-mounted | `PROVEN` | J1 is bottom-left, rotation `180 deg`. |
| J1 opening faces down/off-board | `NOT_PROVEN` | Do not approve without a valid 3D model or connector replacement. |
| J1 pads are on-board | `PROVEN_2D_ONLY` | 2D geometry only. |
| J1 collides with J2/holes/switches | `NO_FINAL_DRC_COLLISION_LISTED` | Still visually inspect the bottom-left mechanical area. |
| J1 missing 3D proof | `BLOCKER` | Replace J1 with smaller verified power connector or provide a valid 3D model. |
| DRC connector/mechanical issues listed | `PROVEN` | Remaining DRC: U2 drill errors plus J1 footprint mismatch warning. |
| Routing remains blocked | `YES` | Do not route. |

## LJ Decision Needed

Choose one before future placement acceptance:

- Replace J1 with a smaller verified bottom-edge power connector.
- Provide/approve a valid J1 3D model and re-run the orientation proof.
- Explicitly accept J1 using 2D footprint geometry only, with recorded mechanical risk.

## Current Recommended Classification

`J2_READY_J1_BLOCKED_REPLACEMENT_REQUIRED`
