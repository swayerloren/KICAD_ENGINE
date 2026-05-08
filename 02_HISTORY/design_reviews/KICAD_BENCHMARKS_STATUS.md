# KiCad Benchmarks Status

Date: 2026-05-03

## Scope

Created the `15_BENCHMARKS/` methodology layer so KiCad Engine can measure progress honestly and eventually compare against other PCB AI tools using controlled evidence.

No benchmark was run. No benchmark result was created. No score was invented.

## Created

- `15_BENCHMARKS/README.md`
- `15_BENCHMARKS/BENCHMARK_METHODOLOGY.md`
- `15_BENCHMARKS/BENCHMARK_RUNNER_PLAN.md`
- `15_BENCHMARKS/tasks/TASK_001_ESP32_S3_MINIMUM_SYSTEM.md`
- `15_BENCHMARKS/tasks/TASK_002_STM32_BLUEPILL_CLONE_REVIEW.md`
- `15_BENCHMARKS/tasks/TASK_003_CAN_BUS_NODE.md`
- `15_BENCHMARKS/tasks/TASK_004_USB_C_POWER_DEVICE.md`
- `15_BENCHMARKS/tasks/TASK_005_12V_AUTOMOTIVE_INPUT.md`
- `15_BENCHMARKS/tasks/TASK_006_CONNECTOR_FOOTPRINT_VERIFICATION.md`
- `15_BENCHMARKS/scoring/SCORING_RUBRIC.md`
- `15_BENCHMARKS/scoring/SCHEMATIC_SCORE.md`
- `15_BENCHMARKS/scoring/PCB_SCORE.md`
- `15_BENCHMARKS/scoring/DATASHEET_SCORE.md`
- `15_BENCHMARKS/scoring/FOOTPRINT_SCORE.md`
- `15_BENCHMARKS/scoring/FAB_PACKAGE_SCORE.md`
- `15_BENCHMARKS/results/README.md`

## Benchmark Coverage

Starter tasks cover:

- ESP32-S3 minimum system.
- STM32 Blue Pill clone-style review.
- CAN bus node.
- USB-C power device.
- Automotive 12 V input.
- Connector footprint verification.

Scoring explicitly covers:

- Correct component selection.
- Source citations.
- Correct symbol.
- Correct footprint.
- Power design correctness.
- Decoupling completeness.
- Boot/debug correctness.
- Connector orientation verification.
- ERC and DRC result handling.
- BOM completeness.
- Manufacturing output completeness.
- Human review flags.
- No hallucinated specs.

## Integration Updates

Updated:

- `AGENTS.md`
- `README.md`
- `README_GPT.md`
- `FOR CHAT GPT.MD`
- `START_HERE_FOR_AI_AGENTS.md`
- `00_CODEX_START/REPO_MAP.md`
- `health_check.py`
- `installer/payload/PAYLOAD_CONTENT_RULES.md`
- `installer/payload/build_payload.py`

The clean installer payload now includes `15_BENCHMARKS/`.

## Validation

Commands run:

- `python health_check.py --repo-root . --no-write`
- `python installer/payload/build_payload.py --source-root .`
- `python health_check.py --repo-root installer/payload/repo-template --no-write`

Results:

- Root health: `PASS=131 WARN=0 FAIL=0`.
- Payload build: completed and regenerated `installer/payload/repo-template`, `installer/payload/payload.manifest.json`, and `installer/payload/PAYLOAD_BUILD_REPORT.md`.
- Payload health: `PASS=131 WARN=0 FAIL=0`.
- Payload manifest includes all requested `15_BENCHMARKS` files.

## Not Done

- No benchmark runner script was implemented.
- No KiCad benchmark project was created.
- No KiCad design files were modified.
- No ERC, DRC, BOM, Gerber, drill, STEP, or manufacturing outputs were generated.
- No comparison to Flux or any other PCB AI tool was scored.

## Next Steps

- Implement the future benchmark runner only after agreeing on result artifact format.
- Create disposable benchmark workspaces for actual runs.
- Add human reviewer worksheets before public comparison claims.
- Keep result folders empty until real runs exist.
