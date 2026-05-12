# ESP32_CSI_WIFI_NODE Copper Pour Request Blocked

Date: `2026-05-10`

## Blocker

The latest real-routing report does not authorize copper-pour progression. The
board still fails the live routing-quality gate, so ground pours and stitching
cannot begin yet.

## Required Before Copper Pour

1. `reports/REAL_PCB_STAGED_ROUTING_REPORT.md` must say
   `REAL_ROUTING_READY_FOR_COPPER_POUR`
2. live routing-quality blockers must clear
3. final copper work must still respect RF keepout, BUCK_SW, USB return, and
   connector/mechanical clearances
