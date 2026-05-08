# Using KiCad Engine With KiCad

KiCad Engine uses your installed KiCad app. It does not replace it.

## Preferred Integration Order

1. Read KiCad project files directly for discovery.
2. Use repo validation scripts.
3. Use `kicad-cli` for ERC, DRC, and exports.
4. Use `pcbnew` Python for board-aware read-only analysis when needed.
5. Use GUI screenshots only when CLI and file inspection are insufficient.
6. Use GUI automation only with explicit approval and safeguards.

## Installed App Audit

The installed app audit inventories:

- KiCad executables.
- `kicad-cli` version.
- Stock symbol libraries.
- Stock footprint libraries.
- 3D model folders.
- Templates and examples.
- KiCad path assumptions.

Reports should be written under `05_OUTPUTS/` and must not modify installed KiCad folders.

## Project-Local Libraries

Project-local library tables usually sit beside the `.kicad_pro` file:

- `sym-lib-table`
- `fp-lib-table`
- `design-block-lib-table`

Resolve project-local libraries before global or stock libraries. Do not edit them without project approval and backup.

## Global Libraries

Agents may read user-global KiCad library tables when needed to resolve references. They must not edit global tables unless the user explicitly requests that and a backup plan exists.
