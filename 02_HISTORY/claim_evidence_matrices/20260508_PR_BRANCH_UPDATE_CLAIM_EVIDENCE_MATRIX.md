# Claim / Evidence Matrix - PR Branch Update

| Claim | Evidence | Status |
| --- | --- | --- |
| The current branch for this task is `hardening/execution-contract`. | `git branch --show-current` | `VERIFIED_BY_COMMAND` |
| The pending worktree contains documentation, generated-index, maintenance, and history artifacts rather than KiCad design-file edits. | `git status --short`, `git diff --name-only` | `VERIFIED_BY_COMMAND` |
| No `.kicad_sch` or `.kicad_pcb` files are intended for staging. | changed-path inspection before staging | `VERIFIED_BY_COMMAND` |
| PR `#1` is the branch target to update after push. | user-supplied PR URL plus post-push `gh pr view 1` verification | `VERIFIED_BY_CONTEXT_OR_COMMAND` |
