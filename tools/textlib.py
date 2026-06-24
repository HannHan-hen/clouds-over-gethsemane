"""Shared manuscript-parsing helpers for the tools/ scripts.

Single source of truth for chapter/scene/line parsing, tokenizing,
sentence splitting, the stopword set, dispersion, and the character-name
roster. Keep manuscript-format assumptions (the ``Chapter N:`` / ``Scene N``
markers) here so every tool stays in sync.
"""
from __future__ import annotations

import os
import re
from collections import namedtuple

WORD_RE = re.compile(r"[a-z0-9']+")
CHAP_RE = re.compile(r"^Chapter\s+(\d+)\s*:", re.IGNORECASE)
SCENE_RE = re.compile(r"^Scene\s+(\d+)", re.IGNORECASE)
SENT_SPLIT_RE = re.compile(r"[.!?]+[\"')\s]")
WILDCARD = "<>"

STOPWORDS = {
    "a", "an", "the", "and", "but", "or", "nor", "for", "so", "yet",
    "as", "at", "by", "in", "into", "of", "off", "on", "onto", "out",
    "over", "to", "up", "with", "from", "about", "after", "before",
    "between", "through", "under", "until", "while", "during", "against",
    "i", "you", "he", "she", "it", "we", "they", "me", "him", "her",
    "us", "them", "my", "your", "his", "its", "our", "their", "mine",
    "this", "that", "these", "those", "who", "whom", "whose", "which",
    "what", "when", "where", "why", "how", "there", "here", "then",
    "is", "am", "are", "was", "were", "be", "been", "being", "do",
    "does", "did", "have", "has", "had", "will", "would", "shall",
    "should", "can", "could", "may", "might", "must", "not", "no",
    "if", "than", "too", "very", "just", "only", "own", "same", "such",
    "more", "most", "some", "any", "all", "both", "each", "few", "other",
    "again", "once", "now", "still",
}

Line = namedtuple("Line", "book chapter scene lineno text")
Chapter = namedtuple("Chapter", "label book number tokens text")


def iter_lines(paths):
    """Yield Line(book, chapter, scene, lineno, text) for narrative lines.

    Chapter/Scene marker lines are consumed (not yielded); blank lines and
    any text before the first chapter marker are skipped. ``lineno`` is
    1-based within its file, so tool output is clickable.
    """
    for path in paths:
        book = os.path.splitext(os.path.basename(path))[0]
        chap = scene = None
        with open(path, encoding="utf-8") as fh:
            for lineno, raw in enumerate(fh, 1):
                stripped = raw.strip()
                m = CHAP_RE.match(stripped)
                if m:
                    chap, scene = int(m.group(1)), None
                    continue
                ms = SCENE_RE.match(stripped)
                if ms:
                    scene = int(ms.group(1))
                    continue
                if chap is None or not stripped:
                    continue
                yield Line(book, chap, scene, lineno, stripped)


def load_chapters(paths):
    """Return [Chapter(label, book, number, tokens, text)], one per chapter."""
    chapters = []
    cur_key = None
    words, texts = [], []

    def flush():
        if cur_key is not None:
            book, num = cur_key
            chapters.append(Chapter(f"{book} ch{num:02d}", book, num,
                                    words[:], " ".join(texts)))

    for ln in iter_lines(paths):
        key = (ln.book, ln.chapter)
        if key != cur_key:
            flush()
            cur_key = key
            words.clear()
            texts.clear()
        words.extend(WORD_RE.findall(ln.text.lower()))
        texts.append(ln.text)
    flush()
    return chapters


def split_sentences(raw_text):
    """Split a chunk of prose into sentence strings (punctuation-based)."""
    return [s for s in SENT_SPLIT_RE.split(raw_text) if WORD_RE.findall(s)]


def sentence_openers(raw_text, depths=(1, 2, 3)):
    """Yield (depth, opener_key) for the leading tokens of each sentence."""
    for sent in split_sentences(raw_text):
        toks = WORD_RE.findall(sent.lstrip(" \"'—–-").lower())
        for d in depths:
            if len(toks) >= d:
                yield d, " ".join(toks[:d])


def deviation_of_proportions(chap_counts, chap_sizes, total):
    """Gries' DP in [0,1]: 0 = perfectly even across chapters, ~1 = all in one."""
    if total == 0:
        return 0.0
    corpus = sum(chap_sizes) or 1
    dp = 0.0
    for idx, size in enumerate(chap_sizes):
        expected = size / corpus
        observed = chap_counts.get(idx, 0) / total
        dp += abs(expected - observed)
    return 0.5 * dp


# Header first-words in characters.md that are descriptors, not people.
_NON_NAME = {"the", "a", "an", "office", "building", "cleaning", "staff",
             "security", "reception", "minor", "extended", "professional",
             "friends", "main", "supporting", "antagonists"}
_SLUG_PREFIX = {"mc", "ml"}  # 'mc-jay-hall' -> jay, 'ml-ian-hagen' -> ian


def load_names(path="characters.md",
               char_dir="source/raw/2026-06-23-novelcrafter-export/characters"):
    """Return (first_names, full_names), lowercased.

    Combines the '### Name' headers in characters.md (skipping descriptor
    headers like 'The Building Manager') with the clean per-character slugs
    in the Novelcrafter export, which is the authoritative roster.
    """
    first, full = set(), set()

    if os.path.exists(path):
        with open(path, encoding="utf-8") as fh:
            for line in fh:
                title = None
                if line.startswith("### "):
                    title = line[4:].split("(")[0].strip()
                else:
                    # Bold-bulleted walk-on registry entries: '- **Meg Randon** —'
                    m = re.match(r"\s*-\s+\*\*([^*]+)\*\*", line)
                    if m:
                        title = m.group(1).strip()
                if title is None:
                    continue
                parts = [p.lower() for p in re.findall(r"[A-Za-z']+", title)
                         if p.lower() not in {"née", "nee"}]
                if not parts or parts[0] in _NON_NAME or parts[0] in STOPWORDS:
                    continue
                first.add(parts[0])
                full.update(parts)

    if os.path.isdir(char_dir):
        for entry in os.listdir(char_dir):
            toks = [t for t in re.split(r"[-_]", entry.lower())
                    if t.isalpha() and len(t) >= 2]
            while toks and toks[0] in _SLUG_PREFIX:
                toks.pop(0)
            # drop the trailing slug id (e.g. '...hall2yvxg...') if non-alpha-ish
            if toks:
                first.add(toks[0])
                full.update(t for t in toks if len(t) >= 2)

    first -= STOPWORDS | _NON_NAME
    full -= STOPWORDS | _NON_NAME
    return first, full
