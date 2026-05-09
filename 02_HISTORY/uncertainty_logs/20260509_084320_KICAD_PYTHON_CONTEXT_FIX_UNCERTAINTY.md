# Uncertainty Log - KiCad Python Context Fix

Date: `2026-05-09`
Task type: `GITHUB_DOCS_ONLY`

## Uncertainties

- The new context helper is verified on the current Windows KiCad 9 packaging layout, not all KiCad distributions.
- Some Linux or macOS installs may expose `pcbnew` through different Python path layouts than the current helper expects.
- The repo did not run a full board-aware extraction or placement-readiness script in this task because the user asked for portability/toolchain fixing, not live project work.

## Impact

These uncertainties do not change the main conclusion: the repo now handles the current machine's `pcbnew` context mismatch safely and documents the correct fallback behavior.
