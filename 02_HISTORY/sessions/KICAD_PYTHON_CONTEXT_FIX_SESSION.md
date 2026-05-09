# KiCad Python Context Fix Session

Date: `2026-05-09`
Task type: `GITHUB_DOCS_ONLY`
Project context: `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE`

## Summary

Fixed the portability gap where `pcbnew` was unavailable from the repo's normal Python runtime by adding explicit KiCad-Python context detection, guarded import probes, and shared bridge behavior for board-aware scripts.

## Work Performed

- audited first-party scripts that require `pcbnew`
- verified the local runtime mismatch between Python `3.12` and KiCad Python `3.11`
- created a dedicated `03_TOOLS/scripts/kicad_api` helper layer
- updated discovery and health checks to distinguish general onboarding from board-aware `pcbnew` workflows
- patched first-party direct-import callers to use the shared bridge instead of raw top-level `import pcbnew`
- updated CI to probe `pcbnew` in warn-only mode and skip read-only placement scoring when unavailable
- updated public and startup-facing docs to explain the KiCad Python context rule

## Key Decisions

- basic onboarding must not hard-fail on missing `pcbnew`
- board-aware scripts should prefer KiCad's bundled `python.exe` over injecting KiCad site-packages into an incompatible interpreter
- a direct-import warning is still useful even when a workable KiCad Python context exists

## Validation

- health check passed with `PASS=18 WARN=2 FAIL=0`
- PowerShell health-check wrapper matched the Python health-check result
- `pcbnew_import_check.py` returned `WARN` with `KICAD_PYTHON` as the recommended context
- KiCad discovery now reports `AVAILABLE_IN_KICAD_PYTHON`
- changed Python files compiled successfully
- no `.kicad_sch`, `.kicad_pcb`, or `.kicad_pro` files changed

## Remaining Risk

- the current fix is verified on the current Windows KiCad 9 packaging layout
- future KiCad packaging variants may need additional root or interpreter detection patterns
- the active project's prompt counter reached `5`, so the next engineering task is blocked until `python 03_TOOLS/scripts/maintenance/run_maintenance_cycle.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE` runs
