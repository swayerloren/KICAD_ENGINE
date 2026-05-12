# Structure Improvement Report

Generated at: `2026-05-10T11:58:18-04:00`

## Summary

- Files recovered from `91_rejected_low_value`: `660`
- Files still in `91_rejected_low_value`: `686`
- Ambiguous files moved to `90_unsorted_review`: `0`
- Affected `_CATEGORY_INDEX.md` files rebuilt: `17`

## Recovered By Destination

| Destination Category | Recovered Files |
| --- | ---: |
| `01_kicad_core` | `3` |
| `02_kicad_python_api` | `14` |
| `04_kicad_libraries_symbols_footprints` | `587` |
| `05_esp32_espressif` | `14` |
| `07_usb_c_high_speed_esd` | `4` |
| `08_power_buck_regulators` | `11` |
| `10_dfm_fabrication_assembly` | `3` |
| `11_calculators_ipc_reference` | `1` |
| `12_forums_peer_review` | `14` |
| `13_vendor_parts_cad_models` | `1` |
| `15_video_reference_index` | `8` |

## Category Counts Before And After

| Category | Before | After |
| --- | ---: | ---: |
| `00_ai_entrypoints` | `10` | `10` |
| `00_source_of_truth` | `0` | `1` |
| `00_engineering_rules` | `0` | `6` |
| `00_retrieval_indexes` | `0` | `3` |
| `01_kicad_core` | `9` | `12` |
| `02_kicad_python_api` | `20` | `34` |
| `03_kicad_file_formats` | `4` | `4` |
| `04_kicad_libraries_symbols_footprints` | `4` | `591` |
| `05_esp32_espressif` | `86` | `100` |
| `06_microcontrollers` | `13` | `13` |
| `07_usb_c_high_speed_esd` | `22` | `26` |
| `08_power_buck_regulators` | `73` | `84` |
| `09_pcb_layout_grounding_emi_si` | `20` | `20` |
| `10_dfm_fabrication_assembly` | `11` | `14` |
| `11_calculators_ipc_reference` | `21` | `22` |
| `12_forums_peer_review` | `1` | `15` |
| `13_vendor_parts_cad_models` | `17` | `18` |
| `14_datasheets_pdf_markdown` | `104` | `103` |
| `15_video_reference_index` | `2` | `10` |
| `90_unsorted_review` | `0` | `0` |
| `91_rejected_low_value` | `1346` | `686` |
| `99_source_logs` | `0` | `0` |

## Newly Created Folders

- `00_source_of_truth/`
- `00_source_of_truth/official_datasheets/`
- `00_source_of_truth/official_app_notes/`
- `00_source_of_truth/kicad_official_docs/`
- `00_source_of_truth/fabricator_rules/`
- `00_engineering_rules/`
- `00_retrieval_indexes/`

## Newly Created Agent Files

- `AGENTS.md` updated with `knowledge_scrape` startup and trust rules
- `CLAUDE.md` created for the same workflow

## Remaining Concerns

- `91_rejected_low_value/` still holds a large number of generic forum shells, search pages, and blocked captures.
- Monolithic Power pages that scraped as blocked content remain rejected and need replacement from better captures if those sources become important.
- `EEVBlog` captures recovered here were mostly channel/index material, not real thread-level reviews; real thread captures are still missing.
- `496` linked URL rows are still marked `needs_rescrape`.
- `57` cleaned Markdown files still show raw HTML residue.
- `3` PDFs still failed extraction.
