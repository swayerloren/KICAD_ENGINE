# Benchmarks Index

Status: `METHODOLOGY_ONLY`

## Key Areas

- `BENCHMARK_METHODOLOGY.md`
- `BENCHMARK_RUNNER_PLAN.md`
- `tasks/`
- `scoring/`
- `results/`

## Required Use

Do not create fake results. Public comparisons require actual artifacts, scoring notes, and human review.

## Core Benchmark Tasks

- `tasks/TASK_001_ESP32_S3_MINIMUM_SYSTEM.md`
- `tasks/TASK_002_STM32_MINIMUM_SYSTEM.md`
- `tasks/TASK_003_CAN_BUS_NODE.md`
- `tasks/TASK_004_USB_C_POWER_DEVICE.md`
- `tasks/TASK_005_12V_AUTOMOTIVE_INPUT.md`
- `tasks/TASK_006_CONNECTOR_FOOTPRINT_VERIFICATION.md`

## Core Scoring Files

- `scoring/SCORING_RUBRIC.md`
- `scoring/SCHEMATIC_SCORE.md`
- `scoring/PCB_SCORE.md`
- `scoring/DATASHEET_SCORE.md`
- `scoring/FOOTPRINT_SCORE.md`
- `scoring/FAB_PACKAGE_SCORE.md`


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
