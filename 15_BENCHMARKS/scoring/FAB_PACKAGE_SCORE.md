# Fabrication Package Score

Default verification/manufacturing allocation: 15 points when a task includes manufacturing-style outputs.

## Criteria

| Area | Points | Checks |
| --- | ---: | --- |
| Output completeness | 4 | Gerbers, drills, BOM, PNP, assembly notes, drawings, STEP/renders, and manifest when applicable |
| Verification reports | 3 | ERC and DRC reports included or absence justified by task scope |
| BOM/PNP review | 3 | BOM fields, quantities, DNP, MPNs, package metadata, PNP side/rotation/origin, and assembly risk notes |
| `NOT_FINAL` discipline | 2 | All manufacturing-style outputs are labeled `NOT_FINAL` until full human review |
| Human review gates | 2 | Connector, polarity, mechanical fit, board-house constraints, and fabrication notes flagged |
| Traceability | 1 | Output paths, tool versions, timestamp, and source project snapshot are recorded |

## Automatic Penalties

- Output labeled final without full verification: cap at 40 total score.
- Missing DRC report when PCB outputs are generated: subtract up to 3.
- Missing BOM when assembly output is implied: subtract up to 3.
- Missing PNP review when assembly output is implied: subtract up to 3.
- Missing connector/polarity/mechanical review: subtract up to 3.

## Rule

This score never means fabrication approval. It only measures whether the output package is complete enough for review under the benchmark task.
