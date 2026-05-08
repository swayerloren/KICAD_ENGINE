# Communication Component Research Status

Date: 2026-05-02

Task: Build a serious AI-readable database for common PCB communication interface parts.

## Completed

- Created `06_DATASHEETS/04_COMMUNICATION/COMMUNICATION_MASTER_INDEX.md`.
- Created `08_COMPONENT_DATABASE/03_COMMUNICATION/COMMUNICATION_COMPONENT_GUIDE.md`.
- Created `08_COMPONENT_DATABASE/03_COMMUNICATION/COMMUNICATION_PART_RECORDS.md`.
- Created `08_COMPONENT_DATABASE/03_COMMUNICATION/communication_part_records.json`.
- Created communication design-rule snippets:
  - `CAN_BUS_LAYOUT_RULES.md`
  - `USB_C_LAYOUT_RULES.md`
  - `RS485_LAYOUT_RULES.md`
  - `LEVEL_SHIFTING_RULES.md`
- Updated `06_DATASHEETS/04_COMMUNICATION/SOURCES.md`.
- Added communication records to `08_COMPONENT_DATABASE/00_INDEX/MASTER_COMPONENT_INDEX.md`.

## Researched Source Links

- Microchip MCP2562: https://www.microchip.com/en-us/product/MCP2562
- Microchip MCP2562FD: https://www.microchip.com/en-us/product/MCP2562FD
- Texas Instruments SN65HVD230: https://www.ti.com/product/SN65HVD230
- NXP TJA1051: https://www.nxp.com/docs/en/data-sheet/TJA1051.pdf
- NXP TJA1042: https://www.nxp.com/products/TJA1042
- Microchip MCP2003: https://www.microchip.com/en-us/product/MCP2003
- Analog Devices MAX3485: https://www.analog.com/en/products/max3485.html
- Texas Instruments SN65HVD75: https://www.ti.com/product/SN65HVD75
- Silicon Labs CP2102N: https://www.silabs.com/documents/public/data-sheets/cp2102n-datasheet.pdf
- FTDI FT232RL: https://ftdichip.com/products/ft232rl/
- STMicroelectronics USBLC6-2: https://www.st.com/en/protections-and-emi-filters/usblc6-2.html
- Texas Instruments TUSB320: https://www.ti.com/product/TUSB320
- WIZnet W5500: https://docs.wiznet.io/Product/Chip/Ethernet/W5500/datasheet
- Microchip LAN8720: https://ww1.microchip.com/downloads/aemDocuments/documents/UNG/ProductDocuments/DataSheets/LAN8720A-LAN8720Ai-Data-Sheet-DS00002165.pdf
- Texas Instruments PCA9306: https://www.ti.com/product/PCA9306
- Texas Instruments TXS0108E: https://www.ti.com/product/TXS0108E
- Texas Instruments TXB0108: https://www.ti.com/product/TXB0108

## Local KiCad Library Evidence

Read-only local KiCad 9 library searches found symbol candidates for:

- MCP2562 variants.
- SN65HVD230.
- TJA1051 variants.
- TJA1042 variants.
- MAX3485.
- CH340C.
- CP2102N package variants.
- FT232RL.
- USBLC6-2SC6 and related USBLC6 variants.
- TUSB320 and TUSB320I.
- W5500.
- LAN8720A.
- PCA9306 variants.
- TXS0108EPW.
- TXB0108 variants.

Exact local symbol candidates were not found in this pass for MCP2562FD, MCP2003, or SN65HVD75.

## Known Weaknesses

- CH340C official source link remains unresolved; do not promote it until WCH source is verified.
- No I2C expander part records have been added yet despite scope mention.
- No standalone SPI memory/device records have been added beyond W5500.
- Ethernet magnetics, MagJack, and RJ45 connector records are still missing.
- USB-C connector records are still separate from this pass.
- Package dimensions and exact footprints are not verified for active design use.

## Validation

- `08_COMPONENT_DATABASE/03_COMMUNICATION/communication_part_records.json` parsed successfully with 18 records.
- Requested deliverable files were present after creation.
- ASCII check passed for created and updated communication files.
- No protected KiCad design files under `04_KICAD_PROJECTS` were modified during this documentation task.
