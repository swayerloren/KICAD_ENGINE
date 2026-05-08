# Routing Decision Log

Status: `PREP_ONLY_DECISIONS_RECORDED`

Generated: `2026-05-08T09:37:20-04:00`

## Decision 1

- Timestamp: `2026-05-08T09:37:20-04:00`
- Decision: `DO_NOT_ROUTE_IN_PREP_TASK`
- Why:
  - user requested setup only
  - live board already has a safe `0`-violation state that should not be disturbed by prep work
  - routing should resume through copied-board rehearsal first for the deferred control nets

## Decision 2

- Timestamp: `2026-05-08T09:37:20-04:00`
- Decision: `USE_ROUTING_WORK_FOLDER_AS_MANDATORY_PASS_LOG`
- Why:
  - future live routing passes need before/after hashes, trace deltas, move deltas, DRC logs, and rollback evidence in one place
  - this project already accumulated stale phase narratives; future routing work needs direct live-board provenance

## Exact Next Routing Batch

- Batch 1 rehearsal only: `/BOOT0`, `/ESP_EN`, `/U0RXD`, `TP1 /+5V_PROTECTED`
- Batch 2 rehearsal only after batch 1 stays clean: `/CC1`, `/CC2`, `/SHIELD`
- Deferred until geometry is proven: USB `D+`/`D-`

## Decision 3

- Timestamp: `2026-05-08T09:50:58-04:00`
- Decision: `USE_GND_ZONE_CONNECTION_REPAIR_BEFORE_NEW_SIGNAL_ROUTING`
- Why:
  - the live board no longer has the `U2 pad 41` drill-rule blocker
  - the remaining board-state blocker in this batch is incomplete `GND` connectivity inside the existing pours
  - copied-board rehearsal with the matching `.kicad_pro` proved that switching both `GND` zones from thermal to full pad connection reduces unconnected items from `44` to `27` with `0` DRC violations

## Decision 4

- Timestamp: `2026-05-08T09:52:00-04:00`
- Decision: `DO_NOT_START_ROUTING_BATCH_2_YET`
- Why:
  - the live board improved, but phase 8 still reports `PARTIAL_ROUTING_EXISTS_NEEDS_AUDIT`
  - live DRC still has `27` unconnected items
  - `10` detectable unrouted nets remain: `/BOOT0`, `/CC1`, `/CC2`, `/DM_C`, `/DM_E`, `/DP_C`, `/DP_E`, `/ESP_EN`, `/SHIELD`, `/U0RXD`

## Decision 5

- Timestamp: `2026-05-08T10:15:29-04:00`
- Decision: `USE_COPIED_BOARD_REHEARSAL_FOR_POWER_BATCH_02`
- Why:
  - this batch edits real power copper on the live board, so rollback evidence must exist before any rip-up
  - `/+5V_IN`, `/+5V_FUSED`, and `/+5V_PROTECTED` can be improved without disturbing USB or deferred control nets
  - `+3V3`, `/BUCK_SW`, and `/BUCK_BST` already provide working connectivity and should remain untouched unless the rehearsal proves a strictly better local geometry

## Decision 6

- Timestamp: `2026-05-08T10:33:16-04:00`
- Decision: `REJECT_DIRECT_POWER_PATH_SIMPLIFICATIONS_THAT_BREAK_CLEARANCE`
- Why:
  - copied-board rehearsal showed that a straightened `/+5V_IN` corridor crosses too close to `J1 pad 1 GND`
  - copied-board rehearsal showed that flattening the `/+5V_PROTECTED` branch through `C2` creates a real short and solder-mask bridge against `C2 pad 1 GND`
  - therefore `/+5V_IN` remains accepted as-is and the left-side `D3 -> C2` protected branch keeps its existing geometry

## Decision 7

- Timestamp: `2026-05-08T10:33:51-04:00`
- Decision: `APPLY_LOCAL_PROTECTED_RAIL_CLEANUP_AND_FUSED_LINK_REWRITE`
- Why:
  - rerouting `F1 -> Q1` as a long horizontal followed by a single 45-degree entry is cleaner and keeps `0` DRC violations
  - widening the `C2 -> U1` protected-rail feed from `0.50 mm` to `0.75 mm` for most of the run improves the regulator input path without disturbing the clearance-constrained left branch
  - the copied-board rehearsal proved this exact candidate keeps `0` violations and `27` unconnected items

## Decision 8

