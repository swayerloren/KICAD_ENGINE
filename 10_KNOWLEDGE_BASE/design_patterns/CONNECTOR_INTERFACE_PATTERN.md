# Connector Interface Pattern

## Purpose

Prevent connector pinout, orientation, and footprint mistakes.

## Required Inputs

- Exact manufacturer part number where possible.
- Connector drawing and footprint land pattern.
- Mating connector or cable assembly.
- Pinout source from the system or harness.
- Mechanical orientation requirement.

## Pattern

- Create a connector record before schematic placement.
- Add pin names based on system function, not only pin numbers.
- Keep pin 1 orientation visible in schematic notes and PCB silkscreen.
- Add protection and filtering near exposed connectors.
- Require human review for connector orientation.

## KiCad Agent Rules

- Generic connectors are `UNVERIFIED_PLACEHOLDER`.
- Do not approve a footprint from pitch alone.
- Do not assume a top-entry, side-entry, SMT, through-hole, keyed, or mirrored variant.
- Verify shell, mounting pads, and courtyard.

## Review Gate

No connector is approved until pin numbering, mating part, mechanical orientation, footprint, and 3D/mechanical fit are reviewed.

