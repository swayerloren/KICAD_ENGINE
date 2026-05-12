# Source Trust Rules

Use this hierarchy whenever the knowledge base contains conflicting or incomplete material.

## Trust Hierarchy

1. Official manufacturer datasheets
2. Official manufacturer app notes
3. Official KiCad docs, dev docs, source docs, and library rules
4. Fabricator docs: JLCPCB, PCBWay, OSH Park, Eurocircuits, 4PCB
5. Engineering forums and peer review
6. Blogs and tutorials
7. Reddit, video indexes, search pages, and other low-value navigation pages

## Default Rule

- The lower the trust level, the less authority it has.
- Forums, blogs, Reddit, and videos can suggest ideas or failure modes, but they do not close an engineering decision by themselves.
- If a lower-trust source conflicts with a datasheet or official doc, the official doc wins unless there is a documented erratum.

## Mandatory Cross-Check Areas

These topics require cross-checking before making a recommendation or changing a design:

- Footprints
  - Verify against the component datasheet package drawing and land pattern guidance.
  - Cross-check against KiCad library rules or a trusted vendor library if used.
- Pinouts
  - Verify against the exact part number and package variant in the datasheet.
  - Do not assume family-level pin compatibility.
- Power supplies
  - Verify regulator selection, ratings, and layout against the datasheet.
  - Prefer an app note or evaluation-board layout for switch-mode placement decisions.
- USB-C
  - Verify CC behavior, role assumptions, connector wiring, protection, and high-speed constraints from official sources.
- RF and antenna
  - Verify antenna keepout, matching, ground clearance, and layout limits from official hardware guidelines.
- ESD
  - Verify device placement, connector proximity, and protection topology against vendor guidance.
- DFM and manufacturing
  - Verify clearances, drills, annular rings, solder mask, and assembly assumptions against the actual fabricator rules.
- Trace width and current
  - Treat calculators as starting points only.
  - Cross-check against copper weight, temperature rise assumptions, and board-house capability.
- Thermal design
  - Verify power dissipation, copper area, vias, exposed pad use, and airflow assumptions from official thermal guidance.

## Minimum Evidence Rule

For any high-risk recommendation, use at least two independent supports when possible:
- one primary source of truth
- one corroborating source or implementation reference

Examples:
- Footprint choice: datasheet + KLC or trusted library rule
- Buck layout: datasheet + official app note or eval board
- USB-C protection: connector/controller datasheet + ESD app note
- ESP32 antenna placement: Espressif hardware design guide + module datasheet

## What Not To Do

- Do not infer a footprint from extracted PDF text alone.
- Do not copy a forum answer into a design rule without checking the underlying datasheet or official note.
- Do not trust search pages, generic indexes, or low-value scrape artifacts for engineering facts.
