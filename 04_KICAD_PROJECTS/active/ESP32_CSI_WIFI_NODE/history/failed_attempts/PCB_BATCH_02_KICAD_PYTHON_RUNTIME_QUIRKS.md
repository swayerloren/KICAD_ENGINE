# PCB Batch 02 KiCad Python Runtime Quirks

Date: `2026-05-08`

Status: `FAILED_ATTEMPTS_CAPTURED`

## Failed Attempt 1

- Attempt: use plain `python` to run `03_TOOLS\scripts\pcb_routing\esp32_csi_power_batch_02_reroute.py`
- Failure:
  - `ModuleNotFoundError: No module named 'pcbnew'`
- Resolution:
  - switched to `C:\Program Files\KiCad\9.0\bin\python.exe`

## Failed Attempt 2

- Attempt: collect via drill/diameter values in the standalone KiCad Python summary path
- Failure:
  - runtime hung while querying via drill data in the SWIG wrapper
- Resolution:
  - removed via drill/diameter inspection from the reusable batch-02 summary script

## Failed Attempt 3

- Attempt: call `GetTracks()` repeatedly after removals inside the reusable apply helper
- Failure:
  - standalone KiCad Python intermittently raised `TypeError: 'SwigPyObject' object is not iterable`
- Resolution:
  - switched the actual rehearsal/live apply path to a single-pass inline KiCad Python sequence with explicit progress flushes

## Failed Attempt 4

- Attempt: over-straighten `/+5V_IN` and flatten `/+5V_PROTECTED`
- Failure:
  - copied-board DRC exposed real `J1` GND and `C2` GND clearance failures
- Resolution:
  - preserved those clearance-constrained geometries and only applied the DRC-clean local power-feed cleanup
