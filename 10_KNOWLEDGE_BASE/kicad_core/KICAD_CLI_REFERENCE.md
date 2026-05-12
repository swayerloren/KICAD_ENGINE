# KiCad CLI Reference

Status: `NORMALIZED_REFERENCE`

## Purpose

Summarize the repo-approved use of `kicad-cli` for repeatable checks and export
steps.

## Core Commands

- `kicad-cli sch erc <file.kicad_sch>`
  - schematic electrical checks on the saved file
- `kicad-cli pcb drc <file.kicad_pcb>`
  - board DRC on the saved file
- `kicad-cli pcb drc --schematic-parity --severity-all --format report <file.kicad_pcb>`
  - authoritative parity-aware DRC for repo gating
- `kicad-cli sch export netlist`
  - schematic connectivity extraction
- `kicad-cli sch export svg|pdf`
  - saved-schematic rendering
- `kicad-cli pcb render`
  - saved-board review images
- `kicad-cli fp export ...` and `kicad-cli sym export ...`
  - library inspection/export workflows

## What CLI Is Good Evidence For

- saved-file ERC/DRC evidence
- parity-aware PCB checks
- read-only visual exports
- netlist/export generation
- repeatable CI-friendly validation

## What CLI Is Not Good Proof For

- whether the open KiCad GUI has unsaved changes
- whether schematic annotation was applied in the live GUI
- GUI-visible ERC marker state when the window is dirty
- interactive human readability judgments by themselves

## Repo Rule

Use CLI by default, but do not overclaim. If the task depends on live GUI
state, native KiCad GUI evidence is stronger than CLI evidence.

## Source Registry References

- `url_000718` - `https://docs.kicad.org/9.0/en/cli/cli.html`
- `url_000727` - `https://docs.kicad.org/9.0/en/kicad/kicad.html`
