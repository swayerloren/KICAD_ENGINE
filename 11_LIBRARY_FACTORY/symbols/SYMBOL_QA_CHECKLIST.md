# Symbol QA Checklist

Use before a custom or candidate symbol is used in a KiCad schematic.

## Source Check

- Exact part number verified.
- Exact package verified.
- Pin table source recorded.
- Datasheet/source URL or local metadata path recorded.

## Pin Check

- Every source pin appears in symbol.
- Every symbol pin appears in source.
- Pin numbers match exact package.
- Pin names match source or documented convention.
- Electrical types reviewed.
- No-connect pins handled intentionally.
- Exposed pad handled intentionally.

## Readability Check

- Boot/reset/programming pins are visible.
- Power pins are visible or hidden by explicit convention.
- Multi-unit placement cannot hide required pins.
- Symbol value and fields are clear.

## Exit Status

- `SYMBOL_PINOUT_VERIFIED`: all checks complete with source evidence.
- `UNVERIFIED_SYMBOL`: source evidence incomplete.
- `REJECTED_SYMBOL`: mismatch found and not resolved.

