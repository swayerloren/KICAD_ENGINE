# STM32F103C8T6 KiCad Symbol Footprint Match

Date: 2026-05-03
Match status: `CANDIDATE_ONLY`
Human review required: `true`

This file records local KiCad candidate evidence for STM32F103C8T6. It does not approve the symbol, footprint, or 3D model for PCB use.

## Evidence Labels

- `VERIFIED_SOURCE_LINK`: official/public URL recorded.
- `VERIFIED_FROM_DATASHEET`: exact pinout or package drawing checked in a named source document.
- `INFERRED_FROM_COMMON_DESIGN`: common match pattern; verify before use.
- `UNVERIFIED`: not checked.
- `NEEDS_HUMAN_REVIEW`: required before schematic/PCB/fab use.

## Match Summary

| Field | Value |
| --- | --- |
| manufacturer | STMicroelectronics |
| MPN | STM32F103C8T6 |
| component record | `08_COMPONENT_DATABASE/01_MICROCONTROLLERS/STM32F103C8T6.md` |
| datasheet URL | https://www.st.com/resource/en/datasheet/stm32f103c8.pdf |
| package drawing source | ST datasheet/package section required; not yet reviewed |
| KiCad symbol candidate | `MCU_ST_STM32F1:STM32F103C8Tx` |
| KiCad footprint candidate | `Package_QFP:LQFP-48_7x7mm_P0.5mm` |
| 3D model candidate | `${KICAD9_3DMODEL_DIR}/Package_QFP.3dshapes/LQFP-48_7x7mm_P0.5mm.step` |
| confidence | `MATCHED_BY_KICAD_LIBRARY_CANDIDATE_ONLY` |

## Local KiCad Evidence

| Evidence | Result | Status |
| --- | --- | --- |
| Symbol search | `STM32F103C8Tx` found in `C:\Program Files\KiCad\9.0\share\kicad\symbols\MCU_ST_STM32F1.kicad_sym` | `VERIFIED_FROM_KICAD_LIBRARY` for existence only |
| Footprint file | `C:\Program Files\KiCad\9.0\share\kicad\footprints\Package_QFP.pretty\LQFP-48_7x7mm_P0.5mm.kicad_mod` exists | `VERIFIED_FROM_KICAD_LIBRARY` for existence only |
| STEP model | `C:\Program Files\KiCad\9.0\share\kicad\3dmodels\Package_QFP.3dshapes\LQFP-48_7x7mm_P0.5mm.step` exists | `VERIFIED_FROM_KICAD_LIBRARY` for existence only |

## Required Promotion Checks

To promote this match to `VERIFIED_FROM_DATASHEET`, an agent must:

1. Open the exact ST datasheet and identify the `STM32F103C8T6` package/order-code row.
2. Confirm the package drawing and pin count.
3. Compare every KiCad symbol pin number/name/electrical type to the datasheet pin table.
4. Compare KiCad footprint pad numbering, pad dimensions, pitch, courtyard, fab outline, silkscreen, and pin-1 marker to the package drawing.
5. Confirm the STEP model orientation matches pin 1.
6. Create/update a verification record under `08_COMPONENT_DATABASE/16_VERIFICATION_RECORDS/`.
7. Require human review before using the match in a layout.

## Hard Warnings

- `NEEDS_HUMAN_REVIEW`: Similar package names are not proof.
- `NEEDS_HUMAN_REVIEW`: KiCad stock library presence is not datasheet verification.
- `NEEDS_HUMAN_REVIEW`: Do not use an exposed-pad LQFP footprint variant unless the exact selected package has an exposed pad.
- `NEEDS_HUMAN_REVIEW`: Do not update PCB from schematic with this part unless the project gate has an explicit footprint/package audit result.
