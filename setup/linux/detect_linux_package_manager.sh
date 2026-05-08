#!/usr/bin/env bash
set -euo pipefail

BEST_ONLY="false"
if [ "${1:-}" = "--best-id" ]; then
  BEST_ONLY="true"
fi

FOUND=()

detect() {
  local id="$1"
  local command_name="$2"
  if command -v "$command_name" >/dev/null 2>&1; then
    FOUND+=("$id|$command_name|$(command -v "$command_name")")
  fi
}

detect apt apt-get
detect dnf dnf
detect yum yum
detect pacman pacman
detect flatpak flatpak
detect snap snap

if [ "${#FOUND[@]}" -eq 0 ]; then
  exit 1
fi

if [ "$BEST_ONLY" = "true" ]; then
  IFS='|' read -r id _command _path <<< "${FOUND[0]}"
  printf '%s\n' "$id"
  exit 0
fi

if [ -r /etc/os-release ]; then
  # shellcheck disable=SC1091
  . /etc/os-release
  echo "Distribution: ${PRETTY_NAME:-${ID:-unknown}}"
fi

echo "Detected package managers:"
for entry in "${FOUND[@]}"; do
  IFS='|' read -r id command_name path_value <<< "$entry"
  echo "- $id ($command_name): $path_value"
done
