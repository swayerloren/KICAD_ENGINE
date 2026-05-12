# Tools Not Bundled By Default

KiCad Engine intentionally does not ship these third-party tools inside the repo
payload.

## Reasons

| Tool or class | Why it is not bundled |
| --- | --- |
| external repos in general | would bloat ZIP downloads and create stale-clone risk |
| `freerouting` | heavyweight external runtime and GPL redistribution review burden |
| `kicad-routing-tools` | better treated as an upstream repo or local clone than bundled source |
| `kicad-component-layout` | external auto-placement repo with compatibility and maintenance uncertainty |
| `kicad-library-utils` | official external utility set, not needed for baseline ZIP use |
| `pcbnew` runtime | provided by the user's KiCad install, not by this repo |
| `node_modules` trees | too large, too machine-specific, and not ZIP-portable |
| Python virtual environments | machine-specific and regenerated locally |
| large binaries, jars, app bundles | portability and attribution burden |

## Repo Rule

KiCad Engine ships the policy, wrappers, requirements, and verification logic.
Users install the optional tools only when they actually need them.
