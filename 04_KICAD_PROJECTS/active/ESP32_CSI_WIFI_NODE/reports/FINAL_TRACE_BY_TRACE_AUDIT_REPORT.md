# Final Trace By Trace Audit Report

Status: `REVIEW_ONLY_PARTIAL_REPAIR_APPLIED`

Generated: `2026-05-08T12:59:26-04:00`

Project: `ESP32_CSI_WIFI_NODE`

Target PCB: `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb`

## Identity

- Backup path: `99_BACKUPS\pre_codex_edits\20260508_124307_ESP32_CSI_WIFI_NODE_final_trace_audit`
- PCB hash before: `38DB921F4A13FFE0C52F2924E2C3E389D404AAF6D4BE1D8D26377D066ECBFC1D`
- PCB hash after: `A90967ABC127674F7008562AAEE46744456F2421550E4B64AD71E91B5D3CF697`
- PCB timestamp before: `2026-05-08 12:31:56 -04:00`
- PCB timestamp after: `2026-05-08 12:56:52 -04:00`
- PCB changed: `YES`

## Audit Scope

- Routed nets audited: `18`
- Track segments audited: `74`
- Vias audited: `32`
- Zone entries audited: `3`
  - `1` antenna keepout zone
  - `2` GND copper zones
- DRC before repair: `0` violations, `17` unconnected items
- DRC after repair: `0` violations, `17` unconnected items

## Routing Scorecard

| Category | Result | Notes |
| --- | --- | --- |
| `critical_net_completeness` | `FAIL` | `/+5V_PROTECTED`, `/BOOT0`, `/ESP_EN`, `/DM_C`, `/DM_E`, `/DP_C`, `/DP_E` remain incomplete |
| `power_path_quality` | `PASS_WITH_REPAIR` | power widths are appropriate and the one acute protection-rail dogleg was repaired |
| `usb_path_quality` | `FAIL` | D+/D- nets remain unrouted; only support nets `/CC1`, `/CC2`, `/SHIELD` exist |
| `rf_keepout_compliance` | `PASS` | no front-copper track crosses the top antenna keepout rectangle |
| `via_count_reasonableness` | `PASS` | vias are concentrated in `+3V3`, `GND`, `SHIELD`, `STATUS_LED`, and duplicated VBUS tie, with no unnecessary via added in this pass |
| `unrouted_net_count` | `FAIL` | DRC still reports `17` unconnected items |
| `drc_risk` | `PASS_WITH_BLOCKERS` | no rule violations, but connectivity remains incomplete |
| `trace_audit_completeness` | `PASS` | every routed net was audited below |
| `human_review_risk` | `HIGH` | USB, power, RF keepout, and incomplete control/testpoint routing still require human review |

Overall routing scorecard status: `AUTO_BLOCKED_BAD_LAYOUT`

## Net By Net Audit

