# Layout Automation Roadmap

## v0.1 Reality And Rules

Status: current target.

- Create realistic layout automation docs.
- Document KiCad, `kicad-cli`, `pcbnew`, IPC, and FreeRouting paths.
- Require human layout gates.

## v0.2 Read-Only Layout Analyzer

Build scripts to:

- Parse footprints and positions.
- List high-risk nets.
- List unverified footprints.
- Detect connectors and polarity parts.
- Generate placement/routing risk report.

## v0.3 Constraint Extractor

Build scripts to:

- Extract net classes.
- Extract rule areas.
- Extract board outline.
- Identify high-risk net classes.
- Create JSON/Markdown constraints.

## v0.4 Placement Proposal Generator

Build scripts/prompts to:

- Create placement group proposals.
- Suggest fixed/mechanical constraints.
- Suggest relative placement.
- Produce no-write Markdown reports first.

## v0.5 Copied-Board Placement Experiment

Only after user approval:

- Copy project.
- Move low-risk footprints through `pcbnew` Python or IPC.
- Run DRC before/after.
- Generate diff and review report.

## v0.6 FreeRouting Manual Review Workflow

- Document tested DSN/SES export/import flow.
- Run only on copied boards.
- Compare before/after DRC.
- Identify route quality issues.

## v0.7 FreeRouting Scripted Experiment

- User supplies FreeRouting path.
- Script validates inputs and output folders.
- No auto-install.
- Run on copied boards only.
- Keep all results `NOT_FINAL`.

## v1.0 Human-Guided Layout Assistant

Credible claim:

KiCad Engine can assist placement/routing planning, risk review, constraint extraction, and DRC comparison in a KiCad-native local workflow.

Not a credible claim yet:

KiCad Engine fully replaces human layout or delivers complete AI autorouting.

