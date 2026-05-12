# Footprint Package Engine Claim Evidence Matrix

Record kind: `claim_evidence_matrix`
Created: `2026-05-10T11:56:21`
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
| The repo now has an enforceable footprint/package proof engine and a working read-only gate that blocks schematic-to-PCB claims when lock-file or high-risk evidence is missing. | 35_FOOTPRINT_PACKAGE_ENGINE/; 03_TOOLS/scripts/footprint_package/; START_HERE_FOR_AI_AGENTS.md; 00_CODEX_START/TASK_ROUTER.md; 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/footprint_package/20260510_115257/FOOTPRINT_PACKAGE_GATE_REPORT.md | `PARTIALLY_VERIFIED` | `HIGH` | `MEDIUM_RISK` | `YES` | The active project still requires lock-file population and high-risk review proof before the gate can pass. |

## Details

The claim is supported by created engine docs, created scripts, updated router/startup docs, project templates, and the generated dry-run report for ESP32_CSI_WIFI_NODE.
