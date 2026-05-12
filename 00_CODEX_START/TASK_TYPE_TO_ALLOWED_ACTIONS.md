# Task Type To Allowed Actions

## Purpose

This file states what actions each task route may perform after the required
docs are read and the blockers are clear.

## Global Defaults

- Prefer CLI/API/file inspection before GUI automation.
- Keep generated evidence in `02_HISTORY/`, `05_OUTPUTS/`, or the active
  project's reports/history folders.
- No route may install tools, clone repositories, or weaken required gates.

## SCHEMATIC_CREATE_OR_REPAIR

Allowed:

- inspect and edit the active project's schematic when the edit gate is clear
- run or review ERC and schematic audit scripts
- run or review the schematic quality gate and per-audit reports
- update project reports, memory, and history

Not allowed:

- claim annotation proof from raw text edits alone
- skip schematic readability review when the task includes cleanup or release

## SCHEMATIC_VISUAL_CLEANUP

Allowed:

- adjust schematic readability and visual layout when the edit gate is clear
- generate full-page renders, crop sets, and close-up review reports
- run or review readability, overlap, block-layout, and wire-vs-label audits
- classify visual status as `PASS`, `FAIL`, or `VISUAL_NOT_VERIFIED`

Not allowed:

- treat automated crop generation as automatic `VISUAL_PASS`

## NATIVE_ANNOTATION

Allowed:

- use the safety-gated KiCad GUI annotation workflow
- safely open the exact target `.kicad_pro` and `.kicad_sch` through the
  dry-run-first auto-open path
- save from KiCad GUI and run GUI/CLI ERC when the workflow allows it
- capture screenshots and GUI evidence

Not allowed:

- use raw `.kicad_sch` text edits as annotation proof
- annotate a disputed or wrong-project GUI window

## FOOTPRINT_PACKAGE_GATE

Allowed:

- assign, review, or reject footprints and packages
- create or update `FOOTPRINT_LOCK.csv`, `SCHEMATIC_READY_PARTS_LIST.md`, and
  `NEEDS_REVIEW_BEFORE_SCHEMATIC.md` when the task explicitly requires it
- create footprint-gap or package-audit reports
- run the read-only footprint/package gate and per-audit scripts
- update component and project memory with evidence-backed decisions

Not allowed:

- approve a footprint without exact package-drawing evidence
- treat a schematic footprint field or name similarity alone as proof

## PCB_UPDATE_FROM_SCHEMATIC

Allowed:

- sync or update the PCB from schematic after the gate passes
- run DRC and PCB-sync verification
- create/update PCB-sync and gate reports

Not allowed:

- route traces
- create zones
- treat PCB creation/update as passing when upstream schematic gates failed

## PCB_PRELAYOUT_VARIANT_PLANNING

Allowed:

- extract a digital twin
- generate at least three placement/routing variants
- project routes, score variants, compare candidates, and write reports
- run connector-truth and projected feasibility audits

Not allowed:

- edit the real `.kicad_pcb`
- claim real placement or routing approval without a passing prelayout gate

## PCB_PLACEMENT

Allowed:

- place or move board components on the real PCB only after all placement gates
  pass
- run DRC and placement visuals
- update placement reports and edit evidence

Not allowed:

- route traces
- create zones
- bypass connector-orientation or antenna-keepout proof

## CONNECTOR_ORIENTATION_AUDIT

Allowed:

- inspect connector direction, board-edge alignment, 3D-model evidence, and
  antenna keepout direction
- mark parts `PASS`, `FAIL`, or `NEEDS_HUMAN_REVIEW`
- write audit reports without touching KiCad source

Not allowed:

- treat XY position or rotation value alone as proof
- waive missing 3D-model proof silently

## PCB_ROUTING

Allowed:

- route copied-board rehearsals when required by the workflow
- route the real PCB in stages only when the routing gate is clear
- run DRC and geometry audit after each stage
- stop and repair issues before the next stage

Not allowed:

- continue after new unconnected or unrouted findings
- ignore geometry-rule failures
- start copper pours before routing completion gates are met

## TRACE_GEOMETRY_AUDIT

Allowed:

- run read-only geometry extraction, audits, and visual overlays
- classify routing quality as `PASS`, `FAIL`, or `NOT_RUN`
- block routing-acceptable claims when geometry is poor

Not allowed:

- call routing acceptable on DRC alone

## PCB_COPPER_ZONES

Allowed:

- create or refill zones only after routing is substantially complete and zone
  blockers are clear
- run DRC and visual review after zone changes

Not allowed:

- start zone work while meaningful unrouted or unconnected nets remain
- violate RF keepout or return-path rules

## FAB_EXPORT

Allowed:

- generate fabrication-style outputs only after the final export gate passes
- label outputs `NOT_FINAL` until full verification and LJ approval exist
- build manifests, checksums, BOM/CPL exports, and packaging reports

Not allowed:

- call an export final without explicit LJ approval
- treat package creation as proof of electrical or mechanical correctness

## KNOWLEDGE_RETRIEVAL

Allowed:

- inspect canonical retrieval indexes, registry files, and topic folders
- compare canonical startup maps against retrieval mirrors
- repair broken route-to-knowledge, route-to-tool, or route-to-rule indexes
- produce short task-specific source paths that avoid broad raw-data reads

Not allowed:

- treat historical migration provenance or retired `knowledge_scrape` residue
  as live source-of-truth
- claim source trust or redistribution status without the registry/license
  evidence

## GITHUB_PUSH_PUBLIC_RELEASE

Allowed:

- inspect release-readiness, license, attribution, security, and payload-scope
  docs
- run non-destructive health, status, and security-scope checks
- update startup/router docs so push/public-release work is forced through the
  correct safety surfaces
- write release-readiness reports and blocker summaries

Not allowed:

- stage, commit, push, or publish without explicit user request
- claim the repo is public-ready while license, attribution, or payload
  blockers remain unresolved

## MEMORY_MAINTENANCE

Allowed:

- update `01_MEMORY/`, `02_HISTORY/`, project memory/history, prompt-counter
  files, and index files
- run maintenance and closeout scripts
- rebuild repo, memory, history, AI-quality, and known-problem indexes

Not allowed:

- delete or replace the existing memory/history systems
- rewrite history to hide prior failures

## OPEN_SOURCE_TOOL_USE

Allowed:

- create or update first-party integration docs, requirements files, and
  install wrappers
- inspect local tool repos and wrappers
- run read-only health checks and support scripts
- run optional-tool verification in dry-run mode
- document tool limits, source policies, and license constraints
- use approved public-source research or sample-project intake workflows

Not allowed:

- install tools
- clone repositories
- vendor downloaded repos, `node_modules`, virtual environments, or large
  binaries into tracked Git content
- edit KiCad design files as part of tool-integration-only work
- bypass license, redistribution, or anti-bot rules
