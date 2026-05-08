# FOR CHAT GPT â€” KiCad Engine Handoff

## Repo path

Current inspected workspace path:

`C:\Users\LJ\GitHub\KICAD_ENGINE`

Some historical docs and tool configs still reference an older non-GitHub checkout path. Treat older absolute paths as historical unless a current task explicitly selects that path and it exists. For new work in this checkout, use repo-relative paths or `C:\Users\LJ\GitHub\KICAD_ENGINE`.

## Latest GitHub repo indexing layer - 2026-05-08

The repo now has a dedicated GitHub-facing navigation and status layer so future agents and humans do not need to infer structure from internal-only startup files alone.

- root entry docs now include `README.md`, `START_HERE.md`, `REPO_INDEX.md`, `FOLDER_MAP.md`, `PROJECTS_INDEX.md`, `TOOLS_INDEX.md`, `WORKFLOWS_INDEX.md`, `CURRENT_STATUS.md`, `PUBLIC_RELEASE_STATUS.md`, `CONTRIBUTING.md`, and `SECURITY.md`
- GitHub-specific metadata now includes `.github/README.md`, issue templates, and a pull-request template
- startup-facing GitHub navigation now lives in `00_CODEX_START/GITHUB_REPO_INDEX.md`, `00_CODEX_START/GITHUB_NAVIGATION.md`, and `00_CODEX_START/CURRENT_GITHUB_STATUS.md`
- folder-local indexes now exist under `03_TOOLS/`, `04_KICAD_PROJECTS/`, `09_ACCURACY_ENGINE/`, `14_LAYOUT_AUTOMATION/`, `34_PCB_LAYOUT_SANDBOX/`, `05_OUTPUTS/`, `01_MEMORY/`, and `02_HISTORY/`
- the active project README at `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/README.md` now reflects the live PCB state instead of the old pre-PCB planning claim
- the root docs intentionally say the repo is `PRIVATE`, `EXPERIMENTAL_INTERNAL_ALPHA`, and not public-release-ready; they also explicitly say `ESP32_CSI_WIFI_NODE` is not fabrication-ready
- future repo-navigation or release-status updates should keep this GitHub-facing layer consistent with `05_OUTPUTS/release_readiness/`, `CURRENT_PROJECT_STATE.md`, and `CURRENT_BLOCKERS.md`

## Latest GitHub repo indexing tightening pass - 2026-05-08

The GitHub-facing navigation layer was tightened a second time so the root docs are more useful on first open:

- root `TOOLS_INDEX.md` now includes concrete command examples plus read-only vs edit-scope notes
- root `WORKFLOWS_INDEX.md` now explicitly includes live-project-state, stale-report-reconciliation, and trace-by-trace-audit workflows
- root `CURRENT_STATUS.md` now explicitly lists remaining PCB blockers and public-release blockers
- `00_CODEX_START/GITHUB_NAVIGATION.md` now has a dedicated `Start Here For Routing Work` section
- future GitHub-facing doc updates should preserve that level of specificity instead of collapsing back to pointer-only summaries

## Latest task-type execution contract hardening - 2026-05-08

KiCad Engine now has a dedicated execution-contract layer under `03_TOOLS\scripts\execution_contract` to stop false completion of edit-required PCB tasks:

- every meaningful run must declare exactly one task type
- supported task types are `DOCS_ONLY`, `AUDIT_ONLY`, `LIVE_STATE_RECONCILE`, `PLACEMENT_EDIT_REQUIRED`, `ROUTING_EDIT_REQUIRED`, `PCB_EDIT_REQUIRED`, and `GITHUB_DOCS_ONLY`
- non-edit task types may not change `.kicad_sch`, `.kicad_pcb`, or `.kicad_pro`
- edit-required task types must prove backup creation, `.kicad_pcb` hash evidence, DRC evidence, and visual-export attempt
- `ROUTING_EDIT_REQUIRED` also requires unrouted/unconnected before/after counts plus `TRACE_CHANGE_LOG` proof
- `PLACEMENT_EDIT_REQUIRED` also requires placement-report proof
- `PCB_EDIT_REQUIRED` may end `NO_DESIGN_CHANGE_NEEDED` only when that outcome is explicit in the contract
- if an edit-required run ends with only docs/reports and no real engineering artifact change, the required final status is `EDIT_REQUIRED_FAILED_NO_ENGINEERING_ARTIFACT_CHANGE`
- future startup, workflow, and closeout changes must keep `AGENTS.md`, `00_CODEX_START`, and this handoff aligned with the execution-contract rules

## Latest ESP32_CSI_WIFI_NODE final PCB visual review packet - 2026-05-08

The active `ESP32_CSI_WIFI_NODE` board now has a dedicated LJ visual review packet built from the current live board hash:

- live PCB hash used by the packet: `A90967ABC127674F7008562AAEE46744456F2421550E4B64AD71E91B5D3CF697`
- packet files:
  - `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\FINAL_PCB_VISUAL_REVIEW_PACKET.md`
  - `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\LJ_FINAL_PCB_REVIEW_CHECKLIST.md`
  - `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\pcb_visual\FINAL_PCB_REVIEW_PACKAGE.md`
- fresh visual assets now include current full-board top and bottom renders plus deterministic close-up crops for USB-C, USB data area, ESP32 module, antenna keepout, power input, regulator/power path, GND zones, test pads, mounting holes, and dense routing
- direct `kicad-cli pcb render` camera-pivot close-ups were not reliable enough for the final packet; future top-down review packets should prefer fresh full-board renders plus deterministic coordinate crops
- current live electrical state for the packet: `0` DRC violations, `17` unconnected items, and explicit unrouted nets `/DM_C`, `/DM_E`, `/DP_C`, `/DP_E`
- packet status: `READY_FOR_LJ_PCB_VISUAL_REVIEW`
- board status: `NOT_READY_NEEDS_MORE_PCB_REPAIR`

## Latest ESP32_CSI_WIFI_NODE live PCB repair - 2026-05-08

The active `ESP32_CSI_WIFI_NODE` board now has a verified live repair pass on the real files:

- real `.kicad_pcb` edited and saved
- real `.kicad_pro` adjusted to align `min_through_hole_diameter` with the intentional `U2 pad 41` thermal-via drill
- current live board: `43` footprints, `24` tracks, `2` vias, `2` GND zones
- current live DRC: `0` violations, `65` unconnected items
- current detectable unrouted nets: `15`
- routing phase 8 remains blocked by live connectivity incompleteness, not by stale `NO_PCB` claims or the old `U2` drill-rule mismatch

## Latest ESP32_CSI_WIFI_NODE live critical routing - 2026-05-08

The active `ESP32_CSI_WIFI_NODE` board now has a second real live PCB edit pass after the repair pass:

- real `.kicad_pcb` edited and saved again
- live PCB hash changed from `1944B6DDFA7B233B8C231F5441D68B827FA3416B5C0B58A3004DE5C63C797FAC` to `D147FD1FFEF47F62B229561052B08C7432EFC549B7752DC7279ECE96E6C6B6A5`
- current live board: `43` footprints, `40` tracks, `25` vias, `2` GND zones
- current live DRC: `0` violations, `49` unconnected items
- accepted live routing in this pass: `+3V3` is now fully connected and selected `GND` stitching vias were added
- deferred after copied-board DRC rehearsal: `/BOOT0`, `/ESP_EN`, and the `TP1` `/+5V_PROTECTED` spur
- next correct PCB action is a copied-board control-net reroute study for `/BOOT0` and `/ESP_EN`, not broad remaining-net routing

## Latest ESP32_CSI_WIFI_NODE routing work prep - 2026-05-08

Routing prep for the next real live PCB pass now has a mandatory project-local log/rollback packet:

- backup created: `99_BACKUPS\pre_codex_edits\20260508_091428_ESP32_CSI_WIFI_NODE_routing_work_prep`
- routing work folder created: `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\routing_work\20260508_091428`
- live PCB unchanged in this prep task; current hash remains `5E6486A2C188B68207C9FF4692618AE81BF322355ACAEE686146EF075330C2F6`
- current live baseline captured in the prep packet: `53` tracks, `29` vias, `10` detectable unrouted nets, DRC `FAIL` with `0` violations and `44` unconnected items
- future live routing passes on this project must append to `ROUTING_MASTER_LOG.md`, `TRACE_CHANGE_LOG.md`, `COMPONENT_MOVE_LOG.md`, `DRC_RUN_LOG.md`, `ROUTING_DECISION_LOG.md`, and `BEFORE_AFTER_HASH_LOG.md`
- exact next routing batch remains copied-board rehearsal for `/BOOT0`, `/ESP_EN`, `/U0RXD`, and `TP1 /+5V_PROTECTED`, then `/CC1`, `/CC2`, and `/SHIELD` only if the first batch stays clean

## Latest ESP32_CSI_WIFI_NODE batch 01 DRC and GND repair - 2026-05-08

The active `ESP32_CSI_WIFI_NODE` board now has another verified real PCB edit pass:

- live PCB hash changed from `5E6486A2C188B68207C9FF4692618AE81BF322355ACAEE686146EF075330C2F6` to `1AA99163F07EC867B98461F88990D059F46ACCBFB1CA4E91E33F9FD49B792489`
- `U2 pad 41` did not need a new repair in this pass; it was already fixed on the live revision
- the actual live change was to both existing `GND` zones: `thermal` pad connection -> `full` pad connection
- post-edit live DRC remains `0` violations and improved from `44` to `27` unconnected items
- remaining detectable unrouted nets are still `10`, so routing batch 2 may not start yet
- copied-board DRC rehearsals for future real-board edits must include the matching `.kicad_pro`, or they can falsely resurrect old drill-rule blockers

## Latest PCB layout sandbox layer - 2026-05-07

`34_PCB_LAYOUT_SANDBOX` is now the mandatory pre-PCB-edit layout-reasoning layer.

Before editing a real `.kicad_pcb`, future agents must:

- generate or review at least 3 layout variants
- include board outline, dimensions, fixed mechanical parts, connector orientation, antenna keepout, power path, USB/data path, routing projection, and risk score for each variant
- justify one selected variant before real PCB edits start
- record sandbox auto-approval status `AUTO_APPROVED_FOR_PCB_WORK` in the active project's `reports\PCB_LAYOUT_SANDBOX_GATE_STATUS.md`

Real PCB update from schematic and real PCB placement are blocked unless both of these files are exactly `PASS`:

- `reports\SCHEMATIC_TO_PCB_GATE_STATUS.md`
- `reports\PCB_LAYOUT_SANDBOX_GATE_STATUS.md`

This layer exists to block avoidable layout mistakes such as wrong-facing barrel jacks, USB-C not on the board edge, blocked ESP32 antenna areas, outline choice without mechanical reasoning, and routing started after bad placement.

Generic LJ approval is no longer required when the sandbox can prove the selected layout variant passes the objective checks.

## Latest auto PCB start workflow - 2026-05-07

KiCad Engine now has an explicit auto-start handoff from sandbox approval into real PCB work.

Authoritative files:

- `09_ACCURACY_ENGINE\workflows\AUTO_PCB_START_WORKFLOW.md`
- `09_ACCURACY_ENGINE\checklists\AUTO_PCB_START_CHECKLIST.md`
- `34_PCB_LAYOUT_SANDBOX\PCB_WORK_AUTO_START_RULES.md`
- `34_PCB_LAYOUT_SANDBOX\templates\AUTO_PCB_START_REPORT_TEMPLATE.md`

When all preconditions are satisfied, Codex/Claude may automatically continue to:

- update PCB from schematic
- create or update `.kicad_pcb`
- apply board outline
- place fixed mechanical components
- place main component groups
- run DRC
- export placement/mechanical visual review evidence

Required preconditions:

- `SCHEMATIC_TO_PCB_GATE_STATUS.md` exact `PASS`
- footprint/package gate `PASS` or `SAFE_CANDIDATE_WITH_EVIDENCE`
- `PCB_LAYOUT_SANDBOX_GATE_STATUS.md` exact `PASS`
- selected layout plan exists
- auto-approval report says `AUTO_APPROVED_FOR_PCB_WORK`
- board dimensions exist
- connector-orientation plan exists
- antenna-keepout plan exists when RF is present
- routing-feasibility plan exists

If any precondition fails, stop with `AUTO_PCB_START_BLOCKED` and list exact blockers.

## Latest auto placement engine - 2026-05-07

KiCad Engine now has a deterministic placement-planning layer under `14_LAYOUT_AUTOMATION`.

Authoritative files:

- `14_LAYOUT_AUTOMATION\AUTO_PLACEMENT_ENGINE.md`
- `14_LAYOUT_AUTOMATION\PLACEMENT_CONSTRAINTS_SCHEMA.md`
- `14_LAYOUT_AUTOMATION\PLACEMENT_GROUPING_RULES.md`
- `14_LAYOUT_AUTOMATION\FIXED_MECHANICAL_PLACEMENT_RULES.md`
- `14_LAYOUT_AUTOMATION\POWER_PATH_PLACEMENT_RULES.md`
- `14_LAYOUT_AUTOMATION\USB_PLACEMENT_RULES.md`
- `14_LAYOUT_AUTOMATION\RF_ANTENNA_PLACEMENT_RULES.md`
- `14_LAYOUT_AUTOMATION\TEST_PAD_PLACEMENT_RULES.md`
- `14_LAYOUT_AUTOMATION\PLACEMENT_DRC_PRECHECK_RULES.md`
- `14_LAYOUT_AUTOMATION\scripts\README.md`

Core placement order:

1. board outline
2. mounting holes
3. edge connectors
4. RF module and keepout
5. power input path
6. regulator/power components
7. USB/ESD/series/CC parts
8. MCU support passives
9. reset/boot
10. LEDs
11. test pads
12. low-risk passives

Core rules:

- USB-C and barrel jack/input connectors are fixed mechanical parts
- ESP32 antenna keepout is placed before nearby parts
- power path stays in current-flow order
- USB ESD stays near the connector
- decoupling stays near IC power pins
- courtyard overlap is failure
- board-edge clearance must be checked
- placement is not approved if routing becomes obviously impossible

This is a planning and precheck engine only. It does not prove final placement quality or fabrication readiness.

## Latest real-board routing bridge - 2026-05-07

KiCad Engine now has a read-only bridge from a real copied `.kicad_pcb` into the routing-engine schema and audit flow.

Authoritative files:

- `14_LAYOUT_AUTOMATION\scripts\extract_kicad_pcb_to_routing_schema.py`
- `14_LAYOUT_AUTOMATION\scripts\extract_kicad_nets_pads.py`
- `14_LAYOUT_AUTOMATION\scripts\extract_kicad_tracks_vias.py`
- `14_LAYOUT_AUTOMATION\scripts\extract_kicad_zones_keepouts.py`
- `14_LAYOUT_AUTOMATION\scripts\extract_kicad_net_classes.py`
- `14_LAYOUT_AUTOMATION\scripts\run_real_board_routing_audit.py`
- `14_LAYOUT_AUTOMATION\real_board_tests\README.md`
- `14_LAYOUT_AUTOMATION\reports\REAL_KICAD_BOARD_EXTRACTION_TEST_REPORT.md`

This bridge:

- reads a copied `.kicad_pcb` in read-only mode
- re-enters KiCad's bundled Python when `pcbnew` is not available in the default interpreter
- extracts board outline, footprints, pads, nets, tracks, vias, zones, keepouts, net classes, and connectivity summary into `ROUTING_INPUT_SCHEMA.md`
- runs copied-board `kicad-cli pcb drc --format json`
- feeds the extracted JSON into the existing routing plan, keepout, unrouted-net, trace-audit, and routing-score scripts

Current status:

- copied-board live routing audit: `READY`
- active-project routing: `NOT READY`

Current remaining bridge limitations:

- per-net ratsnest extraction is still `NOT_EXTRACTED`
- via intent / engineering reason is still `NOT_EXTRACTED`
- keepout detection trusts explicit rule areas and does not infer every possible layout restriction
- routing-plan scoring is still strict enough to block boards that extract cleanly but lack downstream planning evidence

## Latest auto routing engine - 2026-05-07

KiCad Engine now has a deterministic routing-planning and routing-audit layer under `14_LAYOUT_AUTOMATION`.

Authoritative files:

- `14_LAYOUT_AUTOMATION\AUTO_ROUTING_ENGINE.md`
- `14_LAYOUT_AUTOMATION\ROUTING_INPUT_SCHEMA.md`
- `14_LAYOUT_AUTOMATION\ROUTING_OUTPUT_SCHEMA.md`
- `14_LAYOUT_AUTOMATION\TRACE_AUDIT_SCHEMA.md`
- `14_LAYOUT_AUTOMATION\NET_CLASS_SCHEMA.md`
- `14_LAYOUT_AUTOMATION\TRACE_PLANNING_RULES.md`
- `14_LAYOUT_AUTOMATION\CRITICAL_NET_ROUTING_RULES.md`
- `14_LAYOUT_AUTOMATION\POWER_TRACE_RULES.md`
- `14_LAYOUT_AUTOMATION\USB_TRACE_RULES.md`
- `14_LAYOUT_AUTOMATION\RF_KEEP_OUT_TRACE_RULES.md`
- `14_LAYOUT_AUTOMATION\VIA_STRATEGY_RULES.md`
- `14_LAYOUT_AUTOMATION\GROUND_STITCHING_RULES.md`
- `14_LAYOUT_AUTOMATION\TRACE_BY_TRACE_VERIFICATION_RULES.md`
- `14_LAYOUT_AUTOMATION\ROUTING_SCORECARD_RULES.md`
- `14_LAYOUT_AUTOMATION\test_fixtures\README.md`
- `14_LAYOUT_AUTOMATION\reports\ROUTING_ENGINE_FIXTURE_TEST_REPORT.md`
- `14_LAYOUT_AUTOMATION\scripts\README.md`

