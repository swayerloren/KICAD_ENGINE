# Quality Gate Failure - PCB Trace Geometry Gate

Date: `2026-05-10`
Project: `ESP32_CSI_WIFI_NODE`
Gate: `PCB_TRACE_GEOMETRY_AUDIT`
Status: `FAIL`

## Failure Summary

The live board failed the new read-only trace geometry acceptance gate.

## Evidence

- `trace_quality.json` reports `FAIL`
- finding counts:
  - `RIGHT_ANGLE_FOUND = 29`
  - `ACUTE_JOG_FOUND = 1`
  - `UNNECESSARY_ZIGZAG_FOUND = 4`
  - `EXCESSIVE_DETOUR_RATIO = 2`
  - `TEST_POINT_STUB_TOO_LONG = 3`

## Consequence

Codex/Claude must not claim the current routing is acceptable until a fresh geometry audit packet returns `PASS`.
