# ESP32_CSI_WIFI_NODE Component Selection Report

Date: 2026-05-02

Status: pre-schematic component selection review. This is not a final BOM, not a schematic, and not a manufacturing release.

## Scope

This report selects a practical baseline for a compact custom ESP32-S3 CSI WiFi node PCB. It keeps the board as one complete custom PCB with an ESP32-S3 module soldered directly to the board. It does not use a development board, does not use a bare ESP32-S3 chip, and does not include 120 VAC circuitry.

## Primary Source References

- Espressif ESP32-S3-WROOM-1 / ESP32-S3-WROOM-1U datasheet: https://www.espressif.com/sites/default/files/documentation/esp32-s3-wroom-1_wroom-1u_datasheet_en.pdf
- Espressif ESP32-S3 hardware design guidelines, schematic checklist: https://docs.espressif.com/projects/esp-hardware-design-guidelines/en/latest/esp32s3/schematic-checklist.html
- Espressif ESP32-S3 hardware design guidelines, PCB layout design: https://docs.espressif.com/projects/esp-hardware-design-guidelines/en/latest/esp32s3/pcb-layout-design.html
- Espressif USB Type-C hardware design guide: https://docs.espressif.com/projects/esp-iot-solution/en/latest/usb/usb_overview/usb_typec_hardware_guide.html
- Diodes Incorporated AP63200/AP63201/AP63203/AP63205 datasheet: https://www.diodes.com/assets/Datasheets/AP63200-AP63201-AP63203-AP63205.pdf
- TI TPD2EUSB30 product page and datasheet link: https://www.ti.com/product/TPD2EUSB30
- GCT USB4105 USB-C receptacle specification: https://gct.co/files/specs/usb4105-spec.pdf
- Same Sky / CUI Devices PJ-102A datasheet, reviewed as a right-angle through-hole reference only: https://www.digikey.com/en/htmldatasheets/production/665129/0/0/2/pj-102a
- Littelfuse 1206L110THYR product page and 1206L series data: https://www.littelfuse.com/products/fuses-overcurrent-protection/polyswitch-resettable-pptc-devices/surface-mount-polyswitch-resettable-pptc-devices/1206l/1206l110th
- Littelfuse SMAJ5.0A product page: https://www.littelfuse.com/products/overvoltage-protection/tvs-diodes/surface-mount/smaj/smaj5-0a
- Alpha and Omega Semiconductor AO3401A product page and datasheet: https://www.aosmd.com/products/mosfets/p-channel-mosfets-8v-60v/ao3401a

## Recommended Component Baseline

