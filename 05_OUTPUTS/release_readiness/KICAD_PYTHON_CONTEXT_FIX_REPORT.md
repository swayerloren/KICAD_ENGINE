# KiCad Python Context Fix Report

Date: `2026-05-09`
Task type: `GITHUB_DOCS_ONLY`

## Summary

Fixed the portability gap where normal Python `3.12` could not use KiCad's `pcbnew` bindings safely. The repo now detects KiCad-compatible Python context explicitly, keeps `pcbnew` optional for baseline onboarding and CI, and routes board-aware scripts through KiCad's bundled `python.exe` when needed.

## Audit Findings

- Current repo/runtime Python on this machine: `3.12.10`
- Detected KiCad root: `C:\Program Files\KiCad\9.0`
- Detected KiCad Python: `C:\Program Files\KiCad\9.0\bin\python.exe`
- KiCad Python version: `3.11.5`
- Embedded KiCad DLL: `python311.dll`
- Direct current-Python `pcbnew` import: `ModuleNotFoundError`
- Forced discovered-path import into Python `3.12`: `ImportError` with `Module use of python311.dll conflicts with this version of Python.`
- KiCad Python `pcbnew` import: `PASS`

## Classification

### Scripts that require pcbnew

- `14_LAYOUT_AUTOMATION/scripts/_kicad_pcb_bridge_common.py`
- `14_LAYOUT_AUTOMATION/scripts/_placement_common.py`
- `14_LAYOUT_AUTOMATION/scripts/extract_kicad_*`
- `03_TOOLS/scripts/project_state/project_state_common.py`
- `03_TOOLS/scripts/kicad_pcb_intelligence/repair_esp32_csi_wifi_node_*`
- `03_TOOLS/scripts/pcb_routing/esp32_csi_*`

These scripts now use guarded shared-entry behavior instead of assuming the repo's base interpreter can import `pcbnew` directly.

### Scripts that can use kicad-cli or stay read-only without pcbnew

- `health_check.py`
- `health_check.ps1`
- `03_TOOLS/scripts/kicad_discovery/find_kicad.py`
- `03_TOOLS/scripts/kicad_discovery/validate_kicad_install.py`
- `03_TOOLS/scripts/python_env_check.py`
- task-contract validators
- routing-geometry fixture checks
- docs and portability workflows

### CI handling

- GitHub Actions now run `pcbnew_import_check.py` in no-fail mode
- read-only placement scoring is skipped when no workable `pcbnew` context exists
- CI does not require KiCad GUI or `pcbnew`

## Changes Applied

### New KiCad Python context helpers

- `03_TOOLS/scripts/kicad_api/kicad_python_context.py`
- `03_TOOLS/scripts/kicad_api/pcbnew_import_check.py`
- `03_TOOLS/scripts/kicad_api/README.md`
- `docs/KICAD_PYTHON_CONTEXT.md`

### Detection and health updates

- `03_TOOLS/scripts/kicad_discovery/find_kicad.py`
- `03_TOOLS/scripts/kicad_discovery/validate_kicad_install.py`
- `health_check.py`
- `health_check.ps1`
- `03_TOOLS/scripts/python_env_check.py`

### Shared runtime bridge and callers

- `14_LAYOUT_AUTOMATION/scripts/_kicad_pcb_bridge_common.py`
- patched first-party direct-import callers under:
  - `03_TOOLS/scripts/kicad_pcb_intelligence/`
  - `03_TOOLS/scripts/pcb_routing/`

### Docs and CI

- `docs/HEALTH_CHECK.md`
- `docs/PYTHON_SETUP.md`
- `docs/LOCAL_DEV_SETUP.md`
- `LOCAL_SETUP_REQUIREMENTS.md`
- `EXTERNAL_DEPENDENCIES.md`
- `03_TOOLS/scripts/kicad_discovery/README.md`
- `.github/workflows/ci.yml`
- `.github/workflows/docs-check.yml`

## Validation

- `python health_check.py --no-write`
  - `PASS=18 WARN=2 FAIL=0`
- `powershell -ExecutionPolicy Bypass -File .\health_check.ps1 -NoWrite`
  - `PASS=18 WARN=2 FAIL=0`
- `python 03_TOOLS/scripts/kicad_api/pcbnew_import_check.py`
  - `WARN`
  - current Python direct import: `False`
  - KiCad Python import: `True`
  - recommended context: `KICAD_PYTHON`
- `python 03_TOOLS/scripts/kicad_api/kicad_python_context.py`
  - reported current `3.12.10`, KiCad Python `3.11.5`, embedded `python311.dll`, and KiCad-Python-only `pcbnew` availability
- `python 03_TOOLS/scripts/kicad_discovery/validate_kicad_install.py`
  - `PASS` for KiCad root, GUI, CLI, and `pcbnew`
- `python 03_TOOLS/scripts/kicad_discovery/find_kicad.py`
  - `pcbnew.status = AVAILABLE_IN_KICAD_PYTHON`
- `python -m py_compile ...`
  - passed for all changed Python files
- `git diff --name-only -- '*.kicad_sch' '*.kicad_pcb' '*.kicad_pro'`
  - no files returned

## Expected Behavior After This Fix

- ZIP onboarding remains usable without `pcbnew`
- `kicad-cli` and KiCad GUI remain enough for many tasks
- board-aware scripts can detect the mismatch and re-enter through KiCad Python
- GitHub Actions can validate repo portability without requiring KiCad GUI or `pcbnew`

## Remaining Gap

The current machine still cannot import `pcbnew` directly from Python `3.12`, so the warning is expected. That is no longer a portability blocker because the repo now detects the mismatch and handles it explicitly.

## Operational Note

This meaningful repo task incremented the active project prompt counter to `5`. The next engineering task on `ESP32_CSI_WIFI_NODE` should run:

```powershell
python 03_TOOLS/scripts/maintenance/run_maintenance_cycle.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE
```
