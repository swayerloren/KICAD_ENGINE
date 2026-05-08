# CAN FD Node Circuit

## Use Case

Use this pattern for CAN FD designs that need higher data rates than classical CAN.

## Required Evidence

- Exact CAN FD transceiver datasheet.
- MCU CAN FD peripheral capability.
- Network bitrate, cable length, and topology requirements.
- Protection and connector drawings.

## Typical Schematic Block

- MCU FDCAN/CAN FD pins connected to transceiver logic interface.
- Correct VCC/VIO voltage domains.
- CANH/CANL to connector.
- Termination and optional split termination documented.
- TVS and optional common-mode choke evaluated.

## PCB Review Points

- Keep CANH/CANL short, symmetric, and away from noisy switching nodes.
- Avoid unnecessary stubs.
- Use source-backed termination strategy.
- Check transceiver package thermal and exposed-pad requirements.

## Common Mistakes

- Using a classical-only CAN transceiver for CAN FD.
- Assuming every MCU CAN peripheral supports CAN FD.
- Ignoring signal integrity at higher bit rates.
- Mixing 5 V transceiver logic with 3.3 V MCU pins without VIO support.

## Verification Gate

Do not approve until transceiver, MCU peripheral, termination, connector orientation, and protection are verified.

