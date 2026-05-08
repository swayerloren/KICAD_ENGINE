# Connector Orientation Rules

## Purpose

Require explicit connector reasoning before PCB placement or routing starts.

## Core Rules

- Connector orientation must be decided during variant planning, not after routing starts.
- USB-C and barrel jacks are fixed mechanical items unless project requirements explicitly say otherwise.
- Edge-facing connectors must have their mating side facing off-board.
- The connector review must use footprint geometry, body shape, `PCB Edge` indicators where present, and 3D evidence where available.
- Coordinates alone are not proof of correct orientation.

## Required Checks

- Which board edge does the connector serve?
- Which side is the mating/opening side?
- Does the body overhang the edge intentionally?
- Does the footprint expect a board-edge alignment marker?
- Is cable insertion physically usable?
- Does the connector placement steal space from RF or switching-power areas?

## Variant Failure Conditions

- USB-C not aligned to the intended edge when edge-mounted behavior is required.
- Barrel jack opening/front not facing off-board when edge access is required.
- Connector orientation guessed from pads alone.
- Connector left floating inboard with no mechanical justification.

## Related Pattern

- `10_KNOWLEDGE_BASE/design_patterns/CONNECTOR_EDGE_PLACEMENT_PATTERN.md`
