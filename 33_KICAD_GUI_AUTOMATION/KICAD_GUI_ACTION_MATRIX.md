# KiCad GUI Action Matrix

| Action | Default mode | Required flags | Hard blockers | Notes |
| --- | --- | --- | --- | --- |
| detect KiCad windows | `READ_ONLY` | none | none | PowerShell/process discovery only. |
| detect exact Eeschema path | `READ_ONLY` | none | none | Must run before GUI control. |
| detect unsaved `*` state | `READ_ONLY` | none | none | Dirty GUI state is a separate truth source. |
| screenshot Eeschema | `DRY_RUN_FIRST` | `--capture` | no exact target window | Does not edit design files. |
| open exact KiCad project | `DRY_RUN_DEFAULT` | `--live` | wrong-project Eeschema open, ambiguous windows | Launch only the exact `.kicad_pro`. |
| open/focus schematic editor | `DRY_RUN_DEFAULT` | `--live` | wrong-project Eeschema open, ambiguous project-manager controls | Must confirm the exact `.kicad_sch` after open. |
| ensure Eeschema open | `DRY_RUN_DEFAULT` | `--live` | wrong-project Eeschema open, ambiguous windows, dirty `*` window unless explicitly allowed | Safe open-from-closed-state wrapper. |
| native annotation | `DRY_RUN_DEFAULT` | `--live --allow-annotation` | wrong project, no backup, dirty `*` window unless explicitly allowed | Authoritative annotation action. |
| GUI save | `DRY_RUN_DEFAULT` | `--live --allow-save` | no backup, no overwrite confirmation, wrong project | Must save from KiCad GUI after annotation. |
| GUI ERC | `DRY_RUN_DEFAULT` | `--live --allow-gui-erc` | wrong project, dirty `*` window before save | Use after GUI save in the full workflow. |
| full native annotation workflow | `DRY_RUN_DEFAULT` | `--live --allow-annotation --allow-save --allow-gui-erc` | any safety-gate failure | Includes screenshots, backup, GUI ERC, CLI ERC, and saved-schematic scans. |
| PCB update/layout/routing/zones | `PROHIBITED` | N/A | always | Not allowed in this layer. |
| manufacturing output | `PROHIBITED` | N/A | always | Not allowed in this layer. |
