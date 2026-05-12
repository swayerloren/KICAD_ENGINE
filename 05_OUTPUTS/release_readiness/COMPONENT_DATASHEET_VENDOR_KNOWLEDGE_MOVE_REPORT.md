# Component / Datasheet / Vendor Knowledge Move Report

Status: `APPLY_MODE_COMPLETED`

## Scope

Drained these legacy source folders:

- `knowledge_scrape/05_esp32_espressif`
- `knowledge_scrape/06_microcontrollers`
- `knowledge_scrape/13_vendor_parts_cad_models`
- `knowledge_scrape/14_datasheets_pdf_markdown`
- `knowledge_scrape/21_component_package_land_patterns`

## Move Summary

- Total files moved: `596`
- Moved to license quarantine: `375`
- Moved to history/metadata archives: `221`
- Remaining `knowledge_scrape` file count after this phase: `1109`

## Canonical Outputs Added Or Updated

### Datasheet surfaces

- `06_DATASHEETS/README.md`
- `06_DATASHEETS/DATASHEET_INDEX.md`
- `06_DATASHEETS/DATASHEET_SOURCE_POLICY.md`
- `06_DATASHEETS/DATASHEET_REDISTRIBUTION_RULES.md`
- `06_DATASHEETS/espressif/ESP32_SOURCE_INDEX.md`
- `06_DATASHEETS/microcontrollers/MICROCONTROLLER_SOURCE_INDEX.md`

### Component surfaces

- `08_COMPONENT_DATABASE/README.md`
- `08_COMPONENT_DATABASE/COMPONENT_SOURCE_INDEX.md`
- `08_COMPONENT_DATABASE/COMPONENT_EVIDENCE_RULES.md`
- `08_COMPONENT_DATABASE/HIGH_RISK_COMPONENTS_INDEX.md`
- `08_COMPONENT_DATABASE/component_index.json`

### Vendor / CAD / footprint surfaces

- `25_VENDOR_DATABASE/README.md`
- `25_VENDOR_DATABASE/VENDOR_SOURCE_POLICY.md`
- `25_VENDOR_DATABASE/JLCPCB_LCSC_PARTS_INDEX.md`
- `25_VENDOR_DATABASE/DIGIKEY_PARTS_INDEX.md`
- `25_VENDOR_DATABASE/MOUSER_PARTS_INDEX.md`
- `25_VENDOR_DATABASE/VENDOR_PART_NUMBER_CROSS_REFERENCE.md`
- `25_VENDOR_DATABASE/vendor_part_cross_reference.json`
- `29_FOOTPRINT_GAP_ANALYSIS/FOOTPRINT_GAP_RULES.md`
- `29_FOOTPRINT_GAP_ANALYSIS/LAND_PATTERN_SOURCE_INDEX.md`
- `29_FOOTPRINT_GAP_ANALYSIS/HIGH_RISK_FOOTPRINT_GAPS.md`
- `29_FOOTPRINT_GAP_ANALYSIS/footprint_gap_index.json`
- `30_SUPPLIER_FOOTPRINT_MATCHES/SUPPLIER_CAD_MODEL_RULES.md`
- `30_SUPPLIER_FOOTPRINT_MATCHES/CAD_MODEL_SOURCE_INDEX.md`
- `30_SUPPLIER_FOOTPRINT_MATCHES/cad_model_index.json`
- `35_FOOTPRINT_PACKAGE_ENGINE/FOOTPRINT_EVIDENCE_RULES.md`

## License Handling

- Raw ESP32, MCU, vendor, and CAD page captures were moved to:
  `21_LICENSE_ATTRIBUTION/license_risk_reviews/knowledge_scrape_quarantine/`
- Raw PDF and extracted PDF markdown payloads from
  `14_datasheets_pdf_markdown/` were treated as license-sensitive and
  quarantined.
- `23` unmatched raw PDFs remain in quarantine pending manual mapping.

## Validation

- All `596` target ledger rows are marked `MOVED_VALIDATED`.
- All five target source folders were removed.
- New JSON files parse successfully.
- Source registry JSON parses and CSV headers read cleanly.
- No KiCad design files were changed by this task.

## Canonical Follow-On Rule

Future migration prompts must continue from:

- `05_OUTPUTS/release_readiness/KNOWLEDGE_SCRAPE_MIGRATION_LEDGER.csv`
- `05_OUTPUTS/release_readiness/KNOWLEDGE_SCRAPE_DESTINATION_MAP.md`
- `05_OUTPUTS/release_readiness/KNOWLEDGE_SCRAPE_MIGRATION_STATUS.md`
