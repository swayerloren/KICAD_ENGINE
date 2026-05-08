# Footprint Creation Standard

## Required Source Evidence

Before creating or approving a footprint, collect:

- Exact manufacturer part number or exact package code.
- Mechanical/package drawing.
- Recommended land pattern if available.
- Pad dimensions and tolerances.
- Drill sizes for through-hole pads.
- Body outline, height, keepouts, and courtyard guidance.
- Pin 1 orientation.

## Project-Local First

Generated or custom footprints should go into a project-local `.pretty` library unless the user explicitly requests another location.

Do not modify:

- Installed KiCad footprint libraries.
- User-global KiCad footprint libraries.
- User-global `fp-lib-table`.

## Creation Steps

1. Build pads from the package drawing or land-pattern source.
2. Set pad numbers exactly.
3. Define pin 1 orientation and marker.
4. Add fab outline from body dimensions.
5. Add courtyard with suitable clearance.
6. Add silkscreen that does not collide with pads.
7. Set footprint origin intentionally.
8. Add or link a 3D model only after checking orientation and scale.
9. Record source evidence and verification status.

## Approval Rule

Footprint status remains `UNVERIFIED_FOOTPRINT` until exact package or connector drawing evidence is checked. Scripts can flag issues but cannot approve a footprint.

