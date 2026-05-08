# LJ Visual Review Checklist - ESP32_CSI_WIFI_NODE Schematic

Generated: 2026-05-06 15:51 -04:00  
Review packet: `reports/SCHEMATIC_HUMAN_REVIEW_PACKET.md`  
Final schematic status before LJ review: `SCHEMATIC_BLOCKED_NEEDS_HUMAN_REVIEW`

## Instructions

Open the full-page schematic export first, then review each close-up crop. Mark each item `PASS`, `FAIL`, or `NEEDS_REVIEW`. Any `FAIL` or unresolved high-risk `NEEDS_REVIEW` keeps PCB update blocked.

## Full-Page Review

Evidence:

- PDF: `_verification/schematic_visual/full_page/ESP32_CSI_WIFI_NODE.pdf`
- SVG: `_verification/schematic_visual/full_page/ESP32_CSI_WIFI_NODE.svg`
- PNG: `_verification/schematic_visual/full_page/ESP32_CSI_WIFI_NODE.png`

| Item | LJ result | Notes |
| --- | --- | --- |
| Schematic is readable as a whole page. | `NOT_REVIEWED` | |
| No text overlaps symbols, wires, net labels, or other text in a confusing way. | `NOT_REVIEWED` | |
| Reference designators are readable and not duplicated visually. | `NOT_REVIEWED` | |
| Values with `NEEDS_REVIEW` are intentional and visible enough for review. | `NOT_REVIEWED` | |
| No visible footprint/library/path fields clutter normal schematic view. | `NOT_REVIEWED` | |

## Block Review

| Block | Crop path | LJ result | What LJ should inspect |
| --- | --- | --- | --- |
| Input power | `_verification/schematic_visual/crops/input_power.png` | `NOT_REVIEWED` | Barrel jack polarity, `+5V_IN` label, fuse placement in schematic flow, GND connections, and whether value notes are acceptable. |
| Reverse polarity | `_verification/schematic_visual/crops/reverse_polarity.png` | `NOT_REVIEWED` | `Q1` PMOS intent, source/gate/drain naming, body diode direction, gate pull network, and whether AO3401A-class pin mapping remains blocked. |
| TVS and input capacitor | `_verification/schematic_visual/crops/tvs_input_cap.png` | `NOT_REVIEWED` | TVS placement relative to input/protection path, `C1` value `47uF_>=16V_BULK_NEEDS_REVIEW`, polarity/package assumptions, and rail label continuity. |
| Buck regulator | `_verification/schematic_visual/crops/buck_regulator.png` | `NOT_REVIEWED` | AP63203 wiring, input/output capacitors, bootstrap capacitor, inductor value/MPN review, feedback network, EN/PG/SW/BST pins, and `+3V3` output. |
| ESP32 module | `_verification/schematic_visual/crops/esp32_module.png` | `NOT_REVIEWED` | Module variant, 3V3 pins, EN, BOOT/GPIO0, USB pins, UART pins, antenna/module notes, and source-required items. |
| USB-C connector | `_verification/schematic_visual/crops/usb_c_connector.png` | `NOT_REVIEWED` | USB-C pin grouping, receptacle orientation assumptions, VBUS treatment, D+/D- pairing labels, shield net, and exact connector MPN still required. |
| USB ESD | `_verification/schematic_visual/crops/usb_esd.png` | `NOT_REVIEWED` | ESD diode array orientation/pinout, D+/D- in/out labels, GND connection, and whether selected part/package is still open. |
| CC resistors | `_verification/schematic_visual/crops/cc_resistors.png` | `NOT_REVIEWED` | CC1/CC2 resistor values and wiring for USB-C device/UFP behavior, and whether exact resistor/package/source is acceptable. |
| Reset and boot | `_verification/schematic_visual/crops/reset_boot.png` | `NOT_REVIEWED` | EN pull-up, EN capacitor if used, reset button behavior, BOOT/GPIO0 pull-up/button behavior, and ESP32 boot-mode correctness. |
| LEDs | `_verification/schematic_visual/crops/leds.png` | `NOT_REVIEWED` | Power LED polarity/current resistor, status LED polarity/current resistor, and whether `STATUS_LED_GPIO_NEEDS_REVIEW` should be assigned or removed. |
| Test pads | `_verification/schematic_visual/crops/test_pads.png` | `NOT_REVIEWED` | Test-pad list, labels, access intent, UART pads, EN/BOOT pads, 5V/3V3/GND pads, and whether USB D+/D- optional stubs should remain. |
| Mounting holes | `_verification/schematic_visual/crops/mounting_holes.png` | `NOT_REVIEWED` | Mounting-hole count, M2.5 NPTH 2.7 mm assumption, chassis/GND isolation intent, and whether enclosure dimensions are known. |
| Mechanical notes | `_verification/schematic_visual/crops/mechanical_notes.png` | `NOT_REVIEWED` | Mechanical constraints, board outline notes, connector edge assumptions, antenna keepout notes, and missing enclosure/board-size decisions. |

