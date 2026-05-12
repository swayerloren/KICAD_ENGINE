# KiCad Engine â€” ChatGPT / Codex Context README

This file is the high-level context handoff for ChatGPT, Codex, and future AI agents working in the current local `KICAD_ENGINE` checkout. It explains the workspace layout, safety gates, toolchain state, and expected workflow so an agent can operate without guessing.

Historical records may still mention an older non-GitHub checkout path. Treat older absolute paths as historical unless a current file explicitly proves the path exists and the user selects it. For new work, prefer repo-relative paths or the current checkout path above.

Latest knowledge_scrape emptying completion, 2026-05-12:
The `knowledge_scrape/` source folder has now been backed up under
`99_BACKUPS/knowledge_scrape_pre_empty/` and removed from the live repo tree
after final validation classified `READY_TO_EMPTY_KNOWLEDGE_SCRAPE`. The final
`7` legacy PowerShell scrape scripts had already been moved to
`02_HISTORY/knowledge_scrape_migration/obsolete_scripts/` as provenance-only
records, all `2546` ledger rows are `MOVED_VALIDATED`, and normal agent
routing and active tooling must not depend on `knowledge_scrape/` anymore.

Latest canonical knowledge-routing cleanup, 2026-05-11:
Normal agent startup now begins with `START_HERE_FOR_AI_AGENTS.md`,
`00_CODEX_START/TASK_ROUTER.md`, and the
`00_CODEX_START/TASK_TYPE_TO_{KNOWLEDGE,TOOL,RULE}_MAP.md` files, mirrored
under `10_KNOWLEDGE_BASE/retrieval_indexes/`. Canonical knowledge surfaces now
live under `10_KNOWLEDGE_BASE/`, `09_ACCURACY_ENGINE/`, `06_DATASHEETS/`,
`08_COMPONENT_DATABASE/`, `24_FAB_PROFILES/`, `26_AGENT_QUALITY/`, and the
relevant `03_TOOLS/` subtrees such as `03_TOOLS/calculators/` and
`03_TOOLS/scripts/kicad_api/`. Migration provenance, quarantine records, and
release-readiness ledgers remain valid historical evidence under `02_HISTORY/`,
`05_OUTPUTS/release_readiness/`, and `21_LICENSE_ATTRIBUTION/`, but they are
not part of normal agent routing.

Latest reference sample learning system, 2026-05-10:
`32_OPEN_KICAD_SAMPLE_INTAKE` and `07_REFERENCE_DESIGNS` now form the
authoritative open-source sample learning layer. New intake docs cover sample
workflow, license handling, normalization, quality scoring, and anti-copy
rules. New read-only scripts live under `03_TOOLS/scripts/sample_intake/` for
candidate registration, license audit, normalization planning, schematic metric
extraction, PCB metric extraction, and reference-style index building. Future
Codex/Claude sessions may compare generated schematics and PCB layouts against
reviewed human-made examples, but samples remain comparison evidence only and
must not override project-local gates, datasheet proof, connector truth, or
DRC/ERC evidence. Public payloads stay link-first and exclude imported or
normalized sample source unless license review explicitly allows bundling.

Latest footprint/package assignment engine, 2026-05-10:
`35_FOOTPRINT_PACKAGE_ENGINE` is now the authoritative footprint proof layer
before schematic-to-PCB progression. It adds workflow docs, evidence rules,
high-risk footprint rules, lock-file rules, package-drawing proof rules, and
schemas. The paired read-only scripts live under
`03_TOOLS/scripts/footprint_package/` and audit blank footprints,
`FOOTPRINT_LOCK.csv` completeness, source/package evidence, PMOS pin mapping,
connector orientation proof, and high-risk review state. The active-project
support templates now live under `04_KICAD_PROJECTS/_templates/` for
lock/checklist/report starters. Do not treat a footprint field alone as proof;
the canonical dry-run gate is:
`python 03_TOOLS/scripts/footprint_package/run_footprint_package_gate.py --project <ACTIVE_PROJECT_PATH> --no-fail`.

Latest source-backed footprint-lock follow-up, 2026-05-10:
`ESP32_CSI_WIFI_NODE` now has a live `FOOTPRINT_LOCK.csv` covering all `43`
physical symbols. The saved schematic currently has `0` blank footprint
fields, so the current blocker is no longer missing footprint population.
The live footprint-package gate is now `NEEDS_HUMAN_REVIEW`, not `FAIL`,
because exact high-risk proof still remains open. The current exact blockers
are `U2` (`ESP32-S3-WROOM-1U` value still paired with saved footprint
`RF_Module:ESP32-S3-WROOM-1`) and `U3` (`TPD2EUSB30` currently saved as
`Package_TO_SOT_SMD:SOT-23-6` while official TI package evidence points to
`Texas_DRT-3`). Do not let older `0 footprints` or `lock missing` narratives
override this newer live-proof state.

Latest schematic layout engine, 2026-05-10:
`03_TOOLS/scripts/schematic_layout` now provides the dedicated schematic visual
cleanup and layout-planning layer on top of the schematic-quality gate. New
authoritative docs live in `34_SCHEMATIC_QUALITY_ENGINE/`:
`SCHEMATIC_LAYOUT_ALGORITHM.md`, `FUNCTIONAL_BLOCK_TEMPLATES.md`,
`LOCAL_WIRING_STYLE_GUIDE.md`, and `VISUAL_READABILITY_SCORECARD.md`. New
scripts extract functional-block geometry, audit visual flow, audit local wire
usage, score readability, generate block-layout plans, and emit safe
rewrite-plan packets without editing `.kicad_sch` by default. Canonical review
command:
`python 03_TOOLS/scripts/schematic_layout/render_schematic_review_pages.py --project <ACTIVE_PROJECT_PATH> --no-fail`.

Latest schematic quality engine, 2026-05-10: `34_SCHEMATIC_QUALITY_ENGINE`
now defines the mandatory schematic readability gate before PCB update. New
authoritative docs cover readable flow, functional-block grouping, wire-vs-label
rules, native annotation proof, footprint readiness, visual audit rules, and
schematic-to-PCB readiness. The paired read-only script layer under
`03_TOOLS/scripts/schematic_quality/` directly parses `.kicad_sch` files,
audits unresolved `?` references, duplicate refs, blank footprints, visible
review-marker values, estimated text overlaps, block layout, local label
overuse, fresh ERC proof, and current human-visual/native-annotation evidence.
ERC pass alone is now explicitly not enough for schematic readiness claims.

Latest native KiCad annotation auto-open hardening, 2026-05-10:
`33_KICAD_GUI_AUTOMATION` now has a stricter dry-run-first closed-state
recovery workflow. Authoritative docs are
`KICAD_NATIVE_ANNOTATION_WORKFLOW.md`,
`KICAD_AUTO_OPEN_PROJECT_WORKFLOW.md`,
`KICAD_ANNOTATION_DO_AND_DO_NOT.md`,
`KICAD_GUI_ACTION_MATRIX.md`, and `KICAD_GUI_SAFETY_GATES.md`. The upgraded
Windows wrappers now require `--live` for any live GUI action, plus
`--allow-annotation`, `--allow-save`, and `--allow-gui-erc` for the full
authoritative annotation workflow. The workflow now captures before/after
screenshots, creates a backup before live save, runs post-save `kicad-cli`
ERC, scans the saved schematic for unresolved `?` references and duplicate
references, and stops on wrong-project windows or unsaved `*` state unless
explicitly allowed.

Latest optional open-source tool integration layer, 2026-05-10:
`03_TOOLS/open_source_integrations` now defines the repo-approved way to
document and optionally use upstream KiCad-adjacent tools without bloating the
repo. It adds `README.md`, `TOOL_REGISTRY.md`, `INSTALL_POLICY.md`,
`PORTABLE_TOOL_POLICY.md`, `LICENSE_AND_ATTRIBUTION_RULES.md`,
`TOOLS_APPROVED_FOR_LOCAL_USE.md`, `TOOLS_NOT_BUNDLED_REASON.md`, per-tool
profiles, lightweight requirements files, and dry-run-first wrappers under
`setup/`. The default ZIP workflow must still work with no large downloads.
Optional tools install only into `.tools/` or user-local caches, missing tools
must fail gracefully, and upstream repos, `node_modules`, virtual environments,
and large binaries remain untracked by default.

Latest enforceable PCB quality gate, 2026-05-10: `03_TOOLS/scripts/pcb_quality`
is now the authoritative routed-board acceptance layer. It reuses the live DRC,
open-net, geometry, USB, orientation, and GND/zone truth engines and produces a
single judge result from `PASS_FINAL_ROUTING`, `FAIL_DRC`, `FAIL_OPEN_NETS`,
`FAIL_TRACE_GEOMETRY`, `FAIL_TESTPOINT_TOPOLOGY`, `FAIL_POWER_WIDTHS`,
`FAIL_USB_ROUTING`, `FAIL_CONNECTOR_ORIENTATION`, `FAIL_RF_KEEPOUT`,
`FAIL_ZONE_GND`, or `NEEDS_HUMAN_REVIEW`. The template constraints file lives
at `04_KICAD_PROJECTS/_templates/pcb_routing_constraints.template.yaml`, the
active project config example lives at
`04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/config/pcb_routing_constraints.yaml`,
and the canonical command is:
`python 03_TOOLS/scripts/pcb_quality/run_pcb_quality_gate.py --project <ACTIVE_PROJECT_PATH>`.

Latest startup router upgrade, 2026-05-10: future Codex/Claude sessions no
longer need the user to paste huge `READ FIRST` lists. `START_HERE_FOR_AI_AGENTS.md`
now points to `00_CODEX_START/TASK_ROUTER.md`,
`TASK_TYPE_TO_REQUIRED_DOCS.md`, `TASK_TYPE_TO_ALLOWED_ACTIONS.md`,
`TASK_TYPE_TO_BLOCKERS.md`, `TASK_TYPE_TO_OUTPUTS.md`,
`KICAD_ENGINE_CRITICAL_PATH.md`, and `AI_AGENT_FAST_CONTEXT.md`. Hard rule: if
the user asks for schematic, PCB, fab, GUI annotation, memory/history, or
open-source tool work and does not list read-first files, the agent must use
the router automatically. Explicit route coverage now includes schematic
creation/repair, schematic visual cleanup, native KiCad annotation,
footprint/package gate, PCB update from schematic, PCB prelayout variant
planning, PCB placement, connector orientation, PCB routing, trace-geometry
audit, copper zones, fabrication export, memory maintenance, and open-source
tool use. The router now uses `03_TOOLS/scripts/pcb_quality` as the primary
routed-board quality gate, while `03_TOOLS/scripts/pcb_geometry` remains the
lower-level geometry sub-audit layer.

Latest PCB trace-geometry audit layer, 2026-05-10: `03_TOOLS\scripts\pcb_geometry` now provides the read-only geometry acceptance gate for routed boards. New scripts: `extract_tracks.py`, `audit_trace_angles.py`, `audit_trace_quality.py`, `audit_power_loop_geometry.py`, `audit_usb_pair_geometry.py`, and `render_trace_quality_overlays.py`, plus `README.md`. This layer converts live board tracks into real path branches, then blocks routing-acceptable claims on right angles, acute jogs, zigzags, rectangular loops, excessive detour ratios above `2x`, long test-point stubs above `5 mm`, board-edge crossings, RF-keepout crossings, and return-path split risk. DRC pass remains necessary but is still not enough for routing-quality approval.

