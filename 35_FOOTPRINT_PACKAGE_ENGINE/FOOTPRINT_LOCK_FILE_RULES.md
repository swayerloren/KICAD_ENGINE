# Footprint Lock File Rules

## Purpose

`FOOTPRINT_LOCK.csv` is the project-local lock file that proves footprint
assignment decisions.

## Required Path

Place the lock file in the active project root:

`<ACTIVE_PROJECT_PATH>/FOOTPRINT_LOCK.csv`

## Required Columns

- `reference`
- `value`
- `manufacturer_part_number`
- `package`
- `kicad_symbol`
- `kicad_footprint`
- `datasheet_or_source_url`
- `package_drawing_checked`
- `pin_mapping_checked`
- `3d_model_available`
- `risk`
- `human_review_required`
- `notes`

## Rules

- One row per physical symbol.
- Reference values must be unique.
- Lock rows must match the schematic reference and value.
- `kicad_footprint` must match the current schematic footprint field after the
  footprint is assigned.
- `risk` must be `LOW`, `MEDIUM`, or `HIGH`.
- For connectors and mechanical parts, missing 3D-model proof requires
  `human_review_required = yes`.
- Do not treat the lock file as passed if required columns exist but the proof
  fields are blank.

## Review Notes

Use `notes` to record:

- connector orientation proof
- local datasheet path when no URL is available
- special pin-mapping facts
- explicit human-review reason
