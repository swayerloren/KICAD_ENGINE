# Staged Routing Runner

## Purpose

Define a staged routing admission runner so Codex cannot jump between routing
phases without explicit stage contracts.

The runner is a workflow gate. It is not permission to edit KiCad files by
itself.

## Stage Order

1. `placement_readiness`
2. `power_critical`
3. `ground_strategy`
4. `USB_support`
5. `boot_enable_control`
6. `USB_data`
7. `low_speed_remaining`
8. `trace_geometry_cleanup`
9. `final_connectivity`
10. `final_visual_review`

## Contract Rules

Every stage must define:

- required input files
- nets allowed
- nets forbidden
- DRC requirement
- geometry requirement
- hash delta requirement yes/no
- copied-board rehearsal requirement yes/no
- pass/fail output
- next allowed stage

## Runner Behavior

The runner must:

1. resolve the requested project
2. load the requested stage contract
3. verify required input files exist
4. check the current placement-readiness scorecard when routing stages are requested
5. read fresh `LIVE_PROJECT_STATE.json`
6. apply no-progress detector output before allowing broad routing to continue
7. emit explicit stage-ready or stage-blocked output

## Required Rule

If the no-progress detector reports `BLOCKED_REPAIR_MODE`, the runner must stop
broad routing until the recommended targeted repair stage is handled.

## Command

```powershell
python 14_LAYOUT_AUTOMATION\scripts\staged_routing_runner.py `
  --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE `
  --stage boot_enable_control `
  --output-json 05_OUTPUTS\reliability\staged_runner.json `
  --markdown 05_OUTPUTS\reliability\staged_runner.md
```
