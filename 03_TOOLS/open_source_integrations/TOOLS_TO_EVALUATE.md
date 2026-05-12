# Tools To Evaluate

These tools are known candidates but need human or workflow-specific review
before KiCad Engine should rely on them for write-scope tasks.

## Evaluation Backlog

| Tool | Current status | Why not default yet | Evaluation focus |
| --- | --- | --- | --- |
| `freerouting` | external-only | heavyweight runtime, can modify routes, GPL obligations | copied-board rehearsal only, deterministic export/import path, geometry audit follow-up |
| `kicad-routing-tools` | external-only | experimental workflow, not first-party, unclear long-term maintenance | narrow routing rehearsal use and reproducibility |
| `kicad-component-layout` | external-only | aging auto-placement repo, GPL, possible stale KiCad compatibility | version compatibility, output safety, copied-board-only use |
| `kicad-library-utils` | external-only | official but library-maintenance oriented, not a drop-in project gate tool | read-only helper value vs direct repo scripts |
| `SKiDL` | approved optional read-only, write tasks still restricted | can generate designs rather than only inspect them | enforce docs-only or sandbox use in task-specific prompts |
| `circuit-synth` | approved optional read-only, write tasks still restricted | can synthesize schematics, not just inspect them | proof boundaries and task routing |
| `InteractiveHtmlBom` | approved optional, release use still restricted | can generate user-facing package artifacts | `NOT_FINAL` release labeling and reproducible generation |
| `KiBot` | approved optional, release use still restricted | AGPL and broad output surface | command whitelisting, artifact scope, CI rules |

## Default Evaluation Questions

1. Can it stay optional and unbundled?
2. Can it fail gracefully when missing?
3. Can it be run read-only?
4. Can its output be independently verified?
5. Does it create licensing or redistribution burden?
6. Does it require a copied-project or sandbox-only workflow?