| Block | Recommended planning choice | Selected / verified values | Status |
| --- | --- | --- | --- |
| ESP32 module | Espressif `ESP32-S3-WROOM-1U-N16R8` | External antenna WROOM-1U module, 16 MB flash, 8 MB PSRAM | Primary |
| ESP32 alternate | Espressif `ESP32-S3-WROOM-1U-N8R8` | External antenna WROOM-1U module, 8 MB flash, 8 MB PSRAM | Alternate |
| 3.3 V regulator | Diodes `AP63203WU-7` synchronous buck | 3.8 V to 32 V input, fixed 3.3 V, 2 A, TSOT26 | Selected for schematic planning |
| Buck inductor | Shielded power inductor | 3.9 uH, saturation/current rating to exceed AP63203 requirement; target >= 2.7 A and DCR < 100 milliohm | Electrical value verified, exact part NEEDS_REVIEW |
| Buck input cap | Ceramic capacitor near AP63203 VIN | 10 uF, voltage/derating NEEDS_REVIEW | Value verified |
| Buck output caps | Ceramic capacitors near AP63203 VOUT | 2 x 22 uF, voltage/derating NEEDS_REVIEW | Value verified |
| Buck bootstrap cap | Ceramic capacitor BST to SW | 100 nF | Value verified |
| Barrel jack | Final MPN not selected; use a right-angle through-hole 5.5 mm OD / 2.1 mm ID DC jack | Center-positive, edge-facing, mechanically strong, target current rating >= 2 A | NEEDS_REVIEW |
| Input PTC | Littelfuse `1206L110THYR` or equivalent | 1.1 A hold class at 23 C; derates with temperature | Candidate, NEEDS_REVIEW |
| Reverse polarity | P-channel MOSFET protection, AO3401A class | 30 V P-MOS, SOT-23, Rds(on) max 60 milliohm at Vgs = -4.5 V | Candidate, NEEDS_REVIEW |
| 5 V TVS | Littelfuse `SMAJ5.0A` class unidirectional TVS | 5 V standoff, 400 W, 9.2 V max clamp at rated pulse | Candidate, NEEDS_REVIEW |
| Input bulk | Low-ESR bulk capacitor after protection | 47 uF, >= 10 V as a starting point | NEEDS_REVIEW |
| USB-C receptacle | GCT `USB4105` class USB 2.0 Type-C receptacle | USB 2.0 data capable, SMT top-mount, high VBUS/GND collective current ratings | Candidate, NEEDS_REVIEW |
| USB-C CC resistors | Two pull-down resistors | 5.1 k, one from CC1 to GND and one from CC2 to GND | Value verified |
| USB ESD | TI `TPD2EUSB30` class 2-channel low-capacitance ESD array | 2 channels, 5.5 V Vrwm, 0.7 pF typical capacitance | Candidate, NEEDS_REVIEW |
| USB data series resistors | One resistor in series with each USB data line | 22 ohm or 33 ohm, close to ESP32-S3 module pin | Value range verified |
| USB data shunt footprints | DNI capacitor footprint from each USB data line to GND | Value not selected | NEEDS_REVIEW |
| RESET / EN circuit | Tactile switch pulls EN low | 10 k pull-up to 3.3 V, 1 uF EN capacitor to GND | Value verified |
| BOOT circuit | Tactile switch pulls GPIO0 low | 10 k pull-up to 3.3 V; no high-value capacitor on GPIO0 | Value verified / cap warning verified |
| Power LED | Simple low-current LED | 2.2 k series resistor from 3.3 V rail planning default | Calculated, LED part NEEDS_REVIEW |
| Status LED | Simple single-color GPIO LED | 2.2 k series resistor planning default | Recommended; LED/GPIO NEEDS_REVIEW |
| RGB LED | WS2812-style RGB LED | Not recommended for revision A unless user explicitly wants RGB | Not selected |
| Test pads | Probe pads for bring-up | 5V, 3V3, GND, EN, BOOT/GPIO0, U0TXD, U0RXD; optional USB D+/D- | Selected set, footprint NEEDS_REVIEW |
| Mounting holes | Four NPTH holes near corners | M2.5 default: 2.7 mm drill, 5.5 mm to 6.0 mm keepout | Planning default, NEEDS_REVIEW |
| External antenna | U.FL/MHF I/AMC-compatible pigtail to SMA bulkhead | 2.4 GHz, 50 ohm antenna; gain <= 2.33 dBi if relying on module certification limits | NEEDS_REVIEW |

## ESP32-S3-WROOM-1U Verification

- Exact module baseline: `ESP32-S3-WROOM-1U-N16R8`.
- Exact module alternate: `ESP32-S3-WROOM-1U-N8R8`.
- Module type: WROOM-1U external antenna connector version, not PCB antenna version.
- Supply rail: 3.3 V nominal. Datasheet operating range is 3.0 V to 3.6 V.
- Current requirement: Espressif hardware guidance says the 3.3 V supply should provide no less than 500 mA. This board should design the 3.3 V regulator with at least 1 A practical margin because WiFi burst current, USB activity, LEDs, and temperature can reduce margin.
- Decoupling baseline: place 10 uF plus 0.1 uF close to the module 3.3 V entry and use the AP63203 output network of 2 x 22 uF near the regulator. Final capacitor voltage rating, dielectric, size, and DC-bias derating NEEDS_REVIEW.
- EN / reset: use 10 k pull-up from EN / CHIP_PU to 3.3 V and 1 uF from EN to GND. RESET button pulls EN to GND.
- BOOT / download: GPIO0 is a strapping pin. Use 10 k pull-up to 3.3 V and a BOOT button that pulls GPIO0 to GND. Do not add high-value capacitance to GPIO0.
- Other strapping pins: GPIO0, GPIO3, GPIO45, and GPIO46 are strapping pins. Avoid fixed external circuitry that drives the wrong boot state during reset.
- Native USB: GPIO19 is USB D-, GPIO20 is USB D+.
- USB series parts: Espressif recommends 22 ohm or 33 ohm series resistors in the USB data lines and reserved capacitor footprints to ground, placed close to the chip/module side.
- UART debug pads: UART0 defaults are GPIO43 U0TXD and GPIO44 U0RXD. Espressif recommends a 499 ohm series resistor on U0TXD to suppress harmonics if UART0 is routed off-board.
- Antenna: WROOM-1U uses an external antenna connector compatible with U.FL, MHF I, and AMC mating connectors. The module ships without an external antenna. Select a 2.4 GHz, 50 ohm antenna. Espressif notes that using an antenna with different type or gain can require additional EMC/certification work; for baseline planning keep antenna gain at or below 2.33 dBi unless certification work is intentionally expanded.

