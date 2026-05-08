# MAINTENANCE_LAYER_ROOT_CAUSE_AUDIT

Date: `2026-05-07`

## Executive Summary

The maintenance layer existed only as a partial prompt-counter and index-rebuild workflow. It did not reliably rebuild live project truth from KiCad files, it did not detect stale reports using hashes/timestamps, and the phase gate checker trusted stale markdown more than the actual `.kicad_pcb`. That is why `ESP32_CSI_WIFI_NODE` could have a real placed/routed board while the repo still blocked work with stale `NO_PCB` and gate-fail narratives.

## Findings

| Area | Before Repair | Impact |
| --- | --- | --- |
| Prompt counter | Existed in project memory | Counter alone did not enforce meaningful live-state rebuilds |
| Maintenance trigger | Documented/manual only | No robust supervisor was guaranteed to run every 5 prompts |
| Maintenance scope | Mostly memory/history/index rebuilds | Live KiCad truth was not rebuilt into canonical project state |
| Report freshness | No required source hashes on many reports | Old reports could survive without being invalidated |
| Gate checker | Read stale markdown reports directly | Real PCB existence could be ignored |
| Blocker source reporting | Weak | Agents could not tell live blockers from stale blockers |

## Why Stale Reports Survived

1. Reports had no reliable source-hash linkage to the live schematic or PCB.
2. `check_phase_allowed.py` did not rebuild or consult a canonical live project state first.
3. Legacy maintenance focused on memory/history hygiene, not on the live KiCad artifact truth model.
4. The repo had no strong stale-report rules such as:
   - `NO_PCB` is stale if `.kicad_pcb` exists with footprints
   - `0 footprints` is stale if live footprint count is nonzero
   - `routing missing` is stale if live tracks exist
5. Startup/closeout rules referenced maintenance, but the wiring was not strong enough to force reconciliation before gate checks.

## Repair Implemented

### Canonical maintenance supervisor

- `03_TOOLS/scripts/maintenance/run_maintenance_cycle.py`
- `03_TOOLS/scripts/maintenance/prompt_counter.py`
- `03_TOOLS/scripts/maintenance/maintenance_config.json`
- `03_TOOLS/scripts/maintenance/README.md`

### Canonical live project state layer

- `03_TOOLS/scripts/project_state/project_state_common.py`
- `03_TOOLS/scripts/project_state/build_live_project_state.py`
- `03_TOOLS/scripts/project_state/detect_stale_reports.py`
- `03_TOOLS/scripts/project_state/reconcile_project_gates.py`
- `03_TOOLS/scripts/project_state/update_phase_status_from_live_state.py`
- `03_TOOLS/scripts/project_state/live_project_state.schema.json`
- `03_TOOLS/scripts/project_state/README.md`

### Compatibility and gate updates

- repaired `03_TOOLS/scripts/project_gate/check_phase_allowed.py`
- converted legacy `03_TOOLS/scripts/memory_maintenance/*` entrypoints into compatibility wrappers around the canonical maintenance layer

## Validation Result

| Check | Result |
| --- | --- |
| Python syntax validation | `PASS` |
| Maintenance cycle | `PASS` |
| Live project state build | `PASS` |
| Stale report audit | `PASS` |
| Gate reconciliation | `PASS` |
| Phase 2 gate after repair | `ALLOWED` |
| Phase 3 gate after repair | `ALLOWED` |
| Phase 8 gate after repair | `BLOCKED_FOR_REAL_BOARD_REASONS` |

## Live Project Truth Used After Repair

- PCB exists: `YES`
- Board outline exists: `YES`
- Footprints: `43`
- Tracks: `24`
- Vias: `2`
- Zones: `0`
- Detectable unrouted nets: `16`
- DRC: `FAIL`, `12` violations, `65` unconnected
- Classification: `PCB_EXISTS_PARTIAL_ROUTING_EXISTS_NEEDS_AUDIT`

## Remaining Risk

The maintenance layer is now robust enough to stop stale `NO_PCB` blockers from overriding live evidence. It does not convert unsafe physical board state into a pass. Routing remains correctly blocked until the live placement/routed geometry audit, GND strategy, DRC issues, and unrouted critical nets are addressed.
