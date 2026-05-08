# PCB Mechanical Clearance Rules

Status: `MANDATORY_FOR_PCB_PLACEMENT_AND_AUDIT`

Mechanical clearance is part of placement quality. A board is not placement-ready just because parts are inside the outline.

## Required Clearance Checks

Before routing, check:

1. Component courtyard overlaps.
2. Connector shell and plug/cable envelopes.
3. Board-edge clearance for pads, tabs, holes, and bodies.
4. Mounting-hole copper and component clearance.
5. Button finger/tool access.
6. LED visibility.
7. Test pad probe access.
8. RF keepout clearance.
9. Silkscreen over pads, holes, connector bodies, and component courtyards.
10. Tall-component conflicts and enclosure risks.

## Mounting Holes On Narrow Boards

Four mounting holes are not automatically acceptable on compact dev boards.

For narrow boards:

- Do not use four holes unless component and RF keepout clearance is proven.
- Do not place holes in connector mechanical areas.
- Do not place holes in ESP32 RF keepouts.
- If four holes are impractical, switch to a documented two-hole strategy or require LJ decision.

Required classifications:

- `FOUR_HOLE_LAYOUT_CLEARANCE_PROVEN`
- `TWO_HOLE_COMPACT_STRATEGY_RECOMMENDED`
- `4_HOLE_LAYOUT_NOT_PRACTICAL_ON_COMPACT_BOARD`
- `MOUNTING_HOLE_STRATEGY_REQUIRES_LJ_DECISION`

## Pass/Fail Rules

Placement is not ready if DRC reports:

- courtyard overlap,
- component clearance violation,
- copper-to-edge violation needing connector review,
- silkscreen over pads/holes,
- connector mechanical conflict,
- mounting-hole clearance conflict,
- RF keepout conflict.

Unconnected items are expected before routing, but they do not excuse mechanical placement violations.

Routing is blocked until all real placement/mechanical issues are repaired or explicitly accepted by LJ.
