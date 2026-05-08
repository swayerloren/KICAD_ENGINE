# Public Repo Risk Register

Purpose: prioritized risk register for preparing KiCad Engine for public GitHub release. This is a practical engineering release checklist, not legal advice.

## Risk Ratings

- `High`: likely to block public release until reviewed or excluded.
- `Medium`: can ship only with documented mitigation.
- `Low`: ordinary release hygiene item.

## Release Risks

| Risk | Rating | File/folder | Source | License if known | Redistribution status | Recommended action | Safe public release status |
|---|---|---|---|---|---|---|---|
| Bundled AGPL tool repository | High | `03_TOOLS/repos/KiBot/` | INTI-CMNB/KiBot | AGPL-3.0 | High compliance risk if bundled | Exclude from public payload or complete AGPL review and attribution | `requires human review`; exclude by default |
| Bundled GPL tool repository | High | `03_TOOLS/windows/repos/AutoHotkey/` | AutoHotkey/AutoHotkey | GPL-2.0 | High compliance risk if bundled | Exclude from public payload; document official install path | `requires human review`; exclude by default |
| Bundled third-party repos | High | `03_TOOLS/repos/`, `03_TOOLS/windows/repos/` | Multiple GitHub projects | Mixed MIT, AGPL, GPL, nested licenses | Mixed and not release-reviewed | Do not publish vendored repos by default; use links/submodules/install docs | `requires human review` |
| Vendor PDFs in datasheet folder | High | `06_DATASHEETS/99_UNSORTED_INBOX/LEGACY_MIGRATION_20260502_161444/ESPRESSIF/` | Espressif documents | Unknown from local files | Public redistribution unclear | Exclude or replace with link-only metadata unless rights are confirmed | `requires human review`; link-only recommended |
| Private/reference KiCad board copy | High | `04_KICAD_PROJECTS/active/COMMAND_LINK_VERIFIED_REFERENCE/` | User/reference finished board | Unknown | Not safe without owner approval | Exclude from public payload | `requires human review`; exclude by default |
| Active design project | High | `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/` | User active project | Unknown | Not safe unless intentionally published | Exclude unless explicitly approved and sanitized | `requires human review` |
| Generated fabrication-style outputs | High | `05_OUTPUTS/` | Generated and copied outputs | Mixed/unknown | May include fab files, copied examples, private data | Exclude from public payload except curated reviewed reports | `requires human review`; exclude by default |
| Copied KiCad demos and KiBot tests | High | `05_OUTPUTS/clean_sample_candidate_tests/` | Installed demos, KiBot tests, local generated candidates | Mixed/unknown | Not fully audited | Exclude copied/generated demo payloads; rebuild clean first-party sample if needed | `requires human review`; exclude by default |
| Screenshot privacy/design leak | High | `03_TOOLS/windows/logs/screenshots/` | Local screenshots | Unknown | May expose workspace or board data | Exclude screenshots unless sanitized | `requires human review`; exclude by default |
| KiCad-derived generated indexes | Medium | `03_TOOLS/kicad_library_intelligence/GENERATED_INDEXES/` | Generated from installed KiCad library metadata | KiCad library terms not audited here | Derived metadata redistribution not reviewed | Prefer regenerate-on-user-machine; include only reviewed summaries | `requires human review` |
| Archived sample provenance unclear | Medium | `04_KICAD_PROJECTS/archive/` | Local samples or copied examples | Unknown | Unclear | Document provenance or replace with first-party sample | `requires human review` |
| Installer package-manager behavior | Medium | `setup/*/install_missing_*` | First-party scripts using external package managers | Project license after review | Script redistributable, external installs are user-side | Review prompts, package IDs, and no-secret behavior | likely OK after review |
| Vendor document source links may drift | Medium | `06_DATASHEETS/00_INDEX/source_lists/` | Vendor portals | First-party metadata | Metadata likely safe, URLs can rot | Validate links before releases; keep no-download default | likely OK after review |
| Unverified footprint/component claims | Medium | `08_COMPONENT_DATABASE/` | First-party component records with placeholders | Project license after review | Likely redistributable | Keep unverified flags; do not claim footprint correctness without source | likely OK after review |
| Public claims overstate maturity | Medium | `README.md`, `README_GPT.md`, `FOR CHAT GPT.MD`, `ROADMAP.md` | First-party docs | Project license after review | Likely redistributable | Keep wording realistic: AI support, not fab approval or official KiCad product | likely OK after review |
| Missing repository manifest/exclusions | Medium | Release packaging config, `.gitignore`, release checklist | First-party release process | Project license after review | Operational risk | Add explicit release include/exclude manifest before publishing | `requires human review` |
| No clean Git metadata in current workspace | Low | Workspace root | Local filesystem state | Not applicable | `git status` unavailable here | Run audit again in intended Git repository before release | `requires human review` |
| Secrets in logs/history | Low to High depending findings | `01_MEMORY/`, `02_HISTORY/`, `05_OUTPUTS/`, logs | Local generated files | Unknown | Not fully audited by this document | Run secret scan before release; remove secrets if found | `requires human review` |

## Blockers Before Public Release

These should be fixed or explicitly excluded before creating a public GitHub repository or release archive:

- Exclude full third-party cloned repos or complete license review and attribution.
- Exclude `KiBot` and `AutoHotkey` vendored copies unless copyleft obligations are accepted and documented.
- Exclude vendor PDFs unless redistribution rights are confirmed.
- Exclude private active/reference KiCad projects.
- Exclude `05_OUTPUTS/` generated/copy payloads unless individually reviewed.
- Exclude local screenshots and GUI logs that may reveal private design data.
- Add a release manifest that states exactly what is included and excluded.

## Safer Public Release Shape

Recommended first public release contents:

- Root public docs: `README.md`, `DISCLAIMER.md`, `CONTRIBUTING.md`, `SECURITY.md`, `ROADMAP.md`, `PUBLIC_RELEASE_CHECKLIST.md`, and this audit set.
- `00_CODEX_START/` operating manuals and agent rules.
- `.prompts/` prompt packs.
- First-party scripts under `03_TOOLS/scripts/`, `setup/`, and `health_check.*` after review.
- Datasheet and component database scaffolding, metadata, and source-link records, without bundled PDFs.
- No private projects, generated output archives, screenshots, or third-party cloned source trees in the release payload.

## Follow-Up Actions

| Action | Owner | Status |
|---|---|---|
| Decide whether public repo should use vendored tools, submodules, or link-only external tool references | requires human review | open |
| Create release include/exclude manifest | maintainer | open |
| Remove or exclude local migrated vendor PDFs from public payload | maintainer | open |
| Replace private/sample KiCad projects with a verified first-party demo if public examples are needed | maintainer | open |
| Review all installer package IDs and prompts | maintainer | open |
| Run secret scan before release | maintainer | open |
| Review project license compatibility with included first-party scripts and docs | requires human review | open |
| Review KiCad trademark/affiliation wording in public docs | requires human review | open |
