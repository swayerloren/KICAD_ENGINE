# Hallucination Risk Log - Footprint Gap Analysis

Date: 2026-05-03

## Risk

Footprint candidate search can look authoritative because it returns installed KiCad library names and paths. This can cause an agent to treat a name match as approval.

## Mitigation

- All matches are labeled `UNVERIFIED_CANDIDATE`.
- Reports state that exact package drawing and human review are required.
- Connector, RF, USB-C, PMOS, ESD, regulator, mounting-hole, and test-pad categories are flagged as high risk.

## Remaining Risk

Agents must not use these reports to assign production footprints without package drawing review and project-specific verification.

