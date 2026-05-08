# Create PCB Workflow

## Steps

1. Confirm the active project's `reports/SCHEMATIC_TO_PCB_GATE_STATUS.md` is exactly `PASS`.
2. Confirm the active project's footprint/package gate result is `PASS` or `SAFE_CANDIDATE_WITH_EVIDENCE`.
3. Confirm the active project's `reports/PCB_LAYOUT_SANDBOX_GATE_STATUS.md` is exactly `PASS`.
4. Confirm schematic ERC passes.
5. Confirm schematic annotation passes through KiCad-native annotation evidence.
6. Confirm all physical footprints are assigned.
7. Confirm high-risk footprints are either exact-verified or documented as safe candidates with source evidence.
8. Confirm the sandbox report set exists with:
   - at least three variants
   - a variant scorecard
   - a selected layout plan
   - connector-orientation planning
   - antenna-keepout planning
   - board-shape/dimension planning
   - routing-feasibility evidence
   - an auto-approval report
   - sandbox auto-approval status `AUTO_APPROVED_FOR_PCB_WORK`
9. Confirm board dimensions are defined.
10. Confirm active project and backup plan before edits.
11. Read `09_ACCURACY_ENGINE/workflows/AUTO_PCB_START_WORKFLOW.md` and `09_ACCURACY_ENGINE/checklists/AUTO_PCB_START_CHECKLIST.md`.
12. Read relevant `09_ACCURACY_ENGINE/pcb_rules`.
13. Only then update or create the real `.kicad_pcb`.
14. Apply the approved board outline.
15. Place fixed mechanical components according to the auto-approved layout plan.
16. Place main component groups and power-path clusters according to source requirements.
17. Run DRC and export placement visual evidence.
18. Record unresolved risks.

## Exit Criteria

No real PCB update from schematic or placement is allowed until:

- `SCHEMATIC_TO_PCB_GATE_STATUS.md` is exactly `PASS`
- footprint/package gate is `PASS` or `SAFE_CANDIDATE_WITH_EVIDENCE`
- `PCB_LAYOUT_SANDBOX_GATE_STATUS.md` is exactly `PASS`
- the selected variant auto-approval result is `AUTO_APPROVED_FOR_PCB_WORK`
- the `AUTO_PCB_START_WORKFLOW.md` preconditions all pass

No PCB is complete until sandbox variant evidence, sandbox auto-approval evidence, footprint, orientation, polarity, layout, and DRC evidence are recorded.
## Mandatory Accuracy Gate

Before PCB creation, every footprint must have a candidate status and package drawing status. High-risk connector, polarity, RF, USB, CAN, and power-layout items must be exact-verified or explicitly documented as safe candidates before sandbox auto-approval. The selected layout plan is not approved until sandbox auto-approval status `AUTO_APPROVED_FOR_PCB_WORK` is recorded in `PCB_LAYOUT_SANDBOX_GATE_STATUS.md`. After that, automatic PCB start may continue only through `AUTO_PCB_START_WORKFLOW.md`.
