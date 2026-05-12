#!/usr/bin/env python3
"""Classify knowledge_scrape inventory rows into the migration ledger."""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from datetime import date
from pathlib import Path
from typing import Any


def rel(path: Path, root: Path) -> str:
    return str(path.relative_to(root)).replace("/", "\\")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Classify knowledge_scrape inventory into a migration ledger.")
    parser.add_argument("--repo-root", default=".", help="Repository root.")
    parser.add_argument("--source-root", default="knowledge_scrape", help="Source folder.")
    parser.add_argument("--inventory", required=True, help="Input inventory CSV.")
    parser.add_argument("--config", required=True, help="Migration config JSON.")
    parser.add_argument("--ledger", required=True, help="Output ledger CSV.")
    parser.add_argument("--destination-map", required=True, help="Output destination map Markdown.")
    parser.add_argument("--status", required=True, help="Output migration status Markdown.")
    return parser.parse_args()


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def load_url_index(path: Path) -> dict[str, dict[str, str]]:
    if not path.exists():
        return {}
    rows = load_csv(path)
    by_id: dict[str, dict[str, str]] = {}
    for row in rows:
        url_id = str(row.get("id", "")).strip().lower()
        if url_id:
            by_id[url_id] = row
    return by_id


def normalize_rule(rule: dict[str, Any]) -> dict[str, str]:
    return {
        "content_category": str(rule["content_category"]),
        "license_risk": str(rule["license_risk"]),
        "action": str(rule["action"]),
        "destination_root": str(rule["destination_root"]),
    }


def choose_rule(
    repo_relative: str,
    source_relative: str,
    filename: str,
    config: dict[str, Any],
) -> tuple[dict[str, str], str]:
    if "\\" not in source_relative and filename in config.get("root_file_rules", {}):
        return normalize_rule(config["root_file_rules"][filename]), "__ROOT__"

    for entry in sorted(config.get("path_prefix_rules", []), key=lambda item: len(str(item["prefix"])), reverse=True):
        prefix = str(entry["prefix"])
        if source_relative.startswith(prefix):
            return normalize_rule(entry), prefix

    return normalize_rule(config["default_rule"]), ""


def build_destination(source_relative: str, filename: str, rule: dict[str, str], matched_prefix: str) -> str:
    destination_root = Path(rule["destination_root"])
    if matched_prefix == "__ROOT__":
        return str(destination_root / filename).replace("/", "\\")
    if matched_prefix:
        tail = source_relative[len(matched_prefix):].lstrip("\\/")
        if tail:
            return str(destination_root / Path(tail)).replace("/", "\\")
        return str(destination_root / filename).replace("/", "\\")
    return str(destination_root / filename).replace("/", "\\")


def note_from_url_row(url_row: dict[str, str] | None) -> str:
    if not url_row:
        return ""
    parts = []
    for key in ("source_domain", "trust_label", "scrape_status", "knowledge_category", "source_type"):
        value = str(url_row.get(key, "")).strip()
        if value:
            parts.append(f"{key}={value}")
    return "; ".join(parts)


