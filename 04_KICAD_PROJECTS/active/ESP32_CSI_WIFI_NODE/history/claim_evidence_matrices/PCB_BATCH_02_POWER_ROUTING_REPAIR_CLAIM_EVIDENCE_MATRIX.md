# PCB Batch 02 Power Routing Repair Claim Evidence Matrix

Date: `2026-05-08`

| Claim | Evidence |
| --- | --- |
| The live PCB changed | `kicad_pcb` hash changed from `1AA99163...` to `2349A4D2...` |
| `/+5V_FUSED` was rerouted | post-save net summary in `PCB_BATCH_02_TRACE_CHANGE_SUMMARY.md` and live `summary` output |
| `/+5V_PROTECTED` local feed was widened and cleaned | post-save net summary in `PCB_BATCH_02_TRACE_CHANGE_SUMMARY.md` and live `summary` output |
| `/+5V_IN` was intentionally left unchanged | copied-board DRC failures recorded in the batch report and failed-attempt log |
| Post-edit DRC has `0` violations and `27` unconnected items | `reports/PCB_BATCH_02_POWER_ROUTING_REPAIR_DRC.json` |
| `10` detectable unrouted nets remain | `reports/LIVE_PROJECT_STATE.json` after `build_live_project_state.py --apply` |
| Visual exports exist | `_verification/pcb_visual/pcb_batch_02_top.svg`, `_verification/pcb_visual/pcb_batch_02_bottom.svg`, `_verification/pcb_visual/pcb_batch_02_top.png`, `_verification/pcb_visual/pcb_batch_02_bottom.png` |
