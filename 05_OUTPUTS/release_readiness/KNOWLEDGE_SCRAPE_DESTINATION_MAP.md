# Knowledge Scrape Destination Map

Status: `AUTO_GENERATED_MIGRATION_MAP`

This map defines how `knowledge_scrape/` content should be drained into
existing canonical KiCad Engine areas. It does not perform moves by
itself.

## Root File Rules

| Source | Action | Destination Root | Category | License Risk |
| --- | --- | --- | --- | --- |
| `FINAL_KNOWLEDGE_SCRAPE_REPORT.md` | `MOVE_AS_HISTORY_ONLY` | `02_HISTORY\knowledge_scrape_migration\original_metadata` | `knowledge_scrape_legacy_reports` | `LOW` |
| `INDEX.md` | `MOVE_AS_HISTORY_ONLY` | `02_HISTORY\knowledge_scrape_migration\original_metadata` | `knowledge_scrape_legacy_docs` | `LOW` |
| `INGEST_V2_IMPORT_REPORT.md` | `MOVE_AS_HISTORY_ONLY` | `02_HISTORY\knowledge_scrape_migration\original_metadata` | `knowledge_scrape_legacy_reports` | `LOW` |
| `MANIFEST.json` | `MOVE_AS_HISTORY_ONLY` | `02_HISTORY\knowledge_scrape_migration\original_metadata` | `source_registry_manifest` | `LOW` |
| `README.md` | `MOVE_AS_HISTORY_ONLY` | `02_HISTORY\knowledge_scrape_migration\original_metadata` | `knowledge_scrape_legacy_docs` | `LOW` |
| `RESCRAPE_QUEUE.csv` | `MOVE_AS_HISTORY_ONLY` | `02_HISTORY\knowledge_scrape_migration\original_metadata` | `knowledge_scrape_rescrape_queue` | `LOW` |
| `SOURCE_AUDIT.md` | `MOVE_AS_HISTORY_ONLY` | `02_HISTORY\knowledge_scrape_migration\original_metadata` | `knowledge_scrape_legacy_reports` | `LOW` |
| `STRUCTURE_IMPROVEMENT_REPORT.md` | `MOVE_AS_HISTORY_ONLY` | `02_HISTORY\knowledge_scrape_migration\original_metadata` | `knowledge_scrape_legacy_reports` | `LOW` |
| `URL_INDEX.csv` | `MOVE_AS_HISTORY_ONLY` | `02_HISTORY\knowledge_scrape_migration\original_metadata` | `source_registry` | `LOW` |
| `URL_INDEX.json` | `MOVE_AS_HISTORY_ONLY` | `02_HISTORY\knowledge_scrape_migration\original_metadata` | `source_registry` | `LOW` |
| `URL_INDEX.md` | `MOVE_AS_HISTORY_ONLY` | `02_HISTORY\knowledge_scrape_migration\original_metadata` | `source_registry_docs` | `LOW` |

## Path Prefix Rules

