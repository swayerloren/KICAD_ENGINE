# ESP32_CSI_WIFI_NODE Layout Sandbox Variants Created

Date: `2026-05-07`

## Summary

Created three project-local PCB layout sandbox variants for `ESP32_CSI_WIFI_NODE`, compared them with the sandbox scoring rules, and recorded a provisional front-runner without editing the real PCB.

## Work Performed

1. Read the requested startup, sandbox, gate, and project-status files.
2. Incremented the active-project prompt counter and confirmed maintenance was not due.
3. Captured baseline hashes for the active project's `.kicad_pcb`, `.kicad_sch`, and `.kicad_pro` files.
4. Drafted three variants:
   - compact dev-board style
   - connector/mechanical optimized
   - routing/power/RF optimized
5. Scored all three variants with the sandbox scoring script.
6. Wrote comparison and selected-plan files.
7. Updated project memory and the main handoff note with the planning result.
8. Rechecked that no KiCad design files changed.

## Result

- Three variants created: `YES`
- Best conceptual front-runner: `VARIANT_C_ROUTING_POWER_RF_OPTIMIZED`
- Real KiCad PCB placement/editing approved: `NO`

## Follow-Up

- LJ must review the selected plan and the outstanding mechanical assumptions before any PCB placement action is approved.
- Exact package/footprint and upstream schematic-to-PCB gate blockers still need resolution outside this planning task.
