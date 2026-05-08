# PCB Variant Scoring System Claim Evidence Matrix

Record kind: `claim_evidence_matrix`
Created: `2026-05-07T17:21:19`
Scope: `global`
Project: `N/A`
Severity: `LOW`
Confidence: `HIGH`
Claim status: `VERIFIED_BY_FILE`
Risk label: `LOW_RISK`
Gate result: `PASS`
Human review required: `NO`

## Matrix

| Claim | Evidence | Claim Status | Confidence | Risk | Human Review Required | Issue |
| --- | --- | --- | --- | --- | --- | --- |
| KiCad Engine now has a weighted PCB layout variant scoring system and two helper scripts that can score and compare candidate layouts before real PCB edits. | 34_PCB_LAYOUT_SANDBOX/VARIANT_SCORING_RULES.md, templates/VARIANT_SCORECARD_TEMPLATE.md, scripts/score_layout_variant.py, scripts/compare_layout_variants.py, README_GPT.md, FOR CHAT GPT.MD, and 01_MEMORY/DESIGN_RULES_MEMORY.md. | `VERIFIED_BY_FILE` | `HIGH` | `LOW_RISK` | `NO` | The scripts are syntax-checked but not yet proven on a real project variant set. |

## Details

The patch replaced the old loose scoring note with a strict rule set, upgraded the template to include machine-readable JSON input, and added scripts for per-variant scoring and multi-variant comparison.
