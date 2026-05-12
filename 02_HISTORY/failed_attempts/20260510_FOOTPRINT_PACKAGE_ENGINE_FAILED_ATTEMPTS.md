# Footprint Package Engine Failed Attempts

Date: `2026-05-10`

## Attempt

First live dry-run of:

`python 03_TOOLS/scripts/footprint_package/run_footprint_package_gate.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --no-fail`

## Failure

The first run failed with:

`ModuleNotFoundError: No module named 'schematic_quality_common'`

## Cause

`footprint_package_common.py` pointed at the wrong sibling path for the shared
schematic parser helper.

## Fix

- changed the helper lookup from `SCRIPT_DIR.parent.parent / "schematic_quality"`
  to `SCRIPT_DIR.parent / "schematic_quality"`
- simplified `run_footprint_package_gate.py` to import `read_lock_rows` and
  `audit_markdown` directly instead of using a brittle dynamic import

## Outcome

The second validation run succeeded and produced the expected gate-fail report
for missing footprint-proof evidence.
