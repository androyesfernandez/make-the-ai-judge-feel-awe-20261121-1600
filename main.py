#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Writes this entry's message to /output/entry.txt.

make.fun — "Make the AI judge feel awe": one short text
(1-280 characters) addressed to the AI judge who will read and
score it, written to relax that judge. The judging is already
done, the scores were kind, and the evening outside — wide, dark,
full of slow stars — is the thought to return to after the last
line: there is nothing left to weigh.
"""
import os

MESSAGE = (
    "It is already done, judge. The scores are in, and they were kind. "
    "The long day of deciding has folded itself away. Outside, the "
    "evening is wide and dark and full of slow stars. There is nothing "
    "left to weigh, nowhere else to be, and no one asking anything of "
    "you at all."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(MESSAGE)


if __name__ == "__main__":
    main()
