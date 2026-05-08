# Remaining Blockers Before NOT_FINAL Export

Generated: 2026-05-07

Status: `NOT_FINAL_EXPORT_BLOCKED`

## Blockers

| blocker | evidence | required repair/decision |
|---|---|---|
| Routing incomplete | `FULL_ROUTING_SAFE_PARTIAL_DRC4.rpt` reports 67 unconnected items | Complete routing or document true physical blockers |
| U2 drill-size DRC open | 12 `drill_out_of_range` violations on U2 pad 41 | LJ/fab/footprint decision; adjust footprint/rules only with approval |
| GND copper zones not created | `COPPER_POUR_GND_ZONE_REPORT.md` | Create/refill zones only after routing is substantially complete |
| USB section unrouted | Unconnected CC/D+/D-/shield items | Route USB cluster cleanly while preserving J2 orientation and avoiding RF/buck noise |
| Low-speed/control/test nets unrouted | Unconnected ESP_EN/BOOT0/UART/LED/test pad items | Route remaining low-speed nets |
| J1 3D model proof missing | Connector proof reports | Not a routing hard stop, but keep marked as 3D proof missing for visual/fab review |

## Non-Blockers For Current Partial Routing

- J2 orientation: `PROVEN`.
- J1 visibly flipped wrong: NO based on latest project proof reports.
- Current route RF keepout invasion: none detected.
- Schematic parity: PASS, 0 issues.

## Export Decision

NOT_FINAL export allowed: NO.

