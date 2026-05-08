# Repo Maintenance Workflow

KiCad Engine is not just a code repo. It also contains durable memory, project history, live-state reports, and AI-quality evidence.

## When Maintenance Matters

- after meaningful project tasks
- after prompt-counter thresholds are reached
- after live-state or gate-reconciliation changes
- after documentation or repo-structure changes that affect handoff quality

## Typical Maintenance Steps

1. rebuild memory indexes
2. rebuild history indexes
3. rebuild AI-quality indexes
4. rebuild `CURRENT_KNOWN_PROBLEMS.md`
5. update handoff docs if repo workflow changed
6. increment the active project prompt counter for the meaningful task

## Important Boundary

Maintenance keeps the repo state readable and honest. It does not replace engineering validation, KiCad ERC/DRC, or human review.

## Related Files

- [`03_TOOLS/scripts/maintenance/run_maintenance_cycle.py`](../03_TOOLS/scripts/maintenance/run_maintenance_cycle.py)
- [`03_TOOLS/scripts/memory_maintenance/README.md`](../03_TOOLS/scripts/memory_maintenance/README.md)
- [`CURRENT_STATUS.md`](../CURRENT_STATUS.md)
- [FOR CHAT GPT.MD](<../FOR CHAT GPT.MD>)
