# Microchip PIC Minimum System Circuit

## Use Case

Use this pattern for PIC10/12/16/18/24/32 or dsPIC minimum systems.

## Required Evidence

- Exact Microchip datasheet.
- Programming/debug tool guide for PICkit, ICD, or equivalent.
- Exact package drawing.
- Oscillator configuration guidance if using an external crystal or resonator.

## Typical Schematic Block

- VDD/VSS connected and decoupled.
- MCLR/reset network per exact part guidance.
- ICSP header with VPP/MCLR, VDD, VSS, data, and clock pins as required.
- Oscillator circuit only when needed.
- Programming pins kept free of conflicting loads or isolated as required.

## PCB Review Points

- Keep ICSP header accessible.
- Verify MCLR/VPP voltage tolerance and connected circuitry.
- Keep oscillator traces short.
- Verify package pinout against exact suffix.

## Common Mistakes

- Loading ICSP pins so programming fails.
- Incorrect MCLR pullup or missing reset protection.
- Assuming all PICs use the same programming pin names.
- Mixing 5 V and 3.3 V assumptions.

## Verification Gate

Do not mark approved until programming pins, MCLR, oscillator, supply voltage, and package pinout are verified from Microchip sources.

