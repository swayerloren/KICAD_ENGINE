# DRC Run Log

Status: `BASELINE_CAPTURED`

Generated: `2026-05-08T09:37:20-04:00`

## Baseline Run

| Timestamp | Source | Result | Violations | Unconnected Items | Evidence |
| --- | --- | --- | --- | --- | --- |
| `2026-05-08T09:15:23-04:00` | `kicad-cli pcb drc --format json` | `FAIL` | `0` | `44` | `CURRENT_DRC_BASELINE.json`, `CURRENT_DRC_BASELINE.md` |

## Notes

- This prep task did not reroute or refill the live board.
- Remaining block is connectivity completeness, not new geometry damage.

## Batch 01 Runs

| Timestamp | Source | Result | Violations | Unconnected Items | Evidence |
| --- | --- | --- | --- | --- | --- |
| `2026-05-08T09:41:54-04:00` | `kicad-cli pcb drc --format json` | `FAIL` | `0` | `44` | `reports/PCB_BATCH_01_DRC_PRECHECK.json` |
| `2026-05-08T09:52:00-04:00` | `kicad-cli pcb drc --format json` | `FAIL` | `0` | `27` | `reports/PCB_BATCH_01_DRC_AND_GND_REPAIR_DRC.json` |
| `2026-05-08T10:34:27-04:00` | `kicad-cli pcb drc --format json` | `FAIL` | `0` | `27` | `reports/PCB_BATCH_02_POWER_ROUTING_REPAIR_DRC.json` |
| `2026-05-08T11:25:54-04:00` | `kicad-cli pcb drc --format json` | `FAIL` | `0` | `21` | `reports/PCB_BATCH_03_USB_CONTROL_ROUTING_DRC_FIRST.json` |
| `2026-05-08T11:26:08-04:00` | `kicad-cli pcb drc --format json` | `FAIL` | `0` | `21` | `reports/PCB_BATCH_03_USB_CONTROL_ROUTING_DRC_FINAL.json` |
| `2026-05-08T11:26:44-04:00` | `build_live_project_state.py --apply` | `FAIL` | `0` | `21` | `reports/live_project_state/LIVE_PROJECT_STATE_DRC.json` |
| `2026-05-08T12:06:30-04:00` | `kicad-cli pcb drc --format json` | `FAIL` | `0` | `20` | `reports/PCB_BATCH_04_CONTROL_NET_ROUTING_DRC.json` |
| `2026-05-08T12:06:57-04:00` | `build_live_project_state.py --apply` | `FAIL` | `0` | `20` | `reports/live_project_state/LIVE_PROJECT_STATE_DRC.json` |
