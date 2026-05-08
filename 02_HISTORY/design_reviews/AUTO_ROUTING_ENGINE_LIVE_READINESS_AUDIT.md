# AUTO_ROUTING_ENGINE_LIVE_READINESS_AUDIT

Date: `2026-05-07`

Classification: `FIXTURE_TESTED_NOT_READY_FOR_REAL_KICAD_BOARD`

## Audit Summary

The original routing scripts were functional but thin. They parsed ad hoc JSON and performed limited checks, but they were not yet strict enough to support real routing decisions.

This session upgraded the routing layer to:

- use a concrete routing input schema
- use a concrete routing output schema
- define a trace-audit schema
- define a net-class schema
- support realistic sample fixtures
- emit both JSON and Markdown
- enforce hard-fail routing rules
- generate a routing scorecard with exact blockers

## Audit Of Prior Script State

Before this patch, the routing scripts:

- could parse simple JSON inputs
- could build a staged routing order
- could extract critical-net entries
- could detect unrouted nets
- could detect simple keepout crossings
- could audit angles and missing via reasons

But they were still weak in the following ways:

1. no formal routing input schema
2. no formal routing output schema
3. no fixture set for repeatable testing
4. no strict hard-fail rule set
5. no consistent JSON + Markdown output contract
6. no readiness logic beyond simple blocked/pass states
7. no explicit audit-completeness requirement tied to scorecard status

## Improvement Result

After the patch:

- good fixtures pass
- the intentionally bad fixture blocks for the right reasons
- the engine now exposes exact blocker lists instead of vague failure
- the engine now behaves like a routing-planning and audit system rather than a placeholder script set

## Current Readiness Decision

Routing engine ready for a real KiCad PCB test: `NO`

## Exact Blockers Before Real Project Routing

1. No real `.kicad_pcb` extraction path into `ROUTING_INPUT_SCHEMA.md` exists yet.
2. No copied-board `pcbnew` or `kicad-cli` exporter currently produces the routing fixture automatically from a real board.
3. No real-board DRC result is consumed by `score_routing_plan.py`.
4. Differential-pair quality is still approximated; it is not measured from real board geometry.
5. The engine is fixture-tested only; it has not yet been run on a copied KiCad PCB and reviewed against that board’s actual geometry.
6. Active project `ESP32_CSI_WIFI_NODE` remains blocked by upstream schematic/sandbox gates and is not an allowed routing target.

## Recommended Next Step

Build a copied-board routing extractor for `.kicad_pcb` into the routing schema, then run the routing engine against a non-production copied KiCad board with DRC evidence.
