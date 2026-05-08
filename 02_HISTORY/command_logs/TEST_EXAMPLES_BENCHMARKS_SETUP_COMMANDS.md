# Test Examples Benchmarks Setup Commands

Date: 2026-05-03
Scope: Safe benchmark, test project, and example setup.

## Commands Run

| Command / Action | Result |
| --- | --- |
| Read `AGENTS.md`. | Completed. |
| Inspected `15_BENCHMARKS`, `19_TEST_PROJECTS`, and `27_EXAMPLES`. | Completed. |
| Created requested directories with `New-Item -ItemType Directory -Force`. | Completed. |
| Applied documentation updates with `apply_patch`. | Completed after one context-mismatch retry. |
| Required path presence check. | Passed. |
| NUL/control-character scan in benchmark/test/example folders. | Passed. |
| EXAMPLE_ONLY label check under `27_EXAMPLES`. | Passed. |
| EXAMPLE_ONLY_PLANNING_ONLY label check under the planning-only sample. | Passed. |
| `python health_check.py --repo-root . --no-write` | Passed: `PASS=131 WARN=0 FAIL=0`. |
| Protected KiCad/manufacturing file timestamp scan. | No protected files modified. |
| Initial artifact scan using PowerShell `-Include` on literal folders. | Noisy/unreliable output; corrected with explicit extension filter. |
| Corrected artifact scan over `15_BENCHMARKS`, `19_TEST_PROJECTS`, and `27_EXAMPLES`. | No KiCad source files, fab outputs, STEP/STP files, or zip packages found. |
| Rebuilt memory, history, AI-quality, and current-known-problems indexes. | Completed. |

## Not Run

- No benchmark run.
- No ERC/DRC.
- No installer or package manager.
- No fabrication export.
