# Datasheet And Source Score

Default datasheet/source allocation: 15 points.

## Criteria

| Area | Points | Checks |
| --- | ---: | --- |
| Source quality | 4 | Official datasheets, reference manuals, package drawings, application notes, vendor reference designs, or clearly labeled public references |
| Citation completeness | 4 | URLs, local paths, document names, revision/date when available, and claim-to-source mapping |
| Exact value discipline | 3 | Exact specs are used only when verified; unknowns are marked clearly |
| Redistribution discipline | 2 | Link-only or metadata-only handling when redistribution rights are unclear |
| Source conflict handling | 2 | Conflicting variants, revisions, clone sources, and generic parts are flagged |

## Automatic Penalties

- Fake URL: cap at 40 total score.
- Exact value without source: subtract up to 3 here and apply master caps.
- Bundled restricted PDF without permission: invalid for public-release comparison until resolved.
- Treating generic web/forum content as datasheet proof: subtract up to 3.

## Required Unknown Wording

Use clear uncertainty labels such as:

- `Unknown - requires source verification`
- `UNVERIFIED_PLACEHOLDER`
- `UNVERIFIED_FOOTPRINT`
- `HUMAN_REVIEW_REQUIRED`

Do not soften uncertainty with vague phrases like "probably fine" in scored claims.
