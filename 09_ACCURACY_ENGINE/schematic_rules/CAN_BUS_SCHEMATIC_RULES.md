# CAN Bus Schematic Rules

## Scope

CAN and CAN FD transceivers, termination, protection, common-mode chokes, connectors, and MCU interface pins.

## Rules

- Verify exact transceiver part and package.
- Verify logic supply and bus supply domains.
- Check TXD/RXD pin mapping.
- Add termination only where the node is intended to terminate the bus.
- Check split termination requirements when used.
- Add ESD/TVS protection appropriate to the environment.
- Consider common-mode choke only with a source-backed need.
- Flag connector pinout and shield/chassis strategy for human review.

## Required Review Flags

- `CAN_TRANSCEIVER_PINOUT_VERIFIED`
- `CAN_TERMINATION_REVIEW_REQUIRED`
- `CAN_PROTECTION_REVIEW_REQUIRED`
- `CAN_CONNECTOR_ORIENTATION_HUMAN_REVIEW_REQUIRED`
- `CAN_LAYOUT_REVIEW_REQUIRED`

## Exit Criteria

CAN schematic blocks are not complete until transceiver source, termination strategy, connector pinout, and protection are reviewed.
