# Codex KiCad Failure Patterns

Status: `ACTIVE_GUIDANCE`

## Repeated Failures In This Repo

- barrel jack opening confused with pin side
- USB-C mouth pointed inward while placement looked plausible by rotation
- schematic readability over-optimized for labels instead of local wires
- native annotation assumed from file scans instead of KiCad GUI evidence
- zero-DRC state overclaimed while open nets still existed
- routing claimed acceptable despite right angles, acute bends, and long detours
- footprint verification assumed from name similarity

## Required Response

- convert each repeated failure into a blocker, checklist item, or score penalty
- prefer stronger evidence over summary prose
- keep human-review gates when mechanical truth is incomplete

