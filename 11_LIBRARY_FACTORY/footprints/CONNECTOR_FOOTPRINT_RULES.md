# Connector Footprint Rules

Connector footprints are high risk.

## Required Evidence

- Exact connector manufacturer part number.
- Mechanical drawing.
- Recommended PCB layout or land pattern.
- Mating connector or cable assembly.
- Pin 1 location.
- Pin numbering direction.
- Mounting, shell, shield, latch, and keying features.
- 3D/mechanical orientation review when possible.

## Rules

- Generic connectors remain `UNVERIFIED_PLACEHOLDER`.
- Do not approve connector footprints from pitch alone.
- Do not assume variants are compatible.
- Do not ignore mounting pads or shell pads.
- Do not assume USB-C, JST, U.FL, SMA, barrel jack, or automotive connector footprints are interchangeable.

## Human Review Required

Every external connector footprint requires human review for:

- Pin numbering.
- Mating direction.
- Board side.
- Cable exit.
- Mechanical fit.
- Orientation markers.

## Approval Rule

A connector footprint is not approved until exact drawing evidence and human orientation review are recorded.

