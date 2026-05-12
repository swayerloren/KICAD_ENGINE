# Tools Approved For Optional Local Use

These tools are approved for optional local use inside KiCad Engine under the
stated conditions. Approval here does not override task routers, KiCad edit
gates, or release gates.

## Approved Optional Local Use

| Tool | Approval scope | Key condition |
| --- | --- | --- |
| `KiParse` | parsing and read-only data extraction | keep use read-only |
| `kicad-sch-api` | schematic parsing and structured inspection | do not treat generated output as annotation proof |
| `SKiDL` | circuit reasoning, linting experiments, examples | do not overwrite project schematics without a separate approved route |
| `circuit-synth` | structured circuit reasoning and prototype generation | sandbox or docs-first use only unless a later route approves writes |
| `KiBot` | local validation, report generation, controlled `NOT_FINAL` outputs | no final manufacturing claims without normal gates |
| `KiKit` | panelization research and fab-profile rehearsal | copied-output or sandbox use until explicitly approved |
| `gerbonara` | read-only Gerber and drill validation | safe for CI and ZIP-portable wrappers |
| `PyGerber` | read-only Gerber rendering and checks | safe for CI and ZIP-portable wrappers |
| `InteractiveHtmlBom` | local BOM review and review artifacts | generated artifacts remain review outputs |
| `PcbDraw` | PCB render generation for review | review output only |
| `kicad-happy` | read-only KiCad data extraction helpers | confirm command behavior before write use |

## Approved External-Only Use

These are allowed as separately installed dependencies but are not approved for
bundling into the repo:

- `kicad-python / pcbnew`
- `freerouting`
- `kicad-routing-tools`
- `kicad-component-layout`
- `kicad-library-utils`

## Mandatory Conditions

- missing tools must not break unrelated workflows
- install wrappers must stay dry-run by default
- cloned repos and environments must remain outside tracked Git content
- KiCad design edits still require the normal task route and evidence gates
