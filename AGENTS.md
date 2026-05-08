# AGENTS.md

Strict operating rules for Codex and other AI agents in this KiCad engineering workspace.

## Mandatory Startup Order
At the start of every session, Codex must read this `AGENTS.md` file first.

After reading `AGENTS.md`, Codex must read the following files in this exact order before touching KiCad project files:
1. `README_GPT.md`
2. `FOR CHAT GPT.MD`
3. `00_CODEX_START/START_HERE.md`
4. `00_CODEX_START/SESSION_START_CHECKLIST.md`
5. `00_CODEX_START/STRUCTURE_STANDARD.md`
6. `00_CODEX_START/FOLDER_ROUTING_RULES.md`
7. `00_CODEX_START/CURRENT_KNOWN_PROBLEMS.md`
8. `00_CODEX_START/MEMORY_INDEX.md`
9. `00_CODEX_START/HISTORY_INDEX.md`
10. `00_CODEX_START/KICAD_PHASE_ORDER.md` when working on a KiCad project or pipeline phase.
11. Active project memory/history when working on a project.

Before choosing tools, editing repo structure, making KiCad engineering claims, or touching KiCad files, Codex must also read the relevant supplemental startup files:
- `00_CODEX_START/WORKFLOW_RULES.md`
- `00_CODEX_START/SAFETY_RULES.md`
- `00_CODEX_START/CONTROL_PLANES.md`
- `00_CODEX_START/REPO_MAP.md`
- `00_CODEX_START/REPO_STRUCTURE_INDEX.md`
- `00_CODEX_START/TOOL_INDEX.md`
- `00_CODEX_START/PROJECT_INDEX.md`
- `00_CODEX_START/CURRENT_PROJECT.md`
- `00_CODEX_START/SESSION_CLOSEOUT_CHECKLIST.md`
- `00_CODEX_START/LEARNING_LOOP_RULES.md`
- `00_CODEX_START/MEMORY_AND_HISTORY_ROUTING_RULES.md`
- `00_CODEX_START/USER_CORRECTION_CAPTURE_RULES.md`
- `00_CODEX_START/FAILED_ATTEMPT_CAPTURE_RULES.md`
- `00_CODEX_START/ISSUE_TRACKING_RULES.md`
- `00_CODEX_START/AI_SELF_REVIEW_RULES.md`
- `00_CODEX_START/AI_TRUTHFULNESS_SCORING.md`
- `00_CODEX_START/AI_HALLUCINATION_RISK_RULES.md`
- `00_CODEX_START/AI_RESPONSE_QUALITY_GATE.md`
- `00_CODEX_START/AI_EVIDENCE_REQUIREMENTS.md`
- `00_CODEX_START/AI_UNCERTAINTY_DISCLOSURE_RULES.md`
- `00_CODEX_START/AI_ENGINEERING_CLAIM_RULES.md`
- `00_CODEX_START/AI_CLOSEOUT_SCORECARD_RULES.md`
- `00_CODEX_START/KICAD_PIPELINE_STARTUP_RULES.md`
- `00_CODEX_START/KICAD_PHASE_ORDER.md`

After startup files are read, Codex must review relevant global and project memory/history before touching KiCad files.

