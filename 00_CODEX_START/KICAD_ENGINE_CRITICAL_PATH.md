# KiCad Engine Critical Path

## Purpose

This file shows the normal go/no-go path from startup through schematic, PCB,
routing, zones, exports, and closeout.

If a later step is requested before an earlier gate passes, stop and reroute to
the earliest blocker.

## Critical Path

1. Startup and routing
   Read `START_HERE_FOR_AI_AGENTS.md`, `AGENTS.md`,
   `00_CODEX_START/AI_AGENT_FAST_CONTEXT.md`, and `00_CODEX_START/TASK_ROUTER.md`.

2. Active project, prompt counter, and execution contract
   Confirm `00_CODEX_START/CURRENT_PROJECT.md`, check maintenance, and declare
   one execution-contract task type.

3. Schematic creation or repair
   Route: `SCHEMATIC_CREATE_OR_REPAIR`

4. Native annotation proof
   Route: `NATIVE_ANNOTATION`

5. Schematic visual cleanup and readability gate
   Route: `SCHEMATIC_VISUAL_CLEANUP`

6. Footprint and package gate
   Route: `FOOTPRINT_PACKAGE_GATE`

7. Schematic-to-PCB gate
   Route: `PCB_UPDATE_FROM_SCHEMATIC`
   Required before real PCB sync/update.

8. PCB prelayout variant planning
   Route: `PCB_PRELAYOUT_VARIANT_PLANNING`
   Required before real PCB placement or routing.

9. Real PCB placement
   Route: `PCB_PLACEMENT`
   Connector orientation and antenna keepout proof are mandatory here.

10. Real PCB routing
    Route: `PCB_ROUTING`
    Route `TRACE_GEOMETRY_AUDIT` is a mandatory companion gate.

11. Copper zones
    Route: `PCB_COPPER_ZONES`
    Only after routing is substantially complete and clean enough.

12. Final PCB verification and fabrication export
    Route: `FAB_EXPORT`
    Outputs remain `NOT_FINAL` unless LJ explicitly approves final status.

13. Memory/history closeout and maintenance
    Route: `MEMORY_MAINTENANCE`
    Rebuild indexes, refresh known problems, and write quality artifacts.

## Side Routes

- `CONNECTOR_ORIENTATION_AUDIT`
  Use during prelayout, placement, routing, zone, and export decisions.

- `TRACE_GEOMETRY_AUDIT`
  Use whenever routed-trace quality must be judged.

- `OPEN_SOURCE_TOOL_USE`
  Use for local tool repos, source policies, open sample projects, or
  browser-assisted public-source workflows.

## Stop Conditions

Stop progression immediately when:

- native annotation is not proven
- schematic readability is not verified
- footprints are unresolved
- the schematic-to-PCB gate is not exactly `PASS`
- prelayout does not produce three variants and a passing result
- connector orientation is not proven
- DRC or trace-geometry gates fail
- unrouted or unconnected nets remain before zones or exports
- maintenance is due and has not been run
