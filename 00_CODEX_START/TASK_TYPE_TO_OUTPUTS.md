# Task Type To Outputs

## Purpose

This file defines the normal output locations and evidence artifacts expected
from each task route.

All meaningful routes also require session closeout artifacts such as session
logs, command logs, AI self-review, scorecard, claim/evidence matrix, and
uncertainty tracking when applicable.

## SCHEMATIC_CREATE_OR_REPAIR

Typical outputs:

- edited schematic files when the edit gate is allowed
- ERC reports
- active project `reports/schematic_quality/<timestamp>/`
- active project `reports/SCHEMATIC_*.md`
- session and command logs

## SCHEMATIC_VISUAL_CLEANUP

Typical outputs:

- active project `_verification/schematic_visual/`
- active project `reports/CLOSE_UP_REVIEW.md`
- active project `reports/schematic_quality/<timestamp>/`
- rendered image evidence and crop evidence

## NATIVE_ANNOTATION

Typical outputs:

- before/after GUI screenshots and automation reports
- annotation verification reports under project `reports/` or
  `33_KICAD_GUI_AUTOMATION/reports/`
- backup-path evidence
- GUI/CLI ERC evidence
- saved-schematic unresolved-`?` and duplicate-reference scan evidence

## FOOTPRINT_PACKAGE_GATE

Typical outputs:

- active project `FOOTPRINT_LOCK.csv`
- active project `SCHEMATIC_READY_PARTS_LIST.md`
- active project `NEEDS_REVIEW_BEFORE_SCHEMATIC.md`
- footprint/package audit reports
- active project `reports/footprint_package/<timestamp>/`
- gap-analysis or review records under `29_FOOTPRINT_GAP_ANALYSIS/` or project
  `reports/`
- component or project memory updates for durable decisions

## PCB_UPDATE_FROM_SCHEMATIC

Typical outputs:

- updated `.kicad_pcb` when the edit gate is allowed
- active project `reports/PCB_SYNC_STATUS.md`
- DRC evidence
- updated schematic-to-PCB gate or sync reports

## PCB_PRELAYOUT_VARIANT_PLANNING

Typical outputs:

- active project `prelayout_variants/<timestamp>/`
- active project `reports/prelayout_engine/<timestamp>/`
- `PCB_PRELAYOUT_VARIANT_COMPARISON_REPORT.md`
- `PCB_PRELAYOUT_RECOMMENDED_VARIANT.md`
- connector-orientation and route-feasibility audits

## PCB_PLACEMENT

Typical outputs:

- updated `.kicad_pcb` when allowed
- active project `reports/PCB_PLACEMENT_CURRENT_STATE_REPORT.md`
- placement DRC evidence
- active project `_verification/pcb_visual/`
- placement edit contract evidence when a real PCB edit happened

## CONNECTOR_ORIENTATION_AUDIT

Typical outputs:

- active project `reports/mechanical_orientation/`
- connector-orientation JSON or Markdown audits
- issue or memory records for unresolved `NEEDS_HUMAN_REVIEW` items

## PCB_ROUTING

Typical outputs:

- copied-board staged routing reports under `reports/COPIED_BOARD_*`
- real-board staged routing reports under `reports/REAL_PCB_STAGED_ROUTING_*`
- DRC evidence after each stage
- geometry audits after each stage
- active project `_verification/pcb_visual/`
- routing edit contract evidence when a real PCB edit happened

## TRACE_GEOMETRY_AUDIT

Typical outputs:

- active project `reports/pcb_geometry/<timestamp>/trace_quality.json`
- angle audit reports
- SVG or similar overlays for review

## PCB_COPPER_ZONES

Typical outputs:

- updated `.kicad_pcb` when allowed
- zone strategy or zone verification reports
- DRC evidence after refills
- updated PCB visual review outputs

## FAB_EXPORT

Typical outputs:

- fabrication-style outputs under project `fabrication/NOT_FINAL_<timestamp>` or
  approved `05_OUTPUTS/` paths
- manifests, checksums, BOM, CPL/PNP, Gerber, drill, STEP, and review reports
- final export gate reports

## MEMORY_MAINTENANCE

Typical outputs:

- updated `01_MEMORY/` and `02_HISTORY/` entries
- active project `memory/PROMPT_COUNTER.md`
- active project `history/MEMORY_MAINTENANCE_LAST_RUN.md`
- rebuilt repo, memory, history, AI-quality, and known-problem indexes

## OPEN_SOURCE_TOOL_USE

Typical outputs:

- `03_TOOLS/open_source_integrations/` docs and tool profiles
- optional-tool install wrappers and requirements files
- dry-run verification output for optional-tool presence checks
- tool logs and health-check outputs
- source-policy or license-review notes
- sample-intake or public-source research evidence when applicable
- no KiCad design outputs unless a later routed task explicitly allows them
