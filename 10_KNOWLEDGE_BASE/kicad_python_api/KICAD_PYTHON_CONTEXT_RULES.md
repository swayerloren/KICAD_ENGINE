# KiCad Python Context Rules

Status: `NORMALIZED_REFERENCE`

## Hard Rules

1. Board-aware scripts must use a KiCad-compatible Python context.
2. Normal Python is not allowed as proof that `pcbnew` is available.
3. A failing direct import in repo Python is not automatically a blocker if
   KiCad's embedded Python can run the workflow.
4. A passing direct import in one environment does not remove the need for
   version/runtime checks on another machine.

## Repo Tools

- `03_TOOLS/scripts/kicad_api/kicad_python_context.py`
- `03_TOOLS/scripts/kicad_api/pcbnew_import_check.py`
- `03_TOOLS/scripts/kicad_api/safe_pcbnew_helpers.py`

## Evidence Hierarchy

- KiCad's embedded/runtime-compatible Python context
- saved-file CLI validation
- helper-layer extraction results
- plain repo Python assumptions

## Source Registry References

- `url_000950`
- `url_000963` - `https://docs.kicad.org/kicad-python/main/kicad.html`
- `url_002920`
- `url_002929`
- `url_002931` - `https://gitlab.com/kicad/code/kicad-python/-/tree/main`
