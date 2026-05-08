# Uncertainty Log: ESP32 CSI Actual KiCad Annotation Repair

Date: `2026-05-06`

## Uncertainty

Local saved-file validation and `kicad-cli` ERC pass, but the live KiCad GUI was not controlled. If the schematic was already open in KiCad during file edits, the GUI may still show stale pre-repair annotation state until LJ reloads or reopens it.

Status: `REQUIRES_HUMAN_REVIEW`

Severity: `MEDIUM`

Confidence: `HIGH` for saved-file/CLI evidence; `UNVERIFIED` for live GUI display state.

## Required Human Action

LJ should close and reopen or reload the schematic in KiCad, then run/check ERC in the GUI if needed before any visual cleanup resumes.

## Non-Uncertainties

The following are verified by current saved-file evidence:

- no requested unresolved reference patterns were found in the schematic file
- duplicate physical, `#PWR`, and `#FLG` checks pass
- local `kicad-cli sch erc` reports 0 violations

## Still Blocked

PCB update remains blocked by non-annotation gates: visual readability, footprint/package verification, connector orientation, PMOS pin mapping, USB policy, and LJ review.
