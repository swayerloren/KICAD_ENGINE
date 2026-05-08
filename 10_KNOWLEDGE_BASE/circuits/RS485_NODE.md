# RS485 Node Circuit

## Use Case

Use this pattern for differential half-duplex or full-duplex RS485 interfaces.

## Required Evidence

- Exact RS485 transceiver datasheet.
- Bus topology, termination, biasing, and connector pinout.
- Isolation requirement if grounds may differ.

## Typical Schematic Block

- MCU UART TX/RX plus driver-enable and receiver-enable signals.
- A/B bus pins routed to connector.
- Termination installed only where appropriate.
- Bias resistors if required by the bus design.
- TVS and optional isolation for exposed or long cables.

## PCB Review Points

- Route A/B as a differential pair where practical.
- Place protection close to connector.
- Keep isolated and non-isolated grounds separated if using isolation.
- Label A/B polarity carefully because vendor naming can vary.

## Common Mistakes

- Reversing A and B because naming conventions differ.
- Missing DE/RE control.
- Installing termination on every node.
- Assuming common ground is safe for long industrial cables.

## Verification Gate

Do not approve until A/B polarity, termination, biasing, connector orientation, and isolation decision are reviewed.

