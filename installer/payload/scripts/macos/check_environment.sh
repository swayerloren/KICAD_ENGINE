#!/usr/bin/env bash
set -euo pipefail

echo "KiCad Engine macOS packaged-payload environment check"
echo "Read-only. No installs are performed."

check_command() {
  local tool="$1"
  shift || true
  if command -v "$tool" >/dev/null 2>&1; then
    local version=""
    if [ "$#" -gt 0 ]; then
      version="$("$tool" "$@" 2>&1 | head -n 1 || true)"
    fi
    echo "FOUND $tool $(command -v "$tool")${version:+; $version}"
  else
    echo "MISSING $tool"
  fi
}

check_path() {
  local label="$1"
  local candidate="$2"
  if [ -e "$candidate" ]; then
    echo "FOUND $label $candidate"
  else
    echo "MISSING $label $candidate"
  fi
}

check_command kicad-cli version
check_path "KiCad app bundle" "/Applications/KiCad/KiCad.app"
check_path "KiCad app-bundle CLI" "/Applications/KiCad/KiCad.app/Contents/MacOS/kicad-cli"
check_command git --version
check_command python3 --version
check_command node --version
check_command npm --version
check_command code --version
check_path "VS Code app bundle" "/Applications/Visual Studio Code.app"
check_command brew --version
