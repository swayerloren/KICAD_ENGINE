# Layout Automation Reality Check

Date: 2026-05-03

## Purpose

Analyze realistic KiCad-native paths for placement and routing assistance so KiCad Engine can eventually compete with AI PCB tools without making false claims.

## Sources Reviewed

- KiCad 9 PCB Editor documentation: https://docs.kicad.org/9.0/en/pcbnew/pcbnew.html
- KiCad IPC API developer documentation: https://dev-docs.kicad.org/en/apis-and-binding/ipc-api/
- KiCad IPC API add-on developer documentation: https://dev-docs.kicad.org/en/apis-and-binding/ipc-api/for-addon-developers/
- FreeRouting GitHub repository: https://github.com/freerouting/freerouting
- FreeRouting KiCad usage documentation: https://freerouting.org/freerouting/using-with-kicad
- Local installed KiCad 9.0.7 `kicad-cli pcb --help`, `kicad-cli pcb export --help`, and `kicad-cli pcb drc --help`.

## What KiCad Can Do Natively

KiCad has serious interactive PCB layout capabilities:

- Footprint placement, exact movement, rotation, flipping, grouping, alignment, distribution, locking, rule areas, and keepouts.
- Interactive routing with highlight-collisions, push-and-shove, and walk-around modes.
- Differential pair routing, length tuning, and skew tuning.
- Net classes, custom DRC rules, rule areas, and DRC.
- Multichannel layout that can repeat manually placed/routed reference channels into target channels.
- Visual and fabrication outputs for review.

These are strong human-guided layout tools. They are not a general AI auto-layout engine.

## What `kicad-cli` Can Do

Local KiCad 9.0.7 `kicad-cli pcb` help shows:

- `drc`
- `export`
- `render`

`pcb export` supports many fabrication and review outputs, including Gerbers, drill, position, STEP, SVG, PDF, IPC-2581, ODB++, and others.

The audited CLI does not show a complete headless placement or autorouting command.

Best use for KiCad Engine:

- Baseline and post-change DRC.
- Review artifact exports.
- 3D/image rendering for visual review.
- Position/BOM/manufacturing package support.

## What `pcbnew` Python Can Inspect Or Change

KiCad's PCB Python API can inspect board objects such as footprints, drawings, tracks, zones, and netclasses. It can load and save boards.

Realistic uses:

- Read-only footprint placement reports.
- Constraint extraction.
- High-risk net identification.
- Board statistics and DRC preparation.
- Experimental copied-board placement changes.

Risks:

- The API is coupled to KiCad internals and can change.
- Any write can damage board files if not gated.
- It is not a ready-made autorouter.

## What IPC API May Enable

The KiCad IPC API is a promising direction for plugins and external tools that communicate with a running KiCad GUI.

Important limitations from public KiCad docs:

- KiCad 9/10 IPC communication is with a running GUI instance.
- KiCad 9.0 IPC coverage is PCB-editor focused.
- Broader coverage and headless capabilities are version-dependent and should not be assumed for KiCad 9.

Realistic use:

- Future human-in-the-loop placement assistant.
- Plugin-based selection/review UI.
- Safer interaction than coordinate GUI automation.

Do not treat IPC as a current complete headless layout automation layer.

## FreeRouting Feasibility

FreeRouting is a plausible external autorouter candidate.

Public FreeRouting docs describe:

- Specctra DSN input.
- Specctra SES output.
- GUI and CLI use.
- KiCad flow based on exporting DSN and importing SES.

Local KiCad 9.0.7 CLI export help did not list DSN export. Therefore KiCad Engine must prove a reliable DSN/SES path for the user's installed KiCad version before claiming integration.

FreeRouting integration should begin as:

- Manual or copied-board experiment.
- No auto-install.
- User-provided FreeRouting path.
- Baseline DRC.
- Route import.
- Zone refill.
- Post-route DRC.
- Human review.

## What Should Remain Human Review

Human review remains mandatory for:

- Connector orientation.
- Mechanical fit.
- RF placement and routing.
- USB routing and ESD placement.
- CAN/LIN/RS485 connector pinout and termination.
- High-current and switching regulator loops.
- Thermal decisions.
- Crystal/clock placement.
- Ground returns.
- DRC exclusions.
- PNP rotation.
- Manufacturing package approval.

## How AI Can Help Now

AI can realistically:

- Suggest placement groups.
- Identify high-risk nets.
- Extract likely constraints.
- Create routing priority lists.
- Generate manual layout review checklists.
- Compare before/after DRC reports.
- Summarize DRC deltas.
- Flag unverified footprints/connectors before layout work.

## Why Full Auto-Layout Should Not Be Overpromised

Full PCB layout is not just geometry.

It depends on:

- Mechanical constraints.
- Human connector expectations.
- Part availability and package variants.
- Board stackup.
- Power integrity.
- Signal integrity.
- EMC/ESD.
- Thermal paths.
- Manufacturing process.
- Assembly orientation.
- Enclosure and cable behavior.

Until KiCad Engine has implemented and tested an end-to-end placement/routing system, it should claim layout assistance, not complete layout automation.

## Created Planning Files

- `14_LAYOUT_AUTOMATION/README.md`
- `14_LAYOUT_AUTOMATION/PLACEMENT_ASSISTANCE_PLAN.md`
- `14_LAYOUT_AUTOMATION/ROUTING_ASSISTANCE_PLAN.md`
- `14_LAYOUT_AUTOMATION/CONSTRAINT_EXTRACTION_PLAN.md`
- `14_LAYOUT_AUTOMATION/KICAD_AUTOROUTER_OPTIONS.md`
- `14_LAYOUT_AUTOMATION/FREEROUTING_INTEGRATION_PLAN.md`
- `14_LAYOUT_AUTOMATION/AI_PLACEMENT_REVIEW_RULES.md`
- `14_LAYOUT_AUTOMATION/HUMAN_LAYOUT_REVIEW_GATE.md`
- `14_LAYOUT_AUTOMATION/ROADMAP.md`

## Current Status

`14_LAYOUT_AUTOMATION` is planning and review guidance only.

No placement engine, router, FreeRouting integration, DSN/SES importer/exporter, or IPC plugin was implemented in this task.

## Safety Notes

- No KiCad project source files were edited.
- No routing was attempted.
- No placement changes were made.
- No tools were installed.
- No external autorouter was downloaded.

