# PCB Critical Nets Routing Hallucination Risk Log

Date: 2026-05-03

Project: `ESP32_CSI_WIFI_NODE`

## Risk Label

`HIGH_RISK`

## Risk

Routing critical nets without a PCB, verified footprints, placement, stackup, zone strategy, source-backed USB/RF/power constraints, and DRC evidence would require guessing physical design details.

## Controls Used

- No routing was attempted.
- No trace widths, via sizes, USB geometry, RF geometry, or switcher copper dimensions were invented.
- The work was marked `CRITICAL_ROUTING_FAIL`.
- Human review remains required.

## Required Future Evidence

- Gate `PASS`.
- PCB exists and is synced.
- Placement and zone setup pass.
- Critical footprints verified.
- Source-backed USB, RF, power, and regulator layout constraints.
- DRC and close-up visual evidence after routing.

