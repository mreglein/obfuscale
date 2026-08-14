#!/usr/bin/env python3
"""Scan the whole tracked tree (not the staged diff) for host-identifying
strings: absolute local paths and internal-lab hostnames. Exits non-zero on
any unexpected hit.

Deliberately scans `git ls-files`, not `git diff --staged` -- the leaks this
was built to catch (manifest_pairs.csv, challenge_counts*.csv) were already
committed; a staged-only check could never have found them. Run manually,
via pre-commit (local hook), and in CI.
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

# Files that legitimately discuss these patterns by name. Empty for now --
# this repo carries none of the private repo's governance docs that name
# the leak class explicitly. Add entries here only with a comment
# explaining why a match is not a leak.
ALLOWLIST: set[str] = {
    "scripts/check_no_local_paths.py",  # this file's own docstring/patterns
}

BINARY_EXTS = {
    ".png", ".jpg", ".jpeg", ".gif", ".ico", ".pdf",
    ".bin", ".exe", ".dll", ".sys", ".db", ".pyc",
}

PATTERNS = [
    re.compile(r"/home/[a-zA-Z0-9_.\-]+"),
    re.compile(r"/mnt/[a-zA-Z0-9_.\-]+"),
    re.compile(r"\bhermes\b", re.IGNORECASE),
    re.compile(r"\bxerxes\b", re.IGNORECASE),
    re.compile(r"\batlantis\b", re.IGNORECASE),
]


def tracked_files() -> list[str]:
    out = subprocess.run(
        ["git", "ls-files"], cwd=REPO_ROOT, capture_output=True, text=True, check=True
    )
    return [line for line in out.stdout.splitlines() if line]


def main() -> int:
    hits: list[str] = []
    for rel in tracked_files():
        if rel in ALLOWLIST:
            continue
        path = REPO_ROOT / rel
        if path.suffix.lower() in BINARY_EXTS or not path.is_file():
            continue
        try:
            text = path.read_text(errors="ignore")
        except OSError:
            continue
        for lineno, line in enumerate(text.splitlines(), 1):
            for pat in PATTERNS:
                if pat.search(line):
                    hits.append(f"{rel}:{lineno}: {line.strip()[:120]}")
                    break

    if hits:
        print(f"check_no_local_paths: {len(hits)} hit(s) in tracked files:", file=sys.stderr)
        for h in hits:
            print(f"  {h}", file=sys.stderr)
        print(
            "\nIf this is a legitimate policy-doc mention, add the file to "
            "ALLOWLIST in this script with a comment explaining why.",
            file=sys.stderr,
        )
        return 1

    print("check_no_local_paths: clean")
    return 0


if __name__ == "__main__":
    sys.exit(main())
