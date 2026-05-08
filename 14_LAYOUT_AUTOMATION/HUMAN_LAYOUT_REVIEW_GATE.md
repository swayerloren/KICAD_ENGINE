# Human Layout Review Gate

## Purpose

Define what must be reviewed by a human before any AI-assisted placement or routing output is treated as usable for fabrication planning.

## Required Human Review

- Board outline and mechanical constraints.
- Mounting holes.
- Connector orientation and mating direction.
- Pin 1 and polarity markings.
- Footprint verification for exact packages.
- RF placement, keepouts, and feedlines.
- USB differential pair routing and ESD placement.
- CAN/LIN/RS485 termination and connector pinout.
- Switching regulator placement and loops.
- High-current trace widths and thermal relief.
- Crystal/clock placement.
- Ground return paths.
- Test point accessibility.
- DRC results and exclusions.
- PNP rotations.
- Gerber/drill review before fabrication.

## Gate Status Labels

- `LAYOUT_REVIEW_NOT_STARTED`
- `LAYOUT_REVIEW_IN_PROGRESS`
- `HUMAN_LAYOUT_REVIEW_REQUIRED`
- `LAYOUT_REVIEW_BLOCKED`
- `LAYOUT_REVIEW_ACCEPTED_FOR_NEXT_STEP`

## Not Final Rule

Even after layout review, manufacturing outputs remain `NOT_FINAL` until the full fabrication verification gate passes.

## Required Report

Every AI-assisted placement/routing task should produce:

- What changed.
- Why it changed.
- Source evidence used.
- DRC before/after.
- Remaining violations.
- Human review items.
- Explicit final status.

