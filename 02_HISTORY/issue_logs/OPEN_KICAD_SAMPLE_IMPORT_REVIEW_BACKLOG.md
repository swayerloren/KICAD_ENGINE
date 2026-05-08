# Issue Log - Open KiCad Sample Import Review Backlog

Status: `OPEN`

Created: `2026-05-03`

## Issue

Three open KiCad sample projects were imported into the controlled sample-intake area, but they are not reviewed enough for benchmark scoring, public payload inclusion, or engineering claims.

## Affected Samples

- `32_OPEN_KICAD_SAMPLE_INTAKE/normalized_samples/tomasr8_attiny85_dev_board/`
- `32_OPEN_KICAD_SAMPLE_INTAKE/normalized_samples/m4a1x_tps5430/`
- `32_OPEN_KICAD_SAMPLE_INTAKE/normalized_samples/esp_rs_esp_rust_board/`

## Required Before Use As Benchmarks

- Final human license and attribution review.
- KiCad version compatibility check.
- ERC and DRC on normalized copies.
- Visual review.
- Footprint/package audit.
- BOM and PNP review where present.
- Distinguish upstream source Gerbers/outputs from KiCad Engine-generated `NOT_FINAL` outputs.

## Blocked Claims

- Do not claim these samples are verified reference designs.
- Do not claim they pass ERC/DRC.
- Do not claim they are fabrication-ready.
- Do not include them in public release payloads until public bundle review is complete.
