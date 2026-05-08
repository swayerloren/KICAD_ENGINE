# Sample Candidate Record - esp-rs ESP Rust Board

Status: `CANDIDATE_LINK_ONLY`

## Required Fields

| Field | Value |
|---|---|
| Project name | ESP Rust Board |
| Source URL | https://github.com/esp-rs/esp-rust-board |
| Source host | GitHub |
| Source owner | esp-rs |
| License found | CERN Open Hardware Licence Version 2 - Permissive, file path `LICENSE-CERN-OHL` |
| License confidence | HIGH, license file content and GitHub repo metadata checked |
| Includes `.kicad_pro` | Yes, 1 found |
| Includes `.kicad_sch` | Yes, 1 found |
| Includes `.kicad_pcb` | Yes, 1 found |
| Includes BOM | Yes, 2 BOM-like files found |
| Includes Gerbers | Yes, 16 fabrication/Gerber-like files found |
| Includes 3D/STEP | Yes, 5 STEP files found |
| Project category | ESP32-C3, USB-C device, battery-powered development board |
| Complexity level | Medium |
| Public bundle status | `PUBLIC_BUNDLE_ALLOWED` pending attribution preservation and final human license review |
| Recommended action | `TOP_5_CANDIDATE`; recommended for first import after human license/attribution check |

## Evidence Checked

- Repository page: https://github.com/esp-rs/esp-rust-board
- GitHub metadata/file-tree check on 2026-05-03 found `hardware/esp-rust-board/esp-rust-board.kicad_pro`, `.kicad_sch`, and `.kicad_pcb`.
- GitHub license metadata returned `NOASSERTION / Other`; license file content identified CERN-OHL v2 permissive text.

## Why It Is Useful

This is a complete ESP32-C3 open hardware board with USB-C, battery charging, sensors, LEDs, buttons, BOM-like outputs, STEP files, and generated fabrication outputs. It is a strong benchmark for ESP32/USB-C/power-path review workflows.

## Risks And Review Notes

- Imported files must stay under `imported_originals/` and be copied to `normalized_samples/` before analysis.
- Treat generated Gerbers as historical source outputs, not approved KiCad Engine outputs.
- Verify all third-party symbols, footprints, 3D models, and linked datasheets before public bundling.
- Human review required before using it as a public benchmark fixture.
