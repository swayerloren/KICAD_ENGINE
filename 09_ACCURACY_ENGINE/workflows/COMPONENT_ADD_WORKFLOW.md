# Component Add Workflow

## Steps

1. Identify exact component or generic component scope.
2. Find source documents or mark missing source.
3. Create or update component database record.
4. Identify symbol candidates.
5. Verify symbol pinout.
6. Identify footprint candidates.
7. Verify footprint against package drawing or mark unverified.
8. Add schematic support requirements.
9. Add layout and human-review flags.

## Exit Criteria

A component may be used in a schematic only when source status, symbol status, pinout status, footprint status, and layout warning status are explicit.
## Required Evidence Gate

Before adding a component to a schematic or PCB workflow:

1. Read the component record and `08_COMPONENT_DATABASE/00_INDEX/AI_USAGE_RULES.md`.
2. State verification status and source evidence.
3. Verify or block symbol selection.
4. Verify or block footprint selection.
5. Add uncertainty and human-review flags.
6. Create claim/evidence and uncertainty records if engineering claims are made.
