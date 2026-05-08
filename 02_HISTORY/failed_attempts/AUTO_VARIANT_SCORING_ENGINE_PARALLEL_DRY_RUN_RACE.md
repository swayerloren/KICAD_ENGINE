# Failed Attempt - Auto Variant Scoring Engine Parallel Dry Run Race

Date: `2026-05-07`

## What Failed

The first dry-run pass launched dependent commands in parallel. `auto_approve_selected_variant.py` ran before the `auto_selected.json` dependency was guaranteed to exist.

## Impact

No repo damage. The dry-run output set was incomplete until the commands were rerun sequentially.

## Resolution

Rerun selection and approval steps serially for dependent outputs.