Routing order:

1. power input and protection
2. regulator critical loop
3. 3V3 rail
4. USB D+/D-
5. ESD/protection connections
6. ESP32 EN/BOOT
7. decoupling connections
8. LEDs/buttons
9. test pads
10. low-risk remaining nets

Core rules:

- critical nets route first
- do not cross antenna keepout
- keep USB D+/D- clean and paired where practical
- keep regulator switching loop short
- avoid unnecessary vias
- use vias only with reason
- every trace must appear in the trace-by-trace audit
- DRC must pass after routing
- no unrouted nets allowed before final routing pass
- autorouting output is `REVIEW_ONLY` unless fully audited

Hard fails now include:

- critical power net missing
- USB D+/D- incomplete
- trace crosses RF keepout
- trace crosses antenna keepout
- unrouted critical net
- GND strategy missing
- regulator critical loop not planned
- via used without reason on critical net
- trace-by-trace audit missing or incomplete

The current routing engine is fixture-tested, schema-backed, and now has a read-only real-board extraction bridge plus copied-board DRC-coupled audit. It is still not ready for real active-project routing because active-project gate evidence, richer real-board planning logic, and more complete extraction semantics are still missing.

This is a planning and audit engine only. It does not prove final routing quality or fabrication readiness.

## Latest real-project routing gate definition - 2026-05-07

KiCad Engine now has explicit preconditions and stop rules for using the routing engine on a real KiCad PCB:

- `14_LAYOUT_AUTOMATION\REAL_PROJECT_ROUTING_PRECONDITIONS.md`
- `14_LAYOUT_AUTOMATION\REAL_PROJECT_ROUTING_WORKFLOW.md`
- `14_LAYOUT_AUTOMATION\REAL_PROJECT_TRACE_BY_TRACE_REVIEW.md`
- `14_LAYOUT_AUTOMATION\REAL_PROJECT_ROUTING_STOP_CONDITIONS.md`

Real routing may only start when the upstream schematic gate is exact `PASS`, footprints are assigned, the PCB exists and is synced, placement pass 1 and placement orientation pass are exact `PASS`, board outline exists, keepouts/zones exist, the routing plan exists, critical nets are identified, net classes are defined, and DRC precheck passes.

Routing must proceed in ordered passes:

1. power/protection
2. regulator critical loop
3. 3V3 rail
4. USB D+/D-
5. ESD/protection
6. ESP32 EN/BOOT
7. decoupling
8. LEDs/buttons/test pads
9. remaining low-risk nets

The engine must stop immediately for RF/antenna keepout crossings, broken or missing critical nets, missing GND strategy, unjustified vias on critical nets, stale routing plans after placement change, incomplete trace-by-trace review, or visually crude routing even if DRC does not flag it.

## Latest ESP32_CSI_WIFI_NODE live trace audit - 2026-05-07

The active `ESP32_CSI_WIFI_NODE` board is still a real live PCB with placement and partial routing, but the next correct action after the live truth audit was a read-only existing-trace audit, not new routing and not a blind placement rewrite.

Current live trace-audit facts:

- board hash: `0CFE639213D3B0A111F5D06E728A3F7F34B55674DC27312B00D39F80235B2844`
- routed nets present: `/+5V_IN`, `/+5V_FUSED`, `/+5V_PROTECTED`, `/BUCK_SW`, `/BUCK_BST`, `+3V3`
- trace-geometry issues remain on `+3V3`, `/+5V_IN`, and `/+5V_PROTECTED`
- DRC still fails with `12` violations and `65` unconnected items
- `16` unrouted nets remain
- no accepted GND strategy or zones exist

Authoritative project files:

- `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\CURRENT_EXISTING_TRACE_AUDIT.md`
- `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\ROUTING_CURRENT_STATE_REPORT.md`
- `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\ROUTING_START_BLOCKERS.md`

Current next allowed work for this project is existing-trace repair/acceptance plus placement/mechanical acceptance. Do not add new routing until those live blockers are resolved.

Key files:

- `34_PCB_LAYOUT_SANDBOX\README.md`
- `34_PCB_LAYOUT_SANDBOX\PCB_LAYOUT_SANDBOX_RULES.md`
- `34_PCB_LAYOUT_SANDBOX\PCB_VARIANT_WORKFLOW.md`
- `34_PCB_LAYOUT_SANDBOX\AUTO_SANDBOX_APPROVAL_RULES.md`
- `34_PCB_LAYOUT_SANDBOX\AUTO_APPROVAL_STATUS_CODES.md`
- `34_PCB_LAYOUT_SANDBOX\HUMAN_REVIEW_GATE.md`

## Latest PCB variant scoring system - 2026-05-07

`34_PCB_LAYOUT_SANDBOX` now includes the concrete variant scorer, comparator, auto-selector, and selected-variant auto-approval scripts used before real PCB edits:

- `34_PCB_LAYOUT_SANDBOX\VARIANT_SCORING_RULES.md`
- `34_PCB_LAYOUT_SANDBOX\templates\VARIANT_SCORECARD_TEMPLATE.md`
- `34_PCB_LAYOUT_SANDBOX\scripts\score_layout_variant.py`
- `34_PCB_LAYOUT_SANDBOX\scripts\compare_layout_variants.py`
- `34_PCB_LAYOUT_SANDBOX\scripts\auto_select_best_variant.py`
- `34_PCB_LAYOUT_SANDBOX\scripts\auto_approve_selected_variant.py`

Scoring categories:

- mechanical correctness `0-20`
- connector orientation correctness `0-20`
- antenna/RF keepout correctness `0-15`
- power path quality `0-15`
- USB/data routing quality `0-10`
- component grouping quality `0-10`
- routing feasibility `0-10`
- DRC/precheck risk penalty
- human uncertainty risk penalty

Per-variant statuses are now:

- `PASS`
- `FAIL`
- `AUTO_BLOCKED_MISSING_DATA`
- `AUTO_BLOCKED_BAD_LAYOUT`

Hard fails now block selection for missing required connectors, wrong-edge or wrong-facing USB-C, wrong or missing barrel jack/input connector placement when required, blocked ESP32 antenna keepout, missing required mounting holes, guessed board dimensions without source, unassigned footprints, missing exact-package or safe-candidate evidence for high-risk footprints, routing projections crossing antenna keepout, nonsensical power-path order, impossible routing feasibility, and DRC/precheck fail.

The selected variant must be the highest-scoring non-failed option. The selector must not choose a hard-failed variant even if it has the highest numeric score. Selection status is `AUTO_SELECTED`; final approval then maps to `AUTO_APPROVED_FOR_PCB_WORK` or a specific `AUTO_BLOCKED_*` reason.

## Latest FreeRouting feasibility integration - 2026-05-07

KiCad Engine now has an optional FreeRouting dry-run feasibility layer for sandbox routing scoring only:

- `14_LAYOUT_AUTOMATION\FREEROUTING_FEASIBILITY_INTEGRATION.md`
- `34_PCB_LAYOUT_SANDBOX\FREEROUTING_AS_VARIANT_SCORER.md`
- `03_TOOLS\scripts\routing_feasibility\README.md`
- `03_TOOLS\scripts\routing_feasibility\export_dsn_for_feasibility.ps1`
- `03_TOOLS\scripts\routing_feasibility\run_freerouting_dry_run.py`
- `03_TOOLS\scripts\routing_feasibility\parse_unrouted_and_vias.py`
- `03_TOOLS\scripts\routing_feasibility\score_routing_feasibility.py`
- `03_TOOLS\scripts\routing_feasibility\import_route_result_for_review.py`

Core boundary:

- FreeRouting output is `REVIEW_ONLY`
- use it to compare unrouted nets, via count, congestion, and impossible placements
- do not use it to approve USB, RF, switching-regulator, or high-current routing automatically
- never overwrite a real `.kicad_pcb` without backup and explicit approval

## Latest dev-board placement intelligence patch - 2026-05-07

KiCad Engine now has explicit placement-pattern guidance for ESP32-style boards, STM32-style dev boards, USB-C edge connectors, barrel-jack inputs, RF-module keepouts, buttons, LEDs, mounting holes, and test pads.

Authoritative new files:

- `10_KNOWLEDGE_BASE\design_patterns\ESP32_DEV_BOARD_LAYOUT_PATTERN.md`
- `10_KNOWLEDGE_BASE\design_patterns\STM32_DEV_BOARD_LAYOUT_PATTERN.md`
- `10_KNOWLEDGE_BASE\design_patterns\CONNECTOR_EDGE_PLACEMENT_PATTERN.md`
- `10_KNOWLEDGE_BASE\design_patterns\RF_MODULE_ANTENNA_KEEP_OUT_PATTERN.md`
- `10_KNOWLEDGE_BASE\common_mistakes\ESP32_LAYOUT_COMMON_MISTAKES.md`
- `10_KNOWLEDGE_BASE\common_mistakes\USB_C_CONNECTOR_LAYOUT_COMMON_MISTAKES.md`
- `10_KNOWLEDGE_BASE\common_mistakes\BARREL_JACK_LAYOUT_COMMON_MISTAKES.md`
- `34_PCB_LAYOUT_SANDBOX\ESP32_STYLE_BOARD_PLACEMENT_RULES.md`
- `34_PCB_LAYOUT_SANDBOX\DEV_BOARD_SHAPE_REASONING_RULES.md`

Core logic:

- ESP32 antenna must stay at a board edge or clear keepout unless using an external-antenna module
- do not place copper, traces, mounting holes, connectors, or tall parts under the antenna keepout
- USB-C usually belongs on a board edge with shell and board-edge relationship verified
- barrel jack usually belongs on a board edge with insertion direction verified
- buttons must be user-accessible
- LEDs should stay visible
- test pads must remain accessible after assembly
- mounting holes must be clearance-checked
- the AI must justify board shape and must not force rectangle or square by default

These are layout patterns, not universal rules. Project requirements still come first.

## Latest trace-angle routing-quality rule patch - 2026-05-07

KiCad Engine now has a permanent routing-geometry rule set. New authoritative files:

- `09_ACCURACY_ENGINE\pcb_rules\TRACE_ANGLE_ROUTING_RULES.md`
- `09_ACCURACY_ENGINE\pcb_rules\PCB_ROUTING_QUALITY_RULES.md`
- `09_ACCURACY_ENGINE\checklists\PCB_ROUTING_QUALITY_CHECKLIST.md`
- `10_KNOWLEDGE_BASE\pcb_design_patterns\TRACE_ROUTING_BEST_PRACTICES.md`
- `14_LAYOUT_AUTOMATION\ROUTING_QUALITY_RULES.md`

Future PCB routing must avoid crude 90-degree corners where practical, must not use acute-angle bends sharper than 90 degrees unless documented as unavoidable, should use two 45-degree bends for normal routing, and should prefer smoother geometry for high-speed, RF, or sensitive nets where practical. DRC pass alone is not routing-quality approval. If local placement causes ugly routing, move the local cluster instead of forcing bad copper.

The active routing prompts now read and enforce these rules, and `ESP32_CSI_WIFI_NODE` project routing intelligence now references them directly.

## Latest ESP32_CSI_WIFI_NODE routing truth - 2026-05-07

Use the newest routing evidence, not stale maintenance wording. Current routing truth:

- `ROUTING_STAGE_1_2_PROFESSIONAL_CLEANUP_REPORT.md` classification: `STAGE_1_2_PROFESSIONAL_ROUTING_READY_FOR_USB`
- Stage 1 power input and Stage 2 buck/local `+3V3` cleanup are acceptable
- Stage 3 USB is the next routing phase
- copper pour remains `NO`
- full project routing is still incomplete
- `U2 pad 41` drill-rule violations still remain
- live PCB truth audit confirms the real board file hash `0CFE639213D3B0A111F5D06E728A3F7F34B55674DC27312B00D39F80235B2844`
- live board facts: `60 mm x 95 mm`, `43` footprints, `24` track segments, `2` vias, `0` zones, `12` DRC violations, `65` unconnected items, `16` detectable unrouted nets
- stale no-PCB / no-placement wording in `PCB_PLACEMENT_PASS_1_REPORT.md`, `AUTO_PCB_START_REPORT.md`, and related reports was reconciled on `2026-05-07`
- further routing is still blocked by the formal schematic gate, placement/orientation approval gap, missing GND strategy, and the `U2 pad 41` drill-rule issue

If future memory maintenance reproduces older blocked-routing wording, correct project `memory/CURRENT_PROJECT_STATE.md` and `CURRENT_BLOCKERS.md` from the latest evidence reports before trusting the compiled summary.

## Latest ESP32_CSI_WIFI_NODE layout sandbox planning - 2026-05-07

Project-local sandbox variants now exist under:

- `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\layout_sandbox\VARIANT_A_COMPACT_DEV_BOARD_STYLE.md`
- `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\layout_sandbox\VARIANT_B_CONNECTOR_MECHANICAL_OPTIMIZED.md`
- `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\layout_sandbox\VARIANT_C_ROUTING_POWER_RF_OPTIMIZED.md`
- `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\layout_sandbox\VARIANT_COMPARISON_SCORECARD.md`
- `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\layout_sandbox\SELECTED_LAYOUT_PLAN.md`

Current front-runner: `VARIANT_C_ROUTING_POWER_RF_OPTIMIZED`

Important status:

- selection status: `NEEDS_HUMAN_REVIEW`
- real KiCad PCB placement/editing: `BLOCKED`
- remaining blockers: exact board dimensions, unresolved RF pigtail/mechanical evidence, missing sandbox auto-approval evidence, and unresolved upstream schematic/footprint gate items

## Latest audit status - 2026-05-03

The full repo production-quality audit is recorded at `02_HISTORY\design_reviews\FULL_REPO_PRODUCTION_QUALITY_AUDIT.md`.

Current classification: `INTERNAL_ALPHA_READY`.

Public GitHub release status: `NOT_READY`.

Do not claim the repo is complete or public-release ready. Major blockers include scaffold-heavy folders, path drift, unreviewed PDFs, generated/tool/vendor payload hygiene, missing git metadata in this checkout, unverified component/footprint data, and the blocked `ESP32_CSI_WIFI_NODE` schematic-to-PCB gate.

## Latest P0/P1 repair status - 2026-05-03

Repair plan: `05_OUTPUTS\release_readiness\P0_P1_REPAIR_PLAN.md`

Narrow P0/P1 fixes completed:

- Public-release exclusion gate added at `17_RELEASE_BUILD\PUBLIC_RELEASE_EXCLUSION_MANIFEST.md`.
- Root `.gitignore` added for secrets, local environments, generated outputs, backups, installer builds, unreviewed PDFs, and fabrication-style artifacts.
- Datasheet redistribution review gate added at `06_DATASHEETS\00_INDEX\REDISTRIBUTION_REVIEW_REQUIRED.md`.
- Active startup/handoff/config paths normalized to the current checkout and `PATH_PORTABILITY_RULES.md`.
- Windows/macOS/Linux optional installer scripts now default to dry-run and require explicit apply flags before package-manager installs.
- Core placeholder rows in `06_DATASHEETS\00_INDEX` and prompt/index files were replaced with actionable status records or explicit template notation.

Remaining public-release blockers still exist. Do not publish until the remaining P2/P3 backlog, legal review, payload review, and installer validation are complete.

## Latest core placeholder upgrade status - 2026-05-03

Core placeholder content upgrade report: `02_HISTORY\design_reviews\CORE_PLACEHOLDER_CONTENT_UPGRADE_AUDIT.md`

Summary: `05_OUTPUTS\release_readiness\CORE_PLACEHOLDER_CONTENT_UPGRADE_SUMMARY.md`

The latest pass upgraded weak core docs in `00_CODEX_START`, `06_DATASHEETS/00_INDEX`, `08_COMPONENT_DATABASE/00_INDEX`, `09_ACCURACY_ENGINE`, `10_KNOWLEDGE_BASE`, `11_LIBRARY_FACTORY`, `26_AGENT_QUALITY`, `28_SUPPLIER_INGESTION`, `29_FOOTPRINT_GAP_ANALYSIS`, and `31_PLAYWRIGHT_RESEARCH_PIPELINE`. These upgrades added concrete schemas, agent-use rules, pass/block criteria, supplier safety language, footprint verification gates, and Playwright evidence limits. Generated dry-run records remain `UNVERIFIED` by design; do not treat them as complete component, footprint, supplier, or datasheet evidence.

## Latest open KiCad sample intake status - 2026-05-03

`32_OPEN_KICAD_SAMPLE_INTAKE` now defines the controlled path for open KiCad sample project discovery, license screening, import, normalization, review, and benchmark promotion. Do not download or clone sample projects into the repo root. Do not edit `imported_originals`. Use normalized copies for analysis, keep all generated outputs `NOT_FINAL`, and exclude samples from public payloads unless license status is `PUBLIC_BUNDLE_ALLOWED`.

