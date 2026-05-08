# Sample Candidate Record - KiCad Official pic_programmer Demo

Status: `CANDIDATE_LINK_ONLY`

## Required Fields

| Field | Value |
|---|---|
| Project name | KiCad official `pic_programmer` demo |
| Source URL | https://github.com/KiCad/kicad-source-mirror/tree/master/demos/pic_programmer |
| Source host | GitHub mirror of upstream KiCad source |
| Source owner | KiCad |
| License found | Parent repository GitHub metadata reports GPL-3.0; subfolder license scope requires review |
| License confidence | MEDIUM, parent repo metadata and demo directory file listing checked |
| Includes `.kicad_pro` | Yes, 1 found |
| Includes `.kicad_sch` | Yes, 2 found |
| Includes `.kicad_pcb` | Yes, 1 found |
| Includes BOM | No BOM-like file found by targeted directory check |
| Includes Gerbers | No Gerber-like files found by targeted directory check |
| Includes 3D/STEP | No STEP files found by targeted directory check |
| Project category | Official KiCad demo / small PIC programmer example |
| Complexity level | Low to medium |
| Public bundle status | `NEEDS_HUMAN_LICENSE_REVIEW` |
| Recommended action | Link-only official reference; do not import until license scope and bundling policy are reviewed |

## Evidence Checked

- Repository page: https://github.com/KiCad/kicad-source-mirror
- Demo directory checked through GitHub metadata: `demos/pic_programmer/pic_programmer.kicad_pro`, `.kicad_sch`, `.kicad_pcb`, child sheet, and project-local library files are present.
- Parent repository GitHub license metadata reports GPL-3.0.

## Why It Is Useful

This is an official KiCad demo that can help test project opening, simple hierarchical schematic handling, and compatibility with KiCad's own example style.

## Risks And Review Notes

- Because it lives inside the KiCad source monorepo with mixed licensing context, treat it as link-only until human license review.
- Do not copy the whole KiCad source repository.
- If imported later, import only the demo subfolder into `imported_originals/` with attribution and license context preserved.
