# 04 Schematic Electrical Audit

You are working in:

`[REPO_ROOT]`

ACTIVE PROJECT:

`[ACTIVE_PROJECT_PATH]`

Task: run a strict schematic electrical audit. Do not update PCB.

## Read First

1. `AGENTS.md`
2. `.prompts/shared/HUMAN_DRAFTING_MODE.md`
3. `09_ACCURACY_ENGINE/schematic_rules/SCHEMATIC_CREATION_STANDARD.md`
4. `09_ACCURACY_ENGINE/schematic_rules/POWER_NET_RULES.md`
5. `09_ACCURACY_ENGINE/schematic_rules/USB_C_SCHEMATIC_RULES.md`
6. `09_ACCURACY_ENGINE/schematic_rules/CONNECTOR_PIN_NUMBERING_RULES.md`
7. `09_ACCURACY_ENGINE/workflows/FULL_KICAD_PROJECT_PIPELINE.md`
8. Active project BOM lock, ready-parts list, and prior audits if present.

## Do

1. Locate `.kicad_pro` and `.kicad_sch`.
2. Run ERC if possible.
3. Audit power rails, regulators, decoupling, reset/boot, connectors, USB, ESD, polarity-sensitive parts, and high-risk nets.
4. Apply `HUMAN_DRAFTING_MODE` during the audit:
   - orient symbols before labels
   - use local wire before label when the wire would be short and readable
   - keep local MCU support wiring physically readable when near the MCU pins
   - verify emphasized power/ground/common-return rails as real wires, not
     graphics
   - keep reset/boot topology readable enough to prove no direct
     `+3V3`-to-`GND` short path through a switch
   - enforce visible text ownership
5. Audit whether local nets are using labels as a shortcut for bad symbol
   orientation, weak block flow, or avoidable local wiring.
6. Audit text ownership so references and values visibly belong to the correct
   parts and are not crossed by wires.
7. If rendered-page or crop evidence still shows ugly loopback wiring, label
   spray, detached text, or ambiguous rails, keep the audit open even when ERC
   is clean.
8. Do not guess values, pinouts, footprints, or policies.
9. Mark unresolved items `NEEDS_REVIEW` or blocked.
10. Create or update `SCHEMATIC_ELECTRICAL_AUDIT.md` with symbols needing
    rotation/flip/reposition, labels that should become wires, labels kept and
    why, graphic-line versus electrical-wire verification, topology sanity
    result, and ERC/text/unresolved results when available.

## Required Result

Return one result:

- `SCHEMATIC_ELECTRICAL_PASS`
- `SCHEMATIC_ELECTRICAL_FAIL`
- `NEEDS_HUMAN_REVIEW`

AI quality closeout is required.
