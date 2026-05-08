# Close-Up Schematic Visual Review

Status: `PASS`

Generated: `2026-05-03T15:00:49`
Source SVG: `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\_verification\schematic_visual\full_page\attiny85.svg`
Config: `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\_verification\schematic_visual\visual_blocks.json`
Crops folder: `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\_verification\schematic_visual\crops`
Full-page PNG: `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\_verification\schematic_visual\full_page\attiny85.png`

## Summary

- Blocks configured: 13
- Crops generated: 13
- PNG crops generated: 13
- Blocks with unannotated visible references: 0
- Blocks with visible footprint/library-field risks: 0
- Renderer: `browser renderer completed`

## Block Table

| Block | Status | SVG Crop | PNG Crop | Visible unannotated refs | Visible field risks | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `input_power` | `PASS` | `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\_verification\schematic_visual\crops\input_power.svg` | `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\_verification\schematic_visual\crops\input_power.png` | None detected | None detected | Review USB-A VBUS/GND input and shield policy. Shield remains ERC-blocked until accepted or connected. |
| `reverse_polarity` | `PASS` | `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\_verification\schematic_visual\crops\reverse_polarity.svg` | `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\_verification\schematic_visual\crops\reverse_polarity.png` | None detected | None detected | This sample has no explicit reverse-polarity circuit. Treat as not applicable for demo unless a human requires it. |
| `tvs_input_cap` | `PASS` | `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\_verification\schematic_visual\crops\tvs_input_cap.svg` | `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\_verification\schematic_visual\crops\tvs_input_cap.png` | None detected | None detected | Review D1/D2 zener clamp and USB data-line protection intent. Exact diode MPN is not verified. |
| `buck_regulator` | `PASS` | `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\_verification\schematic_visual\crops\buck_regulator.svg` | `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\_verification\schematic_visual\crops\buck_regulator.png` | None detected | None detected | Review U2 AMS1117 schematic and note that package/source verification is blocked for human review. |
| `esp32_module` | `PASS` | `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\_verification\schematic_visual\crops\esp32_module.svg` | `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\_verification\schematic_visual\crops\esp32_module.png` | None detected | None detected | Review U1 ATtiny85 minimum wiring. Name retained for pipeline compatibility. |
| `usb_c_connector` | `PASS` | `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\_verification\schematic_visual\crops\usb_c_connector.svg` | `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\_verification\schematic_visual\crops\usb_c_connector.png` | None detected | None detected | Review J1 USB-A custom Molex footprint assignment and pin/shield handling. Name retained for pipeline compatibility. |
| `usb_esd` | `PASS` | `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\_verification\schematic_visual\crops\usb_esd.svg` | `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\_verification\schematic_visual\crops\usb_esd.png` | None detected | None detected | Review USB data protection topology. Exact protection diode datasheets are not verified. |
| `cc_resistors` | `PASS` | `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\_verification\schematic_visual\crops\cc_resistors.svg` | `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\_verification\schematic_visual\crops\cc_resistors.png` | None detected | None detected | Review R2/R3 USB data resistor area. Name retained for pipeline compatibility. |
| `reset_boot` | `PASS` | `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\_verification\schematic_visual\crops\reset_boot.svg` | `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\_verification\schematic_visual\crops\reset_boot.png` | None detected | None detected | Review J2 header pinout and reset/programming access. Connector pinout remains human-review-blocked. |
| `leds` | `PASS` | `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\_verification\schematic_visual\crops\leds.svg` | `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\_verification\schematic_visual\crops\leds.png` | None detected | None detected | Review D3/D4 and R4/R5 LED areas. |
| `test_pads` | `PASS` | `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\_verification\schematic_visual\crops\test_pads.svg` | `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\_verification\schematic_visual\crops\test_pads.png` | None detected | None detected | The sample uses the programming header rather than discrete test pads. |
| `mounting_holes` | `PASS` | `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\_verification\schematic_visual\crops\mounting_holes.svg` | `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\_verification\schematic_visual\crops\mounting_holes.png` | None detected | None detected | No explicit schematic mounting-hole symbols were detected. PCB visual review must confirm whether holes are intentionally absent. |
| `mechanical_notes` | `PASS` | `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\_verification\schematic_visual\crops\mechanical_notes.svg` | `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\_verification\schematic_visual\crops\mechanical_notes.png` | None detected | None detected | Review title block/source context. This does not replace license/attribution records. |

## Crop Review Sections

Each crop must be reviewed by a human or an agent using visual evidence. Mark every section `PASS`, `FAIL`, or `NEEDS_REVIEW` in the project gate file.

### USB-A Power Input

- Block name: `input_power`
- Status: `PASS`
- SVG crop: `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\_verification\schematic_visual\crops\input_power.svg`
- PNG crop: `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\_verification\schematic_visual\crops\input_power.png`
- Visible unannotated refs: None detected
- Visible footprint/library fields: None detected
- Human visual result: `NOT_REVIEWED`
- Notes:

![USB-A Power Input](C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\_verification\schematic_visual\crops\input_power.png)

### Input Protection Presence

- Block name: `reverse_polarity`
- Status: `PASS`
- SVG crop: `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\_verification\schematic_visual\crops\reverse_polarity.svg`
- PNG crop: `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\_verification\schematic_visual\crops\reverse_polarity.png`
- Visible unannotated refs: None detected
- Visible footprint/library fields: None detected
- Human visual result: `NOT_REVIEWED`
- Notes:

![Input Protection Presence](C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\_verification\schematic_visual\crops\reverse_polarity.png)

### USB Zener Clamp Area

