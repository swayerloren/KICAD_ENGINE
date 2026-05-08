# ESP32_CSI_WIFI_NODE Layout Sandbox Variant Comparison

Date: `2026-05-07`

Status: `NEEDS_HUMAN_REVIEW`

Scope note: comparison only. This file does not approve real `.kicad_pcb` edits.

## Gate Context

- `SCHEMATIC_TO_PCB_GATE_STATUS.md`: `FAIL`
- `FOOTPRINT_PACKAGE_GATE_REPORT.md`: `FAIL`
- `PCB_SYNC_STATUS.md`: `Placement planning may begin: YES`

Interpretation:

- Sandbox planning is allowed and useful.
- Real PCB placement/editing is still blocked by upstream review and approval items.

## Score Summary

| Variant | Concept | Subtotal | Risk | Penalty | Total | Status | Main reason |
| --- | --- | ---: | --- | ---: | ---: | --- | --- |
| `VARIANT_A` | Compact dev-board style | 71 | `MEDIUM` | 5 | 66 | `NEEDS_HUMAN_REVIEW` | Most compact, but most crowded mechanically and electrically |
| `VARIANT_B` | Connector/mechanical optimized | 81 | `LOW` | 2 | 79 | `NEEDS_HUMAN_REVIEW` | Best connector and mounting comfort, but longer electrical paths |
| `VARIANT_C` | Routing/power/RF optimized | 88 | `LOW` | 2 | 86 | `NEEDS_HUMAN_REVIEW` | Best overall electrical structure with the cleanest RF and USB/power path balance |

## Ranking

1. `VARIANT_C` - best total score and cleanest routing structure
2. `VARIANT_B` - strongest mechanical clarity, but electrically less efficient
3. `VARIANT_A` - smallest board, but crowding risk is too high

## Script Result

- Variant count: `3`
- Selected variant ID: `VARIANT_C`
- Selected variant status: `NEEDS_HUMAN_REVIEW`
- Ready for real PCB edit: `NO`

Selection justification from the scorer:

> `VARIANT_C` is the highest-scoring non-failed variant. It carries a `LOW` human-review risk with a total score of `86`.

## Why Variant C Won

- It gives the cleanest separation between:
  - left-side power entry and buck cluster
  - right-side USB chain
  - upper-right RF connector and pigtail service zone
- It keeps the shortest credible:
  - `J1 -> F1 -> Q1 -> D1/C1 -> U1/L1/C2-C5 -> 3V3`
  - `J2 -> U3 -> R6/R7 -> U2`
- It protects the `WROOM-1U` RF connector/pigtail region better than A or B.
- It avoids the worst compact-board routing compression of A.
- It avoids the oversized mechanical-first detours of B.

## Why Variant C Is Still Not Placement-Ready

- Board dimensions are still assumptions, not locked mechanical facts.
- Exact USB-C and barrel-jack footprint/package lock is still unresolved by project gate evidence.
- `U2` `ESP32-S3-WROOM-1U-N16R8` RF connector/pigtail clearance still needs LJ approval.
- The asymmetrical outline must be accepted as a justified shape, not a casual draft.

## Required LJ Review Before PCB Placement

1. Accept or reject the Variant C outline concept.
2. Approve the intended `J1` and `J2` edge locations and facing directions.
3. Approve the `U2` RF connector and pigtail service-zone assumption.
4. Approve whether four mounting holes remain required.
5. Approve the USB test-pad policy for `TP8` and `TP9`.
6. Approve the enclosure-side mechanical assumptions or replace them with exact dimensions.
