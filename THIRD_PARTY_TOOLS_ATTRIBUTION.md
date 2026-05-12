# Third-Party Tools Attribution

Purpose: inventory third-party tools currently present in the workspace and the attribution or release action needed before public GitHub release. This is a practical audit, not legal advice.

## Optional Integration Layer

The current default public-release posture is now:

- keep first-party wrappers, requirements files, and tool profiles in Git
- keep heavyweight upstream repos and install trees out of Git by default
- route optional-tool evaluation through `03_TOOLS/open_source_integrations/`
- treat mixed-license tools such as `MIT`, `Apache-2.0`, `GPL-3.0`, and
  `AGPL-3.0` as documented integrations, not automatic bundling approval

Primary docs:

- `03_TOOLS/open_source_integrations/TOOL_REGISTRY.md`
- `03_TOOLS/open_source_integrations/LICENSE_AND_ATTRIBUTION_RULES.md`
- `03_TOOLS/open_source_integrations/TOOLS_NOT_BUNDLED_REASON.md`

## Release Recommendation

Do not publish full cloned third-party repositories by default. Prefer one of these safer patterns:

- Keep only first-party wrapper scripts and documentation.
- Link to upstream repositories and tell users how to install tools locally.
- Use submodules only after license and maintenance review.
- If a third-party repo is bundled, retain its license file, copyright notices, source URL, and any nested notices.

## Third-Party Repository Inventory

| Local path | Upstream/source | License observed locally | Attribution required | Redistribution status | Recommended public release action | Safe public release status |
|---|---|---|---|---|---|---|
| `03_TOOLS/repos/InteractiveHtmlBom/` | `https://github.com/openscopeproject/InteractiveHtmlBom.git` | MIT | Preserve MIT license and copyright notice for qu1ck; preserve upstream URL | likely allowed with attribution, but full-repo bundling requires review | Replace with source link or documented install step; if included, keep license | `requires human review` |
| `03_TOOLS/repos/KiBot/` | `https://github.com/INTI-CMNB/KiBot.git` | AGPL-3.0 | Preserve AGPL license and upstream notices; review network/source obligations | high compliance risk if bundled | Exclude from public payload unless AGPL obligations are accepted and documented | `requires human review`; exclude by default |
| `03_TOOLS/repos/kicad-happy/` | `https://github.com/aklofas/kicad-happy.git` | MIT | Preserve MIT license and copyright notice for Andrew Klofas | likely allowed with attribution, but full-repo bundling requires review | Replace with source link or documented install step | `requires human review` |
| `03_TOOLS/repos/kicad-mcp-pro/` | `https://github.com/oaslananka/kicad-mcp-pro.git` | MIT | Preserve MIT license and copyright notice for Osman Aslan | likely allowed with attribution, but full-repo bundling requires review | Replace with source link or documented install step | `requires human review` |
| `03_TOOLS/repos/KiCAD-MCP-Server/` | `https://github.com/mixelpixx/KiCAD-MCP-Server.git` | MIT | Preserve MIT license and copyright notice for mixelpixx | likely allowed with attribution, but full-repo bundling requires review | Replace with source link or documented install step | `requires human review` |
| `03_TOOLS/repos/kicanvas/` | `https://github.com/theacodes/kicanvas.git` | MIT plus nested third-party notices | Preserve KiCanvas MIT license, upstream URL, and nested third-party license notices | requires nested asset/license review | Replace with source link or submodule; if bundled, audit nested notices first | `requires human review` |
| `03_TOOLS/repos/PcbDraw/` | `https://github.com/yaqwsx/PcbDraw.git` | MIT | Preserve MIT license and copyright notice for Jan Mrazek; verify local text encoding | likely allowed with attribution, but full-repo bundling requires review | Replace with source link or documented install step | `requires human review` |
| `03_TOOLS/windows/repos/AutoHotkey/` | `https://github.com/AutoHotkey/AutoHotkey.git` | GPL-2.0 | Preserve GPL license and all upstream notices | high compliance risk if bundled | Exclude from public payload; document official install path instead | `requires human review`; exclude by default |
| `03_TOOLS/windows/repos/FlaUI/` | `https://github.com/FlaUI/FlaUI.git` | MIT | Preserve MIT license and upstream notices | likely allowed with attribution, but full-repo bundling requires review | Prefer package/source link rather than bundling | `requires human review` |
| `03_TOOLS/windows/repos/FlaUInspect/` | `https://github.com/FlaUI/FlaUInspect.git` | MIT | Preserve MIT license and FlaUI notice | likely allowed with attribution, but full-repo bundling requires review | Prefer release/source link rather than bundling | `requires human review` |
| `03_TOOLS/windows/repos/SikuliX1/` | `https://github.com/RaiMan/SikuliX1.git` | MIT plus nested licenses | Preserve MIT license, upstream notice for Raimund Hocke, and nested component notices | requires nested component/license review | Prefer source link or install instructions; do not bundle until nested review is complete | `requires human review` |

