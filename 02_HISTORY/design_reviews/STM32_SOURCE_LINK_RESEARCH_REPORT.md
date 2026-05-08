# STM32 Source Link Research Report

Date: 2026-05-03
Status: `PARTIALLY_RESEARCHED_SOURCE_LINKS`

## 1. Families Researched

STM32F0, STM32F1, STM32F2, STM32F3, STM32F4, STM32F7, STM32G0, STM32G4, STM32H5, STM32H7, STM32L0, STM32L1, STM32L4, STM32L5, STM32U0, STM32U5, STM32WB, STM32WL, STM32MP

Note: `STM32MP` is present in the local STM32 folder tree and was included as a supplemental STM32 MPU source index even though the current prompt focused on STM32 MCU families.

## 2. Source Links Added

- `STM32_OFFICIAL_SOURCE_LINKS.csv` rows: 111
- Official/shared application-note and tool rows: 6
- Per-family source-link docs updated: 19

## 3. Part Indexes Added

- `STM32_PART_NUMBER_INDEX.csv` rows: 194
- Exact product-page rows currently marked `OFFICIAL_SOURCE_LINK`: 12
- Prefix or representative candidate rows requiring review: 182

## 4. Dev Board Indexes Added

- `STM32_DEV_BOARD_INDEX.csv` rows: 17
- Dev board/source markdown files updated per family: 19
- Official schematic-pack links are link-only and must not be redistributed as bundled PDFs without policy review.

## 5. Missing Families

No target family folder was skipped.

Families still missing an exact product-page row marked `OFFICIAL_SOURCE_LINK`: STM32F0, STM32F2, STM32F3, STM32F7, STM32H5, STM32L0, STM32L1, STM32L4, STM32L5, STM32U0, STM32WL, STM32MP

## 6. Uncertainty And Risk

- Exact reference manual URLs remain incomplete.
- Exact errata URLs remain incomplete.
- Exact package drawing URLs remain incomplete.
- Many part rows are family/prefix or representative candidates and remain `NEEDS_REVIEW`.
- Some exact board pages/schematic-pack links are indexed, but board revision matching is still required before circuit extraction.
- No PDFs were downloaded or bundled.
- No KiCad design files were edited.

## Result

Current classification: `PARTIALLY_RESEARCHED_SOURCE_LINKS`

This is a source-link index, not a verified STM32 component database.
