# CAN Bus Node Circuit

## Use Case

Use this pattern for a classical CAN node with an MCU CAN controller and CAN transceiver.

## Required Evidence

- Exact CAN transceiver datasheet.
- MCU CAN peripheral pin mapping.
- Bus topology requirements.
- Connector pinout and cable environment.

## Typical Schematic Block

- MCU CAN_TX and CAN_RX connected to transceiver logic pins.
- Transceiver VCC and VIO handled per datasheet.
- CANH and CANL routed to connector.
- Termination strategy documented: installed only where the node is at a bus end.
- TVS/protection considered for external cables.

## PCB Review Points

- Route CANH/CANL as a controlled, symmetric pair where practical.
- Place termination near the transceiver or connector according to design intent.
- Place ESD/TVS near the connector.
- Keep common-mode choke optional and source-backed.

## Common Mistakes

- Installing termination on every node.
- Swapping TX/RX logic pins.
- Ignoring VIO level compatibility with the MCU.
- Omitting protection on external automotive/industrial connectors.

## Verification Gate

Human review is required for connector pinout, termination policy, and cable/environment assumptions.

