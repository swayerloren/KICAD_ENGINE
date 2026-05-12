# Buck Regulator Layout Reference Rules

Status: `REFERENCE_RULES_ACTIVE`

## Purpose

Guide comparison of switching-regulator placement and routing style against
reviewed open-source examples.

## Compare

- regulator, inductor, and bootstrap/output capacitors kept tight
- obvious high-current loops kept compact
- input filtering kept near the power entry
- schematic power flow stays readable
- power traces avoid boxy perimeter detours

## Do Not Assume

- a sample with zero DRC issues has a good current-loop layout
- every buck circuit should copy one exact component arrangement

## Hard Rule

Use reference samples to notice compactness and readability patterns, but keep
the active project's power-loop geometry and component-pin mapping proofs as the
authoritative gate.
