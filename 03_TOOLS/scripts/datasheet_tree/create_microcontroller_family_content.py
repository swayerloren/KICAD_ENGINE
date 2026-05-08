#!/usr/bin/env python3
"""Create conservative AI-readable microcontroller family content stubs.

The generator is intentionally offline and non-destructive by default:
- no PDF downloads;
- no web scraping;
- no KiCad project edits;
- no overwrite of existing files unless --force is passed.
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any


UNKNOWN = "UNKNOWN_REQUIRES_SOURCE"

EVIDENCE_LABELS = """- `VERIFIED_SOURCE_LINK`: official/public source URL recorded.
- `VERIFIED_FROM_DATASHEET`: exact value checked in a named datasheet/reference document.
- `INFERRED_FROM_COMMON_DESIGN`: common design pattern; verify before use.
- `UNVERIFIED`: not checked against source evidence.
- `NEEDS_HUMAN_REVIEW`: must be reviewed before schematic, PCB, BOM, or fabrication use."""


TEMPLATE_OUTPUTS = {
    "{safe_family}_AI_OVERVIEW.md": "FAMILY_AI_OVERVIEW_TEMPLATE.md",
    "{safe_family}_COMMON_PART_NUMBERS.md": "COMMON_PART_NUMBERS_TEMPLATE.md",
    "{safe_part}_PART_RECORD.md": "PART_RECORD_TEMPLATE.md",
    "{safe_part}_SCHEMATIC_NOTES.md": "SCHEMATIC_NOTES_TEMPLATE.md",
    "{safe_part}_PCB_LAYOUT_NOTES.md": "PCB_LAYOUT_NOTES_TEMPLATE.md",
    "{safe_part}_BOOT_DEBUG_NOTES.md": "BOOT_DEBUG_NOTES_TEMPLATE.md",
    "{safe_part}_POWER_CLOCK_NOTES.md": "POWER_CLOCK_NOTES_TEMPLATE.md",
    "{safe_part}_PACKAGE_FOOTPRINT_NOTES.md": "PACKAGE_FOOTPRINT_NOTES_TEMPLATE.md",
    "{safe_part}_DEV_BOARD_NOTES.md": "DEV_BOARD_NOTES_TEMPLATE.md",
    "{safe_family}_COMMON_MISTAKES.md": "COMMON_MISTAKES_TEMPLATE.md",
    "{safe_family}_KICAD_SYMBOL_FOOTPRINT_NOTES.md": "KICAD_SYMBOL_FOOTPRINT_NOTES_TEMPLATE.md",
    "{safe_family}_SOURCE_LINKS.md": "SOURCE_LINKS_TEMPLATE.md",
    "{safe_family}_NEEDS_REVIEW.md": "NEEDS_REVIEW_TEMPLATE.md",
}


@dataclass(frozen=True)
class SourceLink:
    title: str
    url: str
    document_type: str = UNKNOWN
    verification_status: str = "VERIFIED_SOURCE_LINK"
    notes: str = "Link-only seed source. Review before use."


class SafeDict(dict[str, str]):
    def __missing__(self, key: str) -> str:
        return "{" + key + "}"


def safe_token(value: str) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9]+", "_", value.strip())
    cleaned = re.sub(r"_+", "_", cleaned).strip("_")
    return cleaned.upper() or UNKNOWN


def repo_root_from_script() -> Path:
    return Path(__file__).resolve().parents[3]


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"Config must be a JSON object: {path}")
    return data


def parse_source_link(raw: str) -> SourceLink:
    parts = [part.strip() for part in raw.split("|")]
    if len(parts) < 2:
        raise ValueError("--source-link must be formatted as title|url or title|url|document_type|status|notes")
    return SourceLink(
        title=parts[0],
        url=parts[1],
        document_type=parts[2] if len(parts) > 2 and parts[2] else UNKNOWN,
        verification_status=parts[3] if len(parts) > 3 and parts[3] else "VERIFIED_SOURCE_LINK",
        notes=parts[4] if len(parts) > 4 and parts[4] else "Link-only seed source. Review before use.",
    )


def source_links_from_config(config: dict[str, Any]) -> list[SourceLink]:
    links: list[SourceLink] = []
    for item in config.get("source_links", []) or []:
        if not isinstance(item, dict):
            raise ValueError("source_links entries must be JSON objects")
        links.append(
            SourceLink(
                title=str(item.get("title", UNKNOWN)),
                url=str(item.get("url", UNKNOWN)),
                document_type=str(item.get("document_type", UNKNOWN)),
                verification_status=str(item.get("verification_status", "VERIFIED_SOURCE_LINK")),
                notes=str(item.get("notes", "Link-only seed source. Review before use.")),
            )
        )
    return links


def source_link_rows(source_links: list[SourceLink]) -> str:
    if not source_links:
        return f"| `{UNKNOWN}` | `{UNKNOWN}` | `{UNKNOWN}` | `UNVERIFIED` | Add official/public source links. |"
    return "\n".join(
        "| {title} | {doc_type} | {url} | `{status}` | {notes} |".format(
            title=link.title,
            doc_type=link.document_type,
            url=link.url,
            status=link.verification_status,
            notes=link.notes,
        )
        for link in source_links
    )


def source_link_list(source_links: list[SourceLink]) -> str:
    if not source_links:
        return f"- `{UNKNOWN}`"
    return "\n".join(f"- {link.title}: {link.url}" for link in source_links)


def base_readme(context: dict[str, str]) -> str:
    return f"""# {context['family']}

