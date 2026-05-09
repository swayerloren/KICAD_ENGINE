# KiCad Python Context

These helpers handle the portability gap between the repo's normal Python runtime and KiCad's `pcbnew` Python bindings.

## Why This Exists

- many repo scripts can run with normal Python plus `kicad-cli`
- some board-aware workflows need `pcbnew`
- normal Python may not match the Python DLL version bundled with KiCad
- on Windows, this often means Python `3.12` cannot import a KiCad build that ships `python311.dll`

Do not assume `pcbnew` should import inside every Python shell. Detect the current machine first.

## Included Scripts

- `kicad_python_context.py`
  - emits JSON describing the current Python runtime, the detected KiCad Python runtime, and whether `pcbnew` is usable directly or only through KiCad Python
- `pcbnew_import_check.py`
  - emits PASS/WARN/FAIL without opening KiCad GUI windows or triggering wxWidgets popups

## Common Usage

```powershell
python 03_TOOLS/scripts/kicad_api/kicad_python_context.py
python 03_TOOLS/scripts/kicad_api/pcbnew_import_check.py
python 03_TOOLS/scripts/kicad_api/pcbnew_import_check.py --require-pcbnew
```

## Interpretation

- `PASS`
  - the current Python interpreter can import `pcbnew` directly
- `WARN`
  - the current Python interpreter cannot import `pcbnew`, but a KiCad-compatible Python context exists and board-aware scripts should re-enter through KiCad Python
- `FAIL`
  - no workable `pcbnew` context was found

## Rule

For basic ZIP onboarding, docs work, health checks, and CI, `pcbnew` is optional.

For board-aware workflows, agents should:

1. run the health check
2. run the import/context probe
3. use `kicad-cli` when `pcbnew` is not required
4. re-enter through KiCad Python when a real `pcbnew` workflow is required
