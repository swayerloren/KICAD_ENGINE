# USB 5V To 3.3V Rules

Date: 2026-05-02

Status: AI guidance for USB-powered 3.3V PCB rails. Verify against USB, USB-C, regulator, ESD, and connector documentation before design release.

## Scope

This snippet covers boards that use USB VBUS as a 5V source and generate a 3.3V rail for MCUs, sensors, radios, or logic.

It does not approve any specific charger, USB-C implementation, regulator, or ESD part.

## Required Checks

- Is the connector USB-C, Micro-B, Mini-B, Type-A, or another connector.
- Is the port sink-only, source-only, dual-role, data-only, or charge-only.
- Is USB 2.0 data present.
- Does the board need USB PD, or only default USB-C sink behavior.
- What is the maximum 3.3V load current.
- What is the allowed inrush current.
- Whether the USB source is allowed to backfeed from another rail.
- Whether the board has a battery or alternate supply.

## USB-C Sink Basics

- A USB-C sink-only board needs correct CC pull-down behavior.
- Do not connect VBUS to the regulator and omit CC behavior on a USB-C receptacle.
- Do not short both USB-C data-side pins incorrectly. Confirm connector pinout, orientation, and routing.
- If USB data is used, route D+ and D- as a controlled pair appropriate to the board requirements and keep ESD capacitance low enough for the interface.
- If USB PD is used, add a verified PD controller and follow its reference design.

## Protection Chain

A typical USB-powered 3.3V board may need:

1. USB connector.
2. CC resistors or controller.
3. VBUS fuse, PTC, load switch, or eFuse.
4. VBUS TVS or surge protection when appropriate.
5. D+/D-/CC ESD protection when data or Type-C pins leave the connector.
6. Reverse-current or backfeed prevention when another rail can power the board.
7. 5V to 3.3V regulator.
8. Input and output capacitors close to the regulator.
9. 3.3V rail test point.

## Regulator Selection

- Use an LDO only when thermal dissipation is acceptable: heat is voltage drop times load current.
- Use a buck regulator when current or temperature makes an LDO unsuitable.
- Check regulator minimum input voltage at worst-case VBUS sag.
- Check startup and load transient behavior for radios such as ESP32 modules.
- Do not choose AMS1117 by habit; verify heat, dropout, package, and capacitor stability.
- Do not choose tiny LDOs without copper and thermal checks.

## Layout Rules

- Place VBUS protection close to the connector.
- Keep ESD return paths short and direct.
- Keep regulator input and output capacitors close to the regulator pins.
- Keep buck converter switch-node copper compact and away from USB data, RF, reset, boot, and analog traces.
- Keep feedback traces away from switch nodes and noisy current loops.
- Avoid routing USB data under inductors or hot switching loops.
- Label VBUS, 3.3V, and GND test points.

## Common Mistakes

- Treating USB-C as a mechanical connector only and omitting CC pull-downs.
- Using a high-capacitance TVS on USB data lines.
- Backfeeding USB VBUS from a board supply.
- Using an LDO that overheats at the required current.
- Copying a charger-module or dev-board power path without checking the exact schematic.
- Omitting a fuse/eFuse when the downstream rail can short externally.
- Placing the TVS far from the connector.

## Verification Gate

Before treating the USB 5V to 3.3V path as ready:

- Datasheet source links are recorded.
- KiCad symbols match pinouts.
- Footprints match package drawings.
- Regulator thermal estimate is recorded.
- USB-C orientation and CC behavior are reviewed.
- ERC and DRC are clean or waivers are documented.
- Visual review checks polarity, connector pin numbering, protection placement, and copper width.
