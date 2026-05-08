# ESP32_CSI_WIFI_NODE Component Selection Plan

Status: planning only. No component is approved until datasheet, footprint, sourcing, lifecycle, and project-fit checks are complete.

## Selection Priorities

- Use proven, widely available parts with clear datasheets and KiCad-compatible footprints.
- Prefer low-cost parts that are easy for small builders to source.
- Avoid unnecessary complexity unless it improves reliability, protection, or buildability.
- Keep all mains isolation outside the board by using an external certified 5 V DC supply.
- Verify every footprint against the manufacturer drawing before schematic-to-layout handoff.

## Primary Module

- Preferred: `ESP32-S3-WROOM-1U-N16R8`.
- Alternate: `ESP32-S3-WROOM-1U-N8R8`.
- Selection tasks:
  - Confirm exact Espressif ordering code and lifecycle status.
  - Download and store module datasheet, hardware design guidelines, and footprint drawing.
  - Verify WROOM-1U external antenna connector type and mechanical keepout.
  - Verify power, EN, BOOT, USB, strapping, and GPIO recommendations for the selected module.
  - Confirm whether the N16R8 and N8R8 module variants can share one footprint and BOM alternate strategy.

## Power Input Components

- DC barrel jack:
  - Requirement: 5.5 mm x 2.1 mm center-positive.
  - Selection tasks: choose panel/enclosure-friendly footprint, current rating, insertion durability, and mechanical retention.

- Input fuse or resettable polyfuse:
  - Requirement: protect board and supply wiring from faults.
  - Selection tasks: define hold current, trip current, voltage rating, resistance, temperature derating, and fault behavior.

- Reverse-polarity protection:
  - Requirement: protect against reversed barrel input.
  - Candidate approaches: Schottky diode, P-channel MOSFET ideal-diode style protection, or dedicated ideal-diode controller.
  - Selection tasks: compare voltage drop, heat, cost, buildability, and fault behavior.

- 5 V TVS diode:
  - Requirement: clamp transients at barrel input.
  - Selection tasks: choose working voltage, clamp voltage, package, surge capability, and placement strategy.

- Bulk input capacitor:
  - Requirement: stabilize board input and regulator supply.
  - Selection tasks: define capacitance, voltage rating, ESR, ripple, package, and derating.

## 3.3 V Regulator

- Requirement: supply ESP32-S3 module reliably during WiFi current peaks.
- Candidate topology decision:
  - LDO: simpler and lower noise, but thermal margin may be poor from 5 V to 3.3 V at WiFi peak current.
  - Buck regulator: better efficiency and thermal margin, but requires inductor, switching layout discipline, and EMI review.
- Selection tasks:
  - Define worst-case 3.3 V current budget.
  - Confirm regulator transient response for WiFi bursts.
  - Verify thermal performance at expected ambient temperature.
  - Verify inductor, diode or synchronous topology, compensation, and layout guidance if a buck is selected.
  - Confirm package is easy enough for intended builders.

## USB-C And ESD

- USB-C receptacle:
  - Requirement: programming/debug.
  - Selection tasks: choose USB 2.0-capable receptacle, verify footprint, shell tabs, mid-mount/top-mount choice, and enclosure wall alignment.

- USB-C configuration:
  - Requirement: correct CC resistors and power/backfeed behavior.
  - Selection tasks: decide whether board is sink-only, debug-only with separate barrel power, or capable of USB power.

- USB ESD protection:
  - Requirement: protect D+/D- and relevant connector pins.
  - Selection tasks: choose low-capacitance ESD array, package, clamp behavior, and placement close to USB-C.

## User Interface And Test

- BOOT button:
  - Requirement: manual boot/programming mode control.
  - Selection tasks: choose tactile switch footprint, user access, pull resistor strategy, and silkscreen.

- RESET / EN button:
  - Requirement: manual reset.
  - Selection tasks: choose tactile switch footprint, debounce/filtering if needed, and EN timing per module guidance.

- Power LED:
  - Requirement: visible board power indication.
  - Selection tasks: select rail, color, resistor value, brightness, current budget, and enclosure visibility.

- Status LED or RGB LED:
  - Requirement: firmware-controlled status indication.
  - Selection tasks: choose single-color versus RGB, GPIO assignment, current budget, and enclosure light-pipe or visibility approach.

- Test pads:
  - Requirement: 5 V, 3.3 V, and GND.
  - Selection tasks: choose pad size, labeling, probe access, and placement near board edge or bring-up area.

## Mechanical Components

- Mounting holes:
  - Requirement: four holes near corners.
  - Selection tasks: define screw size, plating intent, annular ring or NPTH style, copper keepout, and enclosure standoff geometry.

- Antenna hardware:
  - Requirement: U.FL/IPEX-to-SMA pigtail and screw-on 2.4 GHz enclosure antenna.
  - Selection tasks: define pigtail length, SMA bulkhead style, washer/nut clearance, strain relief, and enclosure wall thickness.

## Parts To Avoid For This Revision

- Bare ESP32-S3 chip.
- ESP32 development boards.
- 120 VAC input components.
- Unverified RF connector substitutions.
- Components without clear datasheets or footprint drawings.
- Parts requiring secret/API-gated sourcing data for basic design verification.

