# Public Payload Allowlist

Status: `ACTIVE_RELEASE_RULES`

Last updated: `2026-05-06`

## Purpose

This file defines what may be copied into a public release payload or installer
workspace template. It is an allowlist, not a release approval. A file that is
listed here must still pass `PAYLOAD_EXCLUDE_RULES.md`,
`PUBLIC_RELEASE_EXCLUSION_MANIFEST.md`, license review, secret scan, size
limits, and human release review before it is distributed.

## Default Allowlist

These first-party files and folders may be included when they pass exclusion
rules:

| Path | Include status | Notes |
| --- | --- | --- |
| `AGENTS.md` | `ALLOW` | Agent operating rules. |
| `README.md` | `ALLOW` | Public overview, must avoid overclaims. |
| `README_GPT.md` | `ALLOW` | AI-agent context, must avoid private details. |
| `FOR CHAT GPT.MD` | `ALLOW_WITH_SANITIZATION` | Include only in sanitized payload form; local history may be too detailed for public bundles. |
| `START_HERE_FOR_USERS.md` | `ALLOW` | User entry point. |
| `START_HERE_FOR_AI_AGENTS.md` | `ALLOW` | AI-agent entry point. |
| `QUICKSTART_WINDOWS.md` | `ALLOW` | Public setup doc. |
| `QUICKSTART_MACOS.md` | `ALLOW` | Public setup doc. |
| `QUICKSTART_LINUX.md` | `ALLOW` | Public setup doc. |
| `.vscode/` | `ALLOW` | Workspace tasks/settings only; no secrets. |
| `.prompts/` | `ALLOW` | Prompt pack files only. |
| `00_CODEX_START/` | `ALLOW` | Startup, gate, memory/history routing, and AI quality rules. |
| `03_TOOLS/scripts/` | `ALLOW` | First-party scripts only; no local environments or cloned repos. |
| `03_TOOLS/kicad*/` | `ALLOW_WITH_GENERATED_OUTPUTS_EXCLUDED` | Docs and scripts are allowed; generated inventories are excluded unless intentionally public and reviewed. |
| `06_DATASHEETS/` | `ALLOW_METADATA_ONLY` | Indexes, source lists, policies, and summaries only. PDFs require redistribution approval. |
| `08_COMPONENT_DATABASE/` | `ALLOW_METADATA_ONLY` | Schemas and records are allowed when verification status is explicit. |
| `09_ACCURACY_ENGINE/` | `ALLOW` | Accuracy and gate rules. |
| `10_KNOWLEDGE_BASE/` | `ALLOW` | General engineering guidance; not datasheet proof. |
| `11_LIBRARY_FACTORY/` | `ALLOW` | Symbol/footprint standards and safe validators. |
| `12_REFERENCE_DESIGN_LIBRARY/` | `ALLOW_LINK_RECORDS` | Link-first records and license notes only. |
| `13_PART_INGESTION/` | `ALLOW` | Workflows and stub generators. |
| `14_LAYOUT_AUTOMATION/` | `ALLOW` | Planning and reality-check docs. |
| `15_BENCHMARKS/` | `ALLOW_NO_FAKE_RESULTS` | Methodology, tasks, rubrics, and real results only. |
| `18_PUBLIC_DOCS/` | `ALLOW` | User documentation. |
| `19_TEST_PROJECTS/README.md` | `ALLOW` | Public sample overview. |
| `19_TEST_PROJECTS/SAMPLE_PROJECTS_INDEX.md` | `ALLOW` | Must show honest sample status. |
| `19_TEST_PROJECTS/HOW_TO_RUN_SAMPLE_PROJECTS.md` | `ALLOW` | User guide. |
| `19_TEST_PROJECTS/HOW_TO_INTERPRET_GATE_RESULTS.md` | `ALLOW` | User guide. |
| `21_LICENSE_ATTRIBUTION/` | `ALLOW_REVIEW_RECORDS` | License/attribution policy and audit records. |
| `22_SECURITY/` | `ALLOW` | Public security policy and script safety rules. |
| `26_AGENT_QUALITY/` | `ALLOW` | AI scoring and evidence rules. |
| `28_SUPPLIER_INGESTION/` | `ALLOW_NO_SECRETS` | Policies, schemas, dry-run connectors, and examples only. |
| `29_FOOTPRINT_GAP_ANALYSIS/` | `ALLOW_NO_LOCAL_GENERATED_INDEXES_BY_DEFAULT` | Scripts and public reports only. |
| `30_SUPPLIER_FOOTPRINT_MATCHES/` | `ALLOW_WITH_EXAMPLE_LABELS` | Match rules and EXAMPLE_ONLY records. |
| `31_PLAYWRIGHT_RESEARCH_PIPELINE/` | `ALLOW_DRY_RUN_ONLY` | Policies, source profiles, templates, and dry-run scripts. |
| `32_OPEN_KICAD_SAMPLE_INTAKE/README.md` | `ALLOW` | Intake policy overview. |
| `32_OPEN_KICAD_SAMPLE_INTAKE/*RULES.md` | `ALLOW` | Source/license/import/review/promotion rules. |
| `32_OPEN_KICAD_SAMPLE_INTAKE/candidates/` | `ALLOW_LINK_RECORDS` | Candidate metadata only; no raw repo copies. |
| `32_OPEN_KICAD_SAMPLE_INTAKE/attribution/` | `ALLOW_REVIEW_RECORDS` | Attribution evidence records. |
| `setup/` | `ALLOW_DRY_RUN_SAFE` | Scripts must ask before installing and must not store credentials. |
| `health_check.py` | `ALLOW` | Safe health check script. |
| `health_check.ps1` | `ALLOW` | Safe health check wrapper. |
| `LICENSE` | `ALLOW` | Repository license. |
| `DISCLAIMER.md` | `ALLOW` | Required public warning. |
| `SECURITY.md` | `ALLOW` | Public security policy. |
| `CONTRIBUTING.md` | `ALLOW` | Public contributor guide. |
| `CHANGELOG.md` | `ALLOW` | Public changelog. |
| `ROADMAP.md` | `ALLOW` | Must avoid overclaims. |

