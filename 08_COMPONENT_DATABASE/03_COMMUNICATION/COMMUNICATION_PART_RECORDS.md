# Communication Part Records

Date: 2026-05-02

Status: starter records for common PCB communication interface parts. Records are not design-approved until exact datasheets, packages, pinouts, footprints, voltage domains, and layout requirements are verified.

Unknown field value:

```text
Unknown - requires source verification
```

## Record Summary

| Record ID | Part | Interface | Source Status | KiCad Candidate Status |
| --- | --- | --- | --- | --- |
| `COMM_MCP2562` | MCP2562 | CAN | Microchip source link recorded | KiCad candidates observed locally |
| `COMM_MCP2562FD` | MCP2562FD | CAN FD | Microchip source link recorded | Exact KiCad symbol not observed locally |
| `COMM_SN65HVD230` | SN65HVD230 | CAN | TI source link recorded | KiCad candidate observed locally |
| `COMM_TJA1051` | TJA1051 | CAN | NXP source link recorded | KiCad candidates observed locally |
| `COMM_TJA1042` | TJA1042 | CAN | NXP source link recorded | KiCad candidates observed locally |
| `COMM_MCP2003_LIN` | MCP2003 LIN | LIN | Microchip source link recorded | Exact KiCad symbol not observed locally |
| `COMM_MAX3485` | MAX3485 | RS485/RS422 | Analog Devices source link recorded | KiCad candidate observed locally |
| `COMM_SN65HVD75` | SN65HVD75 | RS485 | TI source link recorded | Exact KiCad symbol not observed locally |
| `COMM_CH340C` | CH340C | USB UART bridge | Official source unresolved | KiCad candidate observed locally |
| `COMM_CP2102N` | CP2102N | USB UART bridge | Silicon Labs source link recorded | KiCad candidates observed locally |
| `COMM_FT232RL` | FT232RL | USB UART bridge | FTDI source link recorded; lifecycle warning | KiCad candidate observed locally |
| `COMM_USBLC6_2SC6` | USBLC6-2SC6 | USB ESD protection | ST source link recorded | KiCad candidate observed locally |
| `COMM_TUSB320` | TUSB320 | USB Type-C CC logic | TI source link recorded | KiCad candidates observed locally |
| `COMM_W5500` | W5500 | Ethernet controller over SPI | WIZnet source link recorded | KiCad candidate observed locally |
| `COMM_LAN8720` | LAN8720 | Ethernet PHY | Microchip source link recorded | KiCad candidate observed locally |
| `COMM_PCA9306` | PCA9306 | I2C level translator | TI source link recorded | KiCad candidate observed locally |
| `COMM_TXS0108E` | TXS0108E | Level translator | TI source link recorded | KiCad candidate observed locally |
| `COMM_TXB0108` | TXB0108 | Level translator | TI source link recorded | KiCad candidates observed locally |

## Common Record Fields

Every record below includes:

- Verified/source status.
- Voltage domain.
- Package options.
- KiCad symbol and footprint candidates.
- External parts.
- Termination requirements.
- ESD/protection recommendations.
- Layout warnings.
- Common mistakes.
- Datasheet/source link placeholders.

## COMM_MCP2562

- Part number: MCP2562.
- Vendor: Microchip.
- Interface: CAN transceiver.
- Verified/source status: `VERIFIED_FROM_DATASHEET`, `VERIFIED_FROM_KICAD_LIBRARY`, `UNVERIFIED_PLACEHOLDER`.
- Source link: https://www.microchip.com/en-us/product/MCP2562.
- Voltage domain: CAN bus domain plus logic VIO domain per Microchip product description; exact VDD/VIO ranges require datasheet verification.
- Package options: Microchip package suffixes include candidates represented locally by `MF`, `P`, and `SN`; verify exact package drawing.
- KiCad symbol candidates: `Interface_CAN_LIN:MCP2562-E-MF`, `MCP2562-E-P`, `MCP2562-E-SN`, `MCP2562-H-MF`, `MCP2562-H-P`, `MCP2562-H-SN`.
- Common KiCad footprints: DFN/QFN, DIP-8, and SOIC-8 candidates only after suffix verification.
- External parts: local decoupling, CAN termination if board is a bus end, optional split termination, ESD/TVS, connector.
- Termination requirements: normally 120 ohm at each physical bus end; make selectable if board role is unknown.
- ESD/protection recommendations: bus-rated CAN ESD/TVS near connector for external cables.
- Layout warnings: route CANH/CANL together, keep stubs short, place protection near connector.
- Common mistakes: using transceiver without CAN controller, fixed termination on every node, wrong VIO assumptions.

