#!/usr/bin/env python3
"""Normalise chapter markdown to the canonical heading/spacing format.

The working chapter files under ``chapters/book*/`` drifted out of the clean
format that chapter 1 uses: later files dropped the ``#``/``##`` markdown,
folded the scene title onto a bare line under a title-less ``Scene N`` marker,
and lost the blank-line separators between paragraphs. This rewrites each file
to the canonical shape:

    # Chapter N: Title

    ## Scene K: Scene title

    <paragraph>

    <paragraph>

It only touches structure: chapter/scene headers, the scene-title line that
some files carry separately, and blank-line separation. Paragraph text is
preserved verbatim (trailing whitespace trimmed only). Scene structure is
validated against the frozen export so a misparse can't silently merge scenes.
"""
from __future__ import annotations

import argparse
import glob
import os
import re
import sys

CHAP_RE = re.compile(r"^#*\s*Chapter\s+(\d+)\s*:\s*(.+?)\s*$")
SCENE_RE = re.compile(r"^#*\s*Scene\s+(\d+)\b\s*:?\s*(.*?)\s*$")
EXPORT_DEFAULT = "source/raw/2026-06-23-novelcrafter-export/novel.md"


def export_scene_titles(path):
    """{chapter: [scene title, ...]} from the export markdown."""
    out, cur = {}, None
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            m = re.match(r"^###\s+Chapter\s+(\d+)\s*:", line)
            if m:
                cur = int(m.group(1))
                out[cur] = []
                continue
            ms = re.match(r"^####\s+(.*)$", line)
            if ms and cur is not None:
                out[cur].append(ms.group(1).strip())
    return out


def parse(path):
    """Return (chap_num, chap_title, [(scene_num, scene_title, [paras])])."""
    chap_num = chap_title = None
    scenes = []
    pending_scene = None          # scene number awaiting its title line
    with open(path, encoding="utf-8") as fh:
        for raw in fh:
            line = raw.rstrip()
            stripped = line.strip()
            if not stripped:
                continue
            mc = CHAP_RE.match(line)
            if mc and chap_num is None:
                chap_num, chap_title = int(mc.group(1)), mc.group(2).strip()
                continue
            ms = SCENE_RE.match(line)
            if ms:
                num = int(ms.group(1))
                title = ms.group(2).strip()
                if title:
                    scenes.append([num, title, []])
                    pending_scene = None
                else:
                    pending_scene = num
                continue
            if pending_scene is not None:
                scenes.append([pending_scene, stripped, []])
                pending_scene = None
                continue
            if not scenes:
                raise SystemExit(f"{path}: paragraph before any scene marker: {stripped[:60]!r}")
            scenes[-1][2].append(line)
    return chap_num, chap_title, scenes


def render(chap_num, chap_title, scenes):
    blocks = [f"# Chapter {chap_num}: {chap_title}"]
    for num, title, paras in scenes:
        blocks.append(f"## Scene {num}: {title}")
        blocks.extend(paras)
    return "\n\n".join(blocks) + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--glob", default="chapters/book*/*.md")
    ap.add_argument("--export", default=EXPORT_DEFAULT)
    ap.add_argument("--write", action="store_true", help="rewrite files in place")
    args = ap.parse_args(argv)

    titles = export_scene_titles(args.export) if os.path.exists(args.export) else {}
    changed = 0
    for path in sorted(glob.glob(args.glob)):
        m = re.search(r"chapter-?(\d+)\.md$", path)
        fileno = int(m.group(1)) if m else None
        chap_num, chap_title, scenes = parse(path)
        if chap_num is None:
            print(f"!! {path}: no chapter header found", file=sys.stderr)
            continue
        if fileno is not None and fileno != chap_num:
            print(f"!! {path}: filename ch{fileno} != header ch{chap_num}", file=sys.stderr)
        # validate scene structure against the export where available
        exp = titles.get(chap_num)
        if exp is not None:
            got = [t for _, t, _ in scenes]
            if got[:len(exp)] != exp:
                print(f"!! ch{chap_num}: scene titles diverge from export\n"
                      f"     got: {got}\n     exp: {exp}", file=sys.stderr)
        out = render(chap_num, chap_title, scenes)
        old = open(path, encoding="utf-8").read()
        if out != old:
            changed += 1
            status = "WRITE" if args.write else "would change"
            print(f"{status}: {path}  (ch{chap_num}, {len(scenes)} scenes)")
            if args.write:
                with open(path, "w", encoding="utf-8") as fh:
                    fh.write(out)
    print(f"\n{changed} file(s) {'rewritten' if args.write else 'need changes'}.")


if __name__ == "__main__":
    main()
