# Library Factory Scripts

These scripts perform basic read-only checks on KiCad symbol and footprint files.

They do not approve symbols or footprints. They only produce evidence and warnings for human review.

They must not modify input KiCad files, installed KiCad global libraries, user-global library tables, or active project libraries. Report files are written only when an explicit report output path is provided.

## Scripts

- `validate_symbol_file.py`: checks a `.kicad_sym` file for basic KiCad symbol-library structure, fields, pins, duplicate pin numbers, and source/verification fields.
- `validate_footprint_file.py`: checks a `.kicad_mod` file for basic footprint structure, pads, courtyard, fab layer, silkscreen, pin 1 pad, and 3D model status.
- `compare_footprint_to_metadata.py`: compares a `.kicad_mod` file to a JSON metadata file with expected package details.

## Safety

- Read-only for KiCad libraries and design files.
- Does not modify global KiCad libraries.
- Does not modify user-global library tables.
- Reports are optional and written only to paths passed by the user.
- If no report path is passed, the scripts print a small JSON summary to stdout only.

## Example

```powershell
python 11_LIBRARY_FACTORY/scripts/validate_symbol_file.py --symbol path/to/library.kicad_sym --markdown-report 05_OUTPUTS/symbol_report.md --json-report 05_OUTPUTS/symbol_report.json
python 11_LIBRARY_FACTORY/scripts/validate_footprint_file.py --footprint path/to/footprint.kicad_mod --markdown-report 05_OUTPUTS/footprint_report.md --json-report 05_OUTPUTS/footprint_report.json
python 11_LIBRARY_FACTORY/scripts/compare_footprint_to_metadata.py --footprint path/to/footprint.kicad_mod --metadata package_metadata.json
```

## Metadata Example

```json
{
  "part_number": "EXAMPLE",
  "package": "QFN-32",
  "expected_pad_count": 33,
  "expected_pad_numbers": ["1", "2", "3", "EP"],
  "requires_courtyard": true,
  "requires_fab": true,
  "requires_silkscreen": true,
  "requires_3d_model": false,
  "pin1_required": true,
  "source_document": "Vendor package drawing",
  "verification_status": "UNVERIFIED_PLACEHOLDER"
}
```
