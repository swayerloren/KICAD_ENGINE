# University Training Index

Status: `GUIDANCE_ONLY`

This index records which training-style source families are worth consulting and
how much trust they deserve.

## Confidence Bands

- `MEDIUM`: structured lecture archives and university lab material that teach
  process or debugging habits.
- `LOW_TO_MEDIUM`: tutorial collections from fabricators or consultants.
- `LOW`: mixed link farms, general web roundups, and stale course mirrors.

## Approved Use

- Build review checklists.
- Build onboarding notes for schematic or PCB flow.
- Extract repeated failure patterns that must still be verified elsewhere.

## Not Approved As Sole Evidence

- Exact footprint approval
- Connector orientation proof
- Final fab constraint approval
- ERC/DRC equivalence claims
- AI auto-layout readiness claims

## Representative Registry Entries

| Registry ID | Domain | Confidence | Use |
| --- | --- | --- | --- |
| `url_010180` | `pcb.mit.edu` | `MEDIUM` | lecture archive and debugging prompts |
| `url_000012` | `dev-docs.kicad.org` | `HIGH` | promoted elsewhere as official KiCad docs |
| `url_001060` | `docs.oshpark.com` | `MEDIUM` | fabrication workflow comparison only |
| `url_004526` | `jlcpcb.com` | `MEDIUM` | fab capability awareness, not universal rule |

## Migration Outcome

The drained university-training intake mixed official
KiCad docs, vendor app notes, fabricator help pages, GitHub indexes, and forum
threads. That means the raw captures are not a clean canonical training set and
must not be promoted directly into source-of-truth folders.
