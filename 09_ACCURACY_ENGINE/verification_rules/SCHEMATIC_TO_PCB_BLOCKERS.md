# Schematic To PCB Blockers

## Purpose

This file defines hard blockers that prevent an AI agent from moving a KiCad project from schematic work into PCB update, layout, routing, zones, or manufacturing-style output.

## Gate File Rule

PCB work is blocked unless the active project contains:

`reports/SCHEMATIC_TO_PCB_GATE_STATUS.md`

The file must state:

`Gate result: PASS`

Any other state blocks PCB work.

## Hard Blockers

The agent must mark `SCHEMATIC_TO_PCB_GATE_STATUS` as `BLOCKED` when any of these are true:

1. Active project is not confirmed.
2. Target files are outside the active project path.
3. Schematic path is missing or ambiguous.
4. Backup and rollback plan are missing for any intended KiCad edit.
5. Any annotation placeholder remains:
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
6. ERC has not been run for the current schematic revision.
7. ERC report path is missing.
8. ERC failed, or warnings/errors are unresolved.
9. Full-page schematic visual export is missing.
10. Close-up visual review is missing.
11. Any close-up visual review block failed or remains unclear.
12. Footprint, library, or file-path fields are visible in normal schematic view and obscure review.
13. Electrical audit is missing or failed.
14. BOM lock audit is missing or failed.
15. Component values do not match BOM lock and are not intentionally marked `NEEDS_REVIEW`.
16. Any high-risk component has unresolved `NEEDS_REVIEW`.
17. AO3401A symbol/footprint pin mapping is unresolved.
18. USB VBUS policy is unresolved.
19. USB shield policy is unresolved.
20. Power rail naming does not match project standard.
21. Regulator passives are not verified against source evidence.
22. USB-C CC wiring is not verified.
23. USB-C ESD wiring is not verified.
24. USB-C series resistor wiring is not verified where applicable.
25. ESP32 EN wiring is not verified.
26. ESP32 BOOT or strapping behavior is not verified.
27. Any footprint is unassigned.
28. Any footprint is not verified to an exact package drawing.
29. Any connector orientation review is incomplete.
30. Any polarity-sensitive part review is incomplete.
31. Human-review-required items are not listed.
32. A human-review-required high-risk item remains unresolved.

## Forbidden Actions While Blocked

While any blocker exists, an agent must not:

- Update PCB from schematic.
- Import schematic changes into a PCB.
- Create a PCB file from the schematic.
- Place parts.
- Route traces.
- Create or modify zones.
- Move mounting holes.
- Generate Gerbers, drills, pick-and-place, STEP, fab drawings, or assembly outputs.
- Claim layout is ready to begin.

## Blocker Resolution Evidence

Every blocker must be resolved with one of:

- Command output path.
- ERC report path.
- Visual export path.
- Visual review report path.
- Electrical audit report path.
- BOM lock audit path.
- Datasheet or package drawing path or source URL.
- KiCad file inspection evidence.
- User-confirmed decision recorded in project memory/history.

Do not resolve blockers with assumptions.
