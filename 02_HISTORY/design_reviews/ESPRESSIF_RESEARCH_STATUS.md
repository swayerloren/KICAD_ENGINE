# Espressif Research Status

Date: 2026-05-02

Workspace: `C:\Users\LJ\GitHub\KICAD_ENGINE`

## Scope Completed

Created or updated:

- `06_DATASHEETS\01_MICROCONTROLLERS\ESPRESSIF\README.md`
- `06_DATASHEETS\01_MICROCONTROLLERS\ESPRESSIF\ESPRESSIF_MASTER_INDEX.md`
- `08_COMPONENT_DATABASE\01_MICROCONTROLLERS\ESPRESSIF_ESP32_FAMILY.md`
- `08_COMPONENT_DATABASE\01_MICROCONTROLLERS\ESP32_S3_CSI_WIFI_DESIGN_NOTES.md`
- `08_COMPONENT_DATABASE\01_MICROCONTROLLERS\ESPRESSIF_MODULE_RECORDS.md`
- `08_COMPONENT_DATABASE\01_MICROCONTROLLERS\espressif_module_records.json`
- `08_COMPONENT_DATABASE\13_DESIGN_RULE_SNIPPETS\ESP32_LAYOUT_RULES.md`
- `08_COMPONENT_DATABASE\13_DESIGN_RULE_SNIPPETS\ESP32_STRAPPING_BOOT_RULES.md`
- `08_COMPONENT_DATABASE\13_DESIGN_RULE_SNIPPETS\ESP32_RF_ANTENNA_RULES.md`
- `08_COMPONENT_DATABASE\13_DESIGN_RULE_SNIPPETS\ESP32_USB_RULES.md`
- `08_COMPONENT_DATABASE\00_INDEX\MASTER_COMPONENT_INDEX.md`

No datasheet PDFs were downloaded. No KiCad project source files were edited.

Repeat prompt strengthening pass added official dev-board reference links, source-evidence rows in module records, JSON source-evidence URL arrays, and explicit P4/P4X/EOL distinction where relevant.

## Completed Families

| Family | Status | Notes |
| --- | --- | --- |
| ESP32 | PARTIAL_COMPLETE | Legacy ESP32/WROOM/WROVER guidance added. ESP32-WROOM-32 record includes NRND warning. WROVER remains suffix-dependent. |
| ESP32-S2 | PARTIAL_COMPLETE | Family guidance added, including Wi-Fi-only/native-USB positioning. No individual S2 module record was requested. |
| ESP32-S3 | STRONG_INITIAL_COMPLETE | S3 family, S3 WROOM/MINI records, USB/JTAG, strap, RF, and CSI notes added. |
| ESP32-C2 / ESP8684 | PARTIAL_COMPLETE | Family and source-index guidance added. ESP8684 module sources recorded, but no individual C2 module record was requested. |
| ESP32-C3 | PARTIAL_COMPLETE | C3 family and C3-MINI-1 record added. Official library footprint follow-up needed. |
| ESP32-C5 | PARTIAL_COMPLETE | C5 family guidance and source link added. Module maturity/library coverage still needs follow-up. |
| ESP32-C6 | PARTIAL_COMPLETE | C6 family and C6-WROOM-1 record added; USB Serial/JTAG and 802.15.4 notes included. |
| ESP32-H2 | PARTIAL_COMPLETE | H2 family and H2-MINI-1 record added with explicit no-Wi-Fi/no-CSI warning. |
| ESP32-P4 | PARTIAL_COMPLETE | P4 family guidance added with explicit no integrated Wi-Fi/BLE radio warning. |
| ESP8266 | PARTIAL_COMPLETE | Legacy status added; current official docs mark ESP8266EX NRND and recommend ESP8684 as upgraded model. |

## Module Records Created

- ESP32-WROOM-32
- ESP32-WROVER
- ESP32-S3-WROOM-1
- ESP32-S3-WROOM-1U
- ESP32-S3-MINI-1
- ESP32-C3-MINI-1
- ESP32-C6-WROOM-1
- ESP32-H2-MINI-1

## Missing Documents Or Follow-Up Sources

- Exact ESP32-WROVER suffix datasheets for WROVER-B, WROVER-IB, WROVER-E, and WROVER-IE should be reviewed separately before use.
- ESP32-C5 module datasheets and final module records need deeper review.
- Exact Espressif KiCad library symbol/footprint names from `espressif/kicad-libraries` should be inspected in a future approved tool/library review. The repository was only used as an official source link in this pass.
- Official dev board source links for ESP32-DevKitC V4, ESP32-S3-DevKitC-1, ESP32-S3-DevKitM-1, ESP32-C3-DevKitM-1, ESP8684-DevKitM-1, ESP32-C6-DevKitC-1, ESP32-C6-DevKitM-1, ESP32-H2-DevKitM-1, and ESP32-P4/P4X boards are now indexed. Schematic-level extraction and board-specific structured records remain future work.
- Errata documents for each selected chip family were not deeply extracted in this pass.
- ESP-IDF version-specific CSI behavior and known limitations need deeper software research before a CSI product design is frozen.

## Uncertain Specs

- ESP32-S3-WROOM-1 and ESP32-S3-WROOM-1U exact flash/PSRAM options remain suffix-dependent.
- ESP32-WROVER record is intentionally generic; exact electrical and mechanical values require exact suffix.
- ESP32-C6-WROOM-1 flash options and dev-board assumptions should be checked against the current datasheet, product matrix, and exact board revision before BOM selection.
- KiCad stock library candidates were found by name search only. They are not pad-verified, footprint-verified, or approved for use.
- External antenna connector orientation and footprint details for U variants are not verified.
- Peak RF current requirements were not normalized into records because they require exact part, mode, and datasheet table review.
- RF keepout geometry was summarized from hardware-design guidance, but exact keepout footprints were not generated.

## Risk Areas

- False footprint confidence from similar names such as WROOM/WROVER/MINI/S2/S3 shared footprints.
- Selecting ESP32-H2 or ESP32-P4 for Wi-Fi use because they still carry ESP32 branding.
- Treating U and non-U antenna variants as interchangeable.
- Using strap pins for LEDs, buttons, connectors, or level shifters without reset-state analysis.
- Relying on dev-board header pin labels instead of module pad numbers.
- Ignoring USB-C CC/ESD/VBUS requirements when using native USB.
- Bundling restricted datasheet PDFs into a public GitHub release.

## Next Research Needed

1. Inspect official Espressif KiCad library release metadata and symbol/footprint files, without installing unless approved.
2. Build exact records for ESP32-S3-WROOM-1-N8, ESP32-S3-WROOM-1-N16, and common PSRAM variants once exact target parts are chosen.
3. Add official dev-kit schematic summaries and separate them from module records.
4. Extract exact boot/strap tables for S3, C3, C6, H2, C2/ESP8684, and legacy ESP32 into machine-readable snippets.
5. Create module-footprint verification checklists for KiCad stock versus official Espressif PCM library.
6. Research ESP-IDF CSI examples, buffer requirements, and logging architecture for the planned ESP32-S3 CSI WiFi node.
7. Build a no-PDF public release source-link manifest for Espressif documents.
