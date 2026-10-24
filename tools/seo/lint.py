#!/usr/bin/env python3
"""Check every guide in _guides/ against STYLE.md. Exit 1 on any problem.

  python tools/seo/lint.py            # all guides
  python tools/seo/lint.py _guides/find-duplicate-photos.md
"""
from __future__ import annotations

import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
GUIDES = os.path.join(ROOT, "_guides")
REQUIRED = ("title", "description", "date", "query", "slug", "related")
BANNED = {"—": "em-dash", "–": "en-dash", "!": "exclamation mark"}
MARKETING = re.compile(r"\b(seamless(ly)?|powerful|effortless(ly)?|revolutionary|cutting-edge|game-?changer)\b", re.I)


def check(path: str, slugs: set[str]) -> list[str]:
    errs: list[str] = []
    text = open(path, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        return ["no front matter"]
    fm_text, body = m.group(1), m.group(2)
    fm = {}
    for line in fm_text.splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip()
    for k in REQUIRED:
        if not fm.get(k):
            errs.append(f"front matter missing {k}")
    name = os.path.splitext(os.path.basename(path))[0]
    if fm.get("slug") and fm["slug"] != name:
        errs.append(f"slug {fm['slug']} != file name {name}")
    if fm.get("title") and not 30 <= len(fm["title"].strip('"')) <= 70:
        errs.append(f"title length {len(fm['title'])} (want 30-70)")
    if fm.get("description") and not 90 <= len(fm["description"].strip('"')) <= 170:
        errs.append(f"description length {len(fm['description'])} (want 90-170)")
    for slug in re.findall(r"[a-z0-9-]+", fm.get("related", "")):
        if slug not in slugs:
            errs.append(f"related slug {slug} does not exist")
    img = fm.get("image", "")
    if img and not os.path.exists(os.path.join(ROOT, img.lstrip("/"))):
        errs.append(f"image {img} not found")
    prose = re.sub(r"!\[.*?\]\(.*?\)", "", body)
    for ch, what in BANNED.items():
        n = prose.count(ch)
        if n:
            errs.append(f"{n} {what}(s)")
    if re.search(r"[\U0001F300-\U0001FAFF☀-➿]", body):
        errs.append("emoji")
    if re.search(r"^# ", body, re.M):
        errs.append("H1 in body (the layout prints the title)")
    for w in MARKETING.findall(body):
        errs.append(f"marketing word: {w if isinstance(w, str) else w[0]}")
    for link in re.findall(r"\]\((/guides/([a-z0-9-]+)/)\)", body):
        if link[1] not in slugs:
            errs.append(f"link to missing guide {link[0]}")
    words = len(re.findall(r"\b\w+\b", prose))
    if not 450 <= words <= 1000:
        errs.append(f"{words} words (want 500-900)")
    if "## In PixOrg" not in body and "## " not in body:
        errs.append("no H2 sections")
    return errs


def main() -> int:
    paths = sys.argv[1:] or sorted(glob.glob(os.path.join(GUIDES, "*.md")))
    slugs = {os.path.splitext(os.path.basename(p))[0] for p in glob.glob(os.path.join(GUIDES, "*.md"))}
    bad = 0
    for p in paths:
        errs = check(p, slugs)
        rel = os.path.relpath(p, ROOT)
        if errs:
            bad += 1
            print(f"{rel}:")
            for e in errs:
                print(f"  - {e}")
        else:
            print(f"{rel}: ok")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