## 5 V Power Input

- Use a center-positive 5 V DC barrel input. Silkscreen should clearly show `5V DC ONLY`, center-positive polarity, and no 120 VAC.
- Use a mechanically strong through-hole right-angle barrel jack so the connector can face the enclosure wall and tolerate repeated plug insertion.
- Final barrel jack MPN is not selected. The selected part must explicitly support the required 5.5 mm OD / 2.1 mm ID center-positive adapter, have a verified footprint drawing, and meet the current/mechanical requirements. The Same Sky / CUI `PJ-102A` datasheet was reviewed only as a right-angle through-hole current-rated reference, not as the locked final 5.5 mm x 2.1 mm part.

## Input Protection

- PTC: use a resettable fuse after the barrel jack. A 1.1 A hold class such as Littelfuse `1206L110THYR` is the current baseline, but final hold/trip current NEEDS_REVIEW against maximum board load, wall adapter rating, enclosure temperature, and PTC derating.
- Reverse polarity: use a P-channel MOSFET high-side reverse-polarity protection circuit rather than a simple Schottky diode for lower voltage drop and lower heat. AO3401A class SOT-23 P-MOS is a candidate. Final MOSFET, footprint, orientation, gate network, and gate-source protection NEEDS_REVIEW.
- TVS: use a unidirectional TVS at the protected 5 V input. `SMAJ5.0A` is a robust candidate. Final package and leakage/clamp tradeoff NEEDS_REVIEW, especially with 5 V adapter tolerance and regulator absolute maximums.
- Bulk input capacitance: AP63203 requires local 10 uF ceramic input capacitance. Add a board-level bulk footprint after input protection, planning default 47 uF >= 10 V. Exact capacitance, ESR, voltage rating, and package NEEDS_REVIEW.

## 3.3 V Regulator

Primary regulator selection: Diodes `AP63203WU-7`.

Reasons:

- Fixed 3.3 V output and 2 A rating provide margin over the minimum ESP32-S3 supply guidance.
- Buck topology avoids the thermal penalty of dropping 5 V to 3.3 V at high WiFi current.
- TSOT26 package is compact but still practical for assembly if the footprint and soldering rules are followed.
- Datasheet includes recommended values for the fixed 3.3 V AP63203 configuration.

Verified AP63203 application values:

- Inductor: 3.9 uH.
- Input capacitor C1: 10 uF.
- Output capacitor C2: 2 x 22 uF.
- Bootstrap capacitor C3: 100 nF.
- Inductor design target: current rating at least 35 percent higher than maximum load current and DCR below 100 milliohm.

Layout notes:

- Keep VIN capacitor, SW loop, inductor, bootstrap cap, and output capacitors tight to the regulator.
- Provide strong ground returns and thermal copper. The datasheet notes that thermal analysis is required and gives TSOT26 theta-JA guidance.
- Final inductor and capacitor part numbers NEEDS_REVIEW for saturation current, DC bias, temperature, package, cost, and JLCPCB/LCSC availability.

## USB-C Programming And Debug

- Use native ESP32-S3 USB instead of a USB-to-UART bridge for revision A unless a later requirement demands a bridge.
- Wire USB D- to GPIO19 and USB D+ to GPIO20.
- USB-C sink CC configuration: place 5.1 k from CC1 to GND and 5.1 k from CC2 to GND.
- Add USB ESD protection close to the USB-C connector. TI `TPD2EUSB30` is a candidate because it is a 2-channel low-capacitance ESD part suitable for high-speed differential IO.
- Add 22 ohm or 33 ohm series resistors in D+ and D- near the ESP32-S3 module side.
- Reserve small capacitor-to-ground footprints on D+ and D-, DNI by default unless signal testing or Espressif reference schematic review supports loading them.
- Do not directly short USB VBUS to the barrel-derived 5 V rail until the USB power/backfeed policy is decided. Baseline schematic planning should either make USB data/debug require barrel power, or add a reviewed ideal-diode / power-path option. This remains NEEDS_REVIEW.
- USB shield grounding NEEDS_REVIEW. For a plastic enclosure, reserve a flexible strategy: direct shield-to-GND stitching option plus optional RC/capacitor/ESD network footprint if EMC testing or enclosure strategy requires it.

