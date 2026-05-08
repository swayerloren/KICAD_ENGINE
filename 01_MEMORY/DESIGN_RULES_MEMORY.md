# Design Rules Memory

Durable design-rule preferences and placeholders for KiCad projects. Replace `TBD` values with project-specific or fab-specific values only after they are verified.

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
- If local placement causes ugly routing, move the local cluster instead of forcing crude copper.
- Route critical nets first, not random low-risk nets.
- Do not cross RF antenna keepouts.
- Keep USB D+/D- clean and paired where practical.
- Keep regulator switching loops short and compact.
- Avoid unnecessary vias; vias on critical nets should have a reason.
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
- Barrel jack orientation: for horizontal DC barrel jacks, the female circular opening is the front/mating side and the 3-pin solder-leg side is the rear/back side. For edge placement, the female opening must face off-board and the solder/back side must face inward. For bottom-edge placement, the female opening faces down/off-board and the 3-pin solder side faces up/inward.
- Barrel jack evidence: do not approve from pad coordinates alone. Require exact 3D model when available, `F.Fab`/`F.SilkS`/`F.CrtYd` footprint geometry, and manufacturer drawing or product-image evidence. If geometry and 3D evidence are missing, classify `BLOCKED_BY_BARREL_JACK_ORIENTATION_EVIDENCE`.
- USB-C edge orientation: receptacle mouth must face off-board, bottom-edge mouth faces down/off-board, footprint `PCB Edge` line must align to board `Edge.Cuts`, pads must remain on-board, and shell/body overhang must be expected by the footprint. Do not approve USB-C from coordinates alone.

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
