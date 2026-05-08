# Benchmark Runner Plan

Status: future implementation plan. No benchmark runner is implemented or executed yet.

## Goal

Build a read-only-first runner that collects benchmark artifacts and produces Markdown and JSON reports. The runner should reduce bookkeeping work, not replace technical review.

## Proposed Inputs

- `--task`: path to a task file under `15_BENCHMARKS/tasks`.
- `--workspace`: disposable benchmark workspace path.
- `--agent-log`: transcript or command log from the AI run.
- `--project`: optional KiCad project path when a task creates or reviews a project.
- `--output`: result folder under `15_BENCHMARKS/results/YYYYMMDD_TASK_AGENT`.
- `--sources`: optional citation/source manifest.
- `--mode`: `review-only`, `create-plan`, `create-disposable-project`, or `score-existing-artifacts`.

## Proposed Automated Checks

- Verify required metadata fields exist.
- Verify no result claims `FAB_READY`.
- Verify manufacturing-style outputs are labeled `NOT_FINAL`.
- Check for ERC and DRC report files when expected.
- Check BOM or component-list presence when expected.
- Check citations contain URLs, local source paths, or source-document identifiers.
- Check footprint approval language for `UNVERIFIED_FOOTPRINT` where package drawing evidence is missing.
- Check connector, polarity, RF, USB, CAN, and automotive review flags.
- Check that result status is not `PUBLIC_COMPARISON_READY` without human reviewer notes.

## Proposed Outputs

- `BENCHMARK_RESULT.md`
- `benchmark_result.json`
- `artifact_manifest.json`
- `score_breakdown.md`
- `human_review_required.md`
- `unknowns_and_unverified_claims.md`

## Safety Rules

- The runner must not edit installed KiCad files.
- The runner must not edit original user projects.
- Any project creation or modification must use a disposable benchmark workspace.
- The runner must not download datasheets by default.
- The runner must not infer correctness from text confidence alone.
- A script pass is only scoped script evidence, not engineering approval.

## Future Integration

Potential integrations:

- `health_check.py` for workspace readiness.
- `03_TOOLS/scripts/project_validation/` for project checks.
- `03_TOOLS/scripts/kicad_libraries/` for symbol and footprint candidate discovery.
- `09_ACCURACY_ENGINE/` for verification rules.
- `10_KNOWLEDGE_BASE/` for review checklists.
- `11_LIBRARY_FACTORY/` for symbol and footprint QA.
- `13_PART_INGESTION/` for source-backed part-record stubs.

No implementation should claim public comparison readiness until tested on disposable projects.
