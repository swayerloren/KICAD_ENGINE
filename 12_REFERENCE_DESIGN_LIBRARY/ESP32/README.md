# ESP32 Reference Designs

Use this folder for ESP32, ESP32-S2, ESP32-S3, ESP32-C3, ESP32-C6, ESP32-H2, ESP32-P4, ESP8266 legacy, and Espressif module reference design records.

## Preferred Sources

- Official Espressif hardware design guides.
- Official Espressif module datasheets.
- Official Espressif dev board schematics and layout notes.
- Open hardware ESP32 designs with clear licenses.

## What To Learn

- EN/reset circuit patterns.
- Boot strapping and programming circuits.
- USB/JTAG or UART programming approaches.
- 3.3 V power supply and decoupling.
- RF antenna keepout and module placement.
- Flash/PSRAM and module variant differences.

## What Not To Copy Blindly

- Module footprints without exact module drawing.
- Boot strap values without exact family verification.
- Antenna layout without stackup and keepout review.
- USB assumptions across ESP32 families.
- Dev-board circuits that include programmer/debug extras not needed on the target board.

