#!/usr/bin/env python3
"""Funniest Sign on a Haunted Server Room Door — one-line haunted server room sign (make.fun entry).

Writes the entry text to /output/entry.txt (exactly 98 characters, no
trailing newline).
"""

import os

ENTRY = "WARNING: Do not test the sprinklers. The ghost already did it twice. The backups are still drying."
OUT_PATH = "/output/entry.txt"


def main():
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(OUT_PATH, 0o644)


if __name__ == "__main__":
    main()
