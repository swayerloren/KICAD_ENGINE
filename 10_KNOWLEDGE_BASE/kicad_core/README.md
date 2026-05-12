# KiCad Core Knowledge

Status: `NORMALIZED_REFERENCE`

This folder holds concise KiCad core workflow notes distilled from official
KiCad documentation and existing repo validation rules. It is for agent routing
and review planning, not as a replacement for KiCad's own manuals.

## Canonical Files

- `KICAD_CLI_REFERENCE.md`
- `KICAD_ERC_DRC_REFERENCE.md`
- `KICAD_GUI_VS_CLI_ACTIONS.md`

## Use Pattern

1. Use CLI/API/MCP first when they provide repeatable evidence.
2. Use native KiCad GUI workflows for annotation, disputed GUI state, and other
   actions the CLI does not prove reliably.
3. Treat these docs as summaries. For exact syntax or version details, check
   the referenced source-registry entries and the active KiCad install.

## Source Registry References

- `url_000718` - `https://docs.kicad.org/9.0/en/cli/cli.html`
- `url_000720` - `https://docs.kicad.org/9.0/en/eeschema/eeschema.html`
- `url_000723` - `https://docs.kicad.org/9.0/en/getting_started_in_kicad/getting_started_in_kicad.html`
- `url_000727` - `https://docs.kicad.org/9.0/en/kicad/kicad.html`
- `url_000731` - `https://docs.kicad.org/9.0/en/pcbnew/pcbnew.html`

Raw scrape captures from the legacy KiCad core intake are not canonical.
They are drained into archive/quarantine paths by the migration ledger.
