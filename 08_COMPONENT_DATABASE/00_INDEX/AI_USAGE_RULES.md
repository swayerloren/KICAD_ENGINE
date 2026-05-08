# AI Usage Rules

Date: 2026-05-02

Status: mandatory rules for AI agents using `08_COMPONENT_DATABASE`.

## Core Rule

This database helps agents find and organize component evidence. It is not fabrication approval, BOM approval, symbol approval, footprint approval, or datasheet verification.

Playwright research output from `31_PLAYWRIGHT_RESEARCH_PIPELINE` is evidence, not truth. Browser-captured part data, supplier fields, datasheet links, package text, screenshots, and public KiCad library page evidence must remain `UNVERIFIED` until checked against an official datasheet/vendor source or human review.

## Allowed Uses

Agents may use this database to:

- Find candidate parts for research.
- Find missing datasheet work.
- Identify likely KiCad symbol and footprint candidates.
- Generate review checklists.
- Flag known common mistakes.
- Prepare source-verification tasks.
- Cross-link `06_DATASHEETS`, KiCad libraries, and project review reports.

## Disallowed Uses

Agents must not use this database to:

- Pick a final part without datasheet and sourcing review.
- Add a schematic symbol without checking pinout.
- Assign a footprint without checking the package drawing.
- Claim a 3D model proves footprint correctness.
- Skip ERC, DRC, BOM review, or visual review.
- Generate fabrication-ready outputs.
- Replace human review for connector orientation, polarity, power, thermal, RF, or safety-critical decisions.

## Placeholder Rules

If a record contains `UNVERIFIED_PLACEHOLDER`, agents must:

- Treat every technical value as unknown.
- Ask for or perform source verification before design use.
- Keep generated outputs as review-only.
- Preserve the warning in downstream summaries.

## Exactness Rule

Do not invent:

- Voltage ranges.
- Current limits.
- Pin count.
- Package type.
- Land pattern dimensions.
- KiCad symbol names.
- KiCad footprint names.
- 3D model paths.
- Lifecycle status.
- Errata.

Use `Unknown - requires source verification` until checked.

## Required Pre-Use Statement

Before using a component record in an answer, an agent must state:

- record path,
- verification status,
- source evidence status,
- symbol status,
- footprint status,
- package drawing status,
- 3D model status,
- whether human review is required.

If any of those fields are unknown, the agent must not present the part as approved.
