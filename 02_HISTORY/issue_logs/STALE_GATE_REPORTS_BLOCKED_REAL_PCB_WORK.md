# STALE_GATE_REPORTS_BLOCKED_REAL_PCB_WORK

Status: `OPEN_RISK_PARTIALLY_MITIGATED`

Date: `2026-05-07`

## Problem

`ESP32_CSI_WIFI_NODE` had a real `.kicad_pcb` with board outline, `43` footprints, placement, ratsnest, and partial routing, but stale reports and stale gate logic still blocked work as if the board did not exist.

## Root Cause

- legacy maintenance did not rebuild canonical live project state from KiCad files
- stale reports often lacked source hashes and timestamp-aware freshness rules
- the phase gate checker trusted stale markdown over live file evidence

## Fix Applied

- added live project state generation and stale-report detection
- added gate reconciliation based on live file evidence
- repaired `check_phase_allowed.py` so stale `NO_PCB` and `0 footprints` reports cannot override a real board
- added canonical maintenance-cycle wiring and documentation

## Remaining Risk

- some project reports are still weak or stale-prone because they do not yet embed both schematic and PCB hashes
- routing remains blocked for real board-state reasons, not stale-report reasons
- historical project history files still contain old blocked narratives and must be treated as history, not live truth

## Required Follow-Up

- continue adding source hashes to operational gate reports
- keep using `LIVE_PROJECT_STATE.json` and `GATE_RECONCILIATION_REPORT.md` as the current-state truth layer
- do not resume routing until the live existing-trace audit, DRC blockers, GND strategy, and unrouted-net blockers are resolved
