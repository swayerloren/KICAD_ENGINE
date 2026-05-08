#!/usr/bin/env bash

echo "KiCad Engine xdotool window list"
echo "Safety: read-only listing only. No clicks, typing, hotkeys, window moves, or project modifications."
echo

if ! command -v xdotool >/dev/null 2>&1; then
  echo "WARN: xdotool not found"
  exit 0
fi

if [ -z "${DISPLAY:-}" ]; then
  echo "WARN: DISPLAY is not set. xdotool needs an X11 display."
  exit 0
fi

echo "DISPLAY=$DISPLAY"
echo

ids="$(xdotool search --onlyvisible --name '.*' 2>/dev/null || true)"
if [ -z "$ids" ]; then
  echo "INFO: no visible X11 windows found"
  exit 0
fi

for id in $ids; do
  title="$(xdotool getwindowname "$id" 2>/dev/null || echo UNKNOWN)"
  pid="$(xdotool getwindowpid "$id" 2>/dev/null || echo UNKNOWN)"
  geom="$(xdotool getwindowgeometry "$id" 2>/dev/null | tr '\n' ';' || echo UNKNOWN)"
  echo "WINDOW id=$id pid=$pid title=$title geometry=$geom"
done
