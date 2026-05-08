# Communication Master Index

Date: 2026-05-02

Status: link-first source index for common PCB communication interface parts. No datasheet PDFs were downloaded for this update.

## Purpose

This folder is the datasheet and source-index side of the communication component database. It records official source links and verification notes for CAN, CAN FD, LIN, RS485, USB, Ethernet, UART bridge, I2C/SPI helper, and level-shifting parts used in KiCad PCB designs.

Companion database files:

- `08_COMPONENT_DATABASE/03_COMMUNICATION/COMMUNICATION_COMPONENT_GUIDE.md`
- `08_COMPONENT_DATABASE/03_COMMUNICATION/COMMUNICATION_PART_RECORDS.md`
- `08_COMPONENT_DATABASE/03_COMMUNICATION/communication_part_records.json`
- `08_COMPONENT_DATABASE/13_DESIGN_RULE_SNIPPETS/CAN_BUS_LAYOUT_RULES.md`
- `08_COMPONENT_DATABASE/13_DESIGN_RULE_SNIPPETS/USB_C_LAYOUT_RULES.md`
- `08_COMPONENT_DATABASE/13_DESIGN_RULE_SNIPPETS/RS485_LAYOUT_RULES.md`
- `08_COMPONENT_DATABASE/13_DESIGN_RULE_SNIPPETS/LEVEL_SHIFTING_RULES.md`

## Agent Rules

- Do not assume a bus transceiver is correct because a familiar module or Arduino-style board uses it.
- Do not place a communication IC until voltage domain, package suffix, pinout, bus topology, termination, ESD, and external parts are verified.
- Treat KiCad symbols and footprints as candidates only until checked against the exact datasheet package drawing.
- Do not use interface parts outside their intended bus type. A CAN transceiver is not an RS485 transceiver, a USB ESD clamp is not bulk surge protection, and an auto-direction level shifter is not a universal translator.
- Public releases should store source links, metadata, and summaries. Do not bundle datasheet PDFs unless redistribution permission is confirmed.

## Interface Coverage

| Interface | Status | Current Starter Parts | Notes |
| --- | --- | --- | --- |
| CAN | PARTIAL | MCP2562, SN65HVD230, TJA1051, TJA1042 | Termination, common-mode, split termination, ESD, and connector pinout remain project-specific. |
| CAN FD | PARTIAL | MCP2562FD | Verify CAN FD timing, transceiver variant, and controller compatibility. |
| LIN | PARTIAL | MCP2003 | Automotive 12V/LIN bus behavior requires exact datasheet and protection review. |
| RS485 | PARTIAL | MAX3485, SN65HVD75 | Termination and fail-safe biasing must be designed for the bus topology. |
| USB | PARTIAL | CH340C, CP2102N, FT232RL, USBLC6-2SC6, TUSB320 | USB-C CC behavior, ESD, impedance, VBUS, and connector orientation must be checked. |
| Ethernet PHY / controller | PARTIAL | W5500, LAN8720 | Magnetics, termination, oscillator, strap pins, and RMII/SPI routing require detailed review. |
| UART bridges | PARTIAL | CH340C, CP2102N, FT232RL | Driver support and lifecycle status matter for product decisions. |
| I2C expanders | MISSING | None yet | Add after source research. |
| SPI devices | PARTIAL | W5500 | Exact SPI speed, mode, reset, and interrupt behavior require datasheet verification. |
| Level shifters | PARTIAL | PCA9306, TXS0108E, TXB0108 | Auto-direction translators are easy to misuse. Match bus type and drive strength. |

## Source Index

