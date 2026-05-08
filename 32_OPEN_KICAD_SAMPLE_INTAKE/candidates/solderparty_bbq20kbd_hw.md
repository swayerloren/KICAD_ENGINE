# Sample Candidate Record - BBQ20 Keyboard Hardware

Status: `CANDIDATE_LINK_ONLY`

## Required Fields

| Field | Value |
|---|---|
| Project name | BBQ20 Keyboard Hardware |
| Source URL | https://github.com/solderparty/bbq20kbd_hw |
| Source host | GitHub |
| Source owner | solderparty |
| License found | CERN Open Hardware Licence v1.2, file path `LICENSE.md` |
| License confidence | HIGH, license file content and repository tree checked |
| Includes `.kicad_pro` | Yes, 1 found |
| Includes `.kicad_sch` | Yes, 2 found |
| Includes `.kicad_pcb` | Yes, 1 found |
| Includes BOM | Yes, 1 BOM-like file found |
| Includes Gerbers | No Gerber-like files found by metadata scan |
| Includes 3D/STEP | Yes, 3 STEP files found |
| Project category | RP2040 / keyboard / open hardware accessory |
| Complexity level | Medium |
| Public bundle status | `PUBLIC_BUNDLE_ALLOWED` pending attribution preservation and final human license review |
| Recommended action | Good second-wave import candidate |

## Evidence Checked

- Repository page: https://github.com/solderparty/bbq20kbd_hw
- GitHub metadata/file-tree check found `bbq20_keyboard.kicad_pro`, `.kicad_sch`, `.kicad_pcb`, a child schematic, BOM-like file, and STEP files.
- License file content identified CERN-OHL v1.2 text.

## Why It Is Useful

This is a complete open hardware KiCad design from a known open hardware vendor, with RP2040, keyboard/connector concerns, a BOM-like output, and STEP files. It is useful for connector, assembly, and mechanical-review workflows.

## Risks And Review Notes

- Keyboard/connector mechanical fit and orientation are high-risk review items.
- No Gerber-like files were found by metadata scan.
- Public bundling must preserve CERN-OHL license and attribution.
