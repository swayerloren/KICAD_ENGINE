# Espressif Master Source Index

Date: 2026-05-02

Status: link-first research index. No datasheets were downloaded during this research pass.

## Source Priority

1. Official Espressif documentation HTML pages and PDF landing pages.
2. Official Espressif hardware design guidelines.
3. Official Espressif ESP-IDF documentation.
4. Official Espressif GitHub repositories and reference designs.
5. Installed KiCad stock library read-only searches, marked only as candidates.
6. Distributor and community sources only as secondary discovery hints, not design authority.

## Official Source Links

| Topic | Source Type | Official URL | Local Copy | Verification Status | Notes |
| --- | --- | --- | --- | --- | --- |
| Espressif technical documents portal | Vendor portal | https://www.espressif.com/en/support/documents/technical-documents | Link only | SOURCE_LINK_RECORDED | Use this to confirm latest document version before relying on a local copy. |
| Espressif module product matrix | Vendor product portal | https://www.espressif.com/en/products/modules/esp32-s3-wroom-series | Link only | SOURCE_LINK_RECORDED | Product matrix covers many ESP32, ESP8684, ESP32-C/H/S/P modules with dimensions, GPIO count, flash/PSRAM, antenna, dev boards, and footprint links. |
| ESP32-WROOM-32 Datasheet | Module datasheet | https://documentation.espressif.com/esp32-wroom-32_datasheet_en.html | Link only | OFFICIAL_SOURCE_REVIEWED | Current HTML page marks ESP32-WROOM-32 as NRND. |
| ESP32-WROVER / WROVER-B family datasheet | Module datasheet | https://documentation.espressif.com/esp32-wrover-b_datasheet_en.html | Link only | SOURCE_LINK_RECORDED | Exact WROVER suffix must be verified before schematic/footprint use. |
| ESP32 Series Datasheet | SoC datasheet | https://documentation.espressif.com/esp32_datasheet_en.html | Link only | SOURCE_LINK_RECORDED | Needed for legacy ESP32 chip-level boot, strapping, flash, and peripheral details. |
| ESP32-S2 Series Datasheet | SoC datasheet | https://documentation.espressif.com/esp32-s2_datasheet_en.html | Link only | SOURCE_LINK_RECORDED | Needed for S2 Wi-Fi/USB-only designs. |
| ESP32-S3-WROOM-1 / WROOM-1U Datasheet | Module datasheet | https://documentation.espressif.com/esp32-s3-wroom-1_wroom-1u_datasheet_en.html | Link only | OFFICIAL_SOURCE_REVIEWED | Use for S3 WROOM pinout, peripheral schematic, module keepout, and land pattern. |
| ESP32-S3-MINI-1 / MINI-1U Datasheet | Module datasheet | https://documentation.espressif.com/esp32-s3-mini-1_mini-1u_datasheet_en.html | Link only | OFFICIAL_SOURCE_REVIEWED | Confirms S3 MINI variants, 65-pin module definition, flash/PSRAM options, and USB pins. |
| ESP32-C2 / ESP8684 SoC Datasheet | SoC datasheet | https://documentation.espressif.com/esp8684_datasheet_en.html | Link only | SOURCE_LINK_RECORDED | ESP32-C2 module naming often appears as ESP8684. |
| ESP8684-MINI-1 / MINI-1U Datasheet | Module datasheet | https://documentation.espressif.com/esp8684-mini-1_mini-1u_datasheet_en.html | Link only | OFFICIAL_SOURCE_REVIEWED | C2-class MINI module reference. |
| ESP32-C3 Series Datasheet | SoC datasheet | https://documentation.espressif.com/esp32-c3_datasheet_en.html | Link only | OFFICIAL_SOURCE_REVIEWED | Needed for C3 chip boot, GPIO restrictions, USB Serial/JTAG, and RF details. |
| ESP32-C3-MINI-1 / MINI-1U Datasheet | Module datasheet | https://documentation.espressif.com/esp32-c3-mini-1_datasheet_en.html | Link only | OFFICIAL_SOURCE_REVIEWED | Confirms C3 MINI module flash, GPIO count, antenna variants, and operating conditions. |
| ESP32-C5 Series Datasheet | SoC datasheet | https://documentation.espressif.com/esp32-c5_datasheet_en.html | Link only | OFFICIAL_SOURCE_REVIEWED | Current v1.1 document; C5 module/footprint support still needs follow-up. |
| ESP32-C6 Series Datasheet | SoC datasheet | https://documentation.espressif.com/esp32-c6_datasheet_en.html | Link only | SOURCE_LINK_RECORDED | Needed for C6 chip-level boot, USB Serial/JTAG, Wi-Fi 6, BLE, and 802.15.4. |
| ESP32-C6-WROOM-1 / WROOM-1U Datasheet | Module datasheet | https://documentation.espressif.com/esp32-c6-wroom-1_wroom-1u_datasheet_en.html | Link only | OFFICIAL_SOURCE_REVIEWED | Confirms C6 WROOM Wi-Fi 6/BLE/Thread/Zigbee features and module operating range. |
| ESP32-H2 Series Datasheet | SoC datasheet | https://documentation.espressif.com/esp32-h2_datasheet_en.html | Link only | SOURCE_LINK_RECORDED | H2 is BLE + IEEE 802.15.4, not Wi-Fi. |
| ESP32-H2-MINI-1 / MINI-1U Datasheet | Module datasheet | https://documentation.espressif.com/esp32-h2-mini-1_mini-1u_datasheet_en.html | Link only | OFFICIAL_SOURCE_REVIEWED | Confirms H2 MINI Bluetooth LE/802.15.4 role and no Wi-Fi. |
| ESP32-P4 Series Datasheet | SoC datasheet | https://documentation.espressif.com/esp32-p4_datasheet_en.html | Link only | OFFICIAL_SOURCE_REVIEWED | P4 is high-performance MCU; not an integrated Wi-Fi/BLE radio part. |
| ESP8266EX Datasheet | Legacy SoC datasheet | https://documentation.espressif.com/0a-esp8266ex_datasheet_en.html | Link only | OFFICIAL_SOURCE_REVIEWED | Current HTML page marks ESP8266EX NRND and recommends ESP8684 as upgraded model. |
| ESP32-S3 Hardware Design Guidelines | Hardware guide | https://docs.espressif.com/projects/esp-hardware-design-guidelines/en/latest/esp32s3/index.html | Link only | OFFICIAL_SOURCE_REVIEWED | Start here for S3 schematic, layout, boot, USB, and module placement rules. |
| ESP32-S3 Schematic Checklist | Hardware guide | https://docs.espressif.com/projects/esp-hardware-design-guidelines/en/latest/esp32s3/schematic-checklist.html | Link only | OFFICIAL_SOURCE_REVIEWED | Source for S3 strapping pins, EN/reset, flash/PSRAM notes, and USB recommendations. |
| ESP32-S3 PCB Layout Design | Hardware guide | https://docs.espressif.com/projects/esp-hardware-design-guidelines/en/latest/esp32s3/pcb-layout-design.html | Link only | OFFICIAL_SOURCE_REVIEWED | Source for RF/module placement, USB differential routing, SDIO routing, and RF verification. |
| ESP32 Hardware Design Guidelines | Hardware guide | https://docs.espressif.com/projects/esp-hardware-design-guidelines/en/latest/esp32/index.html | Link only | SOURCE_LINK_RECORDED | Needed for legacy ESP32/WROOM/WROVER designs. |
| ESP32-C3 Hardware Design Guidelines | Hardware guide | https://docs.espressif.com/projects/esp-hardware-design-guidelines/en/latest/esp32c3/index.html | Link only | SOURCE_LINK_RECORDED | Needed for C3 module/chip designs. |
| ESP32-C6 Hardware Design Guidelines | Hardware guide | https://docs.espressif.com/projects/esp-hardware-design-guidelines/en/latest/esp32c6/index.html | Link only | SOURCE_LINK_RECORDED | Needed for C6 Wi-Fi 6 + 802.15.4 designs. |
| ESP32-C2 / ESP8684 Hardware Design Guidelines | Hardware guide | https://documentation.espressif.com/esp-hardware-design-guidelines/en/latest/esp32c2/index.html | Link only | SOURCE_LINK_RECORDED | Needed for C2/ESP8684 low-cost designs. |
| ESP-IDF ESP32-S3 Wi-Fi Driver Guide | Software/reference guide | https://docs.espressif.com/projects/esp-idf/en/v4.4.2/esp32s3/api-guides/wifi.html | Link only | OFFICIAL_SOURCE_REVIEWED | Source for S3 Wi-Fi features and CSI enablement steps. |
| esp-csi | Official GitHub repository | https://github.com/espressif/esp-csi | Link only | OFFICIAL_SOURCE_REVIEWED | Official CSI application repository and supported-family reference. |
| Espressif KiCad Library | Official GitHub repository | https://github.com/espressif/kicad-libraries | Link only | OFFICIAL_SOURCE_REVIEWED | Official library for Espressif symbols, footprints, and 3D models. Do not assume installed in this repo. |

