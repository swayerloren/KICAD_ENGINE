#!/usr/bin/env bash

echo "KiCad Engine wmctrl window list"
echo "Safety: read-only listing only. No clicks, typing, hotkeys, window moves, or project modifications."
echo

if ! command -v wmctrl >/dev/null 2>&1; then
  echo "WARN: wmctrl not found"
  exit 0
fi

if [ -z "${DISPLAY:-}" ]; then
  echo "WARN: DISPLAY is not set. wmctrl needs an X11 display."
  exit 0
fi

echo "DISPLAY=$DISPLAY"
echo

if ! wmctrl -l -p -G 2>/dev/null; then
  echo "WARN: wmctrl could not list windows"
fi
