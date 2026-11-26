"""Entry point for the news-image-20261126 entry.

The front page is rendered at build time by render.py (from stories.py)
into entry.png beside this file. This program copies those exact bytes
to the output directory, so the two grader runs always write identical
bytes and the program needs nothing beyond the Python standard library.

Rewritten in the chat-2 rebuild session: the copy is now verified
byte-for-byte against the source before the program reports success,
and a missing or empty source fails loudly instead of writing nothing.
"""
import hashlib
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
MAX_BYTES = 1048576  # the gate's 1 MiB cap for the image file
# The image itself is exactly 1024x1024; render.py asserts that at build time.


def sha256_of(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    if not os.path.isfile(SOURCE):
        raise SystemExit("entry.png is missing beside main.py")
    size = os.path.getsize(SOURCE)
    if size == 0 or size > MAX_BYTES:
        raise SystemExit("entry.png size %d is outside the gate limits" % size)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SOURCE, target)
    if sha256_of(target) != sha256_of(SOURCE):
        raise SystemExit("copied bytes differ from entry.png")
    print("wrote", target, size, "bytes")


if __name__ == "__main__":
    main()
