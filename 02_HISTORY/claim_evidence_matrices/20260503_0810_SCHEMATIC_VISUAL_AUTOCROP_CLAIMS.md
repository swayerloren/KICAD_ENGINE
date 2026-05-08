# Claim/Evidence Matrix: Schematic Visual Autocrop Setup

Record kind: `claim_evidence_matrix`
Created: `2026-05-03T08:10:00`
Scope: `global`
Severity: `LOW`
Confidence: `HIGH`
Claim status: `PARTIALLY_VERIFIED`
Risk label: `MEDIUM_RISK`
Gate result: `PASS_WITH_WARNINGS`
Human review required: `YES`

| Claim | Evidence | Status | Confidence | Human review required |
| --- | --- | --- | --- | --- |
| Visual workflow files were created. | `03_TOOLS/kicad` and `03_TOOLS/scripts/visual` files exist. | `VERIFIED_BY_FILE` | `HIGH` | `NO` |
| PowerShell and Python syntax validation passed. | Parser and `py_compile` commands completed successfully. | `VERIFIED_BY_COMMAND` | `HIGH` | `NO` |
| Active project autocrops were generated. | `CLOSE_UP_REVIEW.json` reports 13 SVG crops and 13 PNG crops. | `VERIFIED_BY_COMMAND` | `HIGH` | `YES` |
| Active project visual review passed. | Not claimed; generated status is `FAIL`. | `CONTRADICTED` | `HIGH` | `YES` |
| Visual crops prove schematic or footprint correctness. | Not claimed. | `UNVERIFIED` | `HIGH` | `YES` |

## Notes

The generated visual report is evidence for gate review, not approval for PCB update.
