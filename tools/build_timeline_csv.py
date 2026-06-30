#!/usr/bin/env python3
"""Build a timeline/events spreadsheet (CSV) from the timeline/*.md files.

One row per scene. Columns:
  Book, Chapter, Chapter Title, Scene, Scene Title,
  Start Date, Day, Duration, What happens, Characters, Milestone, Note

The CSV imports cleanly into Google Sheets (File -> Import) or Excel/Numbers.
Re-run after editing the timelines to regenerate.

Usage:  python3 tools/build_timeline_csv.py
"""
import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TIMELINE_DIR = ROOT / "timeline"
OUT = ROOT / "timeline" / "timeline-events.csv"

# Known cast — matched as whole words against each scene's prose so the
# "Characters" column is best-effort, not authoritative.
CAST = [
    "Ian", "Jay", "Leo", "Amy", "Ela", "Luc", "Kim", "Zoe", "Max", "Sam",
    "Ari", "Ema", "Ira", "Ted", "Tim", "Liv", "Gal", "Rin", "Mac", "Ray",
    "Tia", "Ken", "Turner Senior",
]
CAST_RE = {name: re.compile(rf"\b{re.escape(name)}\b") for name in CAST}

# Lines beginning with one of these labels are treated as structured fields,
# not prose. Everything else inside a scene is the "what happens" description.
FIELD_RE = re.compile(r"^(Start Date|Day|Duration|Milestone|Note):\s*(.*)$")


def detect_characters(text: str) -> str:
    found = [name for name, rx in CAST_RE.items() if rx.search(text)]
    return ", ".join(found)


def parse_file(path: Path, book: str, rows: list):
    chapter = chapter_title = ""
    scene = scene_title = ""
    fields = {}
    desc_lines = []

    def flush():
        if not scene and not desc_lines and not fields:
            return
        if not (chapter or scene):
            return
        what = " ".join(desc_lines).strip()
        rows.append({
            "Book": book,
            "Chapter": chapter,
            "Chapter Title": chapter_title,
            "Scene": scene,
            "Scene Title": scene_title,
            "Start Date": fields.get("Start Date", ""),
            "Day": fields.get("Day", ""),
            "Duration": fields.get("Duration", ""),
            "What happens": what,
            "Characters": detect_characters(what),
            "Milestone": fields.get("Milestone", ""),
            "Note": fields.get("Note", ""),
        })

    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()

        m = re.match(r"^##\s+Chapter\s+(.+)", line)
        if m:
            flush()
            scene = scene_title = ""
            fields, desc_lines = {}, []
            head = m.group(1)
            if ":" in head:
                num, _, title = head.partition(":")
                chapter, chapter_title = num.strip(), title.strip()
            else:
                chapter, chapter_title = head.strip(), ""
            continue

        m = re.match(r"^###\s+(.+)", line)
        if m:
            flush()
            fields, desc_lines = {}, []
            head = m.group(1)
            if ":" in head:
                num, _, title = head.partition(":")
                scene, scene_title = num.strip(), title.strip()
            else:
                scene, scene_title = head.strip(), ""
            continue

        if line.startswith("#"):  # non-chapter section header (e.g. appendices)
            flush()
            scene = scene_title = ""
            fields, desc_lines = {}, []
            continue

        fm = FIELD_RE.match(line)
        if fm and scene:
            fields[fm.group(1)] = fm.group(2).strip()
            continue

        if line and scene and not line.startswith(">") and not line.startswith("---"):
            desc_lines.append(line)

    flush()


def main():
    rows: list = []
    for n in (1, 2, 3):
        path = TIMELINE_DIR / f"book{n}-timeline.md"
        if path.exists():
            parse_file(path, f"Book {n}", rows)

    cols = ["Book", "Chapter", "Chapter Title", "Scene", "Scene Title",
            "Start Date", "Day", "Duration", "What happens", "Characters",
            "Milestone", "Note"]
    with OUT.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(rows)

    print(f"Wrote {len(rows)} rows to {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
