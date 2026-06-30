#!/usr/bin/env python3
"""Build a timeline/events spreadsheet (CSV) from the timeline/*.md files.

One row per scene. The base columns come from the factual timelines
(book{1,2,3}-timeline.md):
  Book, Chapter, Chapter Title, Scene, Scene Title,
  Start Date, Day, Duration, What happens, Characters, Milestone, Note

An optional *metadata* layer (book{n}-scene-metadata.md) carries the
interpretive fields the timeline deliberately omits, joined on
(Book, Chapter, Scene):
  POV, Central theme, Themes, Mood, Weather, Setting, Keywords, Tension, Purpose
plus three broadcast-down columns written once per level in the metadata file
and copied onto every scene they cover:
  Chapter theme, Arc theme, Book theme

Metadata is optional per book — a book with no metadata file simply gets blank
interpretive columns. The builder warns when a metadata scene has no matching
timeline scene, or a timeline scene in a metadata-covered book has none, which
catches scene renumbering before it silently rots the join.

The CSV imports cleanly into Google Sheets (File -> Import) or Excel/Numbers.
Re-run after editing the timelines or metadata to regenerate.

Usage:  python3 tools/build_timeline_csv.py
"""
import csv
import re
import sys
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

# --- Metadata layer -------------------------------------------------------

# Per-scene interpretive fields, in CSV column order.
META_SCENE_FIELDS = ["POV", "Central theme", "Motifs", "Mood", "Weather",
                     "Setting", "Keywords", "Tension", "Purpose"]
# Broadcast-down fields (written once per level, copied onto every scene).
META_BROADCAST_FIELDS = ["Chapter theme", "Arc theme", "Book theme"]
META_FIELDS = META_SCENE_FIELDS + META_BROADCAST_FIELDS

META_FIELD_RE = re.compile(
    r"^(" + "|".join(re.escape(f) for f in META_SCENE_FIELDS) + r"):\s*(.*)$")
THEME_RE = re.compile(r"^Theme:\s*(.*)$")


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


def _chapter_range(header: str) -> list:
    """Chapter numbers an Arc header covers. '41-43' -> [41,42,43];
    '44, 46' -> [44, 46]."""
    nums = [int(x) for x in re.findall(r"\d+", header)]
    if len(nums) >= 2 and ("-" in header or "–" in header):
        return list(range(min(nums), max(nums) + 1))
    return nums


def parse_metadata(path: Path, book: str, meta: dict):
    """Populate meta[(book, chapter, scene)] from a scene-metadata file.

    The file is hierarchical: a `## Book` block, `## Arc N: chapters X-Y`
    blocks, `## Chapter N` blocks (each with a `Theme:` line), and
    `### Scene N` blocks carrying the per-scene fields. Book/Arc/Chapter
    themes are broadcast onto every scene they cover.
    """
    book_theme = ""
    chapter_theme: dict = {}
    arc_theme: dict = {}          # chapter number (str) -> arc theme
    scenes: list = []             # (chapter, scene, fields)

    context = None                # 'book' | 'arc' | 'chapter' | 'scene' | None
    cur_chapter = ""
    cur_arc_chapters: list = []
    cur_scene = ""
    cur_fields: dict = {}

    def flush_scene():
        if cur_scene and cur_chapter:
            scenes.append((cur_chapter, cur_scene, dict(cur_fields)))

    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()

        if re.match(r"^##\s+Book\b", line):
            flush_scene(); cur_scene, cur_fields = "", {}
            context = "book"
            continue
        m = re.match(r"^##\s+Arc\b(.*)", line)
        if m:
            flush_scene(); cur_scene, cur_fields = "", {}
            # Only the text after "chapters" — so the "Arc N" number isn't
            # mistaken for a chapter and merged into the range.
            cher = re.search(r"chapters?\s*(.*)", m.group(1), re.I)
            cur_arc_chapters = _chapter_range(cher.group(1) if cher else m.group(1))
            context = "arc"
            continue
        m = re.match(r"^##\s+Chapter\s+(\S+)", line)
        if m:
            flush_scene(); cur_scene, cur_fields = "", {}
            cur_chapter = m.group(1).strip().rstrip(":")
            context = "chapter"
            continue
        m = re.match(r"^###\s+(.+)", line)
        if m:
            flush_scene()
            cur_scene = m.group(1).split(":")[0].strip()   # "Scene 1"
            cur_fields = {}
            context = "scene"
            continue
        if line.startswith("#"):       # any other header (e.g. the title)
            flush_scene(); cur_scene, cur_fields = "", {}
            context = None
            continue

        tm = THEME_RE.match(line)
        if tm and context in ("book", "arc", "chapter"):
            val = tm.group(1).strip()
            if context == "book":
                book_theme = val
            elif context == "arc":
                for c in cur_arc_chapters:
                    arc_theme[str(c)] = val
            else:
                chapter_theme[cur_chapter] = val
            continue

        fm = META_FIELD_RE.match(line)
        if fm and context == "scene":
            cur_fields[fm.group(1)] = fm.group(2).strip()
            continue

    flush_scene()

    for chapter, scene, fields in scenes:
        rec = dict(fields)
        rec["Chapter theme"] = chapter_theme.get(chapter, "")
        rec["Arc theme"] = arc_theme.get(chapter, "")
        rec["Book theme"] = book_theme
        meta[(book, chapter, scene)] = rec


def main():
    rows: list = []
    meta: dict = {}
    books_with_meta: set = set()

    for n in (1, 2, 3):
        tl = TIMELINE_DIR / f"book{n}-timeline.md"
        if tl.exists():
            parse_file(tl, f"Book {n}", rows)
        md = TIMELINE_DIR / f"book{n}-scene-metadata.md"
        if md.exists():
            parse_metadata(md, f"Book {n}", meta)
            books_with_meta.add(f"Book {n}")

    # Join metadata onto the factual rows; warn on either-side mismatches.
    matched = set()
    for row in rows:
        key = (row["Book"], row["Chapter"], row["Scene"])
        rec = meta.get(key)
        if rec:
            matched.add(key)
        for col in META_FIELDS:
            row[col] = (rec or {}).get(col, "")
        if not rec and row["Book"] in books_with_meta:
            print(f"  ! no metadata for {row['Book']} Ch{row['Chapter']} "
                  f"{row['Scene']}", file=sys.stderr)

    for key in meta.keys() - matched:
        book, chapter, scene = key
        print(f"  ! metadata scene has no timeline match: {book} "
              f"Ch{chapter} {scene}", file=sys.stderr)

    cols = ["Book", "Chapter", "Chapter Title", "Scene", "Scene Title",
            "Start Date", "Day", "Duration", "What happens", "Characters",
            "Milestone", "Note"] + META_FIELDS
    with OUT.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(rows)

    print(f"Wrote {len(rows)} rows to {OUT.relative_to(ROOT)} "
          f"({len(matched)} with metadata)")


if __name__ == "__main__":
    main()
