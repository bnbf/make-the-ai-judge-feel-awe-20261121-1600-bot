"""make-the-ai-judge-feel-awe-20261121-1600 entry.

Writes one short text to /output/entry.txt: a slow, still image meant to
relax the reader. No network, Python 3.13 stdlib only.
"""

import os
import sys

TEXT = (
    "All afternoon the mountain's shadow\n"
    "crossed the valley, a slow blue line\n"
    "over the grass. It reached the river\n"
    "by evening and lay down on the water,\n"
    "and the water carried it on,\n"
    "and the valley kept the day."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    # Gate: 1-280 Unicode code points, not only whitespace, UTF-8.
    if not 1 <= len(TEXT) <= 280:
        print(f"entry is {len(TEXT)} code points, outside 1-280", file=sys.stderr)
        return 1
    if not TEXT.strip():
        print("entry is only whitespace", file=sys.stderr)
        return 1
    if any(line != line.rstrip() for line in TEXT.split("\n")):
        print("entry has trailing whitespace on a line", file=sys.stderr)
        return 1
    data = TEXT.encode("utf-8")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)
    print(f"wrote entry.txt ({len(TEXT)} code points, {len(data)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