## COMM_MCP2562FD

- Part number: MCP2562FD.
- Vendor: Microchip.
- Interface: CAN FD transceiver.
- Verified/source status: `VERIFIED_FROM_DATASHEET`, `UNVERIFIED_PLACEHOLDER`.
- Source link: https://www.microchip.com/en-us/product/MCP2562FD.
- Voltage domain: CAN FD bus domain plus logic domain; exact ranges require datasheet verification.
- Package options: Microchip package suffixes require source verification.
- KiCad symbol candidates: `Unknown - requires source verification`.
- Common KiCad footprints: SOIC/DFN/QFN-style candidates only after exact package verification.
- External parts: decoupling, CAN FD-capable termination/protection strategy, connector.
- Termination requirements: CAN bus termination at physical bus ends; CAN FD makes stubs and impedance more critical.
- ESD/protection recommendations: CAN FD-compatible ESD/TVS selected for bus voltage and capacitance.
- Layout warnings: minimize stubs and connector-to-transceiver distance; verify CAN FD timing budget.
- Common mistakes: assuming CAN FD transceiver gives CAN FD controller support.

## COMM_SN65HVD230

- Part number: SN65HVD230.
- Vendor: Texas Instruments.
- Interface: CAN transceiver.
- Verified/source status: `VERIFIED_FROM_DATASHEET`, `VERIFIED_FROM_KICAD_LIBRARY`, `UNVERIFIED_PLACEHOLDER`.
- Source link: https://www.ti.com/product/SN65HVD230.
- Voltage domain: TI source identifies this as a CAN transceiver for 3.3V systems; exact limits require datasheet verification.
- Package options: SOIC-8 candidate observed from TI/KiCad; verify package suffix.
- KiCad symbol candidates: `Interface_CAN_LIN:SN65HVD230`.
- Common KiCad footprints: `Package_SO:SOIC-8_3.9x4.9mm_P1.27mm` candidate; verify package drawing.
- External parts: decoupling, slope/standby configuration if used, termination if bus end, ESD/TVS.
- Termination requirements: only terminate at bus ends unless project requires otherwise.
- ESD/protection recommendations: external CAN bus protection when leaving the board.
- Layout warnings: keep CAN pair together and avoid noisy regions.
- Common mistakes: confusing transceiver with CAN controller, relying on low-cost modules without pinout/protection review.

## COMM_TJA1051

- Part number: TJA1051.
- Vendor: NXP.
- Interface: high-speed CAN transceiver.
- Verified/source status: `VERIFIED_FROM_DATASHEET`, `VERIFIED_FROM_KICAD_LIBRARY`, `UNVERIFIED_PLACEHOLDER`.
- Source link: https://www.nxp.com/docs/en/data-sheet/TJA1051.pdf.
- Voltage domain: variant-dependent CAN and logic domains; verify exact suffix, especially `-3` and VIO-related variants.
- Package options: SO8 and HVSON-style candidates exist by KiCad symbol family; verify exact NXP package.
- KiCad symbol candidates: `Interface_CAN_LIN:TJA1051T`, `TJA1051T-3`, `TJA1051T-E`, `TJA1051TK-3`.
- Common KiCad footprints: SOIC-8 and HVSON/DFN candidates only after suffix verification.
- External parts: decoupling, termination if bus end, optional split termination/protection, standby/silent pin control when applicable.
- Termination requirements: CAN termination at bus ends; make board termination configurable if role changes.
- ESD/protection recommendations: CAN-rated ESD/TVS near connector for external cable interfaces.
- Layout warnings: verify pinout variant; route CANH/CANL as a pair.
- Common mistakes: selecting the wrong suffix for MCU logic voltage.

