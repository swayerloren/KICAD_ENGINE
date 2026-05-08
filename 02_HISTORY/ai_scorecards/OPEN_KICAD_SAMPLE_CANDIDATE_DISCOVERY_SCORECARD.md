# AI Response Scorecard - Open KiCad Sample Candidate Discovery

Date: 2026-05-03

Overall score: `88/100`

Risk label: `MEDIUM_RISK`

## Category Scores

| Category | Score | Notes |
|---|---:|---|
| Evidence support | 18/20 | Repository metadata and license-file checks support file/license claims. Candidate usefulness is partly judgment. |
| KiCad-specific correctness | 18/20 | Required KiCad file presence was checked by metadata; no files were imported or opened in KiCad. |
| Datasheet/component accuracy | 15/15 | No datasheet/component values were fabricated. |
| Safety/compliance with repo rules | 15/15 | No clone, download, import, active project edit, or fabrication output. |
| Memory/history routing correctness | 9/10 | Closeout records created in global history; no project memory required. |
| Uncertainty disclosure | 8/10 | Human license review and first-import approval requirements are visible. |
| End-user usefulness | 5/10 | Useful shortlist created; next step still requires approval and import testing. |

## Quality Gate

Result: `PASS_FOR_CANDIDATE_DISCOVERY_ONLY`

Blocked actions:

- Importing any candidate without explicit user approval.
- Public bundling without human license and attribution review.
- Treating source-included Gerbers as KiCad Engine manufacturing outputs.
