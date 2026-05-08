# CAN Bus Layout Rules

Date: 2026-05-02

Status: AI guidance for CAN and CAN FD PCB work. Verify against the selected transceiver, controller, connector, and bus standard before release.

## Core Rule

CAN layout is a bus-system problem, not only a transceiver symbol problem.

Agents must verify:

- Whether the design uses classic CAN or CAN FD.
- Whether the MCU has a CAN/CAN FD controller, or an external controller is required.
- Transceiver supply and logic voltage domain.
- Bus connector pinout and polarity.
- Termination strategy.
- ESD and transient protection strategy.
- Cable length, data rate, topology, and number of nodes.
- Common ground or isolation requirements.

## Termination

- A normal CAN trunk uses termination at the two physical ends of the bus.
- Do not place a fixed termination resistor on every node unless the project specifically requires it.
- If the board may be an end node, make termination selectable with a jumper, solder bridge, switch, or BOM option.
- Split termination can reduce noise in some designs, but component values and center filtering must be verified.
- CAN FD makes stubs and reflections more critical than slow classic CAN designs.

## Routing

- Route CANH and CANL together as a pair.
- Keep stubs short.
- Avoid routing CAN bus traces under noisy switch nodes, crystals, RF antennas, or high-current loops.
- Keep the transceiver close to the external connector when practical.
- Place bus ESD/TVS near the connector before the bus traces run across the board.
- Provide a low-impedance return path for protection devices.

## Protection

- Use bus-rated ESD/TVS devices selected for CAN common-mode and surge requirements.
- Do not use generic USB ESD parts on CAN unless voltage, capacitance, and surge ratings are verified.
- For automotive or long-cable CAN, define the transient environment before selecting protection.
- Consider common-mode choke only when the EMC requirement and transceiver guidance support it.

## Common Mistakes

- Reversing CANH and CANL at the connector.
- Adding 120 ohm termination to every node.
- Assuming MCP2562FD creates CAN FD support without a CAN FD controller.
- Connecting a 5V-only logic interface to a 3.3V MCU without VIO or level shifting.
- Omitting standby/silent pin state.
- Treating SN65HVD230 modules as proof that a production layout is correct.

## Verification Gate

Before claiming CAN readiness:

- Datasheet source links are recorded.
- KiCad symbol pinout matches exact package suffix.
- Footprint matches the package drawing.
- Termination placement and optionality are documented.
- Protection is placed at the connector.
- Connector pinout and silkscreen are visually reviewed.
- ERC and DRC are run after schematic/layout edits.