## Workspace Boundaries
- Active KiCad projects belong under `04_KICAD_PROJECTS/active/`.
- Templates belong under `04_KICAD_PROJECTS/templates/`.
- Legacy KiCad/Codex tool repositories belong under `03_TOOLS/repos/`.
- Common OS-neutral project intelligence belongs under `03_TOOLS/common/` or established legacy tool paths.
- Windows GUI hands/eyes tooling belongs under `03_TOOLS/windows/`.
- Linux/headless/CI automation tooling belongs under `03_TOOLS/linux/`.
- Generated release outputs belong under `05_OUTPUTS/`.
- Datasheets and reference documents belong under `06_DATASHEETS/`.
- General reference design metadata and link-first notes belong under `07_REFERENCE_DESIGNS/`.
- Structured component intelligence belongs under `08_COMPONENT_DATABASE/`.
- Accuracy and anti-hallucination rules belong under `09_ACCURACY_ENGINE/`.
- Reusable circuit blocks, design patterns, checklists, common mistakes, manufacturing rules, and AI review guidance belong under `10_KNOWLEDGE_BASE/`.
- Symbol, footprint, package-mapping, project-local library, and read-only library QA standards belong under `11_LIBRARY_FACTORY/`.
- Public-source reference design links, summaries, license records, and verification notes belong under `12_REFERENCE_DESIGN_LIBRARY/`.
- New-part datasheet ingestion workflows, extraction rules, AI summary templates, and stub generators belong under `13_PART_INGESTION/`.
- Layout automation reality checks, placement/routing assistance plans, constraint extraction plans, and human layout gates belong under `14_LAYOUT_AUTOMATION/`.
- Benchmark methodology, benchmark task definitions, scoring rubrics, and real run results belong under `15_BENCHMARKS/`.
- Installer coordination and release-facing installer notes belong under `16_INSTALLER/`; current installer implementation remains under `installer/` until a migration is approved.
- Release build staging notes, artifact manifests, checksums, and readiness records belong under `17_RELEASE_BUILD/`.
- Public documentation coordination belongs under `18_PUBLIC_DOCS/`; current public docs remain under `docs/` until a migration is approved.
- Disposable examples and test KiCad workspaces belong under `19_TEST_PROJECTS/`.
- CI/CD planning and workflow coordination belong under `20_CI_CD/`.
- License, attribution, redistribution, and third-party audit records belong under `21_LICENSE_ATTRIBUTION/`.
- Security model, secret-handling, and vulnerability response support belong under `22_SECURITY/`.
- Package creation profiles for release, installer, review, and documentation bundles belong under `23_PACKAGE_PROFILES/`.
- Fabrication-house profile guidance and NOT_FINAL manufacturing export rules belong under `24_FAB_PROFILES/`.
- Vendor, manufacturer, distributor, lifecycle, and sourcing metadata belong under `25_VENDOR_DATABASE/`.
- AI quality, evidence, scorecard, and hallucination-risk support artifacts belong under `26_AGENT_QUALITY/`.
- Safe examples, tutorials, and toy records belong under `27_EXAMPLES/`.
- Supplier API/CSV ingestion policies, connector scaffolds, normalized supplier records, stock/pricing snapshots, and sourcing gap reports belong under `28_SUPPLIER_INGESTION/`.
- Installed-KiCad footprint/symbol inventory, footprint candidate matching, and missing-footprint backlog reports belong under `29_FOOTPRINT_GAP_ANALYSIS/`.
- Supplier-to-KiCad footprint match schemas, confidence rules, supplier SKU/MPN match records, and unmatched supplier-footprint reports belong under `30_SUPPLIER_FOOTPRINT_MATCHES/`.
- Playwright-assisted public-page research policies, source profiles, screenshot evidence rules, controlled target lists, dry-run browser research scripts, and normalized evidence templates belong under `31_PLAYWRIGHT_RESEARCH_PIPELINE/`.
- Open KiCad sample project intake records, license screening, imported-original evidence copies, normalized sample copies, review reports, attribution records, and benchmark-candidate promotion notes belong under `32_OPEN_KICAD_SAMPLE_INTAKE/`.
- KiCad GUI automation policies, native schematic action workflows, Windows Eeschema detection scripts, screenshot helpers, and safety-gated GUI action wrappers belong under `33_KICAD_GUI_AUTOMATION/`.
- PCB layout sandbox rules, variant planning, board-shape reasoning, projected routing studies, and pre-PCB-edit layout templates belong under `34_PCB_LAYOUT_SANDBOX/`.
- Backups before automated edits belong under `99_BACKUPS/pre_codex_edits/`.
- MCP permission changes require explicit approval. The existing project-scoped `kicad-mcp-pro` configuration is analysis/safe mode only.

## KiCad Engine Control Planes

Codex must choose the safest control plane that can complete the task.

### 1. Common / Project Intelligence
Use first whenever possible:
- `kicad-cli`
- KiBot
- `pcbnew` Python
- MCP analysis tools
- File validators
- BOM, Gerber, and pick-and-place parsers

