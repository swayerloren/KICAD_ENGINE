# Claim / Evidence Matrix

| claim | evidence |
|---|---|
| Placement readiness scoring was added. | `14_LAYOUT_AUTOMATION/PLACEMENT_READINESS_SCORECARD.md`; `14_LAYOUT_AUTOMATION/scripts/score_placement_readiness.py` |
| Real-board placement risk detectors were added. | `detect_connector_orientation_risks.py`; `detect_power_path_placement_risks.py`; `detect_usb_cluster_placement_risks.py`; `detect_antenna_keepout_placement_risks.py`; `detect_testpad_accessibility_risks.py` |
| Routing preconditions now require fresh placement readiness evidence. | `14_LAYOUT_AUTOMATION/REAL_PROJECT_ROUTING_PRECONDITIONS.md`; `14_LAYOUT_AUTOMATION/REAL_PROJECT_ROUTING_WORKFLOW.md`; `09_ACCURACY_ENGINE/checklists/FULL_PIPELINE_GATE_CHECKLIST.md` |
| The active copied board scored placement-ready. | `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/PLACEMENT_READINESS_SCORECARD.md`; `02_HISTORY/design_reviews/PLACEMENT_READINESS_SCORING_AUDIT.md` |
| No KiCad design files were edited. | `git status`; absence of `.kicad_sch`/`.kicad_pcb` modifications in this change set |
