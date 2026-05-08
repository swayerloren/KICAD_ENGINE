# Routing Geometry Quality

- project: `bad_pad_entry_route`
- status: `AUTO_BLOCKED_BAD_LAYOUT`
- trace_count: `2`
- finding_count: `1`

## Hard Fail Statuses

- PAD_ENTRY_GEOMETRY_POOR

## Findings

| net | status | layer | segment_coordinates | reason | recommended_fix |
| --- | --- | --- | --- | --- | --- |
| BOOT0 | PAD_ENTRY_GEOMETRY_POOR | F.Cu | (2.0, 2.0) -> (2.2, 2.0) ; (2.2, 2.0) -> (4.2, 4.0) | Critical net bends after only 0.2 mm of pad runout. | Extend a straight pad exit to at least 0.75 mm before the first bend. |
