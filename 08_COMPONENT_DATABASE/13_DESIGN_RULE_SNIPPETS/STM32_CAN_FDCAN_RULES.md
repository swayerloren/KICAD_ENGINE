# STM32 CAN And FDCAN Rules

Date: 2026-05-02

Status: AI design-rule snippet. Exact peripheral availability, pins, and bus design must be verified from the selected STM32 datasheet/reference manual and transceiver datasheets.

## Source Baseline

- Exact STM32 product page, datasheet, and reference manual.
- ST family documentation for parts with CAN or FDCAN.
- CAN/FDCAN transceiver datasheet and connector requirements.

## Rules

- Confirm whether the MCU has classic CAN 2.0, FDCAN, both, or neither.
- Confirm TX/RX alternate-function pins for the selected package.
- Add an external CAN/CAN FD transceiver. MCU CAN pins are logic-level signals, not bus pins.
- Verify transceiver supply voltage, IO voltage, standby/silent pins, fault pins, and ESD/protection needs.
- Define termination strategy: on-board fixed termination, selectable termination, or no termination depending on bus position.
- For FDCAN, verify data-rate target, transceiver rating, oscillator tolerance, and network topology.
- Connector orientation and CANH/CANL labels must be reviewed visually before manufacturing outputs.

## Common Mistakes

- Connecting MCU CAN_TX/CAN_RX directly to a connector.
- Selecting a CAN 2.0 transceiver for a CAN FD data-rate requirement.
- Forgetting common-mode protection and bus fault exposure.
- Placing termination on every node.
- Swapping CANH/CANL at a connector or cable pinout.

## Verification Checklist

- CAN/FDCAN peripheral exists on exact part/package.
- Pin mux conflicts resolved.
- Transceiver selected and linked.
- Termination plan documented.
- Connector pinout and orientation checked.
