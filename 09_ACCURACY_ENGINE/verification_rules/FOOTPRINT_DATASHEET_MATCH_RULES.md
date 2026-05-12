# Footprint Datasheet Match Rules

## Purpose

Define what counts as a verified footprint and what must be recorded before
schematic-to-PCB progression.

This rule is enforced through:

- `35_FOOTPRINT_PACKAGE_ENGINE/`
- `FOOTPRINT_LOCK.csv`
- `03_TOOLS/scripts/footprint_package/run_footprint_package_gate.py`

## Required Match Evidence

- exact reference and symbol under review
- exact manufacturer part number when known
- exact package code or exact package family proof
- package drawing or recommended land pattern
- KiCad footprint path or project-local footprint name
- pad count and numbering match
- polarity or pin-1 convention match when applicable
- mechanical orientation match for connectors
- explicit review record in `FOOTPRINT_LOCK.csv`

## High-Risk Additions

Also require:

- PMOS and reverse-polarity FETs:
  symbol-pin to footprint-pad proof
- connectors:
  mechanical orientation proof
- connectors and mechanical parts:
  3D-model status or explicit human-review requirement
- modules, regulators, ESD, TVS, inductors, fuses:
  package-drawing proof, not name similarity

## Not Enough

- footprint name looks similar
- package code looks close
- 3D model appears to fit
- another project used it
- DRC is clean
- symbol default footprint field points to it
- lock file row exists but proof fields are blank

## Gate Result

Use `FOOTPRINT_VERIFIED_AGAINST_DRAWING` only when the evidence above is
recorded.

Footprint-to-datasheet match claims require exact package proof. Name
similarity, 3D fit, or clean DRC do not prove package correctness.

Connector, RF, USB-C, barrel-jack, and other mechanical-sensitive footprints
remain `BLOCKED_UNTIL_HUMAN_REVIEW` until exact drawing and orientation are
reviewed.

## Source Registry References

- `url_009904` - TI TPD2E2U06 datasheet
- `url_009905` - TI TPD4E02B04 datasheet
- `url_009915` - TI TPS62180 datasheet
- `url_009918` - TI TPS62933 datasheet
- `url_010060` - USB.org connector-compliance document index entry, supporting only
