# Legal And License Audit

Purpose: practical public-release risk audit for KiCad Engine. This is not legal advice and does not make legal conclusions. Items marked `requires human review` need owner, license, attribution, or redistribution confirmation before a public GitHub release.

## Release Position

KiCad Engine should ship as a local-first KiCad AI workspace, scripts, prompts, and metadata. Public releases should avoid bundling third-party repositories, vendor PDFs, private KiCad projects, generated fabrication outputs, screenshots, or copied demo projects unless each item has a reviewed license and explicit release decision.

Recommended default public payload:

- First-party docs, prompts, schemas, and scripts.
- Link-only datasheet and vendor-document metadata unless redistribution rights are confirmed.
- Generated indexes only when they are clearly derived, license-reviewed, and easy for users to regenerate locally.
- No `03_TOOLS/repos/`, `03_TOOLS/windows/repos/`, `05_OUTPUTS/`, private active projects, or vendor PDFs in the public release archive until reviewed.

## Audit Summary

| Area | File/folder | Source | License if known | Redistribution status | Recommended action | Safe public release status |
|---|---|---|---|---|---|---|
| Third-party tool repo | `03_TOOLS/repos/InteractiveHtmlBom/` | openscopeproject/InteractiveHtmlBom | MIT from local `LICENSE`; copyright qu1ck | Likely allowed with license retention, but bundled full repo requires review | Prefer source link or submodule/install instructions; if bundled, keep license and attribution | `requires human review` |
| Third-party tool repo | `03_TOOLS/repos/KiBot/` | INTI-CMNB/KiBot | AGPL-3.0 from local `LICENSE` | High compliance risk if bundled | Do not include full repo in public payload until AGPL obligations are reviewed | `requires human review`; exclude by default |
| Third-party tool repo | `03_TOOLS/repos/kicad-happy/` | aklofas/kicad-happy | MIT from local `LICENSE` | Likely allowed with license retention, but bundled full repo requires review | Prefer source link or submodule/install instructions | `requires human review` |
| Third-party tool repo | `03_TOOLS/repos/kicad-mcp-pro/` | oaslananka/kicad-mcp-pro | MIT from local `LICENSE` | Likely allowed with license retention, but bundled full repo requires review | Prefer source link or submodule/install instructions | `requires human review` |
| Third-party tool repo | `03_TOOLS/repos/KiCAD-MCP-Server/` | mixelpixx/KiCAD-MCP-Server | MIT from local `LICENSE` | Likely allowed with license retention, but bundled full repo requires review | Prefer source link or submodule/install instructions | `requires human review` |
| Third-party tool repo | `03_TOOLS/repos/kicanvas/` | theacodes/kicanvas | MIT from local `LICENSE.md`; includes nested third-party licenses | Requires review of nested assets and documentation licenses | Prefer source link or submodule/install instructions; review nested notices before bundling | `requires human review` |
| Third-party tool repo | `03_TOOLS/repos/PcbDraw/` | yaqwsx/PcbDraw | MIT from local `LICENSE` | Likely allowed with license retention, but bundled full repo requires review | Prefer source link or submodule/install instructions; verify attribution text encoding | `requires human review` |
| Third-party Windows repo | `03_TOOLS/windows/repos/AutoHotkey/` | AutoHotkey/AutoHotkey | GPL-2.0 from local `license.txt` | High compliance risk if bundled | Do not include full repo in public payload until GPL obligations are reviewed | `requires human review`; exclude by default |
| Third-party Windows repo | `03_TOOLS/windows/repos/FlaUI/` | FlaUI/FlaUI | MIT from local `LICENSE.txt` | Likely allowed with license retention, but bundled full repo requires review | Prefer source link or package-manager install instructions | `requires human review` |
| Third-party Windows repo | `03_TOOLS/windows/repos/FlaUInspect/` | FlaUI/FlaUInspect | MIT from local `LICENSE` | Likely allowed with license retention, but bundled full repo requires review | Prefer source link or release-download instructions | `requires human review` |
| Third-party Windows repo | `03_TOOLS/windows/repos/SikuliX1/` | RaiMan/SikuliX1 | MIT from local `LICENSE`; nested license files present | Requires review of nested components and assets | Prefer source link or package instructions; review nested licenses before bundling | `requires human review` |
| Vendor datasheets | `06_DATASHEETS/99_UNSORTED_INBOX/LEGACY_MIGRATION_20260502_161444/ESPRESSIF/ESP32-S3-WROOM-1U/*.pdf` | Espressif documents, exact redistribution rights not confirmed | Unknown from local files | Public redistribution unclear | Replace public payload with link-only metadata unless redistribution permission is confirmed | `requires human review`; link-only recommended |
| Copied/generated demos | `05_OUTPUTS/clean_sample_candidate_tests/installed_demos_20260430_173955/` | Installed KiCad demos or copied external demos | Mixed local license files; not fully audited | Public redistribution unclear per project | Exclude generated demo copies from public payload unless each source license is reviewed | `requires human review`; exclude by default |
| Copied/generated KiBot tests | `05_OUTPUTS/clean_sample_candidate_tests/kibot_kicad9_20260430_173845/` | KiBot test data copied/generated locally | Likely governed by KiBot repo terms; not independently reviewed | High risk if redistributed as generated payload | Exclude from public payload | `requires human review`; exclude by default |
| Generated sample project | `05_OUTPUTS/clean_sample_candidate_tests/resistor_tht_20260430_173726/` | Local/generated sample or copied example, source not confirmed | Unknown | Unclear | Recreate as first-party sample or exclude until provenance is documented | `requires human review` |
| Private/reference KiCad design | `04_KICAD_PROJECTS/active/COMMAND_LINK_VERIFIED_REFERENCE/` | User/reference finished board copy | Unknown private/project ownership | Not safe without explicit owner approval | Exclude from public payload; keep private or replace with first-party demo | `requires human review`; exclude by default |
| Active KiCad project | `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/` | Current user project | First-party status not confirmed | Not safe without explicit owner approval | Exclude unless intentionally published as a reviewed sample | `requires human review` |
| Archived KiCad sample | `04_KICAD_PROJECTS/archive/CLEAN_KICAD_PASSING_SAMPLE/` | Source unclear; may contain copied symbols/footprints | Unknown | Unclear | Document provenance or regenerate as clean first-party sample | `requires human review` |
| Archived KiCad sample | `04_KICAD_PROJECTS/archive/SAMPLE_KICAD_TEST_PROJECT/` | Local sample or copied example, source unclear | Unknown | Unclear | Document provenance before public release | `requires human review` |
| KiCad-derived generated indexes | `03_TOOLS/kicad_library_intelligence/GENERATED_INDEXES/` | Generated from installed KiCad libraries | KiCad library metadata license not audited here | Likely safer to regenerate locally; redistribution of derived metadata requires review | Exclude generated indexes from release or include only summaries after attribution review | `requires human review` |
| Screenshots | `03_TOOLS/windows/logs/screenshots/` | Local GUI screenshots | Unknown; may contain private project/workspace info | Privacy and design-leak risk | Exclude from public payload unless sanitized | `requires human review`; exclude by default |
| Installer scripts | `setup/` and `health_check.*` | First-party scripts | Project license after review | Redistributable if first-party and reviewed | Review package IDs, prompts, and no-secret behavior before release | Likely OK after script review |
| Prompt packs and docs | `.prompts/`, `00_CODEX_START/`, root quickstarts | First-party generated docs | Project license after review | Likely redistributable | Keep realistic claims and no vendor content copied beyond short references | Likely OK after review |

## Items Requiring Human Review Before Release

- Confirm the project-level license in `LICENSE` is appropriate for first-party docs, scripts, and prompts.
- Decide whether third-party tool repos are excluded, converted to submodules, or replaced by source links and setup instructions.
- Review AGPL/GPL implications for `KiBot` and `AutoHotkey` before bundling any part of those repositories.
- Confirm whether vendor PDFs may be redistributed. If not confirmed, use link-only source records.
- Decide whether any KiCad projects under `04_KICAD_PROJECTS/active/` or `04_KICAD_PROJECTS/archive/` are intentional public samples.
- Exclude or sanitize local screenshots and generated outputs.
- Review generated KiCad library indexes for attribution and license compatibility.

## Practical Public Release Gate

Before a public GitHub release, verify:

- No secrets or local credentials are present.
- No vendor PDFs are bundled unless redistribution rights are confirmed.
- No private project files or generated fabrication packages are included by accident.
- No full third-party cloned repos are bundled without license review and attribution.
- License files for any included third-party code are retained.
- Attribution is present for included third-party code, assets, and generated data.
- Public docs avoid claiming database completeness, fabrication approval, or official KiCad affiliation.
