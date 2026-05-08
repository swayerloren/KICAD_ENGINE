# Failed Attempt

Task: `Staged routing runner and no-progress detector`

## Failure

The first report parser revision incorrectly treated rehearsal text and sidecar
DRC reports as final routing-pass evidence. That produced a false no-progress
event on early routing batches.

## Correction

- excluded DRC-only sidecar reports from edit-run history
- added SHA256 label support
- split direct value labels from composite DRC sentence parsing
- changed repeated-blocker detection to use blocker overlap instead of exact
  whole-set equality
