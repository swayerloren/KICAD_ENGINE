# Connector Edge Placement Pattern

## Warning

These are layout patterns, not universal rules. Some projects require different shapes or orientations. Use project requirements first.

## Purpose

Define the default mechanical logic for USB-C, barrel jacks, and other user-facing cable-entry connectors.

## Pattern

- Put the mating side on the board edge it is meant to serve.
- Verify insertion direction from footprint geometry, body shape, `PCB Edge` markings, 3D model evidence, and manufacturer drawings where available.
- Check that shell tabs, mounting tabs, and body overhang match the intended board-edge relationship.
- Keep cable insertion clear of nearby tall parts, buttons, LEDs, and mounting hardware.

## Rules

- Do not approve connector orientation from pad coordinates alone.
- Do not rotate a connector inboard just to make routing easier.
- Do not place a connector where cable insertion blocks buttons, LEDs, or test access unless the product requirement explicitly accepts it.
- Keep edge connectors away from RF keepouts and switching-power hot spots when alternatives exist.

## Review Gate

Human review is required for connector mouth direction, board-edge alignment, mechanical tab usage, and cable usability.
