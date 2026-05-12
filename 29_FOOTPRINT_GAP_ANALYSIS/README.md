# Footprint Gap Analysis

Status: read-only KiCad library inventory and unverified footprint backlog system.

## PURPOSE

`29_FOOTPRINT_GAP_ANALYSIS/` identifies what footprints and symbols are available in the user's installed KiCad app and where KiCad Engine still needs exact package, connector, module, and assembly-footprint verification records.

## WHAT_BELONGS_HERE

- Installed KiCad footprint and symbol inventory summaries.
- Candidate footprint gap reports.
- High-risk footprint warning lists.
- Land-pattern source indexes and source-backed gap rules.
- Connector, MCU/module, and power package gap reports.
- Read-only scripts that inspect installed KiCad libraries and compare them to component database records.
- Generated JSON and Markdown indexes under `GENERATED_INDEXES/`.

## WHAT_DOES_NOT_BELONG_HERE

- KiCad global library edits.
- Project-local custom libraries.
- Downloaded datasheets or package drawings.
- Final footprint approvals.
- Manufacturing outputs.
- Secrets or supplier credentials.

## AI_AGENT_RULES

- Treat every footprint match as `UNVERIFIED` until checked against the exact manufacturer package drawing.
- Treat connector, RF, USB-C, PMOS, ESD, regulator, mounting-hole, and test-pad footprints as high risk.
- Use installed KiCad library inventory as candidate evidence only, not approval evidence.
- Treat vendor CAD portals and supplier package text as candidate context only.
- Do not modify `C:\Program Files\KiCad` or user global KiCad library tables.
- Route exact verification evidence to `08_COMPONENT_DATABASE/16_VERIFICATION_RECORDS/` when a footprint is promoted beyond candidate status.
- Use `31_PLAYWRIGHT_RESEARCH_PIPELINE` screenshot/source-link evidence only to support candidate investigation. Browser-captured package text does not verify a footprint.

## Canonical Files

- [FOOTPRINT_GAP_RULES.md](FOOTPRINT_GAP_RULES.md)
- [LAND_PATTERN_SOURCE_INDEX.md](LAND_PATTERN_SOURCE_INDEX.md)
- [HIGH_RISK_FOOTPRINT_GAPS.md](HIGH_RISK_FOOTPRINT_GAPS.md)
- [footprint_gap_index.json](footprint_gap_index.json)

## SAFE_EDIT_RULES

- Scripts must be read-only with respect to installed KiCad folders and user global KiCad config.
- Generated outputs belong in `29_FOOTPRINT_GAP_ANALYSIS/GENERATED_INDEXES/`, `05_OUTPUTS/footprint_gap_analysis/`, or `02_HISTORY/design_reviews/`.
- Do not edit `.kicad_mod`, `.pretty`, `.kicad_sym`, `.kicad_sch`, `.kicad_pcb`, or `.kicad_pro` files from this workflow.

## PUBLIC_RELEASE_NOTES

- This folder may contain machine-specific inventory paths such as `C:\Program Files\KiCad\9.0`; mark these as local audit evidence.
- Do not claim KiCad Engine ships verified footprints because candidate rows exist here.
- Before public release, review generated indexes for personal paths and decide whether to publish them or regenerate them locally.
