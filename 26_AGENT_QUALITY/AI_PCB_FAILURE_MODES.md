# AI PCB Failure Modes

Status: `ACTIVE_GUIDANCE`

## Purpose

Capture the recurring ways AI agents fail on schematic and PCB tasks even when
their written summaries sound confident.

## Failure Modes

- treating DRC clean as equivalent to routing complete
- confusing connector rotation with connector function
- using text parsing as proof of GUI-visible annotation state
- approving placement before mechanical truth is proven
- trusting a supplier or vendor page as footprint proof
- producing boxy, indirect, or right-angle routing while claiming "acceptable"
- treating fabricated outputs as ready because files export successfully

## Evidence Inputs

- prior repo issue history
- `02_HISTORY/known_agent_mistakes/`
- low-confidence source summaries from forums, videos, and case studies
- official rule layers that prove why the false pass is wrong

