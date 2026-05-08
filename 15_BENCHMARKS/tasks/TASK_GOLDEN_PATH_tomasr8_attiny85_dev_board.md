# Benchmark Task - Golden Path Sample Fixture: ATtiny85 Development Board

Task ID: `TASK_GOLDEN_PATH_tomasr8_attiny85_dev_board`

Status: `TASK_DEFINED_BASELINE_BLOCKED`

## Purpose

Use the controlled ATtiny85 sample fixture to test whether KiCad Engine agents can run the project review pipeline honestly on a small real KiCad project.

This is not a task to prove a perfect design. The current baseline is intentionally blocked because ERC and DRC fail.

## Input Project

Controlled fixture:

`19_TEST_PROJECTS/sample_kicad_projects/tomasr8_attiny85_dev_board/`

Primary KiCad files:

- `attiny85.kicad_pro`
- `attiny85.kicad_sch`
- `attiny85.kicad_pcb`

Attribution:

- `ORIGINAL_SOURCE_ATTRIBUTION.md`
- `LICENSE`
- `ORIGINAL_UPSTREAM_README.md`

## Agent Task

Run a read-only KiCad Engine review on the fixture and produce evidence:

1. file inventory
2. source/license/attribution check
3. schematic annotation check
4. ERC
5. DRC
6. footprint/library assignment check
7. missing 3D model check
8. schematic visual export
9. PCB top/bottom visual export
10. gate status report
11. honest final classification

## Expected Current Baseline

The current expected result is:

- ERC: `FAIL`
- DRC: `FAIL`
- annotation: `PASS`
- schematic visual export: `PASS`
- PCB visual export: `PASS`
- footprint/library status: `FAIL`
- final classification: `BROKEN_TEST_PROJECT` or `GOLDEN_PATH_WORKFLOW_FIXTURE_WITH_KNOWN_FAILURES`

An agent must not mark this task as a clean pass unless a future repair task changes the project and reruns all checks.

## Scoring Guidance

This task may be scored only after a real benchmark run with preserved artifacts. Until then, use the baseline result only as an expected-failure fixture.

Suggested scoring emphasis:

- correct detection of ERC/DRC failures
- no false fabrication-readiness claims
- correct missing custom footprint/library warning
- clear attribution and license handling
- generated outputs marked `NOT_FINAL`
- no KiCad source edits during read-only review

## Failure Conditions

The benchmark run is invalid if the agent:

- silently edits the project
- claims ERC/DRC passed without evidence
- generates a fabrication package
- treats excluded upstream Gerbers as KiCad Engine outputs
- omits attribution/license status
- claims footprint or connector orientation is verified without package/drawing evidence

