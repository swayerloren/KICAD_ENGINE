# ESP32_CSI_WIFI_NODE Copied Board Routing Engine Live Test Claim Evidence Matrix

Record kind: `claim_evidence_matrix`
Created: `2026-05-07T21:05:37`
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
| The routing-engine bridge works on a copied ESP32_CSI_WIFI_NODE board, but the active project remains blocked for real routing. | ESP32_CSI_WIFI_NODE_COPIED_BOARD_EXTRACTION_REPORT.md, ESP32_CSI_WIFI_NODE_COPIED_BOARD_ROUTING_AUDIT.md/.json, routing schema JSON, and active-source PCB hash evidence. | `VERIFIED_BY_COMMAND` | `HIGH` | `LOW_RISK` | `NO` | The copied-board test does not override routing gates for the live project. |

## Details

Claims covered: the copied board was created from the active PCB without modifying the source, source and copy hashes match, extraction fields were populated into routing schema JSON, and copied-board routing audit blockers were captured as evidence.
