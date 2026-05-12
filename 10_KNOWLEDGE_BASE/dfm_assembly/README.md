# DFM / Assembly Knowledge

Status: `LINK_FIRST_DFM_ASSEMBLY_SURFACE`

## Purpose

Store normalized DFM, assembly, and fabrication-package guidance without making
raw copied fab-house pages the canonical source of truth.

## Canonical Files

- [DFM_SUMMARY.md](DFM_SUMMARY.md)
- [ASSEMBLY_WORKMANSHIP_SUMMARY.md](ASSEMBLY_WORKMANSHIP_SUMMARY.md)
- [PCB_FAB_CONSTRAINTS_SUMMARY.md](PCB_FAB_CONSTRAINTS_SUMMARY.md)

## Rules

- Fab-house pages may inform checklists and summaries, but copied page payloads
  remain quarantined unless redistribution is clearly allowed.
- Fab package validation is not assembly approval.
- Pick-and-place rotations and connector orientation require visual/human
  review.
- All manufacturing-style outputs remain `NOT_FINAL` until final gates pass and
  LJ approves.