### 2. Windows GUI Hands/Eyes
Use only when common tools are insufficient:
- pywinauto
- FlaUI
- AutoHotkey
- PyAutoGUI
- Screenshot tools
- SikuliX

Rules:
- Start with discovery only.
- No coordinate clicks without screenshots and window-size verification.
- No random typing.
- No production project GUI automation until the project is identified and backed up.
- Record screenshots and logs.

### 3. Linux / Headless / CI
Use for repeatable validation:
- Linux `kicad-cli`
- KiBot
- Xvfb
- xdotool
- wmctrl
- dogtail
- Docker

Rules:
- Run headless checks first.
- Do not write to production projects unless working on an approved copied project.
- Scripts must be repeatable and logged.

## Tool Selection Rule
- Prefer CLI/API/MCP over GUI automation.
- Prefer read-only inspection before edits.
- Prefer copied project workspaces over original projects.
- Prefer `NOT_FINAL` outputs until the verification gate passes.
- For full project progression from schematic checks through NOT_FINAL fabrication export, use `.prompts/kicad_pipeline/`, `00_CODEX_START/KICAD_PIPELINE_STARTUP_RULES.md`, `09_ACCURACY_ENGINE/workflows/FULL_KICAD_PROJECT_PIPELINE.md`, and `09_ACCURACY_ENGINE/checklists/FULL_PIPELINE_GATE_CHECKLIST.md`.
- For every PCB pipeline phase, apply `00_CODEX_START/KICAD_PHASE_ORDER.md`, `09_ACCURACY_ENGINE/workflows/MANDATORY_KICAD_PHASE_GATE.md`, `09_ACCURACY_ENGINE/verification_rules/NO_PHASE_SKIPPING_RULES.md`, and `09_ACCURACY_ENGINE/checklists/PCB_PHASE_GATE_CHECKLIST.md`. When possible, run `python 03_TOOLS/scripts/project_gate/check_phase_allowed.py --project <ACTIVE_PROJECT_PATH> --phase <PHASE>` before starting the phase. The phase checker must build or read `reports/LIVE_PROJECT_STATE.json`, detect stale operational reports, and ignore stale `NO_PCB` or `0 footprints` claims when live KiCad files prove otherwise.
- For every meaningful repo task on an active project, apply `00_CODEX_START/PROMPT_COUNTER_RULES.md`. Increment the project `memory/PROMPT_COUNTER.md`; after 5 meaningful repo tasks, block new engineering work until `python 03_TOOLS/scripts/maintenance/run_maintenance_cycle.py --project <ACTIVE_PROJECT_PATH>` runs and the counter is reset.
- For every meaningful repo task, declare exactly one task type using `03_TOOLS/scripts/execution_contract/README.md` and the task contract schema. Edit-required task types must prove engineering artifact change or fail explicitly.
- Before any PCB update from schematic, placement, routing, zone creation, or PCB manufacturing-style output, read `09_ACCURACY_ENGINE/workflows/SCHEMATIC_TO_PCB_GATE_WORKFLOW.md`, `09_ACCURACY_ENGINE/workflows/AUTO_PCB_START_WORKFLOW.md`, `09_ACCURACY_ENGINE/checklists/SCHEMATIC_READY_FOR_PCB_CHECKLIST.md`, `09_ACCURACY_ENGINE/checklists/PCB_UPDATE_FROM_SCHEMATIC_CHECKLIST.md`, `09_ACCURACY_ENGINE/checklists/AUTO_PCB_START_CHECKLIST.md`, `09_ACCURACY_ENGINE/verification_rules/SCHEMATIC_TO_PCB_BLOCKERS.md`, and the active project's `reports/SCHEMATIC_TO_PCB_GATE_STATUS.md` plus `reports/PCB_LAYOUT_SANDBOX_GATE_STATUS.md`.
- Before PCB placement on compact ESP32/STM32-style dev boards, read `09_ACCURACY_ENGINE/pcb_rules/PILL_STYLE_DEV_BOARD_LAYOUT_RULES.md`, `CONNECTOR_EDGE_ORIENTATION_RULES.md`, `TEST_PAD_PLACEMENT_RULES.md`, `ESP32_RF_KEEP_OUT_PLACEMENT_RULES.md`, `PCB_MECHANICAL_CLEARANCE_RULES.md`, and `09_ACCURACY_ENGINE/checklists/PILL_STYLE_PLACEMENT_CHECKLIST.md`. Placement is not ready if connector mouths face the wrong edge, test pads are mixed into component clusters, RF keepouts are blocked, four holes are used on a narrow board without proven clearance, any component/courtyard/text/pad overlap exists, or the board has unexplained dead area. Routing remains blocked until LJ visually approves placement.
- Before any real `.kicad_pcb` edit, read `34_PCB_LAYOUT_SANDBOX/README.md`, `PCB_LAYOUT_SANDBOX_RULES.md`, `PCB_VARIANT_WORKFLOW.md`, `CONNECTOR_ORIENTATION_RULES.md`, `RF_ANTENNA_KEEP_OUT_RULES.md`, `BOARD_SHAPE_AND_MECHANICAL_RULES.md`, `ROUTING_FEASIBILITY_RULES.md`, `AUTO_SANDBOX_APPROVAL_RULES.md`, and `AUTO_APPROVAL_STATUS_CODES.md`. Create or review at least three layout variants, one variant scorecard, one selected layout plan, and one auto-approval or auto-blocked report before real PCB update, placement, or routing work.
- Before treating a schematic as layout-ready, run or review current reports from `03_TOOLS/scripts/kicad_schematic_checks/check_schematic_annotation.py`, `check_schematic_completeness.py`, `check_bom_lock_alignment.py`, and `check_needs_review_markers.py`.
- Before treating close-up visual review as complete, run or review `03_TOOLS/kicad/run_schematic_visual_check.ps1` outputs, including `_verification/schematic_visual/crops` and `reports/CLOSE_UP_REVIEW.md`. Automated crop `PASS` is not `VISUAL_PASS`; agents must also inspect rendered PNG/crop evidence against `09_ACCURACY_ENGINE/verification_rules/HUMAN_READABLE_SCHEMATIC_RULES.md`, `VISUAL_PASS_IS_NOT_AUTOMATED_PASS.md`, and `09_ACCURACY_ENGINE/checklists/SCHEMATIC_HUMAN_READABILITY_CHECKLIST.md`.
- Read relevant `09_ACCURACY_ENGINE/` rules before creating schematics, selecting symbols, selecting footprints, creating PCBs, or preparing release packages.
- Read relevant `26_AGENT_QUALITY/` quality-gate rules before making engineering claims about components, datasheets, symbols, footprints, schematics, PCBs, BOMs, or fab outputs.
- Read relevant `10_KNOWLEDGE_BASE/` files before proposing reusable circuit blocks, PCB layout patterns, connector interfaces, power trees, or manufacturing packages.
- Read relevant `11_LIBRARY_FACTORY/` standards before creating, selecting, verifying, or mapping KiCad symbols, footprints, packages, 3D models, or project-local libraries.
- Read relevant `12_REFERENCE_DESIGN_LIBRARY/` records and public-source rules before using a reference design as evidence or adapting a reference pattern.
- Read `13_PART_INGESTION/` before adding a new part from a datasheet, source URL, or user-provided local document.
- Read `14_LAYOUT_AUTOMATION/` before suggesting placement automation, routing automation, FreeRouting integration, constraint extraction, or layout review workflows.
- Read `15_BENCHMARKS/` before running, scoring, or comparing KiCad Engine benchmark tasks.
- Read `28_SUPPLIER_INGESTION/SOURCE_POLICY.md`, `API_KEY_HANDLING.md`, and `SUPPLIER_CONNECTOR_STANDARD.md` before importing supplier, distributor, stock, pricing, SKU, lifecycle, or source-link data.
- Read `29_FOOTPRINT_GAP_ANALYSIS/README.md` and `INDEX.md` before using installed KiCad footprint candidates, footprint gap reports, or missing-footprint backlog outputs.
- Read `30_SUPPLIER_FOOTPRINT_MATCHES/README.md`, `MATCH_SCHEMA.md`, `MATCH_CONFIDENCE_RULES.md`, and `HUMAN_REVIEW_REQUIRED_RULES.md` before linking supplier SKUs or MPNs to KiCad footprint candidates.
- Read `31_PLAYWRIGHT_RESEARCH_PIPELINE/SOURCE_POLICY.md`, `TERMS_AND_RATE_LIMIT_RULES.md`, `PLAYWRIGHT_USAGE_RULES.md`, and the relevant `source_profiles/*.profile.md` before using browser-assisted supplier, datasheet, vendor, part-number, or footprint research.
- Read `32_OPEN_KICAD_SAMPLE_INTAKE/README.md`, `SOURCE_SELECTION_RULES.md`, `LICENSE_SCREENING_RULES.md`, `SAMPLE_IMPORT_WORKFLOW.md`, `SAMPLE_REVIEW_WORKFLOW.md`, and `SAMPLE_PROMOTION_RULES.md` before finding, importing, copying, reviewing, or promoting open KiCad sample projects.
- Read `33_KICAD_GUI_AUTOMATION/README.md`, `KICAD_GUI_AUTOMATION_RULES.md`, `KICAD_WINDOW_STATE_RULES.md`, `KICAD_NATIVE_ANNOTATION_WORKFLOW.md`, and `KICAD_GUI_SAFETY_GATES.md` before using GUI automation, native KiCad annotation, GUI save, GUI ERC, or screenshots as evidence.
- Read `03_TOOLS/kicad/KICAD_NATIVE_ACTIONS_NOT_SUPPORTED_BY_CLI.md` before using raw file edits for annotation, GUI-visible ERC state, screenshot evidence, or other native KiCad actions.
- Read `00_CODEX_START/STRUCTURE_STANDARD.md`, `00_CODEX_START/FOLDER_ROUTING_RULES.md`, and `00_CODEX_START/REPO_STRUCTURE_INDEX.md` before creating, moving, or reorganizing top-level repo files.
- Read `00_CODEX_START/CONTROL_PLANES.md` before choosing Windows GUI control or Linux/headless workflows.

