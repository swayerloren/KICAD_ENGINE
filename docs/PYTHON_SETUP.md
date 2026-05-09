# Python Setup

KiCad Engine does not require a hidden repo-local virtual environment for the basic ZIP or clone workflow.

## Required

- Python `3.11+`

Core portability scripts such as `health_check.py`, `03_TOOLS/scripts/python_env_check.py`, and the KiCad discovery scripts use only the Python standard library.

## Basic Check

```powershell
python --version
python 03_TOOLS/scripts/python_env_check.py
```

## Optional Package Installs

Most users do not need extra pip packages for the basic repo workflow.

Optional Windows GUI helpers can be installed with:

```powershell
python -m pip install ".[windows-gui]"
```

Those extras support things like:

- `pywinauto`
- `pyautogui`
- `pygetwindow`
- `Pillow`
- `psutil`

## KiCad Python / pcbnew

`pcbnew` is not a normal PyPI dependency for this repo. It comes from a local KiCad install.

Use the KiCad discovery layer to check it:

```powershell
python 03_TOOLS/scripts/kicad_discovery/find_kicad.py
python 03_TOOLS/scripts/kicad_discovery/validate_kicad_install.py
python 03_TOOLS/scripts/kicad_api/kicad_python_context.py
python 03_TOOLS/scripts/kicad_api/pcbnew_import_check.py
```

Normal Python may not import `pcbnew` directly when KiCad ships a different embedded Python version. In that case, board-aware scripts should switch to KiCad's own Python context instead of assuming the repo's base interpreter can load KiCad bindings.

If `pcbnew` is unavailable, the repo can still do docs, audits, health checks, task-contract validation, and routing-geometry fixture tests. Board-aware scripts that inspect or edit real `.kicad_pcb` files will remain blocked until KiCad is installed locally or a KiCad-compatible Python context is available.