## COMM_TJA1042

- Part number: TJA1042.
- Vendor: NXP.
- Interface: high-speed CAN transceiver with standby mode.
- Verified/source status: `VERIFIED_FROM_DATASHEET`, `VERIFIED_FROM_KICAD_LIBRARY`, `UNVERIFIED_PLACEHOLDER`.
- Source link: https://www.nxp.com/products/TJA1042.
- Voltage domain: variant-dependent CAN and logic domains; exact values require datasheet verification.
- Package options: SO8 and HVSON-style candidates by variant; verify exact package.
- KiCad symbol candidates: `Interface_CAN_LIN:TJA1042T`, `TJA1042T-3`, `TJA1042TK-3`.
- Common KiCad footprints: SOIC-8 and HVSON/DFN candidates only after suffix verification.
- External parts: decoupling, standby pin control, termination if bus end, ESD/TVS, connector.
- Termination requirements: same CAN bus termination rules; no fixed termination on every node.
- ESD/protection recommendations: choose CAN-rated protection for environment.
- Layout warnings: keep stubs short and verify standby pin state.
- Common mistakes: leaving standby/control pins ambiguous.

## COMM_MCP2003_LIN

- Part number: MCP2003.
- Vendor: Microchip.
- Interface: LIN transceiver.
- Verified/source status: `VERIFIED_FROM_DATASHEET`, `UNVERIFIED_PLACEHOLDER`.
- Source link: https://www.microchip.com/en-us/product/MCP2003.
- Voltage domain: LIN bus battery-domain plus logic interface; exact ranges require datasheet verification.
- Package options: Microchip suffix-specific; verify exact package.
- KiCad symbol candidates: `Unknown - requires source verification`.
- Common KiCad footprints: SOIC-8, DIP-8, DFN-style candidates only after suffix verification.
- External parts: decoupling, LIN pullup/master network if applicable, connector, automotive transient/reverse protection as required.
- Termination requirements: LIN is not terminated like CAN; use LIN datasheet/reference network.
- ESD/protection recommendations: automotive-rated ESD/transient strategy for external LIN harnesses.
- Layout warnings: keep LIN bus protection close to connector; check battery-domain clearances and fault paths.
- Common mistakes: treating LIN as plain UART or omitting automotive input protection.

## COMM_MAX3485

- Part number: MAX3485.
- Vendor: Analog Devices.
- Interface: RS485/RS422 transceiver.
- Verified/source status: `VERIFIED_FROM_DATASHEET`, `VERIFIED_FROM_KICAD_LIBRARY`, `UNVERIFIED_PLACEHOLDER`.
- Source link: https://www.analog.com/en/products/max3485.html.
- Voltage domain: Analog Devices product page identifies a 3.3V RS485/RS422 transceiver family; exact limits require datasheet verification.
- Package options: package models vary; verify exact suffix.
- KiCad symbol candidates: `Interface_UART:MAX3485`.
- Common KiCad footprints: SOIC-8 and DIP-8 candidates only after package verification.
- External parts: decoupling, termination if bus end, fail-safe bias when required, ESD/TVS, connector.
- Termination requirements: terminate only at bus ends; make selectable when node position is unknown.
- ESD/protection recommendations: RS485-rated TVS/ESD at connector for external cables.
- Layout warnings: route A/B pair together and keep stubs short.
- Common mistakes: reversing A/B labels, missing DE/RE control, adding termination to every node.

## COMM_SN65HVD75

- Part number: SN65HVD75.
- Vendor: Texas Instruments.
- Interface: RS485 transceiver.
- Verified/source status: `VERIFIED_FROM_DATASHEET`, `UNVERIFIED_PLACEHOLDER`.
- Source link: https://www.ti.com/product/SN65HVD75.
- Voltage domain: TI source identifies SN65HVD75 family as RS485; exact supply and IO limits require datasheet verification.
- Package options: TI package suffixes require source verification.
- KiCad symbol candidates: `Unknown - requires source verification`.
- Common KiCad footprints: SOIC-8, VSSOP, or other TI package candidates only after exact suffix verification.
- External parts: decoupling, termination if bus end, fail-safe bias strategy, ESD/TVS, connector.
- Termination requirements: topology-dependent RS485 termination and biasing.
- ESD/protection recommendations: select RS485-rated external protection if field wiring leaves board.
- Layout warnings: define DE/RE logic state; route bus pair together.
- Common mistakes: relying on internal fail-safe without verifying system idle behavior.

