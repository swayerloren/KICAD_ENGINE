# KiCad PCB Format Notes

Status: `NORMALIZED_REFERENCE`

## High-Value Facts

- `.kicad_pcb` is an s-expression board format
- the root token is `kicad_pcb`
- major sections include layers, setup, nets, footprints, tracks, zones, and
  graphic items
- section order is not the main truth; token semantics are
- the `generator` field should not impersonate KiCad itself in third-party
  tools

## Repo Usage

- parsing is acceptable for board-digital-twin extraction and audits
- board-aware scripts should not infer routing quality or parity solely from
  token presence
- KiCad DRC and parity evidence remain stronger than parser-only conclusions

## Source Registry References

- `url_000018`
- `url_000019`
