# Sample Candidate Record - candleLight FD

Status: `CANDIDATE_LINK_ONLY`

## Required Fields

| Field | Value |
|---|---|
| Project name | candleLight FD |
| Source URL | https://github.com/linux-automation/candleLightFD |
| Source host | GitHub |
| Source owner | linux-automation |
| License found | CERN Open Hardware Licence v1.2, file path `LICENSE` |
| License confidence | HIGH, license file content and repository tree checked |
| Includes `.kicad_pro` | Yes, 2 found including panel/release project |
| Includes `.kicad_sch` | Yes, 4 found |
| Includes `.kicad_pcb` | Yes, 2 found |
| Includes BOM | Yes, 7 BOM-like files found |
| Includes Gerbers | Yes, 36 fabrication/Gerber-like files found |
| Includes 3D/STEP | No STEP files found by metadata scan |
| Project category | STM32G0, USB CAN-FD interface, CAN bus |
| Complexity level | Medium |
| Public bundle status | `PUBLIC_BUNDLE_ALLOWED` pending attribution preservation and final human license review |
| Recommended action | `TOP_5_CANDIDATE`; recommended for later import after one smaller fixture |

## Evidence Checked

- Repository page: https://github.com/linux-automation/candleLightFD
- Search result and metadata show `candleLightfd-S01.kicad_pro`, `.kicad_sch`, `.kicad_pcb`, plus `MCU.kicad_sch`, `PSU.kicad_sch`, and `transceiver.kicad_sch`.
- GitHub license metadata returned `NOASSERTION / Other`; license file content identified CERN-OHL v1.2 text.

## Why It Is Useful

This is a real STM32G0 CAN-FD board with hierarchical schematic sheets, USB interface, power supply section, transceiver section, BOM-like files, and fabrication outputs. It is an excellent candidate for CAN, STM32, USB, and manufacturing-output review gates.

## Risks And Review Notes

- CAN transceiver orientation, connector pinout, ESD/protection, USB, and firmware assumptions require review.
- Generated release and panel files should not be treated as KiCad Engine outputs.
- Public bundling must preserve CERN-OHL attribution and source license.
