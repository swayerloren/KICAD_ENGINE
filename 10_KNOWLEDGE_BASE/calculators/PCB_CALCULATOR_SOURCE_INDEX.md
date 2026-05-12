# PCB Calculator Source Index

Status: `CANONICAL_CALCULATOR_SOURCE_INDEX`

Use this index to decide what kind of source is acceptable before trusting a
calculator result.

## Preferred Source Classes

1. Exact component datasheet formulas and example equations.
2. Official app notes and evaluation-board guides.
3. Official KiCad calculator documentation and local KiCad tool output.
4. Fabricator capability pages when the calculation depends on the chosen board
   house.
5. Local project constraints such as stackup, copper weight, target current,
   thermal rise, and routing limits.

## Guidance Only

- Generic web calculators
- Blog posts summarizing IPC-style sizing
- Marketing pages listing impedance or current tables without assumptions

These may be used as sanity checks only.

## Migrated Source Lineage

- Archived calculator metadata: `02_HISTORY/`
- License-risk raw captures: `21_LICENSE_ATTRIBUTION/license_risk_reviews/`
- Canonical registry anchor:
  `10_KNOWLEDGE_BASE/source_registry/SOURCE_REGISTRY.csv`
