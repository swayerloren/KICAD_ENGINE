# Session Closeout Checklist

Use this checklist before ending a meaningful Codex or Claude session.

## Required

- [ ] Session log written.
- [ ] Command log written if commands were run.
- [ ] Failed attempts recorded if anything failed.
- [ ] User corrections recorded if the user corrected the agent.
- [ ] AI self-review created.
- [ ] AI response scorecard created.
- [ ] Claim/evidence matrix created for major engineering claims.
- [ ] Uncertainty logs created for unverified items.
- [ ] Hallucination-risk logs created for guessed, inferred, or weakly sourced claims.
- [ ] Quality-gate failure record created if blocked or failed.
- [ ] Project memory updated only for durable project-specific facts.
- [ ] Global memory updated only for reusable repo-wide facts.
- [ ] Open issues created for unresolved problems.
- [ ] Repository index rebuilt if repo structure changed.
- [ ] Memory index and `01_MEMORY/MASTER_MEMORY_INDEX.md` updated.
- [ ] History index and `02_HISTORY/MASTER_HISTORY_INDEX.md` updated.
- [ ] AI quality index updated.
- [ ] `CURRENT_KNOWN_PROBLEMS.md` rebuilt.
- [ ] Prompt counter incremented for the session, or maintenance cycle run if due.
- [ ] `FOR CHAT GPT.MD` updated if repo structure or workflow changed.
- [ ] No secrets were recorded.
- [ ] No KiCad design files were edited without the required gates.
- [ ] Manufacturing-style outputs remain `NOT_FINAL` unless full verification passed and human approval exists.

## Indexing Commands

Use these safe, non-destructive scripts when indexes need rebuilding:

- `python 03_TOOLS/scripts/indexing/build_repo_index.py --repo-root .`
- `python 03_TOOLS/scripts/indexing/build_memory_index.py --repo-root .`
- `python 03_TOOLS/scripts/indexing/build_history_index.py --repo-root .`
- `python 03_TOOLS/scripts/ai_quality/build_current_known_problems.py --repo-root .`
- `python 03_TOOLS/scripts/ai_quality/build_ai_quality_index.py --repo-root .`
