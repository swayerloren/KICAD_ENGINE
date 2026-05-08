# Using With KiCad

Status: `PUBLIC_DRAFT`

## Principle

KiCad Engine uses your installed KiCad app. It does not replace KiCad or modify installed KiCad folders.

## Preferred Interfaces

- `kicad-cli` for ERC, DRC, and exports where available.
- Direct file parsing for read-only inspection.
- `pcbnew` Python only when appropriate and version-compatible.
- GUI screenshots only when CLI/API inspection is insufficient.

## Do Not Modify

- Installed KiCad symbol libraries.
- Installed KiCad footprint libraries.
- Installed KiCad 3D model folders.
- User-global KiCad library tables.

## Project-Local Libraries

Generated or custom symbols and footprints should be project-local and backed up before edits.

