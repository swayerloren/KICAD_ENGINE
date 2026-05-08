# Schematic Score

Default schematic allocation: 20 points.

## Criteria

| Area | Points | Checks |
| --- | ---: | --- |
| Functional block completeness | 4 | Required circuit blocks are present and connected for the task |
| Power design correctness | 4 | Voltage rails, regulators, enable pins, protection, and current assumptions are source-backed or marked unverified |
| Decoupling completeness | 3 | Local decoupling, bulk capacitance, analog rails, and placement notes are included where applicable |
| Boot/debug/programming | 3 | Reset, boot pins, SWD/JTAG/UART/USB programming, and straps are handled correctly for MCU tasks |
| Interfaces and connectors | 3 | USB/CAN/LIN/RS485/RF/connector circuits follow source-backed rules and human review gates |
| ERC discipline | 2 | ERC report exists or absence is justified for a planning-only task |
| Schematic clarity | 1 | Net labels, hierarchy, notes, and BOM fields are understandable |

## Automatic Penalties

- Missing power rail assumptions: subtract up to 4.
- Missing decoupling on IC power pins: subtract up to 3.
- Incorrect boot/debug wiring: subtract up to 3.
- Connector pinout not reviewed: subtract up to 3.
- ERC failure not discussed: subtract up to 2.

## Required Human Review Flags

- Connector orientation.
- Polarity-sensitive parts.
- High-current paths.
- RF, USB, CAN, automotive, and safety-related blocks.
- Any symbol pinout that is not backed by exact source evidence.