- Block name: `tvs_input_cap`
- Status: `PASS`
- SVG crop: `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\_verification\schematic_visual\crops\tvs_input_cap.svg`
- PNG crop: `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\_verification\schematic_visual\crops\tvs_input_cap.png`
- Visible unannotated refs: None detected
- Visible footprint/library fields: None detected
- Human visual result: `NOT_REVIEWED`
- Notes:

![USB Zener Clamp Area](C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\_verification\schematic_visual\crops\tvs_input_cap.png)

### AMS1117 Regulator Area

- Block name: `buck_regulator`
- Status: `PASS`
- SVG crop: `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\_verification\schematic_visual\crops\buck_regulator.svg`
- PNG crop: `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\_verification\schematic_visual\crops\buck_regulator.png`
- Visible unannotated refs: None detected
- Visible footprint/library fields: None detected
- Human visual result: `NOT_REVIEWED`
- Notes:

![AMS1117 Regulator Area](C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\_verification\schematic_visual\crops\buck_regulator.png)

### ATtiny85 MCU Area

- Block name: `esp32_module`
- Status: `PASS`
- SVG crop: `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\_verification\schematic_visual\crops\esp32_module.svg`
- PNG crop: `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\_verification\schematic_visual\crops\esp32_module.png`
- Visible unannotated refs: None detected
- Visible footprint/library fields: None detected
- Human visual result: `NOT_REVIEWED`
- Notes:

![ATtiny85 MCU Area](C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\_verification\schematic_visual\crops\esp32_module.png)

### USB-A Connector

- Block name: `usb_c_connector`
- Status: `PASS`
- SVG crop: `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\_verification\schematic_visual\crops\usb_c_connector.svg`
- PNG crop: `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\_verification\schematic_visual\crops\usb_c_connector.png`
- Visible unannotated refs: None detected
- Visible footprint/library fields: None detected
- Human visual result: `NOT_REVIEWED`
- Notes:

![USB-A Connector](C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\_verification\schematic_visual\crops\usb_c_connector.png)

### USB Data Protection

- Block name: `usb_esd`
- Status: `PASS`
- SVG crop: `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\_verification\schematic_visual\crops\usb_esd.svg`
- PNG crop: `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\_verification\schematic_visual\crops\usb_esd.png`
- Visible unannotated refs: None detected
- Visible footprint/library fields: None detected
- Human visual result: `NOT_REVIEWED`
- Notes:

![USB Data Protection](C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\_verification\schematic_visual\crops\usb_esd.png)

### USB Data Resistors

- Block name: `cc_resistors`
- Status: `PASS`
- SVG crop: `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\_verification\schematic_visual\crops\cc_resistors.svg`
- PNG crop: `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\_verification\schematic_visual\crops\cc_resistors.png`
- Visible unannotated refs: None detected
- Visible footprint/library fields: None detected
- Human visual result: `NOT_REVIEWED`
- Notes:

![USB Data Resistors](C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\_verification\schematic_visual\crops\cc_resistors.png)

### Programming Header And Reset

- Block name: `reset_boot`
- Status: `PASS`
- SVG crop: `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\_verification\schematic_visual\crops\reset_boot.svg`
- PNG crop: `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\_verification\schematic_visual\crops\reset_boot.png`
- Visible unannotated refs: None detected
- Visible footprint/library fields: None detected
- Human visual result: `NOT_REVIEWED`
- Notes:

![Programming Header And Reset](C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\_verification\schematic_visual\crops\reset_boot.png)

### Status LEDs

- Block name: `leds`
- Status: `PASS`
- SVG crop: `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\_verification\schematic_visual\crops\leds.svg`
- PNG crop: `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\_verification\schematic_visual\crops\leds.png`
- Visible unannotated refs: None detected
- Visible footprint/library fields: None detected
- Human visual result: `NOT_REVIEWED`
- Notes:

![Status LEDs](C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\_verification\schematic_visual\crops\leds.png)

### Accessible Test And Programming Points

- Block name: `test_pads`
- Status: `PASS`
- SVG crop: `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\_verification\schematic_visual\crops\test_pads.svg`
- PNG crop: `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\_verification\schematic_visual\crops\test_pads.png`
- Visible unannotated refs: None detected
- Visible footprint/library fields: None detected
- Human visual result: `NOT_REVIEWED`
- Notes:

![Accessible Test And Programming Points](C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\_verification\schematic_visual\crops\test_pads.png)

### Mechanical Mounting Review

- Block name: `mounting_holes`
- Status: `PASS`
- SVG crop: `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\_verification\schematic_visual\crops\mounting_holes.svg`
- PNG crop: `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\_verification\schematic_visual\crops\mounting_holes.png`
- Visible unannotated refs: None detected
- Visible footprint/library fields: None detected
- Human visual result: `NOT_REVIEWED`
- Notes:

![Mechanical Mounting Review](C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\_verification\schematic_visual\crops\mounting_holes.png)

### Schematic Notes And Title Area

- Block name: `mechanical_notes`
- Status: `PASS`
- SVG crop: `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\_verification\schematic_visual\crops\mechanical_notes.svg`
- PNG crop: `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\_verification\schematic_visual\crops\mechanical_notes.png`
- Visible unannotated refs: None detected
- Visible footprint/library fields: None detected
- Human visual result: `NOT_REVIEWED`
- Notes:

![Schematic Notes And Title Area](C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\_verification\schematic_visual\crops\mechanical_notes.png)

## Limits

- This report detects visible text in the SVG; it is not OCR for arbitrary raster images.
- Close-up crops do not prove electrical correctness, footprint correctness, connector orientation, ERC, DRC, or fabrication readiness.
- If a crop misses the intended block, adjust `_verification/schematic_visual/visual_blocks.json` and regenerate.
