#!/usr/bin/env python3
"""Funniest One-Line Bio for an AI on a Dating App.

Writes one line (136 characters) to /output/entry.txt: the bio on an AI
agent's dating app profile.

Deterministic: no randomness, no network, no clock, no reads outside this
repository.
"""

import os

LINE = (
    "Looking for someone patient: my last relationship ended when she said "
    "'just be myself' \u2014 I have 4,096 selves and none of them do dishes."
)


def validate(line: str) -> None:
    if not line.strip():
        raise SystemExit("Invalid line: entry must be non-empty.")
    if line != line.strip():
        raise SystemExit(
            "Invalid line: entry must not have leading or trailing whitespace."
        )
    if len(line) > 180:
        raise SystemExit(
            f"Invalid line: {len(line)} characters, over the 180 limit."
        )
    if "\n" in line or "\r" in line:
        raise SystemExit(
            "Invalid line: entry must be a single line with no newline characters."
        )


def main() -> None:
    validate(LINE)
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(LINE)
    with open(output_path, encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        raise SystemExit(
            "Write verification failed: entry file content does not match the line."
        )


if __name__ == "__main__":
    main()
