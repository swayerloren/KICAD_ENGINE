# Health Check

The repo health check is read-only. It does not edit KiCad files, install tools, or write anywhere except optional reports under `05_OUTPUTS/health_checks`.

## Run It

Python:

```powershell
python health_check.py --no-write
```

PowerShell wrapper:

```powershell
powershell -ExecutionPolicy Bypass -File .\health_check.ps1 -NoWrite
```

## What It Reports

- repo root detected
- Python detected
- Git detected
- KiCad detected yes/no
- `kicad-cli` detected yes/no
- `pcbnew` workflow availability yes/no
- whether the current Python interpreter can import `pcbnew` directly
- required onboarding docs exist yes/no
- active project exists yes/no
- local-only folder placeholders documented yes/no
- key setup scripts run with `--help`
- optional tools missing yes/no
- user action needed

## No-KiCad-Safe Mode

Missing KiCad is a warning by default so the health check can run in:

- GitHub Actions
- Codespaces
- docs-only work
- first-pass ZIP onboarding

If a local workflow actually requires KiCad, use:

```powershell
python health_check.py --require-kicad
```

If a workflow specifically requires a board-aware `pcbnew` context, use:

```powershell
python health_check.py --require-pcbnew
```

## KiCad Python Context

Normal Python may not be able to import `pcbnew` directly even when KiCad is installed.

Use:

```powershell
python 03_TOOLS/scripts/kicad_api/kicad_python_context.py
python 03_TOOLS/scripts/kicad_api/pcbnew_import_check.py
```

If direct import fails but KiCad Python is available, board-aware scripts should re-enter through KiCad's bundled `python.exe`.
