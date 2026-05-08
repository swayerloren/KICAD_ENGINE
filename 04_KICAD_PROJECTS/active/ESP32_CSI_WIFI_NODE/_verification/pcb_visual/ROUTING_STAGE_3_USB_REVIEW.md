# Routing Stage 3 USB Review

Status: `NOT_RUN_BLOCKED`

Generated: `2026-05-07`

Project: `ESP32_CSI_WIFI_NODE`

## Visual Review Status

No Stage 3 USB images were exported because no PCB edit or USB routing was performed.

Reason:

`MAINTENANCE_DUE_HANDLED_PHASE_GATE_BLOCKED_STAGE_2_NOT_ROUTED`

## Current USB Evidence

- J2 is documented as bottom-edge/off-board and `PROVEN` in `J1_J2_CONNECTOR_ORIENTATION_PROOF.md`.
- USB plan identifies J2, U3, R6, R7, R8, R9, and R5 as the USB cluster.
- TP8/TP9 are USB data test pads and are marked `USB_TEST_PAD_STUB_RISK`.

## Required Future Visual Evidence

When routing is allowed, USB review should include close-up evidence showing:

- J2 to U3 D+/D- entry path
- U3 to R8/R9 series resistor path
- R8/R9 to U2 USB pins
- CC1/CC2 pull-down routing to R6/R7/GND
- shield policy routing if used
- TP8/TP9 stub handling
- clearance from BUCK_SW and U2 RF keepout

Stage 4 low-speed routing may begin: `NO`

