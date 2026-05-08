# Baseline Result - ATtiny85 Development Board Controlled Fixture

Status: `BASELINE_UPDATED_AFTER_PARTIAL_GATE_RUN`

Benchmark task: `15_BENCHMARKS/tasks/TASK_GOLDEN_PATH_tomasr8_attiny85_dev_board.md`

Controlled fixture: `19_TEST_PROJECTS/sample_kicad_projects/tomasr8_attiny85_dev_board/`

## Source Of Baseline

The original baseline was derived from the read-only engineering audit performed on the normalized imported sample:

- Master audit: `32_OPEN_KICAD_SAMPLE_INTAKE/review_reports/SAMPLE_PROJECTS_MASTER_AUDIT.md`
- Engineering audit: `32_OPEN_KICAD_SAMPLE_INTAKE/review_reports/tomasr8_attiny85_dev_board_ENGINEERING_AUDIT.md`
- ERC/DRC report: `32_OPEN_KICAD_SAMPLE_INTAKE/review_reports/tomasr8_attiny85_dev_board_ERC_DRC_REPORT.md`
- Visual audit: `32_OPEN_KICAD_SAMPLE_INTAKE/review_reports/tomasr8_attiny85_dev_board_VISUAL_AUDIT.md`
- Gate status: `32_OPEN_KICAD_SAMPLE_INTAKE/review_reports/tomasr8_attiny85_dev_board_GATE_STATUS.md`

This file has been updated after the controlled golden-path gate run on the promoted sample copy. The run was not a final numeric benchmark score; it was a gated workflow execution with limited low-risk repairs.

Latest gate evidence:

- Gate report: `19_TEST_PROJECTS/sample_kicad_projects/tomasr8_attiny85_dev_board/reports/GOLDEN_PATH_GATE_REPORT.md`
- Repair log: `19_TEST_PROJECTS/sample_kicad_projects/tomasr8_attiny85_dev_board/reports/GOLDEN_PATH_REPAIR_LOG.md`
- Final audit: `19_TEST_PROJECTS/sample_kicad_projects/tomasr8_attiny85_dev_board/reports/GOLDEN_PATH_FINAL_AUDIT.md`

## Baseline Results

| Check | Result | Evidence |
| --- | --- | --- |
| Source/license/attribution | `PASS_PENDING_HUMAN_RELEASE_REVIEW` | MIT license and attribution records preserved |
| KiCad source files | `PASS` | `.kicad_pro`, `.kicad_sch`, `.kicad_pcb` present |
| Annotation | `PASS` | `reports/ANNOTATION_CHECK.md` |
| ERC | `FAIL` | 6 messages: 1 error, 5 warnings |
| DRC | `FAIL` | 15 DRC violations, 13 schematic parity issues, 0 unconnected pads |
| Schematic visual export | `PASS` | full-page SVG/PDF/PNG export succeeded |
| PCB visual export | `PASS` | top/bottom SVG export succeeded |
| Close-up visual review | `PASS_WITH_HUMAN_REVIEW_REQUIRED` | schematic and PCB close-up crops generated |
| Footprint/library status | `PARTIAL` | custom library mapping repaired; exact connector/regulator/header verification remains blocked |
| BOM export | `PASS_REVIEW_ONLY` | `_verification/bom/attiny85_BOM_NOT_FINAL.csv` |
| Manufacturing readiness | `BLOCKED` | no fab package generated; all outputs review-only/NOT_FINAL |

## Baseline Classification

`GOLDEN_PATH_PARTIAL`

This baseline is useful because it proves the workflow can detect failures, apply low-risk project-local repairs, generate review evidence, and preserve blockers honestly. It is not a clean demo pass.

## Score

No numeric benchmark score is assigned.

Reason: this file records a partial gate-run baseline, not a scored benchmark submission. A numeric score requires a dedicated benchmark run with preserved run metadata, artifacts, and reviewer notes.

## Human Review Required

Yes. Required before:

- public payload inclusion
- reference-design promotion
- clean benchmark scoring
- manufacturing-style output generation
- footprint/connector correctness claims
