# Symbol Requirements Extraction

## Required Source Evidence

Extract symbol requirements only from exact source pinout information:

- Datasheet pin table.
- Reference manual pinout section.
- Module pinout table.
- Connector pinout drawing.
- User-confirmed pinout document.

## Extract Fields

- Pin numbers.
- Pin names.
- Pin functions.
- Electrical type.
- Power pins.
- Ground pins.
- No-connect pins.
- Exposed pad pins.
- Alternate functions.
- Reset, boot, programming, clock, and interface pins.

## Rules

- Do not create pinout from memory.
- Do not use a different package pinout.
- Do not hide power pins without deliberate review.
- Keep unclear pins as `Unknown - requires source verification`.

## Related Standards

- `11_LIBRARY_FACTORY/symbols/SYMBOL_CREATION_STANDARD.md`
- `11_LIBRARY_FACTORY/symbols/SYMBOL_PIN_NAMING_RULES.md`
- `11_LIBRARY_FACTORY/symbols/SYMBOL_POWER_PIN_RULES.md`

