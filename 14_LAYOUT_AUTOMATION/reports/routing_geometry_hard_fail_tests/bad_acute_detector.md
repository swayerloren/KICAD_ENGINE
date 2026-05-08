# Acute Jog Detection

- project: `bad_acute_jog_route`
- status: `ACUTE_JOG_FOUND`
- trace_count: `2`
- finding_count: `1`

## Hard Fail Statuses

- ACUTE_JOG_FOUND

## Findings

| net | status | layer | segment_coordinates | reason | recommended_fix |
| --- | --- | --- | --- | --- | --- |
| EN | ACUTE_JOG_FOUND | F.Cu | (2.0, 2.0) -> (7.0, 2.0) ; (7.0, 2.0) -> (9.0, 3.0) | Found a non-45 acute jog of 26.565 degrees. | Rebuild this bend as a 45-degree transition or a straight continuation without an acute jog. |
