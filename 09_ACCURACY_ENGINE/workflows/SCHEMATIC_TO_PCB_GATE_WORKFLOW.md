# Schematic To PCB Gate Workflow

## Purpose

This workflow blocks Codex, Claude, and similar VS Code agents from moving from schematic work into PCB update, placement, layout, routing, zones, or manufacturing-style output until the schematic is proven ready and the active project has an evidence-based sandbox auto-approval result.

The gate is intentionally strict. A schematic that is plausible is not enough. The agent must collect evidence, record review status, and update the project-level gate file before PCB work is allowed.

## Hard Rule

An agent must not update PCB from schematic, import netlist changes, place parts, route traces, create copper zones, tune traces, move footprints, or generate PCB manufacturing outputs unless the active project files `reports/SCHEMATIC_TO_PCB_GATE_STATUS.md` and `reports/PCB_LAYOUT_SANDBOX_GATE_STATUS.md` both exist and both gate results are `PASS`.

If either gate file is missing, stale, incomplete, or marked `BLOCKED`, `FAIL`, `NOT_RUN`, `NEEDS_REVIEW`, or `EVIDENCE_MISSING`, PCB work is blocked.

## Required Inputs

- Active project path confirmed.
- Current schematic path identified.
- Current BOM lock or component lock evidence identified.
- Schematic annotation checker report path identified.
- Schematic completeness checker report path identified.
- BOM lock alignment checker report path identified.
- `NEEDS_REVIEW` marker checker report path identified.
- Current visual exports identified.
- ERC report path identified.
- Electrical audit report path identified.
- Footprint audit report path identified.
- PCB layout sandbox gate report path identified.
- Unresolved `NEEDS_REVIEW` list identified.
- Project memory and history reviewed for open design risks.

## Gate Sequence

1. **Freeze schematic candidate**
   - Stop schematic edits for this review pass.
   - Record schematic file path, timestamp, and intended review scope.

2. **Annotation audit**
   - Run `03_TOOLS/scripts/kicad_schematic_checks/check_schematic_annotation.py`.
   - Save Markdown and JSON reports under the active project's `reports/` folder or another logged evidence folder.
   - Confirm there are no unresolved placeholder references:
     - `C?`
     - `R?`
     - `U?`
     - `D?`
     - `SW?`
     - `J?`
     - `TP?`
     - `MH?`
     - `F?`
     - `Q?`
   - Confirm there are no duplicate physical references, missing reference fields, blank values, vague values where an exact MPN exists in the BOM lock, category/reference mismatches, unassigned physical footprints, or high-risk parts without verification status.
   - Any annotation checker `FAIL` blocks PCB update.

3. **Completeness, BOM-lock, and review-marker audits**
   - Run `03_TOOLS/scripts/kicad_schematic_checks/check_schematic_completeness.py`.
   - Run `03_TOOLS/scripts/kicad_schematic_checks/check_bom_lock_alignment.py` when a BOM lock or ready-parts file is expected.
   - Run `03_TOOLS/scripts/kicad_schematic_checks/check_needs_review_markers.py`.
   - Confirm power input, protection, regulator, MCU/module, required USB-C, ESD, boot/reset, test pads, mounting holes, project/mechanical notes, and expected BOM lock items are present or explicitly blocked.
   - Any missing required block, missing expected BOM item, unresolved high-risk marker, or missing required report blocks PCB update.

4. **ERC audit**
   - Run ERC with the approved KiCad verification workflow.
   - Save the report path.
   - Every ERC item must be fixed, source-justified, or explicitly blocked.
   - A missing ERC report blocks PCB update.

5. **Full-page visual export**
   - Export a full schematic view suitable for review.
   - Save the export path.
   - Missing full-page visual evidence blocks PCB update.

6. **Close-up visual review**
   - Review each functional block at close-up scale.
   - Every block must pass or be explicitly blocked.
   - Normal schematic view must not show footprint, library, or file-path fields that obscure the drawing.

7. **Electrical audit**
   - Review power rails, return paths, enable/reset behavior, boot/strap pins, protection, connector wiring, decoupling, and required passives.
   - Save an electrical audit report path.

8. **BOM lock audit**
   - Confirm all schematic values match the BOM lock or are intentionally marked `NEEDS_REVIEW`.
   - Confirm selected manufacturer parts and package assumptions are known.