## COMM_CH340C

- Part number: CH340C.
- Vendor: WCH / Nanjing Qinheng.
- Interface: USB UART bridge.
- Verified/source status: `VERIFIED_FROM_KICAD_LIBRARY`, `UNVERIFIED_PLACEHOLDER`.
- Source link: `Unknown - requires source verification`.
- Voltage domain: USB device side plus UART logic side; exact supply and V3 behavior require official datasheet verification.
- Package options: KiCad symbol only; verify package and suffix from WCH source.
- KiCad symbol candidates: `Interface_USB:CH340C`.
- Common KiCad footprints: SOIC-16 and SOP/QFN candidates only after exact package verification.
- External parts: USB connector, USB ESD, decoupling, reset/boot wiring as required, UART TX/RX nets, optional status LEDs.
- Termination requirements: no bus termination like CAN/RS485; USB D+/D- routing and CC/VBUS rules still apply.
- ESD/protection recommendations: USB data and VBUS protection at connector.
- Layout warnings: verify USB D+/D- routing and whether external crystal is required for the exact CH340 variant.
- Common mistakes: using CH340G reference circuits for CH340C without checking differences.

## COMM_CP2102N

- Part number: CP2102N.
- Vendor: Silicon Labs.
- Interface: USB UART bridge.
- Verified/source status: `VERIFIED_FROM_DATASHEET`, `VERIFIED_FROM_KICAD_LIBRARY`, `UNVERIFIED_PLACEHOLDER`.
- Source link: https://www.silabs.com/documents/public/data-sheets/cp2102n-datasheet.pdf.
- Voltage domain: USB device side plus configurable UART/GPIO domain; exact supply scheme requires datasheet verification.
- Package options: xQFN20, xQFN24, xQFN28 candidates observed locally.
- KiCad symbol candidates: `Interface_USB:CP2102N-Axx-xQFN20`, `CP2102N-Axx-xQFN24`, `CP2102N-Axx-xQFN28`.
- Common KiCad footprints: QFN20, QFN24, QFN28 candidates only after package drawing verification.
- External parts: USB connector, USB ESD, decoupling, reset circuit if required, UART pins, optional LEDs and handshaking.
- Termination requirements: no bus termination; USB routing rules apply.
- ESD/protection recommendations: low-capacitance USB ESD at connector.
- Layout warnings: verify exposed pad, VBUS/self-powered connection, and reset pin recommendations.
- Common mistakes: omitting required decoupling or miswiring USB power mode.

## COMM_FT232RL

- Part number: FT232RL.
- Vendor: FTDI.
- Interface: USB UART bridge.
- Verified/source status: `VERIFIED_FROM_DATASHEET`, `VERIFIED_FROM_KICAD_LIBRARY`, `UNVERIFIED_PLACEHOLDER`.
- Source link: https://ftdichip.com/products/ft232rl/.
- Voltage domain: USB device side plus UART IO domain; exact IO voltage scheme requires datasheet verification.
- Package options: FTDI product page marks FT232RL as NRND; package verification still required.
- KiCad symbol candidates: `Interface_USB:FT232RL`.
- Common KiCad footprints: SSOP-28/QFN candidates only after exact package verification.
- External parts: USB connector, ESD, decoupling, configuration pins, UART nets, optional LEDs.
- Termination requirements: no bus termination; USB routing rules apply.
- ESD/protection recommendations: USB ESD at connector and VBUS protection as required.
- Layout warnings: verify oscillator/USB support components and driver/lifecycle policy.
- Common mistakes: selecting FT232RL for new design without considering NRND status.

## COMM_USBLC6_2SC6

