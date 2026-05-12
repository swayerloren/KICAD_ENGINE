# Uncertainty Log - PCB Trace Geometry Audit

Date: `2026-05-10`
Task type: `DOCS_ONLY`

## Uncertainties

- Test-point stub detection uses net-matched pad-center proximity because exact pad-edge attach coordinates are not extracted from the live board schema.
- Return-path split detection is heuristic and conservative; it is meant to catch obvious long plane-carving traces, not replace full SI/EMC analysis.
- The current live board exposes `0` extracted RF keepouts, so RF-crossing detection was validated only by execution path, not by a live positive case.

## Impact

These uncertainties do not change the verified result of this task: the toolchain exists, runs in read-only mode, and the current board still fails on multiple concrete geometry issues.
