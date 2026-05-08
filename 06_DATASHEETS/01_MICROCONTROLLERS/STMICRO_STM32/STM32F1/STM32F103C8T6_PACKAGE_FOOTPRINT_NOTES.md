# STM32F103C8T6 Package And Footprint Notes

Date: 2026-05-03
Status: `NEEDS_HUMAN_REVIEW`

This file records candidate KiCad package/footprint evidence. It does not verify that the candidate footprint is correct for STM32F103C8T6.

## Evidence Labels

- `VERIFIED_SOURCE_LINK`: official/public URL recorded.
- `VERIFIED_FROM_DATASHEET`: exact package drawing checked in the ST datasheet/package document.
- `INFERRED_FROM_COMMON_DESIGN`: common footprint choice; not approval.
- `UNVERIFIED`: not checked.
- `NEEDS_HUMAN_REVIEW`: required before PCB.

## Candidate Package/Footprint

| Item | Candidate | Evidence | Status |
| --- | --- | --- | --- |
| orderable part | STM32F103C8T6 | ST product page lists this orderable part | `VERIFIED_SOURCE_LINK` |
| package | LQFP-48 candidate | Common mapping for T6 suffix, but exact datasheet/order-code table must be checked | `NEEDS_HUMAN_REVIEW` |
| KiCad symbol | `MCU_ST_STM32F1:STM32F103C8Tx` | Found in installed KiCad 9 symbol library | `VERIFIED_FROM_KICAD_LIBRARY` for existence only |
| KiCad footprint | `Package_QFP:LQFP-48_7x7mm_P0.5mm` | Found in installed KiCad 9 footprint library | `UNVERIFIED` exact package match |
| KiCad 3D model | `Package_QFP.3dshapes/LQFP-48_7x7mm_P0.5mm.step` | Footprint references local KiCad 9 STEP model | `UNVERIFIED` mechanical fit |

## Verification Required Before PCB

- Check ST package/order-code table for `STM32F103C8T6`.
- Check ST package drawing dimensions, pitch, lead span, body size, pin-1 mark, and tolerances.
- Inspect KiCad symbol pin numbers and hidden power pins against datasheet.
- Inspect KiCad footprint pad numbers, pad geometry, courtyard, fab outline, silkscreen, and pin-1 marker.
- Confirm 3D model orientation with package pin 1 and board assembly view.
- Create a package verification record under `08_COMPONENT_DATABASE/16_VERIFICATION_RECORDS/` if promoted.

## High-Risk Mistakes

- Assuming LQFP-48 from memory.
- Using an exposed-pad LQFP footprint when the selected package has no exposed pad.
- Flipping pin 1 or trusting silkscreen without package drawing.
- Treating 3D model presence as footprint verification.
