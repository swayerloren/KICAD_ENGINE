# PCB Quality Gate Creation Audit

Date: `2026-05-10`
Scope: create an enforceable real-board PCB quality gate that judges routing
acceptability from executable checks rather than Codex prose summaries.

## What Was Added

- `03_TOOLS/scripts/pcb_quality/` with dedicated checks for:
  - KiCad DRC and schematic parity
  - open nets
  - trace geometry
  - testpoint topology
  - power widths
  - USB pair sanity
  - zone/GND status
  - connector orientation
- project routing-constraint template and active-project config
- CI workflow `.github/workflows/pcb-quality-gate.yml`
- startup/workflow documentation hooks so later sessions route to the gate

## Key Correction

The first implementation used plain `kicad-cli pcb drc`, which did not expose
the authoritative schematic-parity count needed for this repo's gate. The
helper was corrected to use:

```powershell
kicad-cli pcb drc --schematic-parity --severity-all --format report
```

That corrected the live judge result for `ESP32_CSI_WIFI_NODE` from a weaker
top-level `FAIL_OPEN_NETS` classification to the authoritative `FAIL_DRC`
classification with `22` schematic parity issues.

## Validation Result

- Python syntax: `PASS`
- Dry-run gate execution: `PASS` in read-only mode
- Live board classification: `FAIL_DRC`
- No KiCad design-file edits: confirmed

## Active Board Status

The authoritative failing packet is:

- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/pcb_quality_gate/20260510_quality_gate_creation_v2/`

Key live blocker counts from that run:

- `22` schematic parity issues
- `13` unconnected items
- `3` detectable unrouted nets
- `36` non-testpoint geometry findings
- USB routing failed
- testpoint topology failed
- power-width checks failed
- connector proof still requires human review

Conclusion: the gate layer is working as intended because it blocks the current
board without relying on agent summary language.
