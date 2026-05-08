# Passives Guide

Date: 2026-05-02

Status: AI-readable starter guide. Generic values are design prompts, not approved BOM entries.

## Scope

This guide covers common capacitors, resistors, jumpers, ferrite beads, common mode chokes, and crystals that appear in many KiCad PCB designs.

## Capacitor Rules

- Verify voltage rating, dielectric, tolerance, package, and effective capacitance after DC bias.
- Use local decoupling for each relevant IC power pin or power-pin group based on the IC datasheet.
- Treat bulk capacitance as a power-integrity choice tied to load steps, regulator stability, and cable/input behavior.
- Verify regulator input and output capacitor ESR and minimum capacitance requirements from the regulator datasheet.

## Resistor Rules

- Verify value, tolerance, voltage rating, power rating, and package.
- Pull-up and pull-down values must be checked against leakage, bus speed, boot strap timing, and external devices.
- 0 ohm jumpers must be sized for current and assembly intent, not used as a hidden design dependency.

## Ferrite And Choke Rules

- Ferrite beads require impedance-vs-frequency, DC current, DC resistance, and power dissipation verification.
- Common mode chokes require mode-specific impedance and signal-integrity review.
- Do not place ferrites or chokes in high-speed paths without checking insertion loss, balance, and vendor layout guidance.

## Crystal Rules

- Select crystal frequency from MCU or radio requirements.
- Verify load capacitance, ESR, drive level, tolerance, stability, aging, and package.
- Calculate load capacitors from the selected crystal and board parasitics. A nominal 22pF capacitor is not universal.

## KiCad Workflow

1. Start from exact IC or connector requirements.
2. Choose a generic placeholder only to document design intent.
3. Replace the placeholder with a manufacturer part before schematic release.
4. Match KiCad footprints to manufacturer package drawings.
5. Keep passive layout rules in the schematic notes or PCB review checklist where they affect routing.
