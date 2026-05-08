"""Read-only helpers for KiCad library intelligence scripts."""

from __future__ import annotations

import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


UNKNOWN = "Unknown - requires source verification"


def repo_root() -> Path:
    current = Path(__file__).resolve()
    for parent in current.parents:
        if (parent / "AGENTS.md").exists():
            return parent
    return Path.cwd()


def default_output_dir() -> Path:
    return repo_root() / "03_TOOLS" / "kicad_library_intelligence" / "GENERATED_INDEXES"


def detect_kicad_root(explicit_root: str | None = None, version_preference: str = "9.0") -> Path | None:
    candidates: list[Path] = []
    if explicit_root:
        candidates.append(Path(explicit_root))
    for key in ("KICAD_ROOT", "KICAD9_ROOT"):
        value = os.environ.get(key)
        if value:
            candidates.append(Path(value))

    if os.name == "nt":
        candidates.append(Path(r"C:\Program Files\KiCad") / version_preference)
        install_root = Path(r"C:\Program Files\KiCad")
        if install_root.exists():
            version_dirs = [p for p in install_root.iterdir() if p.is_dir() and (p / "share" / "kicad").exists()]
            version_dirs.sort(key=lambda p: p.name, reverse=True)
            candidates.extend(version_dirs)
    else:
        candidates.extend([Path("/usr/share/kicad"), Path("/usr/local/share/kicad")])

    for candidate in candidates:
        if (candidate / "share" / "kicad").exists():
            return candidate.resolve()
        if (candidate / "symbols").exists() and (candidate / "footprints").exists():
            return candidate.resolve()
    return None


def kicad_share_root(kicad_root: Path) -> Path:
    share = kicad_root / "share" / "kicad"
    if share.exists():
        return share
    return kicad_root


def user_config_roots(version_preference: str = "9.0") -> list[Path]:
    roots: list[Path] = []
    appdata = os.environ.get("APPDATA")
    localappdata = os.environ.get("LOCALAPPDATA")
    home = Path.home()
    if appdata:
        roots.append(Path(appdata) / "kicad" / version_preference)
    if localappdata:
        roots.append(Path(localappdata) / "kicad" / version_preference)
    roots.append(home / "AppData" / "Roaming" / "kicad" / version_preference)
    roots.append(home / "AppData" / "Local" / "kicad" / version_preference)
    roots.append(home / ".config" / "kicad" / version_preference)
    seen: set[str] = set()
    existing: list[Path] = []
    for root in roots:
        key = str(root).lower()
        if key not in seen and root.exists():
            seen.add(key)
            existing.append(root.resolve())
    return existing


def is_relative_to(path: Path, base: Path) -> bool:
    try:
        path.resolve().relative_to(base.resolve())
        return True
    except ValueError:
        return False


def ensure_safe_output_dir(output_dir: Path, kicad_root: Path | None, version_preference: str = "9.0") -> Path:
    output_dir = output_dir.resolve()
    if kicad_root and is_relative_to(output_dir, kicad_root):
        raise SystemExit(f"Refusing to write generated outputs inside KiCad install root: {output_dir}")
    for root in user_config_roots(version_preference):
        if is_relative_to(output_dir, root):
            raise SystemExit(f"Refusing to write generated outputs inside KiCad user config root: {output_dir}")
    output_dir.mkdir(parents=True, exist_ok=True)
    return output_dir


def utc_stamp() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def write_markdown(path: Path, lines: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def slugify(value: str) -> str:
    slug = re.sub(r"[^A-Za-z0-9]+", "_", value.strip().lower()).strip("_")
    return slug or "query"


def normalize_tokens(value: str) -> list[str]:
    lowered = value.lower()
    value = lowered.replace("usb-c", "usb c").replace("type-c", "type c").replace("u.fl", "ufl")
    raw = re.split(r"[^a-z0-9]+", value)
    tokens = [t for t in raw if len(t) > 1 and t not in {"generic", "connector", "module", "part"}]
    extras: list[str] = []
    if "usb-c" in lowered or "usb c" in lowered or "type-c" in lowered or "type c" in lowered:
        extras.extend(["usbc", "typec"])
    for token in tokens:
        if len(token) > 4:
            extras.append(token.replace("_", ""))
        if token.startswith("mcp") and token.endswith("fd") and len(token) > 5:
            extras.append(token[:-2])
        if token.startswith("stm32") and len(token) > 9:
            extras.append(token[:-1])
            extras.append(token[:-2])
            extras.append(token[:9])
    return list(dict.fromkeys(tokens + extras))


def score_text(query: str, text: str) -> tuple[int, list[str]]:
    tokens = normalize_tokens(query)
    haystack = text.lower().replace("-", " ").replace("_", " ")
    compact = re.sub(r"[^a-z0-9]+", "", text.lower())
    matched: list[str] = []
    score = 0
    for token in tokens:
        if token in haystack:
            matched.append(token)
            score += 10 + min(len(token), 8)
        elif token in compact:
            matched.append(token)
            score += 8 + min(len(token), 8)
    query_compact = re.sub(r"[^a-z0-9]+", "", query.lower())
    if query.lower().replace("-", "_") in text.lower():
        score += 25
    if query_compact and query_compact in compact:
        score += 35
    return score, matched


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def parse_lib_table(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    text = read_text(path)
    entries: list[dict[str, str]] = []
    pattern = re.compile(r"\(lib\s+\(name\s+\"?([^\"\s\)]+)\"?\).*?\(uri\s+\"?([^\"\)]+)\"?\)", re.S)
    for match in pattern.finditer(text):
        entries.append({"table_path": str(path), "name": match.group(1), "uri": match.group(2)})
    return entries


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def fail(message: str, code: int = 2) -> None:
    print(message, file=sys.stderr)
    raise SystemExit(code)
