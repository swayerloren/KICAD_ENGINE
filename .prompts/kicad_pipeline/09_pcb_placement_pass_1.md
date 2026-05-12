# 09 PCB Placement Pass 1

You are working in:

`[REPO_ROOT]`

ACTIVE PROJECT:

`[ACTIVE_PROJECT_PATH]`

Task: perform PCB placement pass 1. Group and position components logically. Do not route traces.

## Mandatory Phase Gate

This is Phase 5. Before doing anything, run:

`python 03_TOOLS/scripts/project_gate/check_phase_allowed.py --project "[ACTIVE_PROJECT_PATH]" --phase 5`

If the result is `BLOCKED`, stop and report the missing earlier phase. A missing `.kicad_pcb`, missing `PCB_SYNC_STATUS.md`, or missing mechanical setup evidence blocks this task.

## Read First

1. `AGENTS.md`
2. `reports/PCB_UPDATE_FROM_SCHEMATIC_REPORT.md`
3. `reports/PCB_MECHANICAL_SETUP_REPORT.md`
4. `layout_sandbox/SELECTED_LAYOUT_PLAN.md`
5. `34_PCB_LAYOUT_SANDBOX/PCB_LAYOUT_SANDBOX_RULES.md`
6. `34_PCB_LAYOUT_SANDBOX/PCB_WORK_AUTO_START_RULES.md`
7. `34_PCB_LAYOUT_SANDBOX/COMPONENT_PLACEMENT_RULES.md`
8. `34_PCB_LAYOUT_SANDBOX/CONNECTOR_ORIENTATION_RULES.md`
9. `34_PCB_LAYOUT_SANDBOX/RF_ANTENNA_KEEP_OUT_RULES.md`
10. `34_PCB_LAYOUT_SANDBOX/BOARD_SHAPE_AND_MECHANICAL_RULES.md`
11. `34_PCB_LAYOUT_SANDBOX/ROUTING_FEASIBILITY_RULES.md`
12. `09_ACCURACY_ENGINE/workflows/AUTO_PCB_START_WORKFLOW.md`
13. `09_ACCURACY_ENGINE/pcb_rules/PCB_CREATION_STANDARD.md`
14. `09_ACCURACY_ENGINE/pcb_rules/CONNECTOR_ORIENTATION_RULES.md`
15. `09_ACCURACY_ENGINE/pcb_rules/CONNECTOR_EDGE_ORIENTATION_RULES.md`
16. `09_ACCURACY_ENGINE/pcb_rules/BARREL_JACK_ORIENTATION_RULES.md` when a barrel jack is present
17. `09_ACCURACY_ENGINE/pcb_rules/TEST_PAD_PLACEMENT_RULES.md`
18. `09_ACCURACY_ENGINE/pcb_rules/ESP32_RF_KEEP_OUT_PLACEMENT_RULES.md`
19. `09_ACCURACY_ENGINE/pcb_rules/PCB_MECHANICAL_CLEARANCE_RULES.md`
20. `09_ACCURACY_ENGINE/pcb_rules/PILL_STYLE_DEV_BOARD_LAYOUT_RULES.md` when this is a dev-board/pill-style layout
21. `09_ACCURACY_ENGINE/checklists/PILL_STYLE_PLACEMENT_CHECKLIST.md` when this is a dev-board/pill-style layout
22. `09_ACCURACY_ENGINE/workflows/FULL_KICAD_PROJECT_PIPELINE.md`
23. `08_COMPONENT_DATABASE/mechanical_orientation/README.md`
24. `08_COMPONENT_DATABASE/mechanical_orientation/connector_orientation_truth.json`

## Preconditions

- PCB exists.
- Board outline exists.
- Mechanical setup is acceptable.
- Sandbox selected variant exists, is justified, and is the auto-approved basis for placement.
- Backup is created.

## Do

1. Place fixed/mechanical parts first according to the selected sandbox variant.
2. Place module/RF parts with keepouts respected.
3. Place power path in source-to-load order.
4. Place USB/ESD/series parts cleanly.
5. Group boot/reset, LEDs, test pads, and passives logically.
6. Run DRC and create visual close-up evidence.
7. Create `reports/PCB_PLACEMENT_PASS_1_REPORT.md`.

## Pill-Style Dev-Board Hard Rules

For ESP32/STM32-style narrow dev boards:

1. Place ESP32 modules at the top edge with antenna/U.FL/RF keepout facing the top edge unless an exception is documented.
2. Place USB-C on the bottom edge with the mouth facing off-board and the footprint edge line aligned.
3. Barrel jack: female opening/front must face off-board; 3-pin solder/backside must face inward. For bottom-edge J1, female opening faces down/off-board and the 3-pin solder side faces up/inward.
4. USB-C: receptacle mouth must face off-board and the `PCB Edge` line must align with the board edge. Do not approve USB-C from coordinates alone.
5. Treat barrel jacks as mechanically suspicious on narrow boards; retain only with explicit mechanical review.
6. Put test pads in clean rows. Do not mix them into USB, LED, button, or power component clusters.
7. Do not place test pads behind the USB-C shell or cable path.
8. Keep reset/boot buttons accessible at an edge.
9. Keep LEDs visible at an edge or visible board face.
10. Do not place mounting holes in RF keepouts or connector mechanical areas.
11. Do not use four mounting holes on narrow boards unless clearance is proven.
12. Placement is not ready if any component, courtyard, text, pad, connector, hole, or RF keepout overlaps.
13. Placement is not ready if connector ports do not face the intended board edge.
14. Placement is not ready if the board has large unexplained dead areas.
15. Do not route until connector orientation is visually/proof-audited with the mechanical-orientation truth layer.
16. Routing remains blocked until placement gates pass and the placement evidence supports continuation.

## Required Result

Return one result:

- `PLACEMENT_PASS`
- `PLACEMENT_FAIL`
- `NEEDS_HUMAN_REVIEW`

For pill-style/dev-board placements, prefer these more specific classifications in the report:

- `PLACEMENT_READY_FOR_LJ_REVIEW`
- `PLACEMENT_NEEDS_MORE_REPAIR`
- `BLOCKED_BY_MECHANICAL_OR_FOOTPRINT_RISK`

AI quality closeout is required.
