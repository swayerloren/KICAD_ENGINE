# Failed Attempts

Session: `PCB_BATCH_04_CONTROL_NET_ROUTING`

Date: `2026-05-08`

## Attempt 1

- Action:
  - broad copied-board `/U0RXD` search without copying the matching `.kicad_pro`
- Failure:
  - false `drill_out_of_range` noise from detached board-rule defaults
- Fix:
  - reran copied-board trials with the matching project `.kicad_pro` beside each copied `.kicad_pcb`

## Attempt 2

- Action:
  - wide brute-force copied-board sweeps for `/U0RXD` and `/BOOT0`
- Failure:
  - long-running searches hit the shell timeout and had to be mined from partial results
- Fix:
  - narrowed the search windows around the first low-violation candidates and continued from saved trial folders

## Attempt 3

- Action:
  - focused copied-board searches for `/BOOT0` and `/ESP_EN`
- Failure:
  - no `0`-violation candidate found on the current board geometry
- Result:
  - nets deferred rather than forced onto the live board
