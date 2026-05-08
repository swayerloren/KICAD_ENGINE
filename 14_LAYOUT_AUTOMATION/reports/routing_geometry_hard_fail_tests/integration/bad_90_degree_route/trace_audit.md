# Trace By Trace Audit

- project: `bad_90_degree_route`
- status: `AUTO_BLOCKED_BAD_LAYOUT`

## Trace Audit

| net | critical | segments | vias | hard_fail_statuses |
| --- | --- | --- | --- | --- |
| BUCK_SW | True | 1 | 0 | _none_ |
| EN | True | 2 | 0 | RIGHT_ANGLE_FOUND |

## Hard Fails

- RIGHT_ANGLE_FOUND

## Detailed Findings

| net | status | layer | segment_coordinates | reason | recommended_fix |
| --- | --- | --- | --- | --- | --- |
| EN | RIGHT_ANGLE_FOUND | F.Cu | (2.0, 2.0) -> (6.0, 2.0) ; (6.0, 2.0) -> (6.0, 6.0) | Found a 90.0 degree bend. Routing requires 45-degree or smoother geometry. | Replace the 90-degree corner with a 45-degree bend or a smoother critical-net path. |
