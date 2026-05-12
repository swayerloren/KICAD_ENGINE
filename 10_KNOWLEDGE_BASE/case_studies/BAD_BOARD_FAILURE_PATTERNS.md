# Bad Board Failure Patterns

Status: `QUALITY_GATE_INPUT`

## Common Failure Themes

- clean DRC but open or unrouted nets remain
- connector mounted on the wrong board edge or facing inward
- right-angle and acute trace corners accepted as "good enough"
- long boxy routes around the board perimeter instead of compact local routing
- test pads placed at the end of long stubs
- RF keepout treated as optional
- decoupling or buck loops spread out for convenience

## How To Use

- Convert repeated failure themes into explicit gate checks.
- Use them as examples in review reports and onboarding notes.
- Keep exact root-cause claims `UNVERIFIED` unless the upstream source is
  official or independently corroborated.

## Registry Anchors

| Registry ID | Domain | Confidence | Lesson |
| --- | --- | --- | --- |
| `url_010180` | `pcb.mit.edu` | `MEDIUM` | debug-focused training can show failure modes, not final rules |
| `url_008388` | `richtek.com` | `LOW_TO_MEDIUM` | vendor app-note capture needs official-path confirmation |
| `url_000720` | `docs.kicad.org` | `HIGH` | official KiCad docs remain process evidence, not board-case proof |

