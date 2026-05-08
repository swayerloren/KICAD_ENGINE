# Routing Test Fixtures

## Purpose

Provide deterministic JSON fixtures for testing the routing engine without touching real KiCad project files.

## Fixtures

- `esp32_usb_power_fixture.json`
  - mixed power + USB + antenna-keepout case
- `can_node_fixture.json`
  - CAN node with power and transceiver routing priorities
- `regulator_power_fixture.json`
  - compact regulator-focused routing case
- `bad_keepout_violation_fixture.json`
  - intentionally broken case for hard-fail coverage

## Use

Run the routing scripts directly against these fixtures.

Expected outcome:

- three fixtures should pass or pass-with-review semantics through planning
- the bad fixture should block with hard fails

## Boundary

These fixtures are synthetic routing models. They are test inputs, not approvals for any real board.