Path: `{context['output_folder']}`

## Purpose

This folder stores source-link-first datasheet metadata, AI-readable design notes, part-level checklists, and KiCad symbol/footprint risk notes for `{context['family']}`.

## Current Status

Classification: `SCAFFOLDED_WITH_AI_SUMMARIES`

This folder is generated from conservative templates. It is useful for planning and review, but it is not a verified datasheet database.

## Evidence Labels

{context['evidence_labels']}

## Agent Rules

- Prefer official manufacturer sources and clearly recorded source URLs.
- Do not download PDFs or vendor documents from this generated scaffold.
- Do not fabricate exact specs.
- Do not approve symbols, footprints, pinouts, packages, or PCB decisions from this folder alone.
- Keep unknown fields marked `{UNKNOWN}`.
"""


def base_index(context: dict[str, str]) -> str:
    return f"""# {context['family']} Index

Date: {context['date']}

Generated AI-readable family index. Files are planning stubs until source-backed verification is complete.

| Topic | Local File | Status |
| --- | --- | --- |
| Family overview | `{context['safe_family']}_AI_OVERVIEW.md` | `SCAFFOLDED_WITH_AI_SUMMARIES` |
| Common part numbers | `{context['safe_family']}_COMMON_PART_NUMBERS.md` | `UNVERIFIED` |
| Representative part record | `{context['safe_part']}_PART_RECORD.md` | `UNVERIFIED_PLACEHOLDER` |
| Schematic notes | `{context['safe_part']}_SCHEMATIC_NOTES.md` | `NEEDS_HUMAN_REVIEW` |
| PCB layout notes | `{context['safe_part']}_PCB_LAYOUT_NOTES.md` | `NEEDS_HUMAN_REVIEW` |
| Boot/debug notes | `{context['safe_part']}_BOOT_DEBUG_NOTES.md` | `NEEDS_HUMAN_REVIEW` |
| Power/clock notes | `{context['safe_part']}_POWER_CLOCK_NOTES.md` | `NEEDS_HUMAN_REVIEW` |
| Package/footprint notes | `{context['safe_part']}_PACKAGE_FOOTPRINT_NOTES.md` | `NEEDS_HUMAN_REVIEW` |
| Dev-board notes | `{context['safe_part']}_DEV_BOARD_NOTES.md` | `LINK_FIRST_REFERENCE_NOTES` |
| Common mistakes | `{context['safe_family']}_COMMON_MISTAKES.md` | `AI_REVIEW_CHECKLIST` |
| KiCad candidate notes | `{context['safe_family']}_KICAD_SYMBOL_FOOTPRINT_NOTES.md` | `CANDIDATE_ONLY` |
| Source links | `{context['safe_family']}_SOURCE_LINKS.md` | `SOURCE_LINK_STUB` |
| Review backlog | `{context['safe_family']}_NEEDS_REVIEW.md` | `OPEN_REVIEW_BACKLOG` |
"""


def base_missing(context: dict[str, str]) -> str:
    return f"""# {context['family']} Missing Documents And Review Backlog

