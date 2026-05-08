# Failed Attempt - New-Item LiteralPath For PCB Visual Directory

Date: `2026-05-06 22:15:29 -04:00`

Command:

```powershell
New-Item -ItemType Directory -Force -LiteralPath 'C:\Users\LJ\GitHub\KICAD_ENGINE\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\pcb_visual'
```

Result:

```text
New-Item : A parameter cannot be found that matches parameter name 'LiteralPath'.
```

Impact:

No KiCad design files were edited. The directory creation was retried successfully with `-Path`.

Resolution:

Use `New-Item -ItemType Directory -Force -Path <path>` for this environment.
