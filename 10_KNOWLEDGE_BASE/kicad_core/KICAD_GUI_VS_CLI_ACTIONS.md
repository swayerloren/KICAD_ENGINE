# KiCad GUI Vs CLI Actions

Status: `NORMALIZED_REFERENCE`

## Default Rule

Prefer CLI/API/MCP for repeatable saved-file work. Use native KiCad GUI for
actions where CLI cannot prove the required state.

| Action | Preferred Plane | Why |
| --- | --- | --- |
| Saved-file ERC | CLI | repeatable and scriptable |
| Saved-file DRC | CLI | repeatable and scriptable |
| Parity-aware DRC | CLI | explicit gate evidence |
| Schematic annotation | GUI | CLI does not authoritatively prove live annotation state |
| Save dirty schematic state | GUI | only KiCad can save the active GUI state |
| GUI-visible ERC markers | GUI | saved-file CLI may lag dirty GUI state |
| PNG/PDF/SVG from saved design | CLI | repeatable export |
| Screenshot of current open KiCad view | GUI/screenshot | reflects actual visible state |
| Board-aware `pcbnew` object inspection | KiCad Python context | binding/runtime sensitive |

## Hard Stops

- do not treat raw `.kicad_sch` text edits as annotation proof
- do not use normal Python import success/failure alone as proof that `pcbnew`
  is available for board-aware workflows
- do not treat saved-file parsing as stronger evidence than native KiCad
  validation when they disagree

## Source Registry References

- `url_000718` - `https://docs.kicad.org/9.0/en/cli/cli.html`
- `url_000720` - `https://docs.kicad.org/9.0/en/eeschema/eeschema.html`
- `url_000731` - `https://docs.kicad.org/9.0/en/pcbnew/pcbnew.html`
