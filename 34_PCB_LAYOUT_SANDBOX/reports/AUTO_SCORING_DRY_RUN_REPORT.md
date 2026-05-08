# Auto Scoring Dry Run Report

Date: `2026-05-07`

Scope: validate the automatic PCB layout variant scoring, comparison, selection, and approval engine without touching any KiCad design files.

## Validation Steps

1. Python syntax-check passed for:
   - `scripts/score_layout_variant.py`
   - `scripts/compare_layout_variants.py`
   - `scripts/auto_select_best_variant.py`
   - `scripts/auto_approve_selected_variant.py`
2. Sample variants created under:
   - `reports/dry_run_samples/variant_a.json`
   - `reports/dry_run_samples/variant_b.json`
   - `reports/dry_run_samples/variant_c.json`
3. Dry-run scoring executed for all three variants.
4. Dry-run comparison, auto-selection, and selected-variant auto-approval executed.

## Dry Run Results

| Variant | Score | Variant status | Notes |
| --- | ---: | --- | --- |
| `VARIANT_A` | `71` | `AUTO_BLOCKED_BAD_LAYOUT` | No hard fail, but below pass threshold |
| `VARIANT_B` | `53` | `FAIL` | Hard-failed on blocked antenna keepout and projected trace crossing |
| `VARIANT_C` | `89` | `PASS` | Highest-ranked non-failed candidate |

## Selection Result

- comparison status: `PASS`
- selected variant: `VARIANT_C`
- selection status: `AUTO_SELECTED`
- selection reason: `VARIANT_C` is the highest-ranked non-failed variant and scored `89`

## Auto Approval Result

- selected variant: `VARIANT_C`
- selected variant status: `PASS`
- auto approval status: `AUTO_APPROVED_FOR_PCB_WORK`

## Output Files

- `reports/dry_run_samples/variant_a.score.json`
- `reports/dry_run_samples/variant_b.score.json`
- `reports/dry_run_samples/variant_c.score.json`
- `reports/dry_run_samples/variant_compare.json`
- `reports/dry_run_samples/auto_selected.json`
- `reports/dry_run_samples/auto_approved.json`

## Conclusion

The engine now:

- scores each variant with the requested category weights
- applies DRC/precheck and uncertainty penalties
- rejects hard-failed candidates from selection
- auto-selects the best remaining candidate
- maps the selected candidate to `AUTO_APPROVED_FOR_PCB_WORK` or a specific `AUTO_BLOCKED_*` status

## No-KiCad-Edit Check

No `.kicad_sch`, `.kicad_pcb`, or `.kicad_pro` files were edited during this task.

