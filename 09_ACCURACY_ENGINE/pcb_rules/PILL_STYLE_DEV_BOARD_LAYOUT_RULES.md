# Pill-Style Dev Board Layout Rules

Status: `MANDATORY_FOR_COMPACT_DEV_BOARD_PLACEMENT`

These rules apply to ESP32, STM32, RP2040, AVR, USB, and similar narrow development boards where the intended form factor is a compact pill/dev-board layout.

## Failure Record

For `ESP32_CSI_WIFI_NODE`, Codex first created an oversized board with a large dead area. After correction, Codex created a better pill-style placement, but still left connector orientation, test-pad crowding, mounting-hole clearance, silkscreen, and mechanical fit problems.

This rule exists to prevent agents from treating a smaller board as acceptable when service access and mechanical constraints are still wrong.

## Required Layout Pattern

1. Use a narrow, purposeful rectangle unless LJ provides another mechanical envelope.
2. Avoid giant dead zones. Unused area must have a documented mechanical, thermal, RF, connector, or assembly reason.
3. For ESP32 module boards, place the module at the top edge with antenna/U.FL/RF keepout facing the top edge unless a documented reason says otherwise.
4. USB-C on dev-board layouts should normally be on the bottom edge with the mouth facing downward/off-board, the footprint `PCB Edge` line aligned to `Edge.Cuts`, pads on-board, and 2D/3D orientation proof where available.
5. Power input must not force an oversized board. Barrel jacks require explicit mechanical review on narrow boards, and `BARREL_JACK_ORIENTATION_RULES.md` must be applied.
6. For bottom-edge barrel jacks, the female circular opening/front must face downward/off-board and the 3-pin solder-leg rear/back side must face upward/inward.
7. Reset/boot buttons must be accessible from an edge by a finger or tool.
8. LEDs must be visible at an edge or clearly visible board face.
9. Test pads must be in clean service rows and not mixed into component clusters.
10. Mounting holes must be placed only where clearance is proven.

## Placement Hard Blocks

Placement is not ready when any of these are true:

- Ports do not face the intended board edge.
- USB-C footprint edge line is not aligned to the board edge or explicitly reviewed.
- USB-C mouth/opening is not proven to face off-board.
- USB-C is approved from coordinates alone without 2D footprint proof and 3D screenshot proof where available.
- Barrel jack female opening/front does not face off-board.
- Barrel jack 3-pin solder-leg rear/back side faces off-board instead of inward.
- Barrel jack orientation is approved from pad coordinates alone.
- A connector shell, plug envelope, or cable path blocks test pads, buttons, LEDs, or mounting hardware.
- Test pads are mixed among resistors, ESD devices, LEDs, buttons, or connector support parts.
- Any component, courtyard, pad, text, mounting hole, board edge, RF keepout, or mechanical area overlaps.
- Four mounting holes are used on a narrow board without proven clearance.
- A barrel jack is retained on a pill board without explicit mechanical review.
- A barrel jack is too bulky for the pill board but is not marked `BARREL_JACK_NOT_PILL_BOARD_FRIENDLY`.
- ESP32 antenna/U.FL/RF keepout is trapped in the board middle or blocked by copper/components/holes.
- Board shape has a large dead area without a documented reason.

## Required Evidence Before Routing

Before routing starts, the placement report or audit must include:

- Board size and rationale.
- Connector edge/orientation table.
- ESP32 RF keepout status.
- Test pad row location and clearance status.
- Button/LED accessibility status.
- Mounting-hole clearance status.
- DRC category summary.
- Visual top/bottom evidence.
- LJ visual approval or explicit risk acceptance.

Routing is blocked until LJ visually approves placement after these checks.
