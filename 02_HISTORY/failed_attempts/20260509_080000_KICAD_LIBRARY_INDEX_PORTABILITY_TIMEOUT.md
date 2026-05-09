# Failed Attempt - KiCad Library Index Portability Cleanup Timeout

Date: `2026-05-09`

## Attempt

Ran:

```powershell
python 03_TOOLS/scripts/kicad_libraries/index_footprints.py --output-dir T_E_M_P/kicad_library_regen_smoke
```

with a `120000` ms timeout.

## Result

- Command timed out before completion.
- No repo source files were harmed.
- The task remained read-only.

## Resolution

- Reran the same command with a `300000` ms timeout.
- The rerun succeeded and wrote the expected temp output files.
