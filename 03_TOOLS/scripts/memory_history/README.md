# Memory And History Scripts

Read-only with respect to KiCad design files. These scripts create markdown records and generated indexes for the KiCad Engine learning loop.

## Safety Rules

- Do not write `.kicad_sch`, `.kicad_pcb`, `.kicad_pro`, symbol libraries, footprint libraries, or manufacturing outputs.
- Do not delete existing history.
- Create timestamped records.
- Mark generated records `UNVERIFIED` unless the caller provides a stronger status.
- Refuse obvious secret-looking content.

## Scripts

- `create_session_log.py`
- `create_failed_attempt.py`
- `create_user_correction.py`
- `create_issue_log.py`
- `create_lesson_learned.py`
- `update_project_memory_stub.py`
- `update_global_memory_stub.py`
- `closeout_session.py`
- `build_memory_index.py`
- `build_history_index.py`

## Examples

Global session log:

```powershell
python 03_TOOLS/scripts/memory_history/create_session_log.py --repo-root . --title "Repo audit session" --summary "Created release audit records."
```

Project correction:

```powershell
python 03_TOOLS/scripts/memory_history/create_user_correction.py --repo-root . --scope project --project-name ESP32_CSI_WIFI_NODE --project-path 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --title "USB-C connector footprint correction" --summary "User reported the selected connector footprint was wrong."
```

Build generated indexes:

```powershell
python 03_TOOLS/scripts/memory_history/build_memory_index.py --repo-root .
python 03_TOOLS/scripts/memory_history/build_history_index.py --repo-root .
```

