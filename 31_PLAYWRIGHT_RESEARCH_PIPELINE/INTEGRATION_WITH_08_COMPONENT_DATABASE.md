# Integration With 08_COMPONENT_DATABASE

Playwright research may help create or update component stubs, but captured browser data is not a verified component record.

## Dry-Run Outputs

- Candidate manufacturer part numbers.
- Candidate supplier SKUs.
- Candidate datasheet links.
- Candidate package text.
- Candidate symbol and footprint search terms.
- Human-review-required notes.

## Required Status

All generated component database updates must remain `UNVERIFIED` or `UNVERIFIED_PLACEHOLDER` until official source and human review evidence exists.

## Prohibited Claims

Do not use Playwright output alone to approve voltage limits, current limits, pinouts, symbol mappings, footprints, package drawings, or lifecycle status.

