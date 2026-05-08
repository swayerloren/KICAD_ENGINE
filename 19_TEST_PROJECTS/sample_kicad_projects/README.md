# Sample KiCad Projects

Status: `HAS_CONTROLLED_SAMPLE_FIXTURES`

Safe sample KiCad projects may live here only after license, attribution, and public-release review. Do not copy active real projects here without explicit approval.

## Current Samples

| Sample | Source | Status | Notes |
| --- | --- | --- | --- |
| `tomasr8_attiny85_dev_board` | `https://github.com/tomasr8/attiny85-dev-board` | `CONTROLLED_GOLDEN_PATH_DEMO_FIXTURE_WITH_KNOWN_FAILURES` | Small MIT-licensed ATtiny85 board copied from normalized sample intake. ERC/DRC currently fail; use as workflow fixture, not a clean design. |

## Rules

- Keep sample attribution and license files with each sample.
- Exclude upstream fabrication outputs unless they are explicitly marked `NOT_FINAL` and required for a review task.
- Do not silently repair sample projects.
- Do not treat a sample as reference-grade or manufacturing-ready unless the relevant KiCad Engine gates pass.
- Put benchmark tasks in `15_BENCHMARKS/tasks/` and actual benchmark results in `15_BENCHMARKS/results/`.
