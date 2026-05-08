# Memory History Maintenance Upgrade Commands

Status: `ACTIVE_EVIDENCE`

Generated date/time: `2026-05-07T12:38:30-04:00`

Project: `KICAD_ENGINE`

Supersedes: `None`

Superseded by: `None`

Evidence files: command outputs observed during this session.

Current relevance: command log for maintenance-system upgrade.

## Commands

```powershell
python -m py_compile 03_TOOLS\scripts\memory_maintenance\*.py
```

Result: passed.

```powershell
python 03_TOOLS\scripts\memory_maintenance\run_memory_maintenance.py --repo-root . --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE
```

Result: dry-run succeeded. It would write eight project memory/history maintenance files.

```powershell
python 03_TOOLS\scripts\memory_maintenance\run_memory_maintenance.py --repo-root . --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE --apply --json-output 05_OUTPUTS\release_readiness\memory_maintenance_apply_result.json
```

Result: apply succeeded. It wrote markdown maintenance files only.

```powershell
python 03_TOOLS\scripts\memory_maintenance\rebuild_memory_indexes.py --repo-root . --apply
python 03_TOOLS\scripts\memory_maintenance\rebuild_history_indexes.py --repo-root . --apply
```

Result: memory and history indexes rebuilt.

```powershell
python 03_TOOLS\scripts\memory_maintenance\detect_duplicate_history.py --repo-root . --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE
```

Result: duplicate blocker topics detected for routing, PCB update, no-PCB, footprint, JLCPCB, NOT_FINAL, placement, Q1, visual-pass, schematic-gate, and PCB-sync records.

```powershell
python 03_TOOLS\scripts\memory_maintenance\normalize_relative_dates.py --repo-root . --project 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE
```

Result: `419` relative-date hits detected for human review.

```powershell
git status --short
```

Result: failed because this checkout did not report as a Git repository.

## KiCad Design File Safety

No command in this session edited `.kicad_sch`, `.kicad_pcb`, `.kicad_pro`, Gerber, drill, BOM, CPL, STEP, or routing data.
