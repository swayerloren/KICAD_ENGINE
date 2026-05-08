# Sample Candidate Record - STM32L0 ESP32 Breakout Board

Status: `CANDIDATE_LINK_ONLY`

## Required Fields

| Field | Value |
|---|---|
| Project name | STM32L0 ESP32 Breakout Board |
| Source URL | https://github.com/mohamedyanis/STM32L0-ESP32-Breakout-Board |
| Source host | GitHub |
| Source owner | mohamedyanis |
| License found | BSD 3-Clause License, file path `LICENSE` |
| License confidence | HIGH, GitHub license metadata and license file content checked |
| Includes `.kicad_pro` | Yes, 1 found |
| Includes `.kicad_sch` | Yes, 1 found |
| Includes `.kicad_pcb` | Yes, 1 found |
| Includes BOM | Yes, 1 BOM-like file found |
| Includes Gerbers | Yes, 18 fabrication/Gerber-like files found |
| Includes 3D/STEP | Yes, 1 STEP file found |
| Project category | STM32L0 plus ESP32 breakout / mixed MCU board |
| Complexity level | Medium |
| Public bundle status | `PUBLIC_BUNDLE_ALLOWED` pending attribution preservation and final human license review |
| Recommended action | Good second-wave candidate; not first import because it mixes STM32 and ESP32 assumptions |

## Evidence Checked

- Repository page: https://github.com/mohamedyanis/STM32L0-ESP32-Breakout-Board
- GitHub metadata/file-tree check found `STM32L0_ESP32_Breakout_Board.kicad_pro`, `.kicad_sch`, and `.kicad_pcb`.
- GitHub license metadata identified BSD-3-Clause.

## Why It Is Useful

This is a complete mixed STM32 and ESP32 board with BOM-like files, fabrication outputs, and STEP. It can exercise multi-MCU schematic review, regulator/input-power checks, and BOM/source alignment.

## Risks And Review Notes

- It is more complex than a beginner fixture because it combines two MCU ecosystems.
- Verify bundled STEP and any third-party library/material licensing before public payload inclusion.
- Treat generated outputs as historical source artifacts only.
