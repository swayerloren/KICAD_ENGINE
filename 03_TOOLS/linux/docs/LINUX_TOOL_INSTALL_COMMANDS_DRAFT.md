# Linux Tool Install Commands Draft

This file lists draft Linux install commands for future reference only.

Do not run these commands from Windows. Do not run them until LJ explicitly approves Linux or WSL setup. Package names vary by distribution and version.

## Ubuntu/Debian Draft Commands

Update package metadata:

```bash
sudo apt update
```

Install X11 window inspection/control helpers:

```bash
sudo apt install xdotool wmctrl
```

Install lower-level input helper if appropriate:

```bash
sudo apt install ydotool
```

Install accessibility automation tooling:

```bash
sudo apt install dogtail
```

Install virtual display and remote X diagnostic tooling:

```bash
sudo apt install xvfb x11vnc
```

Install Python GUI support:

```bash
sudo apt install python3-tk
```

Install screenshot helpers:

```bash
sudo apt install scrot
sudo apt install gnome-screenshot
```

Install KiCad:

```bash
sudo apt install kicad
```

Install KiBot if available from package manager:

```bash
sudo apt install kibot
```

Alternative KiBot install approach for a future dedicated Linux venv:

```bash
python3 -m venv ~/kicad-engine-kibot-venv
~/kicad-engine-kibot-venv/bin/python -m pip install --upgrade pip
~/kicad-engine-kibot-venv/bin/python -m pip install kibot
```

## Fedora Draft Package Names

```bash
sudo dnf install xdotool wmctrl ydotool dogtail xorg-x11-server-Xvfb x11vnc python3-tkinter scrot kicad
```

## Arch Draft Package Names

```bash
sudo pacman -S xdotool wmctrl ydotool dogtail xorg-server-xvfb x11vnc tk scrot kicad
```

## Safety Notes

- These are documentation examples only.
- Do not install tools on a production workstation without checking versions and package sources.
- Do not run GUI automation against real projects first.
- Do not mark generated outputs final without the full KiCad Engine verification gate.
