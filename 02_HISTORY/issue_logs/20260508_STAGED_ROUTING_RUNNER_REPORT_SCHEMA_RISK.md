# Open Issue

Title: `Routing detector still depends on report-label stability`

## Risk

The staged routing runner and no-progress detector currently parse historical
Markdown reports. If future routing reports drift away from the established
labels, replay quality may degrade.

## Recommended Follow-Up

Add a machine-readable routing-pass summary contract so edit-required routing
runs emit canonical JSON for hashes, DRC counts, unconnected counts, unrouted
counts, blocker nets, and stage identity.
