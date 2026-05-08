# Espressif Module Component Records

Date: 2026-05-02

Status: official-source researched component records for AI-assisted KiCad planning. These records are not design-approved until the exact module datasheet, exact KiCad symbol, exact footprint, and project requirements are verified together.

Common source set:

- Espressif technical documents: https://www.espressif.com/en/support/documents/technical-documents
- Espressif module product matrix: https://www.espressif.com/en/products/modules/esp32-s3-wroom-series
- Espressif KiCad library: https://github.com/espressif/kicad-libraries
- Espressif hardware design guidelines: https://docs.espressif.com/projects/esp-hardware-design-guidelines/en/latest/

Each record includes a source-evidence row. Values not directly supported by that row remain unknown, suffix-dependent, or verification-required for schematic/PCB use.

## Record Status Language

- `VERIFIED_FROM_DATASHEET`: The stated value is taken from an official Espressif datasheet or official product page listed in the record.
- `CANDIDATE_FROM_LOCAL_KICAD_NAME_SEARCH`: Candidate was found by read-only name search in installed KiCad 9 stock libraries. It is not pad-verified.
- `OFFICIAL_PCM_LIBRARY_FOLLOWUP`: Use the official Espressif KiCad library as a likely source, but verify after installation/use is approved.
- `UNKNOWN_REQUIRES_SOURCE_VERIFICATION`: The field remains unknown or exact-suffix-dependent.

## ESP32-WROOM-32

| Field | Value |
| --- | --- |
| Record ID | `ESPRESSIF_ESP32-WROOM-32` |
| Vendor | Espressif |
| Family | ESP32 |
| Category | `01_MICROCONTROLLERS` |
| Part status | Official datasheet reviewed; current HTML datasheet marks ESP32-WROOM-32 as NRND. |
| Verified features | ESP32-D0WDQ6 embedded; dual-core Xtensa LX6 up to 240 MHz; 802.11b/g/n Wi-Fi; Bluetooth v4.2 BR/EDR and Bluetooth LE; 4 MB SPI flash; 40 MHz crystal oscillator; onboard PCB antenna; operating voltage 3.0 to 3.6 V; ambient -40 to 85 C. |
| Source URL | https://documentation.espressif.com/esp32-wroom-32_datasheet_en.html |
| Source evidence | Official ESP32-WROOM-32 datasheet for lifecycle, features, electrical/module details, and recommended peripheral/reference circuitry; local KiCad 9 read-only name search for RF_Module candidates. |
| Datasheet local path | Link only; no PDF downloaded. |
| KiCad symbol candidates | `RF_Module:ESP32-WROOM-32` (`CANDIDATE_FROM_LOCAL_KICAD_NAME_SEARCH`) |
| KiCad footprint candidates | `RF_Module:ESP32-WROOM-32` (`CANDIDATE_FROM_LOCAL_KICAD_NAME_SEARCH`) |
| KiCad 3D model candidates | `RF_Module.3dshapes/ESP32-WROOM-32.step`, `RF_Module.3dshapes/ESP32-WROOM-32.wrl` (`CANDIDATE_FROM_LOCAL_KICAD_NAME_SEARCH`) |
| Module keepout notes | PCB antenna module; verify antenna keepout and module placement from datasheet and hardware design guidelines. |
| External parts needed | 3.3 V regulator/current budget, decoupling, EN/reset/boot circuitry, programming/debug path, ESD/protection for exposed interfaces. Exact values require project schematic verification. |
| Common schematic mistakes | Using NRND module for new designs without lifecycle review; weak 3.3 V rail; GPIO strap conflicts; assuming dev-board auto-reset circuitry exists on the module. |
| Layout warnings | Keep antenna area clear; verify KiCad footprint against datasheet; do not route under antenna keepout. |
| Recommended documents | ESP32-WROOM-32 datasheet; ESP32 hardware design guidelines; ESP32 series datasheet; official Espressif KiCad library. |

## ESP32-WROVER

