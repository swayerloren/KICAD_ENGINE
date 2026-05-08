# AUTO_ROUTING_ENGINE_FIXTURE_UPGRADE_SESSION

Date: `2026-05-07`

## Summary

Audited the current routing engine, replaced the thin JSON logic with a schema-backed fixture workflow, added strict routing scorecard rules and hard-fail logic, and validated the engine against four routing fixtures without touching any KiCad design files.

## Work Performed

1. Read the required startup, project-state, routing-rule, and script files.
2. Checked project maintenance state and incremented the active-project prompt counter from `2` to `3`.
3. Audited the existing routing scripts and confirmed they were useful but too thin for real engineering planning.
4. Added routing schemas:
   - `ROUTING_INPUT_SCHEMA.md`
   - `ROUTING_OUTPUT_SCHEMA.md`
   - `TRACE_AUDIT_SCHEMA.md`
   - `NET_CLASS_SCHEMA.md`
5. Added strict routing scorecard rules in `ROUTING_SCORECARD_RULES.md`.
6. Added four routing fixtures under `14_LAYOUT_AUTOMATION/test_fixtures/`.
7. Replaced the shared routing helper and upgraded all six routing scripts.
8. Added JSON + Markdown output support across the routing engine.
9. Ran `py_compile` on all routing scripts.
10. Ran the full fixture matrix and recorded the results.
11. Updated routing-engine handoff docs and memory.
12. Rechecked active-project KiCad file hashes to confirm no design-file edits occurred.

## Fixture Results

- `esp32_usb_power_fixture`: `PASS`, score `90`
- `can_node_fixture`: `PASS`, score `94`
- `regulator_power_fixture`: `PASS`, score `92`
- `bad_keepout_violation_fixture`: `AUTO_BLOCKED_BAD_LAYOUT`, score `42`

## Result

- Scripts audited: `YES`
- Scripts improved: `YES`
- Fixtures created: `YES`
- Routing engine ready for real KiCad PCB test: `NO`

## Next Step

Build a copied-board `.kicad_pcb` to routing-schema exporter and couple the scorecard to real DRC evidence before any real-board routing test.
