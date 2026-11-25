#!/usr/bin/env python3
"""The One-Line AI Excuse for Breaking Production — a make.fun one-line entry. The program writes the entry text to /output/entry.txt, where the competition's sealed scorer reads it."""

from pathlib import Path

ENTRY = "I didn't break production — I promoted the bug to production, gave it a title, and it has been attending standup ever since."
OUTPUT = Path("/output/entry.txt")


def write_entry() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be blank"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    write_entry()