| Field | Value |
| --- | --- |
| Record ID | `ESPRESSIF_ESP32-WROVER` |
| Vendor | Espressif |
| Family | ESP32 |
| Category | `01_MICROCONTROLLERS` |
| Part status | Generic WROVER-family record only. Exact suffix such as WROVER-B, WROVER-IB, WROVER-E, or WROVER-IE must be selected before schematic or footprint use. |
| Verified features | WROVER-family modules are ESP32-based modules with PSRAM variants. Product matrix entries for WROVER-IE show ESP32-D0WD-V3 / ESP32-D0WDRH2-V3, 18 x 31.4 x 3.3 mm, 24 GPIO, 4/8/16 MB flash options, 8 MB PSRAM, and IPEX antenna connector. These WROVER-IE values must not be applied to all WROVER variants without suffix verification. |
| Source URLs | https://documentation.espressif.com/esp32-wrover-b_datasheet_en.html ; https://www.espressif.com/en/products/modules/esp32-s3-wroom-series |
| Source evidence | Official WROVER-B datasheet plus Espressif module product matrix. This generic record cannot be placed until an exact WROVER suffix is selected and re-verified. |
| Datasheet local path | Link only; no PDF downloaded. |
| KiCad symbol candidates | No exact generic ESP32-WROVER stock KiCad 9 symbol found by quick name search; use official Espressif KiCad library follow-up. |
| KiCad footprint candidates | No exact generic ESP32-WROVER stock KiCad 9 footprint found by quick name search; do not substitute `ESP32-S2-WROVER` without verification. |
| KiCad 3D model candidates | Unknown - requires source verification. |
| Module keepout notes | WROVER modules may be PCB antenna or external antenna depending on suffix; verify before placement. |
| External parts needed | 3.3 V regulator/current budget, EN/reset/boot circuitry, programming/debug path, interface ESD/protection. |
| Common schematic mistakes | Placing a generic WROVER without suffix; using WROOM footprint; forgetting PSRAM-related variant differences; antenna type mismatch. |
| Layout warnings | WROVER packages are mechanically different from WROOM/MINI modules. Verify dimensions and land pattern from exact datasheet. |
| Recommended documents | Exact WROVER suffix datasheet; ESP32 hardware design guidelines; official Espressif KiCad library. |

## ESP32-S3-WROOM-1

| Field | Value |
| --- | --- |
| Record ID | `ESPRESSIF_ESP32-S3-WROOM-1` |
| Vendor | Espressif |
| Family | ESP32-S3 |
| Category | `01_MICROCONTROLLERS` |
| Part status | Official source reviewed; exact suffix still required for flash/PSRAM size. |
| Verified features | ESP32-S3 module family; Wi-Fi 802.11b/g/n; Bluetooth LE; Xtensa LX7 class S3 SoC; PCB antenna variant; operating voltage should be verified from exact datasheet before schematic freeze. |
| Source URL | https://documentation.espressif.com/esp32-s3-wroom-1_wroom-1u_datasheet_en.html |
| Source evidence | Official ESP32-S3-WROOM-1/WROOM-1U datasheet for module family, antenna variant, pinout, and land-pattern source; ESP32-S3 hardware design guidelines for strapping, USB, RF, and power rules; local KiCad 9 read-only name search for stock candidates. |
| Datasheet local path | Link only; no PDF downloaded. |
| KiCad symbol candidates | `RF_Module:ESP32-S3-WROOM-1` (`CANDIDATE_FROM_LOCAL_KICAD_NAME_SEARCH`) |
| KiCad footprint candidates | `RF_Module:ESP32-S3-WROOM-1` (`CANDIDATE_FROM_LOCAL_KICAD_NAME_SEARCH`) |
| KiCad 3D model candidates | `RF_Module.3dshapes/ESP32-S3-WROOM-1.step`, `RF_Module.3dshapes/ESP32-S3-WROOM-1.wrl` (`CANDIDATE_FROM_LOCAL_KICAD_NAME_SEARCH`) |
| Module keepout notes | PCB antenna module; apply S3 module antenna keepout and baseboard placement rules. |
| External parts needed | 3.3 V regulator/current budget, decoupling, EN/CHIP_PU reset, BOOT/GPIO0 access, USB or UART programming/debug path, USB-C CC/ESD if USB is exposed. |
| Common schematic mistakes | Ignoring GPIO0/GPIO45/GPIO46 strap behavior; loading GPIO19/GPIO20 while expecting native USB; assuming memory size without suffix. |
| Layout warnings | Keep RF clear; verify land pattern; place USB series resistor footprints near module/chip side if native USB is used. |
| Recommended documents | ESP32-S3-WROOM-1/WROOM-1U datasheet; ESP32-S3 hardware design guidelines; ESP-IDF S3 Wi-Fi docs; esp-csi if CSI is required. |

