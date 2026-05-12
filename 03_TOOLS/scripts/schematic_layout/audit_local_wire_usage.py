#!/usr/bin/env python3
"""Audit whether local functional blocks use wires instead of excessive labels."""

from __future__ import annotations

from pathlib import Path

from schematic_layout_common import (
    BLOCK_DEFINITIONS,
    CHECK_STATUS_FAIL,
    CHECK_STATUS_PASS,
    CHECK_STATUS_WARN,
    common_parser,
    load_layout_context,
    resolve_project_and_schematic,
    write_markdown_and_json,
)


def finding(status: str, code: str, message: str, evidence: str = "") -> dict[str, str]:
    return {"status": status, "code": code, "message": message, "evidence": evidence}


def run_audit(schematic: Path) -> dict:
    context = load_layout_context(schematic)
    findings: list[dict[str, str]] = []

    for block in BLOCK_DEFINITIONS:
        stats = context["block_stats"][block["id"]]
        if stats["symbol_count"] == 0:
            continue
        title = context["blocks"][block["id"]]["title"]
        repeated = ", ".join(f"{name} x{count}" for name, count in stats["repeated_labels"].items())
        evidence = f"{title}: wires={stats['wire_count']}, labels={stats['label_count']}, pin_labels={stats['pin_label_hits']}"

        if stats["wire_count"] == 0 and stats["label_count"] >= 3:
            findings.append(finding(CHECK_STATUS_FAIL, "LOCAL_BLOCK_HAS_LABELS_BUT_NO_WIRES", "Local block relies on labels without local wires.", evidence))
        elif stats["label_count"] >= stats["wire_count"] + 4 and stats["label_count"] >= 6:
            findings.append(finding(CHECK_STATUS_FAIL, "LOCAL_BLOCK_TOO_LABEL_HEAVY", "Local block uses too many labels instead of short local wires.", evidence))
        elif stats["pin_label_hits"] >= 4:
            findings.append(finding(CHECK_STATUS_WARN, "PIN_LABEL_OVERUSE", "Several labels sit directly at local pins where short wires would be clearer.", evidence))
        else:
            findings.append(finding(CHECK_STATUS_PASS, "LOCAL_WIRING_BALANCE_OK", "Local wiring balance is acceptable for this block.", evidence))

        if repeated:
            repeated_status = CHECK_STATUS_FAIL if len(stats["repeated_labels"]) >= 2 else CHECK_STATUS_WARN
            findings.append(
                finding(
                    repeated_status,
                    "REPEATED_LOCAL_NET_LABELS",
                    "Repeated local net labels suggest the block should use more internal wiring.",
                    f"{title}: {repeated}",
                )
            )

    pass_count = sum(1 for item in findings if item["status"] == CHECK_STATUS_PASS)
    warn_count = sum(1 for item in findings if item["status"] == CHECK_STATUS_WARN)
    fail_count = sum(1 for item in findings if item["status"] == CHECK_STATUS_FAIL)
    status = CHECK_STATUS_FAIL if fail_count else CHECK_STATUS_WARN if warn_count else CHECK_STATUS_PASS
    return {
        "generated_at": context["generated_at"],
        "schematic": context["schematic"],
        "audit_id": "local_wire_usage",
        "title": "Local Wire Usage Audit",
        "status": status,
        "counts": {"PASS": pass_count, "WARN": warn_count, "FAIL": fail_count},
        "findings": findings,
        "block_stats": context["block_stats"],
    }


def markdown(result: dict) -> str:
    lines = [
        "# Local Wire Usage Audit",
        "",
        f"Status: `{result['status']}`",
        "",
        f"Generated: `{result['generated_at']}`",
        f"Schematic: `{result['schematic']}`",
        "",
        "## Findings",
        "",
        "| Status | Code | Message | Evidence |",
        "| --- | --- | --- | --- |",
    ]
    for item in result["findings"]:
        lines.append(f"| `{item['status']}` | `{item['code']}` | {item['message'].replace('|', '\\|')} | `{item.get('evidence', '')}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = common_parser("Audit whether local blocks use wires instead of excessive labels.")
    args = parser.parse_args()
    _, schematic = resolve_project_and_schematic(args.project, args.schematic)
    result = run_audit(schematic)
    write_markdown_and_json(markdown(result), result, Path(args.output) if args.output else None, Path(args.json_output) if args.json_output else None)
    return 0 if args.no_fail or result["status"] != CHECK_STATUS_FAIL else 1


if __name__ == "__main__":
    raise SystemExit(main())
