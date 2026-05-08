# BOM and footprint lock claim evidence matrix

Record kind: `claim_evidence_matrix`
Created: `2026-05-06T16:18:16`
Scope: `project`
Project: `ESP32_CSI_WIFI_NODE`
Severity: `HIGH`
Confidence: `HIGH`
Claim status: `VERIFIED_BY_FILE`
Risk label: `BLOCKED_UNTIL_HUMAN_REVIEW`
Gate result: `FAIL`
Human review required: `YES`

## Matrix

| Claim | Evidence | Claim Status | Confidence | Risk | Human Review Required | Issue |
| --- | --- | --- | --- | --- | --- | --- |
| Major claims are backed by generated lock files, source project reports, installed KiCad footprint existence checks, and unchanged schematic hash. | PRE_SCHEMATIC_BOM_LOCK.md row count; PowerShell Test-Path checks; schematic SHA256 A87C36095B9710B0596255A771921DFDAD4A5412F84DC61CD232D28FB4D444C9 | `VERIFIED_BY_FILE` | `HIGH` | `BLOCKED_UNTIL_HUMAN_REVIEW` | `YES` | Candidate footprints are not verified footprints. |

## Details

Claims: 43 physical symbols are accounted for; zero footprints are verified exact package drawing; 30 rows have candidate human-review footprints; 13 rows are blocked; schematic file hash remained unchanged.
