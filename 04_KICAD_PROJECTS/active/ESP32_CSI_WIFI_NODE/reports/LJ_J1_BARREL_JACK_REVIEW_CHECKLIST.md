# LJ J1 Barrel Jack Review Checklist

Status: `ACTIVE_BLOCKER`

Generated: `2026-05-07`

Scope: LJ visual/mechanical review checklist for J1 after barrel-jack orientation repair. Routing remains blocked.

## Classification

`J1_BLOCKED_NEEDS_VERIFIED_3D_MODEL_OR_DIFFERENT_FOOTPRINT`

## Checklist

| Check | Audit status | Evidence |
|---|---|---|
| J1 female barrel opening faces down/off-board at bottom edge | `PROVEN_2D` | F.Fab long-body/front side reaches `Y=94.5`; F.CrtYd front reaches bottom edge `Y=95.0` |
| J1 3-pin solder/backside faces up/inward into PCB | `PROVEN_2D` | pads at `(14.0,80.8)`, `(14.0,86.8)`, `(18.7,83.8)` |
| J1 is not side-mounted | `PROVEN` | J1 is bottom-edge placed with front side toward `Y=95.0`, not left/right edge |
| J1 pads remain on PCB | `PROVEN` | all pad centers inside `X=0..60`, `Y=0..95` board bounds |
| J1 body/courtyard avoids J2 | `PROVEN_BY_SEPARATION_AND_DRC` | J1 courtyard approx `X=9.0..20.5`; J2 at `X=39.0` |
| J1 body/courtyard avoids MH1 | `PROVEN_BY_SEPARATION_AND_DRC` | MH1 at `(4.0,91.0)` outside J1 courtyard bbox |
| J1 body/courtyard avoids MH2 | `PROVEN_BY_SEPARATION_AND_DRC` | MH2 at `(56.0,91.0)` outside J1 courtyard bbox |
| J1 body/courtyard avoids SW1 | `PROVEN_BY_SEPARATION_AND_DRC` | SW1 at `(6.0,64.0)` below/away from J1 courtyard |
| J1 body/courtyard avoids SW2 | `PROVEN_BY_SEPARATION_AND_DRC` | SW2 at `(6.0,54.0)` below/away from J1 courtyard |
| J1 body/courtyard avoids test pads | `PROVEN_BY_SEPARATION_AND_DRC` | TP1-TP9 are right-side row at `X=57.0`, `Y=40.0..72.0` |
| J1 exact 3D model exists | `NOT_PROVEN` | referenced PJ-102AH STEP missing from installed KiCad 9 model library |
| J2 remains bottom-edge mouth-down/off-board | `PROVEN` | J2 PCB Edge line transforms to `(34.0,95.0)` through `(44.0,95.0)` |
| Routing remains blocked | `YES` | current project state and connector rules block routing |

## LJ Review Notes

- The 2D footprint geometry supports the corrected J1 orientation.
- Do not approve J1 from 3D until the exact PJ-102AH-style 3D model is installed or the footprint is replaced with a verified connector/footprint/model set.
- Routing allowed: `NO`
- Copper pour allowed: `NO`

