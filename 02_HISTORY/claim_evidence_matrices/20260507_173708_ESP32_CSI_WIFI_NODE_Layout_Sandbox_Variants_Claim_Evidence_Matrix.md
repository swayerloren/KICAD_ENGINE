# ESP32_CSI_WIFI_NODE Layout Sandbox Variants Claim Evidence Matrix

Record kind: `claim_evidence_matrix`
Created: `2026-05-07T17:37:08`
Scope: `global`
Project: `N/A`
Severity: `LOW`
Confidence: `HIGH`
Claim status: `VERIFIED_BY_COMMAND`
Risk label: `LOW_RISK`
Gate result: `PASS`
Human review required: `NO`

## Matrix

| Claim | Evidence | Claim Status | Confidence | Risk | Human Review Required | Issue |
| --- | --- | --- | --- | --- | --- | --- |
| Three project-local layout sandbox variants now exist for ESP32_CSI_WIFI_NODE, and Variant C is the highest-scoring non-failed sandbox front-runner. | 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/layout_sandbox/*.md files; score_layout_variant.py JSON outputs for A/B/C; compare_layout_variants.py JSON output selecting VARIANT_C; project memory updates and final KiCad hash recheck. | `VERIFIED_BY_COMMAND` | `HIGH` | `LOW_RISK` | `NO` | Variant C is only a provisional sandbox front-runner and is not a placement approval. |

## Details

The patch created the three requested variant plans plus a comparison scorecard and selected-plan document. The scoring scripts reported Variant C as the highest-scoring non-failed option with status NEEDS_HUMAN_REVIEW and ready_for_real_pcb_edit false.
