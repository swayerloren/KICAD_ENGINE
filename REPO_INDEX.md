# Repo Index

This file explains every top-level folder, what it is for, whether it is source or generated material, whether it should live in GitHub, and how reliable it currently is.

| Folder | Purpose | Status | Commit To GitHub | Type | Important Files | Reliability |
|---|---|---|---|---|---|---|
| `.github/` | GitHub repo metadata, issue templates, and PR template | active metadata | yes | docs/config | `.github/README.md`, templates | stable |
| `.prompts/` | prompt packs for Codex and Claude | active support | yes | docs/source | `.prompts/README.md` | experimental |
| `.vscode/` | local editor tasks and workspace helpers | active support | yes | config | `.vscode/tasks.json` | stable |
| `00_CODEX_START/` | mandatory startup, workflow, safety, and navigation control plane | authoritative startup layer | yes | docs/control | `START_HERE.md`, `CURRENT_PROJECT.md`, `GITHUB_NAVIGATION.md` | stable |
| `01_MEMORY/` | durable reusable memory and repo-level lessons | active durable memory | yes | memory | `GLOBAL_MEMORY.md`, `MEMORY_INDEX.md` | needs review |
| `02_HISTORY/` | sessions, command logs, issue logs, failed attempts, AI-quality artifacts | accumulated evidence | yes | history | `HISTORY_INDEX.md`, `sessions/`, `command_logs/` | generated |
| `03_TOOLS/` | scripts, wrappers, audits, routing helpers, maintenance tools | active tooling | yes | source/tools | `TOOLS_INDEX.md`, `scripts/` | experimental |
| `04_KICAD_PROJECTS/` | active, archived, and template KiCad projects | mixed project state | yes | source/projects | `PROJECTS_INDEX.md`, `active/ESP32_CSI_WIFI_NODE/` | needs review |
| `05_OUTPUTS/` | generated output summaries, release-readiness reports, selected committed outputs | partial committed outputs | partial | generated/docs | `OUTPUTS_INDEX.md`, `release_readiness/` | generated |
| `06_DATASHEETS/` | datasheet metadata and linked document structure | active knowledge store | yes | docs/source | folder-specific metadata | needs review |
| `07_REFERENCE_DESIGNS/` | reference design metadata and notes | active knowledge store | yes | docs/source | folder-specific records | needs review |
| `08_COMPONENT_DATABASE/` | structured component intelligence | active data layer | yes | source/data | component records and schemas | experimental |
| `09_ACCURACY_ENGINE/` | accuracy, verification, and anti-hallucination rules | authoritative rules | yes | docs/rules | `README.md`, `ACCURACY_ENGINE_INDEX.md` | stable |
| `10_KNOWLEDGE_BASE/` | reusable engineering guidance and checklists | active knowledge base | yes | docs/knowledge | `README.md` | needs review |
| `11_LIBRARY_FACTORY/` | symbol, footprint, and package QA standards | active standards | yes | docs/standards | `README.md` | needs review |
| `12_REFERENCE_DESIGN_LIBRARY/` | reference-design intake and verification library | active source library | yes | docs/source | `README.md` | experimental |
| `13_PART_INGESTION/` | part-ingestion workflow and stubs | active workflow docs | yes | docs/tools | `README.md` | experimental |
| `14_LAYOUT_AUTOMATION/` | real-world placement/routing planning, routing rules, and scripts | active planning/tool layer | yes | docs/tools | `LAYOUT_AUTOMATION_INDEX.md`, `README.md` | experimental |
| `15_BENCHMARKS/` | benchmark methodology, tasks, and results | active benchmark scaffolding | yes | docs/data | `README.md` | experimental |
| `16_INSTALLER/` | installer coordination docs | partial implementation support | yes | docs | folder docs | experimental |
| `17_RELEASE_BUILD/` | release staging, manifests, and exclusion rules | active release support | yes | docs/generated | release manifests and policies | needs review |
| `18_PUBLIC_DOCS/` | public-facing documentation coordination | active docs support | yes | docs | user-facing docs | needs review |
| `19_TEST_PROJECTS/` | sample/demo projects and controlled fixtures | active demo/test area | yes | source/test | sample project docs | experimental |
| `20_CI_CD/` | CI/CD planning | planning only | yes | docs/config | workflow planning docs | experimental |
| `21_LICENSE_ATTRIBUTION/` | license and attribution audits | active compliance layer | yes | docs/compliance | `LICENSE_AUDIT.md` | needs review |
| `22_SECURITY/` | security policy and rules | active policy layer | yes | docs/security | `SECURITY_POLICY.md` | stable |
| `23_PACKAGE_PROFILES/` | packaging profiles for release/review bundles | planning and profile docs | yes | docs/config | profile docs | experimental |
| `24_FAB_PROFILES/` | fabrication profile guidance | manufacturing guidance | yes | docs/manufacturing | fab profile docs | needs review |
| `25_VENDOR_DATABASE/` | vendor and sourcing metadata | active data layer | yes | source/data | folder records | experimental |
| `26_AGENT_QUALITY/` | AI-quality policy, scorecards, and evidence support | active quality layer | yes | docs/quality | quality rules | stable |
| `27_EXAMPLES/` | safe examples and tutorials | example content | yes | docs/examples | example docs | experimental |
| `28_SUPPLIER_INGESTION/` | supplier ingestion policies and schemas | active policy/data layer | yes | docs/data | source policy docs | experimental |
| `29_FOOTPRINT_GAP_ANALYSIS/` | installed-footprint gap tracking | active analysis layer | yes | docs/data | README and backlog docs | experimental |
| `30_SUPPLIER_FOOTPRINT_MATCHES/` | supplier-to-footprint match rules and data | active matching layer | yes | docs/data | README and schemas | experimental |
| `31_PLAYWRIGHT_RESEARCH_PIPELINE/` | browser-assisted public research workflow docs | active research workflow | yes | docs/tools | source policy and rules | experimental |
| `32_OPEN_KICAD_SAMPLE_INTAKE/` | open-sample intake workflow and normalized copies | active intake workflow | yes | docs/source | intake workflow docs | needs review |
| `33_KICAD_GUI_AUTOMATION/` | GUI automation policy and safety gates | active but safety-gated | yes | docs/tools | README and safety rules | experimental |
| `34_PCB_LAYOUT_SANDBOX/` | pre-PCB-edit layout variant planning and approval rules | active planning gate | yes | docs/tools | `PCB_LAYOUT_SANDBOX_INDEX.md`, `README.md` | experimental |
| `99_BACKUPS/` | local-only backups before automated edits | excluded local-only | no | local-only | excluded by `.gitignore` | local-only |
| `docs/` | legacy public docs root still in use | migration-in-progress | yes | docs | migration-in-progress docs | needs review |
| `installer/` | current installer implementation root | active implementation root | yes | source/tools | installer source | experimental |
| `setup/` | setup helpers and scripts | active setup helpers | yes | source/tools | setup assets | experimental |
| `T_E_M_P/` | temporary local-only scratch area | excluded local-only | no | local-only | excluded by `.gitignore` | local-only |
| `__pycache__/` | Python cache | excluded generated cache | no | generated | ignored | local-only |

## Notes

- `05_OUTPUTS/` is only partially committed. Release-readiness documentation is committed; large generated payloads are mostly excluded.
- `99_BACKUPS/`, copied-board rehearsals, raw sample imports, and caches are intentionally local-only even when they are useful during active engineering work.
- A folder being present in Git does not mean its contents are complete, verified, or ready for public release.