## Controlled Sample Fixture Allowlist

The current promoted sample is:

`19_TEST_PROJECTS/sample_kicad_projects/tomasr8_attiny85_dev_board/`

Current recorded status:

- License evidence: MIT license present.
- Gate result: `BLOCKED_UNTIL_HUMAN_REVIEW`.
- Public bundle status: `PUBLIC_BUNDLE_ALLOWED_PENDING_FINAL_HUMAN_REVIEW`.

Because final human release review is still pending, the public payload must
default to `LINK_ONLY_PLUS_DOCS` for this fixture.

### Allowed Now

The following sample documentation may be included because it is useful,
small, and preserves status/attribution without bundling raw imports:

| Path | Include status | Notes |
| --- | --- | --- |
| `19_TEST_PROJECTS/sample_kicad_projects/tomasr8_attiny85_dev_board/KICAD_ENGINE_SAMPLE_README.md` | `ALLOW` | Public sample explanation. |
| `19_TEST_PROJECTS/sample_kicad_projects/tomasr8_attiny85_dev_board/ORIGINAL_SOURCE_ATTRIBUTION.md` | `ALLOW` | Attribution and release warning. |
| `19_TEST_PROJECTS/sample_kicad_projects/tomasr8_attiny85_dev_board/GOLDEN_PATH_DEMO_STATUS.md` | `ALLOW` | Must retain blocked status. |
| `19_TEST_PROJECTS/sample_kicad_projects/tomasr8_attiny85_dev_board/LICENSE` | `ALLOW` | Upstream MIT license evidence. |
| `19_TEST_PROJECTS/sample_kicad_projects/tomasr8_attiny85_dev_board/ORIGINAL_UPSTREAM_README.md` | `ALLOW_AFTER_LICENSE_REVIEW` | Include only when human review confirms copied README redistribution is acceptable. |
| `19_TEST_PROJECTS/sample_kicad_projects/tomasr8_attiny85_dev_board/reports/*.md` | `ALLOW_SMALL_NOT_FINAL_REVIEW_EVIDENCE` | Markdown reports only, no FAB_READY claims. |

### Blocked Until Final Human Review

These sample files must not be bundled until public-bundle review is complete
and recorded as `PUBLIC_BUNDLE_ALLOWED`:

| Path | Current status | Required before inclusion |
| --- | --- | --- |
| `19_TEST_PROJECTS/sample_kicad_projects/tomasr8_attiny85_dev_board/*.kicad_pro` | `BLOCKED_PENDING_HUMAN_REVIEW` | Final license/release review, attribution approval, and exclusion audit. |
| `19_TEST_PROJECTS/sample_kicad_projects/tomasr8_attiny85_dev_board/*.kicad_sch` | `BLOCKED_PENDING_HUMAN_REVIEW` | Same as above. |
| `19_TEST_PROJECTS/sample_kicad_projects/tomasr8_attiny85_dev_board/*.kicad_pcb` | `BLOCKED_PENDING_HUMAN_REVIEW` | Same as above; must keep blocked engineering status visible. |
| `19_TEST_PROJECTS/sample_kicad_projects/tomasr8_attiny85_dev_board/fp-lib-table` | `BLOCKED_PENDING_HUMAN_REVIEW` | Include only with approved KiCad source bundle. |
| `19_TEST_PROJECTS/sample_kicad_projects/tomasr8_attiny85_dev_board/custom_footprints/` | `BLOCKED_PENDING_HUMAN_REVIEW` | Include only with exact source/attribution and footprint warning. |
| `19_TEST_PROJECTS/sample_kicad_projects/tomasr8_attiny85_dev_board/_verification/` | `BLOCKED_BY_DEFAULT` | Include only small, useful `NOT_FINAL` evidence after size and license review. |
| `19_TEST_PROJECTS/sample_kicad_projects/tomasr8_attiny85_dev_board/.gate_runs/` | `BLOCKED_BY_DEFAULT` | Prefer latest curated report under `05_OUTPUTS/gate_runs/` if intentionally public. |

## Human Review Required Before Any Sample Source Bundle

Before any copied sample KiCad files are included, a human must record:

1. Source URL and imported commit.
2. License file and license confidence.
3. Attribution file path.
4. Public bundle status exactly `PUBLIC_BUNDLE_ALLOWED`.
5. Files intentionally included.
6. Files intentionally excluded.
7. Confirmation that no raw imports, generated fab files, or `FAB_READY`
   outputs are bundled.
8. Confirmation that the sample is labeled `NOT_FINAL` or blocked where
   applicable.

## Rule For Ambiguity

If a file is not clearly allowed here, treat it as excluded until a release
review adds it to this allowlist.
