# Failed Attempt - ESP32_CSI_WIFI_NODE Phase 2 PowerShell Heredoc Failed

Date: `2026-05-07`

## Command Pattern

```powershell
python - <<'PY'
```

## Result

PowerShell rejected the POSIX heredoc syntax.

## Resolution

Used PowerShell here-strings piped into Python:

```powershell
@'
...
'@ | python -
```

