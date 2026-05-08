# Issue Log - Open KiCad Sample Projects Audit Blockers

Date: `2026-05-03`

Status: `OPEN`

Severity: `MEDIUM`

Human review required: `YES`

## Summary

The imported open KiCad sample projects completed read-only engineering audit, but all currently fail ERC and DRC under local KiCad 9.0.7. They must not be promoted as golden-path examples, clean benchmark baselines, reference-grade designs, or public payload samples without a future repair and re-audit pass.

## Affected Samples

- `esp_rs_esp_rust_board`
- `m4a1x_tps5430`
- `tomasr8_attiny85_dev_board`

## Evidence

- `32_OPEN_KICAD_SAMPLE_INTAKE/review_reports/SAMPLE_PROJECTS_MASTER_AUDIT.md`
- `32_OPEN_KICAD_SAMPLE_INTAKE/review_reports/*_ENGINEERING_AUDIT.md`
- `32_OPEN_KICAD_SAMPLE_INTAKE/review_reports/*_ERC_DRC_REPORT.md`
- `32_OPEN_KICAD_SAMPLE_INTAKE/review_reports/*_GATE_STATUS.md`

## Blockers

1. ERC failures or warnings exist in every sample.
2. DRC violations exist in every sample.
3. Footprint/parity issues exist in every sample.
4. Close-up visual crop review was not available because no sample-specific visual block configs were present.
5. None of the samples has passed KiCad Engine promotion gates.

## Required Resolution

- Keep samples classified as `BROKEN_TEST_PROJECT` until repaired in normalized copies and re-audited.
- Do not edit `imported_originals`.
- Do not generate manufacturing outputs from these samples.
- Do not include them in public payloads unless license status and engineering quality are separately approved.

