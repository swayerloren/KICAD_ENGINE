# Integration With 29_FOOTPRINT_GAP_ANALYSIS

Playwright research may collect candidate package and source-link evidence that helps decide which footprint gaps need package-drawing review.

## Allowed Outputs

- Candidate package names from public sources.
- Candidate package drawing source links.
- Screenshot evidence for public library/source pages.
- Notes that a KiCad footprint candidate remains `UNVERIFIED`.

## Rules

- Do not treat supplier package text as footprint verification.
- Do not edit KiCad global libraries.
- Do not write `.kicad_mod` or `.pretty` files.
- Route exact verification evidence to `08_COMPONENT_DATABASE/16_VERIFICATION_RECORDS/` only after a separate verification task.

