#!/usr/bin/env python3
"""Build site-data.js for the local navigator (index.html).

Stdlib only. Run from anywhere:
    python3 scripts/build-index.py
    uv run scripts/build-index.py

Scans allaccess/** and the two course-material folders, embeds the text of
.md/.txt files and records metadata for binaries (html, pdf, pptx, images).
Writes window.SITE_DATA = {...}; to <repo>/site-data.js.
"""
from __future__ import annotations

import json
import mimetypes
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "site-data.js"

SKIP_DIRS = {".git", "node_modules", "vendor", "__pycache__", ".venv", ".idea", ".vscode"}
SKIP_FILES = {".DS_Store"}
TEXT_EXT = {".md", ".txt"}
TYPE_BY_EXT = {
    ".md": "markdown",
    ".txt": "text",
    ".html": "html",
    ".htm": "html",
    ".pdf": "pdf",
    ".pptx": "pptx",
    ".ppt": "pptx",
    ".docx": "docx",
    ".png": "image",
    ".jpg": "image",
    ".jpeg": "image",
    ".gif": "image",
    ".svg": "image",
    ".webp": "image",
    ".mp3": "audio",
    ".m4a": "audio",
    ".wav": "audio",
    ".mp4": "video",
    ".json": "data",
    ".csv": "data",
}
SIM_MARK = "სიმულაცია"
WORD_RE = re.compile(r"[\wႠ-ჿᲐ-Ჿ'-]+", re.UNICODE)
H1_RE = re.compile(r"^#\s+(.+?)\s*#*\s*$", re.MULTILINE)
HTML_TITLE_RE = re.compile(r"<title[^>]*>(.*?)</title>", re.IGNORECASE | re.DOTALL)

# Week 2 PSF sub-groups, in display order.
PSF_GROUPS = [
    ("passport", "პასპორტი და სინთეზი"),
    ("interviews", "ინტერვიუები"),
    ("comic", "კომიქსი"),
    ("prototype", "პროტოტიპი"),
    ("poster", "პოსტერი"),
    ("tests", "ტესტები"),
    ("final", "საბოლოო PSF"),
    ("other", "სხვა"),
]
PSF_ORDER = {k: i for i, (k, _) in enumerate(PSF_GROUPS)}

SECTIONS = [
    ("overview", "მიმოხილვა"),
    ("week1", "კვირა 1: პრობლემა"),
    ("week2-psf", "კვირა 2: Problem-Solution Fit"),
    ("week3", "კვირა 3: Customer Discovery"),
    ("materials", "კურსის მასალები"),
    ("sources", "წყაროები (ტექსტური ამონაწერი)"),
]
SECTION_ORDER = {k: i for i, (k, _) in enumerate(SECTIONS)}


def scan_roots() -> list[Path]:
    roots = []
    aa = ROOT / "allaccess"
    if aa.is_dir():
        roots.append(aa)
    for pattern in ("პრეზენტაციები-*", "დავალებები *"):
        roots.extend(sorted(p for p in ROOT.glob(pattern) if p.is_dir()))
    return roots


def walk(root: Path):
    for p in sorted(root.rglob("*")):
        rel_parts = p.relative_to(ROOT).parts
        if any(part in SKIP_DIRS for part in rel_parts):
            continue
        if p.is_file() and p.name not in SKIP_FILES and not p.name.endswith((".tmp", "~")):
            yield p


def classify(rel: str) -> tuple[str, str | None]:
    parts = rel.split("/")
    if parts[0] != "allaccess":
        return "materials", None
    sub = parts[1] if len(parts) > 2 else ""
    name = parts[-1].lower()
    if sub == "_sources":
        return "sources", None
    if sub == "week1":
        return "week1", None
    if sub == "week3":
        return "week3", None
    if sub == "week2-psf" or name.startswith("allaccess_psf"):
        low = rel.lower()
        if name.startswith("allaccess_psf"):
            g = "final"
        elif "/tests/" in low or name.startswith("test") or "-test" in name or "_test" in name:
            g = "tests"
        elif "/interviews/" in low:
            g = "interviews"
        elif "/comic/" in low:
            g = "comic"
        elif "/prototype/" in low:
            g = "prototype"
        elif "/poster/" in low:
            g = "poster"
        elif len(parts) == 3:
            g = "passport"
        else:
            g = "other"
        return "week2-psf", g
    if len(parts) == 2:
        return "overview", None
    return "overview", None


