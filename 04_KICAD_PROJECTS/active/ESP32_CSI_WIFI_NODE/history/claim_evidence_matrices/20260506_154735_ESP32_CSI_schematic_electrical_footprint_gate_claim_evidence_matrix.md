# ESP32 CSI schematic electrical footprint gate claim evidence matrix

Record kind: `claim_evidence_matrix`
Created: `2026-05-06T15:47:35`
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
| Major claims were tied to ERC, parser, and checker evidence. | reports/SCHEMATIC_ELECTRICAL_GATE_REPORT.md; reports/FOOTPRINT_PACKAGE_GATE_REPORT.md | `PARTIALLY_VERIFIED` | `HIGH` | `BLOCKED_UNTIL_HUMAN_REVIEW` | `YES` | High-risk electrical decisions remain unresolved. |

## Details

ERC pass verified by command. Footprint failure verified by schematic parser and annotation checker. Electrical high-risk blockers are based on schematic values, labels, and existing project reports.
