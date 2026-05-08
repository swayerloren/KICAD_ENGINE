# STM32F1 Pilot Content Completion Claim Evidence Matrix

Date: 2026-05-03

| Claim | Status | Evidence |
| --- | --- | --- |
| STM32F1 pilot files were created/updated. | `VERIFIED_BY_FILE` | Requested files exist under `06_DATASHEETS/01_MICROCONTROLLERS/STMICRO_STM32/STM32F1`. |
| STM32F103C8T6 component record exists. | `VERIFIED_BY_FILE` | `08_COMPONENT_DATABASE/01_MICROCONTROLLERS/STM32F103C8T6.md`. |
| STM32F103C8T6 match record exists. | `VERIFIED_BY_FILE` | `08_COMPONENT_DATABASE/12_KICAD_SYMBOL_FOOTPRINT_MATCHES/STM32F103C8T6_MATCH.md`. |
| Official ST source links were recorded. | `VERIFIED_BY_FILE`, `VERIFIED_SOURCE_LINK` | `SOURCES.md` and `STM32F1_SOURCE_LINKS.md`. |
| No PDFs were downloaded into STM32F1 pilot folder. | `VERIFIED_BY_COMMAND` | `Get-ChildItem` extension check returned no PDF/ZIP files. |
| KiCad symbol candidate exists locally. | `VERIFIED_BY_COMMAND` | `rg` found `STM32F103C8Tx` in installed KiCad 9 symbol library. |
| KiCad footprint candidate exists locally. | `VERIFIED_BY_COMMAND` | `rg` found `LQFP-48_7x7mm_P0.5mm` in installed KiCad 9 footprint library. |
| Candidate footprint is correct for STM32F103C8T6. | `UNVERIFIED` | Explicitly not claimed; requires package drawing review and human review. |
| STM32F103C8T6 pinout is verified. | `UNVERIFIED` | Explicitly not claimed; requires datasheet pin table audit. |
| No KiCad design/library files were modified. | `VERIFIED_BY_COMMAND` | Recent-write check over KiCad design/library extensions returned no files. |