def derive_title(path: Path, ftype: str, content: str | None) -> str:
    if content is not None and ftype == "markdown":
        m = H1_RE.search(content)
        if m:
            return m.group(1).strip()
    if ftype == "html":
        try:
            head = path.read_text(encoding="utf-8", errors="replace")[:20000]
            m = HTML_TITLE_RE.search(head)
            if m:
                t = re.sub(r"\s+", " ", m.group(1)).strip()
                if t:
                    return t
        except OSError:
            pass
    return path.stem.strip() or path.name


SIM_PATH_RE = re.compile(
    r"^allaccess/week2-psf/(interviews/0[^/]*\.md$|tests/|synthesis\.md$|comic/)"
)


def is_simulated(rel: str, section: str, content: str | None) -> bool:
    """Simulated work: known simulated locations, or a banner in the first 15 lines."""
    if section in ("sources", "materials") or rel == "allaccess/BRIEF.md":
        return False
    if SIM_PATH_RE.search(rel):
        return True
    if content is not None:
        return SIM_MARK in "\n".join(content.split("\n")[:15])
    return False


def sort_key(item: dict) -> tuple:
    rel = item["path"]
    name = rel.rsplit("/", 1)[-1].lower()
    # Within a section: BRIEF/README first, then the document's natural path order.
    first = 0 if name in ("brief.md", "readme.md") else 1
    # Inside the interviews folder the roster comes after 01..06.
    roster = 1 if name.startswith("roster") else 0
    return (
        SECTION_ORDER.get(item["section"], 99),
        PSF_ORDER.get(item.get("group") or "", 0),
        first,
        rel.count("/"),
        roster,
        rel.lower(),
    )


def build() -> dict:
    items = []
    for root in scan_roots():
        for p in walk(root):
            rel = p.relative_to(ROOT).as_posix()
            ext = p.suffix.lower()
            ftype = TYPE_BY_EXT.get(ext, "other")
            st = p.stat()
            section, group = classify(rel)
            content = None
            if ext in TEXT_EXT:
                content = p.read_text(encoding="utf-8", errors="replace").replace("\r\n", "\n")
            simulated = is_simulated(rel, section, content)
            item = {
                "path": rel,
                "name": p.name,
                "ext": ext.lstrip("."),
                "type": ftype,
                "mime": mimetypes.guess_type(p.name)[0] or "application/octet-stream",
                "section": section,
                "group": group,
                "title": derive_title(p, ftype, content),
                "size": st.st_size,
                "mtime": datetime.fromtimestamp(st.st_mtime, timezone.utc).isoformat(timespec="seconds"),
                "simulated": simulated,
                "words": len(WORD_RE.findall(content)) if content is not None else 0,
            }
            if content is not None:
                item["content"] = content
            items.append(item)
    items.sort(key=sort_key)
    return {
        "builtAt": datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds"),
        "root": ROOT.name,
        "sections": [{"id": k, "label": v} for k, v in SECTIONS],
        "psfGroups": [{"id": k, "label": v} for k, v in PSF_GROUPS],
        "files": items,
    }


def main() -> int:
    data = build()
    payload = json.dumps(data, ensure_ascii=False, indent=1)
    # Guard against a literal "</script>" inside embedded content.
    payload = payload.replace("</", "<\\/")
    OUT.write_text(f"window.SITE_DATA = {payload};\n", encoding="utf-8")
    n_text = sum(1 for f in data["files"] if "content" in f)
    print(f"wrote {OUT.relative_to(ROOT)}: {len(data['files'])} files ({n_text} with text), built {data['builtAt']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
