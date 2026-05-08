#!/usr/bin/env bash

echo "KiCad Engine Linux environment check"
echo "Safety: read-only checks only. No installs, privileged commands, deletes, or project modifications."
echo

check_command() {
  name="$1"
  if command -v "$name" >/dev/null 2>&1; then
    path="$(command -v "$name")"
    echo "PASS: $name found at $path"
    return 0
  fi
  echo "WARN: $name not found"
  return 1
}

try_version() {
  label="$1"
  shift
  output="$("$@" 2>&1)"
  status="$?"
  if [ "$status" -eq 0 ]; then
    echo "INFO: $label version output:"
    printf '%s\n' "$output" | sed 's/^/  /'
  else
    echo "WARN: $label version command failed or produced no usable output"
    printf '%s\n' "$output" | sed 's/^/  /'
  fi
}

echo "System"
uname -a 2>/dev/null || echo "WARN: uname failed"
if command -v lsb_release >/dev/null 2>&1; then
  lsb_release -a 2>/dev/null
elif [ -r /etc/os-release ]; then
  cat /etc/os-release
else
  echo "WARN: no distribution metadata found"
fi
echo

echo "Display"
echo "DISPLAY=${DISPLAY:-NOT_SET}"
echo "WAYLAND_DISPLAY=${WAYLAND_DISPLAY:-NOT_SET}"
echo "XDG_SESSION_TYPE=${XDG_SESSION_TYPE:-NOT_SET}"
echo

echo "Core commands"
check_command kicad
check_command kicad-cli
check_command python3
check_command pip3
check_command git
check_command node
check_command npm
echo

echo "Linux GUI/headless helpers"
check_command xdotool
check_command wmctrl
check_command ydotool
check_command dogtail
check_command Xvfb
check_command xvfb-run
check_command x11vnc
check_command scrot
check_command gnome-screenshot
echo

if command -v kicad-cli >/dev/null 2>&1; then
  try_version "kicad-cli" kicad-cli version
fi
if command -v python3 >/dev/null 2>&1; then
  try_version "python3" python3 --version
fi
if command -v git >/dev/null 2>&1; then
  try_version "git" git --version
fi

echo
echo "Result: environment check complete. Missing tools are warnings, not installs."
