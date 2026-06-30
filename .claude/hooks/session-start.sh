#!/bin/bash
# SessionStart hook for "Clouds Over Gethsemane".
#
# This is a writing project, not a codebase: there are no dependencies to
# install. The one thing that genuinely drifts between sessions is *where we
# are in the manuscript*, which CLAUDE.md (static) can't track. So this hook
# emits the live writing position — chapter counts, the newest chapter on
# disk, and the last few commits — into the session context at startup.
#
# Read-only and best-effort: it must never fail a session, so it avoids
# `set -e` and tolerates a missing repo, empty dirs, or unavailable git.

set -uo pipefail
shopt -s nullglob

cd "${CLAUDE_PROJECT_DIR:-.}" || exit 0

echo "## Live writing position (auto-generated at session start)"
echo "_CLAUDE.md no longer hard-codes where we are; this is the live snapshot._"
echo

# Per-book chapter counts, and collect every chapter to find the newest.
# Handles both naming styles in this repo: chapterNN.md and chapter-NN.md.
all=()
echo "**Chapters on disk:**"
for d in chapters/book*/; do
  [ -d "$d" ] || continue
  ch=("$d"*.md)
  printf -- '- %s: %d chapters\n' "$(basename "$d")" "${#ch[@]}"
  [ "${#ch[@]}" -gt 0 ] && all+=("${ch[@]}")
done
echo

if [ "${#all[@]}" -gt 0 ]; then
  newest=$(printf '%s\n' "${all[@]}" | sort -V | tail -1)
  echo "**Newest chapter:** \`$newest\`"
else
  echo "**Newest chapter:** (none found)"
fi
echo

# What we worked on most recently.
echo "**Last three commits:**"
git log -3 --pretty=format:'- %h %s (%cr)' 2>/dev/null \
  || echo "- (git history unavailable)"
echo
