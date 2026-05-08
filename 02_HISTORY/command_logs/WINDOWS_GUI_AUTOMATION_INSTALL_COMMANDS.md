# Windows GUI Automation Install Commands

Date: 2026-04-30

## Scope

Created and tested the isolated Windows GUI automation Python environment:

`C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\windows_gui`

No KiCad GUI control was attempted. No KiCad project files were modified. No Linux tools were installed. No repos were moved. MCP permissions were not changed.

## Commands And Results

### 1. Initial venv command using `python`

Command:

```powershell
python -m venv "C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\windows_gui"
```

Result:

```text
FAILED. The term 'python' is not recognized as the name of a cmdlet, function, script file, or operable program.
```

Resolution: used the Windows Python launcher instead. PATH was not modified.

### 2. Create venv using Python launcher

Command:

```powershell
py -3.12 -m venv "C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\windows_gui"
```

Result:

```text
Exit code 0. Venv created.
```

### 3. Check venv Python

Command:

```powershell
& "C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\windows_gui\Scripts\python.exe" --version
```

Output:

```text
Python 3.12.10
```

### 4. Check venv pip

Command:

```powershell
& "C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\windows_gui\Scripts\python.exe" -m pip --version
```

Output:

```text
pip 25.0.1 from C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\windows_gui\Lib\site-packages\pip (python 3.12)
```

### 5. Install requested packages

Command:

```powershell
& "C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\windows_gui\Scripts\python.exe" -m pip install pywinauto pyautogui pygetwindow pyperclip pillow opencv-python psutil
```

Output summary:

```text
Successfully installed comtypes-1.4.16 mouseinfo-0.1.3 numpy-2.4.4 opencv-python-4.13.0.92 pillow-12.2.0 psutil-7.2.2 pyautogui-0.9.54 pygetwindow-0.0.9 pymsgbox-2.0.1 pyperclip-1.11.0 pyrect-0.2.0 pyscreeze-1.0.1 pytweening-1.2.0 pywin32-311 pywinauto-0.6.9 six-1.17.0
```

Note: pip reported a newer pip release was available. pip was not upgraded because this task only installed the requested GUI automation packages.

### 6. Import-only check

Command:

```powershell
@'
import importlib
from importlib import metadata
modules = [
    ('pywinauto', 'pywinauto'),
    ('pyautogui', 'PyAutoGUI'),
    ('pygetwindow', 'PyGetWindow'),
    ('pyperclip', 'pyperclip'),
    ('PIL', 'pillow'),
    ('cv2', 'opencv-python'),
    ('psutil', 'psutil'),
]
for module_name, package_name in modules:
    module = importlib.import_module(module_name)
    version = metadata.version(package_name)
    print(f'IMPORT_OK {module_name} {version}')
print('SAFE_IMPORT_CHECK_COMPLETE')
'@ | & "C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\windows_gui\Scripts\python.exe" -
```

Output:

```text
IMPORT_OK pywinauto 0.6.9
IMPORT_OK pyautogui 0.9.54
IMPORT_OK pygetwindow 0.0.9
IMPORT_OK pyperclip 1.11.0
IMPORT_OK PIL 12.2.0
IMPORT_OK cv2 4.13.0.92
IMPORT_OK psutil 7.2.2
SAFE_IMPORT_CHECK_COMPLETE
```

### 7. Freeze package list

Command:

```powershell
& "C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\windows_gui\Scripts\python.exe" -m pip freeze
```

Output:

```text
comtypes==1.4.16
MouseInfo==0.1.3
numpy==2.4.4
opencv-python==4.13.0.92
pillow==12.2.0
psutil==7.2.2
PyAutoGUI==0.9.54
PyGetWindow==0.0.9
PyMsgBox==2.0.1
pyperclip==1.11.0
PyRect==0.2.0
PyScreeze==1.0.1
pytweening==1.2.0
pywin32==311
pywinauto==0.6.9
six==1.17.0
```

### 8. Syntax-check passive scripts

Commands:

```powershell
& "C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\windows_gui\Scripts\python.exe" -m py_compile "C:\Users\LJ\KICAD_ENGINE\03_TOOLS\windows\scripts\window_discovery\discover_windows.py"
& "C:\Users\LJ\KICAD_ENGINE\03_TOOLS\python_envs\windows_gui\Scripts\python.exe" -m py_compile "C:\Users\LJ\KICAD_ENGINE\03_TOOLS\windows\scripts\screenshots\take_screenshot.py"
```

Result:

```text
Exit code 0 for both syntax checks.
```
