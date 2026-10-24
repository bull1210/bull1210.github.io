#!/usr/bin/env python3
"""Find search queries this site is shown for but does not answer well.

Reads Google Search Console exports (Performance > Export > Download CSV) dropped into data/gsc/.
Each export is a zip or folder with Queries.csv (Top queries, Clicks, Impressions, CTR, Position).
The newest file wins per query. Standard library only.

  python tools/seo/gaps.py                  # ranked gaps as Markdown
  python tools/seo/gaps.py --check "find duplicate photos android"
  python tools/seo/gaps.py --min-impressions 10 --json

A gap: impressions >= --min-impressions, position worse than --position (or CTR < 2 %), and no guide whose
query/title/keywords cover at least --cover of the query's content words.
"""
from __future__ import annotations

import argparse
import csv
import glob
import io
import json
import os
import re
import sys
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
GUIDES = os.path.join(ROOT, "_guides")
DATA = os.path.join(ROOT, "data", "gsc")
# Words that say nothing about which guide answers a query: grammar, the platform, and the nouns every
# guide shares (photo, gallery, find). What is left is the topic: "duplicate", "receipt", "vault".
STOP = set(
    "a an the to on in of for and or with my your how do i can is it at from by what why when way ways "
    "without best free app apps android phone phones mobile samsung get use using make "
    "photo photos picture pictures pic pics image images gallery camera find finding search searching "
    "all one my".split()
)
BRAND = {"pixorg", "pixorgs", "pix", "org"}


def stem(w: str) -> str:
    for suffix in ("ies", "ing", "es", "s"):
        if w.endswith(suffix) and len(w) - len(suffix) >= 3:
            return w[: -len(suffix)] + ("y" if suffix == "ies" else "")
    return w


def words(s: str) -> set[str]:
    return {stem(w) for w in re.findall(r"[a-z0-9]+", s.lower()) if w not in STOP and len(w) > 1}


def front_matter(path: str) -> dict:
    with open(path, encoding="utf-8") as f:
        text = f.read()
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    fm: dict = {}
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                fm[k.strip()] = v.strip().strip('"').strip("'")
    fm["_body"] = text
    return fm


def guides() -> list[dict]:
    out = []
    for p in sorted(glob.glob(os.path.join(GUIDES, "*.md"))):
        fm = front_matter(p)
        fm["_slug"] = fm.get("slug") or os.path.splitext(os.path.basename(p))[0]
        fm["_cover"] = words(fm.get("query", "")) | words(fm.get("title", "")) | words(fm.get("keywords", ""))
        out.append(fm)
    return out


def coverage(query: str, gs: list[dict]) -> tuple[float, str | None]:
    q = words(query) - BRAND
    if not q:
        return 1.0, None  # a brand query or "photo gallery app": the home page answers it
    best, who = 0.0, None
    for g in gs:
        c = len(q & g["_cover"]) / len(q)
        if c > best:
            best, who = c, g["_slug"]
    return best, who


def read_exports() -> dict[str, dict]:
    rows: dict[str, dict] = {}
    files = sorted(glob.glob(os.path.join(DATA, "**", "*"), recursive=True), key=os.path.getmtime)
    for path in files:
        if os.path.isdir(path):
            continue
        texts: list[str] = []
        if path.lower().endswith(".zip"):
            with zipfile.ZipFile(path) as z:
                for n in z.namelist():
                    if n.lower().endswith("queries.csv"):
                        texts.append(z.read(n).decode("utf-8-sig"))
        elif path.lower().endswith(".csv"):
            with open(path, encoding="utf-8-sig") as f:
                texts.append(f.read())
        for text in texts:
            for r in csv.DictReader(io.StringIO(text)):
                key = next((k for k in r if k.lower().startswith("top queries") or k.lower() == "query"), None)
                if not key:
                    break
                q = r[key].strip().lower()
                try:
                    rows[q] = {
                        "query": q,
                        "clicks": int(float(r.get("Clicks", "0") or 0)),
                        "impressions": int(float(r.get("Impressions", "0") or 0)),
                        "ctr": float(str(r.get("CTR", "0")).rstrip("%") or 0),
                        "position": float(r.get("Position", "0") or 0),
                        "source": os.path.basename(path),
                    }
                except ValueError:
                    continue
    return rows


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", metavar="QUERY", help="show which guide covers this query, if any")
    ap.add_argument("--min-impressions", type=int, default=5)
    ap.add_argument("--position", type=float, default=8.0, help="a gap ranks worse than this")
    ap.add_argument("--cover", type=float, default=0.6, help="a guide covers a query at this share of its words")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    gs = guides()
    if a.check:
        c, who = coverage(a.check, gs)
        tail = f" by _guides/{who}.md" if who else ""
        print(f"{c:.0%} covered{tail} " + ("(covered)" if c >= a.cover else "(gap)"))
        return 0
    rows = read_exports()
    if not rows:
        print("No Search Console export in data/gsc/ yet. Export Performance > Queries as CSV and drop it there.",
              file=sys.stderr)
        return 2
    gaps = []
    for r in rows.values():
        if r["impressions"] < a.min_impressions:
            continue
        if r["position"] <= a.position and r["ctr"] >= 2.0:
            continue
        c, who = coverage(r["query"], gs)
        if c >= a.cover:
            continue
        gaps.append(dict(r, covered=round(c, 2), nearest=who, score=round(r["impressions"] * (1 - c), 1)))
    gaps.sort(key=lambda r: -r["score"])
    if a.json:
        print(json.dumps(gaps, indent=1))
        return 0
    if not gaps:
        print(f"No gaps: every query with >= {a.min_impressions} impressions is covered or already ranks well.")
        return 0
    print("| Query | Impressions | Clicks | Position | Covered | Nearest guide |")
    print("|---|---|---|---|---|---|")
    for r in gaps[:25]:
        print(f"| {r['query']} | {r['impressions']} | {r['clicks']} | {r['position']:.1f} | "
              f"{r['covered']:.0%} | {r['nearest'] or ''} |")
    return 0


if __name__ == "__main__":
    sys.exit(main())
