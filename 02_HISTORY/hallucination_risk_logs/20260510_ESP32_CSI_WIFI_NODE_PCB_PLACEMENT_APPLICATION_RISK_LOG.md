# Hallucination Risk Log

- Risk checked: treating the best prelayout variant as approved for real PCB application just because it won the variant comparison.
  - Mitigation: enforced the explicit `PRELAYOUT_VARIANT_READY_FOR_REAL_PCB_APPLICATION` precondition.
- Risk checked: treating `J1` orientation as proven from geometry alone.
  - Mitigation: kept the human-review blocker from the orientation audit.
- Risk checked: implying that no KiCad design files were modified anywhere in the repo.
  - Mitigation: reported that the schematic was already dirty from an earlier task while confirming no new PCB edit happened here.
