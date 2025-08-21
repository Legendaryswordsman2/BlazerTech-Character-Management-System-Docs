#!/usr/bin/env python3
"""
DocFX TOC builder/updater

- Scans ./docs for .md files and mirrors folder structure in docs/toc.yml
- If toc.yml exists, it:
  * keeps existing entry order
  * preserves *existing names* as long as their href still points to a real file
  * removes entries whose relative .md href no longer exists
  * adds missing files (without duplicating existing hrefs)
  * does NOT change names you manually edited

Notes
- Only relative .md hrefs are validated against the docs folder. External/absolute links are left alone.
- New entries get a formatted name (dashes/underscores -> spaces, Title Case).
- Existing entries with the same href are never renamed.
"""
from __future__ import annotations

import os
from pathlib import Path, PurePosixPath
from typing import Any, Dict, List, Optional, Set, Tuple

try:
    import yaml  # PyYAML
except Exception as e:  # pragma: no cover
    raise SystemExit("This script requires PyYAML. Install with: pip install pyyaml")

DOCS_DIR = Path(__file__).parent / "docs"
TOC_PATH = DOCS_DIR / "toc.yml"

# ---------------------------- helpers ----------------------------

def to_posix_rel(path: Path, base: Path) -> str:
    return str(PurePosixPath(path.relative_to(base).as_posix()))


def normalize_href_for_fs(href: str) -> Optional[str]:
    """Return a normalized href suitable for joining with DOCS_DIR, or None if external/absolute.
    - strips URL fragments ("#...")
    - strips leading "./"
    - keeps case (GitHub Pages is case-sensitive)
    - only returns for relative .md paths
    """
    if not isinstance(href, str):
        return None
    href = href.strip()
    if not href:
        return None

    # external or absolute links are ignored for validation
    lowered = href.lower()
    if lowered.startswith("http://") or lowered.startswith("https://") or lowered.startswith("mailto:") or href.startswith("/"):
        return None

    # strip fragment
    if "#" in href:
        href = href.split("#", 1)[0].strip()

    # keep only markdown files
    if not href.endswith(".md"):
        return None

    while href.startswith("./"):
        href = href[2:]

    # Use POSIX-style separators for comparison
    return str(PurePosixPath(href))


def format_name_from_filename(filename: str) -> str:
    name = Path(filename).stem
    return name.replace("-", " ").replace("_", " ").title()


def list_markdown_files(base: Path) -> List[Path]:
    return sorted(p for p in base.rglob("*.md") if p.is_file())


def load_existing_toc(path: Path) -> List[Dict[str, Any]]:
    if not path.exists():
        return []
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not data:
        return []
    if not isinstance(data, list):
        raise SystemExit("toc.yml must be a YAML list at the top level.")
    return data


def dump_toc(path: Path, toc: List[Dict[str, Any]]) -> None:
    text = yaml.dump(
        toc,
        sort_keys=False,
        allow_unicode=True,
        width=120,
    )
    path.write_text(text, encoding="utf-8")


# ------------------------- TOC operations ------------------------

def collect_all_hrefs(toc: List[Dict[str, Any]]) -> Set[str]:
    out: Set[str] = set()
    for entry in toc:
        href = entry.get("href")
        if isinstance(href, str):
            norm = normalize_href_for_fs(href)
            if norm:
                out.add(norm)
        if isinstance(entry.get("items"), list):
            out.update(collect_all_hrefs(entry["items"]))
    return out


def prune_invalid_hrefs_inplace(toc: List[Dict[str, Any]], docs_dir: Path) -> None:
    i = 0
    while i < len(toc):
        entry = toc[i]
        href = entry.get("href")
        items = entry.get("items")

        removed = False
        if isinstance(href, str):
            norm = normalize_href_for_fs(href)
            if norm:  # only validate relative .md paths
                if not (docs_dir / norm).exists():
                    # remove entry whose target no longer exists
                    toc.pop(i)
                    removed = True
        if not removed and isinstance(items, list):
            prune_invalid_hrefs_inplace(items, docs_dir)
            # if items became empty, keep the header (non-clickable) as-is
        if not removed:
            i += 1


def ensure_folder_chain(entries: List[Dict[str, Any]], dir_parts: List[str], current_path: str = "") -> List[Dict[str, Any]]:
    """Find or create (append) a nested folder chain based on dir_parts.
    We try to reuse an existing folder entry by looking for one whose subtree already
    contains files with the matching path prefix. If not found, we create a new header
    using a formatted name for that directory.
    Returns the innermost entries list (the items of the deepest folder).
    """
    if not dir_parts:
        return entries

    target_dir = "/".join([p for p in [current_path, dir_parts[0]] if p])

    # 1) Prefer an entry whose subtree already contains files under target_dir/
    for e in entries:
        items = e.get("items")
        if not isinstance(items, list):
            continue
        if subtree_has_prefix(items, target_dir + "/"):
            return ensure_folder_chain(items, dir_parts[1:], target_dir)

    # 2) Fall back to a name match (useful when subtree is empty but header already exists)
    for e in entries:
        items = e.get("items")
        if not isinstance(items, list):
            continue
        if isinstance(e.get("name"), str) and e["name"].strip().lower() == format_name_from_filename(dir_parts[0]).lower():
            return ensure_folder_chain(items, dir_parts[1:], target_dir)

    # 3) Create new header
    new_header = {"name": format_name_from_filename(dir_parts[0]), "items": []}
    entries.append(new_header)
    return ensure_folder_chain(new_header["items"], dir_parts[1:], target_dir)


def subtree_has_prefix(entries: List[Dict[str, Any]], prefix: str) -> bool:
    for e in entries:
        href = e.get("href")
        if isinstance(href, str):
            norm = normalize_href_for_fs(href)
            if norm and norm.startswith(prefix):
                return True
        items = e.get("items")
        if isinstance(items, list) and subtree_has_prefix(items, prefix):
            return True
    return False


def href_exists_anywhere(toc: List[Dict[str, Any]], target_norm: str) -> bool:
    for e in toc:
        href = e.get("href")
        if isinstance(href, str):
            norm = normalize_href_for_fs(href)
            if norm == target_norm:
                return True
        items = e.get("items")
        if isinstance(items, list) and href_exists_anywhere(items, target_norm):
            return True
    return False


def add_missing_files(toc: List[Dict[str, Any]], docs_dir: Path) -> None:
    all_md = list_markdown_files(docs_dir)
    for md in all_md:
        rel = to_posix_rel(md, docs_dir)  # e.g., "guide/intro.md"
        if href_exists_anywhere(toc, rel):
            continue  # already present somewhere; keep existing name & position

        # Determine folder chain for this file
        parts = rel.split("/")
        dirs, filename = parts[:-1], parts[-1]
        container = ensure_folder_chain(toc, dirs)

        # Append new entry with formatted name
        container.append({
            "name": format_name_from_filename(filename),
            "href": rel,
        })


# ---------------------------- main -------------------------------

def main() -> None:
    if not DOCS_DIR.exists():
        raise SystemExit(f"Docs folder not found: {DOCS_DIR}")

    toc = load_existing_toc(TOC_PATH)

    # 1) Remove entries whose relative .md href no longer exists
    prune_invalid_hrefs_inplace(toc, DOCS_DIR)

    # 2) Add any missing files without touching existing names/order
    add_missing_files(toc, DOCS_DIR)

    # 3) Write back
    dump_toc(TOC_PATH, toc)

    # Summary
    total = len(collect_all_hrefs(toc))
    print(f"Updated {TOC_PATH} with {total} markdown entries.")


if __name__ == "__main__":
    main()
