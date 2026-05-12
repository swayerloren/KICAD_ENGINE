# Design Rules Memory

Durable design-rule preferences and placeholders for KiCad projects. Replace `TBD` values with project-specific or fab-specific values only after they are verified.

## Startup Routing Rule

- Future schematic, PCB, fab, memory/history, and open-source-tool prompts do
  not require the user to paste a giant `READ FIRST` list.
- If the prompt says `Read START_HERE_FOR_AI_AGENTS.md and route yourself
  correctly`, the agent must use `00_CODEX_START/TASK_ROUTER.md` plus the
  companion task-type tables to determine the correct docs automatically.
- Router task routes are workflow categories only. They do not replace the
  execution-contract task types that control whether KiCad design files may
  change.
- Optional upstream KiCad-adjacent tools must route through
  `03_TOOLS/open_source_integrations/` before install suggestions, attribution
  claims, or bundling decisions are made.
- The old scrape-derived corpus is not a permanent canonical knowledge home.
  Future migration work must start from the release-readiness migration ledger
  plus destination/status files, and must drain content into existing
  canonical repo areas instead of creating another parallel knowledge folder.
- After the 2026-05-11 metadata move phase, canonical source-registry and
  retrieval-index entry points are
  `10_KNOWLEDGE_BASE/source_registry/` and
  `10_KNOWLEDGE_BASE/retrieval_indexes/`.
- After the 2026-05-11 unsorted/rejected drain phase, raw low-value copied
  content must default to license-review quarantine when redistribution status
  is unclear. Future agents must not revive public rejected-content payload
  trees for raw copied captures unless rights are proven.
