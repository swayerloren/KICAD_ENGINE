# CAN Layout Rules

## Scope

CAN/CAN FD bus routing, transceiver placement, termination, ESD/TVS, common-mode choke, and connector routing.

## Rules

- Place transceiver near the connector when appropriate.
- Keep CANH/CANL routed as a controlled pair where practical.
- Place termination at intended bus ends only.
- Place TVS/protection close to the connector.
- Review common-mode choke placement if used.
- Keep connector pinout and cable orientation under human review.

## Required Flags

- `CAN_LAYOUT_REVIEW_REQUIRED`
- `CAN_TERMINATION_PLACEMENT_REVIEW_REQUIRED`
- `CAN_PROTECTION_PLACEMENT_REVIEW_REQUIRED`
- `CAN_CONNECTOR_ORIENTATION_HUMAN_REVIEW_REQUIRED`