## Nested License Attention Areas

| Local path | Source | License if known | Redistribution status | Recommended action | Safe public release status |
|---|---|---|---|---|---|
| `03_TOOLS/repos/kicanvas/` | KiCanvas nested assets and dependencies | Mixed; includes nested license files | Not fully audited | Review all nested third-party notices before bundling | `requires human review` |
| `03_TOOLS/windows/repos/SikuliX1/API/src/main/java/jxgrabkey/LICENSE.txt` | SikuliX nested component | Present locally, exact terms not summarized here | Not fully audited | Review and preserve notice if bundled | `requires human review` |
| `03_TOOLS/windows/repos/SikuliX1/IDE/src/main/resources/Lib/xlutils/license.txt` | SikuliX nested library | Present locally, exact terms not summarized here | Not fully audited | Review and preserve notice if bundled | `requires human review` |
| `03_TOOLS/windows/repos/SikuliX1/IDE/src/main/resources/Settings/LICENSE` | SikuliX nested resource | Present locally, exact terms not summarized here | Not fully audited | Review and preserve notice if bundled | `requires human review` |
| `05_OUTPUTS/clean_sample_candidate_tests/installed_demos_20260430_173955/*/LICENSE*` | Copied/generated demo projects | Mixed local license files | Not fully audited | Exclude generated demo copies unless each demo is approved for redistribution | `requires human review` |

## Installer And Setup References

The setup scripts may refer to external tools such as KiCad, Git, Python, Node.js, VS Code, winget, Homebrew, Linux package managers, and optional KiCad utilities. The scripts should not redistribute those tools. They should prompt users and route installation through official package managers or official vendor download pages.

| File/folder | Source | License if known | Redistribution status | Recommended action | Safe public release status |
|---|---|---|---|---|---|
| `setup/windows/install_missing_windows_tools.ps1` | First-party wrapper using package manager commands | Project license after review | Redistributable as first-party script | Confirm prompts, package IDs, and no silent installs | likely OK after review |
| `setup/macos/install_missing_macos_tools.sh` | First-party wrapper using package manager commands | Project license after review | Redistributable as first-party script | Confirm prompts and Homebrew behavior | likely OK after review |
| `setup/linux/install_missing_linux_tools.sh` | First-party wrapper using package manager commands | Project license after review | Redistributable as first-party script | Confirm distro package IDs and no silent installs | likely OK after review |

## Attribution Checklist

Before including any third-party code, assets, or generated derivative data:

- Record upstream source URL and commit or release version.
- Preserve the full license file and copyright notices.
- Preserve nested third-party notices where present.
- Document whether the repo is vendored, submoduled, or installed externally.
- Confirm whether copyleft obligations are acceptable for the public repo.
- Keep third-party source separate from first-party KiCad Engine scripts.
- Do not imply third-party projects endorse KiCad Engine unless explicit permission exists.
