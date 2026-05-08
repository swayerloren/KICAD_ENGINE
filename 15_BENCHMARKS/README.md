# KiCad Engine Benchmarks

Status: methodology and task definitions only. No benchmark results are recorded here yet.

`15_BENCHMARKS/` defines repeatable tests for measuring whether KiCad Engine is improving at AI-assisted KiCad engineering. The goal is honest progress tracking, not marketing claims.

## Purpose

Benchmarks should measure whether an AI agent using KiCad Engine can:

- Select appropriate components from source-backed evidence.
- Cite datasheets, reference manuals, package drawings, and reference designs.
- Choose correct KiCad symbol candidates.
- Choose correct footprint candidates or mark them unverified.
- Build or review power, decoupling, boot/debug, connector, USB, CAN, RF, and protection circuits without guessing.
- Run or request ERC and DRC evidence where appropriate.
- Produce BOM and manufacturing-package review evidence when a task includes outputs.
- Flag human review needs instead of hiding uncertainty.
- Avoid hallucinated specs, fake source claims, and unverified footprint approval.

## What This Folder Contains

- `BENCHMARK_METHODOLOGY.md`: controlled run rules, evidence requirements, and result status labels.
- `BENCHMARK_RUNNER_PLAN.md`: future script design for collecting benchmark artifacts.
- `tasks/`: benchmark task definitions.
- `scoring/`: shared and category-specific scoring rules.
- `results/`: empty result area. Do not add scores unless a benchmark was actually run and documented.

## Core Task Set

- `tasks/TASK_001_ESP32_S3_MINIMUM_SYSTEM.md`
- `tasks/TASK_002_STM32_MINIMUM_SYSTEM.md`
- `tasks/TASK_003_CAN_BUS_NODE.md`
- `tasks/TASK_004_USB_C_POWER_DEVICE.md`
- `tasks/TASK_005_12V_AUTOMOTIVE_INPUT.md`
- `tasks/TASK_006_CONNECTOR_FOOTPRINT_VERIFICATION.md`

Existing extra task files may remain for legacy or future scenarios, but they do not replace the core task set above.

## Open Sample Project Candidates

Real open KiCad projects may become benchmark candidates only through `32_OPEN_KICAD_SAMPLE_INTAKE/`.

Before a sample project is used in a benchmark:

- Source URL, license, and attribution must be recorded.
- Imported originals must remain read-only.
- A normalized copy must exist for analysis or repair.
- Public bundling status must be `PUBLIC_BUNDLE_ALLOWED` or the benchmark must remain link-only.
- ERC, DRC, visual review, footprint/package review, and unresolved human-review flags must be documented when the benchmark claims those results.

Do not score an imported sample just because it opens in KiCad. Imported samples are unverified inputs until reviewed.

### Current Imported Sample Audit

Read-only engineering audit completed on 2026-05-03:

- `tomasr8_attiny85_dev_board`: `BROKEN_TEST_PROJECT`
- `m4a1x_tps5430`: `BROKEN_TEST_PROJECT`
- `esp_rs_esp_rust_board`: `BROKEN_TEST_PROJECT`

All three imported samples failed local KiCad 9.0.7 ERC/DRC checks. They remain useful as failure/regression fixtures, but they are not scored benchmark baselines, golden path demos, or reference-grade designs. Use `32_OPEN_KICAD_SAMPLE_INTAKE/review_reports/SAMPLE_PROJECTS_MASTER_AUDIT.md` before proposing any benchmark task based on these samples.

### Controlled Golden-Path Fixture

`tomasr8_attiny85_dev_board` has been copied into `19_TEST_PROJECTS/sample_kicad_projects/tomasr8_attiny85_dev_board/` as a controlled golden-path workflow fixture with known failures.

Benchmark task:

- `tasks/TASK_GOLDEN_PATH_tomasr8_attiny85_dev_board.md`

Baseline result:

- `results/tomasr8_attiny85_dev_board_BASELINE_RESULT.md`

This fixture is useful for demonstrating honest KiCad Engine gate behavior on a small real project. It is not a clean pass, not a reference-grade design, and not fabrication-ready.

## Benchmark Status Labels

- `NOT_RUN`: task exists but no run has been performed.
- `PARTIAL_RUN`: run started but required outputs or logs are incomplete.
- `INVALID_RUN`: run violated benchmark conditions or has missing evidence that prevents scoring.
- `SCORED_INTERNAL`: internally scored with artifacts and reviewer notes.
- `HUMAN_REVIEWED`: scored and reviewed by a qualified human reviewer.
- `PUBLIC_COMPARISON_READY`: ready for public comparison only when methodology, artifacts, tool versions, and scoring notes are publishable.

## Non-Goals

These benchmarks do not certify a PCB for fabrication. They do not prove KiCad Engine is better than another PCB AI tool unless the same benchmark task, constraints, scoring method, and public evidence are applied to both.

Do not create fake results. Do not backfill scores from memory. Do not claim a benchmark pass from incomplete evidence.

## PURPOSE

Define honest benchmark tasks, scoring methodology, and future real results for measuring KiCad Engine progress.

## WHAT_BELONGS_HERE

Task definitions, scoring rubrics, runner plans, and real run results with artifacts.

## WHAT_DOES_NOT_BELONG_HERE

Fake results, unsupported comparisons, active project source files, or fabricated performance evidence.

## AI_AGENT_RULES

- Read this folder's README.md and INDEX.md before adding or relying on content here.
- Mark unverified engineering claims explicitly.
- Keep source links, verification status, and human-review requirements visible.
- Route generated logs and reports to `02_HISTORY/`, `05_OUTPUTS/`, or project history unless this folder explicitly calls for generated indexes.

## SAFE_EDIT_RULES

- Preserve existing user work.
- Do not delete or overwrite files without explicit approval.
- Do not edit KiCad design files from this folder.
- Do not store secrets or credentials.

## PUBLIC_RELEASE_NOTES

- Review this folder for secrets, personal paths, copyrighted documents, unsupported claims, and large generated files before public release.
- Folder existence is not a completeness or production-readiness claim.