| Net | From / To Summary | Layers | Widths mm | Segments | Vias | Quality Notes | Issues | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `+3V3` | regulator output spine to ESP32 supply, pull-ups, and right-edge test rail | `F.Cu`, `B.Cu` | `0.35`, `0.45`, `0.50` | `21` | `10` | width progression is reasonable; bottom supply spine and stitching are coherent | several orthogonal corners remain but none are acute; acceptable on current incomplete board | `ACCEPTED` |
| `GND` | two copper pours plus stitching-via network | `zones`, `F.Cu/B.Cu vias` | zone + `0.50` / `0.65` vias | `0` segments | `15` | ground strategy exists and supports the current board; no antenna-keepout crossing seen | keepout is respected; final return-current review still depends on completing remaining signal routing | `ACCEPTED` |
| `unconnected-(J2-VBUS-PadA4)` | duplicated USB-C VBUS pad pair tie | `B.Cu` | `0.20` | `3` | `2` | compact local pad-pair tie only | no clear defect | `ACCEPTED` |
| `/+5V_IN` | `J1` input to `F1` | `F.Cu` | `0.75` | `3` | `0` | direct, wide, and compact | no acute bends; no reroute needed | `ACCEPTED` |
| `/+5V_FUSED` | `F1` to `Q1` fused feed | `F.Cu` | `0.75` | `2` | `0` | clean wide entry with single 45-style turn | no defect found | `ACCEPTED` |
| `/+5V_PROTECTED` | `Q1/C2` protected rail into regulator input branch | `F.Cu` | `0.50`, `0.75` | `10` | `0` | widths and branching are appropriate after repair | acute dogleg removed in this pass; TP1 branch still unrouted | `REPAIRED_AND_ACCEPTED` |
| `/BUCK_BST` | `U1` BST support link | `F.Cu` | `0.25` | `2` | `0` | short local support route | no defect found | `ACCEPTED` |
| `/BUCK_SW` | `U1` SW node to `L1` | `F.Cu` | `0.50` | `2` | `0` | short and compact regulator loop element | no defect found | `ACCEPTED` |
| `/BOOT0` | local `R2` to `SW1` closure only | `F.Cu` | `0.20` | `3` | `0` | local cluster route is readable and does not create clearance trouble | still incomplete to `U2` and `TP4`; 90-degree corners remain but are provisional rather than clearly bad | `ACCEPTED_PROVISIONAL` |
| `/ESP_EN` | local `R1/C1/SW2` closure only | `F.Cu` | `0.20` | `4` | `0` | local control cluster is compact and readable | still incomplete to `U2` and `TP2`; provisional orthogonal corners remain | `ACCEPTED_PROVISIONAL` |
| `/CC1` | `J2 A5` to `R6` | `F.Cu` | `0.20` | `2` | `0` | short support route; no odd via use | no defect found | `ACCEPTED` |
| `/CC2` | `J2 B5` to `R7` | `F.Cu` | `0.20` | `3` | `0` | short support route; clean enough on current geometry | no defect found | `ACCEPTED` |
| `/SHIELD` | `J2` shell to `R5` shell-bond path | `B.Cu` | `0.20` | `4` | `3` | via use is intentional and localized to shell tie strategy | no defect found | `ACCEPTED` |
| `/PLED` | local LED branch | `F.Cu` | `0.20` | `1` | `0` | single clean segment | no defect found | `ACCEPTED` |
| `/SLED` | local LED branch | `F.Cu` | `0.20` | `1` | `0` | single clean segment | no defect found | `ACCEPTED` |
| `/STATUS_LED` | ESP32 status output to LED branch | `F.Cu`, `B.Cu` | `0.20` | `5` | `2` | vertical bottom spine is simple and consistent | no defect found | `ACCEPTED` |
| `/U0TXD` | `U2` to `TP6` | `F.Cu` | `0.20` | `3` | `0` | simple right-edge spine | no defect found | `ACCEPTED` |
| `/U0RXD` | `U2` to `TP7` | `F.Cu` | `0.20` | `5` | `0` | simple right-edge spine | no defect found | `ACCEPTED` |

## Accepted Repair

- Net: `/+5V_PROTECTED`
- Why it failed audit:
  - pre-repair geometry used an acute dogleg at the regulator-input branch:
    - `22.475,70.025 -> 21.950,69.500`
    - `21.950,69.500 -> 26.400,69.500`
  - this violated the trace-quality rule even though DRC passed
- Live repair applied:
  - replaced with:
    - `22.475,70.025 -> 22.475,69.500`
    - `22.475,69.500 -> 26.400,69.500`
- Copied-board proof:
  - trial board `routing_work\20260508_091428\final_trace_audit_trials\20260508_125541\candidate_p5v_protected_cleanup.kicad_pcb`
  - trial DRC result: `0` violations, `17` unconnected items

## What Was Not Repaired

- No other routed net showed a clearly bad acute bend, obvious zig-zag, keepout strike, or unjustified via pattern worth live rerouting.
- Incomplete routes on `/BOOT0`, `/ESP_EN`, `/DM_C`, `/DM_E`, `/DP_C`, and `/DP_E` remain connectivity blockers, but they are routing-completeness issues rather than clearly bad existing copper.

## Verification

- Pre-audit inventory: `reports/FINAL_TRACE_AUDIT_PRE_INVENTORY.json`
- Post-audit inventory: `reports/FINAL_TRACE_AUDIT_POST_INVENTORY.json`
- Pre-audit DRC: `reports/FINAL_TRACE_AUDIT_DRC_PRECHECK.json`
- Post-audit DRC: `reports/FINAL_TRACE_AUDIT_DRC_POST.json`

## Final Decision

- Final PCB visual review may begin: `NO`
- Remaining blockers:
  - `17` unconnected items remain
  - USB data nets are still unrouted
  - `/BOOT0`, `/ESP_EN`, and `TP1` spine routing are still incomplete