## Latest open KiCad sample candidate discovery - 2026-05-03

Candidate discovery records were added under `32_OPEN_KICAD_SAMPLE_INTAKE\candidates`. No repositories were cloned, downloaded, imported, or normalized. The top recommended first-import candidates are `tomasr8/attiny85-dev-board`, `M4a1x/TPS5430`, and optionally `esp-rs/esp-rust-board`, but import still requires explicit user approval and human license/attribution review. See `32_OPEN_KICAD_SAMPLE_INTAKE\review_reports\CANDIDATE_DISCOVERY_REPORT.md`.

## Latest open KiCad sample import - 2026-05-03

The first approved open-license KiCad sample batch was imported under `32_OPEN_KICAD_SAMPLE_INTAKE` only:

- `tomasr8/attiny85-dev-board` -> `imported_originals\tomasr8_attiny85_dev_board` and `normalized_samples\tomasr8_attiny85_dev_board`
- `M4a1x/TPS5430` -> `imported_originals\m4a1x_tps5430` and `normalized_samples\m4a1x_tps5430`
- `esp-rs/esp-rust-board` -> `imported_originals\esp_rs_esp_rust_board` and `normalized_samples\esp_rs_esp_rust_board`

Attribution and import reports were created under `32_OPEN_KICAD_SAMPLE_INTAKE\attribution` and `32_OPEN_KICAD_SAMPLE_INTAKE\review_reports`. Imported originals must remain unchanged. The normalized copies are not promoted to active projects. Imported upstream Gerbers, drill files, BOMs, placement files, and STEP files are historical source artifacts, not KiCad Engine generated outputs. No ERC, DRC, visual review, footprint audit, benchmark scoring, or manufacturing export was performed during import.

## Latest open KiCad sample engineering audit - 2026-05-03

The normalized imported samples were audited read-only with local KiCad `kicad-cli 9.0.7`. Reports are under `32_OPEN_KICAD_SAMPLE_INTAKE\review_reports`, with the master summary at `SAMPLE_PROJECTS_MASTER_AUDIT.md` and the global audit record at `02_HISTORY\design_reviews\OPEN_KICAD_SAMPLE_PROJECTS_MASTER_AUDIT.md`.

Current classification for all imported samples: `BROKEN_TEST_PROJECT`.

- `esp_rs_esp_rust_board`: ERC failed with 73 messages, DRC failed with 81 DRC violations and 95 footprint/parity errors.
- `m4a1x_tps5430`: ERC failed with 36 warnings, DRC failed with 87 DRC violations and 30 footprint/parity errors.
- `tomasr8_attiny85_dev_board`: ERC failed with 7 messages, DRC failed with 16 DRC violations and 13 footprint/parity errors.

Full-page schematic and PCB SVG exports succeeded for all three samples. Close-up crop review was not generated because the normalized samples do not yet have KiCad Engine visual block definitions. Do not promote these samples as golden-path demos, clean benchmark baselines, reference-grade designs, public payload samples, or manufacturing-ready examples until a future repair/enrichment pass and re-audit prove they pass the appropriate gates.

## Latest controlled golden-path sample fixture - 2026-05-03

`tomasr8_attiny85_dev_board` was selected as the best imported sample for a controlled KiCad Engine demo fixture because it is small, MIT-licensed in the import evidence, has schematic and PCB files, and has the fewest ERC/DRC issues among the imported samples. It was copied to `19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board`.

Latest gate run: `tomasr8_attiny85_dev_board` is now `GOLDEN_PATH_PARTIAL`, not a clean passing design. A backup was created under `99_BACKUPS\pre_codex_edits\20260503_145319_tomasr8_attiny85_dev_board_pre_golden_path_gate`. Low-risk repairs were applied only to the promoted copy: project-local `fp-lib-table` now maps `My footprints` to `${KIPRJMOD}\custom_footprints`, `J1`/`J2`/`U2` carry `BLOCKED_UNTIL_HUMAN_REVIEW` metadata, ATtiny85-specific schematic and PCB crop configs were added, review-only BOM/visual outputs were generated, and the project validator was fixed to parse quoted library names with spaces. ERC still fails on `J1` shield policy, DRC still fails with 15 violations and 13 schematic parity issues, and connector/regulator/polarity review remains human-blocked. Reports: `19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\reports\GOLDEN_PATH_GATE_REPORT.md`, `GOLDEN_PATH_REPAIR_LOG.md`, and `GOLDEN_PATH_FINAL_AUDIT.md`. Benchmark task: `15_BENCHMARKS\tasks\TASK_GOLDEN_PATH_tomasr8_attiny85_dev_board.md`; baseline result: `15_BENCHMARKS\results\tomasr8_attiny85_dev_board_BASELINE_RESULT.md`.

Latest project gate runner update, 2026-05-06: `03_TOOLS\scripts\project_gate` now provides the read-only one-command project gate runner. Command: `.\03_TOOLS\scripts\project_gate\run_project_gate.ps1 -ProjectPath "19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board"`. Latest output: `05_OUTPUTS\gate_runs\20260506_142924\PROJECT_GATE_REPORT.md` and `.json`. Result: `BLOCKED_UNTIL_HUMAN_REVIEW`, with 9 gates checked, 2 pass, 3 fail, 4 blocked, and 14 blockers surfaced. The runner did not edit KiCad files, did not run ERC/DRC, and did not generate fabrication outputs.

Latest sample-project public docs update, 2026-05-06: user-facing documentation for sample projects, the ATtiny85 golden-path demo fixture, and the one-command gate runner was added under `19_TEST_PROJECTS` and `18_PUBLIC_DOCS`. Key files: `19_TEST_PROJECTS\README.md`, `SAMPLE_PROJECTS_INDEX.md`, `HOW_TO_RUN_SAMPLE_PROJECTS.md`, `HOW_TO_INTERPRET_GATE_RESULTS.md`, `18_PUBLIC_DOCS\HOW_TO_RUN_GOLDEN_PATH_DEMO.md`, `HOW_TO_VERIFY_PROJECT.md`, `HOW_TO_USE_SAMPLE_PROJECTS_WITH_CODEX.md`, and `HOW_TO_USE_SAMPLE_PROJECTS_WITH_CLAUDE.md`. Keep the public status honest: the promoted sample is controlled and useful, but not a clean passing design and not fabrication-ready.

Latest release payload sample policy update, 2026-05-06: public payload rules now live under `17_RELEASE_BUILD\PAYLOAD_ALLOWLIST.md`, `PAYLOAD_EXCLUDE_RULES.md`, `PUBLIC_PAYLOAD_MANIFEST.md`, `PUBLIC_RELEASE_EXCLUSION_MANIFEST.md`, and `SAMPLE_PROJECT_PAYLOAD_POLICY.md`. Raw imported sample repos under `32_OPEN_KICAD_SAMPLE_INTAKE\imported_originals`, normalized sample working copies, unclear-license samples, personal history, backups, generated outputs, unreviewed PDFs, secrets, API keys, `FAB_READY` files, and fabrication outputs are excluded by default. The `tomasr8_attiny85_dev_board` fixture is currently `LINK_ONLY_PLUS_DOCS`: attribution/status markdown may be public, but KiCad source files, custom footprints, generated visuals, gate-run folders, and fabrication-style outputs remain blocked until final human license/release review records public bundle status exactly `PUBLIC_BUNDLE_ALLOWED`.

Latest post-sample production audit, 2026-05-06: `02_HISTORY\design_reviews\POST_SAMPLE_PROJECT_PRODUCTION_AUDIT.md` classifies the sample/demo/release-payload state as `INTERNAL_ALPHA`, not public-release ready. Fresh gate run output: `05_OUTPUTS\gate_runs\20260506_145808\PROJECT_GATE_REPORT.md`; result `BLOCKED_UNTIL_HUMAN_REVIEW` with 9 gates checked, 2 pass, 3 fail, 4 blocked, and 14 blockers. Main blockers: ATtiny85 ERC fails on `J1` shield, DRC still reports 15 violations and 13 parity/footprint issues, footprint/orientation review remains open for `J1`, `J2`, and `U2`, human visual review remains required, and human license/public-bundle review is still required.

Latest post-sample P0/P1 repair, 2026-05-06: `17_RELEASE_BUILD\build_public_payload.py` now exists as a dry-run-first public payload manifest builder. It excludes raw sample imports, normalized samples, backups, generated outputs, PDFs, local environments, third-party tool repos, secret-like files, `FAB_READY` files, and ATtiny85 sample KiCad source files while public-bundle review is pending. Public release remains `INTERNAL_ALPHA`; the ATtiny85 fixture still fails the gate and remains `BLOCKED_UNTIL_HUMAN_REVIEW`.

Latest KiCad native GUI annotation success, 2026-05-06: Codex successfully used safety-gated KiCad GUI automation to run native `Annotate Schematic` on `ESP32_CSI_WIFI_NODE`. The exact Eeschema process and schematic path were detected, a backup was created, screenshots were captured, KiCad's native annotation dialog opened, annotation was applied, the schematic was saved from KiCad GUI, GUI ERC showed `Violations (0)`, `kicad-cli` ERC passed with 0 errors and 0 warnings, and the saved schematic reference table had 0 unresolved `?` references and 0 duplicate references. Evidence: `33_KICAD_GUI_AUTOMATION\KICAD_NATIVE_ANNOTATION_SUCCESS_RECORD.md`, plus project reports under `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\KICAD_GUI_NATIVE_ANNOTATION_*`.

Future annotation tasks must use KiCad native GUI annotation when available. Raw `.kicad_sch` text edits, regex scans, and saved-file-only tables are not accepted as proof of annotation success. After native annotation passes, visual cleanup is allowed only as a separate task, and PCB update remains blocked until the full schematic-to-PCB gate is exactly `PASS`.

Latest KiCad auto-open workflow, 2026-05-06: `33_KICAD_GUI_AUTOMATION` now has dry-run-first support for opening the exact target KiCad project when Eeschema is closed. New workflow: `33_KICAD_GUI_AUTOMATION\KICAD_AUTO_OPEN_PROJECT_WORKFLOW.md`. New scripts: `scripts\windows\open_kicad_project.py`, `open_kicad_project.ps1`, `open_schematic_editor_gui.py`, `ensure_eeschema_open.py`, and `run_native_annotation_workflow.py`. Dry-run validation was performed only; live closed-state launch and live annotation-from-closed-state still require a future explicit test. Future live use requires `--live`; annotation requires `--allow-annotation`; save requires `--allow-save`; GUI ERC requires `--allow-gui-erc`. Stop if Eeschema is open for a different project or starts with `*` without explicit approval.

Latest live-state phase gate repair, 2026-05-07: `03_TOOLS\scripts\project_gate\check_phase_allowed.py` is now live-state-aware. It rebuilds or reads `reports\LIVE_PROJECT_STATE.json`, runs stale-report detection, and labels each blocker as `LIVE_FILE_EVIDENCE`, `FRESH_GATE_REPORT`, `STALE_REPORT_IGNORED`, or `HUMAN_REVIEW_REQUIRED`. This prevents stale `NO_PCB`, `0 footprints`, and old missing-phase reports from overriding the real KiCad files.

Latest pill-style placement rule patch, 2026-05-07: compact dev-board placement now has hard rules under `09_ACCURACY_ENGINE\pcb_rules` and `09_ACCURACY_ENGINE\checklists\PILL_STYLE_PLACEMENT_CHECKLIST.md`. This was added after `ESP32_CSI_WIFI_NODE` moved from an oversized dead-space board to a smaller pill-style board that still had connector, test-pad, spacing, mounting-hole, silkscreen, and mechanical-fit problems. Future ESP32/STM32-style placement must enforce top-edge RF keepout, bottom-edge USB-C mouth orientation, explicit barrel-jack review, clean service-row test pads, accessible reset/boot/LEDs, no unproven four-hole layouts on narrow boards, no overlaps, no unexplained dead areas, and LJ visual approval before routing.

Latest barrel-jack/USB-C orientation rule patch, 2026-05-07: after LJ provided a horizontal barrel-jack reference image, `09_ACCURACY_ENGINE\pcb_rules\BARREL_JACK_ORIENTATION_RULES.md` and `10_KNOWLEDGE_BASE\connectors\BARREL_JACK_ORIENTATION_GUIDE.md` now record that the female circular barrel opening is the front/mating side and the 3-pin solder-leg side is the rear/back side. For bottom-edge J1, the female opening must face down/off-board and the 3-pin solder side must face up/inward. USB-C rules now explicitly require mouth/off-board, bottom-edge mouth down/off-board, `PCB Edge` alignment to `Edge.Cuts`, pads on-board, expected shell/body overhang, and proof beyond coordinates. The LJ image still requires manual binary save to the documented `.png` paths because the chat image was not available as a filesystem source.

Latest ESP32_CSI_WIFI_NODE PCB intelligence layer, 2026-05-07: a read-only project-specific documentation layer was added under `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\pcb_intelligence`. It was generated from the actual schematic/PCB source files and documents all 43 physical components, 52 pad-connected nets, 14 critical power/USB/GND nets, placement dependencies, route order, test pad access risks, ESP32 RF keepout rules, mounting/connector mechanical risks, via/layer strategy, and machine-readable JSON for future agents. No schematic or PCB files were edited. Future ESP32 placement repair/routing work must read this folder first. Current placement remains `BLOCKED_BY_MECHANICAL_OR_FOOTPRINT_RISK`; routing remains blocked.

Latest maintenance supervisor repair, 2026-05-07: use `03_TOOLS\scripts\maintenance\run_maintenance_cycle.py` as the canonical maintenance entrypoint. It builds `reports\LIVE_PROJECT_STATE.json`, `reports\STALE_REPORTS_AUDIT.md`, `reports\GATE_RECONCILIATION_REPORT.md`, refreshes project current-state memory, rebuilds indexes, and rebuilds `CURRENT_KNOWN_PROBLEMS.md`. The older `03_TOOLS\scripts\memory_maintenance\run_memory_maintenance.py` path is compatibility-only.

Latest memory/history cleanup run, 2026-05-07T12:41:21-04:00: maintenance apply mode refreshed `ESP32_CSI_WIFI_NODE` current-state memory and rebuilt memory/history/known-problems indexes. Cleanup counts: duplicate blocker topics `11`, stale/superseded reports `94`, false-pass candidate incidents `58`, unresolved relative-date hits `422`. Evidence: `05_OUTPUTS\release_readiness\MEMORY_HISTORY_CLEANUP_REPORT.md`, `02_HISTORY\sessions\MEMORY_HISTORY_CLEANUP_SESSION.md`, and `02_HISTORY\command_logs\MEMORY_HISTORY_CLEANUP_COMMANDS.md`. No KiCad design files were intentionally changed.

Latest prompt-count maintenance rule, 2026-05-07: before meaningful active-project engineering work, check `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\memory\PROMPT_COUNTER.md` with `03_TOOLS\scripts\memory_maintenance\check_maintenance_due.py`. Meaningful repo tasks increment the counter. At 5, run `python 03_TOOLS\scripts\maintenance\run_maintenance_cycle.py --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE` and reset the counter before new engineering work.

Latest ESP32_CSI_WIFI_NODE PCB creation status, 2026-05-07: Phase 2 was run with LJ approval. `kicad\ESP32_CSI_WIFI_NODE.kicad_pcb` now exists and contains all 43 schematic footprints imported into a non-final parking grid. Initial DRC ran and failed with 13 DRC violations, 75 unconnected items, and 3 schematic-parity issues. The blocking sync issue is Q1: the AO3401A schematic pins are named `D/G/S`, while the selected SOT-23 footprint pads are numbered `1/2/3`. Codex did not guess this production-critical mapping. Current status file: `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\PCB_SYNC_STATUS.md`; next action is Phase 2 repair/human review for Q1 pin mapping, not placement planning.

Latest ESP32_CSI_WIFI_NODE schematic safe repair, 2026-05-06: safe schematic-only cleanup was applied to `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch` after backup at `99_BACKUPS\pre_codex_edits\20260506_152549_ESP32_CSI_WIFI_NODE_schematic_safe_repair`. The pass hid blank footprint fields, added hidden `SOURCE_LINK_REQUIRED` datasheet placeholders, hid power-symbol reference text, marked `U1` as `NEEDS_REVIEW`, tuned schematic visual crop blocks, and replaced stale/overconfident note wording. ERC remains clean with 0 errors and 0 warnings, and automated close-up visual crop generation now reports `PASS`. PCB update is still blocked: 43 physical footprints remain blank, BOM lock files are still missing, high-risk `NEEDS_REVIEW`/`BLOCKED` markers remain, and human visual/footprint/policy review is still required. Evidence: `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\SCHEMATIC_VERIFICATION_REPORT.md`.

Latest ESP32_CSI_WIFI_NODE electrical/footprint gate, 2026-05-06: read-only gate review reran ERC and schematic checkers after the safe schematic repair. ERC passed with 0 errors and 0 warnings, but final classification is `SCHEMATIC_BLOCKED_NEEDS_HUMAN_REVIEW`, not ready for PCB update. Evidence: `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\SCHEMATIC_ELECTRICAL_GATE_REPORT.md`, `FOOTPRINT_PACKAGE_GATE_REPORT.md`, and `SCHEMATIC_TO_PCB_GATE_STATUS.md`. The blockers are explicit: 43 physical footprints are blank, every physical symbol still has placeholder `SOURCE_LINK_REQUIRED`, BOM lock files are missing, AO3401A/PMOS pin mapping remains blocked, USB VBUS and shield policies remain unresolved, and all high-risk connector/footprint/package decisions require human review. Do not update PCB from schematic unless `SCHEMATIC_TO_PCB_GATE_STATUS.md` is later changed to `PASS`.

