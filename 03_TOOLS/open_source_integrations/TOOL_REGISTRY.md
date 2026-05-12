# Optional Tool Registry

Status values used here:

- `approved_optional_local_use`
- `approved_external_only`
- `evaluation_required_before_write`

## Registry

| Tool | Source URL | License | Distribution mode | Primary use | Can edit KiCad files | Read-only safe | CI allowed | Allowed in ZIP release |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `KiParse` | `https://github.com/Atlantix-EDA/KiParse` | MIT | optional | fast schematic/PCB parsing | no known write path in normal usage | yes | yes | no, docs/wrappers only |
| `kicad-python / pcbnew` | `https://gitlab.com/kicad/code/kicad-python` | MIT for `kicad-python`; KiCad install required for `pcbnew` runtime | external-only | native KiCad board API | yes | only when scripts are written read-only | conditional | no |
| `kicad-sch-api` | `https://github.com/circuit-synth/kicad-sch-api` | Apache-2.0 | optional | schematic parsing and generation API | yes | yes for parse-only use | yes | no |
| `SKiDL` | `https://github.com/devbisme/skidl` | MIT | optional | Python-based circuit generation and review helpers | yes | yes for review-only use | yes | no |
| `circuit-synth` | `https://github.com/circuit-synth/circuit-synth` | MIT | optional | circuit description and schematic automation | yes | yes for review-only use | yes | no |
| `freerouting` | `https://github.com/freerouting/freerouting` | GPL-3.0 | external-only | routing rehearsal and feasibility | yes | no by default | conditional | no |
| `kicad-routing-tools` | `https://github.com/mcbridejc/kicad-routing-tools` | MIT | external-only | routing workflows and experiments | yes | no by default | conditional | no |
| `kicad-component-layout` | `https://github.com/asyafix/kicad-component-layout` | GPL-3.0 | external-only | auto-placement experiments | yes | no by default | no by default | no |
| `KiKit` | `https://github.com/yaqwsx/KiKit` | GPL-3.0 | optional | panelization and fab-package helpers | yes | yes for analysis-only subcommands | yes with review | no |
| `KiBot` | `https://github.com/INTI-CMNB/KiBot` | AGPL-3.0 | optional | ERC/DRC wrappers, outputs, automation | yes | yes for read-only validation runs | yes with review | no |
| `gerbonara` | `https://github.com/jaseg/gerbonara` | Apache-2.0 | optional | Gerber and Excellon parsing | no | yes | yes | no |
| `PyGerber` | `https://github.com/Argmaster/pygerber` | MIT | optional | Gerber parsing and rendering | no | yes | yes | no |
| `InteractiveHtmlBom` | `https://github.com/openscopeproject/InteractiveHtmlBom` | MIT | optional | interactive BOM review | yes via plugin/export flow | yes for review generation | yes with review | no |
| `PcbDraw` | `https://github.com/yaqwsx/PcbDraw` | MIT | optional | PCB rendering and visual review | no | yes | yes | no |
| `kicad-happy` | `https://github.com/aklofas/kicad-happy` | MIT | optional | KiCad data extraction and utilities | yes | yes for read-only scripts | yes | no |
| `kicad-library-utils` | `https://gitlab.com/kicad/libraries/kicad-library-utils` | GPL-3.0 | external-only | official library maintenance helpers | yes | conditional | conditional | no |

## Practical Approval Summary

- Approved by default for optional local read-only use:
  - `KiParse`
  - `kicad-sch-api`
  - `SKiDL`
  - `circuit-synth`
  - `KiBot`
  - `KiKit`
  - `gerbonara`
  - `PyGerber`
  - `InteractiveHtmlBom`
  - `PcbDraw`
  - `kicad-happy`
- Approved only as external dependencies, not bundled:
  - `kicad-python / pcbnew`
  - `freerouting`
  - `kicad-routing-tools`
  - `kicad-component-layout`
  - `kicad-library-utils`

## Write-Scope Warning

Many tools in this list can edit KiCad assets or generate derivative design
artifacts. Approval for optional local use does not override the route-specific
KiCad edit gates in `AGENTS.md` and `00_CODEX_START/`.
