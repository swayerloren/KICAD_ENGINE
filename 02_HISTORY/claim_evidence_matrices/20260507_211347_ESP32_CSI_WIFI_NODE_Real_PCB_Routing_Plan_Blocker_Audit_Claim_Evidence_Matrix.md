# ESP32_CSI_WIFI_NODE Real PCB Routing Plan Blocker Audit Claim Evidence Matrix

Record kind: `claim_evidence_matrix`
Created: `2026-05-07T21:13:47`
Scope: `global`
Project: `N/A`
Severity: `LOW`
Confidence: `HIGH`
Claim status: `VERIFIED_BY_COMMAND`
Risk label: `LOW_RISK`
Gate result: `PASS_WITH_WARNINGS`
Human review required: `NO`

## Matrix

| Claim | Evidence | Claim Status | Confidence | Risk | Human Review Required | Issue |
| --- | --- | --- | --- | --- | --- | --- |
| A real routing plan was derived from the live PCB in read-only mode, but the correct final status is ROUTING_BLOCKED. | REAL_PCB_ROUTING_SCHEMA.json, real_board_routing_audit_summary.md, score.json, and the three requested project report files. | `VERIFIED_BY_COMMAND` | `HIGH` | `LOW_RISK` | `NO` | USB D+/D- pair classification is still weak on this board because current naming did not auto-resolve to USB_PAIR role. |

## Details

Claims covered: live-board extraction succeeded, critical/power/GND/unrouted information was derived from the real PCB, no routing was performed, and the exact blockers were preserved in project reports.
