# Routing Geometry Quality

- project: `bad_90_degree_route`
- status: `AUTO_BLOCKED_BAD_LAYOUT`
- trace_count: `2`
- finding_count: `1`

## Hard Fail Statuses

- RIGHT_ANGLE_FOUND

## Findings

| net | status | layer | segment_coordinates | reason | recommended_fix |
| --- | --- | --- | --- | --- | --- |
| EN | RIGHT_ANGLE_FOUND | F.Cu | (2.0, 2.0) -> (6.0, 2.0) ; (6.0, 2.0) -> (6.0, 6.0) | Found a 90.0 degree bend. Routing requires 45-degree or smoother geometry. | Replace the 90-degree corner with a 45-degree bend or a smoother critical-net path. |
