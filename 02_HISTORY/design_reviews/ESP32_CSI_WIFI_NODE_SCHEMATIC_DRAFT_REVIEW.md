# ESP32_CSI_WIFI_NODE Schematic Draft Review

Date: 2026-05-02

Active project: `ESP32_CSI_WIFI_NODE`

Active project path: `C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE`

Reviewed schematic: `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch`

ERC report: `02_HISTORY\erc_drc_reports\ESP32_CSI_WIFI_NODE_SCHEMATIC_DRAFT_ERC.txt`

## Draft Scope

- Created a rough single-sheet KiCad schematic draft for a complete custom ESP32-S3 CSI WiFi node.
- This is not a carrier board and does not include an ESP32 development board.
- No PCB layout, final footprints, Gerbers, drill files, pick-and-place files, or manufacturing outputs were created.
- Schematic is not production-ready and must not be treated as fabrication-ready.

## Completed Blocks

- 5 V barrel jack input, polarity note, PTC fuse, PMOS reverse-polarity protection concept, 5 V TVS, and bulk input capacitor.
- AP63203WU-7 3.3 V buck regulator block with planned datasheet values: 3.9 uH, 10 uF input, 2 x 22 uF output, and 100 nF bootstrap.
- ESP32-S3-WROOM-1U-N16R8 module draft using KiCad `RF_Module:ESP32-S3-WROOM-1` symbol with value set to the preferred -1U module.
- EN/reset and BOOT/GPIO0 circuits.
- Native USB-C programming/debug concept with CC resistors, D+/D- series resistors, USB ESD, VBUS note, and shield strategy note.
- Power LED and simple status LED draft circuits.
- Test/debug pads for 5 V, 3.3 V, GND, EN, BOOT, UART0 TX/RX, and optional USB D+/D- review pads.
- Four mounting hole symbols and enclosure/antenna clearance notes.

## ERC Result

KiCad CLI command:

```powershell
kicad-cli sch erc --output 02_HISTORY\erc_drc_reports\ESP32_CSI_WIFI_NODE_SCHEMATIC_DRAFT_ERC.txt --format report 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch
```

Result:

- ERC completed.
- Messages: 6 total.
- Errors: 5.
- Warnings: 1.

Remaining ERC items:

- Power rails are missing explicit `PWR_FLAG` drivers for GND, protected +5 V, and +3.3 V.
- LED connection wires still need cleanup in KiCad so the rough indicator circuits are ERC-clean.
- AP63203WU cached symbol intentionally uses the AP63200WU pin-compatible base shape with AP63203 naming, causing one library mismatch warning.

## Values Still NEEDS_REVIEW

- Exact 5.5 mm x 2.1 mm barrel jack MPN and footprint.
- PTC hold/trip current, temperature derating, and exact footprint.
- PMOS reverse-polarity device, package, body-diode orientation, and gate protection.
- 5 V TVS exact MPN, package, leakage, and clamp behavior.
- Input bulk capacitor value, ESR, voltage rating, derating, and inrush behavior.
- AP63203 inductor MPN, saturation current, DCR, package, and thermal behavior.
- MLCC MPNs, voltage derating, and JLC/LCSC availability.
- USB-C receptacle MPN and footprint.
- USB VBUS/backfeed policy.
- USB shield grounding/EMC network.
- USB ESD exact MPN/package and placement.
- Final status LED GPIO assignment.
- ESP32-S3-WROOM-1U symbol/footprint equivalence against Espressif recommended land pattern.
- Antenna pigtail/SMA clearance, pigtail length, enclosure wall geometry, and antenna keepout.
- Mounting hole drill/keepout, board outline, and enclosure dimensions.

## Review Notes

- USB VBUS is intentionally not connected to board +5 V in this rough draft. The next schematic pass must choose barrel-only, USB-powered, or protected dual-source behavior.
- The schematic contains design notes instead of final footprints. Footprint assignment must wait for component MPN and mechanical verification.
- The ESP32 module power and native USB labels were corrected after the first ERC pass revealed generated-coordinate inversion.
- Do not start layout until ERC cleanup, component footprint verification, and mechanical outline assumptions are resolved.
