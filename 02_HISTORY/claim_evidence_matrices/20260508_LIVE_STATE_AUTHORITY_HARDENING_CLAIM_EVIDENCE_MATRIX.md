# Claim / Evidence Matrix - Live State Authority Hardening

Date: `2026-05-08`

| Claim | Evidence |
| --- | --- |
| `LIVE_PROJECT_STATE` is now the canonical gate authority path. | `03_TOOLS/scripts/project_state/live_state_authority.py`, `03_TOOLS/scripts/project_state/live_state_gate_wrapper.py`, `03_TOOLS/scripts/project_gate/check_phase_allowed.py` |
| Maintenance now uses the same authority bundle as gates. | `03_TOOLS/scripts/maintenance/run_maintenance_cycle.py`; maintenance run output in `LIVE_STATE_AUTHORITY_HARDENING_COMMANDS.md` |
| Stale reports are ignored when live PCB evidence proves otherwise. | Phase `2`, `3`, and `8` outputs recorded in `LIVE_STATE_AUTHORITY_HARDENING_COMMANDS.md`; stale-report list in validation output |
| Phase `2` is allowed by live PCB evidence. | `check_phase_allowed.py --phase 2` output |
| Phase `3` is allowed by live placement evidence. | `check_phase_allowed.py --phase 3` output |
| Phase `8` remains blocked by live DRC/connectivity state. | `check_phase_allowed.py --phase 8` output |