def build_ledger_rows(
    inventory_rows: list[dict[str, str]],
    config: dict[str, Any],
    url_index: dict[str, dict[str, str]],
    repo_root: Path,
    source_root_name: str,
) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    migration_date = date.today().isoformat()
    for item in inventory_rows:
        original_path = item["original_path"]
        source_relative = original_path.split(f"{source_root_name}\\", 1)[1] if f"{source_root_name}\\" in original_path else Path(original_path).name
        filename = Path(original_path).name
        rule, matched_prefix = choose_rule(original_path, source_relative, filename, config)
        canonical_destination = build_destination(source_relative, filename, rule, matched_prefix)
        url_id = item.get("url_index_id", "").lower()
        url_note = note_from_url_row(url_index.get(url_id))
        note_parts = []
        if matched_prefix and matched_prefix != "__ROOT__":
            note_parts.append(f"matched_prefix={matched_prefix}")
        if url_note:
            note_parts.append(url_note)
        row = {
            "original_path": original_path,
            "file_type": item["file_type"],
            "size_bytes": item["size_bytes"],
            "content_category": rule["content_category"],
            "license_risk": rule["license_risk"],
            "action": rule["action"],
            "canonical_destination": canonical_destination,
            "moved_yes_no": "NO",
            "migration_date": migration_date,
            "validation_status": "INVENTORIED_NOT_MOVED",
            "notes": " | ".join(note_parts),
        }
        rows.append(row)
    return sorted(rows, key=lambda row: row["original_path"].lower())


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def build_destination_map_markdown(config: dict[str, Any]) -> str:
    lines = [
        "# Knowledge Scrape Destination Map",
        "",
        "Status: `AUTO_GENERATED_MIGRATION_MAP`",
        "",
        "This map defines how `knowledge_scrape/` content should be drained into",
        "existing canonical KiCad Engine areas. It does not perform moves by",
        "itself.",
        "",
        "## Root File Rules",
        "",
        "| Source | Action | Destination Root | Category | License Risk |",
        "| --- | --- | --- | --- | --- |",
    ]
    for filename, rule in sorted(config.get("root_file_rules", {}).items()):
        lines.append(
            f"| `{filename}` | `{rule['action']}` | `{rule['destination_root']}` | "
            f"`{rule['content_category']}` | `{rule['license_risk']}` |"
        )

    lines.extend(
        [
            "",
            "## Path Prefix Rules",
            "",
            "| Source Prefix | Action | Destination Root | Category | License Risk |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for rule in sorted(config.get("path_prefix_rules", []), key=lambda item: str(item["prefix"]).lower()):
        lines.append(
            f"| `{rule['prefix']}` | `{rule['action']}` | `{rule['destination_root']}` | "
            f"`{rule['content_category']}` | `{rule['license_risk']}` |"
        )

    lines.extend(
        [
            "",
            "## Default",
            "",
            f"- Action: `{config['default_rule']['action']}`",
            f"- Destination root: `{config['default_rule']['destination_root']}`",
            f"- Category: `{config['default_rule']['content_category']}`",
            f"- License risk: `{config['default_rule']['license_risk']}`",
            "",
            "## Canonical Area Coverage",
            "",
            "- `00_CODEX_START`",
            "- `02_HISTORY`",
            "- `03_TOOLS`",
            "- `06_DATASHEETS`",
            "- `07_REFERENCE_DESIGNS`",
            "- `08_COMPONENT_DATABASE`",
            "- `09_ACCURACY_ENGINE`",
            "- `10_KNOWLEDGE_BASE`",
            "- `11_LIBRARY_FACTORY`",
            "- `12_REFERENCE_DESIGN_LIBRARY`",
            "- `14_LAYOUT_AUTOMATION`",
            "- `21_LICENSE_ATTRIBUTION`",
            "- `24_FAB_PROFILES`",
            "- `26_AGENT_QUALITY`",
            "",
            "Compliance note: because `31_COMPLIANCE_SAFETY_EMC` is not present in",
            "this repo, compliance/EMC/safety content is routed to",
            "`10_KNOWLEDGE_BASE\\compliance_emc_safety\\knowledge_scrape_import`.",
            "",
        ]
    )
    return "\n".join(lines)


def build_status_markdown(
    inventory_rows: list[dict[str, str]],
    ledger_rows: list[dict[str, str]],
    source_root: Path,
) -> str:
    action_counts = Counter(row["action"] for row in ledger_rows)
    license_counts = Counter(row["license_risk"] for row in ledger_rows)
    top_level_counts = Counter(row.get("top_level_folder", "__ROOT__") for row in inventory_rows)
    moved_count = sum(1 for row in ledger_rows if row["moved_yes_no"] == "YES")
    folder_paths = sorted({str(path.relative_to(source_root)).replace("/", "\\") for path in source_root.rglob("*") if path.is_dir()})

    lines = [
        "# Knowledge Scrape Migration Status",
        "",
        "Status: `CONTROLLER_CREATED_NO_SOURCE_MOVES_APPLIED`",
        "",
        f"- Inventory file count: `{len(inventory_rows)}`",
        f"- Ledger row count: `{len(ledger_rows)}`",
        f"- Source files moved: `{moved_count}`",
        f"- Inventory/ledger match: `{'YES' if len(inventory_rows) == len(ledger_rows) else 'NO'}`",
        f"- knowledge_scrape removable now: `{'YES' if len(inventory_rows) == 0 else 'NO'}`",
        "",
        "## Validation",
        "",
        "- The ledger includes every inventoried source file.",
        "- No source file is marked moved in the initial controller state.",
        "- Actual movement is still pending later migration prompts.",
        "",
        "## Action Counts",
        "",
        "| Action | Count |",
        "| --- | ---: |",
    ]
    for action, count in sorted(action_counts.items()):
        lines.append(f"| `{action}` | {count} |")

    lines.extend(["", "## License Risk Counts", "", "| License Risk | Count |", "| --- | ---: |"])
    for risk, count in sorted(license_counts.items()):
        lines.append(f"| `{risk}` | {count} |")

    lines.extend(["", "## Top-Level Folder Counts", "", "| Folder | Count |", "| --- | ---: |"])
    for folder, count in sorted(top_level_counts.items()):
        lines.append(f"| `{folder}` | {count} |")

    lines.extend(["", "## Folders Detected", ""])
    for folder in folder_paths:
        lines.append(f"- `{folder}`")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    repo_root = Path(args.repo_root).resolve()
    source_root = (repo_root / args.source_root).resolve()
    inventory_path = (repo_root / args.inventory).resolve()
    config_path = (repo_root / args.config).resolve()
    ledger_path = (repo_root / args.ledger).resolve()
    destination_map_path = (repo_root / args.destination_map).resolve()
    status_path = (repo_root / args.status).resolve()

    if not source_root.exists():
        raise SystemExit(f"SOURCE_ROOT_NOT_FOUND: {source_root}")

    inventory_rows = load_csv(inventory_path)
    config = json.loads(config_path.read_text(encoding="utf-8"))
    url_index = load_url_index(source_root / "URL_INDEX.csv")

    ledger_rows = build_ledger_rows(
        inventory_rows=inventory_rows,
        config=config,
        url_index=url_index,
        repo_root=repo_root,
        source_root_name=Path(args.source_root).name,
    )

    write_csv(ledger_path, list(config["ledger_columns"]), ledger_rows)
    destination_map_path.parent.mkdir(parents=True, exist_ok=True)
    destination_map_path.write_text(build_destination_map_markdown(config), encoding="utf-8")
    status_path.parent.mkdir(parents=True, exist_ok=True)
    status_path.write_text(build_status_markdown(inventory_rows, ledger_rows, source_root), encoding="utf-8")

    print(f"LEDGER_WRITTEN: {ledger_path}")
    print(f"DESTINATION_MAP_WRITTEN: {destination_map_path}")
    print(f"STATUS_WRITTEN: {status_path}")
    print(f"LEDGER_ROW_COUNT: {len(ledger_rows)}")
    print(f"MOVED_COUNT: {sum(1 for row in ledger_rows if row['moved_yes_no'] == 'YES')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
