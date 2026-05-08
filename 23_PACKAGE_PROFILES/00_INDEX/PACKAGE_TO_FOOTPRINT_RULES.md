# Package To Footprint Rules

Status: `ACTIVE_RULES`

## Prime Rule

Never choose a KiCad footprint from package family or pin count alone.

## Required Evidence

- Exact part number or exact package code.
- Package drawing or manufacturer land pattern.
- Pad count and pad numbering.
- Pitch.
- Body outline.
- Pad or lead dimensions.
- Drill information for through-hole parts.
- Pin 1 or orientation marker.
- Height and courtyard needs when mechanical fit matters.

## Candidate Workflow

1. Identify the exact package and orderable suffix.
2. Find package drawing or land pattern.
3. Search KiCad installed and project-local libraries for candidates.
4. Compare pad count, numbering, pitch, pad dimensions, courtyard, fab outline, and pin 1 marker.
5. Record candidate status and unresolved risks.
6. Require human review before approval.

## High-Risk Packages

- Connectors.
- RF connectors.
- USB-C connectors.
- Modules with antenna keepouts.
- Exposed-pad packages.
- Fine-pitch QFN/DFN/BGA.
- Through-hole parts with mechanical constraints.

## Status Labels

- `FOOTPRINT_CANDIDATE_ONLY`
- `UNVERIFIED_FOOTPRINT`
- `FOOTPRINT_VERIFIED_AGAINST_DRAWING`
- `PROJECT_LOCAL_COPY_RECOMMENDED`
- `BLOCKED_UNTIL_HUMAN_REVIEW`

