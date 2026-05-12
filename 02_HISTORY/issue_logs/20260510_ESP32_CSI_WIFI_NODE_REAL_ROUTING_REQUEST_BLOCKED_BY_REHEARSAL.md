# ESP32_CSI_WIFI_NODE Real Routing Request Blocked By Rehearsal

Date: `2026-05-10`

## Blocker

The latest copied-board routing rehearsal did not produce a candidate approved
for live PCB application. The best copied candidate still fails DRC, open-net,
geometry, USB, and connector-proof gates.

## Required Before Real Routing

1. copied-board rehearsal must report `COPIED_ROUTING_READY_FOR_REAL_BOARD`
2. prompt-counter maintenance must run
3. live routing-quality blockers must still be rechecked before any live edit
