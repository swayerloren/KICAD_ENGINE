# PCBA Export Gate Checklist

Status: `ACTIVE_CHECKLIST`

Use this checklist before any JLCPCB or PCBWay NOT_FINAL manufacturing package is created or reviewed.

## Gate

- [ ] Phase gate allows export.
- [ ] No downstream phase is being skipped.
- [ ] Active project is confirmed.
- [ ] Backup exists before any KiCad-source edit.
- [ ] ERC evidence exists.
- [ ] Schematic parity evidence exists.
- [ ] DRC passes or exact remaining warnings are LJ-approved.
- [ ] No-unrouted-net proof exists.
- [ ] Connector orientation proof exists.
- [ ] Polarity/pin-1 proof exists.
- [ ] Gerber/drill export settings are documented.
- [ ] External Gerber viewer review is complete.
- [ ] JLCPCB package validated if JLCPCB output is created.
- [ ] PCBWay package validated if PCBWay output is created.
- [ ] Assembly notes created.
- [ ] Orientation checks created.
- [ ] Revision folder is new and does not overwrite old outputs.
- [ ] All outputs are marked `NOT_FINAL`.
- [ ] No upload or order is performed by the agent.

If any item fails, export readiness is blocked.

