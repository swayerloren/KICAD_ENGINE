# Public Repo Risk Register

Status: `ACTIVE_REGISTER`

## Risk Categories

| Area | Risk | Default Action |
| --- | --- | --- |
| Secrets | API keys or tokens committed | Block release until removed and rotated |
| Datasheets | Unclear redistribution | Convert to link-only |
| Third-party code | Unknown license | Requires human review |
| Installer | Silent install behavior | Block release |
| KiCad assets | Misuse or copied global libraries | Requires review |
| Docs | Unsupported claims | Revise before release |
| Fab outputs | Final-labeled outputs | Relabel/remove until reviewed |

## Rule

Do not delete risky files automatically. Record and escalate.

