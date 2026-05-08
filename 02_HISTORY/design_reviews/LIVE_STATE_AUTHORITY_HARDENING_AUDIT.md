# Live State Authority Hardening Audit

Date: `2026-05-08`

## Scope

Promote `LIVE_PROJECT_STATE` to the canonical authority for project gates and
status claims on branch `hardening/execution-contract` without editing KiCad
design files.

## Changes

- Added `03_TOOLS/scripts/project_state/live_state_authority.py` as the shared
  authority bundle builder.
- Added `03_TOOLS/scripts/project_state/validate_live_state_before_gate.py` as
  the explicit pre-gate live-state validator.
- Added `03_TOOLS/scripts/project_state/live_state_gate_wrapper.py` as the
  canonical phase gate wrapper.
- Converted `03_TOOLS/scripts/project_gate/check_phase_allowed.py` into a
  compatibility wrapper around the canonical gate wrapper.
- Updated `03_TOOLS/scripts/maintenance/run_maintenance_cycle.py` to consume the
  same live-state authority bundle used by gate checks.
- Updated startup and handoff docs so future agents run live-state validation
  before gate, placement-start, routing-start, or closeout status claims.
- Updated the real routing workflow so `LIVE_PROJECT_STATE` is the top routing
  authority instead of stale markdown.

## Authority Rules Added

1. Every phase or gate check must build or read fresh `LIVE_PROJECT_STATE`
   first.
2. Reports without source hashes are weak context only.
3. Reports older than live `.kicad_pcb` or `.kicad_sch` source hashes or
   timestamps are stale blockers.
4. Stale `NO_PCB`, `0 footprints`, or `no routing` narratives cannot override
   live file evidence.
5. Gates may still block on real live-state failures such as DRC fail,
   unconnected items, unrouted nets, or human-review requirements.
6. Gate output now supports blocker provenance values:
   `LIVE_FILE_EVIDENCE`, `FRESH_GATE_REPORT`, `STALE_REPORT_IGNORED`,
   `TASK_CONTRACT_FAILURE`, and `HUMAN_REVIEW_REQUIRED`.

## Validation

- `python -m py_compile` passed for all changed scripts.
- `python 03_TOOLS/scripts/project_state/validate_live_state_before_gate.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE`
  passed and reported `READ_FRESH_LIVE_PROJECT_STATE`.
- `python 03_TOOLS/scripts/maintenance/run_maintenance_cycle.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE`
  passed and used the shared live-state authority bundle.
- Phase `2` result: `ALLOWED`, status
  `ALREADY_DONE_BY_LIVE_FILE_EVIDENCE`.
- Phase `3` result: `ALLOWED`, status
  `ALREADY_DONE_OR_SUPERSEDED_BY_LIVE_PLACEMENT`.
- Phase `8` result: `BLOCKED`, status
  `PARTIAL_ROUTING_EXISTS_NEEDS_AUDIT`.
- Live output explicitly ignored stale blockers such as old `NO_PCB` and stale
  schematic/sandbox gate reports when live PCB evidence proved otherwise.

## Residual Gap

`TASK_CONTRACT_FAILURE` is now supported by the canonical gate wrapper, but it
only appears when a caller supplies `--task-contract`. Full mandatory contract
injection for every gate invocation still depends on workflow discipline or a
future top-level launcher/CI gate.