## High-Risk Electrical Decisions

| Decision | Current status | LJ result | Notes |
| --- | --- | --- | --- |
| AO3401A-class PMOS pin mapping and package orientation. | `BLOCKED` | `NOT_REVIEWED` | Must be resolved before PCB update. |
| USB VBUS/backfeed policy. | `NEEDS_HUMAN_REVIEW` | `NOT_REVIEWED` | Decide whether/how USB VBUS relates to protected 5V rail. |
| USB shield/EMC strategy. | `NEEDS_HUMAN_REVIEW` | `NOT_REVIEWED` | Confirm DNI/0R strategy or choose alternate network. |
| USB-C connector exact MPN and orientation. | `NEEDS_HUMAN_REVIEW` | `NOT_REVIEWED` | Must be matched to package drawing before footprint assignment. |
| ESP32-S3-WROOM-1U module footprint equivalence. | `NEEDS_HUMAN_REVIEW` | `NOT_REVIEWED` | Verify exact module land pattern and antenna keepout. |
| AP63203 regulator package/passives/layout requirements. | `NEEDS_HUMAN_REVIEW` | `NOT_REVIEWED` | Verify datasheet, MPNs, derating, and switcher layout constraints. |
| Inductor `L1` MPN/rating/package. | `NEEDS_HUMAN_REVIEW` | `NOT_REVIEWED` | Exact part required before layout. |
| Input capacitor `C1` value/voltage/package. | `NEEDS_HUMAN_REVIEW` | `NOT_REVIEWED` | Confirm `47uF >=16V` and package/technology. |
| Mounting holes and mechanical constraints. | `NEEDS_HUMAN_REVIEW` | `NOT_REVIEWED` | Board size/enclosure/hardware must be known before PCB. |

## Footprint/Package Review

Current footprint gate result: `FAIL`

| Item | Current status | LJ result | Notes |
| --- | --- | --- | --- |
| Every physical component has an assigned footprint. | `FAIL` | `NOT_REVIEWED` | 43 physical symbols have blank footprints. |
| Every footprint maps to exact manufacturer package drawing. | `FAIL` | `NOT_REVIEWED` | No package drawing evidence is recorded. |
| Connector orientation reviewed. | `FAIL` | `NOT_REVIEWED` | USB-C and barrel jack are high-risk. |
| Polarity-sensitive orientation reviewed. | `FAIL` | `NOT_REVIEWED` | PMOS, LEDs, TVS, ESD, regulator/package pinout need review. |
| Test pads and mounting holes selected. | `FAIL` | `NOT_REVIEWED` | Exact pad/hole footprints not assigned. |

## Required LJ Decision Before PCB Update

PCB update may proceed only if LJ or a later evidence-backed review resolves all blocking items and updates:

- `reports/SCHEMATIC_TO_PCB_GATE_STATUS.md` to `PASS`
- `reports/FOOTPRINT_PACKAGE_GATE_REPORT.md` with verified package/footprint evidence
- `reports/SCHEMATIC_ELECTRICAL_GATE_REPORT.md` with electrical blockers closed or accepted as non-blocking

Until then:

`PCB_UPDATE_BLOCKED`

