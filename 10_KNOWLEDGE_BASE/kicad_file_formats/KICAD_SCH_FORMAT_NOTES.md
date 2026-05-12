# KiCad Schematic Format Notes

Status: `NORMALIZED_REFERENCE`

## High-Value Facts

- `.kicad_sch` is an s-expression schematic format used from KiCad 6 onward
- the root token is `kicad_sch`
- the file includes symbols, labels, wires, junctions, sheet data, and UUIDs
- hierarchical instance paths are UUID-based, not simple sheet-name strings
- library-symbol sections and symbol-instance data are distinct concerns

## Repo Usage

- parsing is acceptable for annotation audits, footprint audits, layout-intent
  extraction, and readability heuristics
- raw text edits are weaker than KiCad-native actions for annotation proof
- saved-file scans do not override live GUI state disputes

## Source Registry References

- `url_000018`
- `url_000020`
