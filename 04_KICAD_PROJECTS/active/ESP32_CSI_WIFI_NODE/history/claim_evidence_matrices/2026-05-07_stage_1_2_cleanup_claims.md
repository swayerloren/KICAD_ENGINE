# Claim Evidence Matrix - Stage 1/2 Cleanup

Date: `2026-05-07`

| Claim | Evidence | Status |
|---|---|---|
| Backup was created before PCB edits | `99_BACKUPS/pre_codex_edits/20260507_150607_ESP32_CSI_WIFI_NODE_stage1_stage2_cleanup_reroute` | `VERIFIED_BY_FILE` |
| Baseline board had `24` tracks and `2` vias | session count script output captured in command log | `VERIFIED_BY_COMMAND` |
| Current board has `26` tracks and `2` vias | post-route count script output captured in command log | `VERIFIED_BY_COMMAND` |
| `/+5V_IN` and `/+5V_FUSED` are routed | current board net-segment counts and visual exports | `VERIFIED_BY_BOARD_STATE` |
| Local `+3V3` route exists | board state plus `routing_stage_1_2_cleanup_bottom.svg`/top render | `VERIFIED_BY_BOARD_STATE` |
| Schematic parity is still clean | `reports/ROUTING_STAGE_1_2_CLEANUP_POST_DRC_V3.rpt` shows parity `0` | `VERIFIED_BY_DRC` |
| One buck routing defect remains | `reports/ROUTING_STAGE_1_2_CLEANUP_POST_DRC_V3.rpt` shows one `tracks_crossing` violation | `VERIFIED_BY_DRC` |
| The pass is not USB-ready | remaining `tracks_crossing`, `TP1` unrouted, angle audit fail | `VERIFIED_BY_EVIDENCE` |
