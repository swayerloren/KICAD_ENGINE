# ESP32 Strapping And Boot Rules

Date: 2026-05-02

Status: family-level rules. Exact strap pins differ by family and must be checked in the selected datasheet.

Primary sources:

- https://docs.espressif.com/projects/esp-hardware-design-guidelines/en/latest/esp32s3/schematic-checklist.html
- https://documentation.espressif.com/esp32-s3-mini-1_mini-1u_datasheet_en.html
- https://documentation.espressif.com/esp32-s3-wroom-1_wroom-1u_datasheet_en.html
- https://documentation.espressif.com/esp32-c6-wroom-1_wroom-1u_datasheet_en.html

## Core Rule

Strapping pins are sampled at reset or power-up. A pin that is safe after boot can still break boot if external circuitry forces the wrong state during the strap-sampling window.

## ESP32-S3 Verified Notes

- ESP32-S3 strapping pins include GPIO0, GPIO3, GPIO45, and GPIO46.
- ESP32-S3 boot mode is controlled by GPIO0 and GPIO46 for default SPI boot versus joint download boot in the hardware-design-guide boot table.
- Espressif recommends a pull-up resistor on GPIO0.
- Espressif warns not to add high-value capacitors on GPIO0 because this may cause unintended download-mode entry.
- EN/CHIP_PU must not float.

## Agent Checklist

- Identify every strapping pin in the selected chip/module datasheet.
- Record default internal pull state and required external pull state.
- Check every connected peripheral for power-up leakage, pull-ups, pull-downs, LEDs, level shifters, external connectors, and test fixtures.
- Keep BOOT and EN accessible during bring-up.
- Do not use strap pins as board-configuration inputs unless resistor values and reset timing are intentionally designed.
- Do not connect strap pins directly to off-board connectors without protection and boot-state analysis.
- Do not copy an ESP32-S3 strap rule to C3/C6/H2/C2 without checking that family's datasheet.

## KiCad Review Questions

- Does the schematic show explicit strap pin intent?
- Are BOOT and RESET/EN circuits present and labeled?
- Are DTR/RTS auto-program circuits correct for the selected USB-UART bridge or native USB path?
- Are strap pins hidden inside symbol units or buried in module labels?
- Are any strap pins reused for LEDs, buttons, or connector signals that can force boot failure?
