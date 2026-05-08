# Datasheet Package To Footprint Standard

## Purpose

Translate datasheet package evidence into a KiCad footprint choice without guessing.

## Required Evidence

- Package name and code.
- Body dimensions.
- Pin count.
- Pitch.
- Pad or lead dimensions.
- Exposed pad details.
- Recommended land pattern if available.
- Pin 1 orientation.
- Height if mechanical clearance matters.

## Rules

- Package suffix matters.
- Module variants matter.
- Connector variants matter.
- Land pattern recommendations override generic package assumptions when source-backed.
- KiCad stock footprints are candidates until checked against the exact drawing.

## Metadata To Record

- Source document.
- Package code.
- Drawing page or section.
- Footprint library and name.
- Verification status.
- Known deviations from manufacturer land pattern.

## Review Gate

If the datasheet package cannot be mapped cleanly to a footprint, create a project-local candidate and mark it `UNVERIFIED_FOOTPRINT` until reviewed.

