# Claim / Evidence Matrix

| Claim | Evidence |
| --- | --- |
| ERC is clean | `_verification/post_human_drafting_rule_update_regression_test/validation/erc.rpt` |
| Text overlap still fails | `.../validation/text_overlaps.json` |
| Unresolved reference check passes | `.../validation/annotation.json` |
| Schematic readability gate still fails | `.../schematic_quality_gate/schematic_quality_report.json` |
| Human-drafting checker now catches reset/boot and rail-truth issues | `.../human_drafting/human_drafting_quality.json` |
| Repo now distinguishes automated crop success from visual pass | `.../visual/CLOSE_UP_REVIEW.json`, `reports/CLOSE_UP_REVIEW.md`, `VISUAL_PASS_IS_NOT_AUTOMATED_PASS.md` |
| Orientation-before-label and local-wire-before-label are now explicit repo requirements | `34_SCHEMATIC_QUALITY_ENGINE/SCHEMATIC_READABILITY_STANDARD.md`, `SCHEMATIC_WIRING_VS_LABEL_RULES.md`, `09_ACCURACY_ENGINE/schematic_rules/WIRE_VS_NET_LABEL_RULES.md` |
| PCB update remains blocked by separate non-visual gates | `reports/SCHEMATIC_TO_PCB_GATE_STATUS.md`, `reports/PCB_LAYOUT_SANDBOX_GATE_STATUS.md`, `reports/footprint_package/20260513_223516/FOOTPRINT_PACKAGE_GATE_REPORT.md` |
