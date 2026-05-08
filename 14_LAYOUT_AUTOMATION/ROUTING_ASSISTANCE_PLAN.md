# Routing Assistance Plan

## Goal

Provide AI routing assistance without claiming complete autorouting.

## What KiCad Can Do Natively

KiCad includes an interactive router with modes including:

- Highlight collisions.
- Push-and-shove.
- Walk around.

KiCad also supports differential pair routing, length tuning, skew tuning, DRC-aware routing behavior, design rules, net classes, rule areas, and repeated layout workflows.

This is strong human-guided routing support. It is not a general headless AI autorouter.

## What `kicad-cli` Can Do

For routing workflows, `kicad-cli` is most useful for:

- Running DRC.
- Producing DRC JSON/report outputs.
- Exporting review artifacts.
- Rendering boards for visual review.
- Comparing before/after verification outputs.

Local KiCad 9.0.7 help does not show a full autorouting command.

## What `pcbnew` Python Can Inspect Or Change

Potential read-only routing checks:

- Existing tracks and vias.
- Net classes.
- Track widths and via sizes.
- Zones and rule areas.
- Unrouted ratsnest status where available.
- Approximate high-risk net path review.

Potential write operations in copied projects only:

- Add or remove tracks/vias.
- Move tracks.
- Create experimental route proposals.

Reality:

- Hand-rolling a router through `pcbnew` Python is a major project.
- AI-generated track geometry is high risk.
- Any write must be treated as experimental until DRC and human review pass.

## AI Routing Assistance That Is Realistic

Near-term:

- Identify high-risk nets.
- Rank routing priority.
- Suggest layer strategy.
- Suggest which nets should be routed manually first.
- Flag routing near switching nodes, antennas, connectors, or crystals.
- Check DRC before and after manual or experimental routing.
- Summarize DRC violations.

Medium-term:

- Generate critical-net route plans.
- Propose keepouts and net classes.
- Suggest via minimization and return-path checks.
- Detect obviously long or crossing ratsnest groups.
- Compare board revisions.

Long-term:

- External autorouter integration on copied boards.
- Human-approved import of external routing results.
- Local AI review of route quality.

## High-Risk Nets To Check

- RF feedlines.
- USB D+/D-.
- CANH/CANL.
- Differential pairs.
- Clock and crystal nets.
- Switching regulator switch nodes.
- High-current input/output paths.
- Sensitive analog inputs.
- Reset/boot/programming nets near noisy areas.

## Before/After DRC Comparison

For any routing change:

1. Save baseline DRC report.
2. Apply route proposal only on copied project or approved active project.
3. Refill zones if needed.
4. Run DRC with JSON/report output.
5. Compare violation count and severity.
6. Record new, resolved, and unchanged violations.
7. Keep output `NOT_FINAL`.

## No Overpromise Rule

Do not call AI routing complete unless:

- Routing was actually generated.
- All nets are connected.
- DRC is clean or exceptions are reviewed.
- High-risk nets are manually reviewed.
- Manufacturing outputs remain `NOT_FINAL` until full review passes.

