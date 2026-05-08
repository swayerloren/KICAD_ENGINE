# Reference Design Index

Status: `LINK_FIRST_INDEX`

This index tracks reference designs that may inform KiCad Engine schematic, PCB, component, layout, and manufacturing review work.

Reference designs are evidence sources, not automatic approval. Exact component values, pinouts, footprints, connector orientation, RF layout, power layout, and fab constraints still require source-specific verification.

## Allowed Verification Levels

- `VERIFIED`: Source URL, owner, license/redistribution status, design format, and relevant circuit lesson were checked against the cited source.
- `PARTIALLY_VERIFIED`: Some source facts are checked, but license, revision, circuit details, or transferability still require review.
- `LINK_ONLY`: Public link and summary are stored; local files are not copied.
- `UNVERIFIED`: Placeholder or candidate record. Do not use as design evidence.

## Index Columns

| Design Name | Category | Source URL | License | Format | Verification Level | Local Record | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Espressif ESP32-S3 Hardware Design Guidelines | ESP32 | https://docs.espressif.com/projects/esp-hardware-design-guidelines/en/latest/esp32s3/index.html | Official vendor documentation - redistribution requires review | Web documentation | LINK_ONLY | TBD | Use for ESP32-S3 minimum-system, strapping, RF, USB, and module-layout review questions; verify exact module datasheet separately. |
| STMicroelectronics STM32 Nucleo Boards Portal | STM32 | https://www.st.com/content/st_com/en/products/ecosystems/stm32-open-development-environment/stm32-nucleo.html | Official vendor portal - redistribution requires review | Web portal / board resources | LINK_ONLY | TBD | Use as a starting point for Nucleo schematic/package links; verify each board document separately. |
| Microchip Curiosity Development Boards Portal | PIC_AVR | https://www.microchip.com/en-us/tools-resources/evaluation-boards/curiosity | Official vendor portal - redistribution requires review | Web portal / board resources | LINK_ONLY | TBD | Use as a starting point for PIC/AVR dev-board references; verify each board schematic and license separately. |
| Raspberry Pi RP2040 Documentation Portal | PIC_AVR | https://www.raspberrypi.com/documentation/microcontrollers/rp2040.html | Official documentation - redistribution requires review | Web documentation | LINK_ONLY | TBD | Useful MCU-support reference even though RP2040 is not PIC/AVR; move to a dedicated MCU folder if added later. |
| Microchip MCP2562FD Product Page | CAN | https://www.microchip.com/en-us/product/MCP2562FD | Official vendor product page - redistribution requires review | Product page / datasheet link portal | LINK_ONLY | TBD | Use as CAN FD transceiver source entry point; verify datasheet values before design use. |
| Analog Devices AN-960 RS-485/RS-422 Guide | CAN | https://www.analog.com/en/resources/app-notes/an-960.html | Official vendor app note - redistribution requires review | Web app note | LINK_ONLY | TBD | Interface-design background only; not approval for any specific transceiver footprint or termination. |
| Analog Devices AN-1349 RS-485 EMC Guide | CAN | https://www.analog.com/en/resources/app-notes/an-1349.html | Official vendor app note - redistribution requires review | Web app note | LINK_ONLY | TBD | Use for EMC review questions; verify active design requirements separately. |
| TI TIDA-050072 USB-C PD PPS Power Reference Design | USB | https://www.ti.com/tool/TIDA-050072 | Official vendor reference design - redistribution requires review | Reference design portal | LINK_ONLY | TBD | USB-C power reference candidate; do not copy schematic/layout without license, exact part, and requirements review. |
| ATtiny85 Development Board | Small MCU sample | https://github.com/tomasr8/attiny85-dev-board | MIT, local attribution preserved | KiCad project | PARTIALLY_VERIFIED | `32_OPEN_KICAD_SAMPLE_INTAKE/review_reports/tomasr8_attiny85_dev_board_ENGINEERING_AUDIT.md` | Source/license/import are checked, but local ERC/DRC failed. Treat as `BROKEN_TEST_PROJECT`, not reference-grade evidence. |
| TPS5430 DC-DC Buck Converter Module | POWER | https://github.com/M4a1x/TPS5430 | CERN-OHL-S-2.0, local attribution preserved | KiCad project | PARTIALLY_VERIFIED | `32_OPEN_KICAD_SAMPLE_INTAKE/review_reports/m4a1x_tps5430_ENGINEERING_AUDIT.md` | Source/license/import are checked, but local ERC/DRC failed. Upstream JLCPCB/Gerber files are not KiCad Engine outputs. |
| ESP Rust Board | ESP32 / USB / POWER | https://github.com/esp-rs/esp-rust-board | CERN-OHL-P-2.0, local attribution preserved | KiCad project | PARTIALLY_VERIFIED | `32_OPEN_KICAD_SAMPLE_INTAKE/review_reports/esp_rs_esp_rust_board_ENGINEERING_AUDIT.md` | Source/license/import are checked, but local ERC/DRC failed. Treat as a complex failure/regression fixture until repaired and human-reviewed. |

## Category Folders

- `ESP32/`
- `STM32/`
- `PIC_AVR/`
- `POWER/`
- `USB/`
- `CAN/`
- `RF/`
- `AUTOMOTIVE/`

## Rules

- Add a record before relying on a reference design.
- Record license and redistribution status.
- Prefer link-only records unless file redistribution is confirmed.
- Do not copy layouts blindly.
- Do not treat a reference design as proof that a footprint or schematic is correct for another project.
- Promote a record to `VERIFIED` only after a human or agent records the exact source evidence, source date/revision, lesson extracted, and remaining review gates.
