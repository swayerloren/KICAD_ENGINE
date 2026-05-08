# Full Repo Scorecard

Audit date: `2026-05-03`

Classification: `INTERNAL_ALPHA_READY`

Public GitHub release status: `NOT_READY`

| Category | Score | Evidence note |
|---|---:|---|
| repo structure quality | 73 | All requested folders exist, but many are scaffold and generated/tool trees are present. |
| documentation usefulness | 62 | Useful startup/workflow docs exist, but many README/INDEX files are thin or duplicated. |
| KiCad workflow completeness | 70 | Gates and workflows exist, but no complete passing sample project is proven. |
| datasheet database usefulness | 42 | Mostly link/source scaffolding; two PDFs need redistribution review. |
| component database usefulness | 45 | Schemas and records exist; most records are unverified placeholders. |
| footprint intelligence usefulness | 52 | Inventory/gap systems exist; exact high-risk matches are not proven. |
| supplier ingestion readiness | 43 | Dry-run/API-safe structure exists; live verified ingestion is not proven. |
| Playwright pipeline safety | 68 | Conservative policy exists; live capture is blocked locally. |
| installer readiness | 55 | Windows unsigned smoke build exists; production packaging remains open. |
| public docs readiness | 66 | Public docs exist and avoid major overclaims; path drift remains. |
| security/legal readiness | 48 | Policies exist; PDFs, third-party content, and secret-like hits need human review. |
| AI quality/memory/history readiness | 82 | Strong routing and scoring system exists; index/log noise remains. |
| ESP32_CSI_WIFI_NODE project readiness | 20 | Schematic gate is FAIL, no PCB exists, and footprints are unassigned. |

Scores are audit judgments from local scans and file evidence, not benchmark results.