Latest mechanical-orientation truth layer, 2026-05-10: `08_COMPONENT_DATABASE\mechanical_orientation` is now the authoritative connector/mechanical direction layer for edge-facing connectors and RF modules. New files: `README.md`, `connector_orientation_truth.json`, `barrel_jack_orientation_rules.md`, `usb_c_orientation_rules.md`, `esp32_module_antenna_orientation_rules.md`, and `connector_orientation_examples.md`, plus read-only audit scripts under `03_TOOLS\scripts\mechanical_orientation\`. Future connector review must distinguish `port opening`, `pin side`, `body side`, board-edge direction, and antenna keepout direction; XY location and rotation alone are not proof. If the exact 3D model is missing or unresolved, the connector remains `NEEDS_HUMAN_REVIEW`, and routing must stay blocked. Current live dry-run on `ESP32_CSI_WIFI_NODE`: `J2` USB-C `PASS`, `U2` antenna `PASS`, `J1` barrel jack `NEEDS_HUMAN_REVIEW` because its 3D model reference does not currently resolve on this machine.

Latest PCB prelayout engine addition, 2026-05-10: `33_PCB_PRELAYOUT_ENGINE` is now the mandatory digital-twin / variant-planning layer before real PCB placement or routing. New authoritative files: `33_PCB_PRELAYOUT_ENGINE\README.md`, `PCB_PRELAYOUT_ENGINE_WORKFLOW.md`, `PCB_VARIANT_PLANNING_RULES.md`, `PCB_VARIANT_SCORING_RULES.md`, `PCB_DIGITAL_TWIN_SCHEMA.md`, `CONNECTOR_MECHANICAL_TRUTH_SCHEMA.md`, `TRACE_PROJECTION_RULES.md`, `PLACEMENT_TO_ROUTING_FEASIBILITY_GATE.md`, and `README_FOR_CODEX_AND_CLAUDE.md`, plus schemas under `33_PCB_PRELAYOUT_ENGINE\schemas\` and scripts under `03_TOOLS\scripts\pcb_prelayout\`. Real PCB placement is now additionally blocked until the active project's latest `reports\prelayout_engine\*\prelayout_gate_result.json` proves at least three generated variants, at least one passing variant, and `placement_gate_status = PASS`. Real PCB routing is additionally blocked until the same result records `routing_gate_status = PASS`. This layer does not replace `34_PCB_LAYOUT_SANDBOX`; it adds an earlier deterministic stop that blocks wrong-facing connectors, projected open nets, and live-board open-net continuation. Latest live project packet: `ESP32_CSI_WIFI_NODE\prelayout_variants\20260510_093811\` now contains three named variants (`Compact dev-board`, `Routing-first`, `Mechanical-safe`) with top/bottom previews, projected-route angle audits, and a comparator that breaks equal-score ties by fewer projected open nets; the current selected planning candidate is `VARIANT_B`, but real placement and routing remain blocked by `J1` orientation proof incompleteness plus live open-net evidence.


Latest historical-path portability clarification, 2026-05-09: many tracked reports, review packets, sample-intake artifacts, and generated evidence files still preserve original machine-local absolute paths. Those records remain valuable as evidence, but they are not current setup truth. Future startup and onboarding must use repo-relative paths, `docs/PATH_PORTABILITY.md`, `00_CODEX_START/PATH_PORTABILITY_RULES.md`, `python health_check.py --no-write`, and live KiCad discovery on the current machine.

Latest tool-index portability clarification, 2026-05-09: `00_CODEX_START\TOOL_INDEX.md` remains in place for internal/local inventory, but it is now explicitly labeled as machine-specific and must not be used as portable setup truth. Future startup and onboarding should treat root `TOOLS_INDEX.md`, `03_TOOLS\TOOLS_INDEX.md`, `EXTERNAL_DEPENDENCIES.md`, `LOCAL_SETUP_REQUIREMENTS.md`, `docs\HEALTH_CHECK.md`, and live results from `python health_check.py --no-write` as the portable tool source of truth.

Latest KiCad Python context portability fix, 2026-05-09: normal repo Python and KiCad's embedded Python must now be treated as separate runtime contexts. New scripts under `03_TOOLS\scripts\kicad_api\` report whether `pcbnew` is usable in the current interpreter or only through KiCad's bundled `python.exe`. `health_check.py` now keeps `pcbnew` non-blocking for general onboarding, exposes a direct-import warning when appropriate, and hard-fails `pcbnew` only when `--require-pcbnew` is explicitly requested. First-party board-aware scripts now route through the shared bridge instead of relying on raw top-level `import pcbnew`.

Latest KiCad library index portability cleanup, 2026-05-09: the generated payloads under `03_TOOLS\kicad_library_intelligence\GENERATED_INDEXES` are now placeholder-only in Git. The tracked JSON and Markdown inventories were removed from Git tracking because they capture machine-local KiCad install roots, library-table paths, and candidate outputs that are not portable repo truth. Keep only `GENERATED_INDEXES\README.md` tracked, regenerate the indexes locally on the current machine when needed, and do not treat old generated paths or counts as current library truth.

Latest routing_work portability cleanup, 2026-05-09: the large tracked scratch payload under `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\routing_work\20260508_091428` was removed from Git tracking so the portable repo no longer ships copied routing-trial boards and DRC scratch trees in the ZIP. `routing_work` is now placeholder-only in Git by policy: keep `routing_work\README.md` tracked, treat timestamped routing scratch folders as local generated workspace, and do not recommit copied `.kicad_pcb`, `.kicad_pro`, `.kicad_prl`, or DRC scratch payloads unless a small sanitized evidence subset is intentionally approved.

Latest PCB layout sandbox layer, 2026-05-07: `34_PCB_LAYOUT_SANDBOX` is now the mandatory pre-PCB-edit reasoning layer for real boards. Before editing a real `.kicad_pcb`, agents must generate or review at least three layout variants plus one selected-variant justification covering board shape, dimensions, fixed mechanical parts, connector orientation, antenna keepout, projected power/data paths, routing feasibility, and risk scoring. Real PCB update from schematic and placement are now blocked until a project-local `PCB_LAYOUT_SANDBOX_GATE_STATUS.md` exists and records sandbox auto-approval status `AUTO_APPROVED_FOR_PCB_WORK` with a matching evidence report. Generic LJ approval is no longer required when the objective sandbox checks pass. This layer exists to stop avoidable layout failures such as wrong-facing barrel jacks, USB-C not aligned to the board edge, blocked ESP32 antennas, outline choices without mechanical reasoning, and routing started after bad placement.

Latest auto PCB start workflow, 2026-05-07: KiCad Engine now has an explicit evidence-based handoff from sandbox approval into real PCB work. Authoritative files: `09_ACCURACY_ENGINE\workflows\AUTO_PCB_START_WORKFLOW.md`, `09_ACCURACY_ENGINE\checklists\AUTO_PCB_START_CHECKLIST.md`, `34_PCB_LAYOUT_SANDBOX\PCB_WORK_AUTO_START_RULES.md`, and `34_PCB_LAYOUT_SANDBOX\templates\AUTO_PCB_START_REPORT_TEMPLATE.md`. When `SCHEMATIC_TO_PCB_GATE_STATUS.md` is exactly `PASS`, the footprint/package gate is `PASS` or `SAFE_CANDIDATE_WITH_EVIDENCE`, the selected layout plan exists, sandbox auto-approval is `AUTO_APPROVED_FOR_PCB_WORK`, and board-dimension / connector / antenna / routing-feasibility evidence exists, Codex/Claude may automatically continue to PCB update from schematic, real `.kicad_pcb` creation/update, board outline, fixed mechanical placement, grouped placement, DRC, and placement visuals. If any precondition fails, the required status is `AUTO_PCB_START_BLOCKED` with exact blockers.

Latest auto placement engine, 2026-05-07: `14_LAYOUT_AUTOMATION` now includes the first deterministic PCB placement-planning engine. Authoritative files: `AUTO_PLACEMENT_ENGINE.md`, `PLACEMENT_CONSTRAINTS_SCHEMA.md`, `PLACEMENT_GROUPING_RULES.md`, `FIXED_MECHANICAL_PLACEMENT_RULES.md`, `POWER_PATH_PLACEMENT_RULES.md`, `USB_PLACEMENT_RULES.md`, `RF_ANTENNA_PLACEMENT_RULES.md`, `TEST_PAD_PLACEMENT_RULES.md`, `PLACEMENT_DRC_PRECHECK_RULES.md`, and `14_LAYOUT_AUTOMATION\scripts\`. This layer classifies components into placement stages, places fixed mechanical parts first, places power and USB groups in logical order, detects overlap and keepout failures, and scores placement plans before real KiCad placement work. It is a planning/precheck layer only and does not claim complete automatic placement or fabrication-ready placement quality.

Latest real-board routing bridge, 2026-05-07: `14_LAYOUT_AUTOMATION\scripts\` now includes a read-only KiCad PCB extraction bridge for copied-board routing audits. New authoritative files: `extract_kicad_pcb_to_routing_schema.py`, `extract_kicad_nets_pads.py`, `extract_kicad_tracks_vias.py`, `extract_kicad_zones_keepouts.py`, `extract_kicad_net_classes.py`, `run_real_board_routing_audit.py`, `real_board_tests\`, and `reports\REAL_KICAD_BOARD_EXTRACTION_TEST_REPORT.md`. The bridge re-enters KiCad's own Python when needed, reads `.kicad_pcb` files without modifying them, extracts board outline / footprints / pads / nets / tracks / vias / zones / keepouts / net classes into `ROUTING_INPUT_SCHEMA.md`, and couples that with `kicad-cli pcb drc --format json` for copied-board audit runs. Current status: copied-board live test is now possible; active-project routing is still blocked because per-net ratsnest extraction, richer keepout semantics, critical-loop recognition, via-intent extraction, and first active-project gate evidence are not complete.

Latest auto routing engine upgrade, 2026-05-07: `14_LAYOUT_AUTOMATION` routing now has a concrete fixture-driven schema and hard-fail scoring layer. New authoritative files: `ROUTING_INPUT_SCHEMA.md`, `ROUTING_OUTPUT_SCHEMA.md`, `TRACE_AUDIT_SCHEMA.md`, `NET_CLASS_SCHEMA.md`, `ROUTING_SCORECARD_RULES.md`, `test_fixtures\`, and `reports\ROUTING_ENGINE_FIXTURE_TEST_REPORT.md`. The scripts under `14_LAYOUT_AUTOMATION\scripts\` now parse schema-aware routing fixtures, emit both JSON and Markdown, identify critical/power/USB nets, detect RF and antenna keepout crossings, detect unrouted nets, perform per-trace audit, and score routing readiness with explicit hard-fail rules. Current fixture matrix: three good fixtures pass and the intentionally bad keepout case blocks. The engine is still not ready to touch a real KiCad board directly; it still lacks real-board planning maturity and active-project human review evidence.

Latest real-project routing gate definition, 2026-05-07: `14_LAYOUT_AUTOMATION` now also defines the exact evidence gate that must exist before the routing engine may touch a real KiCad PCB. Authoritative files: `REAL_PROJECT_ROUTING_PRECONDITIONS.md`, `REAL_PROJECT_ROUTING_WORKFLOW.md`, `REAL_PROJECT_TRACE_BY_TRACE_REVIEW.md`, and `REAL_PROJECT_ROUTING_STOP_CONDITIONS.md`. Real routing now requires exact upstream schematic and placement passes, a synced PCB, board outline, keepouts/zones, routing plan, critical-net list, net classes, and DRC precheck before the first trace edit. Routing must proceed in ordered passes and must stop immediately on RF/antenna keepout crossings, unrouted critical nets, missing GND strategy, unjustified critical-net vias, visually crude routing, or incomplete trace-by-trace review. This defines the go/no-go contract, but it does not make the engine ready for real-board routing by itself.

Latest PCB variant scoring system, 2026-05-07: `34_PCB_LAYOUT_SANDBOX` now includes a concrete variant scorer, comparator, auto-selector, and selected-variant auto-approval step. Authoritative files: `VARIANT_SCORING_RULES.md`, `templates\VARIANT_SCORECARD_TEMPLATE.md`, `scripts\score_layout_variant.py`, `scripts\compare_layout_variants.py`, `scripts\auto_select_best_variant.py`, and `scripts\auto_approve_selected_variant.py`. Variants are scored across mechanical correctness, connector orientation, RF keepout, power path, USB/data path, grouping quality, and routing feasibility, then penalized for DRC/precheck risk and human uncertainty risk. Per-variant statuses are now `PASS`, `FAIL`, `AUTO_BLOCKED_MISSING_DATA`, or `AUTO_BLOCKED_BAD_LAYOUT`. The selector must never choose a hard-failed variant even if it has the highest numeric score. The approval step then maps the selected candidate to `AUTO_APPROVED_FOR_PCB_WORK` or a specific `AUTO_BLOCKED_*` reason.

Latest FreeRouting feasibility integration, 2026-05-07: KiCad Engine now has an optional FreeRouting dry-run review layer for routing-feasibility scoring only. Authoritative files: `14_LAYOUT_AUTOMATION\FREEROUTING_FEASIBILITY_INTEGRATION.md`, `34_PCB_LAYOUT_SANDBOX\FREEROUTING_AS_VARIANT_SCORER.md`, and `03_TOOLS\scripts\routing_feasibility\`. This layer is for comparing unrouted nets, via pressure, congestion, and impossible placements across layout candidates. All outputs remain `REVIEW_ONLY`; USB, RF, switching-regulator, and high-current routes still require human engineering review.

Latest dev-board placement intelligence patch, 2026-05-07: KiCad Engine now has explicit placement-pattern guidance for ESP32-style boards, STM32-style dev boards, USB-C edge connectors, barrel-jack inputs, RF module antenna keepouts, buttons, LEDs, mounting holes, and test pads. New knowledge-base files: `10_KNOWLEDGE_BASE\design_patterns\ESP32_DEV_BOARD_LAYOUT_PATTERN.md`, `STM32_DEV_BOARD_LAYOUT_PATTERN.md`, `CONNECTOR_EDGE_PLACEMENT_PATTERN.md`, and `RF_MODULE_ANTENNA_KEEP_OUT_PATTERN.md`; new common-mistake files: `ESP32_LAYOUT_COMMON_MISTAKES.md`, `USB_C_CONNECTOR_LAYOUT_COMMON_MISTAKES.md`, and `BARREL_JACK_LAYOUT_COMMON_MISTAKES.md`; new sandbox rules: `34_PCB_LAYOUT_SANDBOX\ESP32_STYLE_BOARD_PLACEMENT_RULES.md` and `DEV_BOARD_SHAPE_REASONING_RULES.md`. These are patterns, not universal rules. Project requirements still come first.

Latest core placeholder upgrade note, 2026-05-03: the core systems named by the production-quality audit were upgraded with more actionable schemas, workflow gates, and AI-agent usage rules. See `02_HISTORY\design_reviews\CORE_PLACEHOLDER_CONTENT_UPGRADE_AUDIT.md` and `05_OUTPUTS\release_readiness\CORE_PLACEHOLDER_CONTENT_UPGRADE_SUMMARY.md`. Generated dry-run research and footprint records remain `UNVERIFIED` by design and must not be treated as verified data.

Latest open KiCad sample intake note, 2026-05-03: `32_OPEN_KICAD_SAMPLE_INTAKE` is now the required intake path for discovering, license-screening, importing, normalizing, reviewing, and promoting open KiCad sample projects. Scripts default to dry-run, imported originals are read-only evidence copies, normalized samples are required before analysis or repair, and no sample may enter a public payload unless license status is `PUBLIC_BUNDLE_ALLOWED`.

Latest project gate runner note, 2026-05-06: `03_TOOLS\scripts\project_gate` now contains the read-only one-command gate runner. Use `.\03_TOOLS\scripts\project_gate\run_project_gate.ps1 -ProjectPath "19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board"` from the repo root. Output is written to `05_OUTPUTS\gate_runs\<timestamp>\PROJECT_GATE_REPORT.md` and `.json`. The runner aggregates existing evidence only; it does not edit KiCad files, run ERC/DRC, or generate fabrication outputs. The current ATtiny85 fixture correctly classifies as `BLOCKED_UNTIL_HUMAN_REVIEW`.

Latest sample-project public docs note, 2026-05-06: polished user docs were added for the controlled sample area and gate runner. Start with `19_TEST_PROJECTS\README.md`, `19_TEST_PROJECTS\SAMPLE_PROJECTS_INDEX.md`, `19_TEST_PROJECTS\HOW_TO_RUN_SAMPLE_PROJECTS.md`, `19_TEST_PROJECTS\HOW_TO_INTERPRET_GATE_RESULTS.md`, `18_PUBLIC_DOCS\HOW_TO_RUN_GOLDEN_PATH_DEMO.md`, and `18_PUBLIC_DOCS\HOW_TO_VERIFY_PROJECT.md`. The docs must continue to state that the ATtiny85 fixture is useful as a blocked-gate demo, not a clean passing design or manufacturing-ready example.

Latest schematic visual gate root-cause audit, 2026-05-06: `02_HISTORY\design_reviews\KICAD_ENGINE_SCHEMATIC_FAILURE_ROOT_CAUSE_AUDIT.md` confirms the ESP32_CSI_WIFI_NODE visual failure was an evidence/status mismatch. The crop generator and prompt pack allowed automated evidence generation to be over-read as visual readiness. `03_TOOLS\scripts\visual\generate_schematic_closeups.py` now uses `AUTOMATED_CROP_PASS_ONLY` for automated-only success, and `.prompts\kicad_pipeline\02_schematic_visual_closeup_audit.md`, `03_schematic_visual_repair.md`, and `06_schematic_to_pcb_gate.md` now require rendered-image inspection before any `VISUAL_PASS` or gate-pass claim. Do not treat older `Close-up visual review status: PASS` records as human-readable approval unless they include block-by-block rendered-image inspection.

Latest KiCad GUI automation layer, 2026-05-06: `33_KICAD_GUI_AUTOMATION` now defines the opt-in safety-gated layer for Eeschema detection, unsaved GUI state detection, exact open schematic path checks, screenshots, and native KiCad workflow wrappers. This was added after the ESP32_CSI_WIFI_NODE annotation mismatch proved saved-file/CLI checks are not enough when the live GUI has unsaved state. Native GUI annotation has now been verified once on `ESP32_CSI_WIFI_NODE`: Codex opened KiCad's native `Annotate Schematic` dialog, applied annotation, saved the schematic from KiCad GUI, ran GUI ERC with `Violations (0)`, ran `kicad-cli` ERC with 0 errors and 0 warnings, and produced a saved schematic reference table with 0 unresolved `?` references and 0 duplicates. Evidence: `33_KICAD_GUI_AUTOMATION\KICAD_NATIVE_ANNOTATION_SUCCESS_RECORD.md`. For future annotation tasks, agents must use this native GUI workflow when available or stop and instruct LJ to run `Tools -> Annotate Schematic -> Re-annotate all symbols -> Save -> Run ERC`. Raw `.kicad_sch` text edits are not annotation proof. Passing annotation only permits separate visual cleanup; PCB update remains blocked until the full schematic-to-PCB gate is exactly `PASS`.

Latest KiCad auto-open workflow, 2026-05-06: `33_KICAD_GUI_AUTOMATION` now includes dry-run-first scripts to recover from `NO_EESCHEMA_WINDOW` by launching the exact target `.kicad_pro`, opening or focusing the schematic editor, confirming the exact `.kicad_sch`, and then handing off to native annotation/save/ERC gates. New workflow doc: `33_KICAD_GUI_AUTOMATION\KICAD_AUTO_OPEN_PROJECT_WORKFLOW.md`. New scripts: `open_kicad_project.py/.ps1`, `open_schematic_editor_gui.py`, `ensure_eeschema_open.py`, and `run_native_annotation_workflow.py`. Live open requires `--live`; live annotation requires `--allow-annotation`; save requires `--allow-save`. This setup was syntax-checked and dry-run-tested only; live closed-state launch still needs a future explicit test. It must stop if Eeschema is open for a different project or has unsaved `*` state.

Latest live-state phase gate repair, 2026-05-07: `03_TOOLS\scripts\project_gate\check_phase_allowed.py` now rebuilds or reads `reports\LIVE_PROJECT_STATE.json`, audits stale operational reports, and prints whether each blocker came from `LIVE_FILE_EVIDENCE`, `FRESH_GATE_REPORT`, `STALE_REPORT_IGNORED`, or `HUMAN_REVIEW_REQUIRED`. This prevents stale `NO_PCB`, `0 footprints`, or missing-phase markdown from overriding real KiCad file evidence. Later phases still block when live DRC, unrouted nets, zones/GND strategy, or fresh trace-audit evidence say the board is not ready.

Latest pill-style placement rule patch, 2026-05-07: `09_ACCURACY_ENGINE\pcb_rules` now includes strict compact dev-board placement rules after `ESP32_CSI_WIFI_NODE` exposed a second-order failure mode: a smaller pill-style layout can still be mechanically bad. New files: `PILL_STYLE_DEV_BOARD_LAYOUT_RULES.md`, `CONNECTOR_EDGE_ORIENTATION_RULES.md`, `TEST_PAD_PLACEMENT_RULES.md`, `ESP32_RF_KEEP_OUT_PLACEMENT_RULES.md`, `PCB_MECHANICAL_CLEARANCE_RULES.md`, and `09_ACCURACY_ENGINE\checklists\PILL_STYLE_PLACEMENT_CHECKLIST.md`. Pipeline prompts `09_pcb_placement_pass_1.md` and `10_pcb_placement_pass_2_orientation.md` now require bottom-facing USB-C on dev boards, explicit barrel-jack review, clean test pad rows, ESP32 RF keepout at the top edge, no unproven four-hole layouts on narrow boards, no overlaps, no unexplained dead areas, and LJ visual approval before routing.

Latest barrel-jack/USB-C orientation rule patch, 2026-05-07: after LJ provided a horizontal barrel-jack reference image, `09_ACCURACY_ENGINE\pcb_rules\BARREL_JACK_ORIENTATION_RULES.md` and `10_KNOWLEDGE_BASE\connectors\BARREL_JACK_ORIENTATION_GUIDE.md` now record that the female circular barrel opening is the front/mating side and the 3-pin solder-leg side is the rear/back side. For bottom-edge J1, the female opening must face down/off-board and the 3-pin solder side must face up/inward. USB-C rules now explicitly require mouth/off-board, bottom-edge mouth down/off-board, `PCB Edge` alignment to `Edge.Cuts`, pads on-board, expected shell/body overhang, and proof beyond coordinates. The LJ image still requires manual binary save to the documented `.png` paths because the chat image was not available as a filesystem source.

Latest maintenance supervisor repair, 2026-05-07: KiCad Engine now has a canonical live-state maintenance supervisor under `03_TOOLS\scripts\maintenance\run_maintenance_cycle.py`. It builds `reports\LIVE_PROJECT_STATE.json` and `.md` from the actual `.kicad_pro`, `.kicad_sch`, and `.kicad_pcb`, runs stale-report detection, reconciles gates, rebuilds memory/history/AI-quality indexes, rebuilds `CURRENT_KNOWN_PROBLEMS.md`, updates project `memory\CURRENT_PROJECT_STATE.md` and `CURRENT_BLOCKERS.md`, and writes `reports\MAINTENANCE_CYCLE_REPORT.md`. The older `03_TOOLS\scripts\memory_maintenance\run_memory_maintenance.py` path is now a compatibility wrapper only.

Latest prompt-count maintenance rule, 2026-05-07: active projects still use a project-specific prompt counter under `memory\PROMPT_COUNTER.md`, but the required maintenance command is now `python 03_TOOLS\scripts\maintenance\run_maintenance_cycle.py --project <active_project>`. At 5 meaningful repo tasks, new engineering work is blocked until that cycle runs and the counter is reset. Compatibility wrappers remain under `03_TOOLS\scripts\memory_maintenance\`.

Latest task-type execution contract hardening, 2026-05-08: KiCad Engine now has a dedicated execution-contract layer under `03_TOOLS\scripts\execution_contract`. Every meaningful Codex run must declare exactly one task type from `DOCS_ONLY`, `AUDIT_ONLY`, `LIVE_STATE_RECONCILE`, `PLACEMENT_EDIT_REQUIRED`, `ROUTING_EDIT_REQUIRED`, `PCB_EDIT_REQUIRED`, or `GITHUB_DOCS_ONLY`. Edit-required task types must prove backup creation, `.kicad_pcb` hash evidence, DRC evidence, and visual-export attempt; routing edits also require unrouted/unconnected counts plus trace-change-log proof, and placement edits require placement-report proof. If an edit-required run ends with only docs/reports and no engineering artifact change, the required outcome is `EDIT_REQUIRED_FAILED_NO_ENGINEERING_ARTIFACT_CHANGE`.

Latest live-state authority hardening, 2026-05-08: KiCad Engine now routes gate decisions through a canonical live-state authority layer under `03_TOOLS\scripts\project_state`. New authority files: `live_state_authority.py`, `validate_live_state_before_gate.py`, and `live_state_gate_wrapper.py`. `LIVE_PROJECT_STATE.json` is now the top authority for project gates, placement/routing-start decisions, and closeout status claims. Reports without source hashes are weak, reports older than the live `.kicad_pcb` or `.kicad_sch` evidence are stale, and stale `NO_PCB`, `0 footprints`, or `no routing` claims cannot overrule live KiCad file evidence. `check_phase_allowed.py` now runs through the wrapper and may report blocker sources as `LIVE_FILE_EVIDENCE`, `FRESH_GATE_REPORT`, `STALE_REPORT_IGNORED`, `TASK_CONTRACT_FAILURE`, or `HUMAN_REVIEW_REQUIRED`. The maintenance cycle now consumes the same authority bundle instead of rebuilding a parallel gate view.

Latest routing geometry hard-fail layer, 2026-05-08: `14_LAYOUT_AUTOMATION` now hard-fails ugly routing geometry instead of treating it as a soft audit note. New authoritative files: `ROUTING_GEOMETRY_HARD_FAIL_RULES.md`, `scripts\route_quality_common.py`, `scripts\routing_geometry_quality.py`, `scripts\detect_right_angle_traces.py`, `scripts\detect_acute_jogs.py`, `scripts\detect_bad_pad_entry.py`, and `scripts\detect_unnecessary_zigzags.py`. `trace_by_trace_audit.py` now records per-finding net, segment coordinates, layer, reason, and recommended fix, and `score_routing_plan.py` now blocks pass status when the trace audit reports `RIGHT_ANGLE_FOUND`, `ACUTE_JOG_FOUND`, `PAD_ENTRY_GEOMETRY_POOR`, `UNNECESSARY_ZIGZAG_FOUND`, `CRITICAL_LOOP_DETOUR_FOUND`, `KEEP_OUT_CROSSING_FOUND`, `UNJUSTIFIED_VIA_FOUND`, or `TRACE_WIDTH_MISMATCH_FOUND`. A DRC-clean route is no longer enough if the geometry is visibly bad.

Latest placement readiness scoring layer, 2026-05-08: `14_LAYOUT_AUTOMATION` now also scores whether a real or copied board placement is actually ready for routing. New authoritative files: `PLACEMENT_READINESS_SCORECARD.md`, `scripts\score_placement_readiness.py`, `scripts\detect_connector_orientation_risks.py`, `scripts\detect_power_path_placement_risks.py`, `scripts\detect_usb_cluster_placement_risks.py`, `scripts\detect_antenna_keepout_placement_risks.py`, and `scripts\detect_testpad_accessibility_risks.py`. The scorer reads the current `.kicad_pcb` in read-only mode, evaluates connector orientation, board-fit, ESP32 antenna keepout, power-path adjacency, USB cluster compactness, test-pad accessibility, clearance, and routing feasibility, then returns exact status `PLACEMENT_READY_FOR_ROUTING`, `PLACEMENT_REPAIR_REQUIRED`, or `PLACEMENT_BLOCKED_HUMAN_REVIEW`. `REAL_PROJECT_ROUTING_PRECONDITIONS.md`, `REAL_PROJECT_ROUTING_WORKFLOW.md`, and `FULL_PIPELINE_GATE_CHECKLIST.md` now require a fresh placement readiness scorecard with exact result `PLACEMENT_READY_FOR_ROUTING` before routing can be treated as eligible.

## 1. Purpose of this repo

`KICAD_ENGINE` is LJ's local-first KiCad engineering workspace for AI-assisted PCB design support, review, verification, documentation, and fabrication preparation. It is organized to keep KiCad projects, project memory, command history, tools, outputs, datasheets, backups, and reference designs separate.

Product positioning, architecture, and agent operating docs:

- `00_CODEX_START\PRODUCT_VISION.md`
- `00_CODEX_START\KICAD_ENGINE_ARCHITECTURE.md`
- `00_CODEX_START\STRUCTURE_STANDARD.md`
- `00_CODEX_START\FOLDER_ROUTING_RULES.md`
- `00_CODEX_START\REPO_STRUCTURE_INDEX.md`
- `00_CODEX_START\KICAD_AGENT_OPERATING_MANUAL.md`
- `00_CODEX_START\KICAD_SAFE_AUTOMATION_RULES.md`
- `00_CODEX_START\KICAD_PIPELINE_STARTUP_RULES.md`
- `09_ACCURACY_ENGINE\workflows\FULL_KICAD_PROJECT_PIPELINE.md`
- `09_ACCURACY_ENGINE\checklists\FULL_PIPELINE_GATE_CHECKLIST.md`
- `03_TOOLS\kicad_app_intelligence\KICAD_AGENT_TASK_MAP.md`
- `.prompts\README.md`
- `.prompts\kicad_pipeline\` prompt files
- `02_HISTORY\design_reviews\KICAD_ENGINE_PRODUCT_GAP_AUDIT.md`

These documents position the repo as a transparent, local, auditable, KiCad-native alternative direction to cloud-first PCB AI tools. The repo should make the user's installed KiCad app easier for Codex, Claude, and similar VS Code-based agents to inspect and automate safely. It should not replace KiCad or claim fabrication readiness without the verification gate.

The workspace supports:

- KiCad schematic and PCB review.
- KiCad automation through safe scripts and installed tools.
- ERC and DRC checks using `kicad-cli`.
- BOM review and export.
- Gerber, drill, STEP, pick-and-place, and visual review workflows.
- Project-specific memory and history.
- Reference design review from finished PCB projects.
- Codex startup control through `AGENTS.md` and `00_CODEX_START`.
- Reusable VS Code prompt packs for Codex, Claude, and similar agents through `.prompts`.

AI review is only assistance. It is not fabrication approval. Manufacturing output is not final until ERC, DRC, BOM, footprint, netlist, datasheet, connector, polarity/orientation, mechanical, and visual review are complete.

## 2. Important rule for AI agents

`AGENTS.md` is the main instruction file. Codex and other agents must read it first when working in this workspace.

Before touching KiCad project files, Codex must read every required file in `00_CODEX_START` in the order defined by `AGENTS.md`, then review relevant memory and history. If `00_CODEX_START\CURRENT_PROJECT.md` says the active project is `NONE`, Codex may work on documentation, tools, prompts, memory, history, indexes, and workspace setup, but must not edit KiCad design files.

KiCad design files include `.kicad_sch`, `.kicad_pcb`, `.kicad_pro`, symbol libraries, footprint libraries, project-local libraries, and manufacturing output files.

### Schematic-to-PCB gate

Codex, Claude, and similar agents must not update PCB from schematic, import schematic changes into PCB, place parts, route traces, create copper zones, or generate PCB manufacturing outputs unless the active project's `reports\SCHEMATIC_TO_PCB_GATE_STATUS.md` exists and its gate result is exactly `PASS`.

The gate requires annotation, ERC, full-page visual export, close-up visual review, hidden footprint/library/path fields in normal view, electrical audit, BOM lock audit, footprint/package drawing audit, connector orientation review, polarity review, project-specific high-risk checks, and all unresolved high-risk `NEEDS_REVIEW` items to pass.

Automated visual crop `PASS` is not human-readable visual `PASS`. A schematic is visually failed if rendered PNG/crop evidence shows overlapping text, values, references, net labels, wires, pins, symbol bodies, power symbols, or review notes inside active circuitry. ERC pass, annotation pass, populated footprints, hidden footprint fields, and no `?` tokens do not prove the schematic is readable. If rendered images cannot be inspected, visual status is `VISUAL_NOT_VERIFIED`, not `PASS`.

Gate documents:

- `09_ACCURACY_ENGINE\workflows\SCHEMATIC_TO_PCB_GATE_WORKFLOW.md`
- `09_ACCURACY_ENGINE\checklists\SCHEMATIC_READY_FOR_PCB_CHECKLIST.md`
- `09_ACCURACY_ENGINE\checklists\SCHEMATIC_HUMAN_READABILITY_CHECKLIST.md`
- `09_ACCURACY_ENGINE\checklists\PCB_UPDATE_FROM_SCHEMATIC_CHECKLIST.md`
- `09_ACCURACY_ENGINE\verification_rules\SCHEMATIC_TO_PCB_BLOCKERS.md`
- `09_ACCURACY_ENGINE\verification_rules\NEEDS_REVIEW_BLOCKER_RULES.md`
- `09_ACCURACY_ENGINE\verification_rules\SCHEMATIC_ANNOTATION_RULES.md`
- `09_ACCURACY_ENGINE\verification_rules\SCHEMATIC_COMPLETENESS_RULES.md`
- `09_ACCURACY_ENGINE\verification_rules\CLOSE_UP_VISUAL_REVIEW_RULES.md`
- `09_ACCURACY_ENGINE\verification_rules\HUMAN_READABLE_SCHEMATIC_RULES.md`
- `09_ACCURACY_ENGINE\verification_rules\VISUAL_PASS_IS_NOT_AUTOMATED_PASS.md`

Schematic screening scripts:

- `03_TOOLS\scripts\kicad_schematic_checks\check_schematic_annotation.py`
- `03_TOOLS\scripts\kicad_schematic_checks\check_schematic_completeness.py`
- `03_TOOLS\scripts\kicad_schematic_checks\check_bom_lock_alignment.py`
- `03_TOOLS\scripts\kicad_schematic_checks\check_needs_review_markers.py`
- `03_TOOLS\kicad\run_schematic_visual_check.ps1`
- `03_TOOLS\scripts\visual\generate_schematic_closeups.py`

### Full KiCad project pipeline

Future KiCad projects must use the reusable pipeline prompt pack under `.prompts\kicad_pipeline` unless the user explicitly approves an exception. The pipeline gates run from schematic annotation/completeness through visual review, electrical audit, footprint/package audit, schematic-to-PCB gate, PCB update, mechanical setup, placement, holes/pads/vias, zones, routing plan, critical routing, remaining routing, final PCB verification, and `NOT_FINAL` fabrication review export.

Agents must also enforce the mandatory phase order in `00_CODEX_START\KICAD_PHASE_ORDER.md`. Before starting a phase, run `03_TOOLS\scripts\project_gate\check_phase_allowed.py --project <ACTIVE_PROJECT_PATH> --phase <PHASE>`. It now consults live project state first and ignores stale operational reports when live KiCad files contradict them. If it returns `BLOCKED`, stop and report the live or fresh-report blocker source instead of inventing a missing earlier phase from stale markdown.

Pipeline documents:

- `00_CODEX_START\KICAD_PIPELINE_STARTUP_RULES.md`
- `00_CODEX_START\KICAD_PHASE_ORDER.md`
- `09_ACCURACY_ENGINE\workflows\FULL_KICAD_PROJECT_PIPELINE.md`
- `09_ACCURACY_ENGINE\workflows\MANDATORY_KICAD_PHASE_GATE.md`
- `09_ACCURACY_ENGINE\checklists\FULL_PIPELINE_GATE_CHECKLIST.md`
- `09_ACCURACY_ENGINE\checklists\PCB_PHASE_GATE_CHECKLIST.md`
- `09_ACCURACY_ENGINE\verification_rules\NO_PHASE_SKIPPING_RULES.md`
- `.prompts\kicad_pipeline\01_schematic_annotation_and_completeness.md` through `.prompts\kicad_pipeline\17_export_not_final_fab_package.md`

Exceptions must be logged with affected gate, user approval evidence, reason, risk, and `HUMAN_REVIEW_REQUIRED`. A later-stage report never authorizes bypassing an earlier gate.

## 3. Root folder structure

### `.codex`

- Purpose: Workspace-local Codex configuration and reusable prompt files.
- Belongs there: `.codex\config.toml`, `.codex\prompts\*.md`.
- Does not belong there: Secrets, project design files, generated manufacturing packages, third-party source repos.
- Codex edit policy: Editable only when explicitly requested. Back up config before changing MCP settings. Do not change the user's global Codex config outside this repo unless explicitly requested.

### `.vscode`

- Purpose: Workspace-local VS Code support for users and AI agents.
- Belongs there: `settings.json`, `extensions.json`, `tasks.json`, and `launch.json`.
- Does not belong there: Secrets, AI credentials, user tokens, generated outputs, KiCad source edits, or machine-private settings.
- Codex edit policy: Editable for workspace task and editor support. Do not assume Codex, Claude, or any AI tool is authenticated; users must log in to their own tools.

### `.prompts`

- Purpose: Reusable prompt pack for VS Code-based Codex, Claude, and similar AI agents.
- Belongs there: `.prompts\README.md`, task prompts under `.prompts\codex` and `.prompts\claude`, shared standards under `.prompts\shared`, and the reusable KiCad project pipeline under `.prompts\kicad_pipeline`.
- Does not belong there: KiCad project files, generated fabrication packages, secrets, downloaded datasheets, or tool installs.
- Codex edit policy: Editable for prompt and workflow updates. Every prompt must require startup reads, no KiCad project edits without active project confirmation and backup, history logging, verification reports, realistic datasheet claims, unverified-footprint warnings, and `NOT_FINAL` labels for generated manufacturing-style outputs.

### `00_CODEX_START`

- Purpose: Startup instructions and indexes that define how Codex begins every KiCad session.
- Belongs there: Startup checklist, workflow rules, safety rules, control-plane summary, product vision, architecture notes, repo map, tool index, memory index, history index, project index, current project status, learning-loop rules, and AI quality/scoring gates.
- Does not belong there: Command transcripts, one-off session logs, project design decisions, secrets.
- Codex edit policy: Editable for workflow/index updates. Keep it strict and current.

### `01_MEMORY`

- Purpose: Durable workspace and project knowledge.
- Belongs there: Long-lived design rules, component preferences, fab preferences, coding rules, global agent lessons, user corrections, verified/failed workflows, common AI mistakes to avoid, AI reliability memory, hallucination-risk memory, quality-gate rules, and durable project memory.
- Does not belong there: Command logs, temporary observations, raw terminal output, credentials.
- Codex edit policy: Editable for durable decisions only. Do not store passwords, API keys, license keys, private tokens, or credentials.

### `02_HISTORY`

- Purpose: Records of work performed, commands run, reviews, ERC/DRC results, and project history.
- Belongs there: Session logs, command logs, design reviews, ERC/DRC reports, fabrication reviews, failed attempts, issue logs, user corrections, lessons learned, workflow runs, AI self-reviews, AI scorecards, claim/evidence matrices, uncertainty logs, hallucination-risk logs, quality-gate failures, and project-specific history.
- Does not belong there: Secrets, durable design preferences that belong in `01_MEMORY`, third-party repos.
- Codex edit policy: Editable after meaningful work. Record commands/results here, not in memory.

### `03_TOOLS`

- Purpose: Local tool repos, isolated environments, automation scripts, and tool logs.
- Belongs there: `repos`, `python_envs`, `node_envs`, `scripts`, `tool_logs`, plus platform roots `common`, `windows`, and `linux`.
- Does not belong there: Real KiCad projects, final fabrication packages, datasheet archives unless a tool specifically needs them.
- Codex edit policy: Scripts and tool logs are editable when requested. Third-party repos under `03_TOOLS\repos` must not be modified casually. Do not move existing repos or environments into platform roots until a migration is explicitly approved.

Platform-aware tool roots:

- `03_TOOLS\common`: OS-neutral KiCad project intelligence such as KiBot, `kicad-cli` wrappers, InteractiveHtmlBom, KiCanvas, PcbDraw, `pcbnew` scripts, MCP servers, and validators.
- `03_TOOLS\windows`: Windows desktop GUI control and visual automation such as pywinauto, FlaUI, FlaUInspect, AutoHotkey, PyAutoGUI, SikuliX, Inspect.exe notes, and Accessibility Insights notes.
- `03_TOOLS\linux`: Linux GUI, headless, CI, and container automation such as xdotool, wmctrl, ydotool, dogtail, Xvfb, x11vnc, PyAutoGUI on X11, SikuliX Linux, Docker, and Linux KiCad CLI.
- Existing legacy paths remain valid until migration is explicitly approved: `03_TOOLS\repos`, `03_TOOLS\scripts`, `03_TOOLS\python_envs`, `03_TOOLS\node_envs`, and `03_TOOLS\tool_logs`.
- Windows GUI automation environment `03_TOOLS\python_envs\windows_gui` is installed for passive discovery/screenshot experiments only.
- Windows GUI helper repos are cloned under `03_TOOLS\windows\repos` for reference only: FlaUI, FlaUInspect, AutoHotkey, and SikuliX1. They are not installed, built, or approved for KiCad control.
- Linux/headless automation has planning docs and starter read-only scripts under `03_TOOLS\linux`; no Linux tools have been installed from Windows and WSL is not assumed configured.

### `04_KICAD_PROJECTS`

- Purpose: Active KiCad projects and project templates.
- Belongs there: `active` real/sample projects and `templates` project templates.
- Does not belong there: Global tool repos, global command logs, final release archives outside the project workflow.
- Codex edit policy: Templates are editable when requested. Active project files are editable only after active project, path, backup, verification plan, and rollback plan are confirmed.

### `05_OUTPUTS`

- Purpose: Generated review and release output area.
- Belongs there: Timestamped reports, exports, review artifacts, non-final manufacturing-style outputs.
- Does not belong there: Source KiCad files that are the canonical project source, secrets, untracked edits to reference projects.
- Codex edit policy: Codex may create timestamped outputs when requested and safe. Do not overwrite or delete older outputs.

### `06_DATASHEETS`

- Purpose: Professional electronics datasheet and reference library.
- Belongs there: Component datasheets, package drawings, errata, application notes, reference designs, vendor portal notes, board-house fabrication/assembly references, and source metadata.
- Does not belong there: Secrets, project source files, generated Gerbers.
- Codex edit policy: Codex may add or organize datasheet references when requested. Do not download datasheets without explicit approval. Do not fabricate claims from missing datasheets.
- Primary index: `06_DATASHEETS\00_INDEX\DATASHEET_LIBRARY_README.md`.
- Master index: `06_DATASHEETS\00_INDEX\MASTER_DATASHEET_INDEX.md`.
- Source rules: `06_DATASHEETS\00_INDEX\VERIFIED_SOURCE_RULES.md` and `06_DATASHEETS\00_INDEX\COPYRIGHT_AND_LINKING_POLICY.md`.
- Current structure: numbered, AI-friendly category folders from `01_MICROCONTROLLERS` through `19_VENDOR_PORTALS`, plus `99_UNSORTED_INBOX`.
- Legacy migration: old top-level folders were preserved under `06_DATASHEETS\99_UNSORTED_INBOX\LEGACY_MIGRATION_20260502_161444`; see `06_DATASHEETS\00_INDEX\MIGRATION_LOG_20260502_161444.md`.
- Research pipeline: `06_DATASHEETS\00_INDEX\RESEARCH_PIPELINE.md`, `PUBLIC_RELEASE_DATASHEET_POLICY.md`, `SOURCE_PRIORITY_RULES.md`, `VENDOR_DOWNLOAD_RULES.md`, and `LINK_ONLY_VS_BUNDLED_POLICY.md`.
- Source lists: `06_DATASHEETS\00_INDEX\source_lists\*.csv` store vendor, family, part, document type, source URL, target folder, redistribution status, and notes. These are metadata-first lists, not downloaded PDF archives.
- Research scripts: `03_TOOLS\scripts\datasheets\validate_datasheet_links.py`, `build_datasheet_index.py`, `create_missing_datasheet_report.py`, and `generate_component_summary_stub.py`.
- Public-release rule: keep datasheets link-only unless redistribution permission is clearly confirmed. The research scripts do not download by default, and their `--download` flag is intentionally disabled.

### `07_REFERENCE_DESIGNS`

- Purpose: General reference design metadata, link-first examples, and review notes that are separate from the curated `12_REFERENCE_DESIGN_LIBRARY`.
- Belongs there: Public-source design links, source notes, lightweight summaries, inspiration records, and early reference candidates pending license/source review.
- Does not belong there: Proprietary copied designs, active KiCad project sources, generated fabrication outputs, unclear-license archives, or claims that a reference design approves a new design.
- Codex edit policy: Editable for metadata and source-link notes when requested. Keep records link-only unless license and redistribution rights are reviewed.

### `08_COMPONENT_DATABASE`

- Purpose: Structured component intelligence beyond raw PDFs for AI-assisted KiCad planning, review, and source-verification workflows.
- Belongs there: Part records, verification flags, KiCad symbol/footprint/3D model candidate links, layout warnings, common mistakes, selection guides, and design-rule snippets.
- Does not belong there: Datasheet PDFs, KiCad project source files, fabrication outputs, or fabricated electrical claims.
- Codex edit policy: Editable for schema, placeholder records, and verified component records when requested. Keep records marked `UNVERIFIED_PLACEHOLDER` until exact datasheet, vendor reference design, KiCad library, or user-confirmed evidence is recorded.
- Primary index: `08_COMPONENT_DATABASE\00_INDEX\COMPONENT_DATABASE_README.md`.
- Master index: `08_COMPONENT_DATABASE\00_INDEX\MASTER_COMPONENT_INDEX.md`.
- Schema and rules: `PART_SCHEMA.md`, `VERIFICATION_LEVELS.md`, `AI_USAGE_RULES.md`, and `KICAD_SYMBOL_FOOTPRINT_LINKING_RULES.md`.
- Initial examples: `EXAMPLE_COMPONENT_RECORDS.md` and `example_component_records.json`; all 19 initial records are placeholders, not approved design data.
- Core starter placeholders: `99_UNVERIFIED_INBOX\core_starter_records\CORE_STARTER_RECORDS.md` and `core_starter_records.json`; all 15 records are `UNVERIFIED_PLACEHOLDER` and require human review.
- No-guess rules: `00_INDEX\DO_NOT_GUESS_RULES.md`.
- Package and verification scaffold: `15_PACKAGE_FOOTPRINT_DATABASE` and `16_VERIFICATION_RECORDS`.

### `09_ACCURACY_ENGINE`

- Purpose: Accuracy and anti-hallucination rule system for schematic creation, PCB creation, component adds, symbol/pinout checks, footprint verification, ERC/DRC interpretation, BOM/PNP/Gerber review, and release-package gates.
- Belongs there: Schematic rules, PCB rules, verification rules, and repeatable workflows that force source-backed design decisions.
- Does not belong there: KiCad project source files, downloaded datasheets, generated manufacturing outputs, secrets, or unsupported electrical claims.
- Codex edit policy: Editable for accuracy-rule improvements when requested. Before creating or editing schematic/PCB content, agents must read the relevant files under `09_ACCURACY_ENGINE`.
- Core rule: every component must have a source; every symbol must map to verified pinout evidence; every footprint must map to an exact package drawing or remain `UNVERIFIED_FOOTPRINT`; every connector orientation, polarity-sensitive part, RF/USB/CAN part, and manufacturing output must keep explicit review status.
- Prompt 3 accuracy gate update: `09_ACCURACY_ENGINE/checklists/ACCURACY_GATE_CHECKLIST.md`, `verification_rules/ERC_DRC_REQUIRED_RULES.md`, `FAB_OUTPUT_NOT_FINAL_RULES.md`, and `HUMAN_REVIEW_GATE_RULES.md` define the mandatory evidence gate for schematic, PCB, BOM, and fab-output claims.
- Schematic-to-PCB gate update: `workflows/SCHEMATIC_TO_PCB_GATE_WORKFLOW.md`, `checklists/SCHEMATIC_READY_FOR_PCB_CHECKLIST.md`, `checklists/PCB_UPDATE_FROM_SCHEMATIC_CHECKLIST.md`, `verification_rules/SCHEMATIC_TO_PCB_BLOCKERS.md`, and `verification_rules/NEEDS_REVIEW_BLOCKER_RULES.md` block PCB update/layout/routing/zones/fab-style outputs until the active project gate file is `PASS`.
- Full KiCad project pipeline update: `workflows/FULL_KICAD_PROJECT_PIPELINE.md`, `checklists/FULL_PIPELINE_GATE_CHECKLIST.md`, `00_CODEX_START/KICAD_PIPELINE_STARTUP_RULES.md`, and `.prompts/kicad_pipeline` define the permanent 17-stage schematic-to-PCB-to-routing-to-NOT_FINAL-fabrication workflow for future projects. The workflow is reusable but not a proof that any specific project has passed.
- Schematic annotation/completeness checker update: `03_TOOLS\scripts\kicad_schematic_checks` provides read-only scripts for annotation, duplicate references, missing values, footprint assignment, BOM-lock alignment, functional-block completeness, and unresolved `NEEDS_REVIEW` markers. These scripts produce evidence for the schematic-to-PCB gate but do not approve footprints, pinouts, connector orientation, or fabrication readiness.
- Automatic schematic visual close-up update: `03_TOOLS\kicad\run_schematic_visual_check.ps1` exports full-page SVG/PDF, optionally renders PNG when a renderer is available, calls `03_TOOLS\scripts\visual\generate_schematic_closeups.py`, and creates `_verification\schematic_visual` crops plus `reports\CLOSE_UP_REVIEW.md`. The visual block config standard is `03_TOOLS\kicad\VISUAL_BLOCK_CONFIG_STANDARD.md`; close-up gate rules are `09_ACCURACY_ENGINE\verification_rules\CLOSE_UP_VISUAL_REVIEW_RULES.md`.

### `10_KNOWLEDGE_BASE`

- Purpose: AI-readable reusable engineering knowledge for practical schematic and PCB creation.
- Belongs there: Circuit block guides, design patterns, pre-review checklists, common mistake lists, manufacturing package rules, and AI-agent stop/verify guidance.
- Does not belong there: Datasheet PDFs, KiCad project source files, generated manufacturing outputs, secrets, or unsourced exact electrical claims.
- Codex edit policy: Editable for knowledge-base improvements when requested. Before proposing common circuits, connector interfaces, power trees, MCU minimum systems, manufacturing packages, or review plans, agents should read the relevant files under `10_KNOWLEDGE_BASE`.
- Core rule: knowledge-base files are planning aids, not datasheet proof. Exact values, pinouts, footprints, connector drawings, stackups, and fab-house requirements still require source verification.
- Prompt 4 core update: the required circuit-pattern pages and common-mistake pages are scaffolded, including PIC-specific mistake guidance. These files are AI guidance only and must not be used as proof of exact values, pinouts, or footprints.

### `11_LIBRARY_FACTORY`

- Purpose: Source-backed KiCad symbol, footprint, package mapping, project-local library, and basic read-only library QA standards.
- Belongs there: Symbol standards, footprint standards, symbol-to-footprint mapping rules, datasheet package-to-footprint rules, project-local library rules, 3D model review guidance, cross-cutting QA workflow, and read-only validation scripts.
- Does not belong there: Installed KiCad global libraries, user-global library tables, KiCad project source files, generated manufacturing outputs, secrets, or unsupported package/pinout claims.
- Codex edit policy: Editable for library-factory standards and scripts when requested. Before creating, selecting, verifying, or mapping symbols and footprints, agents should read the relevant files under `11_LIBRARY_FACTORY`.
- Core rule: symbol creation must be driven by exact pinout evidence, footprint creation must be driven by exact package or connector drawings, connector footprints require human orientation review, 3D models are visualization/mechanical review aids only, and scripts provide basic checks only.
- Library factory setup update: `11_LIBRARY_FACTORY` now includes `symbols`, `footprints`, `mapping`, `3d_models`, `qa`, and `scripts`. The scripts are read-only for input libraries and write reports only when explicit output paths are provided.

### `12_REFERENCE_DESIGN_LIBRARY`

- Purpose: Source-aware reference design records so agents can learn from verified examples without blindly copying them.
- Belongs there: Reference design links, summaries, license notes, verification levels, category checklists, and "what can be learned / what must not be copied" records.
- Does not belong there: Proprietary copied designs without permission, unclear-license design archives, active KiCad project source files, generated manufacturing outputs, secrets, or unsupported claims that a reference design approves a new design.
- Codex edit policy: Editable for reference design records, indexes, and checklists when requested. Keep records link-only unless license and redistribution are reviewed.
- Core rule: reference designs are evidence, not automatic approval. Exact parts, symbols, footprints, connectors, layout constraints, ERC, DRC, and human review still apply.
- Prompt 4 core update: `12_REFERENCE_DESIGN_LIBRARY\00_INDEX` now uses the statuses `VERIFIED`, `PARTIALLY_VERIFIED`, `LINK_ONLY`, and `UNVERIFIED`. Starter records are link-only source portals and must not be treated as copied or fully verified designs.

### `13_PART_INGESTION`

- Purpose: Workflow and stub-generation layer for adding new parts from user-provided datasheets, source URLs, or local document paths.
- Belongs there: Datasheet review workflow, extraction rules, component record generation rules, AI summary template, and scripts that create placeholder datasheet summaries, component records, symbol checklists, and footprint checklists.
- Does not belong there: Downloaded datasheets without redistribution review, scraped website copies, active KiCad project files, fabricated electrical values, verified claims without source evidence, secrets, or credentials.
- Codex edit policy: Editable for ingestion workflow and script improvements when requested. Generated stubs must remain explicit placeholders until datasheet/source review is complete.
- Core rule: ingestion supports link-only public records and user-provided files. It does not require web scraping, PDF redistribution, or fake certainty.

### `14_LAYOUT_AUTOMATION`

- Purpose: Reality-check and planning layer for KiCad-native placement assistance, routing assistance, constraint extraction, FreeRouting integration, and human layout review gates.
- Belongs there: Placement/routing plans, constraint extraction plans, autorouter option analysis, FreeRouting integration plan, AI placement review rules, human layout gates, and roadmap.
- Does not belong there: Active KiCad project source files, generated routed boards, installed autorouter binaries, downloaded tools, manufacturing outputs, or untested claims of complete AI auto-layout/autorouting.
- Codex edit policy: Editable for layout automation planning and future read-only analyzers when requested. Any actual placement/routing writes require active project confirmation, backup, copied workspace preference, DRC before/after, and human review.
- Core rule: KiCad Engine can plan and review layout assistance, but must not claim complete AI autorouting until implementation and test evidence exist.

### `15_BENCHMARKS`

- Purpose: Benchmark methodology, benchmark task definitions, scoring rubrics, and future real run results for measuring KiCad Engine progress honestly.
- Belongs there: Methodology docs, task prompts, scoring rules, runner plans, and documented benchmark results after actual runs.
- Does not belong there: Fake scores, backfilled results from memory, active KiCad project source files, generated manufacturing outputs, secrets, unsupported comparison claims, or fabricated performance evidence.
- Codex edit policy: Editable for benchmark framework improvements when requested. Do not add result folders unless a benchmark run actually happened and artifacts, metadata, scoring notes, and human review status are recorded.
- Core rule: Benchmark claims require evidence. Do not claim KiCad Engine beats another PCB AI tool unless the same task, constraints, scoring method, and evidence standard were used.
- Prompt 8 update: core benchmark task set now includes ESP32-S3 minimum system, STM32 minimum system, CAN bus node, USB-C power device, 12V automotive input, and connector footprint verification. Results remain empty unless a real run is performed.

### `16_INSTALLER`

- Purpose: Installer coordination layer for release-facing installer plans, payload routing, build notes, and status summaries.
- Belongs there: Installer indexes, installer release notes, packaging status, and links to the current implementation under `installer`.
- Does not belong there: Electron source duplicated from `installer`, binaries, credentials, private signing keys, or system-modifying scripts that run silently.
- Codex edit policy: Editable for installer coordination docs. Current installer implementation remains under `installer` until an explicit migration task approves moving it.
- Public release structure update: contains `INSTALLER_ARCHITECTURE.md`, platform installer plans, `PAYLOAD_MANIFEST.md`, `SECURITY_MODEL.md`, `UPDATE_MODEL.md`, and `USER_FLOW.md`. No binaries were built.

### `17_RELEASE_BUILD`

- Purpose: Release build staging records and artifact-readiness coordination.
- Belongs there: Artifact manifests, checksum records, release build reports, packaging notes, and release readiness summaries.
- Does not belong there: Secrets, private signing material, unchecked binaries, old personal logs, or final fabrication outputs.
- Codex edit policy: Editable for release documentation and generated release records. Do not publish releases or claim release readiness without build and smoke-test evidence.
- Public release structure update: contains `RELEASE_BUILD_PLAN.md`, `PAYLOAD_BUILD_RULES.md`, `GITHUB_RELEASE_CHECKLIST.md`, `ARTIFACT_NAMING.md`, and `CHECKSUM_RULES.md`.

### `18_PUBLIC_DOCS`

- Purpose: Public documentation coordination layer for GitHub, website, and installer-facing docs.
- Belongs there: Public doc indexes, publishing plans, audience maps, and migration notes for root docs and `docs`.
- Does not belong there: Internal-only logs, private project facts, secrets, unsupported marketing claims, or copyrighted documents.
- Codex edit policy: Editable for public documentation coordination. Current published docs remain in root and `docs` until a migration is explicitly approved.
- Public release structure update: contains user-facing start, manual, FAQ, troubleshooting, Codex, Claude, KiCad, safety, and cloud PCB AI comparison docs. Root `README.md` now points users to `18_PUBLIC_DOCS/START_HERE_FOR_USERS.md`.

### `19_TEST_PROJECTS`

- Purpose: Disposable KiCad test projects, toy examples, and smoke-test workspaces.
- Belongs there: Clearly labeled test projects, fixtures, expected reports, and readme files explaining test purpose.
- Does not belong there: LJ's active production KiCad projects, finished reference originals, secrets, or fabrication packages presented as final.
- Codex edit policy: Editable for tests only. Test projects must be marked as examples or fixtures and must not be confused with approved production designs.
- Prompt 8 update: `19_TEST_PROJECTS/planning_only/ESP32_S3_SAMPLE_AI_WORKFLOW` is a planning-only, `EXAMPLE_ONLY_PLANNING_ONLY` sample with no KiCad source files or manufacturing outputs.

### `20_CI_CD`

- Purpose: CI/CD planning, local automation standards, and release workflow coordination.
- Belongs there: Workflow design notes, CI checklists, local runner notes, artifact naming standards, and release automation docs.
- Does not belong there: GitHub secrets, deployment credentials, private signing keys, or unreviewed installer binaries.
- Codex edit policy: Editable for CI/CD coordination. GitHub Actions implementation remains under `.github/workflows` unless a migration is approved.
- Public release structure update: contains `GITHUB_ACTIONS_PLAN.md`, `BUILD_MATRIX.md`, `TEST_MATRIX.md`, and `RELEASE_WORKFLOW_PLAN.md`. Draft releases only unless a human approves publishing.

### `21_LICENSE_ATTRIBUTION`

- Purpose: License, attribution, and redistribution audit layer.
- Belongs there: Third-party tool attribution, datasheet redistribution audit records, vendor document risk notes, and public-release license checklists.
- Does not belong there: Legal conclusions presented as attorney advice, copied proprietary material, secrets, or unlicensed vendor documents.
- Codex edit policy: Editable for practical risk notes. Mark uncertain items as requiring human review.
- Public release structure update: contains `LICENSE_AUDIT.md`, `THIRD_PARTY_ATTRIBUTION.md`, `DATASHEET_REDISTRIBUTION_POLICY.md`, `PUBLIC_REPO_RISK_REGISTER.md`, and `VENDOR_DOCUMENT_POLICY.md`.

### `22_SECURITY`

- Purpose: Security model, secret-handling, installer safety, and vulnerability-response support.
- Belongs there: Secret scanning rules, secure installer notes, report-handling process, and safety checklists.
- Does not belong there: Secrets, exploit payloads, private keys, credentials, or silent install behavior.
- Codex edit policy: Editable for defensive documentation and checks. Never store credentials in examples.
- Public release structure update: contains `SECURITY_POLICY.md`, `SECRET_HANDLING_RULES.md`, `INSTALLER_SECURITY_RULES.md`, `SCRIPT_SAFETY_RULES.md`, and `REPORTING_SECURITY_ISSUES.md`.

### `23_PACKAGE_PROFILES`

- Purpose: Component package profiles, package-to-footprint rules, and package verification checklists.
- Belongs there: QFN, QFP, SOIC, SOT, DFN, BGA, module, connector, through-hole, and generic package records plus package-to-footprint rules.
- Does not belong there: Active KiCad source files, exact dimensions without source evidence, final fab packages, secrets, or footprint approval claims.
- Codex edit policy: Editable for package metadata and placeholders. Keep records `UNVERIFIED_PLACEHOLDER` until exact package drawings or manufacturer land patterns are cited.
- Prompt 7 update: added package schema, package-to-footprint rules, verification checklist, and starter placeholders for QFN, QFP, SOIC, SOT-23, ESP32 module, and USB-C connector generic profiles.

### `24_FAB_PROFILES`

- Purpose: Fabrication-house profile guidance and NOT_FINAL manufacturing export standards.
- Belongs there: JLCPCB, PCBWay, generic fab, drill, Gerber, BOM, PNP, assembly note, and DFM profile records.
- Does not belong there: Final manufacturing approvals, unverified fab-house rules, private fab credentials, or live order data.
- Codex edit policy: Editable for fab profile guidance. All generated fab-style outputs remain `NOT_FINAL` until full human review.
- Prompt 7 update: added fab profile schema, Gerber/drill rules, BOM/CPL/PNP rules, assembly note rules, NOT_FINAL output rules, and starter JLCPCB/PCBWay generic output profiles. These are placeholders until sourced.

### `25_VENDOR_DATABASE`

- Purpose: Vendor, manufacturer, distributor, lifecycle, source portal, and sourcing metadata.
- Belongs there: Vendor portal links, manufacturer source priorities, distributor placeholders, lifecycle status notes, and source-confidence metadata.
- Does not belong there: Paid account credentials, scraped distributor data, unlicensed copied vendor documents, or fabricated sourcing claims.
- Codex edit policy: Editable for link-first metadata and placeholders. Verify exact availability, lifecycle, and pricing externally before making purchasing claims.
- Prompt 7 update: added vendor schema, vendor source priority rules, official document link rules, lifecycle status rules, and vendor folders for Espressif, STMicro, Microchip, TI, NXP, Nordic, Raspberry Pi, Molex, TE Connectivity, JST, Wurth, and generic suppliers.

### `26_AGENT_QUALITY`

- Purpose: AI response quality, evidence, scorecard, uncertainty, and hallucination-risk support layer.
- Belongs there: Quality-gate indexes, scoring support records, examples, and future analyzers that complement `00_CODEX_START` and `02_HISTORY`.
- Does not belong there: Unsupported claims, secret logs, project-specific facts that belong in project history, or fake scorecards.
- Codex edit policy: Editable for AI quality support. Real session scorecards and evidence records belong in `02_HISTORY` or project `history`.
- Core policy files: `AI_SELF_REVIEW_RULES.md`, `AI_TRUTHFULNESS_SCORING.md`, `AI_HALLUCINATION_RISK_RULES.md`, `AI_RESPONSE_QUALITY_GATE.md`, and `AI_EVIDENCE_REQUIREMENTS.md`.
- Templates: `templates\AI_RESPONSE_SCORECARD_TEMPLATE.md`, `templates\CLAIM_EVIDENCE_MATRIX_TEMPLATE.md`, and `templates\UNCERTAINTY_LOG_TEMPLATE.md`.
- Mandatory rule: every meaningful Codex/Claude session that makes engineering claims must create a self-review, scorecard, uncertainty log, and claim/evidence matrix.

### `27_EXAMPLES`

- Purpose: Safe examples, tutorials, and toy records for users and agents.
- Belongs there: Example component records, example workflows, tutorial snippets, and non-production sample data.
- Does not belong there: Production-approved design claims, real customer secrets, final fab outputs, or unmarked copied project files.
- Codex edit policy: Editable for examples. Mark examples clearly and do not let examples imply engineering approval.
- Prompt 8 update: example subfolders now exist for prompts, reports, memory/history, component records, datasheet summaries, and quality scorecards. All are `EXAMPLE_ONLY`.

### `28_SUPPLIER_INGESTION`

- Purpose: Supplier and distributor data ingestion layer for official API, user CSV, and manual source-link workflows.
- Belongs there: Connector scaffolds, source policies, API-key handling rules, normalized supplier records, stock/pricing snapshots, datasheet-link metadata, lifecycle metadata, and gap reports.
- Does not belong there: API keys, tokens, passwords, private account data, blind scrapers, cached supplier HTML, restricted raw API responses, downloaded PDFs, or sourcing approvals without review.
- Codex edit policy: Editable for safe connector docs, schemas, and offline import scripts. Live supplier API calls require explicit user approval, credential setup through environment variables or ignored local config, terms/rate-limit review, and no credential logging.
- Current scaffold: connector folders exist for Digi-Key, Mouser, JLCPCB, LCSC, Octopart, Arrow, Avnet, Newark/element14, Farnell, TME, RS Components, Rutronik, Future Electronics, and Manual CSV. Digi-Key, Mouser, JLCPCB, and LCSC now have Python connector stubs that default to `DRY_RUN`, normalize local/sample JSON, emit normalized JSON, do not download PDFs, and refuse live API behavior unless `--live` is explicitly requested. Live API calls are not implemented or tested. Scripts also normalize local JSON/CSV, build indexes, create gap reports, match MPNs to component database text, and create conservative footprint candidate notes. No live API clients are enabled.

### `29_FOOTPRINT_GAP_ANALYSIS`

- Purpose: Installed KiCad footprint and symbol inventory plus footprint candidate gap analysis for common parts and component database records.
- Belongs there: Read-only inventory scripts, generated local KiCad footprint/symbol indexes, high-risk footprint reports, connector/MCU/power gap reports, and missing-footprint backlog records.
- Does not belong there: KiCad global library edits, project-local production libraries, downloaded package drawings, final footprint approvals, manufacturing outputs, or secrets.
- Codex edit policy: Editable for read-only analysis scripts and generated reports. Treat every footprint candidate as `UNVERIFIED` until exact package drawing and human review evidence is recorded.

### `30_SUPPLIER_FOOTPRINT_MATCHES`

- Purpose: Supplier SKU/MPN to KiCad symbol, footprint, and 3D model match tracking with explicit confidence and human-review status.
- Belongs there: Match schemas, confidence rules, human-review rules, supplier-specific match records, example-only records, generated match indexes, confidence reports, and unmatched supplier-part reports.
- Does not belong there: API keys, private supplier data, cached supplier pages, downloaded package drawings, KiCad global library edits, project-local production libraries, or final footprint approvals without evidence.
- Codex edit policy: Editable for schemas, safe scripts, example records, and generated reports. Do not mark connector, PMOS, ESD array, MCU module, or regulator footprints verified from package name only.
- Final audit update on 2026-05-03: supplier/datasheet/footprint readiness is `INTERNAL_ALPHA`, not production-ready. Evidence: `02_HISTORY/design_reviews/SUPPLIER_DATASHEET_FOOTPRINT_FINAL_AUDIT.md` and `05_OUTPUTS/release_readiness/SUPPLIER_DATASHEET_FOOTPRINT_SCORECARD.md`. Main blockers are two legacy Espressif PDFs requiring redistribution review, dry-run-only supplier connectors, example-only supplier-footprint matches, and no exact package-drawing verified footprint approvals.

### `31_PLAYWRIGHT_RESEARCH_PIPELINE`

- Purpose: Dry-run-first Playwright-assisted public-page research pipeline for supplier, datasheet, part-number, vendor, public KiCad library, and footprint-source evidence.
- Belongs there: source policies, terms/rate-limit rules, Playwright usage rules, source profiles, target CSVs, guarded scripts, screenshot evidence rules, normalized output schemas, and integration docs for `06_DATASHEETS`, `08_COMPONENT_DATABASE`, `25_VENDOR_DATABASE`, `28_SUPPLIER_INGESTION`, `29_FOOTPRINT_GAP_ANALYSIS`, and `30_SUPPLIER_FOOTPRINT_MATCHES`.
- Does not belong there: credentials, cookies, browser profiles, private account data, scraped supplier HTML, CAPTCHA bypasses, mass-downloaded PDFs, copyrighted documents without redistribution review, KiCad design files, or final footprint/sourcing approvals.
- Codex edit policy: Editable for safe research policies, target lists, templates, dry-run scripts, and reports. Browser execution requires explicit `--live`; PDF download is disabled by default and requires explicit redistribution-risk confirmation if ever enabled.
- Core rule: Playwright research output is evidence, not truth. Captured browser-page data remains `UNVERIFIED` until checked against official datasheet/vendor evidence or human review.

### `32_OPEN_KICAD_SAMPLE_INTAKE`

- Purpose: Controlled intake system for open KiCad sample projects that may become reference-design evidence, benchmark candidates, or workflow test fixtures.
- Belongs there: candidate records, license screening records, source attribution, read-only imported originals, normalized working copies, sample file audits, review reports, benchmark-candidate promotion notes, templates, and dry-run-first scripts.
- Does not belong there: random repo-root downloads, closed/proprietary projects, edited original samples, active user projects, unlicensed bundled samples, secrets, final manufacturing outputs, or public payload content without `PUBLIC_BUNDLE_ALLOWED` status.
- Codex edit policy: Editable for records, policies, templates, dry-run scripts, and review reports. Do not download, clone, import, or promote projects unless source URL, license status, attribution, KiCad file presence, and public-bundle status are recorded. Do not edit `imported_originals`; create a normalized copy first.
- Core rule: A sample project is evidence, not approval. It remains `UNVERIFIED` until license screening, ERC/DRC where applicable, visual review, footprint/package review, and human-review gates are recorded.

### `99_BACKUPS`

- Purpose: Backup area for pre-edit snapshots and recovery files.
- Belongs there: `99_BACKUPS\pre_codex_edits` backups created before AI/script edits.
- Does not belong there: Active working copies, final release outputs, secrets.
- Codex edit policy: Codex may create backups. Do not delete backups.

### `99_01 Finished PCBs`

- Purpose: Reference library of completed PCB projects and associated fabrication/output files.
- Belongs there: Original finished PCB source, BOMs, fabrication files, Gerbers, drill files, pick-and-place files, PDFs, STL files, backups.
- Does not belong there: Active project work, AI-modified copies, new generated outputs unless explicitly archived as reference.
- Codex edit policy: Read/review only by default. Never edit original finished PCB files directly unless LJ explicitly approves a direct finished-folder repair/review task and Codex creates a snapshot first. Otherwise, create review reports in `02_HISTORY` or copy to a safe review workspace when asked.

## 4. Codex startup flow

Codex startup for this workspace is strict:

1. Read root `AGENTS.md`.
2. Read root `README_GPT.md`.
3. Read root `FOR CHAT GPT.MD`.
4. Read `00_CODEX_START\START_HERE.md`.
5. Read `00_CODEX_START\SESSION_START_CHECKLIST.md`.
6. Read `00_CODEX_START\STRUCTURE_STANDARD.md`.
7. Read `00_CODEX_START\FOLDER_ROUTING_RULES.md`.
8. Read `00_CODEX_START\CURRENT_KNOWN_PROBLEMS.md`.
9. Read `00_CODEX_START\MEMORY_INDEX.md`.
10. Read `00_CODEX_START\HISTORY_INDEX.md`.
11. If working on a project, load active project `memory/` and `history/`.
12. Read task-relevant startup files such as `CONTROL_PLANES.md`, `TOOL_INDEX.md`, `PROJECT_INDEX.md`, `CURRENT_PROJECT.md`, accuracy-engine rules, component-database rules, or installer/release docs.
13. Confirm active project, task mode, likely files, backup plan, verification plan, and rollback plan.
14. Only then inspect or edit KiCad project files, and only if the active project gate allows it.

If the active project is `NONE`, do not edit KiCad design files.

## 4A. KiCad Engine Control Planes

The startup summary for this model is `00_CODEX_START\CONTROL_PLANES.md`.

Codex should choose the safest control plane that can complete the task.

### 1. Common / Project Intelligence

Use first whenever possible:

- `kicad-cli`
- KiBot
- `pcbnew` Python
- MCP analysis tools
- File validators
- BOM, Gerber, and pick-and-place parsers

This plane is preferred for deterministic review, static inspection, repeatable checks, and output generation into approved `NOT_FINAL` folders.

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
- Do not use coordinate clicks without screenshots and window-size verification.
- Do not randomly type into KiCad.
- Do not run production project GUI automation until the project is identified and backed up.
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

Tool selection rule:

- Prefer CLI/API/MCP over GUI automation.
- Prefer read-only inspection before edits.
- Prefer copied project workspaces over original projects.
- Prefer `NOT_FINAL` outputs until the verification gate passes.

## 5. Memory system

`01_MEMORY` stores durable knowledge, not logs. It is for facts and decisions that should guide future sessions.

Required memory files:

- `01_MEMORY\GLOBAL_MEMORY.md`: Workspace-wide context. It states this is an AI-assisted KiCad workspace, Codex should operate from `KICAD_ENGINE` unless inside a project, AI-only review is not enough for fabrication, and clean separation between folders must be preserved.
- `01_MEMORY\DESIGN_RULES_MEMORY.md`: Durable PCB/electrical rules and placeholders for board layers, trace width, clearance, power input, vehicle/12 V rules, ESD/protection, connectors, mechanical rules, silkscreen, test points, and fab constraints.
- `01_MEMORY\COMPONENT_PREFERENCES.md`: Preferred MCUs, CAN transceivers, voltage regulators, connectors, protection parts, avoided parts, verified footprints, and unverified footprints.
- `01_MEMORY\FAB_HOUSE_PREFERENCES.md`: Preferred board house, stackup, trace/space, vias, solder mask, silkscreen, stencil, panelization, and required fabrication outputs.
- `01_MEMORY\CODING_AND_SCRIPTING_RULES.md`: Rules for safe repeated scripts, source-file preservation, output destinations, quoted PowerShell paths, logging, KiCad CLI fallback, and no hardcoded secrets.
- `01_MEMORY\AGENT_LESSONS_LEARNED.md`: Reusable lessons for future AI sessions.
- `01_MEMORY\AGENT_MISTAKES_TO_AVOID.md`: Global recurring AI mistakes and avoidance rules.
- `01_MEMORY\AI_RELIABILITY_MEMORY.md`: Reusable AI quality and reliability rules.
- `01_MEMORY\GLOBAL_HALLUCINATION_RISKS.md`: Repo-wide hallucination-risk patterns.
- `01_MEMORY\GLOBAL_UNVERIFIED_CLAIMS.md`: Claim categories that must stay unverified until evidence exists.
- `01_MEMORY\GLOBAL_QUALITY_GATE_RULES.md`: Mandatory AI quality-gate blockers.
- `01_MEMORY\USER_CORRECTIONS_MEMORY.md`: User corrections that apply across projects.
- `01_MEMORY\VERIFIED_WORKFLOWS.md`: Reusable workflows with evidence.
- `01_MEMORY\FAILED_WORKFLOWS.md`: Workflows that failed and should not be repeated unchanged.
- `01_MEMORY\MEMORY_UPDATE_RULES.md`: Rules for promoting history into durable memory.
- `01_MEMORY\projects\<project-id>\PROJECT_MEMORY.md`: Durable project-specific decisions and constraints.
- `04_KICAD_PROJECTS\active\<project-id>\memory`: Current project-local memory for component decisions, footprint decisions, datasheet decisions, design rules, user corrections, agent mistakes, open design risks, memory update rules, project AI reliability, project hallucination risks, project unverified claims, and project quality-gate rules.

Do not store command output, failed attempts, temporary status, passwords, API keys, license keys, private tokens, or credentials in memory.

## 6. History system

`02_HISTORY` records what happened. It is not the durable design-memory store.

History areas:

- `02_HISTORY\sessions`: Session summaries and meaningful work records.
- `02_HISTORY\command_logs`: Commands run, important outputs, failures, and environment observations.
- `02_HISTORY\design_reviews`: Schematic, PCB, component, architecture, and reference-project review notes.
- `02_HISTORY\erc_drc_reports`: ERC/DRC reports or explanations when checks could not be run.
- `02_HISTORY\fabrication_reviews`: Release readiness, Gerber, drill, BOM, placement, and fab package reviews.
- `02_HISTORY\project_history\<project-id>`: Project-specific history and milestone notes.
- `02_HISTORY\failed_attempts`: Global failed-attempt records.
- `02_HISTORY\issue_logs`: Global unresolved issues and blockers.
- `02_HISTORY\user_corrections`: Global user correction evidence.
- `02_HISTORY\lessons_learned`: Lesson records before promotion into memory.
- `02_HISTORY\known_agent_mistakes`: Evidence records for recurring AI mistakes.
- `02_HISTORY\workflow_runs`: Global workflow-run evidence.
- `02_HISTORY\ai_self_reviews`: Global AI self-review records.
- `02_HISTORY\ai_scorecards`: Global AI response scorecards.
- `02_HISTORY\claim_evidence_matrices`: Global claim/evidence matrices.
- `02_HISTORY\uncertainty_logs`: Global uncertainty logs.
- `02_HISTORY\hallucination_risk_logs`: Global hallucination-risk logs.
- `02_HISTORY\quality_gate_failures`: Global quality-gate failure records.
- `04_KICAD_PROJECTS\active\<project-id>\history`: Current project-local history with sessions, command logs, failed attempts, user corrections, design decisions, issue logs, workflow runs, verification runs, AI self-reviews, AI scorecards, claim/evidence matrices, uncertainty logs, hallucination-risk logs, and quality-gate failures.

After meaningful work, write a session log, command logs if commands were run, failed-attempt records for failures, user-correction records when the user reports a problem, AI self-review, response scorecard, claim/evidence matrix, uncertainty/risk logs as needed, open issue records for unresolved problems, and update memory/history/AI-quality indexes plus `CURRENT_KNOWN_PROBLEMS.md`. Durable project facts go in project memory. Reusable cross-project lessons go in global memory.

Indexing scripts for startup/closeout live in `03_TOOLS\scripts\indexing`:

- `build_repo_index.py`
- `build_memory_index.py`
- `build_history_index.py`
- `build_known_problems.py`

These scripts are safe index builders. They scan repo, memory, and history metadata, then write generated Markdown/JSON indexes and master summaries. They must not edit KiCad design files.

## 6A. AI Quality Gate System

`00_CODEX_START` now includes strict AI truthfulness, hallucination-risk, and response-quality rules:

- `AI_SELF_REVIEW_RULES.md`
- `AI_TRUTHFULNESS_SCORING.md`
- `AI_HALLUCINATION_RISK_RULES.md`
- `AI_RESPONSE_QUALITY_GATE.md`
- `AI_EVIDENCE_REQUIREMENTS.md`
- `AI_UNCERTAINTY_DISCLOSURE_RULES.md`
- `AI_ENGINEERING_CLAIM_RULES.md`
- `AI_CLOSEOUT_SCORECARD_RULES.md`
- `CURRENT_KNOWN_PROBLEMS.md`

Agents must score meaningful responses from 0-100, use claim statuses, mark uncertainty clearly, and set `BLOCKED_UNTIL_HUMAN_REVIEW` when exact footprints, connector orientation, datasheets, ERC/DRC, pinouts, or manufacturing-review evidence is missing.

AI quality scripts live in `03_TOOLS\scripts\ai_quality`.

## 7. Tool system

`03_TOOLS` holds tooling. Existing external repositories still belong in `03_TOOLS\repos` until migration is approved. Tool environments are isolated under `03_TOOLS\python_envs` and `03_TOOLS\node_envs`. Existing scripts live under `03_TOOLS\scripts`. Tool install notes, reports, usage guides, and health checks live under `03_TOOLS\tool_logs`.

VS Code workspace support was added on 2026-05-02:

- Workspace files: `.vscode\settings.json`, `.vscode\extensions.json`, `.vscode\tasks.json`, and `.vscode\launch.json`.
- User entry docs: `START_HERE_FOR_USERS.md`, `START_HERE_FOR_AI_AGENTS.md`, `QUICKSTART_WINDOWS.md`, `QUICKSTART_MACOS.md`, and `QUICKSTART_LINUX.md`.
- Tasks include health check, installed KiCad audit, datasheet index generation, component database file index generation, project validation, ERC, DRC, NOT_FINAL review package export, prompt pack folder open, and setup report generation.
- Extension recommendations are optional and do not include paid tooling. Users must install and log in to Codex, Claude, or other AI tools with their own accounts; the repo does not store AI credentials.

Setup and health-check support was added on 2026-05-02:

- Top-level checks: `health_check.ps1`, `health_check.py`, and `HEALTH_CHECK_REPORT_TEMPLATE.md`.
- Setup folders: `setup\windows`, `setup\macos`, `setup\linux`, and `setup\common`.
- Common helpers: `setup\common\create_repo_folders.py`, `build_indexes.py`, and `write_setup_report.py`.
- OS requirement checks: `setup\windows\check_windows_requirements.ps1`, `setup\macos\check_macos_requirements.sh`, and `setup\linux\check_linux_requirements.sh`.
- Optional installers: `install_missing_windows_tools.ps1`, `install_missing_macos_tools.sh`, and `install_missing_linux_tools.sh`.
- Installer policy: ask before every install, prefer official package managers, never silently install paid tools, never store API keys or credentials, and do not modify KiCad project files.

Future installer planning was added on 2026-05-02:

- Planning folder: `installer`.
- Core docs: `installer\README.md`, `INSTALLER_ARCHITECTURE.md`, `WINDOWS_EXE_PLAN.md`, `MACOS_DMG_PLAN.md`, `LINUX_APPIMAGE_DEB_RPM_PLAN.md`, `PAYLOAD_MANIFEST.md`, `SECURITY_MODEL.md`, `SIGNING_AND_RELEASE_NOTES.md`, `UPDATE_MODEL.md`, and `USER_FLOW.md`.
- Scope: design a future cross-platform installer only; no binaries are built yet.
- Installer goals: create a local `KICAD_ENGINE` workspace, check the user's installed KiCad app, optionally install missing free requirements after confirmation, configure VS Code, install prompt packs, create datasheet/component scaffolding, run health check, and open VS Code.
- Installer restrictions: do not bundle KiCad in v1, do not store AI credentials, do not require paid APIs, do not modify installed KiCad folders, and support Windows first before macOS/Linux.
- Milestones: v0.1 repo template, v0.2 Windows setup scripts, v0.3 KiCad app audit, v0.4 datasheet/component database, v0.5 VS Code prompt packs, v0.6 Windows installer, v0.7 macOS/Linux setup, v1.0 public GitHub release.

Installer payload template generation was added on 2026-05-02:

- Payload template root: `installer\payload\repo-template`.
- Build scripts: `installer\payload\build_payload.ps1` and `installer\payload\build_payload.py`.
- Payload docs: `installer\payload\PAYLOAD_CONTENT_RULES.md` and `installer\payload\PAYLOAD_BUILD_SCRIPT.md`.
- Generated outputs: `installer\payload\payload.manifest.json` and `installer\payload\PAYLOAD_BUILD_REPORT.md`.
- Payload behavior: copy only allowed clean workspace files, generate fresh state files, exclude third-party repos, virtual environments, old logs, backups, generated outputs, local active projects, PDFs, and machine-local Codex config.
- Latest validation: `python health_check.py --repo-root installer\payload\repo-template --no-write` reported PASS=97, WARN=0, FAIL=0.

Cross-platform Electron installer project was added on 2026-05-02:

- Installer package files: `installer\package.json` and `installer\electron-builder.yml`.
- App source: `installer\src\main.js`, `preload.js`, `renderer`, and `installer-core`.
- Installer core modules cover platform detection, dependency checks, workspace copy, command execution, health checks, and setup log writing.
- Dependency manifests: `installer\payload\manifests\dependencies.windows.json`, `dependencies.macos.json`, `dependencies.linux.json`, and generated `payload.manifest.json`.
- Build docs: `installer\docs\WINDOWS_INSTALLER_BUILD.md`, `MACOS_INSTALLER_BUILD.md`, `LINUX_INSTALLER_BUILD.md`, `INSTALLER_SECURITY_MODEL.md`, and `INSTALLER_USER_FLOW.md`.
- npm scripts: `npm run dev`, `npm run build:win`, `npm run build:mac`, `npm run build:linux`, and `npm run package`.
- Validation performed without installing packages: JavaScript syntax check passed, JSON manifests parsed, npm scripts listed, dependency detection found local Windows tools, payload health check passed, and installer-core smoke copy under `05_OUTPUTS\installer_smoke_test` passed health check with PASS=97, WARN=0, FAIL=0.
- Packaging binaries were not built in this session because npm dependencies were not installed; do not claim production readiness yet.

Public GitHub release documentation was added on 2026-05-02:

- Public docs: `LICENSE`, `CONTRIBUTING.md`, `SECURITY.md`, `CODE_OF_CONDUCT.md`, `CHANGELOG.md`, `ROADMAP.md`, `DISCLAIMER.md`, and `PUBLIC_RELEASE_CHECKLIST.md`.
- `README.md` is now public-facing and explains what KiCad Engine is, how it works with installed KiCad, VS Code, Codex, Claude, datasheets, component records, and verification scripts.
- Release positioning: KiCad Engine is not official KiCad, is not fabrication approval, does not claim database completeness, and keeps datasheets link-only unless redistribution rights are confirmed.
- Public checklist gates include no secrets, no restricted PDFs, no final fab outputs mislabeled, tested setup scripts, passing health check, tested Windows quickstart, tested sample project, reviewed license, reviewed attribution, and reviewed third-party tool licenses.

KiCad installed app intelligence was added on 2026-05-02:

- Deep audit: `02_HISTORY\design_reviews\KICAD_INSTALLED_APP_DEEP_AUDIT.md`
- Path map: `03_TOOLS\kicad_app_intelligence\KICAD_9_WINDOWS_PATH_MAP.md`
- CLI reference: `03_TOOLS\kicad_app_intelligence\KICAD_CLI_COMMANDS_REFERENCE.md`
- Library guide: `03_TOOLS\kicad_app_intelligence\KICAD_LIBRARY_DISCOVERY_GUIDE.md`
- Do-not-touch rules: `03_TOOLS\kicad_app_intelligence\KICAD_DO_NOT_TOUCH_RULES.md`
- Agent operating manual: `00_CODEX_START\KICAD_AGENT_OPERATING_MANUAL.md`
- Safe automation rules: `00_CODEX_START\KICAD_SAFE_AUTOMATION_RULES.md`
- Agent task map: `03_TOOLS\kicad_app_intelligence\KICAD_AGENT_TASK_MAP.md`
- Read-only scripts: `03_TOOLS\scripts\kicad_app_audit\audit_kicad_windows.ps1`, `check_kicad_cli.ps1`, and `inventory_kicad_libraries.ps1`

The audit confirmed `C:\Program Files\KiCad\9.0\bin`, `etc`, `lib`, and `share` exist, and `kicad-cli version` reports `9.0.7`. Installed stock assets include 224 symbol library files, 155 footprint library folders with 15,415 footprints, and 105 3D model folders with 14,043 files. Agents may read installed KiCad folders as evidence, but must never write into `C:\Program Files\KiCad`.

Datasheet research pipeline was added on 2026-05-02:

- Policy docs: `06_DATASHEETS\00_INDEX\RESEARCH_PIPELINE.md`, `PUBLIC_RELEASE_DATASHEET_POLICY.md`, `SOURCE_PRIORITY_RULES.md`, `VENDOR_DOWNLOAD_RULES.md`, and `LINK_ONLY_VS_BUNDLED_POLICY.md`.
- Source lists: `06_DATASHEETS\00_INDEX\source_lists\espressif_sources.csv`, `stmicro_sources.csv`, `microchip_sources.csv`, `raspberry_pi_sources.csv`, `nordic_sources.csv`, `power_sources.csv`, `connector_sources.csv`, and `protection_sources.csv`.
- Scripts: `03_TOOLS\scripts\datasheets\validate_datasheet_links.py`, `build_datasheet_index.py`, `create_missing_datasheet_report.py`, and `generate_component_summary_stub.py`.
- Outputs: default reports go under `05_OUTPUTS\datasheet_research`.
- Safety: scripts read CSV/JSON source lists, validate metadata/links where possible, create markdown reports, and do not download documents. The future `--download` flag is present but disabled and returns a non-zero exit until licensing and redistribution handling are explicitly designed.
- Microcontroller family content generator added and used on 2026-05-03: `03_TOOLS\scripts\datasheet_tree\create_microcontroller_family_content.py` creates useful AI-readable microcontroller family folders from conservative templates instead of empty placeholder README/INDEX/MISSING/SOURCES files. It supports `--vendor`, `--family`, `--representative-part`, optional source-link seed metadata, optional JSON config, `--dry-run`, explicit `--force`, and safer `--overwrite-weak` placeholder replacement. It marks unknowns `UNKNOWN_REQUIRES_SOURCE`, does not download PDFs, does not scrape, and skips substantive existing files by default. Batch use upgraded 48 MCU family/vendor folders under `06_DATASHEETS\01_MICROCONTROLLERS`, creating 612 new files and replacing 141 obvious weak placeholders. Evidence: `05_OUTPUTS\datasheet_tree\MCU_TREE_COMPLETION_SUMMARY.md` and `02_HISTORY\design_reviews\MCU_DATASHEET_TREE_UPGRADE_REPORT.md`.
- STM32 datasheet tree completion update on 2026-05-03: `06_DATASHEETS\01_MICROCONTROLLERS\STMICRO_STM32\STM32_AI_MASTER_INDEX.md` now links 19 family folders, each with AI-readable overview, design tips, power/clock/reset notes, boot/debug notes, USB/CAN notes, package/footprint notes, schematic/PCB checklists, common mistakes, dev board references, source links, part-number index scaffolds, and research gaps. The tree is classified `SCAFFOLDED_WITH_AI_SUMMARIES`; exact specs remain `UNKNOWN_REQUIRES_SOURCE`.
- STM32 component guide update on 2026-05-03: read `08_COMPONENT_DATABASE\01_MICROCONTROLLERS\STM32_AI_DESIGN_GUIDE.md` before using STM32 family records for schematic, symbol, footprint, or package decisions.
- STM32 source-link index update on 2026-05-03: `STM32_OFFICIAL_SOURCE_LINKS.csv`, `STM32_PART_NUMBER_INDEX.csv`, and `STM32_DEV_BOARD_INDEX.csv` now provide link-only official/public source metadata. These indexes are `PARTIALLY_RESEARCHED_SOURCE_LINKS`, not verified part approvals.
- STM32F1 pilot content update on 2026-05-03: `06_DATASHEETS\01_MICROCONTROLLERS\STMICRO_STM32\STM32F1` now has STM32F1-specific AI overview, STM32F103C8T6 part record, schematic notes, BOOT/debug notes, power/clock notes, package/footprint notes, dev-board notes, source links, common mistakes, KiCad candidate notes, and a needs-review backlog. `08_COMPONENT_DATABASE\01_MICROCONTROLLERS\STM32F103C8T6.md` and `08_COMPONENT_DATABASE\12_KICAD_SYMBOL_FOOTPRINT_MATCHES\STM32F103C8T6_MATCH.md` record official ST source links and local KiCad 9 candidate evidence. These are not design approvals; symbol pinout, package drawing, footprint, 3D model, BOOT/USB/clock/VDDA decisions, and Blue Pill variant assumptions remain human-review-required.

Platform-aware tool roots now also exist:

- `03_TOOLS\common` for OS-neutral KiCad project intelligence.
- `03_TOOLS\windows` for Windows desktop GUI and visual automation.
- `03_TOOLS\linux` for Linux GUI/headless/CI automation.

Strategy and migration docs:

- `03_TOOLS\TOOL_PLATFORM_STRATEGY.md`
- `03_TOOLS\tool_logs\TOOL_MIGRATION_PLAN.md`
- `03_TOOLS\tool_logs\PLATFORM_TOOL_STRUCTURE_CREATED.md`

No existing repos, scripts, Python environments, or Node environments were moved when the platform roots were created.

Known tools and current roles:

- `kicad-mcp-pro`: Installed in `03_TOOLS\python_envs\kicad-mcp-pro`; configured as workspace-local Codex MCP in analysis mode only. MCP server name: `kicad_mcp_pro_analysis`.
- `kicad-happy`: Installed analysis-only in `03_TOOLS\python_envs\kicad-happy`; used for AI-assisted KiCad review guidance and Python analyzers.
- `KiBot`: Installed in `03_TOOLS\python_envs\kibot`; deterministic output automation engine, not production-proven on real projects yet.
- `InteractiveHtmlBom`: Installed and help-tested; not project-tested on real designs.
- `PcbDraw`: Installed and help-tested; not project-tested on real designs.
- `KiCanvas`: Built/tested in isolated Node workspace; read-only visualization role.
- `windows_gui`: Installed in `03_TOOLS\python_envs\windows_gui` with `pywinauto`, `PyAutoGUI`, `PyGetWindow`, `pyperclip`, `pillow`, `opencv-python`, and `psutil`; import-checked only. It is for passive Windows window discovery and screenshot setup, not uncontrolled KiCad GUI control.
- Windows GUI helper repos: FlaUI, FlaUInspect, AutoHotkey, and SikuliX1 are cloned under `03_TOOLS\windows\repos`; not installed or built.
- Linux/headless automation: planning docs and starter scripts exist under `03_TOOLS\linux`; not installed, not run, and WSL is not assumed configured.
- `KiCAD-MCP-Server`: Cloned under `03_TOOLS\repos\KiCAD-MCP-Server`, not installed and not configured.
- `KiCad CLI`: `kicad-cli` 9.0.7 is installed and available on the user PATH.
- PowerShell scripts: Verification, backup, export, project creation, and health-check scripts are under `03_TOOLS\scripts`.

Do not install tools, pull repos, or modify third-party repositories unless the user explicitly asks.

Windows GUI automation docs and passive scripts:

- `03_TOOLS\windows\docs\WINDOWS_GUI_AUTOMATION_README.md`
- `03_TOOLS\windows\docs\KICAD_GUI_CONTROL_LIMITS.md`
- `03_TOOLS\windows\docs\WINDOWS_GUI_REPO_INDEX.md`
- `03_TOOLS\windows\scripts\window_discovery\discover_windows.py`
- `03_TOOLS\windows\scripts\screenshots\take_screenshot.py`
- `03_TOOLS\windows\scripts\KICAD_GUI_DISCOVERY_README.md`
- `03_TOOLS\windows\scripts\window_discovery\discover_kicad_windows.py`
- `03_TOOLS\windows\scripts\pywinauto\inspect_kicad_uia.py`
- `03_TOOLS\windows\scripts\pywinauto\inspect_kicad_win32.py`
- `03_TOOLS\windows\scripts\screenshots\capture_kicad_window.py`

GUI automation must remain passive until LJ explicitly approves a controlled experiment. Codex must discover windows and capture screenshots before any future control action, and must never randomly click or type into KiCad.

KiCad GUI discovery workflow status:

- Created and syntax/import checked on 2026-04-30.
- First read-only discovery run on 2026-04-30 was safe but did not confirm a real KiCad window. The scripts matched VS Code as a false positive because the title contained `KICAD_ENGINE`; direct process checks found no `kicad.exe`, `eeschema.exe`, or `pcbnew.exe`.
- Filter fix completed on 2026-04-30. High-confidence KiCad windows now require process name `kicad.exe`, `eeschema.exe`, or `pcbnew.exe`.
- Title-only matches are now classified as `LOW_CONFIDENCE_TITLE_ONLY` and are not eligible for UIA inspection, Win32 inspection, screenshots, or control.
- Candidate reports include process name, PID, window title, confidence, reason, and eligibility flags.
- Passive filter-fix test found 0 high-confidence KiCad windows; VS Code and Chrome title matches were correctly kept low-confidence and not inspected or captured.
- Confirmed read-only discovery run completed on 2026-04-30 while KiCad was manually open. It found one high-confidence KiCad window: `kicad.exe` PID `19576`, title `COMMAND LINK DRAFT â€” KiCad 9.0`; `eligible_for_control` remained `false`.
- Confirmed run inspection results: UIA recorded 65 controls and Win32 recorded 241 controls for the KiCad window. VS Code and Chrome title-only candidates were ignored for inspection and screenshot capture.
- Confirmed run screenshot: `03_TOOLS\windows\logs\screenshots\kicad_window_20260430_192827_COMMAND_LINK_DRAFT_KiCad_9_0_19576.png`.
- Reports are written under `03_TOOLS\windows\logs`.
- Screenshots are written under `03_TOOLS\windows\logs\screenshots`.
- Use only when KiCad is already open and LJ clearly intends read-only discovery.
- UIA/Win32 may not expose KiCad canvas internals; use screenshot/visual fallback or non-GUI tools when the UI tree is weak.
- Before any GUI control task, confirm a high-confidence KiCad process window and keep `eligible_for_control=false` unless a future task explicitly approves a specific control action.

Linux/headless automation planning:

- `03_TOOLS\linux\docs\LINUX_AUTOMATION_README.md`
- `03_TOOLS\linux\docs\LINUX_KICAD_HEADLESS_PLAN.md`
- `03_TOOLS\linux\docs\WSL_SETUP_NOTES.md`
- `03_TOOLS\linux\docs\LINUX_TOOL_INSTALL_COMMANDS_DRAFT.md`
- `03_TOOLS\linux\scripts\check_linux_kicad_env.sh`
- `03_TOOLS\linux\scripts\xvfb\run_kicad_headless_check.sh`
- `03_TOOLS\linux\scripts\xdotool\list_windows.sh`
- `03_TOOLS\linux\scripts\wmctrl\list_windows.sh`

The Linux scripts are read-only checks/listing scripts. They contain no `sudo`, package install, delete, project modification, or fabrication-output commands. Linux install commands are documented only as future draft commands and were not run.

## 8. MCP setup

Workspace-local MCP configuration is in:

`.codex\config.toml`

Configured server:

- Name: `kicad_mcp_pro_analysis`
- Command: `03_TOOLS\python_envs\kicad-mcp-pro\Scripts\kicad-mcp-pro.exe`
- Args: `serve --transport stdio --profile analysis`
- Workspace root: `<LOCAL_CHECKOUT>\KICAD_ENGINE`
- Project dir: `04_KICAD_PROJECTS\active`
- Output dir: `05_OUTPUTS\kicad-mcp-pro-analysis`
- KiCad CLI: `C:\Program Files\KiCad\9.0\bin\kicad-cli.exe`

MCP is analysis/safe mode only. Do not enable write, destructive, or manufacturing/export authority unless LJ explicitly approves it for a specific active project after backups and verification plans are confirmed. Do not enable parallel MCP calls until shared KiCad project-state safety is validated.

No real project edits are allowed through MCP until active project and backup gates are satisfied.

## 9. Verification scripts

Scripts are in `03_TOOLS\scripts`. They should use quoted paths, fail safely, create timestamped outputs, write logs, avoid deleting source files, and return non-zero exit codes on failure.

### `find_kicad_project_files.ps1`

- Purpose: Inventory KiCad project files under a project path.
- When to run: At the start of review or verification to identify `.kicad_pro`, `.kicad_sch`, `.kicad_pcb`, symbols, footprints, and related files.
- Creates: Timestamped report/log output.
- Must not do: Modify project files or generate fabrication outputs.

### `backup_kicad_project.ps1`

- Purpose: Copy source project files and local libraries before edits.
- When to run: Before automated edits or verification workflows that need a pre-edit snapshot.
- Creates: `99_BACKUPS\pre_codex_edits\<project-id>_<timestamp>`.
- Must not do: Delete old backups or modify source project files.

### `run_erc.ps1`

- Purpose: Run schematic ERC with `kicad-cli`.
- When to run: After schematic changes and during verification.
- Creates: Timestamped ERC report/log under project reports or output folders.
- Must not do: Change the schematic or mark results fabrication-ready.

### `run_drc.ps1`

- Purpose: Run PCB DRC with `kicad-cli`.
- When to run: After PCB changes and during verification.
- Creates: Timestamped DRC report/log under project reports or output folders.
- Must not do: Change the board or mark results fabrication-ready.

### `export_bom.ps1`

- Purpose: Export a BOM for review.
- When to run: During verification or documentation preparation.
- Creates: Timestamped BOM output/reports.
- Must not do: Treat the BOM as final without component, datasheet, sourcing, and footprint review.

### `export_gerbers.ps1`

- Purpose: Export Gerber files for review.
- When to run: Only after appropriate checks, usually through `full_verify_project.ps1`.
- Creates: Timestamped `NOT_FINAL` Gerber output folders.
- Must not do: Overwrite older Gerbers or label output as final fabrication release.

### `export_drill.ps1`

- Purpose: Export drill files for review.
- When to run: Only after appropriate checks, usually through `full_verify_project.ps1`.
- Creates: Timestamped `NOT_FINAL` drill output folders.
- Must not do: Overwrite older drill files or label output as final fabrication release.

### `export_step.ps1`

- Purpose: Export STEP model for mechanical/visual review.
- When to run: During mechanical review or full verification.
- Creates: Timestamped STEP output.
- Must not do: Treat STEP output as proof of enclosure fit without human review.

### `full_verify_project.ps1`

- Purpose: Run the full gated verification pipeline.
- When to run: For a selected active project after backups are confirmed.
- Creates: Backup, ERC, DRC, BOM, Gerber, drill, STEP logs/outputs, and a verification summary markdown file.
- Must not do: Create final manufacturing output. Gerber/drill/STEP exports are gated behind passing ERC/DRC unless explicitly overridden for review-only testing.

### `kicad_engine_health_check.ps1`

- Purpose: Check workspace folders, startup files, prompts, memory/history, repos, tool statuses, runtime tools, scripts, backups, and outputs.
- When to run: After setup changes or before important KiCad sessions.
- Creates: `03_TOOLS\tool_logs\KICAD_ENGINE_HEALTH_CHECK.md`.
- Must not do: Install tools, delete files, or modify KiCad projects.

### `new_kicad_project_workspace.ps1`

- Purpose: Create a new standard KiCad project workspace under `04_KICAD_PROJECTS\active`.
- When to run: After project name and minimum requirements are confirmed.
- Creates: Project folder, template subfolders, project README/AGENTS files, project memory folder, project history folder, and `PROJECT_INDEX.md` updates.
- Must not do: Overwrite an existing project or update `CURRENT_PROJECT.md` unless explicitly requested by the workflow/user.

## 10. Project workflow

New projects go in:

`04_KICAD_PROJECTS\active`

Standard templates live in:

`04_KICAD_PROJECTS\templates`

Finished PCB reference review templates:

- `04_KICAD_PROJECTS\templates\FINISHED_PCB_REVIEW_CHECKLIST.md`
- `04_KICAD_PROJECTS\templates\REFERENCE_PROJECT_FOLDER_STANDARD.md`

Before creating a real project, use:

`.prompts\codex\02_CREATE_NEW_PROJECT_WORKSPACE.md`

Legacy prompt path, if still present:

`.codex\prompts\CREATE_REAL_KICAD_PROJECT_FROM_REQUIREMENTS.md`

Codex should collect requirements, create only the workspace and requirements file first, then wait before beginning schematic or PCB design.

Reference finished PCBs may exist in a user-local optional folder:

`99_01 Finished PCBs`

Codex should copy or review finished PCBs as reference projects before learning from them. Never edit original finished PCB files directly unless LJ explicitly approves a direct finished-folder repair/review task and Codex creates a snapshot first.

## 11. Finished PCB reference library

Finished PCB reference library, if present:

`99_01 Finished PCBs`

Historical finished PCB reference:

`99_01 Finished PCBs\COMMAND LINK`

Status:

- Finished Fiverr-verified PCB reference, per user-provided context.
- Indexed read-only on 2026-04-30.
- Inventory report: `02_HISTORY\design_reviews\COMMAND_LINK_FINISHED_PCB_INVENTORY.md`.
- Default rule: do not edit originals directly. If edits or experiments are required, create a copied review workspace first unless LJ explicitly approves a direct finished-folder repair/re-export task.
- Direct approved repair/review/re-export session completed on 2026-04-30 after LJ explicitly approved direct work in the finished folder. Reports:
  - `02_HISTORY\design_reviews\COMMAND_LINK_DIRECT_EDIT_REVIEW.md`
  - `02_HISTORY\erc_drc_reports\COMMAND_LINK_DIRECT_EDIT_ERC_DRC_REPORT.md`
  - `02_HISTORY\sessions\COMMAND_LINK_DIRECT_EDIT_SESSION.md`
- Direct session snapshot: `99_BACKUPS\project_snapshots\COMMAND_LINK_DIRECT_EDIT_APPROVED_20260430_203134`
- Direct session result: ERC passed cleanly; DRC still failed with 44 remaining violations. New exports are in `Codex Review Outputs\20260430_203134\new_outputs_NOT_FINAL` and are not fabrication-ready.
- Direct DRC continuation completed on 2026-04-30. Reports:
  - `02_HISTORY\design_reviews\COMMAND_LINK_DRC_CONTINUATION_REVIEW.md`
  - `02_HISTORY\erc_drc_reports\COMMAND_LINK_DRC_CONTINUATION_ERC_DRC_REPORT.md`
  - `02_HISTORY\sessions\COMMAND_LINK_DRC_CONTINUATION_SESSION.md`
  - `02_HISTORY\command_logs\COMMAND_LINK_DRC_CONTINUATION_COMMANDS.md`
- Continuation snapshot: `99_BACKUPS\project_snapshots\COMMAND_LINK_DRC_CONTINUATION_20260430_210726`
- Continuation result: ERC passed cleanly and DRC passed with 0 violations after resolving footprint-library mismatch warnings, R2/U3/U4 starved thermals, and the C3/C9 courtyard overlap. New exports are in `Codex Review Outputs\20260430_210726\new_outputs_NOT_FINAL` and remain `NOT_FINAL`.

Copied review workspace:

- `04_KICAD_PROJECTS\active\COMMAND_LINK_VERIFIED_REFERENCE`
- Created for read-only Codex review and learning.
- Not an active design revision.
- Any design changes must be made in a new revision copy, not in the original finished PCB folder or this reference copy.
- Latest read-only review: `02_HISTORY\design_reviews\COMMAND_LINK_READ_ONLY_REVIEW.md`.
- Latest ERC/DRC review: `02_HISTORY\erc_drc_reports\COMMAND_LINK_ERC_DRC_REVIEW.md`.
- Local review outcome: ERC completed with 2 warnings and DRC completed with 46 violations in the current KiCad environment, so the reference copy is not a clean local verification baseline.

Reference-derived learning artifacts:

- `04_KICAD_PROJECTS\templates\FINISHED_PCB_REVIEW_CHECKLIST.md` captures the standard non-destructive finished-PCB review flow.
- `04_KICAD_PROJECTS\templates\REFERENCE_PROJECT_FOLDER_STANDARD.md` defines how copied reference workspaces should be structured.
- `01_MEMORY\DESIGN_RULES_MEMORY.md`, `01_MEMORY\COMPONENT_PREFERENCES.md`, and `01_MEMORY\FAB_HOUSE_PREFERENCES.md` include COMMAND LINK lessons only where the read-only review provided evidence.
- Observed COMMAND LINK components are recorded as observed/unverified, not as approved preferred parts.
- Observed COMMAND LINK fabrication package structure is recorded as a reference pattern, not as a board-house default.

Observed `COMMAND LINK` reference contents include:

- `COMMAND LINK DRAFT.kicad_pro`
- `COMMAND LINK DRAFT.kicad_sch`
- `COMMAND LINK DRAFT.kicad_pcb`
- `COMMAND LINK BOM.csv`
- `COMMAND LINK DRAFT.pdf`
- `COMMAND LINK DRAFT.stl`
- `Fabrication files`
- `Fabrication files.zip`
- `pick and place file`
- `pick and place file.zip`
- `COMMAND LINK DRAFT-backups`
- Gerber-style files under the fabrication folder.
- Drill files under the fabrication folder.
- Pick-and-place files under the pick-and-place folder.
- `fp-info-cache`
- `COMMAND LINK DRAFT.kicad_sch-bak`

Inventory notes:

- Standalone `.drl`, `.xln`, or `.txt` Excellon drill files were not observed in the visible folder tree; drill data appears to be present as `COMMAND LINK DRAFT-PTH-drl.gbr` and `COMMAND LINK DRAFT-NPTH-drl.gbr`.
- The 2026-04-30 direct repair/re-export session generated standalone Excellon PTH/NPTH `.drl` files under `Codex Review Outputs\20260430_203134\new_outputs_NOT_FINAL\drill`; these are `NOT_FINAL`.
- ERC is now clean in the direct folder after the local U2 library and `CAN_P` label fix.
- DRC is now clean in the direct folder after the 2026-04-30 continuation.
- The continuation created `COMMAND_LINK_EMBEDDED.pretty` and updated 40 board footprint references to project-local exact embedded footprint copies. This preserves physical geometry but changes PNP `Package` metadata for 37 placed parts; ref, side, X/Y, and rotation are unchanged.
- R2/U3/U4 starved thermals were cleared by setting the affected GND pad 2 local zone connection to full and refilling zones.
- The C3/C9 courtyard overlap was cleared by adjusting only the opposing `F.CrtYd` edges; placement and routing were not changed.
- The latest direct NOT_FINAL package is `Codex Review Outputs\20260430_210726\new_outputs_NOT_FINAL`. It includes Gerbers, Excellon drills, BOM, PNP, PDFs, STEP, and copied ERC/DRC reports.
- STEP export still reports missing 3D models for J2, J3, J4, and L1.
- Final fabrication readiness audit completed on 2026-04-30:
  - Report: `02_HISTORY\design_reviews\COMMAND_LINK_FINAL_FAB_READINESS_AUDIT.md`
  - Session: `02_HISTORY\sessions\COMMAND_LINK_FINAL_FAB_READINESS_AUDIT_SESSION.md`
  - Command log: `02_HISTORY\command_logs\COMMAND_LINK_FINAL_FAB_READINESS_AUDIT_COMMANDS.md`
  - Manifest: `99_01 Finished PCBs\COMMAND LINK\Codex Review Outputs\20260430_210726\new_outputs_NOT_FINAL\PACKAGE_MANIFEST.md`
  - Classification: `HUMAN_REVIEW_REQUIRED`
  - Reason: ERC/DRC are clean and package files are present, but connector pinout/orientation, polarity/orientation, manual assembly treatment for J2/J3/J4, PNP package metadata, plated mounting-hole intent, and missing 3D models require human confirmation.
- Archives were not extracted during indexing.

Expected files for finished PCB references:

- `.kicad_pro`
- `.kicad_sch`
- `.kicad_pcb`
- BOM CSV
- Fabrication files
- Gerbers
- Drill files
- Pick-and-place files
- PDF
- STL
- Backups

These are references. They are not active workspaces unless copied into a safe review location or explicitly selected by LJ.

## 12. Rules for reviewing finished PCB projects

- Do not edit the original finished PCB folder.
- Create review reports only, normally under `02_HISTORY\design_reviews` or `02_HISTORY\fabrication_reviews`.
- Compare KiCad source files to fabrication outputs.
- Check BOM, pick-and-place, Gerbers, drill, schematic, PCB, and 3D/STL if present.
- Document reusable design patterns separately from one-off observations.
- Update `01_MEMORY` only with durable lessons that should influence future designs.
- Record commands and review evidence in `02_HISTORY`.
- Do not treat a previous finished PCB as automatically correct or safe for reuse.
- Use `04_KICAD_PROJECTS\templates\FINISHED_PCB_REVIEW_CHECKLIST.md` for future finished-PCB reviews.
- Use `04_KICAD_PROJECTS\templates\REFERENCE_PROJECT_FOLDER_STANDARD.md` when creating copied reference workspaces.

## 13. What ChatGPT should ask the user before real design work

Before real schematic or PCB design work, ask for or confirm:

- Project name.
- Board purpose.
- Input voltage.
- Output voltages.
- Maximum current.
- MCU or processor requirements.
- Communication buses such as CAN, LIN, UART, I2C, SPI, USB, or none.
- Connectors.
- Enclosure or mechanical limits.
- Mounting hole requirements.
- Environment such as vehicle, outdoor, waterproof, vibration, temperature, or benign indoor use.
- Preferred parts.
- Parts to avoid.
- Fabrication house.
- Layer count.
- Board size.
- Special DFM rules.
- Design scope: schematic-only, PCB-only, or full design.

Do not begin design from placeholders. If requirements are unknown, write them as `Unknown` only after the user confirms that is acceptable for the initial workspace.

## 14. Known current setup status

Structure expansion update:

- Created on 2026-05-02.
- Structure standard: `00_CODEX_START\STRUCTURE_STANDARD.md`.
- Folder routing rules: `00_CODEX_START\FOLDER_ROUTING_RULES.md`.
- Repository structure index: `00_CODEX_START\REPO_STRUCTURE_INDEX.md`.
- Structure audit: `02_HISTORY\design_reviews\STRUCTURE_EXPANSION_AUDIT.md`.
- Current classification: `STRUCTURE_EXPANSION_COMPLETE_FOR_REQUEST`.
- Important limitation: the expanded top-level folder scaffold does not by itself prove public-release readiness or production completeness.

Product vision and architecture update:

- Created on 2026-05-02.
- Vision: `00_CODEX_START\PRODUCT_VISION.md`.
- Architecture: `00_CODEX_START\KICAD_ENGINE_ARCHITECTURE.md`.
- Product gap audit: `02_HISTORY\design_reviews\KICAD_ENGINE_PRODUCT_GAP_AUDIT.md`.
- Key audit finding: the repo has a strong safety/workflow foundation, but public-release readiness still needs path portability, public README/license/release hygiene, setup packaging, datasheet/component/footprint schemas, VS Code/Claude integration files, and demonstrated public sample workflows. The datasheet library scaffold now exists, but its contents still need source/revision/copyright curation.

Final setup audit:

- File: `02_HISTORY\design_reviews\KICAD_ENGINE_FINAL_SETUP_AUDIT.md`
- Readiness score: 88 / 100 as of 2026-04-30.

Final production structure audit:

- File: `02_HISTORY\design_reviews\FINAL_PRODUCTION_STRUCTURE_AUDIT.md`
- Scorecard: `05_OUTPUTS\release_readiness\FINAL_STRUCTURE_SCORECARD.md`
- Classification: `INTERNAL_ALPHA_READY` as of 2026-05-03.
- Main blockers before public release: dependency/environment exclusion, PDF redistribution review, generated/reference artifact cleanup, old command-log scrubbing, Git worktree verification, installer platform smoke tests, and verified data maturity.

Latest health check:

- Command: `python health_check.py --repo-root . --no-write`
- Latest observed result on 2026-05-03: PASS 131, WARN 0, FAIL 0.
- Historical report file: `03_TOOLS\tool_logs\KICAD_ENGINE_HEALTH_CHECK.md`
- Blockers: None.

Current installed/available basics:

- KiCad: Installed at `C:\Program Files\KiCad\9.0\bin\kicad.exe`.
- `kicad-cli`: Installed on user PATH, version 9.0.7.
- Python: Available on user PATH, Python 3.12.10.
- pip: Use `python -m pip`; direct `pip.exe` is not confirmed in the Scripts folder.
- Node: v22.15.0.
- npm: 10.9.2.
- Git: 2.52.0.windows.1.
- PowerShell: 5.1.26100.8115.
- Codex CLI: 0.80.0.

Warnings:

- Playwright batch expansion completed in dry-run-only mode on 2026-05-03. Seven batch reports under `31_PLAYWRIGHT_RESEARCH_PIPELINE\reports\BATCH_*` cover 72 source-link-only targets across ESP32, STM32, PIC/AVR, USB-C connectors, CAN, power/protection, RF connectors, antennas, and board hardware. Live browser capture is still blocked because the local Node environment does not have Playwright installed. All records remain `UNVERIFIED` or `SOURCE_LINK_ONLY`; no PDFs, credentials, supplier API calls, or KiCad design files were touched.
- `KiCAD-MCP-Server` is cloned but not installed.
- KiBot is installed but not production-tested on a real project.
- InteractiveHtmlBom is installed/help-tested but not project-tested.
- PcbDraw is installed/help-tested but not project-tested.
- KiCanvas is isolated-build-tested but not project-tested.
- Windows GUI automation packages are installed/import-checked and have been used once for safety-gated native schematic annotation on `ESP32_CSI_WIFI_NODE`. This verifies annotation/save/GUI ERC under gates only; it does not approve general GUI control, PCB work, routing, or manufacturing outputs.
- Windows GUI helper repos are cloned only for reference. FlaUI, FlaUInspect, AutoHotkey, and SikuliX1 have not been built, installed, or used to control KiCad.
- KiCad GUI discovery filtering was fixed on 2026-04-30. Title-only matches such as VS Code with `KICAD_ENGINE` are low-confidence only and cannot be inspected, screenshotted, or controlled.
- Latest KiCad GUI control test with KiCad manually open successfully performed native schematic annotation on `ESP32_CSI_WIFI_NODE` after exact path detection, backup, screenshots, GUI save, GUI ERC, and CLI ERC. A dry-run-first closed-state auto-open workflow now exists, but live open-from-closed-state still needs explicit future testing. Future GUI control must remain task-specific, safety-gated, logged, and limited to approved native actions.
- Linux/headless automation is documentation and starter scripts only. No WSL setup, Linux install, or Linux KiCad automation run has been performed.
- Control-plane rules were added so future agents prefer common CLI/API/MCP project intelligence first, use Windows GUI hands/eyes only when necessary, and reserve Linux/headless/CI for repeatable validation.

Clean sample status:

- `CLEAN_KICAD_PASSING_SAMPLE` validated the full verification success path on a disposable sample.
- Outputs from samples are `NOT_FINAL` and must not be used for manufacturing.

Current project status:

- `00_CODEX_START\CURRENT_PROJECT.md` should be checked every session.
- If it says `NONE`, there is no active real project.

Next recommended real-project step:

- Use `.codex\prompts\CREATE_REAL_KICAD_PROJECT_FROM_REQUIREMENTS.md`.
- Create the workspace and requirements file only.
- Do not begin schematic or PCB design until requirements are complete enough and LJ explicitly proceeds.

## 15. Do not do these things

- Do not edit original finished PCB files unless LJ explicitly approves a direct finished-folder repair/review task and Codex creates a snapshot first.
- Do not delete outputs.
- Do not overwrite Gerbers.
- Do not overwrite older backups.
- Do not treat AI review as fabrication approval.
- Do not store secrets in memory, history, prompts, configs, or reports.
- Do not modify third-party repos casually.
- Do not pull third-party repos unless requested.
- Do not enable destructive MCP profiles casually.
- Do not give MCP servers write or manufacturing/export authority without explicit approval.
- Do not edit KiCad design files when active project is `NONE`.
- Do not generate final fabrication outputs unless ERC, DRC, BOM, footprint, netlist, datasheet, connector, polarity/orientation, power, mechanical, and visual review gates are complete.
- Do not create schematics, select symbols, select footprints, route PCBs, prepare manufacturing outputs, or publish benchmark comparisons from memory; use `09_ACCURACY_ENGINE`, read relevant `10_KNOWLEDGE_BASE` guidance, read relevant `11_LIBRARY_FACTORY` standards, check relevant `12_REFERENCE_DESIGN_LIBRARY` records when using examples, use `13_PART_INGESTION` for new-part stubs, read `14_LAYOUT_AUTOMATION` before placement/routing assistance, read `15_BENCHMARKS` before benchmark scoring or comparison claims, and mark missing evidence explicitly.
- Do not choose GUI automation when CLI/API/MCP inspection can complete the task.
- Do not write to original project sources when a copied project workspace is safer.

## 16. How to update this file

Update `README_GPT.md` whenever any of these change:

- Root folder structure.
- Codex startup rules.
- `AGENTS.md`.
- `00_CODEX_START` files.
- `00_CODEX_START\CONTROL_PLANES.md`.
- Tool installations or tool status.
- MCP configuration.
- Verification scripts.
- Project workflow.
- Memory/history rules.
- AI quality/scoring rules.
- Current finished PCB reference library.
- Health-check or final-audit status.
- Known blockers or readiness score.

When updating this file:

1. Read `AGENTS.md` and relevant `00_CODEX_START` files first.
2. Back up the existing `README_GPT.md` to `99_BACKUPS\pre_codex_edits`.
3. Preserve useful existing context.
4. Do not store secrets.
5. Keep `FOR CHAT GPT.MD` synchronized.
6. Write a session log under `02_HISTORY\sessions`.

`FOR CHAT GPT.MD` is the short handoff file for ChatGPT/Codex. Codex must update it whenever the KiCad Engine repo changes in a meaningful way, including changes to folder structure, startup rules, memory/history systems, tool repos, installed tools, MCP configuration, verification scripts, project templates, active project index, finished PCB reference library, review workflow, health status, known blockers, or readiness score.

If Codex changes repo structure or workflows, update both `README_GPT.md` and `FOR CHAT GPT.MD`. If Codex only changes a KiCad project but not engine structure, update project memory/history and update `FOR CHAT GPT.MD` only if the change affects future ChatGPT/Codex context.

