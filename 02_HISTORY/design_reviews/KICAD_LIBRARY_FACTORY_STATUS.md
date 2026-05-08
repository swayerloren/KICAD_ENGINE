# KiCad Library Factory Status

Date: 2026-05-03

## Purpose

Created `11_LIBRARY_FACTORY/` so Codex, Claude, and similar agents have detailed source-backed standards for creating or verifying KiCad symbols, footprints, package mappings, and project-local libraries.

## Created

- `11_LIBRARY_FACTORY/README.md`
- `11_LIBRARY_FACTORY/symbols/`
- `11_LIBRARY_FACTORY/footprints/`
- `11_LIBRARY_FACTORY/mapping/`
- `11_LIBRARY_FACTORY/scripts/`

## Standards Coverage

- Symbol creation must be driven by exact datasheet or reference-manual pinout evidence.
- Power pins, hidden pins, no-connects, exposed pads, and multi-unit symbols require explicit review.
- Symbol fields must preserve datasheet/source and verification status.
- Footprint creation must be driven by exact package drawing, land pattern, or connector drawing evidence.
- Pad size, drill size, courtyard, fab layer, silkscreen, origin, pin 1, 3D model status, and connector orientation require review.
- Symbol-to-footprint mapping must verify symbol pin numbers against footprint pad numbers.
- Project-local libraries are preferred for generated/custom symbols and footprints.
- Installed KiCad global libraries and user-global library tables must not be modified.

## Scripts

Created basic read-only validators:

- `11_LIBRARY_FACTORY/scripts/validate_symbol_file.py`
- `11_LIBRARY_FACTORY/scripts/validate_footprint_file.py`
- `11_LIBRARY_FACTORY/scripts/compare_footprint_to_metadata.py`

The scripts perform basic structural checks and optional report writing. They do not replace human review, datasheet pinout checks, package drawing checks, connector orientation review, ERC, or DRC.

## Workflow Updates

Updated:

- `09_ACCURACY_ENGINE/workflows/DATASHEET_TO_SYMBOL_WORKFLOW.md`
- `09_ACCURACY_ENGINE/workflows/DATASHEET_TO_FOOTPRINT_WORKFLOW.md`

The workflows now require relevant `11_LIBRARY_FACTORY/` standards, project-local library preference, source evidence, QA checks, and explicit unverified status until review is complete.

## Integration Updates

- Updated `AGENTS.md`.
- Updated `START_HERE_FOR_AI_AGENTS.md`.
- Updated `README.md`.
- Updated `README_GPT.md`.
- Updated `FOR CHAT GPT.MD`.
- Updated `00_CODEX_START/REPO_MAP.md`.
- Updated `health_check.py`.
- Updated installer payload rules and builder allowlist.

## Safety Notes

- No KiCad project source files were edited.
- No installed KiCad libraries were modified.
- No user-global KiCad library tables were modified.
- No tools were installed.
- No exact datasheet values were fabricated.

