# BOM And Output Review - ATtiny85 Golden Path Sample

Status: `NOT_FINAL_REVIEW_ONLY`

Generated: `2026-05-03`

## Outputs Created

The following review-only outputs were generated:

- `_verification/bom/attiny85_BOM_NOT_FINAL.csv`
- `_verification/schematic_visual/full_page/attiny85.svg`
- `_verification/schematic_visual/full_page/attiny85.pdf`
- `_verification/schematic_visual/full_page/attiny85.png`
- `_verification/pcb_visual/attiny85_top_NOT_FINAL.svg`
- `_verification/pcb_visual/attiny85_bottom_NOT_FINAL.svg`
- `_verification/pcb_visual/attiny85_top_NOT_FINAL.png`

No Gerbers, drill files, pick-and-place files, STEP exports, or fabrication packages were generated.

## BOM Content

KiCad exported 13 populated items:

- `D1`, `D2`: 3.6 Zener diodes
- `D3`, `D4`: LEDs
- `J1`: USB-A connector using `My footprints:MOLEX_48037-0001`
- `J2`: 2x5 header/socket
- `R1` through `R5`: resistors
- `U1`: ATtiny85-20P
- `U2`: AMS1117-3.3

## BOM Limitations

- No locked purchasing BOM exists for this demo fixture.
- No supplier SKU, lifecycle status, or exact MPN audit was performed.
- Several schematic datasheet fields are `~` or blank placeholders.
- `J1`, `J2`, and `U2` are intentionally blocked for human review.

## Result

`BOM_REVIEW_PARTIAL`

The BOM export works and is useful for demo review, but it is not a locked assembly BOM.
