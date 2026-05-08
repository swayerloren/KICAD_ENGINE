# ESP32_CSI_WIFI_NODE Selected Layout Plan

Date: `2026-05-07`

Selection type: `PROVISIONAL_SANDBOX_FRONT_RUNNER_ONLY`

Selected variant: `VARIANT_C_ROUTING_POWER_RF_OPTIMIZED`

Selected variant ID: `VARIANT_C`

Selected variant status: `NEEDS_HUMAN_REVIEW`

Real KiCad PCB work approved by this file: `NO`

## Why This Variant Was Selected

`VARIANT_C` is the highest-scoring non-failed variant from the sandbox comparison.

It was selected as the current front-runner because it gives the best overall balance of:

- clean power-entry clustering
- short and credible USB path placement
- protected RF connector/pigtail service space for the `ESP32-S3-WROOM-1U-N16R8`
- fewer routing bottlenecks than the compact concept
- less electrical compromise than the mechanical-first concept

## Planned Placement Direction

- `J1` bottom-left edge, opening down/off-board
- `F1`, `Q1`, `D1`, `C1`, `U1`, `L1`, `C2-C5` clustered from lower-left to center-left
- `J2` bottom-center/right edge, mouth down/off-board
- `U3`, `R6`, `R7` between `J2` and `U2` in the right-side USB corridor
- `U2` upper-right with a reserved RF connector and pigtail service zone
- `SW1` and `SW2` on the right edge above the USB connector height
- `D2`/`R8` and `D3`/`R9` visible above the lower connector envelope
- `TP1-TP7` grouped on the back side; `TP8`/`TP9` optional only
- `MH1-MH4` retained, but the top-right hole moved clear of the RF service zone

## Remaining Risks

- Board width, height, and enclosure constraints are still assumptions.
- Exact USB-C and barrel-jack footprint lock remains blocked by project gate evidence.
- RF pigtail bend radius and enclosure exit path are still LJ review items.
- The asymmetrical outline needs explicit acceptance before placement.
- USB optional test pads remain a signal-integrity risk unless omitted or proven safe.

## LJ Must Approve Before PCB Placement

1. Variant C as the preferred layout direction.
2. The board-shape assumption and dimensional envelope.
3. `J1` and `J2` intended edge placement and facing directions.
4. `U2` RF connector/pigtail clearance and enclosure path.
5. Whether all four mounting holes remain required.
6. Whether `TP8` and `TP9` are omitted, DNI, or retained with a controlled stub policy.
7. Any connector, package, or footprint decisions still blocked in:
   - `reports/SCHEMATIC_TO_PCB_GATE_STATUS.md`
   - `reports/FOOTPRINT_PACKAGE_GATE_REPORT.md`

## Blocking Status

Real KiCad PCB work is still blocked.

Reasons:

- `SCHEMATIC_TO_PCB_GATE_STATUS.md` is still `FAIL`.
- `FOOTPRINT_PACKAGE_GATE_REPORT.md` is still `FAIL`.
- Sandbox selection status is `NEEDS_HUMAN_REVIEW`, not `PASS`.
- LJ review is still required before any placement action is treated as approved.
