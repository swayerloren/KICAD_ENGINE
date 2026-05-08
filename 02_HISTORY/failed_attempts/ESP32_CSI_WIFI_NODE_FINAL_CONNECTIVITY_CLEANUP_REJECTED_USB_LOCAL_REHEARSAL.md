# ESP32_CSI_WIFI_NODE Final Connectivity Cleanup Rejected USB Local Rehearsal

Generated: `2026-05-08T12:34:25-04:00`

## Context

- Task: `PCB_FINAL_CONNECTIVITY_CLEANUP`
- Trial folder: `routing_work\20260508_091428\final_connectivity_cleanup_trials\20260508_122929`

## Failed Candidate

- Candidate: `candidate_control_usb_local.kicad_pcb`
- Intended added local routes:
  - `/BOOT0` local cluster
  - `/ESP_EN` local cluster
  - `/DM_C` local `U3 -> R8`
  - `/DP_C` local `U3 -> R9`

## Initial False Signal

- First copied-board DRC pass showed `36` `drill_out_of_range` violations because the copied board did not yet have the live project `.kicad_pro` beside it.
- That result was rejected as invalid rehearsal context.

## Authoritative Rerun

- After copying the live `.kicad_pro` next to the trial board, the authoritative rerun produced:
  - `4` real violations
  - `15` unconnected items

## Real Violations

- `/DM_C` short to `/DM_E` at `R8`
- `/DP_C` short to `/DM_C` near `U3`
- `2` matching front solder-mask bridges tied to those shorts

## Decision

- Do not carry the USB-local cleanup copper into the live PCB.
- Keep only the control-cluster-only candidate as the accepted live delta for this task.
