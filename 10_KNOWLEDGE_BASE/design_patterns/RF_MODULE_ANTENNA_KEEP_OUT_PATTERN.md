# RF Module Antenna Keep-Out Pattern

## Warning

These are layout patterns, not universal rules. Some projects require different shapes or orientations. Use project requirements first.

## Purpose

Make RF antenna clearance a first-order placement and outline constraint for boards that use modules such as ESP32 WROOM-style parts.

## Pattern

- Put the antenna at the board edge or in the module's documented clear zone.
- Keep the keepout free of copper, traces, vias, mounting holes, connectors, and tall components unless the exact module documentation allows exceptions.
- Keep noisy power clusters away from the antenna edge.
- Keep the board outline from clipping or crowding the antenna field.

## Common Placement Logic

- Define the keepout before finalizing connector positions.
- Define the keepout before choosing mounting-hole locations near the radio side.
- Reject any variant whose projected routing later invades the keepout.

## Review Gate

Human review is required for keepout dimensions, board-edge relationship, and nearby mechanical features.
