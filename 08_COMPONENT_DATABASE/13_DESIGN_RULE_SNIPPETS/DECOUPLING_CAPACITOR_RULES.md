# Decoupling Capacitor Rules

Date: 2026-05-02

Status: rule snippet for AI-assisted schematic and PCB review.

## Selection Rules

- Select decoupling values from the IC datasheet, reference design, or validated power-integrity plan.
- Verify capacitor voltage rating, dielectric, tolerance, package, effective capacitance under DC bias, and temperature behavior.
- Use bulk capacitors where load steps, cable inductance, regulator stability, or board zones require local energy storage.
- Verify regulator input and output capacitor requirements before copying generic values.
- Treat 0.1uF and 10uF as common starting placeholders, not proof of a correct design.

## Layout Rules

- Place each local decoupling capacitor close to its IC power and ground pins.
- Minimize loop area from power pin to capacitor to ground return.
- Use short, direct traces or vias to the relevant power and ground planes.
- Avoid routing high-current or switching loops through sensitive decoupling returns.
- Put bulk capacitance near regulators, connectors, and load clusters as needed.

## KiCad Review Checklist

- Every power pin or power-pin group has a documented decoupling plan.
- Capacitor footprint and voltage rating are compatible with the selected part.
- Capacitor placement is visible in PCB review, not only in schematic.
- Power net names distinguish input, regulated output, analog, digital, RF, and noisy rails.
- DRC catches clearance issues around small passives and dense power pins.

## AI Warnings

- Do not assume "one 0.1uF per chip" is sufficient for MCUs, radios, converters, or high-speed interfaces.
- Do not assume a 10uF MLCC actually provides 10uF at operating voltage.
- Do not silently omit analog or RF rail decoupling because digital power pins are covered.
