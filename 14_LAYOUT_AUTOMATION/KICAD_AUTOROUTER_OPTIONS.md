# KiCad Autorouter Options

## Reality Summary

KiCad provides strong manual and interactive routing tools. Based on current public documentation and local KiCad 9.0.7 CLI help, KiCad Engine should not claim that KiCad has a built-in complete headless autorouter available through `kicad-cli`.

## Native KiCad Routing Support

KiCad PCB Editor supports:

- Interactive routing.
- Push-and-shove behavior.
- Walk-around behavior.
- Collision highlighting.
- Differential pair routing.
- Length tuning.
- Skew tuning.
- DRC-aware routing.
- Net classes and custom rules.
- Rule areas and keepouts.
- Repeated layout for multichannel designs.

Best use for KiCad Engine:

- AI produces routing plans and risk flags.
- Human routes in KiCad.
- KiCad DRC verifies.
- AI interprets DRC and compares before/after results.

## `kicad-cli`

Local KiCad 9.0.7 `kicad-cli pcb` supports:

- `drc`
- `export`
- `render`

`kicad-cli pcb export` supports many manufacturing/review formats, but local help did not show DSN export or an autorouting command.

Best use:

- DRC automation.
- Export review artifacts.
- Render board state.
- Produce reports for AI interpretation.

## `pcbnew` Python

Can inspect and modify PCB data through KiCad's PCB API.

Best near-term use:

- Read-only board analysis.
- Placement reports.
- Constraint reports.
- Risk classification.

Potential future use:

- Project-copy placement experiments.
- Simple scripted placement for known templates.
- Generated rule areas or groups.

Risk:

- Not a stable long-term API.
- Writes can damage board files if poorly implemented.

## IPC API

The KiCad IPC API is promising for GUI-connected plugins and external tools. In KiCad 9/10, public docs describe it as communicating with a running KiCad GUI, with wider headless/export support coming in later versions.

Best future use:

- Human-in-the-loop placement and routing assistant.
- Safer plugin-based integration than coordinate GUI automation.
- Interactive review panels.

## External Autorouter

FreeRouting is the main realistic open-source external autorouter candidate. Integration requires DSN/SES flow and careful review.

## Claim Boundary

KiCad Engine may claim:

- Placement and routing assistance planning.
- DRC-backed review workflows.
- Potential FreeRouting integration plan.

It must not claim:

- Built-in complete AI autorouting.
- Production-safe external routing integration.
- Fabrication-ready layout without human review.

