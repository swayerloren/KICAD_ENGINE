# Human-readable schematic repair claim evidence matrix

Record kind: `claim_evidence_matrix`
Created: `2026-05-06T17:31:26`
Scope: `project`
Project: `ESP32_CSI_WIFI_NODE`
Severity: `HIGH`
Confidence: `HIGH`
Claim status: `PARTIALLY_VERIFIED`
Risk label: `BLOCKED_UNTIL_HUMAN_REVIEW`
Gate result: `FAIL`
Human review required: `YES`

## Matrix

| Claim | Evidence | Claim Status | Confidence | Risk | Human Review Required | Issue |
| --- | --- | --- | --- | --- | --- | --- |
| Major claims are backed by command reports and rendered crop inspection. | reports/SCHEMATIC_HUMAN_READABILITY_REPAIR_REPORT.md | `PARTIALLY_VERIFIED` | `HIGH` | `BLOCKED_UNTIL_HUMAN_REVIEW` | `YES` | Visual and footprint gates remain blocked. |

## Details

ERC pass is verified by kicad-cli report. Annotation pass is verified by checker output. Visual fail is based on direct rendered crop inspection. Footprint verification remains unverified because exact package drawings were not checked.
