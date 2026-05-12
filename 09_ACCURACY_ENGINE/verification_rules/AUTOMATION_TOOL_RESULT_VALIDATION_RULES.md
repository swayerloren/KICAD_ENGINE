# Automation Tool Result Validation Rules

Status: `MANDATORY_FOR_SCRIPT_AND_TOOL_OUTPUTS`

## Hard Rules

1. Automation-tool results must be validated by KiCad ERC/DRC or an
   independent check.
2. Tool version and runtime context must be recorded when the result affects an
   engineering claim.
3. Optional upstream-tool output is advisory until validated locally.
4. File parsing is allowed for audit and extraction, but KiCad-native
   validation remains stronger evidence.
5. Normal Python availability does not prove `pcbnew` availability.
6. Board-aware scripts must use the KiCad Python context rules and safe helper
   layer.

## Required Validation Paths

- Schematic-affecting results -> ERC or GUI-native validation
- PCB-affecting results -> DRC, parity, geometry gate, or independent parser
- Numeric helper results -> independent formula/datasheet cross-check
- Manufacturing/export results -> package validators plus human orientation and
  polarity review

## Disallowed Shortcuts

- treating a successful script exit code as proof
- treating a generated Markdown summary as the judge
- treating a third-party autorouter as trustworthy without quality-gate review
- treating raw file edits as native annotation proof

