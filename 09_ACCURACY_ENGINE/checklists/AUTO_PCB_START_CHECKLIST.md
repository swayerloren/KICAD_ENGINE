# Auto PCB Start Checklist

Status: `ACTIVE_CHECKLIST`

Use this checklist before any automatic real PCB creation, sync, outline, or placement work.

## Auto Start Preconditions

- [ ] Active project is confirmed.
- [ ] Target files are inside the active project.
- [ ] `reports/SCHEMATIC_TO_PCB_GATE_STATUS.md` is exactly `PASS`.
- [ ] Footprint/package gate result is `PASS` or `SAFE_CANDIDATE_WITH_EVIDENCE`.
- [ ] `reports/PCB_LAYOUT_SANDBOX_GATE_STATUS.md` is exactly `PASS`.
- [ ] Selected layout plan exists.
- [ ] Sandbox auto-approval report exists.
- [ ] Sandbox auto-approval status is `AUTO_APPROVED_FOR_PCB_WORK`.
- [ ] Board dimensions are defined.
- [ ] Connector-orientation plan exists.
- [ ] Antenna-keepout plan exists when RF is present.
- [ ] Routing-feasibility plan exists.
- [ ] Backup plan is confirmed.
- [ ] Verification plan is confirmed.
- [ ] Rollback plan is confirmed.

## Allowed Automatic Scope After Pass

- [ ] Update PCB from schematic only.
- [ ] Create or update `.kicad_pcb` only.
- [ ] Apply approved board outline only.
- [ ] Place fixed mechanical components only.
- [ ] Place main component groups only.
- [ ] Run DRC.
- [ ] Export placement/mechanical visual review evidence.

## Still Blocked After Pass

- [ ] Final routing remains blocked until placement gates pass.
- [ ] Gerber/fab/export work remains blocked.
- [ ] Fabrication-ready claims remain blocked.
- [ ] DRC cannot be ignored.
- [ ] Connector, antenna, RF, USB, and power risks remain mandatory review items.

## Required Result

Use only one result:

- `AUTO_PCB_START_PASS`
- `AUTO_PCB_START_BLOCKED`
- `AUTO_PCB_START_FAIL`
