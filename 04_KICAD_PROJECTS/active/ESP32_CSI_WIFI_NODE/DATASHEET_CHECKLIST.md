# ESP32_CSI_WIFI_NODE Datasheet Checklist

Date: 2026-05-02

Status: pre-schematic checklist. All `NEEDS_REVIEW` items must be resolved or intentionally accepted before schematic freeze.

| Block | Candidate / source | Required checks | Status |
| --- | --- | --- | --- |
| ESP32 module primary | Espressif `ESP32-S3-WROOM-1U-N16R8` datasheet: https://www.espressif.com/sites/default/files/documentation/esp32-s3-wroom-1_wroom-1u_datasheet_en.pdf | Confirm ordering code, lifecycle, module dimensions, land pattern, pinout, 3.0 V to 3.6 V rail, antenna connector, flash/PSRAM variant, MPN marking, and JLC sourcing path | NEEDS_REVIEW for sourcing/footprint; electrical baseline verified |
| ESP32 module alternate | Espressif `ESP32-S3-WROOM-1U-N8R8` same datasheet | Confirm footprint and schematic compatibility with N16R8 primary; confirm BOM alternate strategy | NEEDS_REVIEW |
| ESP32 hardware guide | Espressif schematic checklist: https://docs.espressif.com/projects/esp-hardware-design-guidelines/en/latest/esp32s3/schematic-checklist.html | Verify 3.3 V supply current guidance, EN RC, strapping pins, BOOT behavior, USB D+/D- pins, USB series resistor guidance, UART pins, UART TX resistor guidance | VERIFIED_FOR_PLANNING |
| ESP32 layout guide | Espressif PCB layout design: https://docs.espressif.com/projects/esp-hardware-design-guidelines/en/latest/esp32s3/pcb-layout-design.html | Verify module placement, RF/antenna clearance, power routing, ESD placement, USB/UART distance from antenna, grounding | NEEDS_REVIEW during PCB planning |
| External antenna | ESP32-S3-WROOM-1U datasheet and selected pigtail/SMA datasheets | Confirm U.FL/MHF I/AMC mating compatibility, pigtail height, bend radius, strain relief, SMA bulkhead dimensions, antenna gain <= 2.33 dBi unless additional certification work is planned | NEEDS_REVIEW |
| Barrel jack | Final 5.5 mm OD / 2.1 mm ID right-angle through-hole MPN not selected; Same Sky / CUI `PJ-102A` reviewed only as a right-angle through-hole reference: https://www.digikey.com/en/htmldatasheets/production/665129/0/0/2/pj-102a | Select a manufacturer part whose drawing explicitly supports 5.5 mm OD / 2.1 mm ID center-positive adapter use; confirm pinout, current rating, insertion depth, footprint, enclosure edge position, plug clearance | NEEDS_REVIEW |
| PTC fuse | Littelfuse `1206L110THYR`: https://www.littelfuse.com/products/fuses-overcurrent-protection/polyswitch-resettable-pptc-devices/surface-mount-polyswitch-resettable-pptc-devices/1206l/1206l110th | Confirm hold current, trip current, voltage rating, cold/hot resistance, derating at enclosure temperature, trip time, package, JLC/LCSC availability | NEEDS_REVIEW |
| Reverse-polarity MOSFET | AOS `AO3401A`: https://www.aosmd.com/products/mosfets/p-channel-mosfets-8v-60v/ao3401a | Confirm Vds, Vgs, Rds(on), thermal margin, SOT-23 footprint, pinout, circuit orientation, gate resistor/pulldown, optional gate-source zener for adapter misuse | NEEDS_REVIEW |
| 5 V TVS | Littelfuse `SMAJ5.0A`: https://www.littelfuse.com/products/overvoltage-protection/tvs-diodes/surface-mount/smaj/smaj5-0a | Confirm standoff voltage, leakage at adapter tolerance, clamp voltage versus downstream ratings, package size, polarity, surge target, placement | NEEDS_REVIEW |
| Input bulk capacitor | Generic low-ESR capacitor, final MPN not selected | Confirm 47 uF planning value, voltage rating >= 10 V, ESR, ripple, temperature, package, derating, inrush behavior | NEEDS_REVIEW |
| 3.3 V buck regulator | Diodes `AP63203WU-7`: https://www.diodes.com/assets/Datasheets/AP63200-AP63201-AP63203-AP63205.pdf | Confirm fixed 3.3 V variant, 2 A rating, 3.8 V to 32 V input, TSOT26 footprint, thermal data, recommended values, layout rules, JLC/LCSC availability | VERIFIED_FOR_PLANNING; sourcing NEEDS_REVIEW |
| Buck inductor | Final shielded inductor MPN not selected | Must be 3.9 uH for AP63203 baseline; confirm current rating, saturation current, DCR < 100 milliohm target, shielded construction, package, height, JLC/LCSC availability | NEEDS_REVIEW |
| Buck capacitors | Final MLCC MPNs not selected | Confirm 10 uF VIN, 2 x 22 uF VOUT, 100 nF BST, voltage rating, X5R/X7R dielectric, DC-bias derating, package, placement | NEEDS_REVIEW |
| USB-C receptacle | GCT `USB4105`: https://gct.co/files/specs/usb4105-spec.pdf | Confirm exact suffix, footprint, shell stake length, top/mid mount, current ratings, durability, enclosure alignment, JLC/LCSC availability | NEEDS_REVIEW |
| USB-C CC resistors | Espressif USB Type-C guide: https://docs.espressif.com/projects/esp-iot-solution/en/latest/usb/usb_overview/usb_typec_hardware_guide.html | Use one 5.1 k Rd from CC1 to GND and one 5.1 k Rd from CC2 to GND for sink behavior | VERIFIED_FOR_PLANNING |
| USB ESD | TI `TPD2EUSB30`: https://www.ti.com/product/TPD2EUSB30 | Confirm package, pinout, capacitance, working voltage, clamp behavior, layout close to connector, JLC/LCSC availability | NEEDS_REVIEW |
| USB series resistors | Espressif ESP32-S3 schematic checklist | Use 22 ohm or 33 ohm in series with USB D+ and D-, close to module; choose exact value during schematic review | VERIFIED_RANGE |
| USB shunt capacitor footprints | Espressif ESP32-S3 schematic checklist | Reserve footprints to GND on D+ and D-; default DNI unless testing/reference design confirms value | NEEDS_REVIEW |
| USB power path | No final source selected | Decide data-only USB requiring barrel power, USB-powered option, or protected dual-source power path; never directly backfeed host or barrel supply | NEEDS_REVIEW |
| USB shield | Connector datasheet plus EMC strategy | Confirm direct-to-GND, RC/capacitor, ESD/chassis strategy, or selectable footprint based on enclosure and EMC approach | NEEDS_REVIEW |
| RESET switch | Final tactile switch MPN not selected | Confirm switch package, actuation force, lifecycle, footprint, orientation, enclosure access; circuit uses EN to GND with 10 k pull-up and 1 uF cap | Switch NEEDS_REVIEW; circuit verified |
| BOOT switch | Final tactile switch MPN not selected | Confirm switch package, footprint, enclosure access; circuit uses GPIO0 to GND with 10 k pull-up and no large GPIO0 capacitance | Switch NEEDS_REVIEW; circuit verified |
| Power LED | Final LED MPN not selected | Confirm color, Vf, luminous intensity, viewing angle, current target, 2.2 k default resistor, enclosure visibility | NEEDS_REVIEW |
| Status LED | Final LED MPN not selected | Confirm GPIO assignment, LED color, active-high/active-low convention, 2.2 k default resistor, firmware expectations | NEEDS_REVIEW |
| RGB LED | Not selected for revision A | Reopen only if RGB status is a real requirement; confirm power, timing, level, ESD, firmware, and cost if added | NOT_SELECTED |
| Test pads | Final footprints not selected | Confirm pad size, soldermask, labels, probe access, placement, and whether USB D+/D- pads create unacceptable stubs | NEEDS_REVIEW |
| Mounting holes | M2.5 planning default | Confirm 2.7 mm NPTH drill, copper keepout, standoff diameter, washer clearance, board corner radius, enclosure dimensions; consider M3 if board size allows | NEEDS_REVIEW |
| Silkscreen markings | Project requirements | Confirm center-positive symbol, `5V DC ONLY`, connector labels, BOOT/RESET labels, antenna clearance notes, pin labels for test pads | NEEDS_REVIEW during schematic/layout |

## Datasheets Still Needed Locally

- Espressif ESP32-S3-WROOM-1 / WROOM-1U datasheet.
- Espressif ESP32-S3 hardware design guidelines.
- Diodes AP63203 datasheet.
- Final barrel jack datasheet and footprint drawing.
- Final PTC datasheet.
- Final reverse-polarity MOSFET datasheet.
- Final 5 V TVS datasheet.
- Final AP63203 inductor datasheet.
- Final AP63203 capacitor datasheets or verified MLCC derating data.
- Final USB-C receptacle datasheet and footprint drawing.
- Final USB ESD datasheet.
- Final tactile switch datasheet.
- Final LED datasheets.
- Final U.FL/MHF I pigtail, SMA bulkhead, and antenna datasheets.
- Final mounting hardware or enclosure mechanical drawing.
