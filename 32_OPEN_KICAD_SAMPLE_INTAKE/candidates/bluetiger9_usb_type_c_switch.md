# Sample Candidate Record - USB Type-C Switch

Status: `CANDIDATE_LINK_ONLY`

## Required Fields

| Field | Value |
|---|---|
| Project name | USB Type-C Switch |
| Source URL | https://github.com/bluetiger9/USB-Type-C-Switch |
| Source host | GitHub |
| Source owner | bluetiger9 |
| License found | MIT License, file path `LICENSE` |
| License confidence | HIGH, GitHub license metadata and license file content checked |
| Includes `.kicad_pro` | Yes, 1 found |
| Includes `.kicad_sch` | Yes, 5 found |
| Includes `.kicad_pcb` | Yes, 1 found |
| Includes BOM | Yes, 1 BOM-like file found |
| Includes Gerbers | Yes, 19 fabrication/Gerber-like files found |
| Includes 3D/STEP | No STEP files found by metadata scan |
| Project category | USB-C device / USB-C switching / high-speed interface |
| Complexity level | High |
| Public bundle status | `PUBLIC_BUNDLE_ALLOWED` pending attribution preservation and final human license review |
| Recommended action | `TOP_5_CANDIDATE`; defer first import until simpler samples pass |

## Evidence Checked

- Repository page: https://github.com/bluetiger9/USB-Type-C-Switch
- GitHub metadata/file-tree check found `KiCad/USB-TypeC-Switch.kicad_pro`, root sheet, four hierarchical sheets, and PCB.
- GitHub license metadata identified MIT License.

## Why It Is Useful

This is a complete USB Type-C switch project with hierarchical KiCad sheets and fabrication outputs. It is useful for testing USB-C rules, connector orientation review, high-speed routing review, hierarchical schematic parsing, and warning against false confidence.

## Risks And Review Notes

- High-speed USB-C switching is not beginner-level. Do not use as the first import unless the goal is a difficult review fixture.
- Connector orientation, CC policy, shielding, ESD, impedance, and assembly details require human review.
- Treat included Gerbers as source evidence only.
