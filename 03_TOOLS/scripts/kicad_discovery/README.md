# KiCad Discovery

These scripts provide portable, read-only KiCad discovery for fresh ZIP or clone users.

## Purpose

- detect a local KiCad install without assuming `C:\Users\LJ`
- find `kicad.exe` and `kicad-cli`
- probe `pcbnew` availability when possible
- support local overrides when KiCad is installed in a non-default location
- keep CI and Codespaces safe when KiCad is not installed

## Included Scripts

- `find_kicad.py`
  - emits JSON describing the detected KiCad root, CLI, GUI, and `pcbnew` status
- `validate_kicad_install.py`
  - prints a human-readable PASS/WARN/FAIL summary and can hard-fail when KiCad is required

## Common Usage

```powershell
python 03_TOOLS/scripts/kicad_discovery/find_kicad.py
python 03_TOOLS/scripts/kicad_discovery/validate_kicad_install.py
python 03_TOOLS/scripts/kicad_discovery/validate_kicad_install.py --require-kicad --require-cli
```

## Detection Order

1. explicit CLI arguments such as `--kicad-root` or `--kicad-cli`
2. environment variables such as `KICAD_ROOT`, `KICAD_CLI`, and `KICAD_EXE`
3. `PATH`
4. common install paths

Windows install roots currently checked include common KiCad 9, 8, and 7 locations under:

- `C:\Program Files\KiCad\9.0`
- `C:\Program Files\KiCad\8.0`
- `C:\Program Files\KiCad\7.0`

## CI And Codespaces

These scripts do not require KiCad to exist. Missing KiCad should be treated as a warning for docs/script environments and as a failure only when a live KiCad workflow explicitly requires it.
