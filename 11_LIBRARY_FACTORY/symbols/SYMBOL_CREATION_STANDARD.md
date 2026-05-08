# Symbol Creation Standard

## Required Source Evidence

Before creating or approving a symbol, collect:

- Exact part number.
- Package or ordering suffix if the pinout changes by package.
- Datasheet or reference manual.
- Pin table and package pinout.
- Functional pin descriptions.
- Power pin requirements.
- No-connect and exposed-pad requirements.

## Project-Local First

Generated or custom symbols should go into a project-local `.kicad_sym` library unless the user explicitly requests a reusable shared library.

Do not modify:

- Installed KiCad symbol libraries.
- User-global KiCad symbol libraries.
- User-global `sym-lib-table`.

## Creation Steps

1. Create the symbol from an exact source pin table.
2. Add every pin number, pin name, and electrical type.
3. Mark no-connect pins intentionally.
4. Represent exposed pads if electrical or thermal connection matters.
5. Separate units only when it improves readability or matches established KiCad practice.
6. Add required fields: reference, value, footprint candidate, datasheet/source, verification status.
7. Record source title, revision/date if known, and source URL/local path.

## Approval Rule

Symbol status is `SYMBOL_PINOUT_VERIFIED` only after every pin number and function is checked against source evidence. Until then, use `UNVERIFIED_SYMBOL`.

