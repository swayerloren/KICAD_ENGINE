# PCB Batch 03 USB Control Routing Failed Attempts

Status: `CAPTURED`

## Failed Attempt 1

- Context:
  - the interrupted pre-resume batch-03 script summary path called KiCad's via-width API without a layer argument
- Effect:
  - caused assertion noise and prevented the old batch-03 script from closing cleanly after apply
- Resolution:
  - replaced the unsafe summary logic with a layer-aware via diameter helper before resuming the live pass

## Failed Attempt 2

- Context:
  - the immediate post-save copied-board DRC check did not always match the saved copper state on the first run
- Effect:
  - first DRC pass could report the pre-settle unconnected count
- Resolution:
  - reran `kicad-cli pcb drc` after the file settled and used the settled rerun plus refreshed `LIVE_PROJECT_STATE.json` as the authoritative evidence