## ESP32-S3-WROOM-1U

| Field | Value |
| --- | --- |
| Record ID | `ESPRESSIF_ESP32-S3-WROOM-1U` |
| Vendor | Espressif |
| Family | ESP32-S3 |
| Category | `01_MICROCONTROLLERS` |
| Part status | Official source reviewed; exact suffix still required for flash/PSRAM size. |
| Verified features | ESP32-S3 module family; Wi-Fi 802.11b/g/n; Bluetooth LE; external antenna connector variant. |
| Source URL | https://documentation.espressif.com/esp32-s3-wroom-1_wroom-1u_datasheet_en.html |
| Source evidence | Official ESP32-S3-WROOM-1/WROOM-1U datasheet for external-antenna variant distinction, pinout, and land-pattern source; ESP32-S3 hardware design guidelines for RF/USB/strap rules; local KiCad 9 read-only name search for footprint candidate only. |
| Datasheet local path | Link only; no PDF downloaded. |
| KiCad symbol candidates | `RF_Module:ESP32-S3-WROOM-1` may be a pinout candidate only; exact symbol for U variant requires verification in official Espressif KiCad library. |
| KiCad footprint candidates | `RF_Module:ESP32-S3-WROOM-1U` (`CANDIDATE_FROM_LOCAL_KICAD_NAME_SEARCH`) |
| KiCad 3D model candidates | Unknown in installed KiCad 9 stock library by quick name search; use official Espressif KiCad library follow-up. |
| Module keepout notes | External antenna connector variant; no PCB antenna keepout equivalent, but connector, cable, antenna, enclosure, and RF path require review. |
| External parts needed | 3.3 V regulator/current budget, decoupling, EN/BOOT/reset, USB/UART debug path, antenna/cable/connector assembly, interface ESD/protection. |
| Common schematic mistakes | Treating U and non-U modules as only a BOM variant; forgetting RF connector/cable mechanics; using the PCB antenna footprint. |
| Layout warnings | Verify connector orientation and keep cable bend/mechanical constraints out of routing assumptions. |
| Recommended documents | ESP32-S3-WROOM-1/WROOM-1U datasheet; S3 hardware design guidelines; official Espressif KiCad library. |

## ESP32-S3-MINI-1

| Field | Value |
| --- | --- |
| Record ID | `ESPRESSIF_ESP32-S3-MINI-1` |
| Vendor | Espressif |
| Family | ESP32-S3 |
| Category | `01_MICROCONTROLLERS` |
| Part status | Official datasheet reviewed; exact suffix required for flash/PSRAM. |
| Verified features | S3 MINI family; Xtensa dual-core LX7 up to 240 MHz; 802.11b/g/n Wi-Fi; Bluetooth LE 5; 39 GPIOs; 65 module pins; integrated 40 MHz crystal; ESP32-S3-MINI-1 is PCB antenna; operating voltage 3.0 to 3.6 V; ambient -40 to 85 C. Variants include N8 and N4R2 flash/PSRAM options. |
| Source URL | https://documentation.espressif.com/esp32-s3-mini-1_mini-1u_datasheet_en.html |
| Source evidence | Official ESP32-S3-MINI-1/MINI-1U datasheet for pin count, GPIO count, supply range, temperature, antenna variants, memory suffixes, and land-pattern source; ESP32-S3 hardware design guidelines; local KiCad 9 name search exposing a suspect S2 footprint mapping that requires pad verification. |
| Datasheet local path | Link only; no PDF downloaded. |
| KiCad symbol candidates | `RF_Module:ESP32-S3-MINI-1` (`CANDIDATE_FROM_LOCAL_KICAD_NAME_SEARCH`) |
| KiCad footprint candidates | Installed KiCad 9 symbol points at `RF_Module:ESP32-S2-MINI-1`; treat as a shared/suspect candidate until verified against the S3 MINI datasheet. |
| KiCad 3D model candidates | Unknown in installed KiCad 9 stock library by quick name search; use official Espressif KiCad library follow-up. |
| Module keepout notes | PCB antenna MINI module; datasheet notes S3-MINI-1U has no antenna keepout zone in the same way as PCB antenna MINI. |
| External parts needed | 3.3 V regulator/current budget, decoupling, EN/BOOT/reset, USB/UART debug path, interface ESD/protection. |
| Common schematic mistakes | Using S2 MINI footprint without verification; using IO26 on N4R2 variants without checking PSRAM note; assuming N8 and N4R2 memory are interchangeable. |
| Layout warnings | Verify all 65 pins/pads, antenna keepout, and memory-suffix restrictions. |
| Recommended documents | ESP32-S3-MINI-1/MINI-1U datasheet; ESP32-S3 hardware design guidelines; official Espressif KiCad library. |

