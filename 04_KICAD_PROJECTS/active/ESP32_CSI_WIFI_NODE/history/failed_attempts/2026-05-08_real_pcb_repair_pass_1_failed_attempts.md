# Real PCB Repair Pass 1 Failed Attempts

Date: `2026-05-08`

## Failures

| Attempt | Outcome | Resolution |
| --- | --- | --- |
| Initial `kicad-cli pcb export svg` without board-fit options | Produced page-sized review SVG/PNG instead of board-fitted evidence | Re-ran export with `--mode-single --page-size-mode 2 --exclude-drawing-sheet` before generating the final review packet |
| One native net-summary inspection command | Timed out while dumping too much per-track detail | Fell back to the existing trace-audit report plus live-state extraction for routing inventory evidence |
