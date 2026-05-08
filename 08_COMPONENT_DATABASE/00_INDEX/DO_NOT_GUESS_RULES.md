# Component Database Do Not Guess Rules

## Purpose

These rules prevent KiCad Engine agents from turning component records into unsupported schematic, footprint, BOM, or PCB layout claims.

## Absolute Rules

- Do not invent datasheet values.
- Do not infer pinouts from memory.
- Do not approve a KiCad symbol without pinout evidence.
- Do not approve a KiCad footprint without the exact package or connector drawing.
- Do not treat a generic connector record as an exact manufacturer part.
- Do not treat a module footprint as verified unless its land pattern and keepout are checked against the module datasheet.
- Do not treat a 3D model as proof of footprint correctness.
- Do not claim lifecycle, sourcing, or availability without a current source check.
- Do not claim ERC, DRC, BOM, or manufacturing readiness without actual output evidence.

## Placeholder Rule

Records marked `UNVERIFIED_PLACEHOLDER` are allowed for planning and task routing only. They are not approved for:

- schematic placement,
- PCB footprint assignment,
- BOM release,
- purchasing,
- manufacturing package generation,
- benchmark scoring as correct,
- public claims of database completeness.

## Required Before Use In A Schematic

Before a part record can guide a schematic, an agent must verify:

- exact part number and suffix,
- vendor source or datasheet URL,
- datasheet revision or document date if available,
- power pins and required decoupling,
- pinout and special pins,
- reset, boot, strap, mode, or programming pins where applicable,
- required external parts,
- voltage and absolute maximum limits from source documents,
- KiCad symbol candidate mapping to verified pinout.

## Required Before Use In A PCB

Before a part record can guide a PCB, an agent must verify:

- exact package,
- package drawing,
- land pattern or footprint recommendation,
- courtyard and assembly clearances,
- pin 1 / orientation marker,
- connector mating orientation where applicable,
- 3D model status if mechanical fit matters,
- special layout rules for power, RF, USB, CAN, crystals, thermal pads, or high-current paths.

## Quality Gate

Mark the work `BLOCKED_UNTIL_HUMAN_REVIEW` if any of these are true:

- package drawing is missing,
- connector orientation is unverified,
- pinout is inferred,
- symbol candidate is unverified,
- footprint candidate is unverified,
- datasheet source is missing,
- lifecycle/source status is unknown for a part that will be purchased,
- the part is polarity-sensitive and orientation was not checked,
- the part is RF/USB/CAN/power-critical and layout rules were not reviewed.

## AI Response Requirement

When using the component database, agents must state:

- which record was used,
- its verification status,
- what evidence supports it,
- what remains unverified,
- whether human review is required.

