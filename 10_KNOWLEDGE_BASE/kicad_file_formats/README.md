# KiCad File Format Knowledge

Status: `NORMALIZED_REFERENCE`

This folder summarizes the KiCad s-expression file-format concepts most useful
for repo-side audit and extraction tooling.

## Canonical Files

- `KICAD_SCH_FORMAT_NOTES.md`
- `KICAD_PCB_FORMAT_NOTES.md`
- `NETLIST_RATSNEST_AND_CONNECTIVITY_NOTES.md`

## Core Rule

File parsing is allowed for audit, indexing, and extraction. Native KiCad
validation remains stronger evidence than third-party parsing alone.

## Source Registry References

- `url_000018` - `https://dev-docs.kicad.org/en/file-formats/sexpr-intro/index.html`
- `url_000019` - `https://dev-docs.kicad.org/en/file-formats/sexpr-pcb/index.html`
- `url_000020` - `https://dev-docs.kicad.org/en/file-formats/sexpr-schematic/index.html`
- `url_000718` - `https://docs.kicad.org/9.0/en/cli/cli.html`
