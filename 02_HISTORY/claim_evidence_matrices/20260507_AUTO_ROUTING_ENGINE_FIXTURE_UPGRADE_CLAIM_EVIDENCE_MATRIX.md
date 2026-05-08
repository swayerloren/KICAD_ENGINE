# Claim Evidence Matrix

Session: `AUTO_ROUTING_ENGINE_FIXTURE_UPGRADE`

Date: `2026-05-07`

| Claim | Evidence |
| --- | --- |
| The prior routing scripts were useful but thin. | File inspection of `14_LAYOUT_AUTOMATION/scripts/*.py`; `02_HISTORY/design_reviews/AUTO_ROUTING_ENGINE_AUDIT.md` |
| The routing engine now has concrete schemas and fixtures. | New files under `14_LAYOUT_AUTOMATION/` and `14_LAYOUT_AUTOMATION/test_fixtures/` |
| The upgraded scripts emit JSON and Markdown. | Script source inspection and generated files under `14_LAYOUT_AUTOMATION/reports/fixture_runs/` |
| Three good fixtures pass and one bad fixture blocks. | `14_LAYOUT_AUTOMATION/reports/ROUTING_ENGINE_FIXTURE_TEST_REPORT.md` and `fixture_runs/*/score.json` |
| The engine is not ready for a real KiCad board test. | `02_HISTORY/design_reviews/AUTO_ROUTING_ENGINE_LIVE_READINESS_AUDIT.md` |
| No KiCad design files changed. | `Get-FileHash` results recorded in the command log |