- Part number: USBLC6-2SC6.
- Vendor: STMicroelectronics.
- Interface: USB ESD protection.
- Verified/source status: `VERIFIED_FROM_DATASHEET`, `VERIFIED_FROM_KICAD_LIBRARY`, `UNVERIFIED_PLACEHOLDER`.
- Source link: https://www.st.com/en/protections-and-emi-filters/usblc6-2.html.
- Voltage domain: USB data-line ESD clamp domain; exact standoff, capacitance, and clamp behavior require datasheet verification.
- Package options: SC6 and P6 family variants; verify exact package and pinout.
- KiCad symbol candidates: `Power_Protection:USBLC6-2SC6`, `Power_Protection:USBLC6-2P6`.
- Common KiCad footprints: SOT-23-6 / SOT-666-style candidates only after package verification.
- External parts: USB connector and low-impedance ESD return path.
- Termination requirements: none; this is a protection part.
- ESD/protection recommendations: place close to USB connector before long D+/D- traces.
- Layout warnings: route through/near device as recommended and avoid long return paths.
- Common mistakes: using wrong USBLC6 package symbol or placing protection near the IC instead of connector.

## COMM_TUSB320

- Part number: TUSB320.
- Vendor: Texas Instruments.
- Interface: USB Type-C CC logic and port controller.
- Verified/source status: `VERIFIED_FROM_DATASHEET`, `VERIFIED_FROM_KICAD_LIBRARY`, `UNVERIFIED_PLACEHOLDER`.
- Source link: https://www.ti.com/product/TUSB320.
- Voltage domain: USB Type-C CC logic plus controller supply; exact voltage limits require datasheet verification.
- Package options: TI package suffixes require source verification.
- KiCad symbol candidates: `Interface_USB:TUSB320`, `Interface_USB:TUSB320I`.
- Common KiCad footprints: QFN/VQFN candidates only after package drawing verification.
- External parts: USB-C connector, CC routing, VBUS protection, USB ESD, configuration resistors as required.
- Termination requirements: USB-C CC behavior, not CAN/RS485-style termination.
- ESD/protection recommendations: protect CC, D+/D-, and VBUS as required by port role.
- Layout warnings: TUSB320 is not a full USB PD controller; verify port role and current advertisement.
- Common mistakes: using it where full PD negotiation is required.

## COMM_W5500

- Part number: W5500.
- Vendor: WIZnet.
- Interface: hardwired TCP/IP Ethernet controller with SPI host interface.
- Verified/source status: `VERIFIED_FROM_DATASHEET`, `VERIFIED_FROM_KICAD_LIBRARY`, `UNVERIFIED_PLACEHOLDER`.
- Source link: https://docs.wiznet.io/Product/Chip/Ethernet/W5500/datasheet.
- Voltage domain: Ethernet PHY/controller domain plus SPI logic domain; exact supply and IO requirements require datasheet verification.
- Package options: WIZnet package requires datasheet verification.
- KiCad symbol candidates: `Interface_Ethernet:W5500`.
- Common KiCad footprints: LQFP/QFN candidates only after package drawing verification.
- External parts: crystal or clock source, magnetics or MagJack, termination/bias network, decoupling, reset, SPI pullups/series resistors if required, LEDs.
- Termination requirements: Ethernet magnetics and line termination per WIZnet reference design, not generic 120 ohm termination.
- ESD/protection recommendations: Ethernet connector protection and chassis/shield strategy as required.
- Layout warnings: follow WIZnet hardware guide, differential pair routing, magnetics placement, and keepouts.
- Common mistakes: omitting required strap/reserved pin states or copying module magnetics without connector verification.

## COMM_LAN8720

- Part number: LAN8720.
- Vendor: Microchip.
- Interface: Ethernet PHY with RMII.
- Verified/source status: `VERIFIED_FROM_DATASHEET`, `VERIFIED_FROM_KICAD_LIBRARY`, `UNVERIFIED_PLACEHOLDER`.
- Source link: https://ww1.microchip.com/downloads/aemDocuments/documents/UNG/ProductDocuments/DataSheets/LAN8720A-LAN8720Ai-Data-Sheet-DS00002165.pdf.
- Voltage domain: Ethernet PHY domain plus RMII logic domain; exact supply rails require datasheet verification.
- Package options: KiCad description notes QFN-24 for LAN8720A candidate; verify package drawing.
- KiCad symbol candidates: `Interface_Ethernet:LAN8720A`.
- Common KiCad footprints: QFN-24 candidate only after package drawing verification.
- External parts: oscillator/clock, magnetics or MagJack, termination/bias network, decoupling, reset, strap resistors, RMII signals, LEDs.
- Termination requirements: Ethernet termination per Microchip reference design and magnetics selection.
- ESD/protection recommendations: Ethernet connector ESD and shield/chassis strategy as required.
- Layout warnings: RMII clock/data routing, PHY crystal/clock, strap pins, and magnetics placement are critical.
- Common mistakes: missing strap pins, wrong RMII clock direction, and unverified MagJack pinout.

