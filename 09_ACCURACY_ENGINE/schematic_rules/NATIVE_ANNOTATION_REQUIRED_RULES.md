# Native Annotation Required Rules

1. Saved-file scans are not native annotation proof by themselves.
2. Raw `.kicad_sch` text edits are not accepted as annotation proof.
3. Native KiCad annotation or LJ-confirmed manual native annotation is required
   before PCB update.
4. No visible `R?`, `C?`, `D?`, `U?`, `J?`, `TP?`, `SW?`, `MH?`, `#PWR?`, or
   `#FLG?` may remain.
5. If CLI/file scans and the open KiCad GUI disagree, the GUI state wins until
   saved and revalidated.
