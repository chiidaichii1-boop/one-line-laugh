#!/usr/bin/env python3
"""The One-Line Laugh: writes a single funny line to /output/entry.txt.

The line sets up an everyday truth (a fitness tracker counting steps)
and lands a surprise twist at the very end that still makes sense:
the steps were not exercise, they were indecision.
"""

import os

LINE = (
    "My fitness tracker congratulated me on 10,000 steps today, "
    "which is generous, since 9,000 of them were me pacing while "
    "deciding what to eat."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
