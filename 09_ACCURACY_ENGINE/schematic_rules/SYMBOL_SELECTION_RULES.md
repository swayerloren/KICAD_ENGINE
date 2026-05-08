# Symbol Selection Rules

## Prime Rule

A KiCad symbol is a candidate until its pin numbers, functions, units, hidden pins, and electrical types are checked against a verified source.

## Selection Order

1. Project-local symbol library.
2. User-global symbol library, read-only.
3. Installed KiCad stock library.
4. New project-local symbol created from source evidence.

## Required Checks

- Exact part number or generic symbol scope.
- Pin count.
- Pin numbers.
- Pin names and alternate functions.
- Power pins, including hidden power pins.
- No-connect pins and exposed pads.
- Electrical pin types.
- Multi-unit symbol mapping.
- Datasheet/source field.
- Footprint field if present.

## Do Not Approve When

- The symbol name is only similar to the part.
- A package variant has different pin numbers.
- Hidden power pins are not understood.
- The symbol is generic and the connector/part is exact-manufacturer-specific.
- The datasheet is missing.

## Required Status

Use one of:

- `SYMBOL_PINOUT_VERIFIED`
- `SYMBOL_CANDIDATE_ONLY`
- `SYMBOL_PINOUT_UNVERIFIED`
- `SYMBOL_REQUIRES_PROJECT_LOCAL_COPY`
## Mandatory Evidence Gate

A symbol is not selected for design use until its pin count, pin numbers, pin names, hidden pins, electrical types, and power pins are checked against a source document or verified project-local symbol evidence.

Allowed interim status:

- `SYMBOL_CANDIDATE_ONLY`
- `SYMBOL_PINOUT_UNVERIFIED`
- `REQUIRES_HUMAN_REVIEW`

Do not treat a matching symbol name as pinout proof.
