# STM32F1 KiCad Symbol And Footprint Notes

Date: 2026-05-03
Status: `CANDIDATE_ONLY`

This file records installed KiCad 9 candidates for STM32F103C8T6. Candidate existence is not symbol pinout verification and not footprint package verification.

## Evidence Labels

- `VERIFIED_SOURCE_LINK`: official/public URL recorded.
- `VERIFIED_FROM_DATASHEET`: exact datasheet/package drawing checked.
- `INFERRED_FROM_COMMON_DESIGN`: common KiCad usage pattern; verify before use.
- `UNVERIFIED`: not checked against source.
- `NEEDS_HUMAN_REVIEW`: must be reviewed before schematic/PCB/fab use.

## Local KiCad Candidate Evidence

| Candidate | Local Evidence | Status |
| --- | --- | --- |
| `MCU_ST_STM32F1:STM32F103C8Tx` | `C:\Program Files\KiCad\9.0\share\kicad\symbols\MCU_ST_STM32F1.kicad_sym`, symbol line found by read-only search | `VERIFIED_FROM_KICAD_LIBRARY` for existence only |
| `Package_QFP:LQFP-48_7x7mm_P0.5mm` | `C:\Program Files\KiCad\9.0\share\kicad\footprints\Package_QFP.pretty\LQFP-48_7x7mm_P0.5mm.kicad_mod` | `VERIFIED_FROM_KICAD_LIBRARY` for existence only |
| `Package_QFP.3dshapes/LQFP-48_7x7mm_P0.5mm.step` | KiCad footprint references this STEP model and the file exists locally | `VERIFIED_FROM_KICAD_LIBRARY` for existence only |

## What Is Not Verified

- `UNVERIFIED`: Symbol pin numbers against STM32F103C8T6 datasheet.
- `UNVERIFIED`: Symbol electrical pin types and hidden power pins.
- `UNVERIFIED`: LQFP-48 package dimensions against ST package drawing.
- `UNVERIFIED`: Footprint pad geometry, toe/heel/side fillets, courtyard, assembly outline, and pin-1 mark.
- `UNVERIFIED`: 3D model pin-1 orientation and mechanical fit.

## AI Agent Rule

Do not promote this candidate match to `VERIFIED_FROM_DATASHEET` until a footprint/package audit cites the exact ST package drawing and records human review.
