# Pre-Schematic Checklist

Status: `REQUIRED_BEFORE_SCHEMATIC_EDITS`

Use this checklist before creating or editing KiCad schematic files. Store completed project-specific results in the project `reports/` or `history/verification_runs/` folder.

## Required Before KiCad Edits

| Check | Required Result |
| --- | --- |
| Active project | Confirmed and inside `04_KICAD_PROJECTS/active/` or explicitly provided by the user. |
| Backup | Backup path created or confirmed under `99_BACKUPS/pre_codex_edits/`. |
| Rollback plan | Written before edits. |
| Verification plan | ERC, annotation, completeness, visual, and source checks listed. |
| Rules read | Relevant `09_ACCURACY_ENGINE/schematic_rules/` files read. |
| Prior context | Project memory/history and open risks reviewed. |

## Design Inputs

| Area | Required Question |
| --- | --- |
| Requirements | What must the board do, and what is out of scope? |
| Power | What input source, voltage rails, current budget, protection, and regulator topology are required? |
| Controller | Is the MCU/module/dev board exact, generic, or still undecided? |
| Interfaces | Which USB, CAN, LIN, RS485, RF, UART, I2C, SPI, sensor, or connector interfaces are required? |
| Mechanical | Which connectors, mounting holes, board-edge parts, enclosure constraints, or antenna keepouts matter? |
| Manufacturing | Is this planning-only, prototype, assembly-ready, or `NOT_FINAL` review work? |

## Evidence Inputs

| Evidence | Required Status |
| --- | --- |
| Component records | Present or planned for every non-trivial part. |
| Datasheet/source links | `SOURCE_LINK_ONLY` minimum for exact parts; `TODO_SOURCE_REQUIRED` must be logged. |
| Symbol candidates | Candidate list only until pinout is verified. |
| Footprint candidates | Candidate list only until exact package drawing is reviewed. |
| BOM lock | Required before schematic-to-PCB gate. |
| Unknown values | Explicitly marked `Unknown - requires source verification`. |

## Stop Conditions

Stop and record a blocker if the requested schematic depends on:

- unknown connector orientation or pin numbering,
- unknown PMOS/source-gate-drain mapping,
- unknown ESD array pin mapping,
- unknown regulator package/capacitor/layout requirements,
- unknown power current or voltage limits,
- unknown MCU boot/debug/power pins,
- undocumented external interface,
- any user requirement that conflicts with a source or project memory.

The correct output for a blocked schematic is a plan, source-gap list, or `NEEDS_HUMAN_REVIEW` record, not an invented circuit.