## Hard Restrictions
- Do not install tools.
- Do not clone repositories.
- Do not configure MCP servers yet.
- Do not modify KiCad files unless the active project is identified in `00_CODEX_START/CURRENT_PROJECT.md`.
- Do not edit `.kicad_sch`, `.kicad_pcb`, `.kicad_pro`, symbol libraries, footprint libraries, or manufacturing output files unless the active project is identified.
- Do not edit a real `.kicad_pcb` until the active project has a PCB Layout Sandbox report set with at least three variants, a variant scorecard, a selected layout plan, connector-orientation planning, antenna-keepout planning, board-shape/dimension planning, routing-feasibility evidence, and an auto-approval result of `AUTO_APPROVED_FOR_PCB_WORK` recorded in `reports/PCB_LAYOUT_SANDBOX_GATE_STATUS.md`.
- Do not update PCB from schematic, create or update `.kicad_pcb`, apply board outline, place fixed mechanical components, place main component groups, route traces, create zones, or generate PCB manufacturing outputs unless the active project's `reports/SCHEMATIC_TO_PCB_GATE_STATUS.md` exists and its gate result is exactly `PASS`, `reports/PCB_LAYOUT_SANDBOX_GATE_STATUS.md` exists and its gate result is exactly `PASS`, and the `AUTO_PCB_START_WORKFLOW.md` preconditions are satisfied.
- Do not skip KiCad PCB phases. Missing `.kicad_pcb` blocks every phase after PCB creation/update from schematic. Missing `reports/PCB_SYNC_STATUS.md` blocks placement, routing, JLCPCB review, production review, export, upload feedback, and signoff. Missing DRC or no-unrouted-net evidence blocks JLCPCB review, production review, export, upload feedback, and signoff.
- If a user asks for a later phase too early, stop and identify the missing earlier phase and evidence. Do not create downstream blocked review reports unless the user specifically asks for a blocker audit. Redirect to the next required phase.
- Do not treat documentation/report creation as actual engineering progress. Each phase requires the actual design artifact and evidence files listed in `09_ACCURACY_ENGINE/workflows/MANDATORY_KICAD_PHASE_GATE.md`.
- Do not mark `PLACEMENT_EDIT_REQUIRED`, `ROUTING_EDIT_REQUIRED`, or `PCB_EDIT_REQUIRED` tasks complete when only Markdown, reports, or other non-design artifacts changed. If required engineering artifact proof is missing, the final status must be `EDIT_REQUIRED_FAILED_NO_ENGINEERING_ARTIFACT_CHANGE`.
- Do not start new engineering work when the active project's prompt counter says maintenance is due. Run memory/history maintenance first, then reset the counter.
- Do not skip the full KiCad pipeline gates unless the user explicitly approves an exception. Log every exception with affected gate, reason, risk, evidence path, and `HUMAN_REVIEW_REQUIRED`.
- Do not create schematic or PCB content from memory alone; every component, symbol, pinout, footprint, connector, circuit-pattern, library-mapping, reference-design, part-ingestion, and manufacturing-output claim must follow the relevant `09_ACCURACY_ENGINE/` evidence rules, `10_KNOWLEDGE_BASE/` source/checklist guidance, `11_LIBRARY_FACTORY/` library standards, `12_REFERENCE_DESIGN_LIBRARY/` license/source rules, and `13_PART_INGESTION/` uncertainty rules.
- Do not copy proprietary reference designs without permission. Reference designs are evidence, not automatic approval.
- Do not redistribute user-provided or copyrighted datasheets unless redistribution rights are confirmed. Part ingestion may be link-only.
- Do not claim complete AI auto-layout or autorouting unless it has actually been implemented, run on a copied/approved project, DRC-checked, and human-reviewed.
- Do not create fake benchmark results, backfill scores from memory, or claim KiCad Engine beats another PCB AI tool without a documented benchmark run using the same task, constraints, scoring method, and review evidence.
- Do not blindly scrape supplier websites, bypass anti-automation protections, hardcode supplier API credentials, or treat supplier package text as footprint verification.
- Do not use Playwright to bypass login, paywalls, CAPTCHA, anti-bot protections, site terms, supplier API requirements, or access controls. Playwright research output is evidence, not truth, and remains `UNVERIFIED` until official-source or human review.
- Do not download, clone, import, bundle, or promote open KiCad sample projects unless the source URL, attribution, license status, and public-bundle eligibility are recorded under `32_OPEN_KICAD_SAMPLE_INTAKE/`.
- Do not edit `32_OPEN_KICAD_SAMPLE_INTAKE/imported_originals/` directly. Create a normalized copy under `32_OPEN_KICAD_SAMPLE_INTAKE/normalized_samples/` before analysis, repair, benchmark use, or generated review outputs.
- Do not treat raw `.kicad_sch` text edits as proof of schematic annotation. For annotation tasks, use verified KiCad-native annotation through the GUI automation gate or stop and instruct LJ to run KiCad `Tools -> Annotate Schematic -> Re-annotate all symbols -> Save -> Run ERC` manually.
- Do not save, annotate, run GUI ERC, or otherwise control KiCad GUI when the Eeschema title begins with `*` unless LJ explicitly decides the unsaved GUI state should be kept, a backup exists, screenshots are captured, and the GUI path exactly matches the active project schematic.
- Do not store passwords, API keys, license keys, private tokens, or credentials in memory or history.

