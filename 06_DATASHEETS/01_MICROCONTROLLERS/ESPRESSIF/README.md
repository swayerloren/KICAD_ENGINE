# Espressif Datasheet And Reference Library

Date: 2026-05-02

Status: curated link-and-summary index. This folder is not a bundled PDF archive.

## Purpose

This folder stores Espressif source links, local summaries, missing-document trackers, and future user-approved datasheet copies for ESP32-family KiCad design work.

Primary use cases:

- Help Codex, Claude, and similar VS Code-based agents choose the correct ESP32 family or module.
- Keep official datasheet, hardware-design, errata, KiCad-library, reference-design, and ESP-IDF links close to component records.
- Prevent unsafe schematic and PCB assumptions around RF keepout, strapping pins, boot mode, USB/JTAG, EN/reset, flash/PSRAM, and antenna selection.
- Support local-first KiCad workflows without bundling copyrighted PDFs into a public repo by default.

## Covered Families

| Family | Role | KiCad Design Notes |
| --- | --- | --- |
| ESP32 | Legacy Wi-Fi + Bluetooth/BLE SoC and modules. | Many original ESP32 modules are NRND or have newer E/UE replacements; verify lifecycle before new designs. |
| ESP32-S2 | Wi-Fi MCU with native USB OTG, no Bluetooth. | Useful for USB + Wi-Fi designs, but verify module suffix and USB pin use. |
| ESP32-S3 | Wi-Fi + Bluetooth LE MCU with native USB, vector instructions, and common CSI use. | Good default for ESP32-S3-WROOM/MINI module-based designs when BLE and USB are needed. |
| ESP32-C2 / ESP8684 | Low-cost RISC-V Wi-Fi + Bluetooth LE family. | Often appears as ESP8684 modules; verify naming before selecting parts. |
| ESP32-C3 | RISC-V Wi-Fi + Bluetooth LE family. | Good small module option; verify USB Serial/JTAG and boot strapping. |
| ESP32-C5 | Wi-Fi 6-capable newer family. | Datasheet is active/current; verify module maturity and KiCad library support. |
| ESP32-C6 | Wi-Fi 6 + Bluetooth LE + Thread/Zigbee family. | Useful when 802.15.4 is required; verify USB/JTAG pins and module footprint. |
| ESP32-H2 | Bluetooth LE + IEEE 802.15.4, no Wi-Fi. | Do not select for Wi-Fi or Wi-Fi CSI. Pair with another Wi-Fi SoC for Matter border router/bridge designs. |
| ESP32-P4 | High-performance MCU with camera/display/USB/Ethernet-class peripherals, no integrated 2.4 GHz Wi-Fi radio. | Needs a separate radio module/SoC for Wi-Fi or BLE designs. |
| ESP8266 | Legacy Wi-Fi-only family. | NRND in current Espressif docs; prefer ESP32-C2/ESP8684 or newer ESP32 families for new designs unless compatibility requires ESP8266. |

## Primary Indexes

- `ESPRESSIF_MASTER_INDEX.md`: official source links, local status, and document priorities.
- `INDEX.md`: legacy scaffold index retained for compatibility.
- `SOURCES.md`: source-link ledger for future curation.
- `MISSING.md`: missing or unverified documents.

Related component database files:

- `08_COMPONENT_DATABASE\01_MICROCONTROLLERS\ESPRESSIF_ESP32_FAMILY.md`
- `08_COMPONENT_DATABASE\01_MICROCONTROLLERS\ESP32_S3_CSI_WIFI_DESIGN_NOTES.md`
- `08_COMPONENT_DATABASE\01_MICROCONTROLLERS\ESPRESSIF_MODULE_RECORDS.md`
- `08_COMPONENT_DATABASE\01_MICROCONTROLLERS\espressif_module_records.json`
- `08_COMPONENT_DATABASE\13_DESIGN_RULE_SNIPPETS\ESP32_LAYOUT_RULES.md`
- `08_COMPONENT_DATABASE\13_DESIGN_RULE_SNIPPETS\ESP32_STRAPPING_BOOT_RULES.md`
- `08_COMPONENT_DATABASE\13_DESIGN_RULE_SNIPPETS\ESP32_RF_ANTENNA_RULES.md`
- `08_COMPONENT_DATABASE\13_DESIGN_RULE_SNIPPETS\ESP32_USB_RULES.md`

## Agent Rules

- Prefer official Espressif documentation, official Espressif GitHub repositories, official dev-kit schematics, and the official Espressif KiCad library.
- Do not download datasheet PDFs unless the user explicitly approves a specific source and redistribution policy is recorded.
- Do not commit restricted PDFs to a public repo unless redistribution is clearly permitted.
- Store source links, access dates, and AI summaries first.
- Do not rely on distributor pinout images or random board pinout diagrams for schematic design.
- Do not assume WROOM, WROVER, MINI, U, E, IE, C, S, H, or P variants are footprint-compatible.
- Do not assume a stock KiCad footprint is correct until its pads, keepout, courtyard, and pin numbers are checked against the exact module datasheet.
- Treat every RF antenna keepout, USB differential pair, strapping pin, and EN/reset circuit as a design-rule item, not cosmetic metadata.
