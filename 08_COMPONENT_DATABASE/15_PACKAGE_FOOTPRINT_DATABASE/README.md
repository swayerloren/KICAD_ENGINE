# Package Footprint Database

## PURPOSE

Track exact package-to-footprint evidence so AI agents stop assigning KiCad footprints from memory or from generic package names alone.

## WHAT_BELONGS_HERE

- Package verification records.
- Exact package drawing links.
- KiCad footprint comparison notes.
- Pin 1 and orientation evidence.
- Pad geometry, courtyard, silkscreen, fab, and 3D-model review notes.

## WHAT_DOES_NOT_BELONG_HERE

- Unverified package guesses.
- Active KiCad project files.
- Installed KiCad global library edits.
- Connector footprint approvals without exact manufacturer drawings.
- Final fabrication approvals.

## AI_AGENT_RULES

- Use this folder before assigning or approving a footprint.
- Keep generic packages marked `UNVERIFIED` until exact part suffix and drawing are known.
- Connector packages require human orientation review.
- 3D model presence does not prove footprint correctness.

## SAFE_EDIT_RULES

- Add records and source links only.
- Do not modify KiCad libraries from this folder.
- Do not delete old verification records.
- Route generated comparison reports to `16_VERIFICATION_RECORDS/` or `02_HISTORY/`.

## PUBLIC_RELEASE_NOTES

Prefer source links and summary notes. Do not bundle package drawings or vendor PDFs unless redistribution rights are confirmed.

