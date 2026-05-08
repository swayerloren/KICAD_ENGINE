# Hallucination Risk Log: Supplier Connector Stubs

Date: 2026-05-03

Status: `LOW_RISK_WITH_EXPLICIT_LIMITATIONS`

## Risks

| Risk | Severity | Mitigation |
| --- | --- | --- |
| Future agent may treat stubs as completed live API integrations. | `MEDIUM` | README, audit, scorecard, issue log, and handoff docs state live APIs are not implemented or tested. |
| Future agent may treat supplier package fields as footprint verification. | `HIGH` | Connector outputs mark footprint status `UNVERIFIED` and include footprint-risk notes. |
| Future agent may run live supplier calls without user approval. | `HIGH` | Connectors require explicit `--live`, and JLCPCB/LCSC refuse live behavior entirely. |
| Future agent may store API keys in repo docs/logs. | `HIGH` | Environment-variable docs prohibit committing, printing, caching, or logging secret values. |

## Current Session Risk

`LOW`

Only dry-run stubs and docs were created. No live calls, scraping, installs, downloads, KiCad edits, or credential writes were performed.
