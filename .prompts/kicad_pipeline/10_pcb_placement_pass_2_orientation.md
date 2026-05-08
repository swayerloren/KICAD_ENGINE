# 10 PCB Placement Pass 2 Orientation

You are working in:

`[REPO_ROOT]`

ACTIVE PROJECT:

`[ACTIVE_PROJECT_PATH]`

Task: perform placement pass 2 focused on orientation, mechanical correctness, courtyard clearance, and readability. Do not route traces.

## Mandatory Phase Gate

This is Phase 6. Before doing anything, run:

`python 03_TOOLS/scripts/project_gate/check_phase_allowed.py --project "[ACTIVE_PROJECT_PATH]" --phase 6`

If the result is `BLOCKED`, stop and report the missing earlier phase. Do not proceed to routing until placement and placement-audit evidence exists.

## Read First

1. `AGENTS.md`
2. `reports/PCB_PLACEMENT_PASS_1_REPORT.md`
3. `reports/PCB_LAYOUT_SANDBOX_SELECTED_VARIANT.md`
4. `34_PCB_LAYOUT_SANDBOX/CONNECTOR_ORIENTATION_RULES.md`
5. `34_PCB_LAYOUT_SANDBOX/RF_ANTENNA_KEEP_OUT_RULES.md`
6. `34_PCB_LAYOUT_SANDBOX/BOARD_SHAPE_AND_MECHANICAL_RULES.md`
7. `34_PCB_LAYOUT_SANDBOX/HUMAN_REVIEW_GATE.md`
8. `09_ACCURACY_ENGINE/pcb_rules/CONNECTOR_ORIENTATION_RULES.md`
9. `09_ACCURACY_ENGINE/pcb_rules/CONNECTOR_EDGE_ORIENTATION_RULES.md`
10. `09_ACCURACY_ENGINE/pcb_rules/BARREL_JACK_ORIENTATION_RULES.md` when a barrel jack is present
11. `09_ACCURACY_ENGINE/pcb_rules/TEST_PAD_PLACEMENT_RULES.md`
12. `09_ACCURACY_ENGINE/pcb_rules/ESP32_RF_KEEP_OUT_PLACEMENT_RULES.md`
13. `09_ACCURACY_ENGINE/pcb_rules/PCB_MECHANICAL_CLEARANCE_RULES.md`
14. `09_ACCURACY_ENGINE/pcb_rules/PILL_STYLE_DEV_BOARD_LAYOUT_RULES.md` when this is a dev-board/pill-style layout
15. `09_ACCURACY_ENGINE/checklists/PILL_STYLE_PLACEMENT_CHECKLIST.md` when this is a dev-board/pill-style layout
16. `09_ACCURACY_ENGINE/pcb_rules/POLARITY_ORIENTATION_RULES.md`
17. `11_LIBRARY_FACTORY/footprints/FOOTPRINT_QA_CHECKLIST.md`
18. `09_ACCURACY_ENGINE/workflows/FULL_KICAD_PROJECT_PIPELINE.md`

## Do

1. Create backup.
2. Check every footprint against the selected sandbox variant for ref/value readability, pin 1, connector direction, USB shell/mechanical tabs, polarity, ESP32 antenna/keepout, mounting holes, test pads, courtyards, and board edge clearance.
3. Run DRC.
4. Export top/bottom visuals and close-ups.
5. Create `reports/PCB_PLACEMENT_PASS_2_ORIENTATION_REPORT.md`.

## Mandatory Audit Checks

The placement audit must explicitly answer:

1. Does the board match the intended form factor without giant unexplained dead areas?
2. Are all connector ports facing the intended board edge?
3. Is USB-C bottom-edge aligned on dev-board layouts?
4. Is USB-C receptacle mouth proven to face off-board, with the `PCB Edge` line aligned to the board edge and pads on-board?
5. Is any barrel jack retained on a narrow board, and if so is it mechanically accepted or flagged?
6. For any barrel jack, does the female opening/front face off-board and does the 3-pin solder/backside face inward?
7. For bottom-edge J1, does the female opening face down/off-board and the 3-pin solder side face up/inward?
8. Are connector orientations proven by footprint geometry and 3D screenshot evidence where available, not coordinates alone?
9. Are test pads in clean rows and clear of USB-C, connector shells, and component clusters?
10. Are reset/boot buttons accessible?
11. Are LEDs visible and not buried in dense placement?
12. Are mounting holes outside RF keepouts and connector mechanical areas?
13. Is four-hole mounting proven practical on narrow boards?
14. Are all component/courtyard/text/pad overlaps repaired?
15. Is the ESP32 RF keepout at the board edge and clear?
16. Has LJ visually approved placement before routing?

If any answer is `NO`, do not classify placement as routing-ready.

## Required Result

Return one result:

- `PLACEMENT_ORIENTATION_PASS`
- `PLACEMENT_ORIENTATION_FAIL`
- `NEEDS_HUMAN_REVIEW`

For pill-style/dev-board placement audits, use one:

- `PLACEMENT_READY_FOR_LJ_REVIEW`
- `PLACEMENT_NEEDS_MORE_REPAIR`
- `BLOCKED_BY_MECHANICAL_OR_FOOTPRINT_RISK`

Routing remains blocked unless the audit says `PLACEMENT_READY_FOR_LJ_REVIEW` and LJ approves.

Connector-orientation warning: barrel jack female opening/front must face off-board and the 3-pin solder/backside must face inward. USB-C receptacle mouth must face off-board and the footprint `PCB Edge` line must align with the board edge. Do not route until connector orientation is visually/proof-audited.

AI quality closeout is required.
