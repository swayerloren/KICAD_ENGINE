# Claim Evidence Matrix - Footprint Gap Analysis

Date: 2026-05-03

| Claim | Status | Evidence |
| --- | --- | --- |
| KiCad 9 install folders were inspected read-only. | `VERIFIED_BY_COMMAND` | `02_HISTORY/command_logs/FOOTPRINT_GAP_ANALYSIS_COMMANDS.md` |
| Installed KiCad footprint inventory counted 155 libraries and 15,415 footprints. | `VERIFIED_BY_COMMAND` | `29_FOOTPRINT_GAP_ANALYSIS/INSTALLED_KICAD_FOOTPRINT_INVENTORY.md` |
| Installed KiCad symbol inventory counted 223 libraries and 22,582 symbols. | `VERIFIED_BY_COMMAND` | `29_FOOTPRINT_GAP_ANALYSIS/INSTALLED_KICAD_SYMBOL_INVENTORY.md` |
| Component database matching checked 125 records. | `VERIFIED_BY_COMMAND` | `05_OUTPUTS/footprint_gap_analysis/FOOTPRINT_GAP_SUMMARY.md` |
| 107 records had candidate footprint matches and 18 had no candidate match. | `VERIFIED_BY_COMMAND` | `05_OUTPUTS/footprint_gap_analysis/FOOTPRINT_GAP_SUMMARY.md` |
| Candidate matches are not exact footprint approvals. | `VERIFIED_BY_FILE` | `11_LIBRARY_FACTORY/README.md`; `08_COMPONENT_DATABASE/00_INDEX/KICAD_SYMBOL_FOOTPRINT_LINKING_RULES.md`; `29_FOOTPRINT_GAP_ANALYSIS/README.md` |
| No KiCad design files were edited. | `VERIFIED_BY_COMMAND` | No command targeted KiCad design files; command log records scope. |