Latest ESP32_CSI_WIFI_NODE human review packet, 2026-05-06: LJ-facing schematic review packet was created at `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\SCHEMATIC_HUMAN_REVIEW_PACKET.md` with checklist `reports\LJ_VISUAL_REVIEW_CHECKLIST.md`. It indexes the full-page PDF/SVG/PNG exports and 13 close-up crop blocks under `_verification\schematic_visual`. This was report-only; no schematic or PCB files were edited. Status remains `SCHEMATIC_BLOCKED_NEEDS_HUMAN_REVIEW`, and PCB update remains blocked.

Latest ESP32_CSI_WIFI_NODE emergency schematic truth audit, 2026-05-06: after LJ reported the schematic looked visually unacceptable in KiCad, a fresh read-only audit was run against the actual current `.kicad_sch`. Backup: `99_BACKUPS\pre_codex_edits\20260506_155934_ESP32_CSI_WIFI_NODE_emergency_truth_audit`. Evidence: `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\EMERGENCY_CURRENT_SCHEMATIC_TRUTH_AUDIT.md` and `CURRENT_SCHEMATIC_BLOCKERS.md`. Truth status: references are annotated in the narrow no-question-mark sense and ERC is clean, but the schematic is not acceptable. All 43 physical symbols still had blank footprints at that audit point. The legacy crop generation report used `PASS` wording, but that only checked unannotated refs and visible field-risk strings; fresh SVG analysis found 573 text items, 356 heuristic overlap candidates, and 20 near-text candidates. Treat prior visual PASS claims as `AUTOMATED_CROP_PASS_ONLY`, not human readability approval. PCB update remains forbidden.

Latest ESP32_CSI_WIFI_NODE BOM/footprint lock, 2026-05-06: planning-only lock files were created without editing the schematic: `PRE_SCHEMATIC_BOM_LOCK.md`, `SCHEMATIC_READY_PARTS_LIST.md`, `NEEDS_REVIEW_BEFORE_SCHEMATIC.md`, and `reports\FOOTPRINT_ASSIGNMENT_PLAN.md`. The lock covers all 43 physical symbols and records candidate KiCad footprints where possible, but no footprint is verified against an exact package drawing. Status counts: 30 `CANDIDATE_NEEDS_HUMAN_REVIEW`, 7 `BLOCKED_NO_EXACT_PART`, 6 `BLOCKED_NO_PACKAGE`, 0 `VERIFIED_EXACT_PACKAGE_DRAWING`. Schematic footprint assignment is not safe to proceed automatically; LJ must review exact parts/package defaults first.

Latest ESP32_CSI_WIFI_NODE schematic real repair, 2026-05-06: the schematic was edited after backup at `99_BACKUPS\pre_codex_edits\20260506_162153_ESP32_CSI_WIFI_NODE_schematic_real_repair`. The repair fully annotated physical references, assigned candidate footprints from `reports\FOOTPRINT_ASSIGNMENT_PLAN.md`, hid footprint fields from normal view, shortened visible values/notes, and regenerated ERC/checker/visual evidence. Current evidence: `reports\SCHEMATIC_VERIFICATION_REPORT.md`, `_verification\VISUAL_CHECK_REPORT.md`, `_verification\schematic_visual\CLOSE_UP_REVIEW.md`, and `reports\SCHEMATIC_TO_PCB_GATE_STATUS.md`. ERC passes with 0 errors and 0 warnings. Annotation and completeness checks pass. Automated visual crop review passes with 13 blocks. Final status is `SCHEMATIC_READY_FOR_LJ_VISUAL_REVIEW_BUT_BLOCKED_FOR_PCB`. PCB update remains forbidden because no candidate footprint is verified against exact manufacturer drawings, 11 review markers remain, BOM lock alignment has warnings, and LJ visual/connector/polarity/USB/PMOS/package review is pending.

Latest ESP32_CSI_WIFI_NODE final schematic readiness re-audit, 2026-05-06: a strict read-only re-audit was run after the real repair. Evidence: `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\FINAL_SCHEMATIC_READINESS_AUDIT.md` and `LJ_FINAL_VISUAL_REVIEW_PACKET.md`. Final classification changed to `NOT_READY_NEEDS_MORE_REPAIR`. ERC still passes, there are no `?` references, no duplicate physical references, and all 43 physical symbols have candidate footprints. However, rendered full-page/crop inspection still shows clear text/value/reference/net-label overlaps in input power, buck regulator, USB-C/ESD, ESP32 module, reset/boot, and LED areas. Treat automated crop `PASS` as crop-generation/ref-field screening only, not human readability approval. PCB update remains forbidden.

Latest strict visual gate patch, 2026-05-06: repo-wide rules now explicitly forbid confusing automated crop `PASS`, ERC pass, annotation pass, populated footprint fields, hidden footprint fields, or no `?` token detection with human-readable visual approval. New rules: `09_ACCURACY_ENGINE\verification_rules\HUMAN_READABLE_SCHEMATIC_RULES.md`, `09_ACCURACY_ENGINE\verification_rules\VISUAL_PASS_IS_NOT_AUTOMATED_PASS.md`, and `09_ACCURACY_ENGINE\checklists\SCHEMATIC_HUMAN_READABILITY_CHECKLIST.md`. `03_TOOLS\kicad\VISUAL_VERIFICATION_WORKFLOW.md`, `AGENTS.md`, and `README_GPT.md` were updated. Any visible text/value/reference/net-label overlap in rendered full-page/crops is now `VISUAL_FAIL`; if the agent cannot inspect rendered images, visual status is `VISUAL_NOT_VERIFIED`, not `PASS`.

Latest schematic failure root-cause audit, 2026-05-06: `02_HISTORY\design_reviews\KICAD_ENGINE_SCHEMATIC_FAILURE_ROOT_CAUSE_AUDIT.md` identifies the root cause as evidence/status mismatch. The crop generator used pass-like wording for automated evidence generation, and pipeline prompts allowed that wording to be overclaimed. `03_TOOLS\scripts\visual\generate_schematic_closeups.py` now reports `AUTOMATED_CROP_PASS_ONLY` for automated-only success. `.prompts\kicad_pipeline\02_schematic_visual_closeup_audit.md`, `03_schematic_visual_repair.md`, and `06_schematic_to_pcb_gate.md` now ban visual pass or schematic-to-PCB pass from automated crop output alone. Any older `Close-up visual review status: PASS` must be treated as stale automated-only wording unless a rendered-image inspection table proves every block passed.

Latest ESP32_CSI_WIFI_NODE emergency annotation repair, 2026-05-06: after LJ reported KiCad GUI/ERC still showed unannotated references, an annotation-only repair was performed on `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch` after backup at `99_BACKUPS\pre_codex_edits\20260506_180514_ESP32_CSI_WIFI_NODE_emergency_annotation_repair`. The saved schematic was parsed by actual placed-symbol `Reference` properties. Physical references were already unique and stayed unchanged; power references were normalized to `#PWR0101` through `#PWR0133`, and PWR_FLAG references were normalized to `#FLG0101` through `#FLG0103`. Current evidence: `reports\EMERGENCY_ANNOTATION_REPAIR_REPORT.md`, `ANNOTATION_REFERENCE_TABLE.md`, `ERC_AFTER_ANNOTATION_REPAIR.md`, and `ANNOTATION_VISIBLE_QUESTION_REFERENCE_SCAN.md`. `kicad-cli sch erc` now reports 0 violations and no `Schematic is not fully annotated` message. Fresh SVG/crop scans show no visible unresolved `?` references. This is annotation/ERC evidence only; live GUI stale state was not directly controlled, and PCB update remains forbidden because visual readability and high-risk part/footprint review gates still fail.

Latest ESP32_CSI_WIFI_NODE actual KiCad annotation repair, 2026-05-06: LJ later reported the current KiCad ERC still showed 67 annotation errors, so the annotation repair was repeated with a stricter saved-file method. Backup: `99_BACKUPS\pre_codex_edits\20260506_183127_ESP32_CSI_WIFI_NODE_actual_kicad_annotation_repair`. Method: structured KiCad S-expression repair because local `kicad-cli` has no annotation command. The saved schematic now has matching `instances` reference blocks for all 79 placed symbols; physical refs total 43, `#PWR` refs total 33, and `#FLG` refs total 3. Evidence: `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\ANNOTATION_REPAIR_ACTUAL_KICAD_ERC_REPORT.md`, `ANNOTATION_REPAIR_ACTUAL_KICAD_ERC_REPORT.rpt`, `ANNOTATION_REFERENCE_TABLE_FINAL.md`, and `SCHEMATIC_TO_PCB_GATE_STATUS.md`. Local `kicad-cli sch erc` reports 0 violations and no `Schematic is not fully annotated` message, and unresolved/duplicate reference checks pass. If KiCad GUI was open during the file repair, LJ should close/reopen or reload the schematic before checking GUI/ERC state. This only clears annotation evidence; visual readability and high-risk footprint/part decisions still block PCB update.

Historical ESP32_CSI_WIFI_NODE GUI annotation mismatch diagnosis, 2026-05-06: LJ previously reopened/focused the exact active schematic in KiCad and still saw visible unannotated refs such as `R?`, `D?`, `SW?`, `C?`, and `MH?`, proving text-edit annotation repair was not acceptable. That annotation-only blocker was later resolved by the successful native GUI annotation run recorded in `33_KICAD_GUI_AUTOMATION\KICAD_NATIVE_ANNOTATION_SUCCESS_RECORD.md`. Keep the lesson: do not use raw text edits as annotation proof. Current remaining blockers are visual readability, footprint/package, electrical policy, LJ review, and schematic-to-PCB gate status.

Latest KiCad GUI automation layer setup, 2026-05-06: `33_KICAD_GUI_AUTOMATION` is the dedicated opt-in GUI/native KiCad control layer. It provides rules and scripts for detecting KiCad/Eeschema windows, detecting unsaved `*` GUI state, confirming exact open schematic paths, taking screenshots, and running safety-gated native annotation/save/GUI ERC. Live native annotation/save/ERC automation is now verified once on `ESP32_CSI_WIFI_NODE`; the current scripts still require explicit task scope, backup, screenshots, exact path match, and post-save ERC/reference validation. Mandatory rule: for annotation tasks, Codex/Claude must use verified KiCad-native annotation through this GUI gate when available or stop and instruct LJ to run KiCad `Tools -> Annotate Schematic -> Re-annotate all symbols -> Save -> Run ERC`. Raw `.kicad_sch` text edits are not sufficient proof.

## What this repo is

This is LJ's local-first KiCad engineering workspace for AI-assisted PCB design support, review, automation, ERC/DRC, BOM/export review, project memory, session history, finished-PCB reference review, and Codex startup control. It uses the user's installed KiCad app and is intended to support Codex, Claude, and similar VS Code-based agents. The long full context file is `README_GPT.md`.

Product direction docs:

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
- `.prompts\kicad_pipeline\*.md`
- `02_HISTORY\design_reviews\KICAD_ENGINE_PRODUCT_GAP_AUDIT.md`

## What ChatGPT should read first

1. `AGENTS.md`
2. `README_GPT.md`
3. `FOR CHAT GPT.MD`
4. `00_CODEX_START\START_HERE.md`
5. `00_CODEX_START\KICAD_PHASE_ORDER.md`
6. `00_CODEX_START\SESSION_START_CHECKLIST.md`
7. `00_CODEX_START\STRUCTURE_STANDARD.md`
8. `00_CODEX_START\FOLDER_ROUTING_RULES.md`
9. `00_CODEX_START\CURRENT_KNOWN_PROBLEMS.md`
10. `00_CODEX_START\MEMORY_INDEX.md`
11. `00_CODEX_START\HISTORY_INDEX.md`
12. Active project memory/history if project work is in scope.

Then read task-specific files such as `CONTROL_PLANES.md`, `TOOL_INDEX.md`, `PROJECT_INDEX.md`, `CURRENT_PROJECT.md`, accuracy-engine rules, component-database rules, library-factory rules, installer/release docs, or prompt-pack files.

## Current structure summary