- After the 2026-05-12 final `_scripts` drain phase, `knowledge_scrape/`
  should no longer be treated as a live tool surface. The remaining legacy
  PowerShell scrape scripts were moved to
  `02_HISTORY\knowledge_scrape_migration\obsolete_scripts\` as provenance
  only, and normal agent routing/tool use must continue through the canonical
  Python migration, indexing, source-registry, and knowledge-base surfaces.
- After the 2026-05-12 emptying step, the `knowledge_scrape/` folder itself was
  backed up under `99_BACKUPS\knowledge_scrape_pre_empty\` and removed from
  the live repo tree. Any later `knowledge_scrape` mention is historical
  evidence only.
- After the 2026-05-11 KiCad docs knowledge move phase, canonical guidance for
  KiCad core workflows, `pcbnew` context rules, KiCad file formats, and KiCad
  library conventions lives under `10_KNOWLEDGE_BASE/kicad_core/`,
  `kicad_python_api/`, `kicad_file_formats/`, and `kicad_libraries/`. Raw
  scraped pages from those categories are not canonical and must remain in
  license-review quarantine.
- After the 2026-05-11 component/datasheet/vendor knowledge move phase,
  canonical source-backed part intelligence starts with `06_DATASHEETS/`,
  `08_COMPONENT_DATABASE/`, `25_VENDOR_DATABASE/`,
  `29_FOOTPRINT_GAP_ANALYSIS/`, and `30_SUPPLIER_FOOTPRINT_MATCHES/`. Raw
  copied vendor pages, CAD portal pages, raw datasheet PDFs, and extracted PDF
  markdown from legacy migrated sources are not canonical truth and must
  remain in license-review quarantine.
- Vendor part numbers are not footprint proof.
- Supplier CAD models are not automatically trusted.
- Datasheet PDF redistribution must be license-reviewed before public-path use.
- After the 2026-05-11 fab/dfm/compliance knowledge move phase, canonical
  fabrication and compliance guidance starts with
  `10_KNOWLEDGE_BASE/dfm_assembly/`,
  `10_KNOWLEDGE_BASE/compliance_emc_safety/`,
  `24_FAB_PROFILES/`, and the related `09_ACCURACY_ENGINE` export/checklist
  rules. Raw copied fab-house pages, standards-like captures, and compliance
  captures from legacy migrated sources are not canonical truth and must
  remain in license-review quarantine.
- After the 2026-05-11 case-study/training move phase, forums, videos,
  university training, and good-board/bad-board examples must be treated as
  `GUIDANCE_ONLY`. Canonical usage policy now starts with
  `10_KNOWLEDGE_BASE/training/`, `10_KNOWLEDGE_BASE/peer_review/`,
  `10_KNOWLEDGE_BASE/case_studies/`, `26_AGENT_QUALITY/`, and
  `09_ACCURACY_ENGINE/verification_rules/LOW_CONFIDENCE_SOURCE_USAGE_RULES.md`.
- Low-confidence source material may feed failure-pattern checklists and style
  scorecards, but it may not approve footprints, routing, connector
  orientation, EMC, or fabrication readiness by itself.
- Fab package validation is not assembly approval.
- Pick-and-place rotations require visual/human review.
- IPC, UL, and similar standards remain link-only unless redistribution rights
  are explicitly documented.
- Open-source KiCad sample learning work must route through
  `32_OPEN_KICAD_SAMPLE_INTAKE/` first, then use
  `07_REFERENCE_DESIGNS/` for link-first style comparison rules only after
  license and quality review.
- Sample metrics may support comparisons against human-made schematics and PCB
  layouts, but they are not proof of correctness and must not override
  datasheets, connector truth, project-specific gates, or DRC/ERC evidence.
- Do not copy schematic blocks or PCB layouts from sample projects blindly,
  even when the sample is open-source.
- The default repo must stay ZIP-portable. Optional tools install into `.tools/`
  or user-local caches only, and missing tools must fail gracefully.
- Schematic readiness requires more than ERC. Use
  `34_SCHEMATIC_QUALITY_ENGINE/` and
  `03_TOOLS/scripts/schematic_quality/run_schematic_quality_gate.py` for
  readability, native annotation, footprint readiness, and human visual proof
  before PCB update claims.
- Schematic visual cleanup should now route through
  `03_TOOLS/scripts/schematic_layout/` plus
  `34_SCHEMATIC_QUALITY_ENGINE/SCHEMATIC_LAYOUT_ALGORITHM.md`,
  `FUNCTIONAL_BLOCK_TEMPLATES.md`, `LOCAL_WIRING_STYLE_GUIDE.md`, and
  `VISUAL_READABILITY_SCORECARD.md`.
- Do not accept label-heavy local blocks when short local wires would be
  clearer. Repeated same-block labels are a readability blocker, not a style
  preference.
- Native KiCad annotation is authoritative. Use the dry-run-first workflow
  under `33_KICAD_GUI_AUTOMATION/` with `--live`, `--allow-annotation`,
  `--allow-save`, and `--allow-gui-erc` for full live proof; raw
  `.kicad_sch` text edits are not annotation proof.
- Footprint population is not enough for schematic-to-PCB readiness. Use
  `35_FOOTPRINT_PACKAGE_ENGINE/` plus
  `python 03_TOOLS/scripts/footprint_package/run_footprint_package_gate.py --project <ACTIVE_PROJECT_PATH> --no-fail`
  and require `FOOTPRINT_LOCK.csv`, source evidence, package proof, risk
  classification, and high-risk review evidence for every physical symbol.
- If the live schematic already has `0` blank footprint fields, a footprint
  assignment task becomes a proof-and-lock audit, not a blind rewrite task.
  Do not overwrite high-risk saved footprints unless exact package evidence
  proves the replacement; record mismatches like wrong module variant or wrong
  package family as `NEEDS_HUMAN_REVIEW` blockers first.
- Enforceable PCB quality-gate DRC/parity checks must use explicit KiCad
  schematic-parity flags. Plain `kicad-cli pcb drc` is not authoritative for
  parity gating; use `kicad-cli pcb drc --schematic-parity --severity-all
  --format report` or an equivalent wrapper that proves parity counts.

## Default Board Layers
- Default: TBD.
- Notes: Confirm project requirements and fab stackup before layout.

## Trace Width Preferences
- Signal traces: TBD.
- Power traces: TBD.
- High-current traces: TBD.
- Notes: Calculate trace widths from current, copper weight, temperature rise, and routing layer.

## Trace Geometry Rules
- Avoid obvious 90-degree trace corners where practical.
- Avoid acute-angle bends sharper than 90 degrees unless there is no alternative and the exception is documented.
- Use two 45-degree bends as the default direction change for normal routing.
- Prefer smooth, rounded, or filleted routing where practical for high-speed, RF, and sensitive nets.
- Wide power traces still require clean 45-degree-style transitions and clean pad entry.
- DRC pass is required, but visual routing quality is a separate gate.
- A routed region is not acceptable until the read-only geometry audit passes: `python 03_TOOLS\scripts\pcb_geometry\audit_trace_quality.py --project <ACTIVE_PROJECT_PATH>`.
- If local placement causes ugly routing, move the local cluster instead of forcing crude copper.
- Route critical nets first, not random low-risk nets.
- Do not cross RF antenna keepouts.
- Keep USB D+/D- clean and paired where practical.
- Keep regulator switching loops short and compact.
- Avoid unnecessary vias; vias on critical nets should have a reason.
- Avoid rectangular perimeter routes, excessive detours above `2x` direct span, long TP stubs above `5 mm`, and return-path-splitting traces.
- Every trace should appear in a trace-by-trace audit before the routing pass is called acceptable.
- Autorouting output is review-only unless fully audited.
- Real-board routing extraction must stay read-only by default. Extracted fields that KiCad does not expose cleanly should be marked `NOT_EXTRACTED`, not guessed.
- Real copied-board routing audit may use KiCad's own Python plus `kicad-cli pcb drc --format json` as evidence, but active-project routing remains blocked until the real-project routing preconditions and stop conditions are satisfied.

## Clearance Preferences
- General clearance: TBD.
- High-voltage clearance: TBD.
- Creepage assumptions: TBD.
- Notes: Use fab limits only as a minimum; design rules should include margin.

## Power Input Rules
- Input voltage range: TBD.
- Reverse polarity protection: TBD.
- Overcurrent protection: TBD.
- Surge/transient protection: TBD.
- Notes: Verify regulator dissipation, connector ratings, fuse behavior, and ground return paths.

## Vehicle/12V Rules
- Load dump handling: TBD.
- Cranking voltage behavior: TBD.
- Reverse battery behavior: TBD.
- Ignition noise filtering: TBD.
- Notes: Treat vehicle 12V as noisy, transient-heavy, and safety-relevant.

## ESD/Protection Rules
- External connector ESD protection: TBD.
- TVS diode strategy: TBD.
- Series resistance/common-mode filtering: TBD.
- Notes: Keep protection close to connectors and provide low-impedance return paths.

## Connector Rules
- Connector family preference: TBD.
- Pin numbering verification: TBD.
- Keying/polarization requirement: TBD.
- Notes: Verify pinout, orientation, mating part, retention, current rating, and cable strain relief.
- Connector orientation is not proven by XY position or rotation value alone.
- Mechanical connector truth must distinguish the port opening, pin side, body side, and board-edge direction before routing is allowed to start.
- Barrel jack orientation: for horizontal DC barrel jacks, the female circular opening is the front/mating side and the 3-pin solder-leg side is the rear/back side. For edge placement, the female opening must face off-board and the solder/back side must face inward. For bottom-edge placement, the female opening faces down/off-board and the 3-pin solder side faces up/inward.
- Barrel jack evidence: do not approve from pad coordinates alone. Require exact 3D model when available, `F.Fab`/`F.SilkS`/`F.CrtYd` footprint geometry, and manufacturer drawing or product-image evidence. If geometry and 3D evidence are missing, classify `BLOCKED_BY_BARREL_JACK_ORIENTATION_EVIDENCE`.
- USB-C edge orientation: receptacle mouth must face off-board, bottom-edge mouth faces down/off-board, footprint `PCB Edge` line must align to board `Edge.Cuts`, pads must remain on-board, and shell/body overhang must be expected by the footprint. Do not approve USB-C from coordinates alone.
- If a required connector 3D model is missing or unresolved, keep the connector at `NEEDS_HUMAN_REVIEW` and block routing until human review resolves the proof gap.

## PCB Layout Sandbox Gate
- Before any real `.kicad_pcb` edit, create or review a PCB Layout Sandbox report set.
- Every new PCB layout must evaluate at least three variants before first real placement.
- Each variant must capture board shape, dimensions, fixed mechanics, connector orientation, RF keepouts, projected power/data paths, routing feasibility, and risk score.
- Score variants with the sandbox scoring system before selecting one.
- Any hard-fail variant is not selectable even if the rest of the concept looks promising.
- The selected variant must be the highest-scoring non-failed option, with the lowest human-review risk among ties, and must be explicitly justified.
- The sandbox scorer uses two penalty channels: DRC/precheck risk and human uncertainty risk.
- Variant statuses are `PASS`, `FAIL`, `AUTO_BLOCKED_MISSING_DATA`, and `AUTO_BLOCKED_BAD_LAYOUT`.
- The auto selector must never choose a hard-failed variant even if it has the highest numeric score.
- Real PCB update from schematic and real PCB placement are blocked until the active project records `PASS` in `reports/PCB_LAYOUT_SANDBOX_GATE_STATUS.md`.
- `PCB_LAYOUT_SANDBOX_GATE_STATUS.md` must confirm at least three variants, a scorecard, a selected layout plan, connector-orientation planning, antenna-keepout planning, board-shape/dimension planning, routing-feasibility evidence, and sandbox auto-approval status `AUTO_APPROVED_FOR_PCB_WORK`.
- Do not ask for generic manual sandbox approval when the evidence can answer the question.
- If sandbox evidence is incomplete, create an auto-blocked report with exact missing items instead of requesting vague approval.
- `AUTO_APPROVED_FOR_PCB_WORK` is permission to start real PCB sync, board outline, fixed-mechanical placement, grouped placement, DRC, and placement visuals through `AUTO_PCB_START_WORKFLOW.md`.
- `AUTO_APPROVED_FOR_PCB_WORK` is not permission for final routing, fab export, or fabrication-ready claims.
- Do not assume the board outline is rectangular; shape must be justified from mechanical, enclosure, connector, routing, and usability constraints.
- Do not force routing around bad placement. Move the local cluster or reject the variant.
- Do not claim a layout is professional until sandbox planning, routing feasibility, DRC, and visual review all pass.

## PCB Prelayout Gate

- Before real PCB placement or routing, generate a read-only board digital twin and score at least three placement variants with projected route evidence.
- Real PCB placement is blocked until the latest `reports/prelayout_engine/*/prelayout_gate_result.json` records at least three generated variants, at least one passing variant, and `placement_gate_status = PASS`.
- Real PCB routing is additionally blocked until the latest prelayout result records `routing_gate_status = PASS`.
- A selected or live candidate with connector truth `NEEDS_HUMAN_REVIEW` is still blocking; do not treat plausible edge XY plus rotation as enough proof.
- Wrong-facing connectors, projected open nets, projected keepout crossings, and false confidence from DRC-with-open-nets are prelayout blockers, not cleanup notes.
- Treat the prelayout engine as additive to `34_PCB_LAYOUT_SANDBOX`, not as a replacement for sandbox, phase, DRC, or human-review gates.

## Mounting/Mechanical Rules
- Mounting hole size: TBD.
- Keepout around holes: TBD.
- Board edge clearance: TBD.
- Enclosure constraints: TBD.
- Notes: Verify with mechanical drawings before fabrication.

## Placement Intelligence Rules

- ESP32-style modules with onboard antennas should sit at a board edge or in a documented clear antenna zone unless the project uses an external antenna.
- Do not place copper, traces, vias, mounting holes, connectors, test pads, or tall components under an RF antenna keepout unless exact source documentation allows it.
- USB-C and barrel-jack connectors usually belong on a board edge with insertion direction verified from body geometry, footprint evidence, and manufacturer drawings where available.
- USB-C and barrel-jack or other input connectors should be treated as fixed mechanical parts in placement planning.
- Placement order should begin with board outline, holes, edge connectors, and RF keepout before power, USB, MCU support, LEDs, and test pads.
- Power path placement should follow physical current-flow order.
- USB ESD should stay near the USB connector, and USB support parts should remain local to the connector path.
- Courtyard overlap is a placement failure, not a cosmetic issue.
- Board-edge clearance must be checked during placement precheck.
- A placement concept is not acceptable if it creates obviously impossible routing.
- Buttons must remain user-accessible after enclosure and cable insertion.
- LEDs should remain visible and should not be blocked by connector bodies or inserted cables.
- Test pads must remain accessible after assembly.
- Mounting holes must be mechanically spaced and clearance-checked against screw heads, washers, connector bodies, and keepouts.
- Do not force a rectangle or square board shape when the connector, RF, enclosure, or usability requirements suggest another outline.
- Board shape must be justified rather than assumed.

## Silkscreen/Labeling Rules
- Reference designator visibility: TBD.
- Pin 1 marking: required unless physically impossible.
- Connector labels: required for external connectors.
- Polarity labels: required for polarized parts and power input.

## Test Point Rules
- Required rails: TBD.
- Programming/debug points: TBD.
- Communications test points: TBD.
- Notes: Include ground access near measurement points.

## Fabrication Constraints
- Board house: TBD.
- Minimum trace/space: TBD.
- Minimum drill: TBD.
- Copper weight: TBD.
- Surface finish: TBD.
- Notes: Copy verified constraints into `FAB_HOUSE_PREFERENCES.md` when known.

## 2026-05-08: Thermal-Via DRC Rule Lesson

- When a verified footprint intentionally uses exposed-pad thermal vias smaller than the project minimum through-hole diameter rule, do not blindly enlarge the live board geometry first.
- Confirm whether the DRC failure is a project-rule mismatch versus a real padstack defect.
- If the footprint geometry is intentional and source-backed, align the project rule to the real drill size before rewriting the live PCB copper or pad geometry.

## Finished PCB Reference Review Lessons

These lessons come from the read-only review of `COMMAND_LINK_VERIFIED_REFERENCE` on 2026-04-30. They are review rules and caution flags, not automatic design defaults.

- Finished PCB references must be checked for source-to-output completeness: `.kicad_pro`, `.kicad_sch`, `.kicad_pcb`, BOM, pick-and-place, Gerbers, drill-related files, PDF, and STL when available.
- A finished reference is not a clean baseline if local ERC or DRC returns violations. Classify each issue as design issue, fabrication exception, intentional waiver, or local library/environment drift before reusing the pattern.
- For future assembly reviews, compare BOM references against pick-and-place references. In `COMMAND LINK`, `J2`, `J3`, and `J4` were present in the BOM but absent from pick-and-place; this may indicate manual assembly, but it must be documented explicitly before an assembly package is considered complete.
- Fabrication package review should confirm copper layers, solder mask layers, silkscreen layers, paste layers when assembly is required, board outline, drill-related files, and Gerber job/package metadata.
- DRC review should explicitly check for courtyard overlap, starved thermals, co-located holes, footprint/library mismatches, missing library footprints, unconnected pads, and footprint errors.
- Missing symbol or footprint libraries in a reference review should be recorded as environment/library completeness issues before deciding whether the underlying design is defective.

## 2026-05-07: PCBA Export Design Rule

- Do not treat BOM/CPL/centroid validation as assembly approval.
- Pick-and-place rotations must be visually checked before upload approval.
- Barrel jack and USB-C orientation must be manually/proof verified before upload.
- IC pin 1, diode/LED polarity, capacitor polarity, and connector mating direction must be verified before export approval.
- Solder paste layers, board outline, drill files, mounting holes/slots, and external Gerber-viewer review are required before upload approval.

## 2026-05-07: PCB Routing Geometry Rule

- Avoid 90-degree corners where practical.
- Never use acute trace bends sharper than 90 degrees unless no reasonable alternative exists and the exception is documented.
- Use two 45-degree bends for normal routing.
- Prefer smooth or rounded routing for high-speed, RF, or sensitive nets where practical.
- Do not accept crude routing just because DRC passes.
- Treat routing automation as a fixture-backed planning and audit layer, not as permission to touch a real board. Real routing remains blocked until schema-aware planning, hard-fail handling, trace-by-trace audit completeness, and copied-board KiCad evidence exist.

## Live State And Stale Report Rules

- Maintenance and phase gating must derive current PCB truth from the live `.kicad_pro`, `.kicad_sch`, and `.kicad_pcb` files before trusting markdown summaries.
- Operational gate or state reports should record source hashes for the schematic and PCB they inspected.
- A stale report must not override live file evidence that a PCB exists, footprints exist, placement exists, or routing exists.
- A stale report may still be preserved as history, but it must be marked ignored or superseded when live file truth contradicts it.

## 2026-05-07: FreeRouting Feasibility Rule

- FreeRouting may be used as an optional routing-feasibility probe only.
- Treat all FreeRouting outputs as `REVIEW_ONLY`.
- Use FreeRouting to compare congestion, unrouted nets, via pressure, and impossible placements.
- Do not use FreeRouting to auto-approve USB, RF, switching-regulator, or high-current routing.
- Never overwrite the real PCB from FreeRouting output without backup and explicit approval.

## 2026-05-07: Real Project Routing Gate

- Do not let the routing engine touch a real KiCad PCB until exact upstream gates, synced PCB evidence, board outline, keepouts/zones, routing plan, critical-net list, net classes, and DRC precheck all exist.
- Real routing must proceed in ordered passes: power/protection, regulator critical loop, 3V3 rail, USB D+/D-, ESD/protection, control nets, decoupling, user I/O/test pads, then low-risk remainder.
- Stop routing immediately for RF/antenna keepout crossings, unrouted critical nets, missing GND strategy, unjustified critical-net vias, stale routing plans after placement change, incomplete trace-by-trace review, or visually crude routing even if DRC does not flag it.

## 2026-05-08: Real Routing Prep Packet

- Before each real active-project routing pass, create a `routing_work\<timestamp>\` folder inside the active project.
- The prep packet must include a live PCB snapshot, backup path, before/after hash log, trace change log, component move log, DRC run log, routing decision log, current net/ratsnest baseline, current trace baseline, current placement baseline, and current DRC baseline.
- If the prep packet is incomplete, do not start the live routing pass.

## 2026-05-08: Copied-Board DRC Rehearsal Rule

- When rehearsing real-board PCB edits on a copied board, keep the matching project `.kicad_pro` beside the copied `.kicad_pcb`.
- Detached copied-board DRC runs can silently fall back to different board-rule defaults and produce false blocker regressions.
- Treat copied-board rehearsal results as invalid until the copied project preserves the live rule context.

## 2026-05-08: Scripted PCB Edit Verification Rule

- After a scripted KiCad Python PCB edit, validate the saved board with a fresh `kicad-cli pcb drc` artifact written to a short, project-local report path.
- If a first post-save DRC result contradicts the copied-board proof or the saved copper inventory, rerun the DRC after the board file settles before rejecting the route candidate.
- Treat the settled rerun plus the refreshed `LIVE_PROJECT_STATE.json` as the authoritative post-edit evidence.

## 2026-05-08: Duplicate Switch Pad Classification Rule

- When a tactile-switch footprint leaves one same-net duplicate pad unrouted after the functional cluster is connected, classify the untouched twin as `expected duplicate pad/open` unless the footprint evidence proves both pads must be copper-tied.
- Do not force duplicate switch-pad bridges on a production PCB just to drive the unconnected-item count down.
- Prioritize routing the functional pull-up, capacitor, MCU pin, and test-pad spine first; treat duplicate switch-pad cleanup as optional and footprint-review dependent.

## 2026-05-08: Acute Power-Branch Cleanup Rule

- A DRC-clean trace can still fail the trace-by-trace audit if it creates a true acute corner on a power or protection net.
- When an acute power-branch dogleg is found, prefer a copied-board-proven replacement that converts it to a short vertical-plus-horizontal or 45/135 geometry without increasing via count.
- Do not churn the rest of the routed board for cosmetic reasons once the single clearly bad acute feature has been removed.

## 2026-05-10: Project-Specific Schematic Intelligence Rule

- Before more schematic repair or any schematic-to-PCB update on an active project, create or refresh a project-local `schematic_intelligence/` layer built from the saved `.kicad_sch` plus current audit/gate evidence.
- The intelligence layer should document functional blocks, net inventory, footprint state, annotation state, visible review markers, readability defects, and a safe repair sequence.
- Do not let future sessions infer block intent, review status, or PCB-readiness only from raw schematic text when the project-specific intelligence layer exists.

## 2026-05-10: Schematic Tooling Import Rule

- Any repo script that edits or inspects KiCad schematics through `kicad_sch_api`
  must either run inside the repo-managed KiCad Python environment or add the
  repo-local `03_TOOLS/python_envs/kicad-mcp-pro/Lib/site-packages` fallback to
  `sys.path`.
- Do not assume the default `python` interpreter on the machine can import
  `kicad_sch_api` successfully.

## 2026-05-10: Prelayout Variant Truth Rule

- A projected route-angle `PASS` or even a perfect angle score does not make a
  prelayout variant ready for real PCB use by itself.
- Real placement remains blocked until connector orientation proof, footprint
  proof, projected open-net checks, and the live-board gate all pass together.
- Treat synthetic projected-route success as feasibility evidence only, not as
  permission to touch the real `.kicad_pcb`.

## 2026-05-10: Final PCB Visual Packet Freshness Rule

- A final PCB visual review packet is not current proof unless its recorded PCB
  hash matches the live `.kicad_pcb` hash being reviewed.
- Stale top/bottom renders, close-up crops, or 3D screenshots may be useful for
  comparison, but they do not satisfy final-review or export gates.
- If the stored visual packet hash differs from the live PCB hash, classify the
  visual gate as `STALE_OR_NOT_CURRENT`, not `PASS`.

## 2026-05-11: Engineering Knowledge Migration Rule

- Raw scraped engineering notes must not become a parallel rules system under
  new scrape-import trees when canonical rule/checklist folders
  already exist.
- Normalize enforceable guidance into `09_ACCURACY_ENGINE/`,
  `34_SCHEMATIC_QUALITY_ENGINE/`, `33_PCB_PRELAYOUT_ENGINE/`, and
  `03_TOOLS/scripts/pcb_quality/` as appropriate.
- Move raw scraped captures to migration history or license quarantine, not
  into source-of-truth rule folders.
## Latest Durable Rules - 2026-05-11

- Future agents must route startup and knowledge lookup through
  `START_HERE_FOR_AI_AGENTS.md`, `00_CODEX_START/TASK_ROUTER.md`, and the
  canonical `TASK_TYPE_TO_*_MAP.md` files, not through drained legacy scrape
  entrypoint concepts.
- Calculator outputs are first-pass aids only. Record the source/formula and
  validate the result independently before using it as engineering evidence.
- Optional or first-party automation results are not proof by themselves; they
  require KiCad ERC/DRC, parity, or another independent check.
