# Open KiCad Sample Intake Index

Status: `ACTIVE_INDEX_WITH_IMPORTED_SAMPLES`

Last updated: `2026-05-03`

| Area | File / Folder | Purpose | Status |
| --- | --- | --- | --- |
| System overview | `README.md` | Explains controlled intake rules and folder roles. | ACTIVE |
| Workflow | `SAMPLE_INTAKE_WORKFLOW.md` | Dry-run-first candidate to reference-learning workflow. | ACTIVE |
| License rules | `SAMPLE_LICENSE_RULES.md` | Public-bundle and license review rules for samples. | ACTIVE |
| Normalization rules | `SAMPLE_NORMALIZATION_RULES.md` | Rules for preserved originals and working copies. | ACTIVE |
| Quality scorecard | `SAMPLE_QUALITY_SCORECARD.md` | Scores whether a sample is useful as learning material. | ACTIVE |
| Anti-copy rules | `SAMPLE_DO_NOT_COPY_RULES.md` | Prevents blind schematic/layout copying from samples. | ACTIVE |
| Source rules | `SOURCE_SELECTION_RULES.md` | Defines acceptable public sample sources. | ACTIVE |
| License screening | `LICENSE_SCREENING_RULES.md` | Defines license statuses and public-bundle gate. | ACTIVE |
| Schema | `SAMPLE_PROJECT_SCHEMA.md` | Required fields for candidate/import/review records. | ACTIVE |
| Import workflow | `SAMPLE_IMPORT_WORKFLOW.md` | Safe import and original-preservation workflow. | ACTIVE |
| Review workflow | `SAMPLE_REVIEW_WORKFLOW.md` | ERC/DRC/visual/file/fab review workflow. | ACTIVE |
| Promotion rules | `SAMPLE_PROMOTION_RULES.md` | Rules for reference, benchmark, or public-payload promotion. | ACTIVE |
| Blocked sources | `DO_NOT_IMPORT_LIST.md` | Projects/sources that should not be copied. | ACTIVE |
| Candidate records | `candidates/` | Source-link and screening records. | ACTIVE |
| Original imports | `imported_originals/` | Preserved read-only originals. | 3 IMPORTED |
| Normalized copies | `normalized_samples/` | Review/repair/benchmark working copies. | 3 CREATED |
| Reports | `review_reports/` | Audit outputs. | ACTIVE |
| Scripts | `scripts/` | Safe dry-run-first helpers. | ACTIVE |
| Templates | `templates/` | Record templates. | ACTIVE |

## Learning System

The intake layer now feeds a reference-learning system. Sample metrics may be
promoted into `07_REFERENCE_DESIGNS/` as link-first style comparison rules
after license and quality review.

## Agent Routing

- Use `candidates/` before import.
- Use `imported_originals/` only for preserved originals.
- Use `normalized_samples/` for any inspection that might write files.
- Use `review_reports/` for generated reports.
- Use `attribution/` for license and attribution evidence.
- Use `benchmark_candidates/` only after `SAMPLE_PROMOTION_RULES.md` is satisfied.

## Imported Samples

| Sample | Source | License | Imported original | Normalized copy | Import report | Status |
| --- | --- | --- | --- | --- | --- | --- |
| ATtiny85 Development Board | https://github.com/tomasr8/attiny85-dev-board | MIT | `imported_originals/tomasr8_attiny85_dev_board/` | `normalized_samples/tomasr8_attiny85_dev_board/` | `review_reports/tomasr8_attiny85_dev_board_IMPORT_REPORT.md` | `AUDITED_BROKEN_TEST_PROJECT` |
| TPS5430 DC-DC Buck Converter Module | https://github.com/M4a1x/TPS5430 | CERN-OHL-S-2.0 | `imported_originals/m4a1x_tps5430/` | `normalized_samples/m4a1x_tps5430/` | `review_reports/m4a1x_tps5430_IMPORT_REPORT.md` | `AUDITED_BROKEN_TEST_PROJECT` |
| ESP Rust Board | https://github.com/esp-rs/esp-rust-board | CERN-OHL-P-2.0 | `imported_originals/esp_rs_esp_rust_board/` | `normalized_samples/esp_rs_esp_rust_board/` | `review_reports/esp_rs_esp_rust_board_IMPORT_REPORT.md` | `AUDITED_BROKEN_TEST_PROJECT` |

## Current Import Warnings

- Imported originals must not be edited.
- Imported source Gerbers, drill files, BOMs, placement files, and STEP files are upstream artifacts, not KiCad Engine generated outputs.
- None of the imported samples has passed KiCad Engine ERC, DRC, visual, footprint/package, BOM, license, or benchmark review yet.
- Public payload inclusion still requires final human license and release review.

## Engineering Audit Status

Read-only audit report: `review_reports/SAMPLE_PROJECTS_MASTER_AUDIT.md`

| Sample | Classification | ERC | DRC | Annotation | Visual exports | Promotion status |
| --- | --- | --- | --- | --- | --- | --- |
| `tomasr8_attiny85_dev_board` | `BROKEN_TEST_PROJECT` | fail, 7 ERC messages | fail, 16 DRC violations plus 13 footprint errors | pass, no unannotated refs | schematic/top/bottom SVG exported | blocked from golden path, benchmark scoring, and public payload |
| `m4a1x_tps5430` | `BROKEN_TEST_PROJECT` | fail, 36 ERC messages | fail, 87 DRC violations plus 30 footprint errors | pass, no unannotated refs | schematic/top/bottom SVG exported | blocked from golden path, benchmark scoring, and public payload |
| `esp_rs_esp_rust_board` | `BROKEN_TEST_PROJECT` | fail, 73 ERC messages | fail, 81 DRC violations plus 95 footprint errors | pass, no unannotated refs | schematic/top/bottom SVG exported | blocked from golden path, benchmark scoring, and public payload |

These samples are currently useful as regression/failure fixtures. They are not suitable as clean demo projects, verified reference designs, or scored benchmarks without repair and human review.

## Controlled Test Project Promotion

`tomasr8_attiny85_dev_board` was promoted into `19_TEST_PROJECTS/sample_kicad_projects/tomasr8_attiny85_dev_board/` as a controlled golden-path workflow fixture with known failures.

Promotion notes:

- It was selected because it is the smallest imported project, has schematic and PCB files, has MIT license evidence, and has the fewest ERC/DRC issues among the imported samples.
- Upstream Gerbers, drill files, PDFs, bootloader files, and large media were excluded from the controlled copy.
- The fixture remains blocked from clean golden-path, reference-design, public-payload, and fabrication-ready claims.
- Benchmark task: `15_BENCHMARKS/tasks/TASK_GOLDEN_PATH_tomasr8_attiny85_dev_board.md`
- Baseline result: `15_BENCHMARKS/results/tomasr8_attiny85_dev_board_BASELINE_RESULT.md`
