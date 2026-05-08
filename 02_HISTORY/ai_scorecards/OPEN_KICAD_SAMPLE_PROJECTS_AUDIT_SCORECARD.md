# AI Response Scorecard - Open KiCad Sample Projects Audit

Date: `2026-05-03`

Overall score: `90/100`

Risk label: `MEDIUM_RISK`

Quality gate: `PASS_FOR_READ_ONLY_AUDIT`, `BLOCKED_FOR_SAMPLE_PROMOTION`

## Scores

| category | score | notes |
| --- | ---: | --- |
| Evidence support | 19/20 | Claims are tied to generated reports and KiCad CLI outputs. |
| KiCad-specific correctness | 18/20 | Used `kicad-cli` ERC/DRC and SVG exports; no design edits. Close-up crops could not be generated without configs. |
| Datasheet/component accuracy | 14/15 | No unverified datasheet values were introduced. |
| Safety/compliance with repo rules | 15/15 | Read-only sample audit; no KiCad source edits or manufacturing exports. |
| Memory/history routing correctness | 9/10 | Global history/quality routing was used. |
| Uncertainty disclosure | 9/10 | Close-up visual and design-intent limitations were documented. |
| End-user usefulness | 6/10 | Strong blocker report, but samples still need future repair/enrichment for demo usefulness. |

## Result

The audit deliverable is usable. The imported sample set remains blocked from promotion until future repair and re-audit.

