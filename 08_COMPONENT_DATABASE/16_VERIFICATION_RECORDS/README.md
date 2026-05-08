# Component Verification Records

## PURPOSE

Store component-level verification evidence that supports or blocks use of records in schematics, PCBs, BOMs, and reviews.

## WHAT_BELONGS_HERE

- Symbol verification summaries.
- Footprint verification summaries.
- Package drawing check records.
- Datasheet source review notes.
- Human-review status records.
- Component database audit records.

## WHAT_DOES_NOT_BELONG_HERE

- Active KiCad design files.
- Raw vendor PDF archives without redistribution review.
- Fabrication outputs.
- Unverified claims promoted as approved.
- Secrets or distributor credentials.

## AI_AGENT_RULES

- A verification record must state what was checked, what source was used, and what remains unverified.
- Use `VERIFIED_BY_DATASHEET`, `VERIFIED_FROM_KICAD_LIBRARY`, `USER_CONFIRMED`, or `UNVERIFIED_PLACEHOLDER` consistently.
- Keep high-risk connector, RF, power, and package claims human-review-required until evidence is complete.

## SAFE_EDIT_RULES

- Add timestamped records.
- Preserve old records.
- Do not overwrite contradictory evidence; create a new record and mark conflicts.
- Do not edit KiCad design files from here.

## PUBLIC_RELEASE_NOTES

Public records should avoid private project details and should link to sources instead of bundling restricted documents.

