# Public Release Next Steps

Date: 2026-05-03

## Required Before Public GitHub Release

1. Create a clean public release branch or export.
   - Add `.gitignore`.
   - Exclude `node_modules`, `installer/build`, `03_TOOLS/repos`, `03_TOOLS/windows/repos`, `03_TOOLS/python_envs`, `03_TOOLS/node_envs`, `05_OUTPUTS`, `99_BACKUPS`, and private project folders.
   - Use `installer/payload/repo-template` as the baseline for the installable workspace.

2. Remove or exclude PDFs with unclear redistribution.
   - Replace bundled Espressif PDFs with source-link metadata.
   - Keep local/private PDFs out of public release archives.

3. Remove or exclude private and unclear-provenance KiCad projects.
   - Exclude `COMMAND_LINK_VERIFIED_REFERENCE`.
   - Exclude `ESP32_CSI_WIFI_NODE` unless it is explicitly sanitized and approved as a public sample.
   - Replace current samples with a first-party minimal sample if public examples are needed.

4. Remove generated manufacturing-style outputs from public source.
   - Keep only docs and scripts.
   - If sample outputs are needed, regenerate them from a public sample and label them `NOT_FINAL`.

5. Complete legal/license cleanup.
   - Decide whether third-party tools are links, submodules, installer-managed dependencies, or vendored code.
   - Do not vendor AGPL/GPL/mixed-license repos without explicit compliance review.
   - Keep attribution docs updated.

6. Run a real secret scan on the intended release tree.
   - The clean payload passed this audit's checks.
   - The development tree still has old logs and should not be treated as release-clean.

7. Test installer artifacts on clean systems.
   - Windows: signed or explicitly unsigned EXE, GUI launch/install/uninstall, clean Windows VM/account, SmartScreen notes.
   - macOS: DMG/PKG build on macOS runner, signing, notarization, stapling, Gatekeeper test.
   - Linux: AppImage launch tests, DEB install/uninstall tests, manual tar or zip fallback.

8. Run GitHub Actions in the actual public repository.
   - Confirm Windows/macOS/Linux workflows complete.
   - Confirm artifacts and SHA256 checksums are uploaded.
   - Confirm draft release workflow remains draft-only.

9. Add public sample/benchmark evidence later.
   - Create a clean first-party KiCad sample project.
   - Run ERC/DRC/BOM/package checks.
   - Use `15_BENCHMARKS` only after actual runs exist.

## Suggested Public Alpha Release Shape

Ship:

- First-party docs.
- Prompt packs.
- VS Code config.
- Setup scripts.
- Health checks.
- Installer source.
- Clean payload template.
- Datasheet/component scaffolding and link-only metadata.
- Accuracy, knowledge, library, reference-design, ingestion, layout, and benchmark docs.

Do not ship:

- Private projects.
- Generated outputs.
- Vendor PDFs.
- Third-party cloned repos.
- Virtual environments.
- Build artifacts.
- Old command logs.
- Screenshots.
- Any final fab package.

## Classification Target Path

- Current: `INTERNAL_ALPHA`.
- Next target: `PUBLIC_ALPHA` after source cleanup, PDF removal, public branch creation, and payload-only release review.
- Later target: `PUBLIC_BETA` after clean-machine installer tests on Windows, macOS, and Linux.
- Final target: `PUBLIC_RELEASE_READY` after signing/notarization, legal review, sample project validation, and release workflow proof.
