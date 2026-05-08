# PCB Update From Schematic Checklist

## Purpose

Use this checklist only after `reports/SCHEMATIC_TO_PCB_GATE_STATUS.md` is marked `PASS`. This checklist does not replace the schematic-to-PCB gate. It controls the first PCB update/layout step after the gate passes.

## Absolute Preconditions

- Active project confirmed.
- Target files are inside the active project path.
- Backup exists in `99_BACKUPS/pre_codex_edits/` or the approved project backup location.
- `reports/SCHEMATIC_TO_PCB_GATE_STATUS.md` exists.
- Gate result is exactly `PASS`.
- Gate evidence is current for the schematic revision being used.
- Project memory and history were reviewed.
- Rollback plan is documented.

If any precondition is missing, stop. Do not update PCB.

## Allowed Actions After PASS

After backup and explicit task scope confirmation, an agent may:

- Update PCB from schematic.
- Import netlist-equivalent changes.
- Place footprints for review.
- Create early layout planning artifacts.
- Run DRC after PCB changes.
- Produce review-only visual outputs.

## Still Not Final

Even after the schematic-to-PCB gate passes, the following remain `NOT_FINAL`:

- Placement.
- Routing.
- Copper zones.
- Gerbers.
- Drill files.
- Pick-and-place files.
- STEP files.
- Assembly drawings.
- Fab packages.

Manufacturing output remains `NOT_FINAL` until the full release-package workflow passes.

## PCB Update Checklist

| # | Check | Status | Evidence path | Notes |
|---|---|---|---|---|
| 1 | Schematic-to-PCB gate file exists. | NOT_RUN |  |  |
| 2 | Gate result is `PASS`. | NOT_RUN |  |  |
| 3 | Backup created or confirmed. | NOT_RUN |  |  |
| 4 | Schematic revision recorded. | NOT_RUN |  |  |
| 5 | PCB file path identified or creation explicitly approved. | NOT_RUN |  |  |
| 6 | Footprint library paths resolved. | NOT_RUN |  |  |
| 7 | Project-local library tables checked. | NOT_RUN |  |  |
| 8 | High-risk footprints reviewed before placement. | NOT_RUN |  |  |
| 9 | Connector orientation review notes available. | NOT_RUN |  |  |
| 10 | Post-update DRC plan prepared. | NOT_RUN |  |  |
| 11 | Post-update visual review plan prepared. | NOT_RUN |  |  |
| 12 | Rollback plan recorded. | NOT_RUN |  |  |

## Required After PCB Update

- Save command log.
- Run DRC or explain why DRC could not be run.
- Record before/after files changed.
- Record new unresolved issues.
- Keep all generated layout and fab-style outputs marked `NOT_FINAL`.

## Blocked Actions

Do not proceed if:

- The gate is not `PASS`.
- The schematic changed after the gate was marked `PASS`.
- ERC was rerun and failed.
- A footprint changed without package drawing verification.
- A connector orientation issue was found.
- A high-risk `NEEDS_REVIEW` item exists.
