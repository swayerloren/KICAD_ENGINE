# Connector Orientation Rules

## Prime Rule

Every connector orientation requires human review unless exact drawing, footprint, mating connector, and mechanical evidence are verified.

## Required Checks

- Pin 1 location.
- Top/bottom view drawing interpretation.
- Mating connector orientation.
- Cable exit direction.
- Board edge or panel location.
- 3D model orientation.
- Silkscreen and fab-layer pin markings.

## High-Risk Connectors

- USB-C.
- Micro USB.
- FFC/FPC.
- U.FL/IPEX.
- SMA edge launch.
- Automotive harness connectors.
- Board-to-board connectors.
- Shrouded headers.

## Required Status

- `CONNECTOR_ORIENTATION_HUMAN_REVIEW_REQUIRED`
- `CONNECTOR_ORIENTATION_VERIFIED`
- `MATING_CONNECTOR_UNKNOWN`
- `FOOTPRINT_PIN_NUMBERING_UNVERIFIED`
