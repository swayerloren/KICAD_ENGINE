# Real KiCad PCB Routing Bridge Claim Evidence Matrix

Record kind: `claim_evidence_matrix`
Created: `2026-05-07T21:00:12`
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
| A read-only bridge now exists from copied .kicad_pcb files into the routing-engine schema and audit flow, but active-project routing remains blocked. | 14_LAYOUT_AUTOMATION bridge scripts, real_board_tests outputs, REAL_KICAD_BOARD_EXTRACTION_TEST_REPORT.md, copied-board summary report, py_compile results, and final ESP32_CSI_WIFI_NODE SHA256 hashes. | `VERIFIED_BY_COMMAND` | `HIGH` | `LOW_RISK` | `NO` | The bridge still leaves some fields NOT_EXTRACTED and does not make active-project routing permissible. |

## Details

Main claims: the bridge scripts exist, copied-board extraction and DRC-coupled audit ran successfully, ordinary copper zones are no longer misclassified as keepouts, and the active ESP32 project KiCad files were not modified.
