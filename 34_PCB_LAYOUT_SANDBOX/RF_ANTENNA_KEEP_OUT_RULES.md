# RF Antenna Keep-Out Rules

## Purpose

Make antenna clearance a first-order placement constraint during sandbox planning.

## Core Rules

- Define the ESP32 or other RF-module antenna keepout before placing nearby components.
- Keep the antenna zone at the board edge or in the module's required open area.
- Do not place connectors, regulators, large copper features, shields, or test points in the antenna keepout.
- Do not let the planned board outline clip or crowd the antenna clearance area.
- If a variant cannot keep the antenna clear, it fails regardless of routing convenience elsewhere.

## Required Variant Evidence

- keepout shape
- keepout dimensions
- board-edge relationship
- nearby-component clearance notes
- blocked/unblocked status

## Routing Projection Rule

Any projected route that would later require copper, stitching, or component intrusion into the RF keepout is a sandbox failure signal.

## Related Pattern

- `10_KNOWLEDGE_BASE/design_patterns/RF_MODULE_ANTENNA_KEEP_OUT_PATTERN.md`
