# ESP32_CSI_WIFI_NODE Project Memory

Status: `UNVERIFIED_PROJECT_MEMORY`

Durable project-specific facts belong here. This local project memory supplements the older global project memory at `01_MEMORY/projects/ESP32_CSI_WIFI_NODE/PROJECT_MEMORY.md`.

## Project Scope

- Project: `ESP32_CSI_WIFI_NODE`
- Type: Active custom ESP32-S3 CSI WiFi node PCB workspace.
- Current status: Active design project with rough schematic draft history elsewhere in the repo.
- Manufacturing status: `NOT_FINAL`

## Durable Rules

- Keep this project separate from reusable global memory.
- Do not edit KiCad source files unless the active project, backup, rollback plan, and verification plan are confirmed.
- Treat schematic, PCB, footprint, connector, antenna, and power-path decisions as project-specific unless promoted through a reviewed global lesson.
- Live project truth now comes from `reports/LIVE_PROJECT_STATE.json`, `reports/STALE_REPORTS_AUDIT.md`, and `reports/GATE_RECONCILIATION_REPORT.md`.
- Do not trust older `NO_PCB`, `0 footprints`, or `phase 2 not done` narratives when the live board file proves otherwise.
- The routing-engine bridge can extract this project's PCB in read-only mode for audit work, but active-project routing remains blocked until the live routing blockers are cleared.
- The 2026-05-08 live critical routing pass changed the live board hash to `D147FD1FFEF47F62B229561052B08C7432EFC549B7752DC7279ECE96E6C6B6A5`.
- The current live board now shows `43` footprints, `40` tracks, `25` vias, `2` zones, `0` DRC violations, and `49` unconnected items.
- The accepted 2026-05-08 live routing subset completed `+3V3` and improved `GND`, but intentionally deferred `/BOOT0`, `/ESP_EN`, and the `TP1` `/+5V_PROTECTED` branch after copied-board rehearsals produced DRC crossings on those branches.
- The 2026-05-08 full non-critical routing pass changed the live board hash to `5E6486A2C188B68207C9FF4692618AE81BF322355ACAEE686146EF075330C2F6`.
- The current live board now shows `43` footprints, `53` tracks, `29` vias, `2` zones, `0` DRC violations, and `44` unconnected items.
- The accepted non-critical live subset completed `/PLED`, `/SLED`, `/STATUS_LED`, `/U0TXD`, and the duplicated USB-C VBUS pad-pair tie, but still deferred `/U0RXD`, `/BOOT0`, `/ESP_EN`, `TP1 /+5V_PROTECTED`, `CC1`, `CC2`, `/SHIELD`, and additional `GND` cleanup because copied-board rehearsals did not reach clean geometry for those nets.
- The `U2 pad 41` false drill-rule blocker was resolved by lowering the project minimum through-hole diameter to `0.20 mm` to match the intentional exposed-pad thermal-via drill pattern.
- Current routing continuation is still blocked by live connectivity incompleteness and routed-geometry review needs, not by missing GND strategy or `U2` drill-rule errors.
- Every future live routing pass on this board must start from a `routing_work\<timestamp>\` folder with a live PCB snapshot, `ROUTING_MASTER_LOG.md`, `TRACE_CHANGE_LOG.md`, `COMPONENT_MOVE_LOG.md`, `DRC_RUN_LOG.md`, `ROUTING_DECISION_LOG.md`, `BEFORE_AFTER_HASH_LOG.md`, and current net/trace/placement/DRC baselines.
- The 2026-05-08 `PCB_BATCH_01_DRC_AND_GND_REPAIR` live pass changed the board hash to `1AA99163F07EC867B98461F88990D059F46ACCBFB1CA4E91E33F9FD49B792489`.
- In that batch, `U2 pad 41` was confirmed already fixed on the current revision, and the real improvement came from changing both existing `GND` zones from `thermal` to `full` pad connection.
- That GND zone refinement kept DRC at `0` violations and reduced unconnected items from `44` to `27`, but routing batch 2 is still blocked by `10` detectable unrouted nets and remaining live connectivity buckets.
- The 2026-05-08 resumed `PCB_BATCH_03_USB_CONTROL_ROUTING` live pass repaired the batch-03 KiCad script and changed the live board hash to `22ED35E8FF9CC96F16014B66A2DCF669520D10A7A3C005ACEC3C68F29B9CF3F4`.
- That batch routed only the copied-board-proven USB-support subset: `/CC1`, `/CC2`, and `/SHIELD`.
- After batch 03, the live board shows `62` tracks, `32` vias, `2` zones, `0` DRC violations, `21` unconnected items, and `7` detectable unrouted nets.
- The remaining deferred nets after batch 03 are `/BOOT0`, `/ESP_EN`, `/U0RXD`, `/DP_C`, `/DP_E`, `/DM_C`, and `/DM_E`; they still require copied-board rehearsal that holds `0` DRC violations before any further live routing.
- The 2026-05-08 `PCB_BATCH_04_CONTROL_NET_ROUTING` live pass changed the board hash to `7BB955071DCABD9AA6A4B8F71F749AE14DF36F7E041F6C3FE657CDC17C62CF3C`.
- That batch routed only the copied-board-proven `/U0RXD` control net.
- After batch 04, the live board shows `67` tracks, `32` vias, `2` zones, `0` DRC violations, `20` unconnected items, and `6` detectable unrouted nets.
- `/BOOT0` and `/ESP_EN` remain deferred because current copied-board rehearsal windows still force `U0TXD` crossings, `GND` or `+3V3` shorts, or solder-mask bridges on the present placement.
- USB data routing remains blocked until `/BOOT0` and `/ESP_EN` have their own copied-board-proven `0`-violation routes.
- The 2026-05-08 final connectivity cleanup live pass changed the board hash to `38DB921F4A13FFE0C52F2924E2C3E389D404AAF6D4BE1D8D26377D066ECBFC1D`.
- That cleanup applied only the copied-board-proven local left-cluster closures for `/BOOT0` and `/ESP_EN`; it did not route the unresolved U2/test-pad/USB spine connections.
- After final cleanup, the live board shows `74` tracks, `32` vias, `2` zones, `0` DRC violations, and `17` unconnected items.
- Remaining duplicate opens on `SW1 pad 1` and `SW2 pad 1` should be treated as expected duplicate tactile-switch pads unless a future footprint review proves both pads must be copper-tied.
- Remaining blockers are the real must-route items on `/+5V_PROTECTED`, `/BOOT0`, `/ESP_EN`, `/DM_C`, `/DM_E`, `/DP_C`, and `/DP_E`; do not treat them as stale-report artifacts.
- The 2026-05-08 full trace-by-trace routing audit changed the board hash to `A90967ABC127674F7008562AAEE46744456F2421550E4B64AD71E91B5D3CF697`.
- That audit reviewed all `18` routed nets and found exactly one clearly bad routed feature worth live repair: an acute dogleg on `/+5V_PROTECTED`.
- The accepted repair replaced that acute bend with a cleaner short vertical drop plus horizontal run while preserving `0` DRC violations and `17` unconnected items.
- After the trace audit repair, the board still is not ready for final visual review because connectivity remains incomplete even though routed-trace quality is materially cleaner.
- The 2026-05-08 final LJ PCB visual review package was generated from fresh `kicad-cli pcb render` top and bottom board renders plus deterministic coordinate crops stored under `_verification/pcb_visual/`.
- For this project, direct `kicad-cli pcb render` camera-pivot close-ups were not reliable enough for top-down human inspection; deterministic crops from fresh full-board renders are the preferred review-packet method.
- The review packet is ready for LJ visual inspection, but the board itself remains `NOT_READY_NEEDS_MORE_PCB_REPAIR` while `17` unconnected items remain and `/DM_C`, `/DM_E`, `/DP_C`, and `/DP_E` are still explicitly unrouted.

## Evidence Links

- Global project memory: `01_MEMORY/projects/ESP32_CSI_WIFI_NODE/PROJECT_MEMORY.md`
- Project history: `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/history/`
- Copied-board routing-engine evidence: `14_LAYOUT_AUTOMATION/real_board_tests/reports/ESP32_CSI_WIFI_NODE_COPIED_BOARD_EXTRACTION_REPORT.md`, `14_LAYOUT_AUTOMATION/real_board_tests/reports/ESP32_CSI_WIFI_NODE_COPIED_BOARD_ROUTING_AUDIT.md`
- Placement block evidence: `reports/SCHEMATIC_TO_PCB_GATE_STATUS.md`, `reports/PCB_LAYOUT_SANDBOX_GATE_STATUS.md`, `02_HISTORY/sessions/ESP32_CSI_WIFI_NODE_REAL_PCB_UPDATE_FROM_SCHEMATIC_SESSION.md`
- Live routing-plan evidence: `reports/REAL_PCB_ROUTING_SCHEMA.json`, `reports/REAL_PCB_ROUTING_PLAN.md`, `reports/ROUTING_PRECHECK_SCORECARD.md`, `reports/ROUTING_START_BLOCKERS.md`
- Rehearsal block evidence: `reports/REAL_PCB_ROUTING_PLAN.md`, `reports/ROUTING_PRECHECK_SCORECARD.md`, `reports/ROUTING_START_BLOCKERS.md`
