# Schematic Review Checklist

Use this checklist before claiming schematic work is complete.

## Component Evidence

- [ ] Every component has a source or missing-source flag.
- [ ] Every exact value has source evidence or is marked unknown.
- [ ] Lifecycle and package status are recorded when relevant.

## Symbol And Pinout

- [ ] Symbol library and symbol name are recorded.
- [ ] Pin numbers match source.
- [ ] Power pins are visible or intentionally handled.
- [ ] Exposed pads and no-connect pins are handled.

## Power

- [ ] Every rail has a name and source.
- [ ] Voltage domains are explicit.
- [ ] Decoupling is source-backed or marked unverified.
- [ ] Regulator support components are reviewed.

## Interfaces

- [ ] USB review flags resolved or recorded.
- [ ] CAN review flags resolved or recorded.
- [ ] RF review flags resolved or recorded.
- [ ] Connector pin numbering and orientation require human review unless verified.

## Verification

- [ ] ERC run or reason documented.
- [ ] ERC findings interpreted.
- [ ] Remaining risks recorded as `HUMAN_REVIEW_REQUIRED`.
