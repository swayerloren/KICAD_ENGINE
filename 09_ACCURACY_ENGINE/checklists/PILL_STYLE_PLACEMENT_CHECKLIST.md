# Pill-Style Placement Checklist

Status: `MANDATORY_FOR_COMPACT_DEV_BOARD_PLACEMENT_REVIEW`

Use this checklist for ESP32/STM32/RP2040/AVR-style compact development boards before routing.

## Board Shape

- `[ ]` Board is a compact pill/dev-board shape, not an oversized rectangle.
- `[ ]` Board has no giant dead areas without documented mechanical, thermal, RF, or connector reason.
- `[ ]` Board size is stated in the placement report.

## ESP32 / RF

- `[ ]` ESP32 module is at the top edge unless a documented exception exists.
- `[ ]` Antenna/U.FL/RF keepout faces the top edge.
- `[ ]` RF keepout is clear of components, traces, copper, vias, holes, and silkscreen clutter.
- `[ ]` ESP32 footprint/keepout width fits the board or is explicitly classified for LJ review.

## Connectors

- `[ ]` USB-C is on the bottom edge for dev-board layouts unless a documented exception exists.
- `[ ]` USB-C mouth faces downward/off-board.
- `[ ]` USB-C footprint edge line aligns with the board edge or is explicitly reviewed.
- `[ ]` USB-C pads remain on-board and shell/body overhang is mechanically expected by the footprint.
- `[ ]` USB-C orientation is proven by 2D footprint evidence and 3D screenshot evidence where available, not coordinates alone.
- `[ ]` Barrel jack female circular opening/front faces off-board.
- `[ ]` Bottom-edge barrel jack female opening faces downward/off-board.
- `[ ]` Barrel jack 3-pin solder-leg rear/back side faces inward toward the PCB body.
- `[ ]` Barrel jack orientation is backed by `F.Fab`/`F.SilkS`/`F.CrtYd` geometry plus manufacturer/product-image or exact 3D evidence.
- `[ ]` Barrel jack is not approved from pad coordinates alone.
- `[ ]` Barrel jack is not side-mounted unless LJ explicitly approved side-entry placement.
- `[ ]` Barrel jack is accepted only after mechanical review or flagged as not pill-board-friendly.
- `[ ]` No connector plug/cable path blocks test pads, buttons, LEDs, or mounting holes.

## Test Pads

- `[ ]` Test pads are in a clean row or rows.
- `[ ]` Test pads are not mixed into USB, LED, button, or power component clusters.
- `[ ]` Test pads are not crowded behind USB-C.
- `[ ]` Labels are readable and not over pads.
- `[ ]` USB D+/D- test pads are explicitly flagged for stub-risk review if present.

## Controls And Indicators

- `[ ]` Reset and boot buttons are accessible from an edge.
- `[ ]` LEDs are visible at an edge or visible face.
- `[ ]` LED resistors are near LEDs but not crowding test pads.

## Power And USB Clusters

- `[ ]` Power path is compact and ordered from input to regulator to load.
- `[ ]` Buck regulator switch loop components are close.
- `[ ]` USB ESD/CC/series parts are compact behind USB-C.
- `[ ]` USB support parts are not mixed into the test pad service row.

## Mechanical Clearance

- `[ ]` Mounting holes have component/copper/courtyard clearance.
- `[ ]` Top holes are not in ESP32 RF keepout.
- `[ ]` Four-hole strategy is proven or two-hole strategy is documented.
- `[ ]` No component/courtyard/text/pad overlap exists.
- `[ ]` No silkscreen is over pads, holes, or connector bodies.

## Routing Gate

- `[ ]` DRC categories are classified.
- `[ ]` Real placement issues are repaired or explicitly accepted.
- `[ ]` LJ visually approves placement.
- `[ ]` Routing remains blocked until LJ approval is recorded.

Allowed final classifications:

- `PLACEMENT_READY_FOR_LJ_REVIEW`
- `PLACEMENT_NEEDS_MORE_REPAIR`
- `BLOCKED_BY_MECHANICAL_OR_FOOTPRINT_RISK`
