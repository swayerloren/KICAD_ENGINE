# STM32 Minimum System Circuit

## Use Case

Use this pattern for a bare STM32 microcontroller design.

## Required Evidence

- Exact STM32 part datasheet.
- Family reference manual.
- ST hardware getting-started or application note for the family.
- Exact package drawing.

## Typical Schematic Block

- All VDD/VSS pins connected and decoupled.
- VDDA/VSSA handled separately when present.
- NRST circuit per ST guidance.
- BOOT0 or boot configuration pins handled per exact family.
- SWD header with SWDIO, SWCLK, reset, ground, and target voltage reference.
- Clocking plan: internal oscillator, HSE crystal, LSE crystal, or external clock.

## PCB Review Points

- Place decoupling near each supply pin group.
- Keep crystal traces short and follow the crystal/load-capacitor layout guide.
- Keep analog supply and ground treatment deliberate.
- Verify every power pin is present in the KiCad symbol.

## Common Mistakes

- Missing hidden power pins in the symbol.
- Leaving BOOT0 floating when the part requires a defined state.
- Forgetting VDDA/VSSA.
- Copying Blue Pill assumptions into a different STM32 family.
- Using a package footprint that matches pin count but not package variant.

## Verification Gate

Do not mark approved until the exact part/package power pins, boot pins, debug pins, clock pins, and footprint are verified.

