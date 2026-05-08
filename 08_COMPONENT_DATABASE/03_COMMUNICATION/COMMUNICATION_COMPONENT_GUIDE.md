# Communication Component Guide

Date: 2026-05-02

Status: AI-readable guide for communication interface components. This is not a design-approved preferred-parts list.

## Purpose

This guide helps Codex, Claude, and similar agents reason about common communication interface parts in KiCad designs without confusing protocol, voltage domain, connector wiring, ESD protection, termination, and layout requirements.

The component records are in:

- `08_COMPONENT_DATABASE/03_COMMUNICATION/COMMUNICATION_PART_RECORDS.md`
- `08_COMPONENT_DATABASE/03_COMMUNICATION/communication_part_records.json`

## Required Agent Workflow

1. Identify the interface: CAN, CAN FD, LIN, RS485, USB, Ethernet, UART, I2C, SPI, or level shifting.
2. Identify voltage domains on both sides of the part.
3. Identify whether the part is a controller, transceiver, PHY, bridge, protection device, or passive translator.
4. Verify exact package suffix and pinout from the official datasheet.
5. Verify KiCad symbol pin mapping against the datasheet.
6. Verify footprint dimensions against the exact package drawing.
7. Add required external parts: termination, pullups, bias resistors, ESD/TVS, common-mode chokes, crystals, magnetics, reset circuits, boot/strap resistors, or connectors.
8. Check layout constraints for the bus and connector.
9. Run ERC/DRC after implementation and perform visual review of pin numbering, polarity, connector orientation, and protection placement.

## Interface Roles

| Role | Examples | What Agents Must Not Confuse |
| --- | --- | --- |
| CAN transceiver | MCP2562, SN65HVD230, TJA1051, TJA1042 | A transceiver is not a CAN controller. The MCU must provide CAN or an external controller must exist. |
| CAN FD transceiver | MCP2562FD | CAN FD transceiver support does not mean the MCU/controller supports CAN FD. |
| LIN transceiver | MCP2003 | LIN has automotive battery-domain concerns and cannot be treated like UART wiring. |
| RS485 transceiver | MAX3485, SN65HVD75 | RS485 bus termination and biasing depend on topology. |
| USB UART bridge | CH340C, CP2102N, FT232RL | USB layout, VBUS, ESD, driver support, and reset behavior must be checked. |
| USB Type-C CC controller | TUSB320 | CC logic is not a full USB PD controller by itself. |
| USB ESD protection | USBLC6-2SC6 | ESD devices do not replace USB connector, CC, VBUS, or routing requirements. |
| Ethernet controller / PHY | W5500, LAN8720 | Magnetics, clocks, strap pins, and controlled routing are part of the design. |
| Level translator | PCA9306, TXS0108E, TXB0108 | Auto-direction level shifters are not universal and must match bus electrical behavior. |

## Common External Parts

- CAN/CAN FD: termination, optional split termination, common-mode choke when needed, ESD/TVS, connector, local decoupling, standby/silent pin control.
- LIN: pullup or master/slave network as required, reverse battery and automotive transient protection, local decoupling, connector protection.
- RS485: termination, fail-safe biasing when needed, TVS/ESD, common-mode choke when needed, connector, local decoupling, direction control.
- USB: connector, VBUS protection, CC resistors or controller for USB-C, ESD arrays, series resistors only when source guidance calls for them, controlled D+/D- routing.
- Ethernet: crystal/oscillator, magnetics or MagJack, termination networks, center-tap biasing, common-mode choke when required, LEDs, strap resistors, keepouts.
- I2C level shifting: pullups on both sides, reference rails, enable control, bus capacitance review.
- Push-pull level shifting: direction control or verified auto-direction suitability, output enable, capacitors, and load review.

## Common Mistakes

- Using MCP2562 or SN65HVD230 without a CAN controller.
- Using CAN FD transceivers with non-CAN-FD controllers and expecting CAN FD operation.
- Omitting CAN or RS485 termination strategy.
- Placing ESD protection far from the connector.
- Using TXB0108 for I2C or other open-drain buses without source verification.
- Using TXS0108E on heavy capacitive loads or strong push-pull buses without checking the datasheet.
- Assuming USB-C works with only D+/D- and VBUS.
- Using USBLC6 package variants with the wrong pinout.
- Forgetting Ethernet PHY strap pins or oscillator requirements.
- Copying module schematics without verifying magnetics, connector orientation, and shield/earth strategy.

## KiCad Review Rules

- Use symbol names as candidates only.
- Prefer exact part symbols when present, but still verify pinout.
- Match package suffix to footprint, not only pin count.
- Check bus-side pins against connector pin numbering.
- Place protection before long traces enter the board.
- Keep differential pairs together and avoid stubs where the bus requires it.
- Add explicit net labels for bus polarity: CANH/CANL, A/B, D+/D-, TX/RX, MDC/MDIO, RMII, SPI.
- Require visual review for connector orientation and silkscreen labels.
