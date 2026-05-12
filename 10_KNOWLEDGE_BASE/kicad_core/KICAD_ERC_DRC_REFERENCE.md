# KiCad ERC DRC Reference

Status: `NORMALIZED_REFERENCE`

## ERC

Use ERC after meaningful schematic edits and before schematic-to-PCB claims.

Strongest evidence order:

1. native KiCad GUI ERC when live GUI state matters
2. `kicad-cli sch erc` on the saved schematic
3. project-linked report artifacts that are current and hash-matched

ERC alone does not prove schematic readability, annotation correctness, or
footprint-package readiness.

## DRC

Use DRC after meaningful PCB edits and before routing/fab claims.

Strongest evidence order:

1. native KiCad DRC or `kicad-cli pcb drc` on the saved PCB
2. parity-aware DRC with `--schematic-parity`
3. linked current reports tied to the live board hash

Zero geometry-rule violations do not prove there are no unrouted nets, no
quality problems, or no connector/mechanical mistakes.

## Required Repo Interpretation

- saved-file parsing is weaker than native KiCad validation
- `kicad-cli pcb drc --schematic-parity --severity-all --format report` is the
  preferred parity gate
- trace geometry, connector orientation, and prelayout feasibility remain
  separate gates
- annotation disputes must use native KiCad GUI workflow

## Source Registry References

- `url_000718` - `https://docs.kicad.org/9.0/en/cli/cli.html`
- `url_000720` - `https://docs.kicad.org/9.0/en/eeschema/eeschema.html`
- `url_000731` - `https://docs.kicad.org/9.0/en/pcbnew/pcbnew.html`
