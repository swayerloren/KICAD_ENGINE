# Claim Evidence Matrix - Test Examples Benchmarks Setup

Date: 2026-05-03

| Claim | Status | Evidence | Human Review Required |
| --- | --- | --- | --- |
| Requested benchmark files and folders exist. | VERIFIED_BY_COMMAND | Required path presence check passed. | No |
| Requested test project folders and planning-only sample exist. | VERIFIED_BY_COMMAND | Required path presence check passed. | No |
| Requested example folders exist. | VERIFIED_BY_COMMAND | Required path presence check passed. | No |
| Examples are marked `EXAMPLE_ONLY`. | VERIFIED_BY_COMMAND | Label check over `27_EXAMPLES` passed. | No |
| Planning-only sample files are marked `EXAMPLE_ONLY_PLANNING_ONLY`. | VERIFIED_BY_COMMAND | Label check over sample folder passed. | No |
| No benchmark results were created. | VERIFIED_BY_COMMAND | `15_BENCHMARKS/results` contains only `README.md`. | No |
| No KiCad source or fab artifacts were created in benchmark/test/example folders. | VERIFIED_BY_COMMAND | Corrected artifact scan returned no files. | No |
| Health check passed. | VERIFIED_BY_COMMAND | `python health_check.py --repo-root . --no-write` reported `PASS=131 WARN=0 FAIL=0`. | No |

