# ESP32_CSI_WIFI_NODE Project Memory

Durable project decisions, constraints, and preferences belong here.

Do not store command logs or secrets in this file.

## Project Status

- Created: 2026-05-02.
- Status: active design project with rough schematic draft.
- Active project path: `C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE`
- KiCad source status: rough draft KiCad project and schematic created under `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad`. No PCB layout, Gerbers, or manufacturing outputs have been created.

## Durable Design Decisions

- This is one complete custom PCB with an ESP32-S3 module soldered directly to the PCB.
- This is not a carrier board and not a board for plugging in an ESP32 development board.
- Do not use a bare ESP32-S3 chip for this revision.
- Preferred module: `ESP32-S3-WROOM-1U-N16R8`.
- Acceptable alternate module: `ESP32-S3-WROOM-1U-N8R8`.
- Use the WROOM-1U external antenna variant with U.FL/IPEX-to-SMA pigtail support for a screw-on 2.4 GHz enclosure antenna.
- Do not include 120 VAC on the PCB.
- Use an external certified 5 V DC wall power supply.
- Use a 5.5 mm x 2.1 mm center-positive DC barrel jack for power input.
- Include input fuse/polyfuse, reverse-polarity protection, 5 V TVS protection, bulk input capacitance, and a 3.3 V regulator.
- Include USB-C for programming/debug and USB ESD protection.
- Include BOOT and RESET / EN buttons.
- Include a power LED and either a status LED or RGB LED.
- Include 5 V, 3.3 V, and GND test pads.
- Use a compact rectangular board with four corner mounting holes.
- Place barrel jack and USB-C for enclosure-wall access.
- Reserve mechanical clearance for antenna pigtail, SMA hardware, connector plugs, mounting hardware, and 3D printed enclosure features.

## Verification Rules

- Do not create or edit KiCad design files until the active project and backup plan are confirmed for that specific task.
- Run ERC after schematic creation or any schematic edit.
- Run DRC after PCB creation or any PCB edit.
- Treat all manufacturing-style outputs as `NOT_FINAL` until ERC, DRC, BOM, footprint, netlist, datasheet, connector, polarity/orientation, power/protection, antenna/mechanical, and visual review gates pass.

## Open Requirements

- Exact board dimensions and enclosure internal dimensions.
- Layer count, stackup, and fab house.
- 3.3 V regulator topology and current/thermal target.
- USB debug architecture: native USB versus USB-to-UART bridge.
- USB power/backfeed policy.
- Status LED versus RGB LED.
- Mounting hole diameter, screw size, and standoff keepout.
- Antenna pigtail length, SMA bulkhead style, and enclosure wall geometry.

## Component Selection Review - 2026-05-02

- Component research report created at `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\COMPONENT_SELECTION_REPORT.md`.
- Datasheet checklist created at `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\DATASHEET_CHECKLIST.md`.
- Primary ESP32 module remains `ESP32-S3-WROOM-1U-N16R8`.
- Acceptable ESP32 alternate remains `ESP32-S3-WROOM-1U-N8R8`.
- Use native ESP32-S3 USB for revision A schematic planning. GPIO19 is USB D- and GPIO20 is USB D+.
- Do not add a USB-to-UART bridge unless a later requirement makes it necessary.
- Preferred 3.3 V regulator topology is a buck regulator, not a 5 V to 3.3 V linear regulator, because WiFi current peaks and enclosed operation make LDO heat unattractive.
- Selected regulator candidate for schematic planning: Diodes `AP63203WU-7`, fixed 3.3 V, 2 A, TSOT26.
- AP63203 verified planning values: 3.9 uH inductor, 10 uF input capacitor, 2 x 22 uF output capacitors, and 100 nF bootstrap capacitor.
- EN / reset planning circuit: 10 k pull-up to 3.3 V, 1 uF capacitor to GND, RESET button to GND.
- BOOT planning circuit: GPIO0 with 10 k pull-up to 3.3 V and BOOT button to GND; avoid high-value capacitance on GPIO0.
- USB-C sink CC planning values: 5.1 k from CC1 to GND and 5.1 k from CC2 to GND.
- USB D+/D- planning values: 22 ohm or 33 ohm series resistors near the module side; reserve capacitor footprints to GND as DNI/NEEDS_REVIEW.
- Prefer a simple single-color GPIO status LED for revision A. Do not use WS2812/RGB unless the user explicitly adds RGB indication as a real requirement.
- Use test pads for 5V, 3V3, GND, EN, BOOT/GPIO0, U0TXD/GPIO43, and U0RXD/GPIO44. USB D+/D- pads are optional and must avoid harmful stubs.
- Default mounting assumption is M2.5 hardware with 2.7 mm NPTH holes and 5.5 mm to 6.0 mm keepout, pending enclosure confirmation.
- Candidate input protection stack is resettable PTC, P-channel MOSFET reverse-polarity protection, 5 V TVS, and board-level bulk capacitance.
- Candidate parts needing final review include an exact 5.5 mm OD / 2.1 mm ID right-angle through-hole barrel jack MPN, Littelfuse `1206L110THYR` class PTC, AO3401A class P-channel MOSFET, Littelfuse `SMAJ5.0A` class TVS, GCT `USB4105` class USB-C receptacle, and TI `TPD2EUSB30` class USB ESD.

### Open Requirements After Component Review

- Confirm USB power policy: barrel-only, USB-powered, or protected dual-source. Do not directly tie USB VBUS to the barrel 5 V rail without a reviewed power path.
- Confirm final current budget and PTC hold/trip current under enclosure temperature.
- Confirm final JLCPCB/LCSC availability for all candidates.
- Confirm all connector, module, regulator, switch, LED, pigtail, SMA, antenna, and mounting footprints against manufacturer drawings.
- Confirm exact input bulk capacitor value, ESR, voltage rating, derating, and inrush behavior.
- Confirm USB shield grounding strategy.
- Confirm board dimensions, mounting hardware, connector placement, antenna pigtail length, SMA bulkhead style, and enclosure wall geometry.

## Rough Schematic Draft - 2026-05-02

- Rough draft KiCad project file: `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pro`.
- Rough draft schematic: `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch`.
- ERC report: `02_HISTORY\erc_drc_reports\ESP32_CSI_WIFI_NODE_SCHEMATIC_DRAFT_ERC.txt`.
- Design review: `02_HISTORY\design_reviews\ESP32_CSI_WIFI_NODE_SCHEMATIC_DRAFT_REVIEW.md`.
- Backup/snapshot before KiCad source creation: `99_BACKUPS\pre_codex_edits\ESP32_CSI_WIFI_NODE_SCHEMATIC_DRAFT_20260502_143643`.
- The schematic is a readable first draft only. It is not ERC-clean, not layout-ready, and not fabrication-ready.
- USB VBUS remains intentionally not tied to the board 5 V rail pending a reviewed USB power/backfeed policy.
- No PCB layout, footprints, Gerbers, BOM release, or manufacturing outputs were generated.
