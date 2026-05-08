# Copper Pour GND Zone Report

Generated: 2026-05-07

Status: `NOT_CREATED_ROUTING_PARTIAL`

## Decision

GND copper pours were not created in this session.

Reason: routing is not substantially complete. Final DRC still reports 67 unconnected items, including USB, low-speed, +3V3 distribution, GND, and `/+5V_FUSED`. Creating board-wide GND zones at this state would hide routing incompleteness and could introduce copper/clearance issues before the routed topology is stable.

## Zone Counts

| item | before | after |
|---|---:|---:|
| Board copper zones | 0 | 0 |
| New F.Cu GND zones | 0 | 0 |
| New B.Cu GND zones | 0 | 0 |
| New stitching vias | 0 | 0 |

The ESP32 RF no-copper keepout remains present as footprint keepout geometry and was not converted into or replaced by a copper zone.

## RF Keepout

Result: `NO_COPPER_POUR_CREATED__NO_TRACK_OR_VIA_POINT_HITS`

Current track/via inspection found zero route endpoints or vias inside the RF keepout rectangle recorded in project intelligence (`x=6..54`, `y=0.25..21.25`).

## Copper Pour Classification

`COPPER_POUR_BLOCKED_BY_INCOMPLETE_ROUTING`