9. **Footprint and package audit**
   - Confirm every symbol has a footprint.
   - Confirm every footprint maps to an exact manufacturer package drawing or is blocked.
   - Connector orientation and polarity-sensitive orientation must be reviewed by a human unless exact drawing, 3D model, and orientation notes are verified.

10. **High-risk `NEEDS_REVIEW` audit**
   - No unresolved `NEEDS_REVIEW` may remain on high-risk electrical or mechanical items.
   - High-risk includes power path, USB-C, MOSFET pin mapping, ESP32 boot/reset, connectors, protection, RF, polarity, and fabrication-affecting footprints.

11. **Project-specific blockers**
    - Resolve or explicitly block:
      - AO3401A symbol/footprint pin mapping.
      - USB VBUS and shield policy.
      - Power rail naming.
      - Regulator passives.
      - USB-C CC, ESD, and series resistor wiring.
      - ESP32 EN and BOOT wiring.

12. **PCB layout sandbox gate**
    - Confirm `reports/PCB_LAYOUT_SANDBOX_GATE_STATUS.md` exists.
    - Confirm the active project has a PCB Layout Sandbox report set.
    - Confirm at least three layout variants were created.
    - Confirm a variant scorecard exists.
    - Confirm a selected layout plan exists.
    - Confirm connector-orientation planning exists.
    - Confirm antenna-keepout planning exists.
    - Confirm board-shape/dimension planning exists.
    - Confirm routing-feasibility evidence exists.
    - Confirm the sandbox auto-approval report exists.
    - Confirm the sandbox auto-approval status is `AUTO_APPROVED_FOR_PCB_WORK`.
    - Confirm the project can satisfy `09_ACCURACY_ENGINE/workflows/AUTO_PCB_START_WORKFLOW.md` without generic LJ approval.
    - If any sandbox precondition is missing or blocked, do not ask for generic LJ approval. Create or update an auto-blocked report with exact missing items.

13. **Human review list**
    - List every item that still requires human review.
    - If any human-review-required item is high risk, the gate cannot be `PASS`.

14. **Update gate status**
    - Update `reports/SCHEMATIC_TO_PCB_GATE_STATUS.md`.
    - Update `reports/PCB_LAYOUT_SANDBOX_GATE_STATUS.md` when sandbox evidence is reviewed in the same pass.
    - Use only these gate results:
      - `PASS`
      - `BLOCKED`
      - `FAIL`
      - `NOT_RUN`
    - Do not mark `PASS` unless every required item has evidence.

## Required Evidence Table

The gate status file must include an evidence table with these fields:

- Gate item.
- Status.
- Evidence path.
- Reviewer or agent.
- Date.
- Human review required.
- Notes.

Allowed statuses:

- `PASS`
- `FAIL`
- `BLOCKED`
- `NOT_RUN`
- `EVIDENCE_MISSING`
- `NEEDS_REVIEW`

## Pass Criteria

The schematic-to-PCB gate can be marked `PASS` only when:

- All required checks pass.
- All required reports and visual exports are linked.
- No unresolved high-risk `NEEDS_REVIEW` remains.
- All footprints are verified to exact package drawings.
- Connector orientation review is complete.
- Polarity-sensitive part review is complete.
- Human-review-required items are listed and none block PCB work.
- `PCB_LAYOUT_SANDBOX_GATE_STATUS.md` is exactly `PASS`, which means the sandbox exists, three variants exist, the scorecard exists, the selected layout plan exists, connector-orientation planning exists, antenna-keepout planning exists, board-shape/dimension planning exists, routing-feasibility evidence exists, and the sandbox auto-approval status is `AUTO_APPROVED_FOR_PCB_WORK`.
- The project can enter `AUTO_PCB_START_WORKFLOW.md` without missing evidence.

## Blocked Actions Until PASS

Until the gate result is `PASS`, agents must not:

- Update PCB from schematic.
- Import netlist changes into PCB.
- Place or move parts.
- Route traces.
- Create or modify zones.
- Assign layout constraints as final.
- Generate Gerbers, drills, pick-and-place, STEP, fab drawings, or assembly packages.
- Claim PCB layout can begin.

## Closeout Requirements

After any gate review pass, record:

- Session log.
- Command log if commands were run.
- ERC report path if ERC was run.
- Visual review report paths.
- PCB layout sandbox gate report path if sandbox evidence was checked.
- AI self-review.
- Response scorecard.
- Claim/evidence matrix.
- Uncertainty log.
- Open issue or quality-gate failure for any unresolved blocker.