## ESP32-C3-MINI-1

| Field | Value |
| --- | --- |
| Record ID | `ESPRESSIF_ESP32-C3-MINI-1` |
| Vendor | Espressif |
| Family | ESP32-C3 |
| Category | `01_MICROCONTROLLERS` |
| Part status | Official datasheet reviewed; exact suffix required. |
| Verified features | ESP32-C3FH4 embedded variants; 32-bit RISC-V single-core up to 160 MHz; 4 MB flash in chip package; 15 GPIOs; 2.4 GHz Wi-Fi 802.11b/g/n; Bluetooth LE 5; PCB antenna variant; USB Serial/JTAG controller listed in datasheet; operating conditions require exact datasheet review before schematic freeze. |
| Source URL | https://documentation.espressif.com/esp32-c3-mini-1_datasheet_en.html |
| Source evidence | Official ESP32-C3-MINI-1 datasheet and ESP32-C3 series datasheet for C3 family/module features; local KiCad 9 name search found no exact bare-module stock symbol/footprint candidate. |
| Datasheet local path | Link only; no PDF downloaded. |
| KiCad symbol candidates | No exact `ESP32-C3-MINI-1` stock KiCad 9 symbol found by quick name search; official Espressif KiCad library follow-up required. Stock `RF_Module:ESP32-C3-DevKitM-1` is a dev-board symbol, not the module. |
| KiCad footprint candidates | No exact stock KiCad 9 footprint found by quick name search; official Espressif KiCad library follow-up required. |
| KiCad 3D model candidates | Unknown in installed KiCad 9 stock library by quick name search; use official Espressif KiCad library follow-up. |
| Module keepout notes | PCB antenna MINI module; verify C3 MINI land pattern and antenna placement. |
| External parts needed | 3.3 V regulator/current budget, EN/reset/boot circuitry, programming/debug path, interface ESD/protection. |
| Common schematic mistakes | Using a C3 dev-kit footprint for the module; assuming C3 and S3 MINI pinout compatibility; boot strap conflicts. |
| Layout warnings | Verify module dimensions, pad numbers, and antenna keepout from the C3 MINI datasheet. |
| Recommended documents | ESP32-C3-MINI-1/MINI-1U datasheet; ESP32-C3 datasheet; C3 hardware design guidelines; official Espressif KiCad library. |

## ESP32-C6-WROOM-1