## Research Outputs To Capture Next

- Datasheets and hardware design guides under `datasheets/` or `06_DATASHEETS/` as appropriate.
- Candidate BOM table with manufacturer part numbers, vendor links, lifecycle status, and package/footprint mapping.
- Footprint verification notes for every connector, module, regulator, protection part, switch, LED, and test pad.
- Open-risk list for anything not yet verified.

## Reviewed Candidate Baseline - 2026-05-02

Status: component selection review complete enough to begin schematic planning, but not a final BOM and not approved for PCB layout or manufacturing.

Primary outputs from this review:

- `COMPONENT_SELECTION_REPORT.md`
- `DATASHEET_CHECKLIST.md`

### Selected For Schematic Planning

| Block | Planning selection | Notes |
| --- | --- | --- |
| ESP32 module | `ESP32-S3-WROOM-1U-N16R8` primary; `ESP32-S3-WROOM-1U-N8R8` alternate | External antenna WROOM-1U module only. No dev board and no bare ESP32-S3 chip. |
| 3.3 V regulator | Diodes `AP63203WU-7` | Fixed 3.3 V, 2 A synchronous buck, TSOT26. Better thermal margin than a 5 V to 3.3 V LDO. |
| USB architecture | Native ESP32-S3 USB | GPIO19 = USB D-, GPIO20 = USB D+. Do not add USB-to-UART bridge unless later required. |
| Status indicator | Simple single-color GPIO LED | Preferred over WS2812/RGB for lower cost, lower current, simpler firmware, and better reliability. |
| Input protection | PTC + P-channel MOSFET reverse-polarity protection + 5 V TVS | Final parts and exact topology remain under review. |
| Antenna | WROOM-1U external connector with U.FL/MHF I/AMC-compatible pigtail to SMA bulkhead | Final pigtail, SMA, antenna gain, and enclosure fit remain under review. |

### Verified Electrical Values

- ESP32 module rail: 3.3 V nominal; valid module supply range 3.0 V to 3.6 V.
- ESP32-S3 supply current guidance: design 3.3 V source for no less than 500 mA; project target is at least 1 A practical margin.
- AP63203 application values: 3.9 uH inductor, 10 uF input capacitor, 2 x 22 uF output capacitors, 100 nF bootstrap capacitor.
- AP63203 inductor requirement: choose current rating at least 35 percent over maximum load current; target DCR below 100 milliohm.
- EN / CHIP_PU circuit: 10 k pull-up to 3.3 V and 1 uF capacitor to GND.
- BOOT / GPIO0 circuit: 10 k pull-up to 3.3 V and momentary switch to GND. Avoid high-value capacitance on GPIO0.
- USB-C sink configuration: 5.1 k from CC1 to GND and 5.1 k from CC2 to GND.
- USB D+/D- series resistors: 22 ohm or 33 ohm near the ESP32-S3 module side.
- UART0 debug pins: U0TXD = GPIO43, U0RXD = GPIO44. If U0TXD leaves the board, include Espressif-recommended 499 ohm series resistor.
- Power LED planning resistor: 2.2 k from 3.3 V rail.
- Status LED planning resistor: 2.2 k from selected GPIO path.
- Mounting hole planning default: M2.5, 2.7 mm NPTH drill, 5.5 mm to 6.0 mm keepout.

### Candidate Parts Requiring Final Review

- Barrel jack: exact MPN not selected. Must be a right-angle through-hole 5.5 mm OD / 2.1 mm ID center-positive jack with verified footprint, current rating, and enclosure fit.
- PTC: Littelfuse `1206L110THYR` or equivalent 1.1 A hold class. Confirm trip behavior and temperature derating against final current budget.
- Reverse-polarity MOSFET: AO3401A class P-channel MOSFET. Confirm orientation, gate protection, thermal margin, pinout, and availability.
- TVS: Littelfuse `SMAJ5.0A` class unidirectional 5 V TVS. Confirm leakage, clamp, package, and placement.
- USB-C receptacle: GCT `USB4105` class. Confirm exact suffix, footprint, shell stake length, and JLCPCB/LCSC availability.
- USB ESD: TI `TPD2EUSB30` class. Confirm package, routing, and sourcing.
- Switches, LEDs, test pads, inductor, capacitors, pigtail, SMA bulkhead, antenna, and mounting hardware all need final manufacturer part numbers and footprint checks.

### Open Design Policy Items

- USB power/backfeed policy is still open. Do not directly short USB VBUS to the barrel-derived 5 V rail in the schematic. Either make USB data/debug require barrel power or add a reviewed protected power-path option.
- USB shield grounding strategy is still open. Reserve a flexible grounding/RC/ESD footprint strategy until enclosure and EMC assumptions are settled.
- Input bulk capacitor planning value is 47 uF, >= 10 V, but exact capacitor type, ESR, package, and inrush impact NEEDS_REVIEW.
- JLCPCB/LCSC availability was not assumed as final for any candidate part.
- Board dimensions, connector edge placement, antenna pigtail length, SMA bulkhead style, and enclosure wall thickness remain missing mechanical requirements.
