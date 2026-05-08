# FreeRouting Integration Plan

## Reality Summary

FreeRouting is a plausible external autorouter candidate. It is not yet integrated, installed, or tested by KiCad Engine.

Public FreeRouting documentation describes:

- Input through Specctra design files (`.dsn`).
- Output through Specctra session files (`.ses`).
- GUI and CLI operation.
- KiCad integration through exporting DSN and importing SES.
- CLI options such as loading design input and saving routed session output.

## What Must Be Proven

Before KiCad Engine can claim FreeRouting support, it must prove:

- How to export DSN from the user's KiCad version.
- How to import SES back into KiCad.
- Whether this can be done from CLI, plugin, GUI, or controlled workflow.
- How constraints translate.
- How zones, keepouts, net classes, differential pairs, and board rules survive the round trip.
- Whether Java/FreeRouting is installed or user-approved.
- Whether license and packaging requirements are acceptable.

## Candidate Workflow

1. Confirm active project and backup.
2. Copy board to an experimental workspace.
3. Run baseline DRC.
4. Export DSN from KiCad using a validated method.
5. Run FreeRouting manually or through an approved local CLI command.
6. Save SES.
7. Import SES into the copied KiCad board.
8. Refill zones.
9. Run DRC.
10. Compare before/after DRC.
11. Generate human review report.
12. Keep all outputs `NOT_FINAL`.

## Integration Modes

### Manual First

User exports DSN, runs FreeRouting, imports SES, then KiCad Engine reviews before/after.

Lowest automation risk.

### Scripted Local Experiment

KiCad Engine runs FreeRouting CLI on a copied board after user provides the FreeRouting executable/JAR path.

Requires:

- No auto-install.
- User-approved command.
- Output isolation.
- DRC comparison.

### Plugin / IPC Future

Use KiCad IPC or plugin workflow to coordinate DSN/SES export/import when stable enough.

Requires implementation and testing.

## Risks

- Routing quality may be poor for high-speed, RF, power, or dense boards.
- Constraints may not translate fully.
- Differential pairs and length constraints need verification.
- Zones may need refill.
- Human review remains mandatory.
- FreeRouting may require Java or separate installation.
- CLI/API versions may change.

## No Claim Rule

Do not claim "FreeRouting integrated" until a repeatable KiCad Engine workflow exists and has passed smoke tests on sample projects.

