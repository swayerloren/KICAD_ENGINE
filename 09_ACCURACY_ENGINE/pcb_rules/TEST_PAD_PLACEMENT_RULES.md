# Test Pad Placement Rules

Status: `MANDATORY_FOR_PCB_PLACEMENT`

Test pads are service features. They must remain accessible after connectors, cables, enclosure parts, and fingers/tools are considered.

## Required Pattern

1. Place test pads in one or more clean rows.
2. Keep test pads out of component clusters.
3. Keep test pads away from USB-C shells, barrel-jack bodies, switches, LEDs, and mounting holes.
4. Labels must be readable and not overlap pads or nearby components.
5. Do not use test pads as filler in arbitrary empty space.
6. Do not place test pads in RF keepout areas.

## Spacing Rules

Unless a project-specific fixture requires otherwise:

- Keep at least `1.5 mm` practical clearance from test pad copper to neighboring component courtyards.
- Use consistent pitch in a row.
- Leave enough room for a probe tip and label.
- Avoid putting tall parts immediately beside test pads.
- Avoid placing test pads behind a connector mouth or cable exit.

## USB Data Pads

USB D+/D- test pads are high-risk because they can create stubs.

If included, the placement report must flag:

- `USB_TEST_PAD_STUB_RISK`
- pad location
- expected stub length before routing
- LJ decision to keep, move, DNP, or remove in a future schematic revision

## Placement Hard Blocks

Placement is not ready if:

- Test pads are mixed with `R6/R7/R8/R9`, ESD parts, LED resistors, switches, or connector support clusters.
- Test pads are crowded behind USB-C.
- Test pad labels overlap pads or silkscreen.
- Pads are inaccessible due to plug/cable/enclosure/mounting hardware.
- Any test pad overlaps a courtyard or violates clearance.

Routing is blocked until test pad accessibility is reviewed.
