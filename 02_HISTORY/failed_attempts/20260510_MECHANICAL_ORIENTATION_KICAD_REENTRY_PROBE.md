# Failed Attempt - Mechanical Orientation KiCad Re-entry Probe

Date: `2026-05-10`

## Attempt

Tried quick one-off inline Python probes to inspect live placement/model data directly before the shared orientation helper existed.

## Result

- A direct inline import from a numeric-prefixed repo path failed because Python module syntax cannot import from a path segment like `14_LAYOUT_AUTOMATION...`.
- A stdin-fed KiCad Python re-entry attempt failed with:
  `can't find '__main__' module in 'C:\\Users\\LJ\\GitHub\\KICAD_ENGINE'`

## Resolution

- Moved the needed logic into the shared read-only helpers instead of relying on brittle inline probes.
- Reused the existing board-extraction bridge and then ran the dedicated audit scripts successfully.

## Final Outcome

The final implementation and validation succeeded; the failure only affected exploratory probing and did not edit any KiCad design files.
