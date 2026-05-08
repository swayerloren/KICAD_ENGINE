# STM32 Dev Board Layout Pattern

## Warning

These are layout patterns, not universal rules. Some projects require different shapes or orientations. Use project requirements first.

## Purpose

Capture the default placement logic for compact STM32-style development boards that need clean connector access, programming access, and practical bring-up.

## Default Pattern

- Place USB-C or the primary power-data connector on the edge it physically serves.
- Keep SWD, UART, or programming headers accessible without removing major assemblies.
- Keep reset and boot-mode controls user-accessible.
- Keep LEDs visible during normal use.
- Keep analog-sensitive areas away from switching power clusters and noisy cable-entry regions.
- Keep test pads reachable after assembly, preferably in ordered rows or grouped service zones.

## Placement Rules

- Put cable-entry connectors on edges, not stranded inboard.
- Place programming and debug access where clips, probes, or cables can actually reach them.
- Keep regulators and inductors out of crowded connector mouths.
- If the board includes a radio module, apply RF keepout rules before finalizing shape or hole placement.
- Do not hide essential buttons under mezzanine cards, tall connectors, or overhanging cables.

## Shape Guidance

- Use the board shape that best serves connector spacing, button access, mounting-hole clearance, and routing feasibility.
- A rectangle is common, but it is not mandatory.
- If the mechanical requirement is asymmetric, the outline may be asymmetric.

## Human Review Gate

Human review is required for programming access, connector orientation, mounting-hole spacing, and any shape chosen mainly for enclosure or cable reasons.