| Part / Topic | Vendor / Publisher | Document Type | Source URL | Local PDF | Verification Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| MCP2562 | Microchip | Product page and datasheet source | https://www.microchip.com/en-us/product/MCP2562 | Not bundled | SOURCE_LINK_RECORDED | High-speed CAN transceiver with standby and VIO pin per Microchip page; verify exact suffix. |
| MCP2562FD | Microchip | Product page and datasheet source | https://www.microchip.com/en-us/product/MCP2562FD | Not bundled | SOURCE_LINK_RECORDED | CAN FD transceiver family; verify exact CAN FD timing and package. |
| SN65HVD230 | Texas Instruments | Product page and datasheet source | https://www.ti.com/product/SN65HVD230 | Not bundled | SOURCE_LINK_RECORDED | Verify 3.3V CAN domain, common-mode, slope control, and package. |
| TJA1051 | NXP | Datasheet source | https://www.nxp.com/docs/en/data-sheet/TJA1051.pdf | Not bundled | SOURCE_LINK_RECORDED | Verify variant suffix because VIO and feature differences matter. |
| TJA1042 | NXP | Product page and datasheet source | https://www.nxp.com/products/TJA1042 | Not bundled | SOURCE_LINK_RECORDED | Verify TJA1042 variant, standby behavior, and package. |
| MCP2003 LIN | Microchip | Product page and datasheet source | https://www.microchip.com/en-us/product/MCP2003 | Not bundled | SOURCE_LINK_RECORDED | Verify LIN bus protection, battery domain, and package. |
| MAX3485 | Analog Devices | Product page and datasheet source | https://www.analog.com/en/products/max3485.html | Not bundled | SOURCE_LINK_RECORDED | RS485/RS422 transceiver; verify termination, biasing, and package. |
| SN65HVD75 | Texas Instruments | Product page and datasheet source | https://www.ti.com/product/SN65HVD75 | Not bundled | SOURCE_LINK_RECORDED | RS485 transceiver; verify half-duplex pins and ESD rating from datasheet. |
| CH340C | WCH / Nanjing Qinheng | Source placeholder | Unknown - requires source verification | Not bundled | UNVERIFIED_PLACEHOLDER | KiCad has a CH340C symbol with distributor datasheet link; official source still needs verification. |
| CP2102N | Silicon Labs | Datasheet source | https://www.silabs.com/documents/public/data-sheets/cp2102n-datasheet.pdf | Not bundled | SOURCE_LINK_RECORDED | Verify package, USB self/bus power scheme, reset, and regulator pins. |
| FT232RL | FTDI | Product page and datasheet source | https://ftdichip.com/products/ft232rl/ | Not bundled | SOURCE_LINK_RECORDED | FTDI page marks FT232RL as NRND; verify lifecycle before new designs. |
| USBLC6-2SC6 | STMicroelectronics | Product page and datasheet source | https://www.st.com/en/protections-and-emi-filters/usblc6-2.html | Not bundled | SOURCE_LINK_RECORDED | USB ESD protection device; verify package and capacitance for the interface. |
| TUSB320 | Texas Instruments | Product page and datasheet source | https://www.ti.com/product/TUSB320 | Not bundled | SOURCE_LINK_RECORDED | USB Type-C CC logic; not a full USB PD controller. |
| W5500 | WIZnet | Datasheet source | https://docs.wiznet.io/Product/Chip/Ethernet/W5500/datasheet | Not bundled | SOURCE_LINK_RECORDED | Hardwired TCP/IP Ethernet controller with SPI interface; verify magnetics and hardware guide. |
| LAN8720 | Microchip | Datasheet source | https://ww1.microchip.com/downloads/aemDocuments/documents/UNG/ProductDocuments/DataSheets/LAN8720A-LAN8720Ai-Data-Sheet-DS00002165.pdf | Not bundled | SOURCE_LINK_RECORDED | Ethernet PHY with RMII; verify oscillator, strap pins, magnetics, and package. |
| PCA9306 | Texas Instruments | Product page and datasheet source | https://www.ti.com/product/PCA9306 | Not bundled | SOURCE_LINK_RECORDED | I2C/SMBus level translator; verify pullups and voltage references. |
| TXS0108E | Texas Instruments | Product page and datasheet source | https://www.ti.com/product/TXS0108E | Not bundled | SOURCE_LINK_RECORDED | Bidirectional translator; verify bus type, capacitance, pullups, and drive strength. |
| TXB0108 | Texas Instruments | Product page and datasheet source | https://www.ti.com/product/TXB0108 | Not bundled | SOURCE_LINK_RECORDED | Auto-direction translator; not universal for open-drain or heavily loaded buses. |

## Local KiCad Library Evidence

Read-only searches of the installed KiCad 9 symbol libraries found starter candidates for:

- `Interface_CAN_LIN:MCP2562-E-MF`, `MCP2562-E-P`, `MCP2562-E-SN`, and high-temperature MCP2562 variants.
- `Interface_CAN_LIN:SN65HVD230`.
- `Interface_CAN_LIN:TJA1051T`, `TJA1051T-3`, `TJA1051T-E`, `TJA1051TK-3`.
- `Interface_CAN_LIN:TJA1042T`, `TJA1042T-3`, `TJA1042TK-3`.
- `Interface_UART:MAX3485`.
- `Interface_USB:CH340C`, `CP2102N-Axx-xQFN20`, `CP2102N-Axx-xQFN24`, `CP2102N-Axx-xQFN28`, `FT232RL`, `TUSB320`, `TUSB320I`.
- `Power_Protection:USBLC6-2SC6`, `USBLC6-2P6`, and related USBLC6 symbols.
- `Interface_Ethernet:LAN8720A`, `W5500`.
- `Interface:PCA9306`.
- `Logic_LevelTranslator:TXS0108EPW`, `TXB0108PW`, `TXB0108DQSR`, `TXB0108RGY`.

No exact local symbol candidates were found in this pass for `MCP2562FD`, `MCP2003`, or `SN65HVD75`.

## Missing Follow-Up Work

- Add specific I2C expander records.
- Add specific SPI peripheral records beyond W5500.
- Add Ethernet magnetics and RJ45 connector records.
- Add specific USB-C receptacle and CC/controller reference circuits.
- Add CAN connector pinout and protection pattern records.
- Add exact footprint-to-package verification for any part used in an active project.
