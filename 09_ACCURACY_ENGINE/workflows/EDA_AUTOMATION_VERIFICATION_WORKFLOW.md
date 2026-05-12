# EDA Automation Verification Workflow

Status: `MANDATORY_FOR_TOOL_DRIVEN_RESULTS`

Use this workflow whenever a script, optional third-party tool, calculator, or
automation wrapper produces an engineering result that could influence a
schematic, PCB, export, or release decision.

## Goals

1. Separate tool output from engineering proof.
2. Record tool/version/input assumptions.
3. Validate results with KiCad-native checks or an independent calculation.

## Workflow

1. Define the task and record the intended use of the tool result.
2. Record the tool identity:
   - script/tool name
   - version or commit if known
   - runtime context
3. Record the inputs:
   - project path
   - file hashes when applicable
   - numeric assumptions
   - source/formula note
4. Run the tool in the safest mode first:
   - dry-run
   - read-only
   - copied project
5. Validate the output independently:
   - KiCad ERC for schematic consequences
   - KiCad DRC or parity for PCB consequences
   - a second script or hand calculation for numeric outputs
6. Record the result as one of:
   - `VALIDATED`
   - `VALIDATED_WITH_HUMAN_REVIEW_REQUIRED`
   - `UNVERIFIED`
   - `REJECTED`
7. If validation fails or cannot run, block the engineering claim.

## Hard Rules

- Automation results are not self-proving.
- Optional open-source tool output must be treated as advisory until validated.
- Normal Python import success does not prove KiCad `pcbnew` context exists.
- For board-aware scripts, confirm KiCad Python context first.
- GUI-only KiCad actions still require the native GUI workflow and safety gates.