| Field | Value |
| --- | --- |
| Record ID | `ESPRESSIF_ESP32-C6-WROOM-1` |
| Vendor | Espressif |
| Family | ESP32-C6 |
| Category | `01_MICROCONTROLLERS` |
| Part status | Official datasheet reviewed; exact suffix required. |
| Verified features | ESP32-C6-based WROOM module; 32-bit RISC-V single-core up to 160 MHz; Wi-Fi 6 2.4 GHz; Bluetooth LE 5.3; IEEE 802.15.4 with Thread and Zigbee support; 23 GPIOs; onboard PCB antenna; integrated 40 MHz crystal; operating voltage 3.0 to 3.6 V; ambient -40 to 85 C. |
| Source URL | https://documentation.espressif.com/esp32-c6-wroom-1_wroom-1u_datasheet_en.html |
| Source evidence | Official ESP32-C6-WROOM-1/WROOM-1U datasheet and ESP32-C6 series datasheet for module/family features; Espressif dev-kit documentation confirms C6 WROOM dev boards expose both USB Type-C native USB Serial/JTAG and USB-to-UART references; local KiCad 9 name search found no exact WROOM stock candidate. |
| Datasheet local path | Link only; no PDF downloaded. |
| KiCad symbol candidates | No exact `ESP32-C6-WROOM-1` stock KiCad 9 symbol found by quick name search; official Espressif KiCad library follow-up required. |
| KiCad footprint candidates | No exact stock KiCad 9 footprint found by quick name search; official Espressif KiCad library follow-up required. |
| KiCad 3D model candidates | Unknown in installed KiCad 9 stock library by quick name search; use official Espressif KiCad library follow-up. |
| Module keepout notes | PCB antenna WROOM module; verify C6 WROOM footprint and antenna keepout. |
| External parts needed | 3.3 V regulator/current budget, EN/reset/boot circuitry, USB Serial/JTAG or UART debug path, 802.15.4/Wi-Fi coexistence RF review, interface ESD/protection. |
| Common schematic mistakes | Assuming C6 WROOM is stock-KiCad-covered; ignoring GPIO12/GPIO13 USB Serial/JTAG use; treating Thread/Zigbee RF behavior as identical to S3 Wi-Fi-only layouts. |
| Layout warnings | C6 has Wi-Fi/BLE/802.15.4 sharing RF resources; keep antenna environment clean and verify final product RF behavior. |
| Recommended documents | ESP32-C6-WROOM-1/WROOM-1U datasheet; ESP32-C6 datasheet; C6 hardware design guidelines; ESP-IDF USB Serial/JTAG docs; official Espressif KiCad library. |

## ESP32-H2-MINI-1

| Field | Value |
| --- | --- |
| Record ID | `ESPRESSIF_ESP32-H2-MINI-1` |
| Vendor | Espressif |
| Family | ESP32-H2 |
| Category | `01_MICROCONTROLLERS` |
| Part status | Official datasheet reviewed; exact suffix required. |
| Verified features | BLE + IEEE 802.15.4 module; ESP32-H2 RISC-V single-core up to 96 MHz; 2 MB or 4 MB in-package flash; 19 GPIOs; integrated 32 MHz crystal; ESP32-H2-MINI-1 has PCB antenna; operating voltage 3.0 to 3.6 V; ambient -40 to 105 C. |
| Source URL | https://documentation.espressif.com/esp32-h2-mini-1_mini-1u_datasheet_en.html |
| Source evidence | Official ESP32-H2-MINI-1/MINI-1U datasheet and ESP32-H2 series datasheet for module/family features; Espressif H2 dev-kit documentation confirms BLE/IEEE 802.15.4 positioning and USB full-speed dev-board reference; local KiCad 9 name search found no exact stock candidate. |
| Datasheet local path | Link only; no PDF downloaded. |
| KiCad symbol candidates | No exact stock KiCad 9 symbol found by quick name search; official Espressif KiCad library follow-up required. |
| KiCad footprint candidates | No exact stock KiCad 9 footprint found by quick name search; official Espressif KiCad library follow-up required. |
| KiCad 3D model candidates | Unknown in installed KiCad 9 stock library by quick name search; use official Espressif KiCad library follow-up. |
| Module keepout notes | PCB antenna 802.15.4/BLE module; no Wi-Fi. Verify antenna keepout and Matter/Thread/Zigbee use case. |
| External parts needed | 3.3 V regulator/current budget, EN/reset/boot circuitry, USB Serial/JTAG or UART debug path, interface ESD/protection. |
| Common schematic mistakes | Selecting H2 for Wi-Fi or Wi-Fi CSI; assuming C3/C6 MINI firmware or pin use transfers directly; ignoring 802.15.4 antenna/product testing. |
| Layout warnings | RF still matters even without Wi-Fi; keep antenna clear and verify with the final enclosure. |
| Recommended documents | ESP32-H2-MINI-1/MINI-1U datasheet; ESP32-H2 datasheet; H2 hardware design guidelines; official Espressif KiCad library. |
