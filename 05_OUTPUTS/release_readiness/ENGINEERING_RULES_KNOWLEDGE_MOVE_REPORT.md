# Engineering Rules Knowledge Move Report

Date: `2026-05-11`
Task type: `DOCS_ONLY`

## Scope

Drain these `knowledge_scrape/` folders into canonical rule/checklist and
history/quarantine locations:

- `00_engineering_rules`
- `07_usb_c_high_speed_esd`
- `08_power_buck_regulators`
- `09_pcb_layout_grounding_emi_si`
- `20_manufacturer_layout_guides`
- `23_rf_wifi_antenna_layout`
- `24_power_integrity_decoupling`
- `25_signal_integrity_high_speed`
- `26_thermal_mechanical_enclosure`
- `27_test_debug_validation`

## Canonical Outputs

- New enforceable PCB rules under `09_ACCURACY_ENGINE/pcb_rules/`
- New enforceable schematic rules under `09_ACCURACY_ENGINE/schematic_rules/`
- New checklists under `09_ACCURACY_ENGINE/checklists/`
- Updated schematic-quality, prelayout, and PCB-quality gate docs
- New normalized summary areas under:
  - `10_KNOWLEDGE_BASE/summaries/`
  - `10_KNOWLEDGE_BASE/pcb_layout/`
  - `10_KNOWLEDGE_BASE/usb_c/`
  - `10_KNOWLEDGE_BASE/power_integrity/`
  - `10_KNOWLEDGE_BASE/rf_wifi/`
  - `10_KNOWLEDGE_BASE/thermal_mechanical/`

## Move Result

- Target source files moved: `149`
- Target source files quarantined: `131`
- Target source files archived to history: `18`
- Target source folders remaining: `0`
- `knowledge_scrape` file count before phase: `1854`
- `knowledge_scrape` file count after phase: `1705`

## Destination Summary

- Internal legacy rule notes:
  - `02_HISTORY/knowledge_scrape_migration/engineering_rules_archive/`
- Category metadata and empty-folder markers:
  - `02_HISTORY/knowledge_scrape_migration/engineering_metadata/`
- Raw scraped technical captures:
  - `21_LICENSE_ATTRIBUTION/license_risk_reviews/knowledge_scrape_quarantine/`

## Validation

- Every targeted source file has a moved ledger row: `PASS`
- Every targeted source folder is removed: `PASS`
- Rule docs cite source-registry entries: `PASS`
- Checklists link to canonical rules: `PASS`
- KiCad design files were not changed by this task: `PASS`

## Integrity Note

`git status` still shows the active schematic as dirty from earlier work, but
its SHA-256 remains unchanged in this task:

- SCH: `A82DD63FBD226227F777677D6EF5491BC9EAF27411A369C13A24C014F82F24E6`
- PCB: `ACA326C7B7C96AA67FED119E8DF54BDEBF80148C6B5F34F998780137C2BA1DD1`
- PRO: `CE1853F7614F591B5AF042ECBCF17ACC3BEB3D97091540B7B913D949900532D5`
