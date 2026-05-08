# Placement Assistance Plan

## Goal

Create a KiCad-native workflow where AI suggests placement groups and review priorities without pretending to solve final placement automatically.

## What KiCad Can Do Natively

KiCad PCB Editor supports manual placement tools, including:

- Move and drag footprints.
- Set exact footprint position, rotation, and side.
- Align and distribute selected objects.
- Group objects.
- Lock objects.
- Rule areas and keepouts.
- Multichannel layout for repeated circuits, where a manually placed/routed reference channel can be repeated into target areas.

These features are useful for human-guided placement. They are not the same as a general-purpose AI auto-placement engine.

## What `kicad-cli` Can Do

Based on local KiCad 9.0.7 help, `kicad-cli pcb` supports DRC, exports, and 3D rendering. It does not expose a complete headless footprint auto-placement command.

Useful placement-adjacent uses:

- Run DRC before and after placement changes.
- Export position files for review.
- Export SVG/PDF/renders for visual review.
- Generate reports that an AI can summarize.

## What `pcbnew` Python Can Inspect Or Change

The PCB Python API can inspect board objects such as footprints, tracks, zones, drawings, and netclasses. It can also load and save boards.

Potential uses:

- Read footprint references, positions, rotations, sides, and locks.
- Read pad/net connectivity for grouping.
- Identify unplaced or out-of-board footprints.
- Generate placement reports.
- In a copied project only, move footprints to proposed positions.

Risk:

- `pcbnew` Python is coupled to KiCad internals and changes across versions.
- Any write requires active project, backup, copied workspace preference, rollback plan, and DRC verification.

## What IPC API May Enable

KiCad's IPC API is intended for controlling a running KiCad instance and building plugins or external integrations. In KiCad 9/10, it is GUI-session based, not a standalone headless file-manipulation library.

Potential future use:

- Interactive placement helper plugin.
- Visual selection/grouping assistant.
- Human-in-the-loop placement review UI.
- Safer alternative to ad hoc GUI automation.

Current limitation:

- Treat IPC placement automation as experimental until implemented and tested in this repo.

## AI Placement Proposal Inputs

- Board outline.
- Mechanical constraints.
- Connector locations and cable directions.
- Mounting holes.
- Component list and footprints.
- Netlist connectivity.
- Power tree.
- High-risk nets: RF, USB, CAN, clock, crystal, differential pairs, high-current, switching nodes.
- Datasheet layout notes.
- Reference design lessons.

## AI Placement Proposal Outputs

Generate Markdown first:

- Fixed items.
- Placement groups.
- Keepout zones.
- Suggested relative positions.
- High-risk net route priorities.
- Items requiring human review.
- DRC baseline and post-change comparison plan.

Do not write placement changes directly unless the user requests it and KiCad edit gates are satisfied.

## Suggested Placement Groups

- Connectors and mechanical parts.
- Power input and protection.
- Switching regulators and inductors.
- MCU/module and decoupling.
- Programming/debug connector.
- USB interface.
- CAN/LIN/RS485 interface.
- RF module/antenna.
- Sensors/analog front end.
- Status LEDs/buttons/test points.

## Human Review Required

Human layout review remains required for:

- Connector orientation.
- RF placement and keepout.
- USB connector and ESD placement.
- CAN/LIN/RS485 connector pinout and protection.
- High-current and thermal paths.
- Crystal/clock placement.
- Mechanical fit and enclosure clearance.

