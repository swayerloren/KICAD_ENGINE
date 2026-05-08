# Library QA Workflow

Status: `AI_GUIDANCE_ONLY`

## Workflow

1. Identify the exact component, package, and intended KiCad project context.
2. Confirm whether the library item is stock KiCad, user global, or project-local.
3. Read the source documents: datasheet pinout, package drawing, land pattern, connector drawing, and mechanical drawing where applicable.
4. Validate symbol structure with `scripts/validate_symbol_file.py` when a symbol file is available.
5. Validate footprint structure with `scripts/validate_footprint_file.py` when a footprint file is available.
6. Compare footprint metadata with `scripts/compare_footprint_to_metadata.py` when a metadata JSON record exists.
7. Record findings under `02_HISTORY` or project history, not inside installed KiCad folders.
8. Record durable verified mappings under `08_COMPONENT_DATABASE/12_KICAD_SYMBOL_FOOTPRINT_MATCHES/`, `15_PACKAGE_FOOTPRINT_DATABASE/`, or `16_VERIFICATION_RECORDS/`.
9. Keep unresolved risks open until a human reviews them.

## Required Status Separation

Track these independently:

- Symbol pinout status.
- Footprint package-drawing status.
- Symbol-to-footprint mapping status.
- 3D model path/orientation status.
- Connector orientation status.
- Human review status.

## Blocking Conditions

Mark `BLOCKED_UNTIL_HUMAN_REVIEW` if any of these are true:

- Exact package drawing is missing.
- Connector drawing or orientation is missing.
- Footprint pad numbering is not compared to the source.
- Symbol pinout is inferred from a different package.
- 3D model conflicts with footprint or board-side orientation.
- KiCad design files would need edits but active project and backup are not confirmed.

## Script Safety

The scripts in `11_LIBRARY_FACTORY/scripts/` must remain read-only for input libraries. They may write reports only when the user passes explicit output paths.

