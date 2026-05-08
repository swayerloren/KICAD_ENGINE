# REAL_PROJECT_ROUTING_ENGINE_BLOCKERS_REMAIN

Status: `OPEN`

Date: `2026-05-07`

## Summary

The routing engine now has exact real-project preconditions and routing-stop rules, but it is still blocked from use on a real KiCad PCB.

## Exact Blockers

1. No exporter currently converts a real `.kicad_pcb` into the routing input schema.
2. No copied-board routing-state extractor currently feeds real trace, keepout, and net-class data into the audit scripts.
3. No DRC-coupled real-board score path exists yet for the routing scorecard.
4. No first copied-board live run with human-reviewed evidence exists yet.
5. Blocked active projects remain ineligible until their own upstream gates pass.

## Next Step

Build the real-board exporter and copied-board audit path, then run the routing engine on a non-production copied KiCad board.
