#!/usr/bin/env bash

echo "KiCad Engine Xvfb/headless readiness check"
echo "Safety: read-only checks only. No installs, privileged commands, deletes, project edits, or fabrication outputs."
echo

missing=0

if ! command -v Xvfb >/dev/null 2>&1; then
  echo "WARN: Xvfb not found"
  missing=1
else
  echo "PASS: Xvfb found at $(command -v Xvfb)"
fi

if command -v xvfb-run >/dev/null 2>&1; then
  echo "PASS: xvfb-run found at $(command -v xvfb-run)"
else
  echo "WARN: xvfb-run not found"
fi

if ! command -v kicad-cli >/dev/null 2>&1; then
  echo "WARN: kicad-cli not found"
  missing=1
else
  echo "PASS: kicad-cli found at $(command -v kicad-cli)"
  echo "INFO: kicad-cli version:"
  kicad-cli version 2>/dev/null || echo "WARN: kicad-cli version failed"
fi

echo
echo "DISPLAY=${DISPLAY:-NOT_SET}"
echo "WAYLAND_DISPLAY=${WAYLAND_DISPLAY:-NOT_SET}"
echo

if [ "$missing" -ne 0 ]; then
  echo "Result: partial readiness. Missing tools must be installed in a Linux environment before headless GUI checks."
else
  echo "Result: basic headless prerequisites found. Run only on disposable samples until validated."
fi
