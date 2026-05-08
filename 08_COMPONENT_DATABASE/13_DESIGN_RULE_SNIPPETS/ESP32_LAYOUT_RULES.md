# ESP32 Layout Rules

Date: 2026-05-02

Status: family-level layout rules. Verify against the exact Espressif hardware design guide and module datasheet before PCB work.

Primary sources:

- https://docs.espressif.com/projects/esp-hardware-design-guidelines/en/latest/esp32s3/pcb-layout-design.html
- https://docs.espressif.com/projects/esp-hardware-design-guidelines/en/latest/esp32s3/schematic-checklist.html
- https://docs.espressif.com/projects/esp-hardware-design-guidelines/en/latest/

## Universal Module Rules

- Place PCB antenna modules at the board edge when possible.
- Keep module antenna regions clear of copper, routing, components, mounting hardware, batteries, shields, displays, and metal enclosure features.
- Do not route signals under the module antenna keepout.
- For ESP32-S3 PCB antenna module placement where the antenna cannot be outside the baseboard, Espressif recommends at least 15 mm antenna-area clearance in all directions.
- Treat U.FL/IPEX modules as RF connector designs, not as automatic layout simplifications.
- Keep switching regulators, inductors, fast clocks, display flex cables, and USB noise away from RF sections.
- Verify every castellated pad, exposed pad, ground pad, keepout, and paste recommendation against the exact module drawing.

## Power Integrity

- Route module 3.3 V as a low-impedance supply with local decoupling and nearby bulk capacitance.
- Budget for Wi-Fi transmit peaks.
- Use a regulator with enough transient current margin.
- Keep high-current loops short and away from the module antenna and RF side.
- Do not power an ESP32 RF module from an under-sized USB-UART regulator without a current budget.

## High-Speed And Digital Interfaces

- Keep UART boot/programming traces short and away from crystal/RF-sensitive areas where the hardware guide calls this out.
- For SDIO/SPI/flash/PSRAM-related signals, respect length, impedance, and pin-ownership notes in the family hardware guide.
- Do not use flash/PSRAM pins as GPIO unless the exact module suffix proves they are free.
- Add series resistor footprints where Espressif recommends or where signal-integrity bring-up risk is high.

## KiCad Implementation Checks

- Add explicit antenna keepout geometry on `Dwgs.User`, `Cmts.User`, or a documented keepout layer in addition to relying on footprint graphics.
- Confirm courtyard does not encourage other components into the RF clearance area.
- Compare pad numbers to the datasheet pin table, not only to symbol names.
- Check the 3D model only as mechanical context; it is not electrical or RF proof.
- Mark manufacturing outputs `NOT_FINAL` until RF placement and module-footprint review are complete.
