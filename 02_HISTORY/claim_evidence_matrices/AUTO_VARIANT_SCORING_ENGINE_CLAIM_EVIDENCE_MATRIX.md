# Claim / Evidence Matrix - Auto Variant Scoring Engine

Date: `2026-05-07`

| Claim | Evidence |
| --- | --- |
| The scorer now returns `PASS`, `FAIL`, `AUTO_BLOCKED_MISSING_DATA`, or `AUTO_BLOCKED_BAD_LAYOUT` | `34_PCB_LAYOUT_SANDBOX/scripts/score_layout_variant.py`, `34_PCB_LAYOUT_SANDBOX/VARIANT_SCORING_RULES.md` |
| Hard-failed variants are excluded from automatic selection | `34_PCB_LAYOUT_SANDBOX/scripts/compare_layout_variants.py`, `34_PCB_LAYOUT_SANDBOX/scripts/auto_select_best_variant.py` |
| The selector chose `VARIANT_C` in the dry run | `34_PCB_LAYOUT_SANDBOX/reports/dry_run_samples/variant_compare.json`, `34_PCB_LAYOUT_SANDBOX/reports/dry_run_samples/auto_selected.json` |
| The approval step produced `AUTO_APPROVED_FOR_PCB_WORK` with passing context | `34_PCB_LAYOUT_SANDBOX/reports/dry_run_samples/auto_approved.json` |
| No KiCad design files were edited | task scope plus active-project hash recheck in command log |

