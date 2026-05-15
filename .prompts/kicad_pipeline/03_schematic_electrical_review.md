# 03 Schematic Electrical Review

You are working in:

`[REPO_ROOT]`

ACTIVE PROJECT:

`[ACTIVE_PROJECT_PATH]`

Task: run a strict schematic electrical review without updating PCB.

## Read First

1. `AGENTS.md`
2. `.prompts/shared/HUMAN_DRAFTING_MODE.md`
3. `34_SCHEMATIC_QUALITY_ENGINE/SCHEMATIC_TO_PCB_READY_GATE.md`
4. `34_SCHEMATIC_QUALITY_ENGINE/VISUAL_READABILITY_SCORECARD.md`
5. `09_ACCURACY_ENGINE/schematic_rules/SCHEMATIC_CREATION_STANDARD.md`
6. `09_ACCURACY_ENGINE/schematic_rules/POWER_NET_RULES.md`
7. `09_ACCURACY_ENGINE/schematic_rules/USB_C_SCHEMATIC_RULES.md`
8. `09_ACCURACY_ENGINE/checklists/SCHEMATIC_READY_FOR_PCB_CHECKLIST.md`
9. Active project BOM lock, ready-parts list, and prior audits if present

## Do

1. Locate the target `.kicad_sch`.
2. Run ERC if possible.
3. Review power rails, regulator support parts, reset and boot, connectors,
   USB, ESD, polarity-sensitive parts, and high-risk nets.
4. Review the latest schematic layout score so electrical correctness does not
   get misreported as visual readiness.
5. Apply `HUMAN_DRAFTING_MODE` checks during the review:
   - local wire before net label
   - orient symbols before labels
   - local MCU support wiring should read physically when local
   - visually emphasized rails must be verified as real wires on the intended
     nets
   - reset/boot topology must remain readable and sane beyond ERC
   - text ownership must be visually correct
6. Explicitly check that reset and boot switches cannot create direct
   `+3V3`-to-`GND` short paths and that local capacitors return to the intended
   nodes.
7. Do not guess values, pinouts, footprints, or policies.
8. Mark unresolved items `NEEDS_REVIEW` or blocked.
9. If rendered-page or crop evidence still shows bad symbol orientation,
   avoidable local labels, ugly loopback wiring, detached text, or ambiguous
   rails, keep the issue open even when ERC is clean.
10. Report symbols that need rotation/flip/reposition, labels that should
    become wires, labels kept and why, graphic-line versus electrical-wire
    verification, topology sanity result, and ERC/text/unresolved results when
    available.

## Required Result

Return one result:

- `SCHEMATIC_ELECTRICAL_PASS`
- `SCHEMATIC_ELECTRICAL_FAIL`
- `NEEDS_HUMAN_REVIEW`
