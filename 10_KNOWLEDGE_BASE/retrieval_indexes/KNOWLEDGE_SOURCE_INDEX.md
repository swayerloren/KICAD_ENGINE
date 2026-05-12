# Knowledge Source Index

Status: `CANONICAL_SOURCE_REGISTRY_SUMMARY_POST_AI_ENTRYPOINT_TOOL_MOVE`

Generated: `2026-05-11`

## Registry Summary

- Source rows: `10236`
- Source domains in archived domain summary: `101`
- Manifest keys captured: `10`

## Scrape Status Counts

- `failed`: `7107`
- `not_found_in_outputs`: `1344`
- `success`: `1141`
- `needs_rescrape`: `424`
- `rejected`: `220`

## Top Knowledge Categories

- `06_microcontrollers`: `3925`
- `90_unsorted_review`: `1926`
- `12_forums_peer_review`: `1784`
- `01_kicad_core`: `962`
- `04_kicad_libraries_symbols_footprints`: `615`
- `13_vendor_parts_cad_models`: `257`
- `91_rejected_low_value`: `159`
- `15_video_reference_index`: `159`
- `19_university_training`: `139`
- `08_power_buck_regulators`: `83`
- `05_esp32_espressif`: `49`
- `10_dfm_fabrication_assembly`: `33`
- `18_case_studies_good_boards`: `31`
- `07_usb_c_high_speed_esd`: `28`
- `29_standards_ipc_ul_safety`: `22`
- `31_compliance_safety_emc`: `18`
- `02_kicad_python_api`: `12`
- `09_pcb_layout_grounding_emi_si`: `9`
- `11_calculators_ipc_reference`: `9`
- `16_ai_pcb_failure_modes`: `8`

## Top Domains

- `ww1.microchip.com`: `1254` URLs
- `www.st.com`: `1115` URLs
- `hackaday.com`: `1009` URLs
- `docs.kicad.org`: `977` URLs
- `www.microchip.com`: `911` URLs
- `forum.kicad.info`: `717` URLs
- `electronics.stackexchange.com`: `626` URLs
- `gitlab.com`: `600` URLs
- `www.eevblog.com`: `414` URLs
- `www.ti.com`: `394` URLs
- `example.com`: `276` URLs
- `www.nxp.com`: `216` URLs
- `www.digikey.com`: `212` URLs
- `forum.microchip.com`: `200` URLs
- `www.allaboutcircuits.com`: `200` URLs

## Original Metadata Archive

- Archived migration metadata and source logs live under `02_HISTORY/`.

## Notes

- Use `START_HERE_FOR_AI_AGENTS.md`, `00_CODEX_START/TASK_ROUTER.md`, and the
  `TASK_TYPE_TO_*_MAP.md` files for normal startup and routing.
- The old calculator scrape folder is now drained. Canonical calculator policy
  and first-pass tools now live under `10_KNOWLEDGE_BASE/calculators/` and
  `03_TOOLS/calculators/`.
- Automation-tool validation rules now live under `09_ACCURACY_ENGINE/` and
  apply to both first-party scripts and optional upstream tools.
- The original migration metadata/report/index files are no longer needed for normal agent lookup.
- Future metadata lookup should start here or in `10_KNOWLEDGE_BASE/source_registry/`.
- The 2026-05-11 component/datasheet/vendor move phase promoted canonical
  source-index surfaces under `06_DATASHEETS/`, `08_COMPONENT_DATABASE/`,
  `25_VENDOR_DATABASE/`, `29_FOOTPRINT_GAP_ANALYSIS/`, and
  `30_SUPPLIER_FOOTPRINT_MATCHES/`, while moving raw copied payloads to
  license quarantine.
- The 2026-05-11 fab/dfm/compliance move phase promoted canonical DFM,
  assembly, export, EMC, and link-only standards surfaces under
  `10_KNOWLEDGE_BASE/dfm_assembly/`,
  `10_KNOWLEDGE_BASE/compliance_emc_safety/`,
  `24_FAB_PROFILES/`, and `09_ACCURACY_ENGINE/`, while moving raw copied
  captures to license quarantine.
