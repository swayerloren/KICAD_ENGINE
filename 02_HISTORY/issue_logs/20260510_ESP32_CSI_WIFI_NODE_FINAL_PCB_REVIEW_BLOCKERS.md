# ESP32_CSI_WIFI_NODE Final PCB Review Blockers

Date: `2026-05-10`

Status: `OPEN`

## Blockers

1. `22` schematic parity issues remain.
2. `13` unconnected items remain.
3. `/DM_C`, `/DP_C`, and `/DP_E` remain detectably unrouted.
4. `36` trace-geometry findings remain.
5. TP3, TP6, and TP7 violate the test-point stub rule.
6. Four configured power nets are below minimum width.
7. USB route sanity still fails.
8. J1 orientation still needs human review.
9. Current final PCB visual assets are stale relative to the live PCB hash.

## Required Closure

- Repaired live board gate packet with current hash-matched visual evidence.
