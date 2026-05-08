# Failed Workflows

Reusable memory for workflows that failed and should not be repeated without changes.

Detailed attempts belong in `02_HISTORY/failed_attempts/` or project `history/failed_attempts/`. This file stores only the durable lesson.

## Record Format

```text
ID:
Date:
Status: UNVERIFIED | USER_CONFIRMED | SUPERSEDED
Workflow:
Failure mode:
Root cause:
Do not repeat:
Replacement workflow:
Evidence:
```

## Current Failed Workflows

ID: `DOWNSTREAM_REVIEWS_BEFORE_VALID_PCB_EVIDENCE`
Date: `2026-05-07`
Status: `USER_CONFIRMED`
Workflow: Running JLCPCB, mechanical, BOM production, export, upload feedback, or signoff reviews before prior PCB phases have real evidence.
Failure mode: Reports were created while earlier artifacts were missing, stale, or blocked.
Root cause: Missing hard phase gate and missing current-truth maintenance layer.
Do not repeat: Do not run downstream reviews before phase evidence exists; do not create blocked future-phase reports unless LJ asks for a blocker audit.
Replacement workflow: Run `check_phase_allowed.py` and `run_memory_maintenance.py`; redirect to the next allowed phase.
Evidence: `09_ACCURACY_ENGINE/workflows/MANDATORY_KICAD_PHASE_GATE.md`; `03_TOOLS/scripts/memory_maintenance/`.
