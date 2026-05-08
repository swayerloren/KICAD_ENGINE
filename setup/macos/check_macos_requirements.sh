#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
OUTPUT_DIR="$REPO_ROOT/05_OUTPUTS/setup_reports"
TIMESTAMP="$(date +"%Y%m%d_%H%M%S")"
REPORT_PATH="$OUTPUT_DIR/MACOS_REQUIREMENTS_CHECK_${TIMESTAMP}.md"
JSON_PATH="$OUTPUT_DIR/MACOS_REQUIREMENTS_CHECK_${TIMESTAMP}.json"

mkdir -p "$OUTPUT_DIR"

RESULTS=()
JSON_PYTHON=""
if command -v python3 >/dev/null 2>&1; then
  JSON_PYTHON="python3"
elif command -v python >/dev/null 2>&1; then
  JSON_PYTHON="python"
fi

add_result() {
  local status="$1"
  local name="$2"
  local detail="$3"
  RESULTS+=("$status|$name|$detail")
  printf '%-6s %s - %s\n' "$status" "$name" "$detail"
}

command_detail() {
  local command_name="$1"
  shift
  if command -v "$command_name" >/dev/null 2>&1; then
    local command_path
    command_path="$(command -v "$command_name")"
    local version_output
    version_output="$("$command_name" "$@" 2>&1 | head -n 1 || true)"
    add_result "PASS" "$command_name" "$command_path${version_output:+; $version_output}"
    return 0
  fi
  add_result "FAIL" "$command_name" "Not found on PATH."
  return 1
}

path_detail() {
  local label="$1"
  local candidate="$2"
  if [ -e "$candidate" ]; then
    add_result "PASS" "$label" "$candidate"
    return 0
  fi
  add_result "FAIL" "$label" "Missing: $candidate"
  return 1
}

executable_path_detail() {
  local label="$1"
  local candidate="$2"
  if [ -x "$candidate" ]; then
    local version_output
    version_output="$("$candidate" version 2>&1 | head -n 1 || true)"
    add_result "PASS" "$label" "$candidate${version_output:+; $version_output}"
    return 0
  fi
  add_result "FAIL" "$label" "Missing or not executable: $candidate"
  return 1
}

find_first_existing_path() {
  for candidate in "$@"; do
    if [ -e "$candidate" ]; then
      printf '%s\n' "$candidate"
      return 0
    fi
  done
  return 1
}

find_first_executable_path() {
  for candidate in "$@"; do
    if [ -x "$candidate" ]; then
      printf '%s\n' "$candidate"
      return 0
    fi
  done
  return 1
}

echo "KiCad Engine macOS requirements check"
echo "Repo root: $REPO_ROOT"
echo "This check is read-only. It does not install tools, collect credentials, or modify KiCad."
echo ""

KICAD_APP="/Applications/KiCad/KiCad.app"
KICAD_APP_ALT="/Applications/KiCad.app"
KICAD_BUNDLE_CLI="/Applications/KiCad/KiCad.app/Contents/MacOS/kicad-cli"
KICAD_BUNDLE_CLI_ALT="/Applications/KiCad.app/Contents/MacOS/kicad-cli"
VSCODE_APP="/Applications/Visual Studio Code.app"

if KICAD_APP_FOUND="$(find_first_existing_path "$KICAD_APP" "$KICAD_APP_ALT")"; then
  add_result "PASS" "KiCad app bundle" "$KICAD_APP_FOUND"
else
  add_result "FAIL" "KiCad app bundle" "Missing: $KICAD_APP or $KICAD_APP_ALT"
fi

if command -v kicad-cli >/dev/null 2>&1; then
  command_detail "kicad-cli" version || true
elif KICAD_CLI_FOUND="$(find_first_executable_path "$KICAD_BUNDLE_CLI" "$KICAD_BUNDLE_CLI_ALT")"; then
  executable_path_detail "kicad-cli app-bundle path" "$KICAD_CLI_FOUND" || true
else
  add_result "FAIL" "kicad-cli" "Missing from PATH and app-bundle paths."
fi

command_detail "git" --version || true

if command -v python3 >/dev/null 2>&1; then
  command_detail "python3" --version || true
elif command -v python >/dev/null 2>&1; then
  command_detail "python" --version || true