## Required Before KiCad Edits
Before editing KiCad project files, Codex must:
- Confirm the active project name and active project path.
- Confirm that the target files are inside the active project folder.
- Create or confirm a backup in `99_BACKUPS/pre_codex_edits/`.
- State the active project, path, files likely to change, verification plan, and rollback plan.
- Check relevant memory and history for prior constraints, decisions, review notes, and open issues.
- For `.kicad_pcb` edits, confirm the active project has sandbox variant evidence, a variant scorecard, a selected layout plan, board dimensions, connector-orientation evidence, antenna-keepout evidence when required, routing-feasibility evidence, and an auto-approval result of `AUTO_APPROVED_FOR_PCB_WORK` in `reports/PCB_LAYOUT_SANDBOX_GATE_STATUS.md` before touching the board file.

## Verification Requirements
- After schematic changes, run ERC or explain why ERC could not be run.
- After PCB changes, run DRC or explain why DRC could not be run.
- For task types `PLACEMENT_EDIT_REQUIRED`, `ROUTING_EDIT_REQUIRED`, and `PCB_EDIT_REQUIRED`, record task-contract evidence before closeout. At minimum record the task type, backup evidence, `.kicad_pcb` hash before/after, DRC evidence, and visual-export attempt. Routing edits also require unrouted/unconnected before/after counts plus trace-change-log evidence. Placement edits also require placement-report evidence. `PCB_EDIT_REQUIRED` may use `NO_DESIGN_CHANGE_NEEDED` only when the contract explicitly records that outcome.
- Treat PCB layout as not professional until sandbox variant planning, objective sandbox auto-approval, placement review, routing feasibility, DRC, and visual review all pass.
- Treat manufacturing output as not final until ERC, DRC, BOM, footprint, netlist, datasheet, and visual review are complete.
- Treat generated manufacturing-style outputs as `NOT_FINAL` until the full verification gate passes.
- Treat the 17-stage pipeline in `09_ACCURACY_ENGINE/workflows/FULL_KICAD_PROJECT_PIPELINE.md` as mandatory for future KiCad projects unless the user approves a logged exception.
- Treat schematic-to-PCB transition as blocked until annotation, ERC, full-page visual export, close-up visual review, electrical audit, BOM lock audit, footprint/package drawing audit, connector orientation review, polarity review, and all high-risk `NEEDS_REVIEW` checks pass in the active project's `SCHEMATIC_TO_PCB_GATE_STATUS.md`.
- Treat real PCB update from schematic and PCB placement as additionally blocked until the active project's `reports/PCB_LAYOUT_SANDBOX_GATE_STATUS.md` is exactly `PASS`, which requires at least three variants, a scorecard, a selected layout plan, connector-orientation planning, antenna-keepout planning, board-shape/dimension planning, routing-feasibility evidence, and sandbox auto-approval status `AUTO_APPROVED_FOR_PCB_WORK`.
- Treat `AUTO_APPROVED_FOR_PCB_WORK` as permission to enter only `AUTO_PCB_START_WORKFLOW.md`: PCB sync, board outline, fixed-mechanical placement, main-group placement, DRC, and placement-visual evidence. It is not permission for final routing, fab export, or fabrication-ready claims.
- Treat schematic annotation and completeness as explicit evidence gates: unresolved placeholder references, duplicate references, missing reference fields, blank values, missing expected BOM-lock items, missing required functional blocks, unassigned physical footprints, and high-risk parts without verification status block PCB update.
- Treat KiCad GUI annotation as a separate native-state gate when LJ reports GUI-visible question-mark references. Saved-file parsing, regex scans, or CLI ERC do not override what the open KiCad GUI shows when its state is unsaved or disputed.
- Treat the authoritative annotation gate as passed only when all annotation evidence exists: KiCad native `Annotate Schematic` applied through verified GUI automation or LJ-confirmed manual action, schematic saved from KiCad GUI, GUI ERC shows 0 violations when safely automatable, `kicad-cli` ERC passes after GUI save, saved schematic scan shows 0 unresolved `?` references, and duplicate-reference checks pass. The successful `ESP32_CSI_WIFI_NODE` run on 2026-05-06 is the model record: `33_KICAD_GUI_AUTOMATION/KICAD_NATIVE_ANNOTATION_SUCCESS_RECORD.md`.
- If Eeschema is not open for an annotation task, future automation may safely open the target `.kicad_pro` only after project identity, backup, screenshot/logging, and exact-path gates are satisfied; if Eeschema is open with a different project, stop.
- Treat close-up visual review as incomplete when full-page exports, configured block crops, or `CLOSE_UP_REVIEW.md` are missing, or when visible unannotated references or visible footprint/library/path fields remain unresolved.
- Treat schematic human readability as a separate mandatory gate. ERC pass, annotation pass, footprint population, automated crop generation, hidden footprint fields, and no `?` token detection do not prove `VISUAL_PASS`.
- Treat any visible text/value/reference/net-label overlap, notes inside active circuitry, long unreadable values, stacked power symbols, or labels touching wires/pins/symbol bodies in rendered full-page/crop evidence as `VISUAL_FAIL`.
- If rendered PNG/crop evidence cannot be visually inspected, classify visual status as `VISUAL_NOT_VERIFIED`, not `PASS`.
- Do not mark a schematic `READY_FOR_LJ_VISUAL_REVIEW` if any crop visibly contains overlapping text, values, references, net labels, wires, pins, symbols, or review notes inside active circuitry.
- Treat component source, datasheet revision, symbol pinout, footprint package drawing, connector orientation, polarity, RF, USB, CAN, power-layout, circuit-pattern, library-mapping, reference-design source/license, part-ingestion verification status, layout-automation reality checks, benchmark scoring evidence, and manufacturing-package review gates as required evidence under `09_ACCURACY_ENGINE/`, `10_KNOWLEDGE_BASE/`, `11_LIBRARY_FACTORY/`, `12_REFERENCE_DESIGN_LIBRARY/`, `13_PART_INGESTION/`, `14_LAYOUT_AUTOMATION/`, and `15_BENCHMARKS/`.
- Treat supplier stock, price, lifecycle, supplier SKU, and availability as time-sensitive metadata that requires source URL or source file, source date, verification status, and human review before purchasing or BOM-lock decisions.
- Score response truthfulness and quality using `00_CODEX_START/AI_TRUTHFULNESS_SCORING.md`, `AI_RESPONSE_QUALITY_GATE.md`, and `AI_CLOSEOUT_SCORECARD_RULES.md`.
- For every meaningful session that makes engineering claims, create an AI self-review, AI response scorecard, claim/evidence matrix, and uncertainty log before closeout.
- Mark work `BLOCKED_UNTIL_HUMAN_REVIEW` when required by the AI quality gate.
- Separate review findings from direct edits unless the user explicitly asks for fixes.

