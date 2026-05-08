# Repo Index

This file explains every top-level folder, what it is for, whether it is source or generated material, whether it should live in GitHub, and how reliable it currently is.

| Path | Purpose | Type | Commit To GitHub | Reliability | Important Files |
|---|---|---|---|---|---|
| `.github/` | GitHub repo metadata, issue templates, PR template, future workflow helpers | docs/config | yes | stable | `.github/README.md`, templates |
| `.prompts/` | prompt packs for Codex and Claude | docs/source | yes | experimental | `.prompts/README.md` |
| `.vscode/` | local editor tasks and workspace helpers | config | yes | stable | `.vscode/tasks.json` |
| `00_CODEX_START/` | mandatory startup, workflow, safety, and navigation control plane | docs/control | yes | stable | `START_HERE.md`, `CURRENT_PROJECT.md`, `GITHUB_NAVIGATION.md` |
| `01_MEMORY/` | durable reusable memory and repo-level lessons | memory | yes | needs review | `GLOBAL_MEMORY.md`, `MEMORY_INDEX.md` |
| `02_HISTORY/` | sessions, command logs, issue logs, failed attempts, AI-quality artifacts | history | yes | generated | `HISTORY_INDEX.md`, `sessions/`, `command_logs/` |
| `03_TOOLS/` | scripts, wrappers, audits, routing helpers, maintenance tools | source/tools | yes | experimental | `TOOLS_INDEX.md`, `scripts/` |
| `04_KICAD_PROJECTS/` | active, archived, and template KiCad projects | source/projects | yes | mixed | `PROJECTS_INDEX.md`, `active/ESP32_CSI_WIFI_NODE/` |
| `05_OUTPUTS/` | generated output summaries, release-readiness reports, selected committed outputs | generated/docs | partial | generated | `OUTPUTS_INDEX.md`, `release_readiness/` |
| `06_DATASHEETS/` | datasheet metadata and linked document structure | source/docs | yes | needs review | folder-specific metadata |
| `07_REFERENCE_DESIGNS/` | reference design metadata and notes | source/docs | yes | needs review | folder-specific records |
| `08_COMPONENT_DATABASE/` | structured component intelligence | source/data | yes | experimental | component records and schemas |
| `09_ACCURACY_ENGINE/` | accuracy, verification, and anti-hallucination rules | docs/rules | yes | stable | `README.md`, `ACCURACY_ENGINE_INDEX.md` |
| `10_KNOWLEDGE_BASE/` | reusable engineering guidance and checklists | docs/knowledge | yes | needs review | `README.md` |
| `11_LIBRARY_FACTORY/` | symbol, footprint, and package QA standards | docs/standards | yes | needs review | `README.md` |
| `12_REFERENCE_DESIGN_LIBRARY/` | reference-design intake and verification library | docs/source | yes | experimental | `README.md` |
| `13_PART_INGESTION/` | part-ingestion workflow and stubs | docs/tools | yes | experimental | `README.md` |
| `14_LAYOUT_AUTOMATION/` | real-world placement/routing planning, routing rules, and scripts | docs/tools | yes | experimental | `LAYOUT_AUTOMATION_INDEX.md`, `README.md` |
| `15_BENCHMARKS/` | benchmark methodology, tasks, and results | docs/data | yes | experimental | `README.md` |
| `16_INSTALLER/` | installer coordination docs | docs | yes | experimental | folder docs |
| `17_RELEASE_BUILD/` | release staging, manifests, and exclusion rules | docs/generated | yes | needs review | release manifests and policies |
| `18_PUBLIC_DOCS/` | public-facing documentation coordination | docs | yes | needs review | user-facing docs |
| `19_TEST_PROJECTS/` | sample/demo projects and controlled fixtures | source/test | yes | experimental | sample project docs |
| `20_CI_CD/` | CI/CD planning | docs/config | yes | experimental | workflow planning docs |
| `21_LICENSE_ATTRIBUTION/` | license and attribution audits | docs/compliance | yes | needs review | `LICENSE_AUDIT.md` |
| `22_SECURITY/` | security policy and rules | docs/security | yes | stable | `SECURITY_POLICY.md` |
| `23_PACKAGE_PROFILES/` | packaging profiles for release/review bundles | docs/config | yes | experimental | profile docs |
| `24_FAB_PROFILES/` | fabrication profile guidance | docs/manufacturing | yes | needs review | fab profile docs |
| `25_VENDOR_DATABASE/` | vendor and sourcing metadata | source/data | yes | experimental | folder records |
| `26_AGENT_QUALITY/` | AI-quality policy, scorecards, and evidence support | docs/quality | yes | stable | quality rules |
| `27_EXAMPLES/` | safe examples and tutorials | docs/examples | yes | experimental | example docs |
| `28_SUPPLIER_INGESTION/` | supplier ingestion policies and schemas | docs/data | yes | experimental | source policy docs |
| `29_FOOTPRINT_GAP_ANALYSIS/` | installed-footprint gap tracking | docs/data | yes | experimental | README and backlog docs |
| `30_SUPPLIER_FOOTPRINT_MATCHES/` | supplier-to-footprint match rules and data | docs/data | yes | experimental | README and schemas |
| `31_PLAYWRIGHT_RESEARCH_PIPELINE/` | browser-assisted public research workflow docs | docs/tools | yes | experimental | source policy and rules |
| `32_OPEN_KICAD_SAMPLE_INTAKE/` | open-sample intake workflow and normalized copies | docs/source | yes | needs review | intake workflow docs |
| `33_KICAD_GUI_AUTOMATION/` | GUI automation policy and safety gates | docs/tools | yes | experimental | README and safety rules |
| `34_PCB_LAYOUT_SANDBOX/` | pre-PCB-edit layout variant planning and approval rules | docs/tools | yes | experimental | `PCB_LAYOUT_SANDBOX_INDEX.md`, `README.md` |
| `99_BACKUPS/` | local-only backups before automated edits | local-only | no | local-only | excluded by `.gitignore` |
| `docs/` | legacy public docs root still in use | docs | yes | needs review | migration-in-progress docs |
| `installer/` | current installer implementation root | source/tools | yes | experimental | installer source |
| `setup/` | setup helpers and scripts | source/tools | yes | experimental | setup assets |
| `T_E_M_P/` | temporary local-only scratch area | local-only | no | local-only | excluded by `.gitignore` |
| `__pycache__/` | Python cache | generated | no | local-only | ignored |

## Notes

- `05_OUTPUTS/` is only partially committed. Release-readiness documentation is committed; large generated payloads are mostly excluded.
- `99_BACKUPS/`, copied-board rehearsals, raw sample imports, and caches are intentionally local-only even when they are useful during active engineering work.
- A folder being present in Git does not mean its contents are complete, verified, or ready for public release.
