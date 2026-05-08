from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path
from typing import Any


SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from parse_unrouted_and_vias import build_metrics  # noqa: E402


def common_parent(paths: list[Path]) -> Path:
    return Path(os.path.commonpath([str(path.resolve()) for path in paths]))


def container_relpath(base: Path, target: Path) -> str:
    return target.resolve().relative_to(base.resolve()).as_posix()


def detect_runtime(mode: str, docker_executable: str, java_executable: str, freerouting_jar: Path | None) -> tuple[str, list[str], str]:
    if mode in {"auto", "docker"} and shutil.which(docker_executable):
        return "docker", [], "Docker runtime detected."
    if mode in {"auto", "jar"} and freerouting_jar is not None and freerouting_jar.exists() and shutil.which(java_executable):
        return "jar", [], "Java plus FreeRouting JAR detected."

    reasons: list[str] = []
    if mode in {"auto", "docker"} and not shutil.which(docker_executable):
        reasons.append(f"{docker_executable} not found")
    if mode in {"auto", "jar"}:
        if freerouting_jar is None:
            reasons.append("freerouting jar path not provided")
        elif not freerouting_jar.exists():
            reasons.append(f"freerouting jar missing: {freerouting_jar}")
        if not shutil.which(java_executable):
            reasons.append(f"{java_executable} not found")
    return "unavailable", reasons, "No supported FreeRouting runtime detected."


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run FreeRouting as a dry-run routing-feasibility probe.")
    parser.add_argument("--dsn", type=Path, required=True, help="Specctra DSN input path.")
    parser.add_argument("--output-dir", type=Path, required=True, help="Output directory for review artifacts.")
    parser.add_argument("--mode", choices=["auto", "docker", "jar"], default="auto")
    parser.add_argument("--freerouting-jar", type=Path, help="Path to freerouting.jar.")
    parser.add_argument("--docker-image", default="freerouting/freerouting:latest")
    parser.add_argument("--docker-executable", default="docker")
    parser.add_argument("--java-executable", default="java")
    parser.add_argument("--max-passes", type=int, default=20)
    parser.add_argument("--threads", type=int, default=4)
    parser.add_argument("--timeout-sec", type=int, default=300)
    parser.add_argument("--variant-id", help="Optional variant identifier.")
    parser.add_argument("--project", help="Optional project name.")
    parser.add_argument("--ignore-net", action="append", default=[], help="Optional net to ignore.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    dsn_path = args.dsn.resolve()
    if not dsn_path.exists():
        raise SystemExit(f"DSN input not found: {dsn_path}")

    output_dir = args.output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    ses_path = output_dir / f"{dsn_path.stem}.ses"
    stdout_path = output_dir / "freerouting.stdout.log"
    stderr_path = output_dir / "freerouting.stderr.log"
    manifest_path = output_dir / "run_manifest.json"

    runtime, runtime_reasons, runtime_note = detect_runtime(
        mode=args.mode,
        docker_executable=args.docker_executable,
        java_executable=args.java_executable,
        freerouting_jar=args.freerouting_jar,
    )

    manifest: dict[str, Any] = {
        "tool": "run_freerouting_dry_run",
        "project": args.project,
        "variant_id": args.variant_id,
        "review_status": "REVIEW_ONLY",
        "run_status": "UNAVAILABLE" if runtime == "unavailable" else "READY",
        "runtime_mode": runtime,
        "runtime_note": runtime_note,
        "runtime_reasons": runtime_reasons,
        "dsn_path": str(dsn_path),
        "ses_path": str(ses_path),
        "stdout_log": str(stdout_path),
        "stderr_log": str(stderr_path),
        "command": [],
        "high_risk_review_required": ["USB", "RF", "SWITCHING_REGULATOR", "HIGH_CURRENT"],
        "notes": [
            "FreeRouting output is review-only.",
            "Do not treat this dry run as final routing approval.",
            "Do not auto-approve USB, RF, switching, or high-current nets from this result.",
        ],
    }

    if runtime == "unavailable":
        manifest["metrics"] = build_metrics(dsn_text=dsn_path.read_text(encoding="utf-8", errors="ignore"))
        manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
        print(json.dumps(manifest, indent=2))
        return 0

    if runtime == "docker":
        mount_root = common_parent([dsn_path, output_dir])
        command = [
            args.docker_executable,
            "run",
            "--rm",
            "-v",
            f"{mount_root}:/work",
            "-w",
            "/work",
            args.docker_image,
            "-de",
            container_relpath(mount_root, dsn_path),
            "-do",
            container_relpath(mount_root, ses_path),
            "-mp",
            str(args.max_passes),
            "-mt",
            str(args.threads),
            f"--router.max_passes={args.max_passes}",
        ]
    else:
        command = [
            args.java_executable,
            "-jar",
            str(args.freerouting_jar.resolve()),
            "-de",
            str(dsn_path),
            "-do",
            str(ses_path),
            "-mp",
            str(args.max_passes),
            "-mt",
            str(args.threads),
            f"--router.max_passes={args.max_passes}",
        ]

    for ignored_net in args.ignore_net:
        command.extend(["-inc", ignored_net])

    manifest["command"] = command
    start = time.perf_counter()
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=args.timeout_sec,
            check=False,
        )
        manifest["run_status"] = "COMPLETED" if result.returncode == 0 else "ERROR"
        manifest["return_code"] = result.returncode
        stdout_text = result.stdout
        stderr_text = result.stderr
    except subprocess.TimeoutExpired as exc:
        manifest["run_status"] = "TIMEOUT"
        manifest["return_code"] = None
        stdout_text = exc.stdout or ""
        stderr_text = exc.stderr or ""
        stderr_text += f"\nTimed out after {args.timeout_sec} seconds."
    elapsed = round(time.perf_counter() - start, 3)
    manifest["wall_seconds"] = elapsed

    stdout_path.write_text(stdout_text, encoding="utf-8")
    stderr_path.write_text(stderr_text, encoding="utf-8")

    dsn_text = dsn_path.read_text(encoding="utf-8", errors="ignore")
    ses_text = ses_path.read_text(encoding="utf-8", errors="ignore") if ses_path.exists() else ""
    manifest["metrics"] = build_metrics(
        log_text="\n".join([stdout_text, stderr_text]),
        dsn_text=dsn_text,
        ses_text=ses_text,
    )
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(manifest, indent=2))
    return 0 if manifest["run_status"] in {"COMPLETED", "UNAVAILABLE"} else 1


if __name__ == "__main__":
    raise SystemExit(main())
