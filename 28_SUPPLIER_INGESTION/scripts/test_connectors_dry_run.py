#!/usr/bin/env python3
"""Dry-run smoke test helper for supplier connector stubs.

This script is intentionally offline. It runs each connector without --live,
checks that JSON is emitted, and verifies the safety flags that matter for
public-release use. It is not executed by the connector modules themselves.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
CONNECTORS = {
    "digikey": REPO_ROOT / "connectors" / "digikey" / "digikey_connector.py",
    "mouser": REPO_ROOT / "connectors" / "mouser" / "mouser_connector.py",
    "jlcpcb": REPO_ROOT / "connectors" / "jlcpcb" / "jlcpcb_connector.py",
    "lcsc": REPO_ROOT / "connectors" / "lcsc" / "lcsc_connector.py",
}


def run_connector(name: str, script: Path, query: str) -> dict:
    command = [sys.executable, str(script), "--query", query]
    completed = subprocess.run(command, check=False, capture_output=True, text=True)
    if completed.returncode != 0:
        raise RuntimeError(f"{name} dry-run failed with exit code {completed.returncode}: {completed.stderr.strip()}")
    try:
        payload = json.loads(completed.stdout)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"{name} did not emit valid JSON") from exc
    if payload.get("mode") != "DRY_RUN":
        raise RuntimeError(f"{name} did not report DRY_RUN mode")
    if payload.get("live_call_made") is not False:
        raise RuntimeError(f"{name} reported live_call_made not false")
    if payload.get("pdfs_downloaded") is not False:
        raise RuntimeError(f"{name} reported pdfs_downloaded not false")
    return payload


def write_report(path: Path, results: dict[str, dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write("# Supplier Connector Dry-Run Test Report\n\n")
        handle.write("Status: `DRY_RUN_ONLY`\n\n")
        for name, payload in results.items():
            handle.write(f"## {name}\n\n")
            handle.write(f"- Mode: `{payload.get('mode')}`\n")
            handle.write(f"- Live call made: `{payload.get('live_call_made')}`\n")
            handle.write(f"- PDFs downloaded: `{payload.get('pdfs_downloaded')}`\n")
            handle.write(f"- Records emitted: `{len(payload.get('records', []))}`\n\n")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run offline dry-run tests for supplier connector stubs.")
    parser.add_argument("--query", default="EXAMPLE_ONLY_PART", help="Example query used for dry-run output.")
    parser.add_argument(
        "--report",
        type=Path,
        default=REPO_ROOT / "reports" / "connector_dry_run" / "DRY_RUN_TEST_REPORT.md",
        help="Optional markdown report path.",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    results: dict[str, dict] = {}
    for name, script in CONNECTORS.items():
        if not script.exists():
            raise FileNotFoundError(f"Missing connector script: {script}")
        results[name] = run_connector(name, script, args.query)
    write_report(args.report, results)
    print(f"DRY_RUN connector tests passed. Report: {args.report}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