| Source Prefix | Action | Destination Root | Category | License Risk |
| --- | --- | --- | --- | --- |
| `00_ai_entrypoints\` | `MOVE_AS_HISTORY_ONLY` | `02_HISTORY\knowledge_scrape_migration\entrypoint_metadata\00_ai_entrypoints` | `entrypoint_metadata` | `LOW` |
| `00_engineering_rules\` | `MOVE_AS_HISTORY_ONLY` | `02_HISTORY\knowledge_scrape_migration\engineering_rules_archive\00_engineering_rules` | `engineering_rule_note_archive` | `LOW` |
| `00_retrieval_indexes\` | `MOVE_AS_HISTORY_ONLY` | `02_HISTORY\knowledge_scrape_migration\retrieval_metadata\00_retrieval_indexes` | `retrieval_metadata` | `LOW` |
| `00_source_of_truth\fabricator_rules\` | `MOVE_AS_FAB_RULE` | `24_FAB_PROFILES\knowledge_scrape_import` | `fabricator_rules` | `MEDIUM` |
| `00_source_of_truth\kicad_official_docs\` | `MOVE_NORMALIZED` | `10_KNOWLEDGE_BASE\kicad_official\knowledge_scrape_normalized` | `kicad_official_docs` | `MEDIUM` |
| `00_source_of_truth\official_app_notes\` | `MOVE_NORMALIZED` | `10_KNOWLEDGE_BASE\official_app_notes\knowledge_scrape_normalized` | `official_app_notes` | `MEDIUM` |
| `00_source_of_truth\official_datasheets\` | `MOVE_AS_DATASHEET_INDEX` | `06_DATASHEETS\knowledge_scrape_import\official_datasheets` | `official_datasheet_refs` | `MEDIUM` |
| `00_source_of_truth\SOURCE_OF_TRUTH_INDEX.md` | `MOVE_AS_HISTORY_ONLY` | `02_HISTORY\knowledge_scrape_migration\source_of_truth_metadata\00_source_of_truth` | `source_of_truth_metadata` | `LOW` |
| `01_kicad_core\` | `MOVE_TO_LICENSE_QUARANTINE` | `21_LICENSE_ATTRIBUTION\license_risk_reviews\knowledge_scrape_quarantine\01_kicad_core` | `kicad_core_reference` | `MEDIUM` |
| `01_kicad_core\.gitkeep` | `MOVE_AS_HISTORY_ONLY` | `02_HISTORY\knowledge_scrape_migration\kicad_docs_import_metadata\01_kicad_core` | `kicad_core_index_metadata` | `LOW` |
| `01_kicad_core\_CATEGORY_INDEX.md` | `MOVE_AS_HISTORY_ONLY` | `02_HISTORY\knowledge_scrape_migration\kicad_docs_import_metadata\01_kicad_core` | `kicad_core_index_metadata` | `LOW` |
| `02_kicad_python_api\` | `MOVE_TO_LICENSE_QUARANTINE` | `21_LICENSE_ATTRIBUTION\license_risk_reviews\knowledge_scrape_quarantine\02_kicad_python_api` | `kicad_python_api_reference` | `LOW` |
| `02_kicad_python_api\.gitkeep` | `MOVE_AS_HISTORY_ONLY` | `02_HISTORY\knowledge_scrape_migration\kicad_docs_import_metadata\02_kicad_python_api` | `kicad_python_api_index_metadata` | `LOW` |
| `02_kicad_python_api\_CATEGORY_INDEX.md` | `MOVE_AS_HISTORY_ONLY` | `02_HISTORY\knowledge_scrape_migration\kicad_docs_import_metadata\02_kicad_python_api` | `kicad_python_api_index_metadata` | `LOW` |
| `03_kicad_file_formats\` | `MOVE_TO_LICENSE_QUARANTINE` | `21_LICENSE_ATTRIBUTION\license_risk_reviews\knowledge_scrape_quarantine\03_kicad_file_formats` | `kicad_file_formats` | `MEDIUM` |
| `03_kicad_file_formats\.gitkeep` | `MOVE_AS_HISTORY_ONLY` | `02_HISTORY\knowledge_scrape_migration\kicad_docs_import_metadata\03_kicad_file_formats` | `kicad_file_formats_index_metadata` | `LOW` |
| `03_kicad_file_formats\_CATEGORY_INDEX.md` | `MOVE_AS_HISTORY_ONLY` | `02_HISTORY\knowledge_scrape_migration\kicad_docs_import_metadata\03_kicad_file_formats` | `kicad_file_formats_index_metadata` | `LOW` |
| `04_kicad_libraries_symbols_footprints\` | `MOVE_TO_LICENSE_QUARANTINE` | `21_LICENSE_ATTRIBUTION\license_risk_reviews\knowledge_scrape_quarantine\04_kicad_libraries_symbols_footprints` | `library_symbol_footprint_reference` | `MEDIUM` |
| `04_kicad_libraries_symbols_footprints\.gitkeep` | `MOVE_AS_HISTORY_ONLY` | `02_HISTORY\knowledge_scrape_migration\kicad_docs_import_metadata\04_kicad_libraries_symbols_footprints` | `kicad_libraries_index_metadata` | `LOW` |
| `04_kicad_libraries_symbols_footprints\_CATEGORY_INDEX.md` | `MOVE_AS_HISTORY_ONLY` | `02_HISTORY\knowledge_scrape_migration\kicad_docs_import_metadata\04_kicad_libraries_symbols_footprints` | `kicad_libraries_index_metadata` | `LOW` |
| `05_esp32_espressif\` | `MOVE_TO_LICENSE_QUARANTINE` | `21_LICENSE_ATTRIBUTION\license_risk_reviews\knowledge_scrape_quarantine\05_esp32_espressif` | `esp32_component_reference_capture` | `MEDIUM` |
| `05_esp32_espressif\.gitkeep` | `MOVE_AS_HISTORY_ONLY` | `02_HISTORY\knowledge_scrape_migration\component_datasheet_metadata\05_esp32_espressif` | `component_datasheet_metadata` | `LOW` |
| `05_esp32_espressif\_CATEGORY_INDEX.md` | `MOVE_AS_HISTORY_ONLY` | `02_HISTORY\knowledge_scrape_migration\component_datasheet_metadata\05_esp32_espressif` | `component_datasheet_metadata` | `LOW` |
| `06_microcontrollers\` | `MOVE_TO_LICENSE_QUARANTINE` | `21_LICENSE_ATTRIBUTION\license_risk_reviews\knowledge_scrape_quarantine\06_microcontrollers` | `microcontroller_reference_capture` | `MEDIUM` |
| `06_microcontrollers\.gitkeep` | `MOVE_AS_HISTORY_ONLY` | `02_HISTORY\knowledge_scrape_migration\component_datasheet_metadata\06_microcontrollers` | `component_datasheet_metadata` | `LOW` |
| `06_microcontrollers\_CATEGORY_INDEX.md` | `MOVE_AS_HISTORY_ONLY` | `02_HISTORY\knowledge_scrape_migration\component_datasheet_metadata\06_microcontrollers` | `component_datasheet_metadata` | `LOW` |
| `07_usb_c_high_speed_esd\` | `MOVE_TO_LICENSE_QUARANTINE` | `21_LICENSE_ATTRIBUTION\license_risk_reviews\knowledge_scrape_quarantine\07_usb_c_high_speed_esd` | `usb_c_esd_reference` | `MEDIUM` |
| `07_usb_c_high_speed_esd\.gitkeep` | `MOVE_AS_HISTORY_ONLY` | `02_HISTORY\knowledge_scrape_migration\engineering_metadata\07_usb_c_high_speed_esd` | `engineering_metadata` | `LOW` |
| `07_usb_c_high_speed_esd\_CATEGORY_INDEX.md` | `MOVE_AS_HISTORY_ONLY` | `02_HISTORY\knowledge_scrape_migration\engineering_metadata\07_usb_c_high_speed_esd` | `engineering_metadata` | `LOW` |
| `08_power_buck_regulators\` | `MOVE_TO_LICENSE_QUARANTINE` | `21_LICENSE_ATTRIBUTION\license_risk_reviews\knowledge_scrape_quarantine\08_power_buck_regulators` | `buck_regulator_reference` | `MEDIUM` |
| `08_power_buck_regulators\.gitkeep` | `MOVE_AS_HISTORY_ONLY` | `02_HISTORY\knowledge_scrape_migration\engineering_metadata\08_power_buck_regulators` | `engineering_metadata` | `LOW` |
| `08_power_buck_regulators\_CATEGORY_INDEX.md` | `MOVE_AS_HISTORY_ONLY` | `02_HISTORY\knowledge_scrape_migration\engineering_metadata\08_power_buck_regulators` | `engineering_metadata` | `LOW` |
| `09_pcb_layout_grounding_emi_si\` | `MOVE_TO_LICENSE_QUARANTINE` | `21_LICENSE_ATTRIBUTION\license_risk_reviews\knowledge_scrape_quarantine\09_pcb_layout_grounding_emi_si` | `pcb_layout_emi_si_rules` | `MEDIUM` |
| `09_pcb_layout_grounding_emi_si\.gitkeep` | `MOVE_AS_HISTORY_ONLY` | `02_HISTORY\knowledge_scrape_migration\engineering_metadata\09_pcb_layout_grounding_emi_si` | `engineering_metadata` | `LOW` |
| `09_pcb_layout_grounding_emi_si\_CATEGORY_INDEX.md` | `MOVE_AS_HISTORY_ONLY` | `02_HISTORY\knowledge_scrape_migration\engineering_metadata\09_pcb_layout_grounding_emi_si` | `engineering_metadata` | `LOW` |
| `10_dfm_fabrication_assembly\` | `MOVE_TO_LICENSE_QUARANTINE` | `21_LICENSE_ATTRIBUTION\license_risk_reviews\knowledge_scrape_quarantine\10_dfm_fabrication_assembly` | `dfm_fabrication_reference_capture` | `MEDIUM` |
| `10_dfm_fabrication_assembly\.gitkeep` | `MOVE_AS_HISTORY_ONLY` | `02_HISTORY\knowledge_scrape_migration\fab_dfm_compliance_metadata\10_dfm_fabrication_assembly` | `fab_dfm_compliance_metadata` | `LOW` |
| `10_dfm_fabrication_assembly\_CATEGORY_INDEX.md` | `MOVE_AS_HISTORY_ONLY` | `02_HISTORY\knowledge_scrape_migration\fab_dfm_compliance_metadata\10_dfm_fabrication_assembly` | `fab_dfm_compliance_metadata` | `LOW` |
| `11_calculators_ipc_reference\` | `MOVE_TO_LICENSE_QUARANTINE` | `21_LICENSE_ATTRIBUTION\license_risk_reviews\knowledge_scrape_quarantine\11_calculators_ipc_reference` | `calculator_reference_capture` | `MEDIUM` |
| `11_calculators_ipc_reference\.gitkeep` | `MOVE_AS_HISTORY_ONLY` | `02_HISTORY\knowledge_scrape_migration\calculator_metadata\11_calculators_ipc_reference` | `calculator_metadata` | `LOW` |
| `11_calculators_ipc_reference\_CATEGORY_INDEX.md` | `MOVE_AS_HISTORY_ONLY` | `02_HISTORY\knowledge_scrape_migration\calculator_metadata\11_calculators_ipc_reference` | `calculator_metadata` | `LOW` |
| `12_forums_peer_review\` | `MOVE_TO_LICENSE_QUARANTINE` | `21_LICENSE_ATTRIBUTION\license_risk_reviews\knowledge_scrape_quarantine\12_forums_peer_review` | `forums_peer_review_raw_capture` | `HIGH` |
| `12_forums_peer_review\.gitkeep` | `MOVE_AS_HISTORY_ONLY` | `02_HISTORY\knowledge_scrape_migration\case_study_training_metadata\12_forums_peer_review` | `case_study_training_metadata` | `LOW` |
| `12_forums_peer_review\_CATEGORY_INDEX.md` | `MOVE_AS_HISTORY_ONLY` | `02_HISTORY\knowledge_scrape_migration\case_study_training_metadata\12_forums_peer_review` | `case_study_training_metadata` | `LOW` |
| `13_vendor_parts_cad_models\` | `MOVE_TO_LICENSE_QUARANTINE` | `21_LICENSE_ATTRIBUTION\license_risk_reviews\knowledge_scrape_quarantine\13_vendor_parts_cad_models` | `vendor_cad_reference_capture` | `MEDIUM` |
| `13_vendor_parts_cad_models\.gitkeep` | `MOVE_AS_HISTORY_ONLY` | `02_HISTORY\knowledge_scrape_migration\component_datasheet_metadata\13_vendor_parts_cad_models` | `component_datasheet_metadata` | `LOW` |
| `13_vendor_parts_cad_models\_CATEGORY_INDEX.md` | `MOVE_AS_HISTORY_ONLY` | `02_HISTORY\knowledge_scrape_migration\component_datasheet_metadata\13_vendor_parts_cad_models` | `component_datasheet_metadata` | `LOW` |
| `14_datasheets_pdf_markdown\_CATEGORY_INDEX.md` | `MOVE_AS_HISTORY_ONLY` | `02_HISTORY\knowledge_scrape_migration\component_datasheet_metadata\14_datasheets_pdf_markdown` | `component_datasheet_metadata` | `LOW` |
| `14_datasheets_pdf_markdown\extracted_markdown\` | `MOVE_TO_LICENSE_QUARANTINE` | `21_LICENSE_ATTRIBUTION\license_risk_reviews\knowledge_scrape_quarantine\14_datasheets_pdf_markdown\extracted_markdown` | `extracted_datasheet_markdown` | `HIGH` |
| `14_datasheets_pdf_markdown\extraction_logs\` | `MOVE_AS_HISTORY_ONLY` | `02_HISTORY\knowledge_scrape_migration\datasheet_extraction_logs\14_datasheets_pdf_markdown` | `datasheet_extraction_logs` | `LOW` |
| `14_datasheets_pdf_markdown\original_pdf\` | `MOVE_TO_LICENSE_QUARANTINE` | `21_LICENSE_ATTRIBUTION\license_risk_reviews\knowledge_scrape_quarantine\14_datasheets_pdf_markdown\original_pdf` | `original_datasheet_pdf` | `HIGH` |
| `14_datasheets_pdf_markdown\PDF_INDEX.csv` | `MOVE_AS_HISTORY_ONLY` | `02_HISTORY\knowledge_scrape_migration\component_datasheet_metadata\14_datasheets_pdf_markdown` | `datasheet_index_metadata` | `LOW` |
| `14_datasheets_pdf_markdown\PDF_INDEX.md` | `MOVE_AS_HISTORY_ONLY` | `02_HISTORY\knowledge_scrape_migration\component_datasheet_metadata\14_datasheets_pdf_markdown` | `datasheet_index_metadata` | `LOW` |
| `15_video_reference_index\` | `MOVE_TO_LICENSE_QUARANTINE` | `21_LICENSE_ATTRIBUTION\license_risk_reviews\knowledge_scrape_quarantine\15_video_reference_index` | `video_reference_capture` | `HIGH` |
| `15_video_reference_index\.gitkeep` | `MOVE_AS_HISTORY_ONLY` | `02_HISTORY\knowledge_scrape_migration\case_study_training_metadata\15_video_reference_index` | `case_study_training_metadata` | `LOW` |
| `15_video_reference_index\_CATEGORY_INDEX.md` | `MOVE_AS_HISTORY_ONLY` | `02_HISTORY\knowledge_scrape_migration\case_study_training_metadata\15_video_reference_index` | `case_study_training_metadata` | `LOW` |
| `16_ai_pcb_failure_modes\` | `MOVE_TO_LICENSE_QUARANTINE` | `21_LICENSE_ATTRIBUTION\license_risk_reviews\knowledge_scrape_quarantine\16_ai_pcb_failure_modes` | `ai_failure_mode_reference_capture` | `MEDIUM` |
| `16_ai_pcb_failure_modes\.gitkeep` | `MOVE_AS_HISTORY_ONLY` | `02_HISTORY\knowledge_scrape_migration\case_study_training_metadata\16_ai_pcb_failure_modes` | `case_study_training_metadata` | `LOW` |
| `16_ai_pcb_failure_modes\_CATEGORY_INDEX.md` | `MOVE_AS_HISTORY_ONLY` | `02_HISTORY\knowledge_scrape_migration\case_study_training_metadata\16_ai_pcb_failure_modes` | `case_study_training_metadata` | `LOW` |
| `17_case_studies_bad_boards\` | `MOVE_TO_LICENSE_QUARANTINE` | `21_LICENSE_ATTRIBUTION\license_risk_reviews\knowledge_scrape_quarantine\17_case_studies_bad_boards` | `bad_board_case_study_capture` | `MEDIUM` |
| `17_case_studies_bad_boards\.gitkeep` | `MOVE_AS_HISTORY_ONLY` | `02_HISTORY\knowledge_scrape_migration\case_study_training_metadata\17_case_studies_bad_boards` | `case_study_training_metadata` | `LOW` |
| `17_case_studies_bad_boards\_CATEGORY_INDEX.md` | `MOVE_AS_HISTORY_ONLY` | `02_HISTORY\knowledge_scrape_migration\case_study_training_metadata\17_case_studies_bad_boards` | `case_study_training_metadata` | `LOW` |
| `18_case_studies_good_boards\` | `MOVE_TO_LICENSE_QUARANTINE` | `21_LICENSE_ATTRIBUTION\license_risk_reviews\knowledge_scrape_quarantine\18_case_studies_good_boards` | `good_board_case_study_capture` | `MEDIUM` |
| `18_case_studies_good_boards\.gitkeep` | `MOVE_AS_HISTORY_ONLY` | `02_HISTORY\knowledge_scrape_migration\case_study_training_metadata\18_case_studies_good_boards` | `case_study_training_metadata` | `LOW` |
| `18_case_studies_good_boards\_CATEGORY_INDEX.md` | `MOVE_AS_HISTORY_ONLY` | `02_HISTORY\knowledge_scrape_migration\case_study_training_metadata\18_case_studies_good_boards` | `case_study_training_metadata` | `LOW` |
| `19_university_training\` | `MOVE_TO_LICENSE_QUARANTINE` | `21_LICENSE_ATTRIBUTION\license_risk_reviews\knowledge_scrape_quarantine\19_university_training` | `university_training_capture` | `HIGH` |
| `19_university_training\.gitkeep` | `MOVE_AS_HISTORY_ONLY` | `02_HISTORY\knowledge_scrape_migration\case_study_training_metadata\19_university_training` | `case_study_training_metadata` | `LOW` |
| `19_university_training\_CATEGORY_INDEX.md` | `MOVE_AS_HISTORY_ONLY` | `02_HISTORY\knowledge_scrape_migration\case_study_training_metadata\19_university_training` | `case_study_training_metadata` | `LOW` |
| `20_manufacturer_layout_guides\` | `MOVE_AS_HISTORY_ONLY` | `02_HISTORY\knowledge_scrape_migration\engineering_metadata\20_manufacturer_layout_guides` | `engineering_metadata` | `LOW` |
| `21_component_package_land_patterns\` | `MOVE_TO_LICENSE_QUARANTINE` | `21_LICENSE_ATTRIBUTION\license_risk_reviews\knowledge_scrape_quarantine\21_component_package_land_patterns` | `land_pattern_reference_capture` | `MEDIUM` |
| `21_component_package_land_patterns\_CATEGORY_INDEX.md` | `MOVE_AS_HISTORY_ONLY` | `02_HISTORY\knowledge_scrape_migration\component_datasheet_metadata\21_component_package_land_patterns` | `component_datasheet_metadata` | `LOW` |
| `22_automotive_harsh_environment\` | `MOVE_TO_LICENSE_QUARANTINE` | `21_LICENSE_ATTRIBUTION\license_risk_reviews\knowledge_scrape_quarantine\22_automotive_harsh_environment` | `harsh_environment_reference_capture` | `MEDIUM` |
| `22_automotive_harsh_environment\_CATEGORY_INDEX.md` | `MOVE_AS_HISTORY_ONLY` | `02_HISTORY\knowledge_scrape_migration\fab_dfm_compliance_metadata\22_automotive_harsh_environment` | `fab_dfm_compliance_metadata` | `LOW` |
| `23_rf_wifi_antenna_layout\` | `MOVE_AS_HISTORY_ONLY` | `02_HISTORY\knowledge_scrape_migration\engineering_metadata\23_rf_wifi_antenna_layout` | `engineering_metadata` | `LOW` |
| `24_power_integrity_decoupling\` | `MOVE_AS_HISTORY_ONLY` | `02_HISTORY\knowledge_scrape_migration\engineering_metadata\24_power_integrity_decoupling` | `engineering_metadata` | `LOW` |
| `25_signal_integrity_high_speed\` | `MOVE_AS_HISTORY_ONLY` | `02_HISTORY\knowledge_scrape_migration\engineering_metadata\25_signal_integrity_high_speed` | `engineering_metadata` | `LOW` |
| `26_thermal_mechanical_enclosure\` | `MOVE_AS_HISTORY_ONLY` | `02_HISTORY\knowledge_scrape_migration\engineering_metadata\26_thermal_mechanical_enclosure` | `engineering_metadata` | `LOW` |
| `27_test_debug_validation\` | `MOVE_AS_HISTORY_ONLY` | `02_HISTORY\knowledge_scrape_migration\engineering_metadata\27_test_debug_validation` | `engineering_metadata` | `LOW` |
| `28_high_reliability_aerospace_workmanship\` | `MOVE_TO_LICENSE_QUARANTINE` | `21_LICENSE_ATTRIBUTION\license_risk_reviews\knowledge_scrape_quarantine\28_high_reliability_aerospace_workmanship` | `high_reliability_reference_capture` | `MEDIUM` |
| `28_high_reliability_aerospace_workmanship\_CATEGORY_INDEX.md` | `MOVE_AS_HISTORY_ONLY` | `02_HISTORY\knowledge_scrape_migration\fab_dfm_compliance_metadata\28_high_reliability_aerospace_workmanship` | `fab_dfm_compliance_metadata` | `LOW` |
| `29_standards_ipc_ul_safety\` | `MOVE_TO_LICENSE_QUARANTINE` | `21_LICENSE_ATTRIBUTION\license_risk_reviews\knowledge_scrape_quarantine\29_standards_ipc_ul_safety` | `standards_ipc_ul_safety_capture` | `HIGH` |
| `29_standards_ipc_ul_safety\_CATEGORY_INDEX.md` | `MOVE_AS_HISTORY_ONLY` | `02_HISTORY\knowledge_scrape_migration\fab_dfm_compliance_metadata\29_standards_ipc_ul_safety` | `fab_dfm_compliance_metadata` | `LOW` |
| `30_eda_automation_verification\` | `MOVE_AS_HISTORY_ONLY` | `02_HISTORY\knowledge_scrape_migration\automation_metadata\30_eda_automation_verification` | `automation_metadata` | `LOW` |
| `30_eda_automation_verification\_CATEGORY_INDEX.md` | `MOVE_AS_HISTORY_ONLY` | `02_HISTORY\knowledge_scrape_migration\automation_metadata\30_eda_automation_verification` | `automation_metadata` | `LOW` |
| `31_compliance_safety_emc\` | `MOVE_TO_LICENSE_QUARANTINE` | `21_LICENSE_ATTRIBUTION\license_risk_reviews\knowledge_scrape_quarantine\31_compliance_safety_emc` | `compliance_emc_reference_capture` | `MEDIUM` |
| `31_compliance_safety_emc\_CATEGORY_INDEX.md` | `MOVE_AS_HISTORY_ONLY` | `02_HISTORY\knowledge_scrape_migration\fab_dfm_compliance_metadata\31_compliance_safety_emc` | `fab_dfm_compliance_metadata` | `LOW` |
| `90_unsorted_review\` | `NEEDS_HUMAN_REVIEW` | `21_LICENSE_ATTRIBUTION\license_risk_reviews\knowledge_scrape_quarantine\90_unsorted_review` | `unsorted_review_capture` | `UNCLEAR` |
| `90_unsorted_review\.gitkeep` | `MOVE_AS_HISTORY_ONLY` | `02_HISTORY\knowledge_scrape_migration\unsorted_review\90_unsorted_review` | `unsorted_review_metadata` | `LOW` |
| `90_unsorted_review\_CATEGORY_INDEX.md` | `MOVE_AS_HISTORY_ONLY` | `02_HISTORY\knowledge_scrape_migration\unsorted_review\90_unsorted_review` | `unsorted_review_metadata` | `LOW` |
| `91_rejected_low_value\` | `MOVE_TO_LICENSE_QUARANTINE` | `21_LICENSE_ATTRIBUTION\license_risk_reviews\knowledge_scrape_quarantine\91_rejected_low_value` | `rejected_low_value_capture` | `HIGH` |
| `91_rejected_low_value\.gitkeep` | `MOVE_AS_HISTORY_ONLY` | `02_HISTORY\knowledge_scrape_migration\rejected_low_value\91_rejected_low_value` | `rejected_low_value_metadata` | `LOW` |
| `91_rejected_low_value\_CATEGORY_INDEX.md` | `MOVE_AS_HISTORY_ONLY` | `02_HISTORY\knowledge_scrape_migration\rejected_low_value\91_rejected_low_value` | `rejected_low_value_metadata` | `LOW` |
| `99_source_logs\` | `MOVE_AS_HISTORY_ONLY` | `02_HISTORY\knowledge_scrape_migration\source_logs` | `source_logs` | `LOW` |
| `_logs\` | `MOVE_AS_HISTORY_ONLY` | `02_HISTORY\knowledge_scrape_migration\original_metadata\_logs` | `migration_logs` | `LOW` |
| `_raw_inventory\` | `MOVE_AS_HISTORY_ONLY` | `02_HISTORY\knowledge_scrape_migration\original_metadata\_raw_inventory` | `raw_inventory` | `LOW` |
| `_scripts\` | `MOVE_AS_HISTORY_ONLY` | `02_HISTORY\knowledge_scrape_migration\obsolete_scripts` | `legacy_tooling_obsolete` | `LOW` |
| `_source_registry\` | `MOVE_AS_HISTORY_ONLY` | `02_HISTORY\knowledge_scrape_migration\original_metadata\_source_registry` | `source_registry` | `LOW` |

## Default

- Action: `NEEDS_HUMAN_REVIEW`
- Destination root: `02_HISTORY\knowledge_scrape_review_queue`
- Category: `unclassified`
- License risk: `UNCLEAR`

## Canonical Area Coverage

- `00_CODEX_START`
- `02_HISTORY`
- `03_TOOLS`
- `06_DATASHEETS`
- `07_REFERENCE_DESIGNS`
- `08_COMPONENT_DATABASE`
- `09_ACCURACY_ENGINE`
- `10_KNOWLEDGE_BASE`
- `11_LIBRARY_FACTORY`
- `12_REFERENCE_DESIGN_LIBRARY`
- `14_LAYOUT_AUTOMATION`
- `21_LICENSE_ATTRIBUTION`
- `24_FAB_PROFILES`
- `26_AGENT_QUALITY`

Compliance note: because `31_COMPLIANCE_SAFETY_EMC` is not present in
this repo, compliance/EMC/safety content is routed to
`10_KNOWLEDGE_BASE\compliance_emc_safety\knowledge_scrape_import`.