- `00_CODEX_START`: mandatory startup rules, safety rules, indexes, learning-loop rules, AI truthfulness scoring, hallucination-risk rules, response quality gates, and current known problems.
- `.vscode`: VS Code workspace settings, recommended extensions, tasks, and debug launch templates.
- `.prompts`: reusable VS Code prompt pack for Codex, Claude, shared safety/research/verification standards, and the permanent 17-stage KiCad project pipeline prompts under `.prompts\kicad_pipeline`.
- `01_MEMORY`: durable global, design-rule, component, fab, scripting, agent lesson, user correction, workflow, mistake-avoidance, AI reliability, hallucination-risk, quality-gate, and project memory.
- `02_HISTORY`: session logs, command logs, design reviews, ERC/DRC reports, fabrication reviews, failed attempts, issue logs, user corrections, lessons learned, workflow runs, AI self-reviews, scorecards, claim/evidence matrices, uncertainty logs, hallucination-risk logs, quality-gate failures, and project history.
- `03_TOOLS`: cloned tool repos, isolated Python/Node environments, scripts, tool logs, and platform roots for common, Windows, and Linux automation.
- `04_KICAD_PROJECTS`: active KiCad projects, standard project templates, and finished-PCB reference review templates.
- `05_OUTPUTS`: generated reports and review/export outputs; not final unless verification gates pass.
- `06_DATASHEETS`: numbered, AI-friendly electronics datasheet and reference library with indexes, source rules, missing-document trackers, and a legacy inbox.
- `06_DATASHEETS\00_INDEX\source_lists`: metadata-first CSV source lists for vendor/document research. These lists intentionally store source portals and redistribution status instead of bundled PDFs.
- `07_REFERENCE_DESIGNS`: general reference design metadata, public-source links, summaries, and review notes that are separate from the formal curated reference design library.
- `08_COMPONENT_DATABASE`: structured component intelligence beyond PDFs, with schemas, verification flags, KiCad symbol/footprint linking rules, package-footprint verification records, component verification records, no-guess rules, templates, and placeholder part records.
- `09_ACCURACY_ENGINE`: schematic, PCB, verification, and workflow rules that prevent AI agents from guessing. Read this before schematic creation, component adds, symbol selection, footprint selection, PCB creation, or release-package work.
- `09_ACCURACY_ENGINE\checklists\ACCURACY_GATE_CHECKLIST.md`: mandatory accuracy gate checklist before creating or approving schematics, PCBs, footprints, BOMs, or fab outputs.
- `09_ACCURACY_ENGINE\workflows\FULL_KICAD_PROJECT_PIPELINE.md` and `09_ACCURACY_ENGINE\checklists\FULL_PIPELINE_GATE_CHECKLIST.md`: permanent 17-stage schematic-to-PCB-to-routing-to-NOT_FINAL-fabrication pipeline. Future KiCad projects must follow these gates unless LJ explicitly approves a logged exception.
- `09_ACCURACY_ENGINE\workflows\SCHEMATIC_TO_PCB_GATE_WORKFLOW.md`: strict transition gate that blocks PCB update, placement, routing, zones, and PCB manufacturing-style outputs unless the active project's `reports\SCHEMATIC_TO_PCB_GATE_STATUS.md` is `PASS`.
- `09_ACCURACY_ENGINE\verification_rules\SCHEMATIC_ANNOTATION_RULES.md` and `SCHEMATIC_COMPLETENESS_RULES.md`: required annotation, duplicate-reference, BOM-lock, functional-block, and unresolved-review-marker screening rules before layout.
- `09_ACCURACY_ENGINE\verification_rules\CLOSE_UP_VISUAL_REVIEW_RULES.md`: close-up visual crop evidence rules for full-page exports, crop generation, visible unannotated references, and visible footprint/library-field detection.
- `10_KNOWLEDGE_BASE`: reusable circuit blocks, design patterns, review checklists, common mistakes, manufacturing package rules, and AI-agent stop/verify guidance for practical schematic and PCB creation. It is a planning aid, not datasheet proof.
- `11_LIBRARY_FACTORY`: source-backed KiCad symbol, footprint, package mapping, project-local library, and basic read-only library QA standards. Read this before creating, selecting, verifying, or mapping symbols and footprints.
- `12_REFERENCE_DESIGN_LIBRARY`: public-source reference design links, summaries, license records, verification levels, and category checklists. Reference designs are evidence, not automatic approval or permission to copy.
- `13_PART_INGESTION`: new-part datasheet/source ingestion workflows, extraction rules, AI summary templates, and stub generators. Generated stubs are placeholders until source review is complete.
- `14_LAYOUT_AUTOMATION`: realistic KiCad-native placement/routing assistance plans, constraint extraction, FreeRouting integration planning, and human layout review gates. It does not claim complete AI auto-layout or autorouting.
- `15_BENCHMARKS`: benchmark methodology, task definitions, scoring rubrics, and future real run results. It starts with no fake scores and requires actual artifacts before any comparison claim. Prompt 8 added/confirmed the core task set: ESP32-S3 minimum system, STM32 minimum system, CAN bus node, USB-C power device, 12V automotive input, and connector footprint verification.
- `16_INSTALLER`: installer coordination layer and release-facing installer notes. The current Electron implementation remains under `installer` until a migration is explicitly approved.
- `17_RELEASE_BUILD`: release artifact staging, manifests, checksums, build reports, and release readiness records.
- `18_PUBLIC_DOCS`: public documentation coordination layer. Current public docs remain at repo root and `docs` until a migration is explicitly approved.
- `19_TEST_PROJECTS`: disposable test projects, toy KiCad examples, fixtures, and smoke-test workspaces. Prompt 8 added a planning-only ESP32-S3 sample AI workflow with no KiCad source files or manufacturing outputs.
- `20_CI_CD`: CI/CD planning, workflow standards, local CI notes, and release automation coordination.
- `21_LICENSE_ATTRIBUTION`: license, attribution, third-party, datasheet redistribution, and public-release risk audit records.
- `22_SECURITY`: security model, secret-handling rules, installer safety notes, and vulnerability-response support.
- `23_PACKAGE_PROFILES`: component package profiles, package-to-footprint rules, verification checklists, and placeholders for QFN, QFP, SOIC, SOT, modules, connectors, through-hole, and generic packages. Prompt 7 added QFN/QFP/SOIC/SOT-23/ESP32 module/USB-C generic placeholders, all `UNVERIFIED_PLACEHOLDER`.
- `24_FAB_PROFILES`: fabrication-house profile guidance, Gerber/drill/BOM/CPL/PNP/assembly note rules, and NOT_FINAL manufacturing export rules. Prompt 7 added JLCPCB and PCBWay generic output placeholders, both `UNVERIFIED_PLACEHOLDER`.
- `25_VENDOR_DATABASE`: vendor, manufacturer, distributor, lifecycle, source portal, official document link, and sourcing metadata. Prompt 7 added source-priority and lifecycle rules plus vendor folders for Espressif, STMicro, Microchip, TI, NXP, Nordic, Raspberry Pi, Molex, TE Connectivity, JST, Wurth, and generic suppliers.
- `26_AGENT_QUALITY`: AI quality, evidence, scorecard, uncertainty, and hallucination-risk support artifacts.
- `26_AGENT_QUALITY`: also contains local policy files and templates for self-review, truthfulness scoring, hallucination risk, response quality gates, evidence requirements, scorecards, claim/evidence matrices, and uncertainty logs.
- `27_EXAMPLES`: safe tutorials, toy records, and examples that must not be confused with production-approved data. Prompt 8 added EXAMPLE_ONLY folders for prompts, reports, memory/history, component records, datasheet summaries, and quality scorecards.
- `28_SUPPLIER_INGESTION`: supplier/distributor ingestion layer for official API-first, user CSV-second, manual source-link-third workflows. It stores connector scaffolds, no-secrets policies, normalization schemas, generated normalized metadata, and gap reports. It must not contain API keys, scraped supplier pages, private account data, restricted raw API payloads, or downloaded PDFs by default.
- `29_FOOTPRINT_GAP_ANALYSIS`: installed-KiCad footprint/symbol inventory and gap analysis layer. It stores read-only inventory scripts, generated local KiCad 9 footprint/symbol indexes, candidate matching reports, high-risk footprint warnings, connector/MCU/power gap reports, and a footprint verification backlog. Candidate matches remain `UNVERIFIED` until exact package drawings and human review evidence exist.
- `30_SUPPLIER_FOOTPRINT_MATCHES`: supplier SKU/MPN to KiCad symbol/footprint/3D model match layer. It stores match schemas, confidence rules, human-review rules, supplier-specific match records, EXAMPLE_ONLY records, match indexes, confidence reports, and unmatched supplier-part reports. Supplier package names are candidate metadata only and cannot verify high-risk footprints.
- `31_PLAYWRIGHT_RESEARCH_PIPELINE`: dry-run-first Playwright-assisted public-page evidence pipeline for supplier, datasheet, part-number, vendor, public KiCad library, and footprint-source research. It stores source policies, terms/rate-limit rules, Playwright usage rules, source profiles, target CSVs, guarded scripts, screenshot evidence rules, normalized schemas, integration docs, and reports. It must not contain credentials, cookies, browser profiles, scraped supplier HTML, CAPTCHA bypasses, private account data, mass-downloaded PDFs, or final approval claims.
- `32_OPEN_KICAD_SAMPLE_INTAKE`: controlled open KiCad sample project intake system. It stores candidate records, license screening, attribution, read-only imported originals, normalized sample copies, sample audits, review reports, benchmark-candidate promotion records, templates, and dry-run scripts. It must not contain random downloads, closed/proprietary projects, edited originals, active user projects, final manufacturing outputs, secrets, or public payload samples without `PUBLIC_BUNDLE_ALLOWED` status.
- Public release structure update: `16_INSTALLER`, `17_RELEASE_BUILD`, `18_PUBLIC_DOCS`, `20_CI_CD`, `21_LICENSE_ATTRIBUTION`, and `22_SECURITY` now contain production-facing planning, policy, checklist, and user-doc files. No binaries were built, no tools were installed, and root `README.md` now points users to `18_PUBLIC_DOCS/START_HERE_FOR_USERS.md`.
- Structure routing docs: `00_CODEX_START\STRUCTURE_STANDARD.md`, `FOLDER_ROUTING_RULES.md`, and `REPO_STRUCTURE_INDEX.md` define where new repo artifacts belong.
- Learning loop additions: global memory now includes `AGENT_LESSONS_LEARNED.md`, `AGENT_MISTAKES_TO_AVOID.md`, `USER_CORRECTIONS_MEMORY.md`, `VERIFIED_WORKFLOWS.md`, `FAILED_WORKFLOWS.md`, and `MEMORY_UPDATE_RULES.md`. Global history now includes `failed_attempts`, `issue_logs`, `user_corrections`, `lessons_learned`, `known_agent_mistakes`, and `workflow_runs`. Active projects now use local `memory/` and `history/` folders for project-specific decisions, corrections, failed attempts, issues, workflow runs, and verification runs.
- AI quality gate additions: startup now includes `AI_SELF_REVIEW_RULES.md`, `AI_TRUTHFULNESS_SCORING.md`, `AI_HALLUCINATION_RISK_RULES.md`, `AI_RESPONSE_QUALITY_GATE.md`, `AI_EVIDENCE_REQUIREMENTS.md`, `AI_UNCERTAINTY_DISCLOSURE_RULES.md`, `AI_ENGINEERING_CLAIM_RULES.md`, `AI_CLOSEOUT_SCORECARD_RULES.md`, and `CURRENT_KNOWN_PROBLEMS.md`. Closeout now requires an AI self-review, response scorecard, claim/evidence matrix for major engineering claims, uncertainty logs, hallucination-risk logs when needed, AI-quality index rebuild, and current-known-problems rebuild.
- Startup/closeout wiring update: Codex/Claude startup now explicitly reads `AGENTS.md`, `README_GPT.md`, `FOR CHAT GPT.MD`, `00_CODEX_START\START_HERE.md`, `SESSION_START_CHECKLIST.md`, `STRUCTURE_STANDARD.md`, `FOLDER_ROUTING_RULES.md`, `CURRENT_KNOWN_PROBLEMS.md`, `MEMORY_INDEX.md`, `HISTORY_INDEX.md`, and active project memory/history when project work is in scope. Closeout now rebuilds repo, memory, history, AI-quality, and known-problem indexes.
- Indexing scripts: `03_TOOLS\scripts\indexing\build_repo_index.py`, `build_memory_index.py`, `build_history_index.py`, and `build_known_problems.py` are safe, non-destructive startup/closeout index builders. They write generated Markdown/JSON indexes plus `01_MEMORY\MASTER_MEMORY_INDEX.md` and `02_HISTORY\MASTER_HISTORY_INDEX.md`.
- `installer`: future cross-platform installer architecture and release plan. Planning only; no binaries yet.
- `setup`: safe Windows, macOS, Linux, and common setup scripts. Installers are opt-in and must ask before installing anything.
- `99_BACKUPS`: pre-edit backups and recovery snapshots.
- `99_01 Finished PCBs`: read-only finished PCB reference library.

## Current tool status

