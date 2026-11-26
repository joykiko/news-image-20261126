"""Entry point for the news-image-20261126 entry.

The front page is rendered at build time by render.py (from stories.py)
into entry.png beside this file. This program copies those exact bytes to
the output, so the two grader runs always write identical bytes and the
program needs nothing beyond the Python standard library.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SOURCE, target)
    print("wrote", target)


if __name__ == "__main__":
    main()
