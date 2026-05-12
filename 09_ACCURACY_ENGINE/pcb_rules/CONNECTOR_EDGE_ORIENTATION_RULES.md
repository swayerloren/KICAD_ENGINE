# Connector Edge Orientation Rules

Status: `MANDATORY_FOR_PCB_PLACEMENT`

These rules define connector edge placement and orientation checks. They supplement `CONNECTOR_ORIENTATION_RULES.md`.

Also read `BARREL_JACK_ORIENTATION_RULES.md` before approving any DC barrel jack placement.
Also read `08_COMPONENT_DATABASE/mechanical_orientation/connector_orientation_truth.json` before approving barrel-jack, USB-C, or other edge-facing connector truth.

## Edge Connector Requirements

1. A connector must have a declared intended board edge before placement.
2. The connector port/mouth/opening must face off-board through that intended edge.
3. Footprint edge-line markings must align to the board edge when the footprint provides them.
4. Intentional shell or connector-body overhang is allowed only when pads, mechanical tabs, courtyard, and board-edge clearance are legal or explicitly reviewed.
5. Connector plug/cable envelopes must not block test pads, buttons, LEDs, mounting holes, or required inspection areas.

## USB-C Dev-Board Default

For pill/dev-board layouts:

- `J2` USB-C should normally be centered on the bottom edge.
- The USB-C mouth must face downward/off-board.
- The USB-C receptacle mouth/opening must face off-board for any edge-mounted placement.
- For bottom-edge USB-C placement, the receptacle mouth faces downward/off-board.
- The footprint `PCB Edge` indicator must align to board `Edge.Cuts` when the footprint provides one.
- Pads must remain on the PCB; connector shell/body overhang must be mechanically expected by the footprint.
- Do not approve USB-C orientation from coordinate position alone.
- If the exact USB-C 3D model is missing or unresolved, classify `NEEDS_HUMAN_REVIEW`.
- Require 2D footprint proof and 3D screenshot proof where available.
- USB ESD, CC resistors, and series resistors must be behind the connector, not mixed into the test pad row.
- Do not place test pads directly behind the USB-C shell or cable entry area.
- Board-edge clearance warnings on USB-C pads or shell tabs require footprint edge-line review before routing.

## Barrel Jack Rule

Barrel jacks are usually not pill-board-friendly.

If a barrel jack is retained:

- Prefer a lower-left or lower-side edge.
- The female circular barrel opening is the front/mating side and must face outward/off-board.
- The 3-pin solder-leg side is the rear/back side and must face inward toward the PCB body.
- For bottom-edge placement, the female opening faces downward/off-board and the 3-pin solder side faces upward/inward.
- If the 3-pin solder side is closest to the bottom edge, the barrel jack is flipped wrong.
- Do not approve barrel jack orientation from pad coordinates alone.
- Require evidence from exact 3D model when available, footprint `F.Fab`/`F.SilkS`/`F.CrtYd` geometry, and a manufacturer drawing or product image.
- If no 3D model and no clear footprint geometry exist, classify `BLOCKED_BY_BARREL_JACK_ORIENTATION_EVIDENCE`.
- If the footprint family is known but the exact 3D model is missing or unresolved, classify `NEEDS_HUMAN_REVIEW`.
- The footprint and plug envelope must not force a large dead board area.
- Do not side-mount `J1` unless LJ explicitly approves.
- The placement report must classify it as one of:
  - `BARREL_JACK_ACCEPTED_WITH_CLEARANCE`
  - `BARREL_JACK_REQUIRES_LJ_MECHANICAL_REVIEW`
  - `J1_BARREL_JACK_NOT_PILL_BOARD_FRIENDLY`
  - `BARREL_JACK_NOT_PILL_BOARD_FRIENDLY`
  - `BLOCKED_BY_BARREL_JACK_ORIENTATION_EVIDENCE`

## Pass/Fail Criteria

Connector placement fails if:

- Any port faces into the board.
- Any connector intended for edge use is stranded away from its edge.
- The edge line is visibly misaligned and not documented.
- Connector overhang blocks service access.
- The connector creates courtyard, board-edge, pad, shell-tab, or mounting-hole conflicts.

Routing is blocked until connector orientation is reviewed and accepted.
