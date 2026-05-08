# Critical Net Routing Rules

## Purpose

Define the routing expectations for nets that must be handled first.

## Critical Classes

- power entry and protection
- regulator switching loop
- main 3V3 rail
- USB D+/D-
- ESD / connector protection connections
- RF feed or keepout-adjacent traces
- boot / reset / enable nets near noisy areas
- decoupling connections

## Rules

- Critical nets route before cosmetic or low-risk nets.
- Critical-net routing must remain short, intentional, and reviewable.
- If a critical-net route looks awkward, placement repair should be considered before forcing copper.
- Every critical net must be called out explicitly in the routing plan and in the trace-by-trace audit.
