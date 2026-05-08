# Datasheet To Symbol Workflow

Use this workflow when creating, selecting, or verifying a KiCad symbol from a datasheet or reference manual.

Required companion standards:

- `11_LIBRARY_FACTORY/README.md`
- `11_LIBRARY_FACTORY/symbols/SYMBOL_CREATION_STANDARD.md`
- `11_LIBRARY_FACTORY/symbols/SYMBOL_PIN_NAMING_RULES.md`
- `11_LIBRARY_FACTORY/symbols/SYMBOL_POWER_PIN_RULES.md`
- `11_LIBRARY_FACTORY/symbols/SYMBOL_MULTI_UNIT_RULES.md`
- `11_LIBRARY_FACTORY/symbols/SYMBOL_FIELD_RULES.md`
- `11_LIBRARY_FACTORY/symbols/SYMBOL_DATASHEET_LINK_RULES.md`
- `11_LIBRARY_FACTORY/symbols/SYMBOL_QA_CHECKLIST.md`
- `11_LIBRARY_FACTORY/mapping/PROJECT_LOCAL_LIBRARY_RULES.md`

## Hard Rules

- Do not create or approve a symbol from memory.
- Do not use a pinout from a different package.
- Do not modify installed KiCad symbol libraries.
- Prefer project-local `.kicad_sym` libraries for generated/custom symbols.
- Keep status `UNVERIFIED_SYMBOL` until every pin is checked against source evidence.

## Steps

1. Identify exact part number and package.
2. Record source document and revision if known.
3. Extract pin table, package pinout, power pins, no-connect pins, exposed pads, and alternate functions.
4. Check whether a stock KiCad symbol is only a candidate or truly package-correct.
5. Choose an existing verified symbol or create a project-local symbol.
6. Map every pin number, name, function, and electrical type.
7. Handle hidden power pins, no-connects, exposed pads, and alternate units deliberately.
8. Add symbol fields: reference, value, footprint candidate, datasheet, MPN, manufacturer, verification status, and source document.
9. Add or update datasheet/source links without bundling restricted PDFs.
10. Run `11_LIBRARY_FACTORY/scripts/validate_symbol_file.py` if a symbol file exists and record the report.
11. Review against source before schematic use.

## Required Review Questions

- Does every source pin appear in the symbol?
- Does every symbol pin appear in the source?
- Are pin numbers correct for the exact package?
- Are power pins visible or intentionally handled by KiCad convention?
- Are boot, reset, programming, clock, and interface pins obvious?
- Are no-connect and exposed-pad pins handled intentionally?
- Is the datasheet/source link exact enough for later review?

## Failure Conditions

Keep status `UNVERIFIED_SYMBOL` or `REJECTED_SYMBOL` if:

- Any pin is missing.
- Any pin number is uncertain.
- The source document is missing.
- The package pinout differs from the candidate symbol.
- Hidden power pins could hide ERC issues.
- The symbol comes from an unknown third-party source.

## Exit Criteria

Symbol status is `SYMBOL_PINOUT_VERIFIED` only after every pin has been compared to source evidence and the symbol QA checklist passes.

Script output is supporting evidence only. It does not replace human/source review.
