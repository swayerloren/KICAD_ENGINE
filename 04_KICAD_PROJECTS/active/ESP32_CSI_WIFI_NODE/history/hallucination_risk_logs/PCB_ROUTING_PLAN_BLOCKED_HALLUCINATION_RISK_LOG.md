# PCB Routing Plan Hallucination Risk Log

Date: 2026-05-03

Project: `ESP32_CSI_WIFI_NODE`

## Risk Label

`HIGH_RISK`

## Risk

Routing plans can easily create false confidence by inventing trace widths, clearances, via sizes, impedance geometry, RF keepouts, connector orientation, or switcher layout details before source and PCB evidence exists.

## Controls Used

- Exact widths, clearances, vias, impedance, and RF geometry were not invented.
- Routing was marked blocked.
- Human review was required for high-risk routing constraints.
- Claims were tied to local reports and rule files.

## Required Future Evidence

- Gate `PASS`.
- PCB exists and is synced.
- Board outline and stackup.
- Fab profile and DRC constraints.
- Verified footprints and placement.
- Source-backed USB, RF, power, regulator, connector, and antenna layout evidence.

