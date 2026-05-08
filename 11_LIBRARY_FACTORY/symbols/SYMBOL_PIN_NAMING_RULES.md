# Symbol Pin Naming Rules

## Naming Source

Use the pin names from the datasheet or reference manual as the primary source.

## Rules

- Preserve exact pin names where they are meaningful.
- Use active-low notation consistently, preferably `_N` unless the datasheet convention is clearer.
- Do not rename pins to guessed functions.
- Do not hide alternate functions that affect design selection.
- Use visible names for boot, reset, programming, clock, power, and communication pins.
- Mark uncertain names as `Unknown - requires source verification`.

## Pin Numbering

- Pin numbers must match the exact package.
- Do not use a pinout from a different package.
- Do not assume modules, bare ICs, and dev boards share pin numbering.
- Exposed pads must be represented if the datasheet assigns a pad number or required connection.

## Review Questions

- Does every symbol pin number appear in the source pin table?
- Does every source pin appear in the symbol?
- Are no-connect pins intentional?
- Are boot/reset/programming pins obvious?