Date: {context['date']}

| Priority | Part / Topic | Needed Evidence | Reason Needed | Status |
| --- | --- | --- | --- | --- |
| High | `{context['representative_part']}` | official datasheet and product page | identity, electrical limits, pinout, package | `NEEDS_HUMAN_REVIEW` |
| High | `{context['representative_part']}` | reference manual or programming guide | boot/debug/clock/peripheral behavior | `NEEDS_HUMAN_REVIEW` |
| High | `{context['representative_part']}` | package drawing | footprint verification | `NEEDS_HUMAN_REVIEW` |
| Medium | `{context['family']}` | official errata | known limitations | `UNVERIFIED` |
| Medium | `{context['family']}` | official dev-board/reference design links | minimum system patterns | `UNVERIFIED` |
"""


def base_sources(context: dict[str, str]) -> str:
    return f"""# {context['family']} Sources

Date: {context['date']}

Record authoritative source locations before relying on any document. Link-only by default.

| Vendor / Publisher | Part / Topic | Document Type | Source URL | Verification Status | Notes |
| --- | --- | --- | --- | --- | --- |
{context['source_link_rows']}
"""


def build_context(args: argparse.Namespace, config: dict[str, Any], source_links: list[SourceLink]) -> dict[str, str]:
    vendor = args.vendor or config.get("vendor")
    family = args.family or config.get("family")
    representative_part = args.representative_part or config.get("representative_part")
    if not vendor or not family or not representative_part:
        raise ValueError("vendor, family, and representative_part are required")

    repo_root = Path(args.repo_root).resolve() if args.repo_root else repo_root_from_script()
    output_folder_value = args.output_folder or config.get("output_folder")
    if output_folder_value:
        output_folder = Path(output_folder_value)
        if not output_folder.is_absolute():
            output_folder = repo_root / output_folder
    else:
        output_folder = repo_root / "06_DATASHEETS" / "01_MICROCONTROLLERS" / str(vendor) / str(family)

    return {
        "vendor": str(vendor),
        "family": str(family),
        "representative_part": str(representative_part),
        "safe_vendor": safe_token(str(vendor)),
        "safe_family": safe_token(str(family)),
        "safe_part": safe_token(str(representative_part)),
        "date": args.date or date.today().isoformat(),
        "unknown": UNKNOWN,
        "evidence_labels": EVIDENCE_LABELS,
        "source_link_rows": source_link_rows(source_links),
        "source_link_list": source_link_list(source_links),
        "repo_root": str(repo_root),
        "output_folder": str(output_folder.relative_to(repo_root)) if output_folder.is_relative_to(repo_root) else str(output_folder),
        "output_folder_abs": str(output_folder),
    }


def render_template(template_path: Path, context: dict[str, str]) -> str:
    text = template_path.read_text(encoding="utf-8")
    return text.format_map(SafeDict(context)).rstrip() + "\n"


def target_name(pattern: str, context: dict[str, str]) -> str:
    return pattern.format_map(SafeDict(context))


def collect_outputs(script_dir: Path, context: dict[str, str]) -> dict[str, str]:
    templates_dir = script_dir / "templates"
    outputs = {
        "README.md": base_readme(context),
        "INDEX.md": base_index(context),
        "MISSING.md": base_missing(context),
        "SOURCES.md": base_sources(context),
    }
    for output_pattern, template_name in TEMPLATE_OUTPUTS.items():
        outputs[target_name(output_pattern, context)] = render_template(templates_dir / template_name, context)
    return outputs


def is_weak_placeholder(path: Path) -> bool:
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return False
    stripped = text.strip()
    if not stripped:
        return True
    lowered = stripped.lower()
    weak_markers = [
        "intentionally empty until documents are curated",
        "| todo | todo | todo | todo | todo | missing |",
        "add entries as documents are verified",
        "path: $rel",
        "for $name",
        "scaffolded for future curation",
    ]
    if any(marker in lowered for marker in weak_markers):
        return True
    if len(stripped.splitlines()) <= 12 and "todo" in lowered and "missing" in lowered:
        return True
    return False


def write_outputs(
    output_folder: Path,
    outputs: dict[str, str],
    force: bool,
    dry_run: bool,
    overwrite_weak: bool,
) -> list[dict[str, str]]:
    results: list[dict[str, str]] = []
    if not dry_run:
        output_folder.mkdir(parents=True, exist_ok=True)
    for name, content in sorted(outputs.items()):
        target = output_folder / name
        exists_before = target.exists()
        if exists_before and not force:
            if overwrite_weak and is_weak_placeholder(target):
                if dry_run:
                    results.append({"path": str(target), "status": "WOULD_OVERWRITE_WEAK_PLACEHOLDER"})
                    continue
                target.write_text(content, encoding="utf-8", newline="\n")
                results.append({"path": str(target), "status": "OVERWROTE_WEAK_PLACEHOLDER"})
                continue
            results.append({"path": str(target), "status": "SKIPPED_EXISTS"})
            continue
        if dry_run:
            results.append({"path": str(target), "status": "WOULD_WRITE" if not exists_before else "WOULD_OVERWRITE"})
            continue
        target.write_text(content, encoding="utf-8", newline="\n")
        results.append({"path": str(target), "status": "OVERWROTE" if exists_before else "WROTE"})
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description="Create safe microcontroller family content stubs.")
    parser.add_argument("--repo-root", default=None, help="Repository root. Defaults to auto-detected repo root.")
    parser.add_argument("--config", default=None, help="Optional JSON config matching family_content_schema.json.")
    parser.add_argument("--vendor", default=None, help="Vendor folder/name, e.g. STMICRO_STM32.")
    parser.add_argument("--family", default=None, help="Family name, e.g. STM32F4.")
    parser.add_argument("--representative-part", default=None, help="Representative part, e.g. STM32F401CCU6.")
    parser.add_argument("--output-folder", default=None, help="Optional explicit output folder.")
    parser.add_argument("--source-link", action="append", default=[], help="Seed source as title|url|document_type|status|notes.")
    parser.add_argument("--date", default=None, help="Override date, YYYY-MM-DD.")
    parser.add_argument("--force", action="store_true", help="Overwrite existing files.")
    parser.add_argument("--overwrite-weak", action="store_true", help="Overwrite only obvious placeholder boilerplate files.")
    parser.add_argument("--dry-run", action="store_true", help="Show planned writes without writing files.")
    parser.add_argument("--json", action="store_true", help="Print machine-readable summary.")
    args = parser.parse_args()

    config: dict[str, Any] = load_json(Path(args.config).resolve()) if args.config else {}
    links = source_links_from_config(config)
    links.extend(parse_source_link(raw) for raw in args.source_link)
    context = build_context(args, config, links)
    output_folder = Path(context["output_folder_abs"])
    outputs = collect_outputs(Path(__file__).resolve().parent, context)
    results = write_outputs(output_folder, outputs, args.force, args.dry_run, args.overwrite_weak)

    summary = {
        "output_folder": str(output_folder),
        "file_count": len(results),
        "wrote": sum(1 for item in results if item["status"] in {"WROTE", "OVERWROTE", "OVERWROTE_WEAK_PLACEHOLDER"}),
        "skipped": sum(1 for item in results if item["status"] == "SKIPPED_EXISTS"),
        "dry_run": args.dry_run,
        "results": results,
    }
    if args.json:
        print(json.dumps(summary, indent=2))
    else:
        print(f"Output folder: {summary['output_folder']}")
        print(f"Files considered: {summary['file_count']}")
        print(f"Wrote/overwrote: {summary['wrote']}")
        print(f"Skipped existing: {summary['skipped']}")
        if args.dry_run:
            print("Dry run only; no files written.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
