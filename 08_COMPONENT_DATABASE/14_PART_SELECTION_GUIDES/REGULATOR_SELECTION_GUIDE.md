# Regulator Selection Guide

Date: 2026-05-02

Status: AI-readable selection guide for common PCB regulators. This is not a preferred-parts list.

## First Questions

Before selecting a regulator, answer:

- What is the minimum, nominal, and maximum input voltage.
- What is the output voltage and tolerance requirement.
- What is the average, peak, and startup load current.
- Is low noise more important than efficiency.
- What ambient temperature and enclosure conditions apply.
- What fault behavior is required.
- Is the output powering RF, analog, USB, MCU core, sensors, motors, relays, or connectors.
- Is the board powered from USB, battery, wall adapter, or vehicle input.
- Are there size, EMI, heat, or cost limits.

## LDO Decision

Use an LDO when:

- Input voltage is close enough to output voltage for acceptable heat.
- Load current is modest.
- Low noise or simplicity matters.
- Layout area and BOM complexity must stay low.

Avoid an LDO when:

- Power dissipation is too high.
- Dropout margin is not available.
- The exact output capacitor stability rules are not verified.
- The package cannot shed the heat in the board environment.

Agent calculation required:

```text
LDO heat = (VIN - VOUT) * ILOAD
```

If the result is not clearly safe for the package and PCB copper, choose a switching regulator or reduce the load.

## Buck Decision

Use a buck regulator when:

- Input voltage is higher than output voltage.
- Load current makes an LDO inefficient or hot.
- Battery life, USB current budget, or thermal performance matters.

Avoid a buck when:

- Layout cannot be controlled.
- EMI risk is unacceptable.
- Inductor and compensation values are not verified.
- The switch-node, input loop, and feedback routing cannot be reviewed.

Buck design must verify:

- Input voltage range.
- Output current and transient response.
- Inductor value, saturation current, and DCR.
- Catch diode rating for asynchronous parts.
- Input and output capacitor value, voltage, dielectric, ripple, and placement.
- Feedback divider and compensation.
- Thermal pad and copper.
- Vendor layout example.

## Boost And Buck-Boost Decision

Use boost or buck-boost only when the power tree requires it. These topologies are more sensitive to startup, current limit, load disconnect, battery sag, and compensation.

This database does not yet include source-verified boost or buck-boost part records. Agents should mark boost selection as missing research until records are added.

## Battery Charger Decision

Battery charger ICs require battery chemistry, cell count, capacity, charge current, thermal limits, protection assumptions, connector polarity, termination behavior, and safety review.

Do not use TP4056 or MCP73831 as generic battery magic. They are starting points for single-cell charger research only, and project-specific battery safety rules must dominate.

## Common Starter Parts In This Database

| Role | Starter Records | Primary Warning |
| --- | --- | --- |
| Older buck regulator | LM2596 | Large external parts, heat, diode, and layout still matter. |
| Compact buck regulator | MP1584 | MPS marks MP1584 not recommended for new designs; verify lifecycle before new work. |
| Wide-input buck | TPS5430 | High-current layout and thermal review required. |
| Low-current buck | TPS62177 | Verify current target, package, and sleep-mode behavior. |
| Legacy/common LDO | AMS1117-3.3 | Heat and clone/source ambiguity are major risks. |
| Small 3.3V LDO | AP2112K-3.3 | Verify package suffix, pinout, capacitor requirements, and thermal margin. |
| Low quiescent LDO | MCP1700 | Verify current, dropout, package, and capacitor requirements. |
| Modern small LDO | TLV755P | Verify fixed-voltage suffix, package, and output capacitor. |
| Small LDO | MIC5504 | Verify exact output-voltage suffix and thermal behavior. |
| Linear Li-ion charger | MCP73831 | Verify battery safety, charge current, thermals, and status behavior. |
| Common charger ecosystem | TP4056 | Official source and module behavior must be verified before use. |

## AI Selection Rules

- If exact input range is unknown, do not choose a regulator.
- If load current is unknown, do not choose a package.
- If thermal environment is unknown, do not approve an LDO.
- If the output powers an ESP32, radio, USB peripheral, motor, relay, or external connector, require transient-current and protection review.
- If the part is common on low-cost modules, do not assume those modules are reference designs.
- If a package has an exposed pad, do not ignore the pad or vias.
- If a buck regulator has a switch node, require layout review before confidence.

## KiCad Review Rules

- Match symbol suffix to fixed voltage and package.
- Match footprint to package drawing, not just pin count.
- Check capacitor footprints for voltage and dielectric derating.
- Check inductor footprint for saturation-current capable parts.
- Check diode footprint and polarity for asynchronous buck designs.
- Label rails clearly.
- Add test points for major rails.
- Run ERC/DRC and perform visual review before any fabrication-style output.
