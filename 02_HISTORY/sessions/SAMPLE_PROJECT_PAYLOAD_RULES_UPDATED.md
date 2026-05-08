# Session Log - Sample Project Payload Rules Updated

Date: `2026-05-06`

## Task

Update public release payload rules so only safe, licensed, useful sample
project files are included, while raw imports, personal history, backups,
unsafe outputs, unclear-license files, secrets, PDFs without redistribution
review, and fabrication-style outputs are excluded.

## Work Completed

- Created `17_RELEASE_BUILD/PAYLOAD_ALLOWLIST.md`.
- Created `17_RELEASE_BUILD/PAYLOAD_EXCLUDE_RULES.md`.
- Created `17_RELEASE_BUILD/PUBLIC_PAYLOAD_MANIFEST.md`.
- Created `17_RELEASE_BUILD/SAMPLE_PROJECT_PAYLOAD_POLICY.md`.
- Updated `17_RELEASE_BUILD/PUBLIC_RELEASE_EXCLUSION_MANIFEST.md`.
- Updated `17_RELEASE_BUILD/README.md` and `17_RELEASE_BUILD/INDEX.md`.
- Updated `FOR CHAT GPT.MD` with release payload sample policy status.
- Created `05_OUTPUTS/release_readiness/SAMPLE_PAYLOAD_AUDIT.md`.

## Key Decision

The controlled `tomasr8_attiny85_dev_board` fixture is currently
`LINK_ONLY_PLUS_DOCS` for public payload purposes. Its source KiCad files,
custom footprints, generated visuals, gate-run folders, and fabrication-style
outputs remain excluded until final human license/release review records public
bundle status exactly `PUBLIC_BUNDLE_ALLOWED`.

## KiCad Design File Safety

No `.kicad_pro`, `.kicad_sch`, `.kicad_pcb`, or `.kicad_mod` files were edited.

## Validation

- Required release policy files exist.
- Targeted secret assignment scan on changed release docs found no matches.
- `17_RELEASE_BUILD/build_public_payload.py` is missing, so no dry-run public
  payload build was run.
- Existing installer payload builder is not a public sample payload builder and
  does not expose a dry-run flag.

## Remaining Work

- Build a real `17_RELEASE_BUILD/build_public_payload.py` with dry-run default.
- Complete human release review for the ATtiny85 fixture.
- Keep the license audit status visible as `REQUIRES_HUMAN_REVIEW`.
