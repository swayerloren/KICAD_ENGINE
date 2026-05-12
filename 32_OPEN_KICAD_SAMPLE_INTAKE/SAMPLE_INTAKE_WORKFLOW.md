# Sample Intake Workflow

Status: `ACTIVE_DRY_RUN_FIRST_WORKFLOW`

## Purpose

Define the safe path for bringing an open-source KiCad sample into KiCad
Engine as learning material without treating it as verified engineering truth.

## Required Stages

1. Register the candidate before any import.
2. Screen license evidence and public-bundle eligibility.
3. Confirm the sample actually contains KiCad project files.
4. Preserve the upstream copy under `imported_originals/` without edits.
5. Create a normalized working copy before any repair or metric extraction that
   might write files.
6. Extract schematic and PCB reference metrics in read-only mode.
7. Score the sample for readability, routing quality, connector correctness,
   and reuse safety.
8. Promote only reviewed lessons into `07_REFERENCE_DESIGNS/`,
   `12_REFERENCE_DESIGN_LIBRARY/`, or `15_BENCHMARKS/`.

## Dry-Run First Rule

Candidate registration, license screening, normalization planning, metric
extraction, and reference-index building must support dry-run mode first.

Dry-run is the default unless the command explicitly says otherwise.

## Required Records

Every candidate or imported sample should have:

- source URL
- source owner
- license status
- public bundle status
- attribution record
- KiCad file presence summary
- normalization status
- schematic metrics
- PCB metrics
- review notes

## Learning System Rule

Samples are comparison evidence, not copy targets.

Codex and Claude may use sample metrics to ask questions such as:

- Is the generated schematic more label-heavy than human-made examples?
- Does the board place edge connectors more consistently than reviewed samples?
- Is the USB block or buck layout visually less coherent than known examples?

They may not copy a sample layout or schematic block verbatim without separate
license review and explicit human approval.

## Promotion Rule

Only samples with clear license handling and reviewed metrics may influence:

- `07_REFERENCE_DESIGNS/`
- `12_REFERENCE_DESIGN_LIBRARY/`
- `15_BENCHMARKS/`
- public payload decisions

Imported originals remain preservation evidence only.
