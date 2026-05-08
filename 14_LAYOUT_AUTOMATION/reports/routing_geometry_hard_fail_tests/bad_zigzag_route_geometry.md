# Routing Geometry Quality

- project: `bad_zigzag_route`
- status: `AUTO_BLOCKED_BAD_LAYOUT`
- trace_count: `2`
- finding_count: `1`

## Hard Fail Statuses

- UNNECESSARY_ZIGZAG_FOUND

## Findings

| net | status | layer | segment_coordinates | reason | recommended_fix |
| --- | --- | --- | --- | --- | --- |
| EN | UNNECESSARY_ZIGZAG_FOUND | F.Cu | (2.0, 2.0) -> (3.0, 2.0) ; (3.0, 2.0) -> (5.0, 4.0) ; (5.0, 4.0) -> (7.0, 4.0) ; (7.0, 4.0) -> (9.0, 2.0) ; (9.0, 2.0) -> (10.0, 2.0) | Trace length is 9.657 mm versus 8.0 mm direct with repeated geometry reversals. | Collapse the jog sequence into a simpler 45-degree path with fewer bends and no unnecessary reversals. |
