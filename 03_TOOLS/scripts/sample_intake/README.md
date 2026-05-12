# Sample Intake Scripts

Status: `ACTIVE_DRY_RUN_FIRST_SCRIPT_LAYER`

## Purpose

Provide safe local tooling for open-source KiCad sample intake, license
screening, normalization planning, metric extraction, and reference-style index
generation.

## Scripts

- `register_sample_candidate.py`
  Creates or previews a sample candidate record. Dry-run by default.
- `audit_sample_license.py`
  Screens a local sample folder for common license evidence. Read-only.
- `normalize_sample_project.py`
  Plans or creates a normalized working copy from an imported original sample.
- `extract_sample_schematic_metrics.py`
  Parses `.kicad_sch` files and extracts readability-oriented reference metrics.
- `extract_sample_pcb_metrics.py`
  Extracts read-only PCB metrics and routing-style signals from `.kicad_pcb`.
- `build_reference_style_index.py`
  Aggregates sample metrics into a reference index for future comparison work.

## Safety Rules

- Dry-run first.
- No network access is required.
- No active KiCad project path is allowed as a normalization source.
- Imported originals are read-only.
- Reference metrics are comparison evidence, not correctness proof.
