# USB-C Layout Rules

Date: 2026-05-02

Status: AI guidance for USB-C and USB 2.0 PCB work. Verify against the USB-C connector, selected controller, ESD device, and USB requirements before release.

## Core Rule

USB-C is not only a connector shape. A USB-C design must define port role, CC behavior, VBUS behavior, data routing, ESD protection, and orientation mapping.

## Required Questions

- Is the port sink, source, dual-role, debug, or charge-only.
- Is USB 2.0 data used.
- Is USB PD required.
- Is the board bus-powered, self-powered, or battery-powered.
- Can another rail backfeed VBUS.
- Is the connector receptacle, plug, mid-mount, vertical, or edge-mounted.
- What cable/connector orientation and shield strategy are required.

## CC And VBUS

- A sink-only USB-C receptacle requires correct CC pull-down behavior or a verified CC controller.
- A source or dual-role port requires source/role logic and current advertisement rules.
- TUSB320-style CC logic is not a full USB PD controller.
- Do not connect VBUS directly to board power without current limiting, protection, and backfeed review.
- Add test points only where they do not create stubs or ESD exposure.

## D+/D- Routing

- Route D+ and D- as a pair.
- Keep the pair short, direct, and away from switch nodes, inductors, RF antennas, and high-current loops.
- Avoid unnecessary stubs and vias.
- Use the connector datasheet to map top/bottom D+ and D- pins correctly.
- Do not rely on visual pin names from a random footprint; verify pad numbers.

## ESD Protection

- Place ESD devices close to the connector.
- Choose low-capacitance ESD parts appropriate for USB data.
- Verify USBLC6 package variant and pinout before use.
- Provide a short return path for ESD current.
- VBUS protection and D+/D-/CC protection may require different devices.

## Common Mistakes

- Omitting CC resistors on a USB-C sink.
- Using USB-C as a four-wire Micro-B substitute.
- Mirroring D+ and D- incorrectly through a receptacle footprint.
- Backfeeding VBUS from the board.
- Placing ESD protection after long traces.
- Using a high-capacitance TVS on data lines.
- Assuming USB UART bridges need no reset, decoupling, oscillator, or driver review.

## Verification Gate

Before claiming USB-C readiness:

- Connector datasheet and footprint are verified.
- CC behavior is documented.
- VBUS current/protection/backfeed behavior is documented.
- ESD part package and pinout are checked.
- D+ and D- routing is visually reviewed.
- ERC and DRC are run after implementation.
