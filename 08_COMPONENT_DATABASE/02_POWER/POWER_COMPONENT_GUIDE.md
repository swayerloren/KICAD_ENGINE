# Power Component Guide

Date: 2026-05-02

Status: AI-readable guide for common PCB power parts. This is not a design-approved preferred-parts list.

## Purpose

This guide teaches Codex, Claude, and similar agents how to reason about common PCB power parts in KiCad without pretending that a generic symbol or a familiar module is enough evidence for a correct design.

Power components are high-risk because they combine electrical limits, heat, layout sensitivity, external component selection, sourcing, and safety behavior. Agents must treat power design as a verification workflow, not a part-name lookup.

## Required Agent Workflow

1. Identify the source and load.
2. Define the required input-voltage range, output voltage, load current, transient current, efficiency, noise, temperature, and fault behavior.
3. Choose topology before choosing a part.
4. Read the official datasheet and vendor layout guidance.
5. Check exact package suffix and pinout.
6. Check KiCad symbol pin mapping against the datasheet.
7. Check footprint dimensions against the exact package drawing.
8. Check external components: capacitors, inductor, diode, sense resistors, feedback network, compensation, thermistor, fuse, TVS, and MOSFETs.
9. Check heat using power dissipation and board copper assumptions.
10. Run ERC and DRC after implementation, then visually review polarity, connector orientation, copper width, thermal relief, and protection placement.

## Topology Selection

| Topology | Use When | Avoid When | Agent Warning |
| --- | --- | --- | --- |
| Buck regulator | Input is higher than output and load current or heat makes an LDO inefficient. | Layout skill, EMI, inductor choice, or switch-node control cannot be verified. | Do not copy random module layouts into a custom PCB. |
| LDO | Input is close to output, load current is modest, noise matters, or simplicity matters. | Voltage drop times current creates too much heat. | Output capacitor value and ESR/stability rules are part-specific. |
| Boost regulator | Output must be higher than input. | Startup, inrush, current limit, or battery behavior is not defined. | No boost records exist yet in this database. |
| Buck-boost | Input can cross above and below output. | Simpler buck or LDO can satisfy the requirement. | Needs part-specific compensation, inductor, thermal, and EMI review. |
| Linear charger | Single-cell battery charging with modest power and datasheet-supported battery chemistry. | Thermal behavior, battery protection, termination, or charge current is unknown. | Charger ICs are safety-relevant; do not invent battery details. |
| eFuse / hot-swap | Input needs controlled current, inrush, short-circuit, or overvoltage behavior. | The exact fault envelope is unknown. | eFuses still require SOA and thermal checks. |
| PTC fuse | Low-cost resettable overcurrent protection with acceptable hold/trip behavior. | Precise current limiting, fast fault interruption, or low resistance is required. | PTC trip behavior changes strongly with temperature. |
| TVS diode | External connector or supply rail needs transient clamp protection. | Source impedance, fuse coordination, standoff voltage, clamp voltage, and surge waveform are unknown. | A TVS without a return path and upstream impedance may not protect anything. |

## Power Part Records

Structured starter records are in:

- `08_COMPONENT_DATABASE/02_POWER/POWER_PART_RECORDS.md`
- `08_COMPONENT_DATABASE/02_POWER/power_part_records.json`

Current starter coverage:

- Buck regulators: LM2596, MP1584, TPS5430, TPS62177.
- LDOs: AMS1117-3.3, AP2112K-3.3, MCP1700, TLV755P, MIC5504.
- Battery chargers: TP4056, MCP73831.
- Protection: resettable polyfuse, SMAJ TVS diode, USB TVS diode, Schottky reverse-polarity diode, P-channel MOSFET reverse-polarity circuit.

Missing dedicated records:

- Boost regulators.
- Buck-boost regulators.
- Dedicated eFuses.
- Dedicated ideal-diode controllers.
- Automotive-qualified regulators and protection controllers.

## KiCad Usage Rules

- Use exact KiCad symbols only after checking the datasheet pinout.
- Do not use a regulator symbol variant with the wrong fixed voltage suffix.
- Do not use a footprint because it looks mechanically similar.
- Check exposed-pad footprints against the package drawing and thermal recommendations.
- For switching regulators, inspect the PCB layout for input capacitor loop, diode loop if asynchronous, switch-node copper area, inductor placement, feedback trace routing, thermal copper, and ground return.
- For LDOs, inspect input/output capacitor placement, thermal copper, enable pin state, and output capacitor requirements.
- For chargers, inspect battery connector polarity, battery protection assumptions, charge-current resistor, status LEDs, thermistor pins, and thermal path.
- For TVS and ESD parts, place protection at the connector before long traces enter the board.
- For reverse-polarity circuits, check MOSFET body diode orientation and gate-source voltage protection.

## Common False Confidence Traps

- Treating a common e-commerce LM2596 or MP1584 board as a verified reference design.
- Assuming AMS1117 is acceptable for 5V to 3.3V without heat calculation.
- Assuming any USB TVS array is valid for high-speed USB data.
- Assuming a polyfuse will protect semiconductors quickly.
- Assuming a TVS part number is valid because the package matches.
- Assuming charger modules include full battery protection.
- Assuming automotive 12V means only 12V nominal.
- Using exact part claims from memory instead of the current datasheet.

## Review Checklist

- Input connector current and voltage rating verified.
- Fuse or current limit selected from real hold/trip or limit data.
- Reverse polarity protection checked for voltage drop, heat, and body diode direction.
- TVS selected for standoff voltage, clamp voltage, pulse rating, and capacitance.
- Regulator input range covers steady-state and transient conditions.
- Regulator output current and thermal behavior are checked.
- External capacitor value, voltage, dielectric, ESR, and placement are checked.
- Switching regulator inductor saturation current and DCR are checked.
- Catch diode or synchronous rectifier path is checked.
- Feedback divider and compensation are checked when applicable.
- Battery charger chemistry, charge current, termination, and thermal behavior are checked.
- KiCad symbol, footprint, and 3D model are candidate-matched but still verified against the datasheet.
