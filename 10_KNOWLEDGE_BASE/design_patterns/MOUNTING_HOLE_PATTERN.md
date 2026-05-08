# Mounting Hole Pattern

## Purpose

Treat mounting holes as mechanical and electrical design features, not decoration.

## Required Inputs

- Screw size or standoff requirement.
- Hole plating intent.
- Keepout around screw head, washer, and standoff.
- Chassis/grounding strategy.
- Board outline and enclosure constraints.

## Pattern

- Define mounting holes during board outline planning.
- Use footprints that match plated or non-plated intent.
- Add copper keepout or chassis connection intentionally.
- Verify courtyard and 3D clearance.

## Common Mistakes

- Using plated holes when non-plated mechanical holes were intended.
- Connecting mounting holes to ground without reviewing chassis/noise/ESD behavior.
- Placing components too close to screw heads.
- Forgetting enclosure tolerance.

## Review Gate

Human review is required for hole size, plating, chassis/ground connection, and mechanical clearance.

