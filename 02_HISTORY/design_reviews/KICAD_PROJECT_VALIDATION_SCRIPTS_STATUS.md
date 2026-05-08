# KiCad Project Validation Scripts Status

Date: 2026-05-02

Scope: read-only KiCad project validation scripts for AI-assisted project review.

## Created

- `03_TOOLS/scripts/project_validation/validate_kicad_project.ps1`
- `03_TOOLS/scripts/project_validation/validate_kicad_project.py`
- `03_TOOLS/scripts/project_validation/check_project_libraries.py`
- `03_TOOLS/scripts/project_validation/check_missing_footprints.py`
- `03_TOOLS/scripts/project_validation/check_missing_3d_models.py`
- `03_TOOLS/scripts/project_validation/check_unconnected_power.py`
- `03_TOOLS/scripts/project_validation/check_connector_orientation_review_needed.py`
- `03_TOOLS/scripts/project_validation/check_bom_has_datasheets.py`
- `03_TOOLS/scripts/project_validation/check_component_database_matches.py`
- `03_TOOLS/scripts/project_validation/README.md`

## Capabilities

- Checks project, schematic, and PCB file presence.
- Checks project-local library tables and symbol library resolution.
- Checks footprint library and assigned footprint file resolution.
- Checks missing PCB 3D model references.
- Checks `kicad-cli` availability for ERC, DRC, and BOM export.
- Checks static power-symbol/no-connect inventory and warns that ERC is still required.
- Checks datasheet evidence and component database matches.
- Flags connector, polarity, RF, USB, CAN, LIN, and automotive review needs.
- Writes Markdown and JSON reports.

## Safety

- No automatic fixes are attempted.
- Reports are written under `05_OUTPUTS/project_validation` by default.
- The validator refuses to write reports inside a project folder unless explicitly allowed.
- No KiCad source files, library tables, installed KiCad files, or user-global KiCad config files are modified.

## Self-Test

Validated against:

`04_KICAD_PROJECTS/archive/SAMPLE_KICAD_TEST_PROJECT/kicad`

Generated reports:

- `05_OUTPUTS/project_validation/script_selftest_sample/project_validation_report.md`
- `05_OUTPUTS/project_validation/script_selftest_sample_after_patch/project_validation_report.md`
- `05_OUTPUTS/project_validation/script_selftest_full/project_validation_report.md`
- `05_OUTPUTS/project_validation/script_selftest_ps_wrapper/project_validation_report.md`

Observed final full self-test status:

- Overall: `FAIL`
- PASS: 5
- WARN: 6
- FAIL: 1

The sample failed because assigned footprint libraries/files did not fully resolve. That is expected validation behavior for the archived sample and did not modify project files.

## Validation

- Python compile check passed for all Python scripts.
- `--list-checks` returned all check IDs.
- Python main validator generated Markdown and JSON reports.
- PowerShell wrapper generated Markdown and JSON reports.
- JSON reports parsed successfully.
- Protected KiCad project file guard passed.
