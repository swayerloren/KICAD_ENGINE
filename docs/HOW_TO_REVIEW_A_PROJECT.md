# How To Review A Project

Project review should gather evidence without changing source files unless fixes are explicitly requested and backed up.

## Review Order

1. Read project files and local library tables.
2. Run project validation.
3. Run ERC.
4. Run DRC.
5. Compare schematic symbols to datasheets.
6. Compare footprints to package drawings.
7. Review connectors, polarity, RF, USB, CAN, and power inputs.
8. Review BOM and datasheet coverage.
9. Export review outputs as `NOT_FINAL` if needed.
10. Record findings under `02_HISTORY/` or `05_OUTPUTS/`.

## Validation Command

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\03_TOOLS\scripts\project_validation\validate_kicad_project.ps1 -ProjectPath "C:\path\to\project"
```

or:

```bash
python 03_TOOLS/scripts/project_validation/validate_kicad_project.py "/path/to/project"
```

## Review Language

Use precise status:

- `PASS_BY_SCRIPT`
- `WARN_HUMAN_REVIEW_REQUIRED`
- `FAIL_MISSING_INPUT`
- `NOT_FINAL`
- `UNKNOWN_REQUIRES_SOURCE_VERIFICATION`

Avoid saying a board is ready unless the user has reviewed and accepted the complete verification evidence.