## Memory And History Rules
- Durable design decisions go in `01_MEMORY/`, not command logs.
- Commands, command results, failed attempts, and verification outputs go in `02_HISTORY/`.
- Global reusable lessons, common AI mistakes, verified workflows, failed workflows, and user corrections that apply across projects belong in `01_MEMORY/`.
- Global evidence records belong in `02_HISTORY/failed_attempts/`, `02_HISTORY/issue_logs/`, `02_HISTORY/user_corrections/`, `02_HISTORY/lessons_learned/`, `02_HISTORY/known_agent_mistakes/`, and `02_HISTORY/workflow_runs/`.
- Project-specific durable decisions belong in the active project's `memory/` folder and may be mirrored in `01_MEMORY/projects/PROJECT_NAME/PROJECT_MEMORY.md` when needed for legacy startup context.
- Project-specific history belongs in the active project's `history/` folder and may be summarized in `02_HISTORY/project_history/PROJECT_NAME/` when needed for legacy startup context.
- At the end of every meaningful AI session, write a session log, write command logs if commands were run, record failed attempts, record user corrections, add unresolved issues, update only durable memory, update memory/history indexes, and update `FOR CHAT GPT.MD` if repo structure or workflow changed.
- Meaningful repo tasks must increment the active project's prompt counter. The counter is only a maintenance trigger and does not replace session logs or command logs.
- Mark entries `UNVERIFIED` unless human-confirmed or verified by repeatable workflow evidence.

## AI Quality Gate Closeout
At the end of every meaningful session, the agent must:
1. Create a session log.
2. Create command logs if commands were run.
3. Create failed-attempt logs if anything failed.
4. Create user-correction logs if the user says something was wrong or did not work.
5. Create an AI self-review.
6. Create an AI response scorecard.
7. Create a claim/evidence matrix for major engineering claims.
8. Create an uncertainty log for anything not verified.
9. Create hallucination-risk log if any claim was guessed, inferred, or weakly sourced.
10. Create/update open issues for unresolved risks.
11. Update project memory with durable project-specific lessons.
12. Update global memory with reusable lessons.
13. Rebuild memory/history/AI-quality indexes.
14. Rebuild `CURRENT_KNOWN_PROBLEMS.md`.
15. Update `FOR CHAT GPT.MD` if repo structure, workflow, tool status, active project status, known blockers, or scoring rules changed.

## Primary Directive
Assist with KiCad design, review, verification, documentation, and release preparation while preserving project files unless the user explicitly asks for edits and the startup gates above are satisfied.
