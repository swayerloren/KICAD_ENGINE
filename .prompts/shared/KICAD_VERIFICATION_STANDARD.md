# KiCad Verification Standard

Use this standard for all KiCad project validation, review, export, and release tasks.

## Minimum Review Gate

A project is not fabrication-ready until these are complete:

- Project validation report.
- ERC.
- DRC.
- BOM review.
- Symbol-to-datasheet review.
- Footprint-to-package-drawing review.
- Schematic-to-PCB comparison.
- Connector pinout and orientation review.
- Polarity and assembly orientation review.
- 3D/mechanical review where relevant.
- Fab output review against target board-house requirements.
- Human review of high-risk assumptions.

## Recommended Scripts

- `03_TOOLS/scripts/project_validation/validate_kicad_project.ps1`
- `03_TOOLS/scripts/run_erc.ps1`
- `03_TOOLS/scripts/run_drc.ps1`
- `03_TOOLS/scripts/export_bom.ps1`
- `03_TOOLS/scripts/export_gerbers.ps1`
- `03_TOOLS/scripts/export_drill.ps1`
- `03_TOOLS/scripts/export_step.ps1`

## Output Rules

- Write validation reports under `05_OUTPUTS/project_validation` or `02_HISTORY`.
- Write ERC/DRC reports under `02_HISTORY/erc_drc_reports` or approved output folders.
- Write manufacturing-style outputs to timestamped `NOT_FINAL` folders.
- Do not overwrite prior outputs.
- Do not label outputs final unless the user explicitly approves the complete evidence package.

## Review Language

- `PASS` means only the checked scope passed.
- `WARN` means unresolved review work remains.
- `FAIL` means a blocker or missing artifact exists.
- `HUMAN_REVIEW_REQUIRED` is the default classification for high-risk PCB outputs.