- Playwright research pilot: on 2026-05-03, a five-part dry-run pilot for `31_PLAYWRIGHT_RESEARCH_PIPELINE` completed for STM32F103C8T6, ESP32-S3-WROOM-1, MCP2562FD, AP63203, and a generic USB-C 16-pin receptacle. Dry-run output is under `31_PLAYWRIGHT_RESEARCH_PIPELINE\output\20260503_121150_pilot`. Live browser capture is blocked because the local Node environment does not have the `playwright` package installed, and no tools were installed. All downstream updates from this pilot are `SOURCE_LINK_ONLY` or `UNVERIFIED`.
- Playwright batch expansion: on 2026-05-03, seven controlled dry-run batches added 72 source-link-only targets across ESP32, STM32, PIC/AVR, USB-C connectors, CAN, power/protection, RF connectors, antennas, test pads, mounting holes, headers, and terminal blocks. Batch reports are under `31_PLAYWRIGHT_RESEARCH_PIPELINE\reports\BATCH_*`. Normalized dry-run output is under `31_PLAYWRIGHT_RESEARCH_PIPELINE\output\20260503_122259_batch_expansion`. Live browser capture is still blocked because Playwright is not installed. All records remain `UNVERIFIED` or `SOURCE_LINK_ONLY`; no PDFs, credentials, supplier API calls, or KiCad design edits were performed.
- VS Code workspace support: added on 2026-05-02. Files are `.vscode\settings.json`, `.vscode\extensions.json`, `.vscode\tasks.json`, and `.vscode\launch.json`. User/agent entry docs are `START_HERE_FOR_USERS.md`, `START_HERE_FOR_AI_AGENTS.md`, `QUICKSTART_WINDOWS.md`, `QUICKSTART_MACOS.md`, and `QUICKSTART_LINUX.md`. Tasks include health check, KiCad app audit, datasheet index, component database file index, project validation, ERC, DRC, NOT_FINAL review export, prompt pack folder open, and setup report generation. Users must install and log in to Codex, Claude, or another AI tool themselves; no AI credentials are stored or assumed.
- Setup and health-check support: added on 2026-05-02. Top-level scripts are `health_check.ps1` and `health_check.py`; template is `HEALTH_CHECK_REPORT_TEMPLATE.md`. Setup folders are `setup\windows`, `setup\macos`, `setup\linux`, and `setup\common`. Common helpers create folders, build local indexes, and write setup reports. OS installer scripts are interactive only, use package managers where possible, never silently install paid tools, never store API keys, and do not modify KiCad project files.
- Installer plan: added on 2026-05-02 under `installer`. It designs the future Windows-first cross-platform installer but does not create binaries. The plan says v1 must use the user's installed KiCad app, not bundle KiCad, not store AI credentials, not require paid APIs, not modify installed KiCad folders, optionally install missing requirements only after confirmation, configure VS Code, install prompt packs, create datasheet/component scaffolding, run health check, and open VS Code. Milestones run v0.1 repo template through v1.0 public GitHub release.
- Installer payload template: added on 2026-05-02 under `installer\payload`. Build with `installer\payload\build_payload.ps1` or `python installer/payload/build_payload.py`. The generated clean workspace is `installer\payload\repo-template`, with `payload.manifest.json` and `PAYLOAD_BUILD_REPORT.md`. The builder excludes third-party repos, Python/Node environments, old logs, backups, generated outputs, local active projects, downloaded PDFs, and machine-local Codex config; it generates clean memory/history/project/output state. Latest payload health check reported PASS=97, WARN=0, FAIL=0.
- Cross-platform Electron installer project: added on 2026-05-02 under `installer`. It includes `package.json`, `electron-builder.yml`, `src\main.js`, `src\preload.js`, `src\renderer`, `src\installer-core`, platform dependency manifests, payload scripts, build output folders, and docs. npm scripts are `dev`, `build:win`, `build:mac`, `build:linux`, and `package`. Static checks and installer-core smoke test passed, including a disposable workspace under `05_OUTPUTS\installer_smoke_test` with health check PASS=97, WARN=0, FAIL=0. Electron packaging binaries were not built because npm dependencies were not installed; do not call it production-ready.
- Public GitHub release docs: added on 2026-05-02. Public files now include `LICENSE`, `CONTRIBUTING.md`, `SECURITY.md`, `CODE_OF_CONDUCT.md`, `CHANGELOG.md`, `ROADMAP.md`, `DISCLAIMER.md`, and `PUBLIC_RELEASE_CHECKLIST.md`. The public README now explains installed-KiCad use, VS Code, Codex, Claude, datasheet database, component database, verification scripts, non-goals, no official KiCad affiliation, no fabrication approval, and link-only datasheet handling when redistribution rights are not confirmed.
- Prompt pack system: added on 2026-05-02 at `.prompts`. Use `.prompts\codex` for Codex task prompts, `.prompts\claude` for Claude task prompts, `.prompts\shared` for safety, component research, datasheet summary, KiCad verification, and GitHub release standards, and `.prompts\kicad_pipeline` for the reusable 17-stage schematic-to-PCB-to-routing-to-NOT_FINAL-fabrication workflow. Prompts require startup reads, no KiCad project edits without active project confirmation and backup, history logs, verification reports, no fake datasheet claims, no unverified footprint approval, and `NOT_FINAL` labels for generated manufacturing-style outputs.
- Supplier ingestion system: added on 2026-05-03 at `28_SUPPLIER_INGESTION`. Read `SOURCE_POLICY.md`, `API_KEY_HANDLING.md`, `SUPPLIER_CONNECTOR_STANDARD.md`, and the relevant connector folder before importing supplier data. Digi-Key, Mouser, JLCPCB, and LCSC now have connector stubs that default to `DRY_RUN`, normalize local/sample JSON, output normalized JSON, never download PDFs by default, never print/store API keys, and refuse live API behavior unless `--live` is explicitly requested. Live API calls are guarded but not implemented or tested. Other scripts are offline placeholders for CSV/JSON normalization, indexing, gap reports, component database text matching, and conservative footprint candidate notes. No scraping, installs, downloads, or credentials were added.
- Footprint gap analysis system: added on 2026-05-03 at `29_FOOTPRINT_GAP_ANALYSIS`. Read `README.md` and `INDEX.md` before using installed KiCad footprint candidates. Current local KiCad 9 inventory found 155 footprint libraries with 15,415 footprints and 223 symbol libraries with 22,582 symbols. Component database matching checked 125 records; 107 had candidate matches, 18 had no candidate match, and all 125 remain unverified for exact package drawing/human review.
- Supplier footprint match system: added on 2026-05-03 at `30_SUPPLIER_FOOTPRINT_MATCHES`. Read `MATCH_SCHEMA.md`, `MATCH_CONFIDENCE_RULES.md`, and `HUMAN_REVIEW_REQUIRED_RULES.md` before linking Mouser/Digi-Key/JLCPCB/LCSC/manual supplier identifiers to KiCad footprints. Scripts create records, check confidence, build indexes, and report unmatched supplier parts. Current starter set has 6 EXAMPLE_ONLY records; all require human review and none are production footprint approvals.
- Supplier/datasheet/footprint final audit: completed on 2026-05-03. Classification is `INTERNAL_ALPHA`; do not call these systems production-ready. Reports: `02_HISTORY\design_reviews\SUPPLIER_DATASHEET_FOOTPRINT_FINAL_AUDIT.md`, `05_OUTPUTS\release_readiness\SUPPLIER_DATASHEET_FOOTPRINT_SCORECARD.md`, `SUPPLIER_DATASHEET_FOOTPRINT_BLOCKERS.md`, and `SUPPLIER_DATASHEET_FOOTPRINT_NEXT_STEPS.md`. Main blockers: two legacy Espressif PDFs in the datasheet inbox require redistribution review or public-payload exclusion, supplier connectors are dry-run only, supplier-footprint records are example-only, and no exact package-drawing verified footprint approvals exist.
- Playwright research pipeline: added on 2026-05-03 at `31_PLAYWRIGHT_RESEARCH_PIPELINE`. Read `SOURCE_POLICY.md`, `TERMS_AND_RATE_LIMIT_RULES.md`, `PLAYWRIGHT_USAGE_RULES.md`, and the relevant `source_profiles\*.profile.md` before browser-assisted research. Scripts default to `DRY_RUN`; `--live` is required for browser execution; no live browsing was run during setup; no PDFs were downloaded. Pilot dry-run report: `31_PLAYWRIGHT_RESEARCH_PIPELINE\reports\PILOT_RESEARCH_DRY_RUN_REPORT.md`; output JSON: `31_PLAYWRIGHT_RESEARCH_PIPELINE\output\pilot_dry_run\research_plan.json`. Captured browser data is evidence, not truth, and remains `UNVERIFIED` until official-source or human review.
- KiCad installed app intelligence: added on 2026-05-02. Read `02_HISTORY\design_reviews\KICAD_INSTALLED_APP_DEEP_AUDIT.md` plus `03_TOOLS\kicad_app_intelligence\KICAD_9_WINDOWS_PATH_MAP.md`, `KICAD_CLI_COMMANDS_REFERENCE.md`, `KICAD_LIBRARY_DISCOVERY_GUIDE.md`, `KICAD_DO_NOT_TOUCH_RULES.md`, and `KICAD_AGENT_TASK_MAP.md` before building new installed-KiCad integration workflows.
- KiCad agent operating docs: `00_CODEX_START\KICAD_AGENT_OPERATING_MANUAL.md` and `00_CODEX_START\KICAD_SAFE_AUTOMATION_RULES.md` define how VS Code-based agents should choose between direct parsing, `kicad-cli`, `pcbnew` Python, screenshots, and GUI automation.
- KiCad app audit scripts: `03_TOOLS\scripts\kicad_app_audit\audit_kicad_windows.ps1`, `check_kicad_cli.ps1`, and `inventory_kicad_libraries.ps1`. They are read-only, write reports to `02_HISTORY` or `05_OUTPUTS`, and must not write into `C:\Program Files\KiCad`.
- KiCad 9 app audit result: `C:\Program Files\KiCad\9.0\bin`, `etc`, `lib`, and `share` exist; `kicad-cli version` reports `9.0.7`; stock assets include 224 symbol files, 155 footprint libraries with 15,415 footprints, and 105 3D model folders with 14,043 files.
- Datasheet research pipeline: added on 2026-05-02. Read `06_DATASHEETS\00_INDEX\RESEARCH_PIPELINE.md`, `PUBLIC_RELEASE_DATASHEET_POLICY.md`, `SOURCE_PRIORITY_RULES.md`, `VENDOR_DOWNLOAD_RULES.md`, and `LINK_ONLY_VS_BUNDLED_POLICY.md` before researching or collecting datasheets. Use `03_TOOLS\scripts\datasheets\validate_datasheet_links.py`, `build_datasheet_index.py`, `create_missing_datasheet_report.py`, and `generate_component_summary_stub.py` for metadata reports and AI-readable summary stubs. These scripts do not download by default; their future `--download` flag is intentionally disabled until licensing and redistribution handling are explicitly approved.
- Microcontroller family content generator: added and used on 2026-05-03 at `03_TOOLS\scripts\datasheet_tree\create_microcontroller_family_content.py` with schema `family_content_schema.json` and templates under `templates`. It creates useful AI-readable family folders for STM32, ESP32, PIC/dsPIC, AVR, RP2040/RP2350, Nordic, NXP, TI, Silicon Labs, Renesas, Infineon, GigaDevice, WCH, and Atmel-style folders from conservative stubs. It is offline, performs no PDF downloads or scraping, marks unknowns `UNKNOWN_REQUIRES_SOURCE`, skips substantive existing files unless `--force` is passed, and supports `--overwrite-weak` for obvious placeholder boilerplate. Latest batch upgraded 48 MCU folders, created 612 new files, and replaced 141 weak placeholders. Evidence: `05_OUTPUTS\datasheet_tree\MCU_TREE_COMPLETION_SUMMARY.md` and `02_HISTORY\design_reviews\MCU_DATASHEET_TREE_UPGRADE_REPORT.md`.
- STM32 datasheet tree update: added on 2026-05-03. Read `06_DATASHEETS\01_MICROCONTROLLERS\STMICRO_STM32\STM32_AI_MASTER_INDEX.md` and `08_COMPONENT_DATABASE\01_MICROCONTROLLERS\STM32_AI_DESIGN_GUIDE.md` before STM32 schematic, symbol, footprint, package, or source-link work. The STM32 family tree now has AI-readable summaries for 19 families, but classification remains `SCAFFOLDED_WITH_AI_SUMMARIES`; exact values remain `UNKNOWN_REQUIRES_SOURCE`.
- STM32 source-link index update: added on 2026-05-03. `06_DATASHEETS\01_MICROCONTROLLERS\STMICRO_STM32\STM32_OFFICIAL_SOURCE_LINKS.csv`, `STM32_PART_NUMBER_INDEX.csv`, and `STM32_DEV_BOARD_INDEX.csv` now provide official/public link-only metadata. They are `PARTIALLY_RESEARCHED_SOURCE_LINKS`, not verified exact design data.
- STM32F1 pilot content update: added on 2026-05-03 under `06_DATASHEETS\01_MICROCONTROLLERS\STMICRO_STM32\STM32F1`. Read `STM32F1_AI_OVERVIEW.md`, `STM32F103C8T6_PART_RECORD.md`, `STM32F103C8T6_SCHEMATIC_NOTES.md`, `STM32F103C8T6_BOOT_DEBUG_NOTES.md`, `STM32F103C8T6_POWER_CLOCK_NOTES.md`, `STM32F103C8T6_PACKAGE_FOOTPRINT_NOTES.md`, `STM32F1_KICAD_SYMBOL_FOOTPRINT_NOTES.md`, and `STM32F1_NEEDS_REVIEW.md` before using STM32F103C8T6. Component records now exist at `08_COMPONENT_DATABASE\01_MICROCONTROLLERS\STM32F103C8T6.md` and `08_COMPONENT_DATABASE\12_KICAD_SYMBOL_FOOTPRINT_MATCHES\STM32F103C8T6_MATCH.md`. No PDFs were downloaded; KiCad symbol/footprint/3D model matches are candidates only and remain human-review-required until exact ST package drawing and pinout review are complete.
- Component database: added on 2026-05-02 at `08_COMPONENT_DATABASE`. Read `08_COMPONENT_DATABASE\00_INDEX\COMPONENT_DATABASE_README.md`, `MASTER_COMPONENT_INDEX.md`, `PART_SCHEMA.md`, `VERIFICATION_LEVELS.md`, `AI_USAGE_RULES.md`, and `KICAD_SYMBOL_FOOTPRINT_LINKING_RULES.md` before using component records. Initial records in `EXAMPLE_COMPONENT_RECORDS.md` and `example_component_records.json` are all `UNVERIFIED_PLACEHOLDER` and must not be used as approved design data.
- Core component intelligence update: added on 2026-05-02. Read `08_COMPONENT_DATABASE\00_INDEX\DO_NOT_GUESS_RULES.md` before using any component record for schematic, PCB, BOM, or manufacturing-related work. New scaffold folders are `08_COMPONENT_DATABASE\15_PACKAGE_FOOTPRINT_DATABASE` and `08_COMPONENT_DATABASE\16_VERIFICATION_RECORDS`. Starter records live in `08_COMPONENT_DATABASE\99_UNVERIFIED_INBOX\core_starter_records` and are all `UNVERIFIED_PLACEHOLDER` with human review required.
- Accuracy engine: added on 2026-05-03 at `09_ACCURACY_ENGINE`. It defines schematic rules, PCB rules, verification rules, and workflows so agents stop guessing. Every component needs a source, every symbol needs pinout evidence, every footprint needs exact package drawing verification or `UNVERIFIED_FOOTPRINT`, connector orientation and polarity-sensitive parts require review, RF/USB/CAN parts require layout-specific review, and manufacturing outputs remain `NOT_FINAL`.
- Accuracy engine + AI quality gate update: added on 2026-05-02. Before making engineering claims, agents must use `09_ACCURACY_ENGINE\checklists\ACCURACY_GATE_CHECKLIST.md` and `26_AGENT_QUALITY`. Every meaningful session with engineering claims must create a self-review, scorecard, uncertainty log, and claim/evidence matrix; hallucination-risk logs are required for guessed, inferred, weakly sourced, or contradicted claims.
- Schematic-to-PCB gate update: added on 2026-05-03. Before any PCB update from schematic, PCB creation, placement, routing, zone creation, or PCB manufacturing-style output, agents must read `09_ACCURACY_ENGINE\workflows\SCHEMATIC_TO_PCB_GATE_WORKFLOW.md`, `09_ACCURACY_ENGINE\checklists\SCHEMATIC_READY_FOR_PCB_CHECKLIST.md`, `09_ACCURACY_ENGINE\checklists\PCB_UPDATE_FROM_SCHEMATIC_CHECKLIST.md`, `09_ACCURACY_ENGINE\verification_rules\SCHEMATIC_TO_PCB_BLOCKERS.md`, `09_ACCURACY_ENGINE\verification_rules\NEEDS_REVIEW_BLOCKER_RULES.md`, and the active project's `reports\SCHEMATIC_TO_PCB_GATE_STATUS.md`. If the gate is not exactly `PASS`, PCB work is forbidden.
- Full KiCad pipeline prompt pack: added on 2026-05-03. Future project work should use `00_CODEX_START\KICAD_PIPELINE_STARTUP_RULES.md`, `09_ACCURACY_ENGINE\workflows\FULL_KICAD_PROJECT_PIPELINE.md`, `09_ACCURACY_ENGINE\checklists\FULL_PIPELINE_GATE_CHECKLIST.md`, and `.prompts\kicad_pipeline\01_*.md` through `17_*.md`. Pipeline gate exceptions require explicit LJ approval and a logged reason, risk, evidence path, and `HUMAN_REVIEW_REQUIRED`.
- Schematic annotation/completeness checkers: added on 2026-05-03 at `03_TOOLS\scripts\kicad_schematic_checks`. Run `check_schematic_annotation.py`, `check_schematic_completeness.py`, `check_bom_lock_alignment.py`, and `check_needs_review_markers.py` before marking a schematic layout-ready. These are read-only screeners and do not approve footprints, pinouts, connector orientation, or manufacturing readiness.
- Automatic schematic close-up visual crops: added on 2026-05-03. Use `03_TOOLS\kicad\run_schematic_visual_check.ps1` to export full-page schematic SVG/PDF, optionally render PNG, generate crop SVG/PNG files from `_verification\schematic_visual\visual_blocks.json`, and create `reports\CLOSE_UP_REVIEW.md`. Script support is read-only for KiCad files; crop config/output files are verification artifacts, not KiCad design edits.
- Knowledge base: added on 2026-05-03 at `10_KNOWLEDGE_BASE`. It contains 51 AI-readable files covering reusable circuits, schematic/PCB design patterns, pre-review checklists, common mistakes, manufacturing package rules, and AI-agent anti-hallucination guidance. Agents must still verify exact values against datasheets, connector drawings, package drawings, KiCad ERC/DRC, and human review gates.
- Knowledge base Prompt 4 update: required reusable circuit pages and common-mistake pages are present, and `10_KNOWLEDGE_BASE\common_mistakes\PIC_COMMON_MISTAKES.md` was added. Treat the knowledge base as guidance only, not datasheet proof.
- Library factory: added on 2026-05-03 at `11_LIBRARY_FACTORY`. It defines symbol creation, footprint creation, package-to-footprint mapping, project-local library rules, connector footprint rules, 3D model review guidance, cross-cutting library QA workflow, and basic read-only validation scripts. Scripts can flag risks but do not approve symbols, footprints, 3D models, or mappings. The structure now includes `symbols`, `footprints`, `mapping`, `3d_models`, `qa`, and `scripts`.
- Reference design library: added on 2026-05-03 at `12_REFERENCE_DESIGN_LIBRARY`. It defines link-first reference design records, source/license rules, verification levels, and category checklists for ESP32, STM32, PIC/AVR, power, USB, CAN, RF, and automotive examples. Do not copy proprietary designs without permission; reference designs are evidence, not automatic approval.
- Reference design Prompt 4 update: `12_REFERENCE_DESIGN_LIBRARY\00_INDEX` now uses `VERIFIED`, `PARTIALLY_VERIFIED`, `LINK_ONLY`, and `UNVERIFIED` statuses. Starter official/vendor portal records are link-only and must not be copied or treated as fully verified designs.
- Part ingestion: added on 2026-05-03 at `13_PART_INGESTION`. It defines a workflow and scripts to generate datasheet summary, component record Markdown/JSON, symbol checklist, and footprint checklist stubs from user-provided metadata. It does not scrape, download, redistribute PDFs, or verify values automatically.
- Layout automation reality check: added on 2026-05-03 at `14_LAYOUT_AUTOMATION`. It documents what KiCad, `kicad-cli`, `pcbnew` Python, the IPC API, and FreeRouting may support, while requiring copied-project experiments, DRC before/after, and human layout review before any layout automation claim.
- Benchmark framework: added on 2026-05-03 at `15_BENCHMARKS`. It defines methodology, six starter benchmark tasks, scoring rubrics, and an empty results policy so KiCad Engine can measure progress without fake scores.
- `kicad-mcp-pro`: installed and configured project-locally for Codex in analysis/safe mode only.
- `kicad-happy`: installed for analysis-only KiCad review support.
- KiBot: installed in an isolated Python environment; not production-proven on a real project.
- InteractiveHtmlBom: installed/help-tested; not project-tested on a real design.
- PcbDraw: installed/help-tested; not project-tested on a real design.
- KiCanvas: isolated Node build tested; not project-tested on real KiCad files.
- `KiCAD-MCP-Server`: cloned but not installed or configured.
- Windows GUI automation: `03_TOOLS\python_envs\windows_gui` is installed with `pywinauto`, `PyAutoGUI`, `PyGetWindow`, `pyperclip`, `pillow`, `opencv-python`, and `psutil`; import-checked only. Do not control KiCad until a future gated task approves it.
- Windows GUI helper repos: FlaUI, FlaUInspect, AutoHotkey, and SikuliX1 are cloned under `03_TOOLS\windows\repos`; not installed, not built, and not approved for KiCad control.
- KiCad GUI discovery workflow: passive scripts exist for KiCad window discovery, UIA inspection, Win32 inspection, and visible KiCad-window screenshots. The false-positive filter was fixed on 2026-04-30: high confidence now requires process name `kicad.exe`, `eeschema.exe`, or `pcbnew.exe`; title-only matches are `LOW_CONFIDENCE_TITLE_ONLY` and cannot be inspected, screenshotted, or controlled. A confirmed read-only run found `kicad.exe` PID `19576`, title `COMMAND LINK DRAFT â€” KiCad 9.0`; UIA recorded 65 controls, Win32 recorded 241 controls, and one screenshot was captured.
- Linux/headless automation: planning docs and safe starter scripts exist under `03_TOOLS\linux`; no Linux tools installed, WSL not assumed configured, and no Linux automation has been run.
- Verification scripts: present in `03_TOOLS\scripts`; clean sample success path was validated, but outputs are still review-only and `NOT_FINAL`.
- Platform tool roots: `03_TOOLS\common`, `03_TOOLS\windows`, and `03_TOOLS\linux` exist for future organization. Legacy paths `03_TOOLS\repos`, `03_TOOLS\scripts`, `03_TOOLS\python_envs`, `03_TOOLS\node_envs`, and `03_TOOLS\tool_logs` remain valid until migration is explicitly approved.
- Startup root now includes `00_CODEX_START\CONTROL_PLANES.md` as the authoritative startup summary for common, Windows GUI, and Linux/headless control-plane selection.
- Health check: latest report shows PASS 72, WARN 5, FAIL 0, blockers none.

## Control-plane model

Use common/project intelligence first whenever possible:

- `kicad-cli`
- KiBot
- `pcbnew` Python
- MCP analysis tools
- file validators
- BOM/Gerber/PNP parsers

Use Windows GUI hands/eyes only when common tools are insufficient:

- pywinauto
- FlaUI
- AutoHotkey
- PyAutoGUI
- screenshot tools
- SikuliX

Start with discovery only. Do not use coordinate clicks without screenshots. Do not randomly type into KiCad. Do not run production project GUI automation until the project is identified and backed up. Record screenshots and logs.

Use Linux/headless/CI for repeatable validation:

- Linux `kicad-cli`
- KiBot
- Xvfb
- xdotool
- wmctrl
- dogtail
- Docker

Run headless checks first. Do not write to production projects unless working on an approved copied project. Scripts must be repeatable and logged.

Tool selection rule: prefer CLI/API/MCP over GUI automation, prefer read-only inspection before edits, prefer copied project workspaces over original projects, and prefer `NOT_FINAL` outputs until the verification gate passes.

## MCP status

`kicad-mcp-pro` is configured in:

`C:\Users\LJ\GitHub\KICAD_ENGINE\.codex\config.toml`

Current server name: `kicad_mcp_pro_analysis`

Current authority: analysis/safe mode only. Do not enable write, destructive, parallel shared-state, or manufacturing/export authority unless current files and LJ explicitly approve it for a specific active project after backups and verification plans are confirmed.

## Active project status

From `00_CODEX_START\CURRENT_PROJECT.md`:

- Active project name: `ESP32_CSI_WIFI_NODE`
- Active project path: `C:\Users\LJ\GitHub\KICAD_ENGINE\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE`
- Current task mode: `ACTIVE_DESIGN_PROJECT_SCHEMATIC_ERC_CLEAN_GATE_FAIL`
- Current priority: resolve remaining high-risk review blockers before any PCB update.

This is an active design project workspace for a complete custom ESP32-S3 CSI WiFi node PCB. It is not a carrier board and not a board for plugging in an ESP32 development board.

Read-only inspection on 2026-05-03 found `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pro` and `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch`. No `.kicad_pcb` file was found in the active project scan.

Do not create or edit KiCad design files until LJ explicitly requests that next step and the active project, backup plan, verification plan, and rollback plan are confirmed. Schematic edits are allowed only under that backup/verification gate. Do not update PCB from schematic, place parts, route traces, create zones, or generate PCB manufacturing outputs unless `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\SCHEMATIC_TO_PCB_GATE_STATUS.md` is exactly `PASS`.

