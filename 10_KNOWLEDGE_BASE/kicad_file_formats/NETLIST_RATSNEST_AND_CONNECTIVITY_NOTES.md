# Netlist Ratsnest And Connectivity Notes

Status: `NORMALIZED_REFERENCE`

## Distinctions

- schematic netlist:
  - logical connectivity exported from the saved schematic
- PCB nets:
  - board-side net objects and assignments in the `.kicad_pcb`
- ratsnest/unrouted state:
  - expected connections not yet satisfied by copper
- DRC connectivity findings:
  - KiCad's own judgment on saved board state and parity

## Repo Rule

Do not treat file parsing alone as proof that all nets are routed. Use native
KiCad DRC, unrouted/open-net audits, and parity-aware checks.

## Practical Implications

- a board can have zero geometry-rule violations and still have unrouted nets
- prelayout projection is planning evidence, not routing completion evidence
- copied-board rehearsal results do not override live-board parity or DRC

## Source Registry References

- `url_000018`
- `url_000019`
- `url_000020`
- `url_000718`