else
  add_result "FAIL" "Python" "Neither python3 nor python was found on PATH."
fi

command_detail "node" --version || true
command_detail "npm" --version || true

if command -v code >/dev/null 2>&1; then
  command_detail "code" --version || true
elif [ -e "$VSCODE_APP" ]; then
  add_result "PASS" "VS Code app bundle" "$VSCODE_APP"
else
  add_result "FAIL" "VS Code" "Missing from PATH and /Applications."
fi

if command -v brew >/dev/null 2>&1; then
  command_detail "brew" --version || true
else
  add_result "WARN" "Homebrew" "Not found. Manual installs remain supported."
fi

PASS_COUNT=0
WARN_COUNT=0
FAIL_COUNT=0
for entry in "${RESULTS[@]}"; do
  IFS='|' read -r status _name _detail <<< "$entry"
  case "$status" in
    PASS) PASS_COUNT=$((PASS_COUNT + 1)) ;;
    WARN) WARN_COUNT=$((WARN_COUNT + 1)) ;;
    FAIL) FAIL_COUNT=$((FAIL_COUNT + 1)) ;;
  esac
done

{
  echo "# macOS Requirements Check"
  echo ""
  echo "Generated: $(date -u +"%Y-%m-%dT%H:%M:%SZ")"
  echo "Repo root: \`$REPO_ROOT\`"
  echo ""
  echo "This report is read-only. It does not install tools, collect AI credentials, modify the KiCad app bundle, or write global KiCad libraries."
  echo ""
  echo "## Summary"
  echo ""
  echo "- PASS: $PASS_COUNT"
  echo "- WARN: $WARN_COUNT"
  echo "- FAIL: $FAIL_COUNT"
  echo ""
  echo "## Results"
  echo ""
  echo "| Status | Check | Detail |"
  echo "| --- | --- | --- |"
  for entry in "${RESULTS[@]}"; do
    IFS='|' read -r status name detail <<< "$entry"
    echo "| $status | $name | $detail |"
  done
  echo ""
  echo "## Manual Install References"
  echo ""
  echo "- KiCad: https://www.kicad.org/download/macos/"
  echo "- Git: https://git-scm.com/download/mac"
  echo "- Python: https://www.python.org/downloads/macos/"
  echo "- Node.js: https://nodejs.org/"
  echo "- VS Code: https://code.visualstudio.com/"
  echo "- Homebrew: https://brew.sh/"
} > "$REPORT_PATH"

if [ -n "$JSON_PYTHON" ]; then
  {
    echo "{"
    echo "  \"generated_utc\": \"$(date -u +"%Y-%m-%dT%H:%M:%SZ")\","
    echo "  \"repo_root\": $(printf '%s' "$REPO_ROOT" | "$JSON_PYTHON" -c 'import json,sys; print(json.dumps(sys.stdin.read()))'),"
    echo "  \"summary\": {\"PASS\": $PASS_COUNT, \"WARN\": $WARN_COUNT, \"FAIL\": $FAIL_COUNT},"
    echo "  \"results\": ["
    for index in "${!RESULTS[@]}"; do
      IFS='|' read -r status name detail <<< "${RESULTS[$index]}"
      comma=","
      if [ "$index" -eq "$((${#RESULTS[@]} - 1))" ]; then
        comma=""
      fi
      printf '    {"status": %s, "name": %s, "detail": %s}%s\n' \
        "$(printf '%s' "$status" | "$JSON_PYTHON" -c 'import json,sys; print(json.dumps(sys.stdin.read()))')" \
        "$(printf '%s' "$name" | "$JSON_PYTHON" -c 'import json,sys; print(json.dumps(sys.stdin.read()))')" \
        "$(printf '%s' "$detail" | "$JSON_PYTHON" -c 'import json,sys; print(json.dumps(sys.stdin.read()))')" \
        "$comma"
    done
    echo "  ]"
    echo "}"
  } > "$JSON_PATH"
else
  JSON_PATH="not written; Python is required for JSON escaping"
fi

echo ""
echo "Report: $REPORT_PATH"
echo "JSON: $JSON_PATH"

if [ "$FAIL_COUNT" -gt 0 ]; then
  exit 1
fi
