# Sample Candidate Record - Mitayi Pico D1

Status: `CANDIDATE_LINK_ONLY`

## Required Fields

| Field | Value |
|---|---|
| Project name | Mitayi Pico D1 |
| Source URL | https://github.com/CIRCUITSTATE/Mitayi-Pico-D1 |
| Source host | GitHub |
| Source owner | CIRCUITSTATE |
| License found | MIT License, file path `LICENSE` |
| License confidence | HIGH, GitHub license metadata and license file content checked |
| Includes `.kicad_pro` | Yes, 8 found across current and revision folders |
| Includes `.kicad_sch` | Yes, 8 found |
| Includes `.kicad_pcb` | Yes, 8 found |
| Includes BOM | Yes, 48 BOM-like files found |
| Includes Gerbers | Yes, 509 fabrication/Gerber-like files found |
| Includes 3D/STEP | Yes, 13 STEP files found |
| Project category | RP2040 development board |
| Complexity level | Medium |
| Public bundle status | `PUBLIC_BUNDLE_ALLOWED` pending attribution preservation and final human license review |
| Recommended action | `TOP_5_CANDIDATE`; good first import if revision/output pruning is handled carefully |

## Evidence Checked

- Repository page: https://github.com/CIRCUITSTATE/Mitayi-Pico-D1
- GitHub metadata/file-tree check found current KiCad project files plus multiple revision folders.
- GitHub license metadata identified MIT License.

## Why It Is Useful

This is a complete RP2040 development-board project with current and historical revisions, BOM-like outputs, STEP files, and fabrication outputs. It can test sample normalization, revision selection, BOM review, and RP2040 schematic/PCB checks.

## Risks And Review Notes

- The repository contains many revision and generated-output files; first import must choose one current project scope.
- Review payload size before bundling.
- Treat all fabrication outputs as source evidence only, not final KiCad Engine outputs.
