# Component Research Standard

Use this standard when researching parts for KiCad Engine.

## Source Priority

1. Official vendor datasheet or product page.
2. Official reference manual, hardware design guide, errata, or app note.
3. Official reference design or evaluation board schematic.
4. KiCad stock library evidence.
5. Distributor pages only as search aids, not final authority.

## Required Fields

Capture:

- Vendor.
- Part number.
- Family.
- Package.
- Lifecycle status if available.
- Source URLs.
- Datasheet local path or link-only status.
- KiCad symbol candidates.
- KiCad footprint candidates.
- 3D model candidates.
- Power notes.
- Pinout status.
- Footprint status.
- Layout notes.
- Required external parts.
- Common mistakes.
- Known errata.
- Verification flags.

## Verification Flags

Use only flags that are actually proven:

- `VERIFIED_FROM_DATASHEET`
- `VERIFIED_FROM_VENDOR_REFERENCE_DESIGN`
- `VERIFIED_FROM_KICAD_LIBRARY`
- `USER_CONFIRMED`
- `UNVERIFIED_PLACEHOLDER`

## Prohibited Claims

Do not invent:

- Voltage ranges.
- Current limits.
- Absolute maximum ratings.
- Pin functions.
- Package dimensions.
- Thermal claims.
- RF performance.
- USB/CAN compliance.
- Lifecycle status.

Use `Unknown - requires source verification` when exact data has not been confirmed.

## Output

Write records under `08_COMPONENT_DATABASE` and source links under `06_DATASHEETS/00_INDEX` or the relevant category folder. Do not download PDFs unless the user explicitly asks and redistribution rules are clear.
