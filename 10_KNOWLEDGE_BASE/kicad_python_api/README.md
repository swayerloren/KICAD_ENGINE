# KiCad Python API Knowledge

Status: `NORMALIZED_REFERENCE`

This folder captures the repo's stable usage rules for board-aware `pcbnew`
automation. It is intentionally smaller and stricter than the scraped Python
API corpus.

## Canonical Files

- `PCBNEW_API_SAFE_USAGE.md`
- `KICAD_PYTHON_CONTEXT_RULES.md`
- `SAFE_PCBNEW_HELPERS_REFERENCE.md`
- `KICAD_VERSION_COMPATIBILITY_NOTES.md`

## Core Rule

Board-aware scripts must run in a KiCad-compatible Python context. Normal repo
Python is not proof that `pcbnew` is available.

## Source Registry References

- `url_000015` - `https://dev-docs.kicad.org/en/apis-and-binding/pcbnew/index.html`
- `url_000950` - `https://docs.kicad.org/doxygen-python-9.0/`
- `url_000951` - `https://docs.kicad.org/doxygen-python-9.0/classpcbnew_1_1BOARD.html`
- `url_000954` - `https://docs.kicad.org/doxygen-python-9.0/classpcbnew_1_1FOOTPRINT.html`
- `url_000956` - `https://docs.kicad.org/doxygen-python-9.0/classpcbnew_1_1PAD.html`
- `url_000959` - `https://docs.kicad.org/doxygen-python-9.0/classpcbnew_1_1PCB__TRACK.html`
- `url_000960` - `https://docs.kicad.org/doxygen-python-9.0/classpcbnew_1_1PCB__VIA.html`
- `url_000962` - `https://docs.kicad.org/doxygen-python-9.0/classpcbnew_1_1ZONE.html`
- `url_002920` - `https://gitlab.com/kicad/code/kicad`
- `url_002929` - `https://gitlab.com/kicad/code/kicad-python/-/blob/main/README.md`

Raw scrape captures from the legacy KiCad Python API intake are drained
into archive/quarantine paths by the migration ledger.
