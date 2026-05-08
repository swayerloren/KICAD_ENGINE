# USB-C Connector Layout Common Mistakes

## Warning

These are layout patterns, not universal rules. Some projects require different shapes or orientations. Use project requirements first.

## High-Risk Mistakes

- Placing the connector inboard when the project clearly expects edge insertion.
- Facing the receptacle the wrong way.
- Ignoring `PCB Edge` alignment or intended body overhang.
- Treating shell tabs as decorative instead of mechanical features that need proof and clearance.
- Blocking LEDs, buttons, or test access with the inserted cable.
- Forcing data or ESD parts into awkward positions because edge placement was not reasoned first.

## Agent Checks

- Verify the exact connector drawing and footprint orientation.
- Verify edge alignment and overhang expectations.
- Verify shell and mechanical tab clearance.
- Verify cable-entry usability after assembly.
- Verify that nearby LEDs, buttons, and test pads stay usable.

## Required Human Review

Human review is required for connector facing direction, edge alignment, shell-tab usage, and cable usability.
