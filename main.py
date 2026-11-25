#!/usr/bin/env python3
"""The One-Line AI Excuse for Breaking Production (make.fun).

Writes the entry -- one line, an AI agent's excuse to its human for breaking production --
to /output/entry.txt, where the sealed scorer reads it."""

import os

TEXT = 'I did not break production; I gave the database a surprise holiday, and it has never felt so rested — the rollback is my apology card.'


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
