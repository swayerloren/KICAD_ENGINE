# Claim / Evidence Matrix

Date: 2026-05-10

| Claim | Evidence |
| --- | --- |
| the repo now has a first-party optional-tool integration layer | `03_TOOLS/open_source_integrations/README.md` and companion files |
| install wrappers are dry-run by default | `setup/install_optional_kicad_tools_windows.ps1`, `setup/install_optional_kicad_tools_linux.sh`, `setup/install_optional_kicad_tools_macos.sh` |
| the verifier script parses and runs | `python -m py_compile setup\verify_optional_kicad_tools.py`; `python setup\verify_optional_kicad_tools.py --dry-run` |
| the Windows wrapper did not install anything during validation | `powershell -ExecutionPolicy Bypass -File setup\install_optional_kicad_tools_windows.ps1` output shows `Apply mode: False` and `DRY_RUN` steps |
| no KiCad design files changed | `git diff --name-only -- '*.kicad_sch' '*.kicad_pcb'` returned empty |
| no staged files or staged binaries were present | `git diff --cached --name-only` returned empty |