## Buttons And LEDs

- RESET / EN button: momentary tactile switch from EN to GND, with 10 k pull-up to 3.3 V and 1 uF EN capacitor to GND.
- BOOT button: momentary tactile switch from GPIO0 to GND, with 10 k pull-up to 3.3 V. Avoid high-value capacitance on GPIO0.
- Power LED: simple low-current LED on 3.3 V rail with a 2.2 k resistor as the planning default. Final LED color, luminous intensity, and resistor value NEEDS_REVIEW with the actual LED datasheet and enclosure visibility.
- Status LED: prefer one simple single-color GPIO LED with a 2.2 k series resistor planning default.
- RGB LED: not recommended for revision A. A WS2812-style LED adds current draw, firmware timing/protocol dependency, possible level-margin concerns at 3.3 V, and more parts. It is only worth including if RGB indication is a real user requirement.

## Test Pads

Required:

- 5V after input protection.
- 3V3 regulator output.
- GND, preferably more than one pad.
- EN.
- BOOT / GPIO0.

Recommended:

- U0TXD / GPIO43.
- U0RXD / GPIO44.
- USB D+ and D- only if the pads can be placed without harmful stubs.

Pad size, style, and location NEEDS_REVIEW. Use clearly labeled bring-up pads that can be probed in an enclosure-friendly position.

## Mechanical Baseline

- Board: compact rectangle.
- Mounting: four corner NPTH holes. Planning default is M2.5 hardware with 2.7 mm drill and 5.5 mm to 6.0 mm keepout. M3 may be used if the final board size allows it.
- Barrel jack: board edge, facing enclosure wall, with plug insertion clearance.
- USB-C: board edge, facing enclosure wall, with shell/mechanical tab footprint verified against the connector drawing.
- Antenna: reserve access above the WROOM-1U external antenna connector, pigtail bend clearance, strain relief, and SMA bulkhead nut/washer clearance. Exact pigtail length and SMA bulkhead style NEEDS_REVIEW.

## Values Selected

- ESP32 module rail: 3.3 V nominal, valid module range 3.0 V to 3.6 V.
- Regulator minimum design output current: at least 1 A; selected regulator is 2 A.
- AP63203 inductor: 3.9 uH.
- AP63203 input capacitor: 10 uF.
- AP63203 output capacitors: 2 x 22 uF.
- AP63203 bootstrap capacitor: 100 nF.
- EN pull-up: 10 k.
- EN capacitor: 1 uF.
- BOOT / GPIO0 pull-up: 10 k.
- USB-C CC resistors: 5.1 k on CC1 and 5.1 k on CC2.
- USB D+/D- series resistors: 22 ohm or 33 ohm.
- Power LED resistor planning value: 2.2 k.
- Status LED resistor planning value: 2.2 k.
- UART0 TX series resistor if UART pad/header is routed off-board: 499 ohm.
- M2.5 mounting hole planning drill: 2.7 mm NPTH.

## NEEDS_REVIEW Before Schematic Freeze

- Confirm exact module order codes, lifecycle, and footprint for `ESP32-S3-WROOM-1U-N16R8` and `ESP32-S3-WROOM-1U-N8R8`.
- Confirm whether the board must be powered by USB-C, barrel only, or both with a protected power path.
- Confirm final barrel jack mating compatibility with the required 5.5 mm x 2.1 mm center-positive adapter.
- Confirm PTC hold/trip current after current budget and temperature derating.
- Confirm reverse-polarity MOSFET circuit orientation, gate protection, and final part.
- Confirm 5 V TVS package, leakage, clamp voltage, and placement relative to fuse and reverse-polarity protection.
- Confirm input bulk capacitance and voltage rating.
- Confirm AP63203 JLCPCB/LCSC availability and exact inductor/capacitor part numbers.
- Confirm USB-C receptacle final part, footprint, and enclosure alignment.
- Confirm USB shield grounding strategy.
- Confirm whether USB data shunt capacitor footprints should be present and DNI.
- Confirm switch part numbers and footprints.
- Confirm LED color, brightness, resistor values, GPIO assignment, and enclosure visibility.
- Confirm test pad footprint and whether USB D+/D- pads are acceptable.
- Confirm mounting screw size, standoff keepout, board dimensions, connector edge positions, antenna pigtail length, SMA bulkhead style, and enclosure wall thickness.
- Confirm JLCPCB assembly availability for all selected candidates; no availability was assumed as final in this review.