## Official Dev Board Reference Links

Dev boards are useful reference designs, but they are not drop-in custom PCB schematics. They include board-specific regulators, USB bridges, connectors, LEDs, jumpers, buttons, and routing choices.

| Board | Primary Module / Chip | Official URL | Use For | Do Not Use For |
| --- | --- | --- | --- | --- |
| ESP32-DevKitC V4 | ESP32-WROOM-32E / ESP32-WROOM-32UE variants | https://docs.espressif.com/projects/esp-dev-kits/en/latest/esp32/esp32-devkitc/user_guide.html | Legacy ESP32 USB-UART, power, boot/reset, and header reference. | Proving ESP32-WROOM-32 original NRND suitability. |
| ESP32-DevKitM-1 | ESP32-MINI-1 / MINI-1U | https://docs.espressif.com/projects/esp-dev-kits/en/latest/esp32/esp32-devkitm-1/user_guide.html | ESP32 MINI dev-board power/header patterns. | WROOM/WROVER footprint proof. |
| ESP32-S3-DevKitC-1 | ESP32-S3-WROOM-1 / WROOM-1U / WROOM-2 | https://docs.espressif.com/projects/esp-dev-kits/en/latest/esp32s3/esp32-s3-devkitc-1/index.html | S3 WROOM dev-board power, USB, boot/reset, and headers. | Direct module footprint proof without the module datasheet. |
| ESP32-S3-DevKitM-1 | ESP32-S3-MINI-1 | https://docs.espressif.com/projects/esp-idf/en/latest/esp32s3/hw-reference/esp32s3/user-guide-devkitm-1.html | S3 MINI dev-board wiring and USB/UART bring-up reference. | Assuming S3 WROOM and S3 MINI are mechanically interchangeable. |
| ESP32-C3-DevKitM-1 | ESP32-C3-MINI-1 | https://docs.espressif.com/projects/esp-dev-kits/en/latest/esp32c3/esp32-c3-devkitm-1/user_guide.html | C3 MINI power, reset, USB, UART, and header reference. | Using a dev-board KiCad symbol as the bare module symbol. |
| ESP8684-DevKitM-1 | ESP8684-MINI-1 / ESP32-C2 class | https://docs.espressif.com/projects/esp-dev-kits/en/latest/esp8684/esp8684-devkitm-1/user_guide.html | C2/ESP8684 module bring-up, low-cost Wi-Fi/BLE node reference. | Assuming C3/C6 pin compatibility. |
| ESP32-C6-DevKitC-1 | ESP32-C6-WROOM-1 / WROOM-1U | https://docs.espressif.com/projects/esp-dev-kits/en/latest/esp32c6/esp32-c6-devkitc-1/user_guide.html | C6 WROOM USB Type-C, USB Serial/JTAG, current-measurement jumper, and Thread/Zigbee/Wi-Fi reference. | Treating C6 WROOM as stock KiCad-covered without library verification. |
| ESP32-C6-DevKitM-1 | ESP32-C6-MINI-1 / MINI-1U | https://docs.espressif.com/projects/esp-dev-kits/en/latest/esp32c6/esp32-c6-devkitm-1/user_guide.html | C6 MINI dev-board reference. | C6 WROOM footprint proof. |
| ESP32-H2-DevKitM-1 | ESP32-H2-MINI-1 / MINI-1U | https://docs.espressif.com/projects/esp-dev-kits/en/latest/esp32h2/esp32-h2-devkitm-1/user_guide.html | H2 BLE/802.15.4 power, reset, current measurement, and header reference. | Any Wi-Fi or Wi-Fi CSI design. |
| ESP32-P4X-Function-EV-Board | ESP32-P4-class MCU plus companion radio architecture | https://docs.espressif.com/projects/esp-dev-kits/en/latest/esp32p4/esp32-p4x-function-ev-board/user_guide.html | Current P4X board family reference for multimedia, USB, camera/display, and companion-radio architecture. | Claiming ESP32-P4 has integrated Wi-Fi/BLE. |
| ESP32-P4-Function-EV-Board | ESP32-P4 plus ESP32-C6-MINI-1 radio module | https://docs.espressif.com/projects/esp-dev-kits/en/latest/esp32p4/esp32-p4-function-ev-board/user_guide.html | EOL P4 board reference for P4 as a high-performance MCU that needs a companion radio for Wi-Fi/BLE. | Starting a new design from an EOL board without checking the current P4X guide. |

## Local KiCad Candidate Search Notes

Read-only searches of the installed KiCad 9 stock libraries found candidate stock symbols/footprints for some modules, including `RF_Module:ESP32-WROOM-32`, `RF_Module:ESP32-S3-WROOM-1`, `RF_Module:ESP32-S3-MINI-1`, and `RF_Module:ESP32-C6-MINI-1`. Some requested modules such as ESP32-C6-WROOM-1, ESP32-H2-MINI-1, ESP32-C3-MINI-1, and generic ESP32-WROVER did not appear as exact stock KiCad 9 symbol/footprint candidates in this quick name search.

Use the official Espressif KiCad Library as the preferred future source for exact Espressif module footprints, but still perform pad-by-pad verification against the module datasheet before schematic or PCB use.

## Local File Policy

- Keep this folder link-first for public release.
- If a datasheet is later downloaded with user approval, store it under the correct family folder and record revision, source URL, access date, redistribution status, and checksum.
- If redistribution status is unknown, do not include the PDF in a public GitHub release.