- Timestamp: `2026-05-08T11:12:19-04:00`
- Decision: `APPLY_ONLY_THE_USB_SUPPORT_SUBSET_PROVEN_ON_CURRENT-BOARD_REHEARSAL`
- Why:
  - the copied-board trial `20260508_110218_usb_low3` held `0` DRC violations and reduced unconnected items from `27` to `21`
  - no current-board rehearsal candidate for `/DM_C`, `/DP_C`, `/DM_E`, `/DP_E`, `/BOOT0`, `/ESP_EN`, or `/U0RXD` has yet survived DRC cleanly
  - the stop-condition rule is to preserve the live board's current `0`-violation geometry rather than forcing speculative USB/control routes into the production file

## Decision 9

- Timestamp: `2026-05-08T11:23:50-04:00`
- Decision: `RESUME_BATCH_03_FROM_PROVEN_DELTA_INSTEAD_OF_RESTARTING_THE_PASS`
- Why:
  - the interrupted run already isolated the copied-board delta and confirmed that the live production file remained unchanged at hash `2349A4D2679F7ACAE1199FC302E42AAC69B84234CB12214031CFD63993CE172E`
  - restarting broad rehearsal would waste time and risk drift from the already-proven `/CC1`, `/CC2`, `/SHIELD` candidate
  - the batch-03 script needed a safety repair for via-summary extraction before it could be trusted to complete cleanly under KiCad Python

## Decision 10

- Timestamp: `2026-05-08T11:26:44-04:00`
- Decision: `COMPLETE_BATCH_03_WITH_USB_SUPPORT_ONLY_AND_DEFER_THE_REST`
- Why:
  - the repaired batch-03 script applied the copied-board-proven `/CC1`, `/CC2`, `/SHIELD` delta directly to the live board and changed the production PCB hash
  - live DRC improved to `21` unconnected items with `0` violations and the detectable unrouted-net list dropped from `10` to `7`
  - `/BOOT0`, `/ESP_EN`, `/U0RXD`, `/DP_C`, `/DP_E`, `/DM_C`, and `/DM_E` remain deferred because no batch-03 copied-board rehearsal for those nets held `0` DRC violations on the current board

## Decision 11

- Timestamp: `2026-05-08T11:43:27-04:00`
- Decision: `START_BATCH_04_WITH_NEW_COPIED-BOARD_SEARCH_INSTEAD_OF_REUSING_FAILED_BATCH-03_CONTROL_PATHS`
- Why:
  - prior rehearsal artifacts prove the remaining control nets are sensitive to the current right-side and lower-mid copper field
  - none of the saved batch-03 `/BOOT0`, `/ESP_EN`, or `/U0RXD` candidates held `0` DRC violations
  - batch 04 therefore starts from the current live hash and re-tests only the allowed control/UART subset against the up-to-date board

## Decision 12

- Timestamp: `2026-05-08T12:06:57-04:00`
- Decision: `APPLY_ONLY_U0RXD_AND_DEFER_BOOT0_PLUS_ESP_EN`
- Why:
  - the batch-04 copied-board recheck for `/U0RXD` held `0` violations and reduced unconnected items from `21` to `20`
  - the focused `/BOOT0` front-side search bottomed out at `4` violations because the current board geometry still forces `U0TXD` crossings and left-cluster shorts/mask bridges
  - the focused `/ESP_EN` front-side cluster search bottomed out at `19` violations with repeated `GND`, `+3V3`, and solder-mask conflicts

## Decision 13

- Timestamp: `2026-05-08T12:31:56-04:00`
- Decision: `APPLY_ONLY_LOCAL_CONTROL_CLUSTER_CLEANUP_AND_REJECT_USB_LOCAL_REHEARSAL`
- Why:
  - the copied-board `candidate_control_local` preserved `0` DRC violations and reduced unconnected items from `20` to `17`
  - the copied-board `candidate_control_usb_local` reduced opens further but introduced `4` real violations, including `/DM_C` to `/DM_E` and `/DP_C` to `/DM_C` shorts
  - the remaining switch duplicate-pad opens are better classified as expected footprint behavior than force-bridged on the live board

## Decision 14

- Timestamp: `2026-05-08T12:56:52-04:00`
- Decision: `REPAIR_ONLY_THE_P5V_PROTECTED_ACUTE_DOGLEG_AND_ACCEPT_THE_REST`
- Why:
  - the trace-by-trace audit found one clearly bad routed feature: a true acute bend on the `/+5V_PROTECTED` regulator-input branch
  - copied-board rehearsal proved the vertical-plus-horizontal replacement keeps `0` DRC violations and the same `17` unconnected items
  - the remaining routed nets are incomplete or provisional in places, but they do not currently show clearly bad geometry that justifies more live copper churn
