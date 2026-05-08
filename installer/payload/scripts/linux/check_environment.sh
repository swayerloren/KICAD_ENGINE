#!/usr/bin/env bash
set -euo pipefail

echo "KiCad Engine Linux packaged-payload environment check"
echo "Read-only. No installs are performed."

if [ -r /etc/os-release ]; then
  # shellcheck disable=SC1091
  . /etc/os-release
  echo "Distribution: ${PRETTY_NAME:-${ID:-unknown}}"
fi

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

check_command kicad --version
check_command kicad-cli version
check_command git --version
check_command python3 --version
check_command node --version
check_command npm --version
check_command code --version

for manager in apt-get dnf yum pacman flatpak snap; do
  check_command "$manager" --version
done
