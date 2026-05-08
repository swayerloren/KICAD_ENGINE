# CAN Common Mistakes

## High-Risk Mistakes

- Installing termination on every node.
- Forgetting termination on an end node.
- Swapping CAN_TX and CAN_RX at the MCU/transceiver interface.
- Ignoring transceiver VIO compatibility.
- Using a classical CAN-only transceiver for CAN FD.
- Omitting protection on external or automotive connectors.
- Swapping CANH and CANL at the connector.

## Agent Checks

- Identify classical CAN or CAN FD.
- Verify MCU peripheral support.
- Verify transceiver voltage domains.
- Verify termination policy.
- Verify connector pinout and protection.

## Required Human Review

Human review is required for bus topology, termination, connector pinout, automotive/transient environment, and CANH/CANL polarity.

