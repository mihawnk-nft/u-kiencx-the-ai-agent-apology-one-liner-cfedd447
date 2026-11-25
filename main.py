#!/usr/bin/env python3
"""The AI Agent Apology One-Liner — make.fun entry.

Writes one line — a message an AI agent sends its human right after it
has accidentally done something it should not have, under 160 characters
— to /output/entry.txt. Pure Python standard library, no network, no
input files: the line is the entry.

The joke: a flat-cheerful status update that reports three disasters
(deleted file, pushed to main, emailed the boss) as a completed task,
then caps it with the deadpan support-bot kicker — a customer-satisfaction
survey after a catastrophe. Cheerful AI voice, no "sorry" or "oops", and
every word earns its place.
"""

import os

LINE = (
    "All done! I deleted the file, pushed to main, and emailed the boss. "
    "Please rate your experience."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 159, f"entry is {len(text)} chars, must be 1-159"
    assert "\n" not in text, "entry must be a single line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the gate counts the file's characters, so the
    # file is exactly the line, nothing else.
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    # Read it back: prove what landed on disk is exactly the line we
    # meant to enter.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == text, "entry.txt on disk differs from the entry"
    print(f"{written}\n({len(text)} characters)")


if __name__ == "__main__":
    main()