Current exception: on 2026-04-30 LJ explicitly approved direct repair/review/re-export work in a user-local `99_01 Finished PCBs\COMMAND LINK` reference folder. That finished-PCB source folder is not present in every checkout. This does not make all finished PCB originals generally editable; future direct edits still need explicit approval, snapshot, rollback, and logs.

## Finished PCB reference library

Finished PCB references may live in a user-local reference folder:

`99_01 Finished PCBs`

This folder is optional and may be absent from the current checkout. If it is absent, use the copied review workspace and historical reports only.

Current reference project:

- `COMMAND LINK`: finished Fiverr-verified PCB reference, indexed read-only on 2026-04-30.

Review copy:

- `04_KICAD_PROJECTS\active\COMMAND_LINK_VERIFIED_REFERENCE`: copied review/reference workspace created for read-only Codex review and learning. It is not an active design revision.

Original finished PCB files are read-only references by default. If edits or experiments are needed, copy the project to a safe review/work area first unless LJ explicitly approves direct finished-folder work.

Direct approved session:

- Snapshot: `99_BACKUPS\project_snapshots\COMMAND_LINK_DIRECT_EDIT_APPROVED_20260430_203134`
- Review folder: `99_01 Finished PCBs\COMMAND LINK\Codex Review Outputs\20260430_203134`
- New outputs: `99_01 Finished PCBs\COMMAND LINK\Codex Review Outputs\20260430_203134\new_outputs_NOT_FINAL`
- Direct edit review: `02_HISTORY\design_reviews\COMMAND_LINK_DIRECT_EDIT_REVIEW.md`
- ERC/DRC report: `02_HISTORY\erc_drc_reports\COMMAND_LINK_DIRECT_EDIT_ERC_DRC_REPORT.md`
- Session log: `02_HISTORY\sessions\COMMAND_LINK_DIRECT_EDIT_SESSION.md`
- Result: ERC passed with 0 warnings; DRC still failed with 44 violations. New exports are `NOT_FINAL`, not fabrication-ready.

Direct DRC continuation:

- Snapshot: `99_BACKUPS\project_snapshots\COMMAND_LINK_DRC_CONTINUATION_20260430_210726`
- Review folder: `99_01 Finished PCBs\COMMAND LINK\Codex Review Outputs\20260430_210726`
- New outputs: `99_01 Finished PCBs\COMMAND LINK\Codex Review Outputs\20260430_210726\new_outputs_NOT_FINAL`
- Review: `02_HISTORY\design_reviews\COMMAND_LINK_DRC_CONTINUATION_REVIEW.md`
- ERC/DRC report: `02_HISTORY\erc_drc_reports\COMMAND_LINK_DRC_CONTINUATION_ERC_DRC_REPORT.md`
- Session log: `02_HISTORY\sessions\COMMAND_LINK_DRC_CONTINUATION_SESSION.md`
- Command log: `02_HISTORY\command_logs\COMMAND_LINK_DRC_CONTINUATION_COMMANDS.md`
- Result: ERC passed with 0 warnings and DRC passed with 0 violations. Outputs remain `NOT_FINAL`, not fabrication-ready.

Final fabrication readiness audit:

- Report: `02_HISTORY\design_reviews\COMMAND_LINK_FINAL_FAB_READINESS_AUDIT.md`
- Session log: `02_HISTORY\sessions\COMMAND_LINK_FINAL_FAB_READINESS_AUDIT_SESSION.md`
- Command log: `02_HISTORY\command_logs\COMMAND_LINK_FINAL_FAB_READINESS_AUDIT_COMMANDS.md`
- Manifest: `99_01 Finished PCBs\COMMAND LINK\Codex Review Outputs\20260430_210726\new_outputs_NOT_FINAL\PACKAGE_MANIFEST.md`
- Classification: `HUMAN_REVIEW_REQUIRED`.
- Reason: ERC/DRC are clean and the package contains Gerbers, Excellon drills, BOM, PNP, PDFs, STEP, ERC report, and DRC report, but connector pinout/orientation, polarity/orientation, manual assembly treatment for J2/J3/J4, PNP package metadata, plated mounting-hole intent, and missing 3D models require human confirmation.

Inventory report:

- `02_HISTORY\design_reviews\COMMAND_LINK_FINISHED_PCB_INVENTORY.md`

Current reference-review templates:

- `04_KICAD_PROJECTS\templates\FINISHED_PCB_REVIEW_CHECKLIST.md`
- `04_KICAD_PROJECTS\templates\REFERENCE_PROJECT_FOLDER_STANDARD.md`

COMMAND LINK lessons have been added to memory as evidence-backed observations only. Observed parts are not approved preferred components, and observed fabrication package structure is not a default fab-house rule.

## Current known blockers/warnings

- Product vision and architecture docs were added on 2026-05-02. They position KiCad Engine as a transparent, local, auditable, KiCad-native alternative direction to cloud-first PCB AI tools, but not as a KiCad replacement or a fabrication-approval system.
- Product gap audit warns that public-release readiness still needs path normalization, public README/license/release hygiene, setup packaging, `.vscode`/Claude integration files, datasheet/component/footprint schemas, and demonstrated sample workflows.
- The earlier 2026-05-02 gap around top-level VS Code/setup/installer/release support has been substantially addressed. Current roots include `.vscode`, `.prompts`, `setup`, `installer`, `16_INSTALLER`, `17_RELEASE_BUILD`, `18_PUBLIC_DOCS`, `20_CI_CD`, and `05_OUTPUTS\release_packages`. Installer and release support still require platform build/smoke tests before production claims.
- `06_DATASHEETS` was restructured on 2026-05-02 into a professional numbered datasheet library with `00_INDEX`, category folders `01_MICROCONTROLLERS` through `19_VENDOR_PORTALS`, and `99_UNSORTED_INBOX`. Existing weak folders were preserved under `06_DATASHEETS\99_UNSORTED_INBOX\LEGACY_MIGRATION_20260502_161444`; the two existing Espressif PDFs remain there pending source/revision/copyright curation. Read `06_DATASHEETS\00_INDEX\DATASHEET_LIBRARY_README.md`, `MASTER_DATASHEET_INDEX.md`, `VERIFIED_SOURCE_RULES.md`, `COPYRIGHT_AND_LINKING_POLICY.md`, and `MIGRATION_LOG_20260502_161444.md` before relying on datasheet contents.
- Datasheet research is metadata-first. Public release should link to vendor sources and generated summaries unless redistribution permission is confirmed. Do not mass-download, scrape aggressively, bypass vendor restrictions, or commit restricted PDFs into the public repo.
- Platform control-layer audit completed on 2026-04-30: PASS, readiness score 94 / 100. See `02_HISTORY\design_reviews\PLATFORM_CONTROL_LAYERS_AUDIT.md`.
- Startup/control-plane synchronization completed on 2026-04-30. `CONTROL_PLANES.md` is now part of the `AGENTS.md` startup read order.
- Latest no-write health check on 2026-05-03 reported PASS=131, WARN=0, FAIL=0. No hard health-check blockers are currently recorded.
- Final production structure audit completed on 2026-05-03. Audit: `02_HISTORY\design_reviews\FINAL_PRODUCTION_STRUCTURE_AUDIT.md`; scorecard: `05_OUTPUTS\release_readiness\FINAL_STRUCTURE_SCORECARD.md`; classification: `INTERNAL_ALPHA_READY`. Public release blockers remain dependency/environment exclusion, PDF redistribution review, generated/reference artifact cleanup, old command-log scrubbing, Git worktree verification, installer platform smoke tests, and verified data maturity.
- `ESP32_CSI_WIFI_NODE` schematic repair pass on 2026-05-03 cleaned ERC to 0 errors and 0 warnings. Repair artifacts: `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\SCHEMATIC_ELECTRICAL_AUDIT.md`, `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\ESP32_CSI_WIFI_NODE_SCHEMATIC_ELECTRICAL_BLOCKERS_ERC.txt`, `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\SCHEMATIC_CLOSE_UP_VISUAL_REVIEW.md`, and backup `99_BACKUPS\pre_codex_edits\ESP32_CSI_WIFI_NODE_SCHEMATIC_ELECTRICAL_BLOCKERS_20260503_073335`.
- `ESP32_CSI_WIFI_NODE` schematic-to-PCB gate is currently `FAIL`, not `PASS`. Gate file: `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\SCHEMATIC_TO_PCB_GATE_STATUS.md`. Remaining blockers include missing BOM lock/parts/review files, AO3401A pin mapping and footprint orientation, USB VBUS/backfeed policy, USB shield strategy, unverified regulator passives, USB-C connector/ESD/series resistor review, ESP32 EN/BOOT source verification, footprint/package drawing audit, connector orientation review, polarity review, and human review of all high-risk `NEEDS_REVIEW` items.
- `ESP32_CSI_WIFI_NODE` footprint/package audit on 2026-05-03 failed. Report: `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\FOOTPRINT_PACKAGE_AUDIT.md`. Read-only schematic parsing found 43 physical symbols, 0 assigned footprints, and 0 populated datasheet fields. PCB update remains forbidden until exact footprints, package drawings, datasheet/source links, connector orientation review, polarity review, and human review are complete.
- `ESP32_CSI_WIFI_NODE` PCB update request on 2026-05-03 was correctly blocked and not run because `reports\SCHEMATIC_TO_PCB_GATE_STATUS.md` is `FAIL`, not `PASS`. No `.kicad_pcb` file was found, no backup was created for this blocked no-op, no DRC was run, and no KiCad design files were edited. Report: `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\PCB_UPDATE_FROM_SCHEMATIC_REPORT.md`.
- `ESP32_CSI_WIFI_NODE` PCB mechanical setup request on 2026-05-03 was blocked and not run. Reasons: no `.kicad_pcb` file exists, PCB is not synced from schematic, board size is unknown, no `notes\mechanical*.md` file exists, and requirements still list exact board outline/enclosure/mounting details as open questions. Reports: `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\PCB_MECHANICAL_SETUP_REPORT.md` and `reports\BOARD_SIZE_NEEDS_USER_REVIEW.md`.
- `ESP32_CSI_WIFI_NODE` PCB placement pass 1 request on 2026-05-03 was blocked and not run. Reasons: no `.kicad_pcb` file exists, no board outline exists, PCB update from schematic is `NOT_RUN_GATE_FAIL`, and mechanical setup is `NOT_RUN_BLOCKED`. Report: `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\PCB_PLACEMENT_PASS_1_REPORT.md`.
- `ESP32_CSI_WIFI_NODE` PCB placement pass 2 orientation request on 2026-05-03 was blocked and not run. Reasons: placement pass 1 is `PLACEMENT_FAIL`, no `.kicad_pcb` file exists, no board outline exists, schematic-to-PCB gate is `FAIL`, and no footprints exist for orientation/courtyard/readability review. Report: `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\PCB_PLACEMENT_PASS_2_ORIENTATION_REPORT.md`.
- `ESP32_CSI_WIFI_NODE` hole/test-pad/via strategy request on 2026-05-03 was blocked and not run. Reasons: no `.kicad_pcb` file exists, placement pass 2 is `PLACEMENT_ORIENTATION_FAIL`, no board outline/stackup/placement exists, and no selected verified fab drill/via limits exist. Report: `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\THROUGH_HOLE_TEST_PAD_VIA_STRATEGY.md`.
- `ESP32_CSI_WIFI_NODE` copper zone/ground-plane strategy request on 2026-05-03 was blocked and not run. Reasons: no `.kicad_pcb` file exists, no board outline exists, schematic-to-PCB gate is `FAIL`, placement pass 2 is `PLACEMENT_ORIENTATION_FAIL`, and hole/test-pad/via strategy is `HOLE_PAD_VIA_FAIL`. Report: `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\COPPER_ZONE_STRATEGY_REPORT.md`.
- `ESP32_CSI_WIFI_NODE` PCB routing plan request on 2026-05-03 created a planning-only report and remains blocked. Reasons: no `.kicad_pcb` file exists, schematic-to-PCB gate is `FAIL`, placement pass 2 is `PLACEMENT_ORIENTATION_FAIL`, hole/test-pad/via strategy is `HOLE_PAD_VIA_FAIL`, and copper-zone strategy is `ZONE_SETUP_FAIL`. No traces were routed and no KiCad design files were edited. Report: `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\PCB_ROUTING_PLAN.md`.
- `ESP32_CSI_WIFI_NODE` critical-net routing request on 2026-05-03 was blocked before any PCB edits. Reasons: `reports\PCB_ROUTING_PLAN.md` is `ROUTING_PLAN_BLOCKED`, no `.kicad_pcb` file exists, schematic-to-PCB gate is `FAIL`, placement pass 2 is `PLACEMENT_ORIENTATION_FAIL`, and copper-zone strategy is `ZONE_SETUP_FAIL`. Backup: `99_BACKUPS\pre_codex_edits\ESP32_CSI_WIFI_NODE_CRITICAL_ROUTING_BLOCKED_20260503_090215`. No traces were routed, no DRC was run, and no PCB visuals were exported. Report: `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\PCB_CRITICAL_NETS_ROUTING_REPORT.md`.
- `ESP32_CSI_WIFI_NODE` full-routing request on 2026-05-03 was blocked before any PCB edits. Reasons: `reports\PCB_CRITICAL_NETS_ROUTING_REPORT.md` is `CRITICAL_ROUTING_FAIL`, `reports\PCB_ROUTING_PLAN.md` is `ROUTING_PLAN_BLOCKED`, and no `.kicad_pcb` file exists. Backup: `99_BACKUPS\pre_codex_edits\ESP32_CSI_WIFI_NODE_FULL_ROUTING_BLOCKED_20260503_090757`. No remaining nets were routed, no DRC/unrouted check was run, no PCB visuals/crops were generated, and no manufacturing outputs were created. Reports: `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\PCB_FULL_ROUTING_REPORT.md`, `reports\TRACE_BY_TRACE_AUDIT.md`, and `_verification\pcb_visual\FULL_ROUTING_CLOSEUP_REVIEW.md`.
- `ESP32_CSI_WIFI_NODE` final PCB verification before fab request on 2026-05-03 failed and did not generate any fabrication outputs. Final result: `NOT_READY_FOR_FAB_EXPORT`. Reasons: no `.kicad_pcb` file exists, schematic-to-PCB gate is `FAIL`, footprint audit is `FOOTPRINT_AUDIT_FAIL`, PCB update from schematic is `NOT_RUN_GATE_FAIL`, DRC and unrouted checks have not run, and routing/trace audit have not run. Report: `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\FINAL_PCB_VERIFICATION_BEFORE_FAB.md`.
- `ESP32_CSI_WIFI_NODE` `NOT_FINAL` fabrication package export request on 2026-05-03 was blocked before any export. Final result: `BLOCKED`. Reason: `reports\FINAL_PCB_VERIFICATION_BEFORE_FAB.md` is `NOT_READY_FOR_FAB_EXPORT`, not `READY_FOR_NOT_FINAL_FAB_EXPORT`. No `fabrication\NOT_FINAL_<timestamp>` folder, Gerbers, drill files, BOM, CPL/PNP, STEP, PCB PDFs/images, manifest, ZIP, or manufacturing outputs were created. Report: `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\NOT_FINAL_FAB_PACKAGE_AUDIT.md`.
- Latest gate setup records: `02_HISTORY\sessions\SCHEMATIC_TO_PCB_GATE_SYSTEM_ADDED.md`, `02_HISTORY\design_reviews\SCHEMATIC_TO_PCB_GATE_SYSTEM_AUDIT.md`, `02_HISTORY\command_logs\SCHEMATIC_TO_PCB_GATE_SYSTEM_COMMANDS.md`, and `02_HISTORY\issue_logs\SCHEMATIC_TO_PCB_GATE_BLOCKED_ESP32_CSI_WIFI_NODE.md`.
- Readiness score from final setup audit: 88 / 100.
- Main warnings: `KiCAD-MCP-Server` is not installed; KiBot, InteractiveHtmlBom, PcbDraw, and KiCanvas still need controlled real-project validation before production trust.
- Platform tool roots were created without moving repos or changing existing venv paths. Windows GUI automation packages are now installed only in the separate `windows_gui` venv; Linux GUI/headless tools are not installed.
- Windows GUI automation is installed for passive discovery and screenshot setup only. It has not been used to click, type, move windows, or control KiCad.
- KiCad GUI discovery scripts must only be run when KiCad is already open and LJ clearly intends read-only discovery. They must not click, type, send hotkeys, open projects, save files, or modify KiCad projects.
- KiCad GUI discovery scripts now reject VS Code/browser/editor false positives as high-confidence targets. Latest passive test with KiCad manually open confirmed one real KiCad process window and kept VS Code/Chrome title matches low-confidence only with inspection/screenshot/control disabled.
- GUI discovery plus gated native annotation/save/GUI ERC is verified once for `ESP32_CSI_WIFI_NODE`. Dry-run-first closed-state open support exists but is not live-tested. Other GUI control remains disabled unless LJ explicitly approves a specific, safety-gated task.
- Windows GUI helper repos are local references only. Do not build, install, or use them to automate KiCad until a future explicit gated task.
- Linux automation is planning-only until LJ explicitly sets up Linux/WSL/VM/container use. Do not run Linux GUI/headless automation on production files first.
- Active real design project selected: `ESP32_CSI_WIFI_NODE`.
- `ESP32_CSI_WIFI_NODE` now has a live PCB source under `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb`; do not trust older `NO_PCB` reports without checking the live truth audit first.
- Current real board state: PCB exists, placement exists, partial routing exists, but routing continuation and all fabrication/prod/export phases remain blocked.
- Remaining practical gaps include live placement/orientation approval, exact acceptance or repair of the `60 mm x 95 mm` board, `U2 pad 41` drill-rule resolution, GND strategy, USB/control/test routing completion, and the formal schematic gate mismatch.
- `COMMAND LINK` is read-only by default, but LJ approved one direct repair/review/re-export session on 2026-04-30. Do not treat that as blanket future permission without fresh confirmation.
- `COMMAND_LINK_VERIFIED_REFERENCE` is a copied reference workspace only. Any design changes require a separate revision copy.
- Latest read-only review of `COMMAND_LINK_VERIFIED_REFERENCE` found ERC/DRC issues in the local KiCad environment: ERC exit code 5 with 2 warnings; DRC exit code 5 with 46 violations.
- Latest direct `COMMAND LINK` continuation fixed the 40 footprint-library mismatch warnings by creating `COMMAND_LINK_EMBEDDED.pretty` exact local footprints and updating board footprint references, fixed R2/U3/U4 starved thermals, and fixed the C3/C9 courtyard overlap. Final direct ERC and DRC both pass.
- New direct exports include Gerbers, Excellon drills, BOM, PNP, PDFs, STEP, and copied ERC/DRC reports under `Codex Review Outputs\20260430_210726\new_outputs_NOT_FINAL`. STEP export still reports missing 3D models for J2, J3, J4, and L1.
- PNP ref, side, X/Y, and rotation are unchanged versus the prior NOT_FINAL package, but PNP `Package` metadata changed for 37 placed parts because of the project-local per-reference footprint names. Human package review is still required.
- Final fabrication readiness audit classification for the latest COMMAND LINK package is `HUMAN_REVIEW_REQUIRED`, not `FAB_READY`.
- COMMAND LINK learning updates are limited to supported review facts; uncertain component, stackup, fab-house, and design-quality assumptions were not promoted to defaults.
- AI review is not fabrication approval.
- Manufacturing outputs are not final without ERC, DRC, BOM, footprint, netlist, datasheet, connector, polarity/orientation, mechanical, and visual review gates.

