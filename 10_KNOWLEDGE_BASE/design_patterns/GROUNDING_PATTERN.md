# Grounding Pattern

## Purpose

Make ground strategy deliberate, especially around power, analog, RF, USB, CAN, and chassis interfaces.

## Required Inputs

- Signal domains.
- High-current return paths.
- Switching regulator location.
- Connector shield/chassis behavior.
- Analog and RF requirements.

## Pattern

- Prefer a continuous ground reference for most digital boards.
- Keep high-current switching loops compact.
- Route sensitive analog/RF returns deliberately.
- Add stitching vias near high-frequency return paths and connector shields where appropriate.
- Document any split-ground decision before using it.

## Common Mistakes

- Splitting ground without controlling return paths.
- Routing high-speed traces over plane gaps.
- Letting switching current return through sensor or RF grounds.
- Treating connector shield as ordinary digital ground without review.

## Review Gate

Ground strategy must be reviewed before PCB routing, and any split or chassis connection must have a written reason.

