# Barrel Jack Layout Common Mistakes

## Warning

These are layout patterns, not universal rules. Some projects require different shapes or orientations. Use project requirements first.

## High-Risk Mistakes

- Guessing the front or mating side from pad coordinates alone.
- Rotating the barrel jack so the opening does not face off-board.
- Leaving the jack inboard with no mechanical reason.
- Blocking insertion with buttons, LEDs, tall capacitors, or mounting hardware.
- Crowding the power-protection and regulator input cluster so the power path becomes nonsensical.
- Picking a board shape that makes the jack awkward to insert or mechanically weak.

## Agent Checks

- Verify the exact front-opening direction from drawing, body geometry, or 3D evidence.
- Verify the intended board edge.
- Verify cable-entry clearance and strain space.
- Verify that input protection and regulator clusters still fit sensibly behind the connector.

## Required Human Review

Human review is required for connector opening direction, edge placement, mechanical clearance, and power-entry path logic.