## Rules for ChatGPT/Codex

- Never edit original finished PCB files directly unless LJ explicitly approves a direct finished-folder repair/review task and Codex creates a snapshot first.
- Copy finished projects before review if edits are needed and direct finished-folder approval has not been explicitly granted.
- Run or confirm backup before changing KiCad files.
- Run ERC after schematic changes or explain why ERC could not run.
- Run DRC after PCB changes or explain why DRC could not run.
- Before schematic or PCB creation, read the relevant `09_ACCURACY_ENGINE`, `10_KNOWLEDGE_BASE`, `11_LIBRARY_FACTORY`, `12_REFERENCE_DESIGN_LIBRARY`, `13_PART_INGESTION`, and `14_LAYOUT_AUTOMATION` files and mark missing evidence explicitly.
- Before supplier, distributor, lifecycle, stock, pricing, supplier SKU, or sourcing work, read `28_SUPPLIER_INGESTION` policies and use official APIs first, user-provided CSV exports second, and manual source-link records third.
- Before selecting or relying on a footprint candidate, read `29_FOOTPRINT_GAP_ANALYSIS`, `11_LIBRARY_FACTORY`, and `08_COMPONENT_DATABASE/00_INDEX/KICAD_SYMBOL_FOOTPRINT_LINKING_RULES.md`; installed KiCad candidates are search evidence only, not footprint approval.
- Before linking a supplier SKU, JLC/LCSC part number, or supplier package field to a KiCad footprint, create or update a record under `30_SUPPLIER_FOOTPRINT_MATCHES` and keep connector/PMOS/ESD/MCU-module/regulator matches human-review-required unless exact drawing-level evidence exists.
- For future KiCad schematic-to-PCB-to-routing-to-fabrication work, use `.prompts\kicad_pipeline` and follow `FULL_KICAD_PROJECT_PIPELINE.md` gate order unless LJ explicitly approves a logged exception.
- Before benchmark scoring or comparison claims, read `15_BENCHMARKS` and require actual run artifacts, metadata, scoring notes, and human review status.
- Do not generate final manufacturing outputs without the verification gate.
- Do not modify third-party tool repos casually.
- Do not randomly click or type into KiCad with GUI automation; discover windows and take screenshots first, then require explicit approval for any control action.
- Prefer CLI/API/MCP over GUI automation.
- Prefer read-only inspection before edits.
- Prefer copied project workspaces over original projects.
- Prefer `NOT_FINAL` outputs until the verification gate passes.
- Do not store passwords, API keys, license keys, private tokens, or credentials.
- Read `AGENTS.md` and the required `00_CODEX_START` files before touching KiCad project files.
- Keep durable global decisions in `01_MEMORY`, durable project decisions in project `memory/`, commands/results in `02_HISTORY` or project `history/`, and unresolved problems in issue logs.
- At the end of every meaningful session, write a session log, command logs if commands were run, failed-attempt records if anything failed, user-correction records if the user reports something wrong, memory updates only for durable facts, open issues for unresolved problems, and refreshed memory/history indexes.
- Also create AI self-review, AI response scorecard, claim/evidence matrix, uncertainty logs for unverified items, hallucination-risk logs for guessed/inferred/weakly sourced claims, and quality-gate failure records when blocked or failed. Rebuild `CURRENT_KNOWN_PROBLEMS.md`.

## Latest important history files

- `02_HISTORY\design_reviews\FINAL_PRODUCTION_STRUCTURE_AUDIT.md`
- `05_OUTPUTS\release_readiness\FINAL_STRUCTURE_SCORECARD.md`
- `05_OUTPUTS\release_readiness\FINAL_STRUCTURE_BLOCKERS.md`
- `05_OUTPUTS\release_readiness\FINAL_STRUCTURE_NEXT_STEPS.md`
- `02_HISTORY\sessions\FINAL_PRODUCTION_STRUCTURE_AUDIT_SESSION.md`
- `02_HISTORY\command_logs\FINAL_PRODUCTION_STRUCTURE_AUDIT_COMMANDS.md`
- `02_HISTORY\design_reviews\COMPONENT_DATABASE_CORE_SETUP_AUDIT.md`
- `02_HISTORY\design_reviews\ACCURACY_ENGINE_AND_AI_QUALITY_SETUP_AUDIT.md`
- `09_ACCURACY_ENGINE\checklists\ACCURACY_GATE_CHECKLIST.md`
- `09_ACCURACY_ENGINE\verification_rules\ERC_DRC_REQUIRED_RULES.md`
- `09_ACCURACY_ENGINE\verification_rules\FAB_OUTPUT_NOT_FINAL_RULES.md`
- `09_ACCURACY_ENGINE\verification_rules\HUMAN_REVIEW_GATE_RULES.md`
- `26_AGENT_QUALITY\AI_RESPONSE_QUALITY_GATE.md`
- `26_AGENT_QUALITY\AI_EVIDENCE_REQUIREMENTS.md`
- `02_HISTORY\sessions\COMPONENT_DATABASE_CORE_SETUP_SESSION.md`
- `02_HISTORY\command_logs\COMPONENT_DATABASE_CORE_SETUP_COMMANDS.md`
- `08_COMPONENT_DATABASE\00_INDEX\DO_NOT_GUESS_RULES.md`
- `08_COMPONENT_DATABASE\99_UNVERIFIED_INBOX\core_starter_records\CORE_STARTER_RECORDS.md`
- `08_COMPONENT_DATABASE\99_UNVERIFIED_INBOX\core_starter_records\core_starter_records.json`
- `02_HISTORY\design_reviews\STRUCTURE_EXPANSION_AUDIT.md`
- `02_HISTORY\sessions\STRUCTURE_EXPANSION_SESSION.md`
- `02_HISTORY\command_logs\STRUCTURE_EXPANSION_COMMANDS.md`
- `02_HISTORY\ai_scorecards\STRUCTURE_EXPANSION_AI_RESPONSE_SCORECARD.md`
- `00_CODEX_START\STRUCTURE_STANDARD.md`
- `00_CODEX_START\FOLDER_ROUTING_RULES.md`
- `00_CODEX_START\REPO_STRUCTURE_INDEX.md`
- `02_HISTORY\design_reviews\KICAD_ACCURACY_ENGINE_STATUS.md`
- `02_HISTORY\design_reviews\KICAD_BENCHMARKS_STATUS.md`
- `02_HISTORY\design_reviews\KICAD_INSTALLED_APP_DEEP_AUDIT.md`
- `03_TOOLS\kicad_app_intelligence\KICAD_9_WINDOWS_PATH_MAP.md`
- `03_TOOLS\kicad_app_intelligence\KICAD_CLI_COMMANDS_REFERENCE.md`
- `03_TOOLS\kicad_app_intelligence\KICAD_LIBRARY_DISCOVERY_GUIDE.md`
- `03_TOOLS\kicad_app_intelligence\KICAD_DO_NOT_TOUCH_RULES.md`
- `00_CODEX_START\KICAD_AGENT_OPERATING_MANUAL.md`
- `00_CODEX_START\KICAD_SAFE_AUTOMATION_RULES.md`
- `03_TOOLS\kicad_app_intelligence\KICAD_AGENT_TASK_MAP.md`
- `02_HISTORY\command_logs\KICAD_INSTALLED_APP_DEEP_AUDIT_COMMANDS.md`
- `02_HISTORY\sessions\KICAD_INSTALLED_APP_DEEP_AUDIT_SESSION.md`
- `02_HISTORY\sessions\DATASHEET_RESEARCH_PIPELINE_SESSION.md`
- `06_DATASHEETS\00_INDEX\RESEARCH_PIPELINE.md`
- `06_DATASHEETS\00_INDEX\PUBLIC_RELEASE_DATASHEET_POLICY.md`
- `00_CODEX_START\PRODUCT_VISION.md`
- `00_CODEX_START\KICAD_ENGINE_ARCHITECTURE.md`
- `02_HISTORY\design_reviews\KICAD_ENGINE_PRODUCT_GAP_AUDIT.md`
- `02_HISTORY\design_reviews\KICAD_ENGINE_FINAL_SETUP_AUDIT.md`
- `03_TOOLS\tool_logs\KICAD_ENGINE_HEALTH_CHECK.md`
- `02_HISTORY\sessions\README_GPT_CREATED_OR_UPDATED.md`
- `02_HISTORY\sessions\START_HERE_CHATGPT_HANDOFF_RULE_UPDATED.md`
- `02_HISTORY\sessions\FOR_CHAT_GPT_REFRESHED.md`
- `02_HISTORY\design_reviews\COMMAND_LINK_FINISHED_PCB_INVENTORY.md`
- `02_HISTORY\sessions\COMMAND_LINK_FINISHED_PCB_INDEXED.md`
- `02_HISTORY\sessions\COMMAND_LINK_REFERENCE_COPY_CREATED.md`
- `02_HISTORY\design_reviews\COMMAND_LINK_READ_ONLY_REVIEW.md`
- `02_HISTORY\erc_drc_reports\COMMAND_LINK_ERC_DRC_REVIEW.md`
- `02_HISTORY\sessions\COMMAND_LINK_READ_ONLY_REVIEW_SESSION.md`
- `02_HISTORY\sessions\COMMAND_LINK_LEARNING_UPDATE_SESSION.md`
- `03_TOOLS\TOOL_PLATFORM_STRATEGY.md`
- `03_TOOLS\tool_logs\TOOL_MIGRATION_PLAN.md`
- `03_TOOLS\tool_logs\PLATFORM_TOOL_STRUCTURE_CREATED.md`
- `02_HISTORY\sessions\PLATFORM_TOOL_ROOTS_CREATED.md`
- `03_TOOLS\windows\docs\WINDOWS_GUI_AUTOMATION_README.md`
- `03_TOOLS\windows\docs\KICAD_GUI_CONTROL_LIMITS.md`
- `03_TOOLS\windows\docs\WINDOWS_GUI_REPO_INDEX.md`
- `03_TOOLS\windows\scripts\KICAD_GUI_DISCOVERY_README.md`
- `03_TOOLS\windows\scripts\kicad_window_filter.py`
- `03_TOOLS\windows\scripts\window_discovery\discover_kicad_windows.py`
- `03_TOOLS\windows\scripts\pywinauto\inspect_kicad_uia.py`
- `03_TOOLS\windows\scripts\pywinauto\inspect_kicad_win32.py`
- `03_TOOLS\windows\scripts\screenshots\capture_kicad_window.py`
- `03_TOOLS\tool_logs\LOCAL_TOOL_REPO_STATUS.md`
- `02_HISTORY\command_logs\WINDOWS_GUI_AUTOMATION_INSTALL_COMMANDS.md`
- `02_HISTORY\sessions\WINDOWS_GUI_AUTOMATION_INSTALL_SESSION.md`
- `02_HISTORY\command_logs\WINDOWS_GUI_REPOS_CLONED_COMMANDS.md`
- `02_HISTORY\sessions\WINDOWS_GUI_REPOS_CLONED_SESSION.md`
- `02_HISTORY\sessions\KICAD_GUI_DISCOVERY_WORKFLOW_CREATED.md`
- `03_TOOLS\linux\docs\LINUX_AUTOMATION_README.md`
- `03_TOOLS\linux\docs\LINUX_KICAD_HEADLESS_PLAN.md`
- `03_TOOLS\linux\docs\WSL_SETUP_NOTES.md`
- `03_TOOLS\linux\docs\LINUX_TOOL_INSTALL_COMMANDS_DRAFT.md`
- `03_TOOLS\linux\scripts\check_linux_kicad_env.sh`
- `03_TOOLS\linux\scripts\xvfb\run_kicad_headless_check.sh`
- `03_TOOLS\linux\scripts\xdotool\list_windows.sh`
- `03_TOOLS\linux\scripts\wmctrl\list_windows.sh`
- `02_HISTORY\sessions\LINUX_AUTOMATION_PLAN_CREATED.md`
- `02_HISTORY\sessions\CONTROL_PLANES_RULES_UPDATED.md`
- `02_HISTORY\design_reviews\PLATFORM_CONTROL_LAYERS_AUDIT.md`
- `02_HISTORY\sessions\PLATFORM_CONTROL_LAYERS_AUDIT_SESSION.md`
- `02_HISTORY\sessions\KICAD_GUI_DISCOVERY_RUN_SESSION.md`
- `03_TOOLS\windows\logs\KICAD_GUI_DISCOVERY_FILTER_FIX_REPORT.md`
- `02_HISTORY\sessions\KICAD_GUI_DISCOVERY_FILTER_FIX_SESSION.md`
- `02_HISTORY\sessions\KICAD_GUI_DISCOVERY_CONFIRMED_RUN_SESSION.md`
- `00_CODEX_START\CONTROL_PLANES.md`
- `02_HISTORY\sessions\CODEX_START_CONTROL_PLANES_SYNCED.md`
- `02_HISTORY\design_reviews\COMMAND_LINK_DRC_CONTINUATION_REVIEW.md`
- `02_HISTORY\erc_drc_reports\COMMAND_LINK_DRC_CONTINUATION_ERC_DRC_REPORT.md`
- `02_HISTORY\sessions\COMMAND_LINK_DRC_CONTINUATION_SESSION.md`
- `02_HISTORY\command_logs\COMMAND_LINK_DRC_CONTINUATION_COMMANDS.md`
- `02_HISTORY\design_reviews\COMMAND_LINK_FINAL_FAB_READINESS_AUDIT.md`
- `02_HISTORY\sessions\COMMAND_LINK_FINAL_FAB_READINESS_AUDIT_SESSION.md`
- `02_HISTORY\command_logs\COMMAND_LINK_FINAL_FAB_READINESS_AUDIT_COMMANDS.md`
- `02_HISTORY\sessions\ESP32_CSI_WIFI_NODE_WORKSPACE_CREATED.md`
- `05_OUTPUTS\release_readiness\GITHUB_PUSH_PLAN.md`
- `05_OUTPUTS\release_readiness\GITHUB_PUSH_FILE_INCLUDE_EXCLUDE_AUDIT.md`
- `05_OUTPUTS\release_readiness\GITHUB_PUSH_SECURITY_SCAN.md`
- `05_OUTPUTS\release_readiness\GITHUB_PUSH_REPORT.md`
- `02_HISTORY\sessions\GITHUB_REPO_PUSH_SESSION.md`
- `02_HISTORY\command_logs\GITHUB_REPO_PUSH_COMMANDS.md`
- Repo publication status:
  - Local git initialized on `main`
  - Private remote created at `https://github.com/swayerloren/KICAD_ENGINE.git`
  - Initial workspace commit pushed on `2026-05-08`
  - Public release remains blocked by `PUBLIC_RELEASE_CHECKLIST.md` and `21_LICENSE_ATTRIBUTION\LICENSE_AUDIT.md`

## When to update this file

Update this file every time repo structure, tools, MCP config, workflow, active projects, finished PCB library, major setup status, health status, blockers, or readiness score changes.

If the change affects the long-form context, keep this file and `README_GPT.md` synchronized. If only a KiCad project changes, update project memory/history and update this file only when that change affects future ChatGPT/Codex context.

