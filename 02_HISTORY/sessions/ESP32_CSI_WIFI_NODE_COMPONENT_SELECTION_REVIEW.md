# ESP32_CSI_WIFI_NODE Component Selection Review Session

Date: 2026-05-02

Workspace: `C:\Users\LJ\KICAD_ENGINE`

Active project: `ESP32_CSI_WIFI_NODE`

Active project path: `C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE`

## Scope

Performed component research and created a pre-schematic verified component plan for a complete custom ESP32-S3-WROOM-1U CSI WiFi node PCB.

No schematic, PCB layout, Gerbers, drill files, BOM release, or manufacturing outputs were created.

## Startup And Context

- Read root `AGENTS.md`.
- Read root startup files in the required order.
- Confirmed active project from `00_CODEX_START\CURRENT_PROJECT.md`.
- Read project requirements, design plan, component selection plan, project memory, and project-local `AGENTS.md`.
- Confirmed this project currently has documentation only and no KiCad source files requiring ERC/DRC.

## Backup

- Backed up existing planning files before edits to `99_BACKUPS\pre_codex_edits\ESP32_CSI_WIFI_NODE_COMPONENT_SELECTION_20260502_142743`.
- Backed up:
  - `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\COMPONENT_SELECTION_PLAN.md`
  - `01_MEMORY\projects\ESP32_CSI_WIFI_NODE\PROJECT_MEMORY.md`

## Sources Used

- Espressif ESP32-S3-WROOM-1 / ESP32-S3-WROOM-1U datasheet.
- Espressif ESP32-S3 hardware design guidelines, schematic checklist.
- Espressif ESP32-S3 hardware design guidelines, PCB layout design.
- Espressif USB Type-C hardware design guide.
- Diodes Incorporated AP63200/AP63201/AP63203/AP63205 datasheet.
- TI TPD2EUSB30 product page and datasheet link.
- GCT USB4105 USB-C receptacle specification.
- Same Sky / CUI Devices PJ-102A datasheet, reviewed only as a right-angle through-hole barrel jack reference and not selected as the final 5.5 mm x 2.1 mm MPN.
- Littelfuse 1206L110THYR product page and 1206L series data.
- Littelfuse SMAJ5.0A product page.
- Alpha and Omega Semiconductor AO3401A product page and datasheet.

## Files Created

- `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\COMPONENT_SELECTION_REPORT.md`
- `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\DATASHEET_CHECKLIST.md`
- `02_HISTORY\sessions\ESP32_CSI_WIFI_NODE_COMPONENT_SELECTION_REVIEW.md`

## Files Updated

- `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\COMPONENT_SELECTION_PLAN.md`
- `01_MEMORY\projects\ESP32_CSI_WIFI_NODE\PROJECT_MEMORY.md`

## Key Component Decisions

- Primary module: `ESP32-S3-WROOM-1U-N16R8`.
- Alternate module: `ESP32-S3-WROOM-1U-N8R8`.
- Regulator candidate: Diodes `AP63203WU-7`, fixed 3.3 V, 2 A, TSOT26.
- Use native ESP32-S3 USB rather than a USB-to-UART bridge for revision A planning.
- Prefer simple single-color GPIO status LED over WS2812/RGB for revision A.
- Use input protection stack: PTC, P-channel MOSFET reverse-polarity protection, 5 V TVS, and bulk input capacitance.

## Values Selected

- ESP32 module rail: 3.3 V nominal, valid module range 3.0 V to 3.6 V.
- 3.3 V regulator current target: at least 1 A practical margin; selected regulator is 2 A.
- AP63203 inductor: 3.9 uH.
- AP63203 input capacitor: 10 uF.
- AP63203 output capacitors: 2 x 22 uF.
- AP63203 bootstrap capacitor: 100 nF.
- EN pull-up: 10 k.
- EN capacitor: 1 uF.
- BOOT / GPIO0 pull-up: 10 k.
- USB-C CC resistors: 5.1 k on CC1 and 5.1 k on CC2.
- USB D+/D- series resistors: 22 ohm or 33 ohm.
- Power LED planning resistor: 2.2 k.
- Status LED planning resistor: 2.2 k.
- UART0 TX series resistor if routed off-board: 499 ohm.
- Mounting hole planning default: M2.5 with 2.7 mm NPTH drill.

## Remaining NEEDS_REVIEW Items

- USB power/backfeed policy.
- Final current budget and PTC hold/trip current under temperature.
- Final barrel jack mating compatibility with 5.5 mm x 2.1 mm center-positive adapters.
- Reverse-polarity MOSFET orientation, gate network, and final part.
- 5 V TVS leakage/clamp/package choice.
- Input bulk capacitance value, ESR, package, voltage rating, and inrush behavior.
- AP63203 inductor and MLCC manufacturer part numbers.
- USB-C receptacle exact suffix, footprint, and enclosure alignment.
- USB ESD final package and sourcing.
- USB shield grounding strategy.
- Switch, LED, test pad, pigtail, SMA bulkhead, antenna, mounting hardware, and enclosure mechanical details.
- JLCPCB/LCSC availability for all selected candidates.

## Verification Notes

- ERC not run because no schematic exists.
- DRC not run because no PCB layout exists.
- No KiCad design source files were created or modified.
- No manufacturing output was created.
