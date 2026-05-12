# Schematic Layout Engine Claim Evidence Matrix

Record kind: `claim_evidence_matrix`
Created: `2026-05-10T11:35:04`
Scope: `global`
Project: `N/A`
Severity: `MEDIUM`
Confidence: `HIGH`
Claim status: `PARTIALLY_VERIFIED`
Risk label: `MEDIUM_RISK`
Gate result: `PASS_WITH_WARNINGS`
Human review required: `YES`

## Matrix

| Claim | Evidence | Claim Status | Confidence | Risk | Human Review Required | Issue |
| --- | --- | --- | --- | --- | --- | --- |
| The repo now has a schematic layout engine that extracts, audits, scores, and plans schematic cleanup in read-only mode. | 03_TOOLS/scripts/schematic_layout/; 34_SCHEMATIC_QUALITY_ENGINE/SCHEMATIC_LAYOUT_ALGORITHM.md; 34_SCHEMATIC_QUALITY_ENGINE/FUNCTIONAL_BLOCK_TEMPLATES.md; 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/schematic_layout/20260510_113053/SCHEMATIC_LAYOUT_REVIEW.md | `PARTIALLY_VERIFIED` | `HIGH` | `MEDIUM_RISK` | `YES` | Apply-mode schematic rewriting remains intentionally blocked and the active schematic still fails readability. |

## Details

The claim is supported by the new schematic-layout scripts, the new 34-series layout docs, prompt updates, and the generated project review packet.