## COMM_PCA9306

- Part number: PCA9306.
- Vendor: Texas Instruments.
- Interface: I2C/SMBus level translator.
- Verified/source status: `VERIFIED_FROM_DATASHEET`, `VERIFIED_FROM_KICAD_LIBRARY`, `UNVERIFIED_PLACEHOLDER`.
- Source link: https://www.ti.com/product/PCA9306.
- Voltage domain: side 1 and side 2 reference rails for I2C/SMBus; exact ranges require datasheet verification.
- Package options: package suffixes vary; verify exact package.
- KiCad symbol candidates: `Interface:PCA9306`, `PCA9306D`, `PCA9306DC`, `PCA9306DC1`, `PCA9306DP`.
- Common KiCad footprints: SOIC/TSSOP/VSSOP/XSON candidates only after suffix verification.
- External parts: pullups on both bus sides, reference rails, enable control, decoupling.
- Termination requirements: I2C pullup sizing, not transmission-line termination.
- ESD/protection recommendations: add external ESD if bus leaves the board.
- Layout warnings: keep I2C traces short where possible and check bus capacitance/rise time.
- Common mistakes: omitting pullups or reversing low/high reference sides.

## COMM_TXS0108E

- Part number: TXS0108E.
- Vendor: Texas Instruments.
- Interface: 8-bit bidirectional level translator.
- Verified/source status: `VERIFIED_FROM_DATASHEET`, `VERIFIED_FROM_KICAD_LIBRARY`, `UNVERIFIED_PLACEHOLDER`.
- Source link: https://www.ti.com/product/TXS0108E.
- Voltage domain: side A and side B voltage rails; exact ranges require datasheet verification.
- Package options: KiCad candidate observed for PW package; verify exact suffix.
- KiCad symbol candidates: `Logic_LevelTranslator:TXS0108EPW`.
- Common KiCad footprints: TSSOP-20 candidate and other TI package candidates after suffix verification.
- External parts: decoupling on both rails, output enable state, pullups where datasheet requires.
- Termination requirements: not bus termination; bus-specific pullups/loads must be verified.
- ESD/protection recommendations: external ESD required if translated signals leave the board.
- Layout warnings: check capacitive load, pullup strength, and drive behavior.
- Common mistakes: treating TXS0108E as a universal high-speed push-pull translator.

## COMM_TXB0108

- Part number: TXB0108.
- Vendor: Texas Instruments.
- Interface: 8-bit auto-direction level translator.
- Verified/source status: `VERIFIED_FROM_DATASHEET`, `VERIFIED_FROM_KICAD_LIBRARY`, `UNVERIFIED_PLACEHOLDER`.
- Source link: https://www.ti.com/product/TXB0108.
- Voltage domain: side A and side B voltage rails; exact ranges require datasheet verification.
- Package options: PW, DQS, and RGY candidates observed locally; verify exact suffix.
- KiCad symbol candidates: `Logic_LevelTranslator:TXB0108PW`, `TXB0108DQSR`, `TXB0108RGY`.
- Common KiCad footprints: TSSOP-20, SON/QFN/VQFN candidates only after package verification.
- External parts: decoupling on both rails, output enable state, bus-specific series/pull components only if datasheet allows.
- Termination requirements: not bus termination; verify signal loading and direction behavior.
- ESD/protection recommendations: external ESD if signals leave the board.
- Layout warnings: keep translated nets short and avoid heavy capacitive loads.
- Common mistakes: using TXB0108 for I2C/open-drain buses or strong pullup networks.
