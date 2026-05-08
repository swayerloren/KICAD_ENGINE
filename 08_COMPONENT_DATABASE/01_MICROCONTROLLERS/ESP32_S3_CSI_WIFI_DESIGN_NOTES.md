# ESP32-S3 CSI Wi-Fi Design Notes

Date: 2026-05-02

Status: research summary for AI-assisted KiCad planning. Exact schematic and PCB work still requires the selected ESP32-S3 module datasheet, hardware design guidelines, ESP-IDF version, and user requirements.

## Primary Sources

- ESP32-S3-WROOM-1 / WROOM-1U Datasheet: https://documentation.espressif.com/esp32-s3-wroom-1_wroom-1u_datasheet_en.html
- ESP32-S3-MINI-1 / MINI-1U Datasheet: https://documentation.espressif.com/esp32-s3-mini-1_mini-1u_datasheet_en.html
- ESP32-S3 Hardware Design Guidelines: https://docs.espressif.com/projects/esp-hardware-design-guidelines/en/latest/esp32s3/index.html
- ESP32-S3 Schematic Checklist: https://docs.espressif.com/projects/esp-hardware-design-guidelines/en/latest/esp32s3/schematic-checklist.html
- ESP32-S3 PCB Layout Design: https://docs.espressif.com/projects/esp-hardware-design-guidelines/en/latest/esp32s3/pcb-layout-design.html
- ESP-IDF ESP32-S3 Wi-Fi Driver Guide: https://docs.espressif.com/projects/esp-idf/en/v4.4.2/esp32s3/api-guides/wifi.html
- Official esp-csi repository: https://github.com/espressif/esp-csi

## What CSI Changes In Hardware Planning

Wi-Fi CSI is primarily a Wi-Fi driver and data-capture feature, but the board must be designed so the RF and power environment is stable and repeatable.

For KiCad planning, this means:

- Prefer an official ESP32-S3 module unless the user explicitly wants custom RF design.
- Choose PCB antenna versus external antenna intentionally.
- Keep the antenna placement and enclosure repeatable between test units.
- Avoid noisy buck regulators, LCD clocks, USB noise, and high-current switching near the RF section.
- Keep the module supply robust enough for Wi-Fi transmit peaks.
- Bring out a reliable logging/debug path so CSI data capture does not depend on fragile temporary wiring.
- Confirm ESP-IDF CSI support and target version before freezing hardware assumptions.

## Recommended Module Direction

| Module Direction | Use When | Hardware Notes |
| --- | --- | --- |
| ESP32-S3-WROOM-1 | General-purpose S3 Wi-Fi/BLE with PCB antenna. | Best default for first CSI boards if a PCB antenna is acceptable and board edge placement is possible. |
| ESP32-S3-WROOM-1U | External antenna is required. | Requires antenna connector, antenna cable, mechanical retention, enclosure review, and RF test plan. |
| ESP32-S3-MINI-1 | Smaller board area is important. | Verify 65-pin module footprint, memory suffix, and antenna keepout before use. |
| ESP32-S3-MINI-1U | Smaller module with external antenna. | Verify exact connector-side footprint and antenna mechanical design. |
| Bare ESP32-S3 chip | Only for advanced RF/custom layout work. | Requires crystal, RF matching, antenna, flash/PSRAM, and stricter layout validation. Not recommended as a first CSI board. |

## USB And Debug Choices

ESP32-S3 supports native USB functions, including USB Serial/JTAG. The S3 hardware guide maps USB D- to GPIO19 and D+ to GPIO20 and recommends resistor footprints near the chip/module side.

For a CSI node:

- Decide whether the board needs native USB, external USB-UART, both, or a programming header.
- If USB-C is used, include correct CC pull-downs for a device/UFP design, ESD protection, VBUS handling, and shield treatment.
- Do not load GPIO19/GPIO20 with other circuitry if native USB flashing, serial console, or USB/JTAG debugging is required.
- Keep a fallback UART boot/programming path if the firmware might disable USB Serial/JTAG behavior.

## Strapping And Boot Rules

ESP32-S3 strap pins include GPIO0, GPIO3, GPIO45, and GPIO46. GPIO0/GPIO46 are relevant to SPI boot and joint download boot. The hardware guide recommends a pull-up on GPIO0 and warns against adding high-value capacitors on GPIO0.

For a CSI node:

- Keep BOOT/GPIO0 accessible through a button, header, or proven auto-program circuit.
- Keep EN/CHIP_PU accessible for reset.
- Do not use strap pins for external connector signals without checking power-up levels.
- Do not place large capacitors or heavy loads on strap pins.
- Review GPIO45 and GPIO46 before using them for anything connected off-board.

## RF/Antenna Checklist

- Place PCB antenna modules at the board edge when possible.
- Keep the antenna region clear of copper, pours, traces, components, batteries, shields, and displays.
- If the antenna cannot extend beyond the baseboard, follow the Espressif layout guide clearance recommendations and record the reason.
- For external antennas, verify the exact U.FL/IPEX connector orientation, footprint, cable bend radius, and antenna mounting.
- Do not assume a dev-board antenna placement will work inside the final enclosure.
- Plan at least a practical throughput/range check for the assembled product.

## Power Checklist

- Budget for Wi-Fi transmit peaks, not only average current.
- Place bulk capacitance near the module supply entry and local decoupling near supply pins per the module/reference design.
- Keep switching regulators and inductors away from the RF/antenna side.
- If USB powers the board, confirm VBUS path, fuse/current limit, ESD, and regulator thermal behavior.
- Avoid long thin 3.3 V routes feeding the module.

## CSI Firmware And Data-Path Notes

ESP-IDF documents CSI enablement through Wi-Fi menuconfig, CSI callback registration, CSI config, and enabling CSI. The callback runs from the Wi-Fi task; long processing should be deferred to another task/queue.

Hardware implications:

- Provide enough flash/PSRAM for the intended firmware, buffering, and logging path.
- Decide whether CSI records go over USB CDC, UART, Wi-Fi, SD card, or another interface.
- If time alignment between nodes matters, define synchronization hardware early; do not assume generic ESP32-S3 boards are phase-coherent.
- Keep test pads or headers for debug access during RF/CSI bring-up.

## Avoid False Confidence

- A board that boots and sends Wi-Fi packets is not automatically a good CSI board.
- A stock KiCad footprint does not prove the antenna keepout is correct.
- A 3D model does not prove RF clearance.
- A dev board does not prove the same module placement will work in a custom enclosure.
- CSI support in software does not remove the need for RF verification.
