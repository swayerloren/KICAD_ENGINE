# Hallucination Risk Log

- Risk checked: treating a high angle-feasibility score as permission for real placement.
  - Mitigation: kept the final classification blocked unless the full prelayout gate passed.
- Risk checked: treating connector XY position or rotation as sufficient proof.
  - Mitigation: used the mechanical-orientation truth layer and kept `J1` at `NEEDS_HUMAN_REVIEW`.
- Risk checked: assuming the repo had no KiCad design-file changes because this run was read-only.
  - Mitigation: checked `git diff` directly and disclosed that the schematic was already dirty from a previous task.
