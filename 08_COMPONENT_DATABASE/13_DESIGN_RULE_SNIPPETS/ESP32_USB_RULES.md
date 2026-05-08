# ESP32 USB Rules

Date: 2026-05-02

Status: family-level USB guidance. Verify pin mapping and peripheral support for the exact ESP32 family and module.

Primary sources:

- https://docs.espressif.com/projects/esp-hardware-design-guidelines/en/latest/esp32s3/schematic-checklist.html
- https://docs.espressif.com/projects/esp-hardware-design-guidelines/en/latest/esp32s3/pcb-layout-design.html
- https://docs.espressif.com/projects/esp-idf/en/stable/esp32c6/api-guides/usb-serial-jtag-console.html
- https://docs.espressif.com/projects/esp-idf/en/stable/esp32c6/api-guides/jtag-debugging/configure-builtin-jtag.html

## ESP32-S3 Verified Notes

- ESP32-S3 has full-speed USB OTG with integrated transceivers and a USB Serial/JTAG controller.
- ESP32-S3 GPIO19 is USB D- and GPIO20 is USB D+ in Espressif's hardware guideline.
- Espressif recommends 22/33 ohm series resistor footprints between those pins and the USB connector, placed close to the chip/module side.
- Espressif's S3 layout guide recommends USB differential pairs routed in parallel with equal length and 90 ohm differential impedance within +/-10%.

## ESP32-C6 Verified Notes

- ESP32-C6 contains a USB Serial/JTAG controller.
- ESP-IDF documentation maps ESP32-C6 USB Serial/JTAG to GPIO12 D- and GPIO13 D+.
- ESP-IDF documentation notes USB Serial/JTAG can support serial console, flashing, and JTAG debugging.

## USB-C Device/UFP Checklist

- Add correct CC pull-down resistors for a USB-C device.
- Add USB ESD protection near the connector.
- Define VBUS sensing/power behavior.
- Decide shield-to-ground treatment.
- Route D+/D- as a controlled differential pair where required by the design.
- Keep stubs short and avoid unnecessary vias; add return vias if layer transitions are unavoidable.
- Do not share native USB pins with circuits that can disturb boot, flashing, serial console, or JTAG.

## Native USB Versus USB-UART

- Native USB can reduce BOM but can be affected by firmware, boot mode, drivers, and pin reuse.
- A USB-UART bridge is more traditional and can support auto-reset/boot circuits through DTR/RTS.
- Some boards may include both native USB and UART debug pads.
- Decide the programming and debug path before schematic capture, not after routing.

## KiCad Review Checks

- Are D+ and D- mapped to the correct pins for the exact chip/module?
- Are series resistor and ESD footprints present?
- Are USB-C CC resistors present and correctly tied for the device role?
- Is VBUS handled safely?
- Are USB pins free from conflicting GPIO assignments?
- Is a fallback boot/debug path available for early bring-up?
