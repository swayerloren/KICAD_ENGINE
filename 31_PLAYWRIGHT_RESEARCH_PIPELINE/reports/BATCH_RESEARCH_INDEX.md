# Batch Research Index

Run ID: `20260503_122259_batch_expansion`

Status: `DRY_RUN_BATCH_EXPANSION_COMPLETE`

Live capture status: `BLOCKED_PLAYWRIGHT_NOT_AVAILABLE`

No PDFs were downloaded. No credentials were used. No KiCad design files were edited. This does not make the database complete.

| Batch | Scope | Records | Classification | Report |
| --- | --- | ---: | --- | --- |
| `batch_001_esp32` | ESP32 modules and dev boards | 10 | `SOURCE_LINKS_CAPTURED` + `NEEDS_HUMAN_REVIEW` | `BATCH_001_ESP32_REPORT.md` |
| `batch_002_stm32` | STM32 common chips and dev boards | 12 | `SOURCE_LINKS_CAPTURED` + `NEEDS_HUMAN_REVIEW` | `BATCH_002_STM32_REPORT.md` |
| `batch_003_pic_avr` | PIC/AVR common chips and dev boards | 10 | `SOURCE_LINKS_CAPTURED` + `NEEDS_HUMAN_REVIEW` | `BATCH_003_PIC_AVR_REPORT.md` |
| `batch_004_usb_c_connectors` | USB-C connectors | 7 | `SOURCE_LINKS_CAPTURED` + `NEEDS_HUMAN_REVIEW` | `BATCH_004_USB_C_CONNECTORS_REPORT.md` |
| `batch_005_can` | CAN transceivers and adjacent LIN target | 7 | `SOURCE_LINKS_CAPTURED` + `NEEDS_HUMAN_REVIEW` | `BATCH_005_CAN_REPORT.md` |
| `batch_006_power` | USB ESD/protection, regulators, and power protection | 15 | `SOURCE_LINKS_CAPTURED` + `NEEDS_HUMAN_REVIEW` | `BATCH_006_POWER_REPORT.md` |
| `batch_007_rf_connectors` | RF connectors, antennas, test pads, mounting holes, headers, and terminal blocks | 11 | `SOURCE_LINKS_CAPTURED` + `NEEDS_HUMAN_REVIEW` | `BATCH_007_RF_CONNECTORS_REPORT.md` |

## Output Files

- Batch dry-run outputs: `31_PLAYWRIGHT_RESEARCH_PIPELINE/output/20260503_122259_batch_expansion/`
- Consolidated normalized records: `31_PLAYWRIGHT_RESEARCH_PIPELINE/output/20260503_122259_batch_expansion/batch_expansion_all_normalized_records.json`
- Consolidated source links: `31_PLAYWRIGHT_RESEARCH_PIPELINE/output/20260503_122259_batch_expansion/batch_expansion_source_links.csv`
- Datasheet source links: `06_DATASHEETS/00_INDEX/PLAYWRIGHT_BATCH_SOURCE_LINKS.csv`
- Component stubs: `08_COMPONENT_DATABASE/99_UNVERIFIED_INBOX/playwright_batches/BATCH_COMPONENT_STUBS.json`
- Vendor source links: `25_VENDOR_DATABASE/00_INDEX/PLAYWRIGHT_BATCH_SOURCE_LINKS.json`
- Supplier normalized metadata: `28_SUPPLIER_INGESTION/normalized/playwright_batch_expansion/batch_expansion_normalized_records.json`
- Footprint backlog: `29_FOOTPRINT_GAP_ANALYSIS/reports/BATCH_MISSING_FOOTPRINT_BACKLOG.json`
- Supplier-footprint placeholders: `30_SUPPLIER_FOOTPRINT_MATCHES/matches/manual_source_link/BATCH_UNVERIFIED_MATCH_RECORDS.json`

## Rules

- Treat all rows as `UNVERIFIED` or `SOURCE_LINK_ONLY`.
- Do not claim database completeness.
- Do not mark any footprint verified without exact package drawing and human review.
- Do not download PDFs by default.

