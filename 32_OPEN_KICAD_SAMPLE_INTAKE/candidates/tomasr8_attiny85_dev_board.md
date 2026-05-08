# Sample Candidate Record - ATtiny85 Dev Board

Status: `CANDIDATE_LINK_ONLY`

## Required Fields

| Field | Value |
|---|---|
| Project name | ATtiny85 Development Board |
| Source URL | https://github.com/tomasr8/attiny85-dev-board |
| Source host | GitHub |
| Source owner | tomasr8 |
| License found | MIT License, file path `LICENSE` |
| License confidence | HIGH, GitHub license metadata and license file content checked |
| Includes `.kicad_pro` | Yes, 1 found |
| Includes `.kicad_sch` | Yes, 1 found |
| Includes `.kicad_pcb` | Yes, 1 found |
| Includes BOM | No BOM-like file found by metadata scan |
| Includes Gerbers | Yes, 11 fabrication/Gerber-like files found |
| Includes 3D/STEP | No STEP files found by metadata scan |
| Project category | Small beginner-friendly microcontroller board |
| Complexity level | Low |
| Public bundle status | `PUBLIC_BUNDLE_ALLOWED` pending attribution preservation and final human license review |
| Recommended action | `TOP_5_CANDIDATE`; recommended for first import |

## Evidence Checked

- Repository page: https://github.com/tomasr8/attiny85-dev-board
- GitHub metadata/file-tree check found `attiny85.kicad_pro`, `.kicad_sch`, and `.kicad_pcb`.
- GitHub license metadata identified MIT License.

## Why It Is Useful

This is a small, complete KiCad project with schematic, PCB, and Gerber outputs. It is a practical first fixture for validating import, normalization, file audit, ERC/DRC setup, and visual review before attempting complex MCU or USB-C projects.

## Risks And Review Notes

- No BOM-like file was found by metadata scan.
- ATtiny reset/programming and connector assumptions still require review.
- Included Gerbers are historical source outputs, not KiCad Engine outputs.
