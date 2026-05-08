# Connector Pin Numbering Rules

## Prime Rule

Every connector pin numbering and orientation decision requires human review unless exact manufacturer drawing evidence and mating orientation are verified.

## Required Evidence

- Exact manufacturer part number.
- Datasheet or mechanical drawing.
- Pin numbering view orientation.
- Mating connector or cable orientation.
- Footprint pad numbering.
- 3D model or mechanical model when available.

## High-Risk Patterns

- Bottom-view drawings confused with top-view footprints.
- Mirrored cable pinouts.
- USB-C dual-row numbering.
- Board-edge RF connectors.
- Automotive harness connectors.
- Shrouded or keyed headers.
- FFC/FPC top-contact versus bottom-contact connectors.

## Required Status

Use:

- `CONNECTOR_PIN_NUMBERING_VERIFIED`
- `CONNECTOR_ORIENTATION_HUMAN_REVIEW_REQUIRED`
- `CONNECTOR_MATING_PART_UNKNOWN`
- `CONNECTOR_FOOTPRINT_UNVERIFIED`

## Rule

Do not approve a connector schematic or PCB footprint from a generic name alone.
