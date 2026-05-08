# LIN Node Circuit

## Use Case

Use this pattern for Local Interconnect Network nodes in automotive or embedded harnesses.

## Required Evidence

- Exact LIN transceiver datasheet.
- Supply and wake/sleep behavior requirements.
- Connector and harness pinout.
- Automotive transient/protection requirements.

## Typical Schematic Block

- MCU UART TX/RX connected to LIN transceiver logic pins.
- LIN bus pin routed to connector.
- Battery/supply input protection as required by environment.
- Pullup/master termination only where the node is the LIN master.
- Wake, sleep, inhibit, or enable pins handled per datasheet.

## PCB Review Points

- Place bus protection near connector.
- Keep high-current automotive input paths away from logic.
- Verify thermal behavior if transceiver is powered from battery rail.
- Label connector pins clearly.

## Common Mistakes

- Adding master pullup on slave nodes.
- Forgetting wake/sleep pin default states.
- Treating LIN as plain UART without transceiver requirements.
- Omitting automotive transient protection.

## Verification Gate

Human review is required for master/slave role, connector pinout, and automotive power environment.

