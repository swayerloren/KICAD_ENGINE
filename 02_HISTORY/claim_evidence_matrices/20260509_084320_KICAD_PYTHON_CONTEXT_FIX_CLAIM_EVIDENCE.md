# Claim Evidence Matrix - KiCad Python Context Fix

Date: `2026-05-09`
Task type: `GITHUB_DOCS_ONLY`

| Claim | Evidence |
| --- | --- |
| Normal repo Python and KiCad Python are mismatched on this machine. | `python 03_TOOLS/scripts/kicad_api/kicad_python_context.py` reported current Python `3.12.10`, KiCad Python `3.11.5`, and embedded `python311.dll`. |
| Forcing KiCad site-packages into Python `3.12` reproduces the expected DLL conflict. | `kicad_python_context.py` discovered-path probe reported `ImportError: Module use of python311.dll conflicts with this version of Python.` |
| A workable `pcbnew` context still exists via KiCad Python. | `python 03_TOOLS/scripts/kicad_api/pcbnew_import_check.py` returned `WARN` with `kicad_python_available = True` and recommended context `KICAD_PYTHON`. |
| First-party board-aware scripts no longer rely on raw top-level `import pcbnew`. | Patched files under `03_TOOLS/scripts/kicad_pcb_intelligence/`, `03_TOOLS/scripts/pcb_routing/`, and `14_LAYOUT_AUTOMATION/scripts/_kicad_pcb_bridge_common.py`; import audit rerun afterwards. |
| Health checks and CI no longer require `pcbnew` for baseline portability validation. | Updated `health_check.py`, `health_check.ps1`, and `.github/workflows/ci.yml`; local health check passed with `PASS=18 WARN=2 FAIL=0`. |
| No KiCad design files changed. | `git diff --name-only -- '*.kicad_sch' '*.kicad_pcb' '*.kicad_pro'` returned no files. |
