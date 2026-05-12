# Claim / Evidence Matrix

| Claim | Evidence |
| --- | --- |
| `64` files moved | ledger rows tagged with `phase=fab_dfm_compliance_knowledge_move` |
| target folders drained | source-folder existence checks returned `False` for all `5` folders |
| raw standards/compliance captures quarantined | ledger action `MOVE_TO_LICENSE_QUARANTINE` plus quarantine destination paths |
| no manufacturing outputs generated | `manufacturing/rev_A` checks remained `False` |
| no KiCad design files changed in this task | `git diff --name-only -- '*.kicad_sch' '*.kicad_pcb' '*.kicad_pro'` showed only the preexisting schematic path |
