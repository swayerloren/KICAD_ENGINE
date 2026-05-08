# Prompt Counter Rule Upgrade Commands

Status: `ACTIVE_EVIDENCE`

Generated date/time: `2026-05-07T12:45:00-04:00`

Project: `KICAD_ENGINE`

Supersedes: `None`

Superseded by: `None`

Evidence files: command outputs from the prompt-counter rule upgrade.

Current relevance: command log for prompt-counter scripts and validation.

## Commands

```powershell
python -m py_compile 03_TOOLS\scripts\memory_maintenance\increment_prompt_counter.py 03_TOOLS\scripts\memory_maintenance\check_maintenance_due.py 03_TOOLS\scripts\memory_maintenance\reset_prompt_counter_after_maintenance.py
```

Result: `PASS`

```powershell
python 03_TOOLS\scripts\memory_maintenance\increment_prompt_counter.py --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE --reason "validation dry run"
```

Result:

```text
DRY_RUN: ...\PROMPT_COUNTER.md 1 -> 2
MAINTENANCE_DUE: NO
```

```powershell
python 03_TOOLS\scripts\memory_maintenance\check_maintenance_due.py --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE
```

Result:

```text
PROMPT_COUNT: 1
MAINTENANCE_THRESHOLD: 5
MAINTENANCE_DUE: NO
RESULT: MAINTENANCE_NOT_DUE
```

```powershell
python 03_TOOLS\scripts\memory_maintenance\reset_prompt_counter_after_maintenance.py --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE
```

Result:

```text
DRY_RUN: would reset ...\PROMPT_COUNTER.md to 0
MAINTENANCE_DUE: NO
```

```powershell
python 03_TOOLS\scripts\memory_maintenance\rebuild_memory_indexes.py --repo-root . --apply
python 03_TOOLS\scripts\memory_maintenance\rebuild_history_indexes.py --repo-root . --apply
python 03_TOOLS\scripts\indexing\build_known_problems.py --repo-root .
```

Result: indexes rebuilt.

## KiCad Design File Confirmation

Observed after validation:

- `ESP32_CSI_WIFI_NODE.kicad_sch`: `2026-05-07 10:39:37`
- `ESP32_CSI_WIFI_NODE.kicad_pcb`: `2026-05-07 12:30:31`
- `ESP32_CSI_WIFI_NODE.kicad_pro`: `2026-05-07 10:45:13`

No KiCad design-file edit commands were run.
