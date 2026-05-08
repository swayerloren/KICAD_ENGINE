# PCB Layout Sandbox Scripts

## Purpose

These scripts score, compare, auto-select, and auto-approve PCB layout variants before any real `.kicad_pcb` edit.

## Scripts

### `score_layout_variant.py`

Scores one variant and returns one of:

- `PASS`
- `FAIL`
- `AUTO_BLOCKED_MISSING_DATA`
- `AUTO_BLOCKED_BAD_LAYOUT`

### `compare_layout_variants.py`

Compares at least three variants, ranks them, and records the best non-failed candidate.

### `auto_select_best_variant.py`

Picks the highest-ranked non-failed candidate and marks it:

- `AUTO_SELECTED`

or, if every candidate hard-fails:

- `AUTO_BLOCKED_BAD_LAYOUT`

### `auto_approve_selected_variant.py`

Combines the selected candidate with project-level approval context and returns:

- `AUTO_APPROVED_FOR_PCB_WORK`
- `AUTO_BLOCKED_MISSING_DATA`
- `AUTO_BLOCKED_BAD_LAYOUT`
- `AUTO_BLOCKED_ROUTING_FEASIBILITY_FAIL`
- `AUTO_BLOCKED_HIGH_RISK_FOOTPRINT_UNVERIFIED`
- `AUTO_BLOCKED_MECHANICAL_CONFLICT`
- `AUTO_BLOCKED_ANTENNA_KEEPOUT_VIOLATION`
- `AUTO_BLOCKED_CONNECTOR_ORIENTATION_UNKNOWN`
- `AUTO_BLOCKED_DRC_PRECHECK_FAIL`

## Core Rule

The selector must not choose a hard-failed variant, even if it has the highest numeric score.

## Variant Input

Each variant file may be:

- `.json`
- Markdown with one fenced `json` block

Expected fields include:

- category scores
- DRC/precheck risk
- human uncertainty risk
- connector presence/orientation booleans
- RF keepout booleans
- board-shape and board-dimension evidence booleans
- footprint evidence booleans
- routing-feasibility booleans

## Approval Context Input

`auto_approve_selected_variant.py` expects project-level boolean evidence for:

- schematic gate
- ERC
- KiCad-native annotation verification
- footprint completeness
- high-risk footprint evidence
- connector orientation
- board shape and dimensions
- RF keepout definition
- variant-count and scorecard evidence
- routing feasibility
- DRC/precheck blocker state

## Example Commands

```powershell
python 34_PCB_LAYOUT_SANDBOX/scripts/score_layout_variant.py 34_PCB_LAYOUT_SANDBOX/reports/dry_run_samples/variant_a.json
python 34_PCB_LAYOUT_SANDBOX/scripts/compare_layout_variants.py 34_PCB_LAYOUT_SANDBOX/reports/dry_run_samples/variant_a.json 34_PCB_LAYOUT_SANDBOX/reports/dry_run_samples/variant_b.json 34_PCB_LAYOUT_SANDBOX/reports/dry_run_samples/variant_c.json
python 34_PCB_LAYOUT_SANDBOX/scripts/auto_select_best_variant.py 34_PCB_LAYOUT_SANDBOX/reports/dry_run_samples/variant_a.json 34_PCB_LAYOUT_SANDBOX/reports/dry_run_samples/variant_b.json 34_PCB_LAYOUT_SANDBOX/reports/dry_run_samples/variant_c.json
python 34_PCB_LAYOUT_SANDBOX/scripts/auto_approve_selected_variant.py 34_PCB_LAYOUT_SANDBOX/reports/dry_run_samples/auto_selected.json 34_PCB_LAYOUT_SANDBOX/reports/dry_run_samples/approval_context_pass.json
```
