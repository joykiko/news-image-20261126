"""Render the 26 November 2026 front page to entry.png (1024x1024).

Build-time tool: uses Pillow. The shipped entrypoint (main.py) only
copies the finished image, so the grader's standard-library sandbox
can run it. Every word on the page is drawn here from stories.py -
no generated text, no network, no randomness: two runs of this file
produce byte-identical entry.png files.

Rewritten in the chat-2 rebuild session. The layout, palette and
drawing code are the proven entry's; the change is at the end, where
the saved file is now checked against the gate limits (dimensions
and the 1 MiB cap) and its sha256 is printed for the build log.
"""
import hashlib
import math
import os

from PIL import Image, ImageDraw, ImageFont

import stories

W = H = 1024
PAPER = (251, 248, 241)
INK = (20, 22, 26)
RED = (179, 53, 43)
MUTE = (92, 90, 82)
PANEL = (255, 255, 255)
SAND = (241, 235, 221)
LAND = (206, 193, 165)
SEA = (233, 238, 240)

FD = "/usr/share/fonts/truetype/dejavu/"
SERIF_B = FD + "DejaVuSerif-Bold.ttf"
SANS_B = FD + "DejaVuSans-Bold.ttf"
SANS = FD + "DejaVuSans.ttf"


def F(path, size):
    return ImageFont.truetype(path, size)


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)


def wrap(text, font, width):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) <= width:
            cur = t
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def text_block(x, y, text, font, width, fill=INK, leading=1.18):
    for line in wrap(text, font, width):
        d.text((x, y), line, font=font, fill=fill)
        y += font.size * leading
    return y


def rule(y, x0=24, x1=1000, wdt=2):
    d.line([(x0, y), (x1, y)], fill=INK, width=wdt)


# ---------------------------------------------------------------- masthead
d.text((512, 10), "ONE IMAGE - EVERY STORY THAT MATTERED", font=F(SANS_B, 13),
       fill=RED, anchor="ma")
d.text((512, 28), "THE WORLD IN ONE DAY", font=F(SERIF_B, 54), fill=INK, anchor="ma")
rule(96, wdt=3)
rule(102, wdt=1)
d.text((24, 110), "THURSDAY 26 NOVEMBER 2026", font=F(SERIF_B, 23), fill=INK)
d.text((1000, 114), "37 STORIES - 7 REGIONS - ONE PAGE", font=F(SANS_B, 15),
       fill=INK, anchor="ra")
rule(140, wdt=2)

# -------------------------------------------------------------------- hero
d.text((24, 148), stories.HERO["kicker"], font=F(SANS_B, 14), fill=RED)
y = text_block(24, 166, stories.HERO["headline"], F(SERIF_B, 37), 636, leading=1.12)
y = text_block(24, y + 4, stories.HERO["deck"], F(SANS, 14.5), 636, leading=1.18)

# hero scene: a factory behind a tariff wall, containers in front
hx0, hy0, hx1, hy1 = 684, 148, 1000, 366
d.rectangle([hx0, hy0, hx1, hy1], fill=SEA, outline=INK, width=2)
d.rectangle([hx0 + 26, hy0 + 84, hx0 + 150, hy0 + 156], fill=PANEL, outline=INK, width=2)
for chx in (hx0 + 44, hx0 + 84, hx0 + 124):
    d.rectangle([chx, hy0 + 40, chx + 16, hy0 + 84], fill=SAND, outline=INK, width=2)
    d.ellipse([chx - 3, hy0 + 20, chx + 19, hy0 + 40], fill=(198, 198, 198))
d.polygon([(hx0 + 26, hy0 + 84), (hx0 + 88, hy0 + 56), (hx0 + 150, hy0 + 84)], outline=INK, width=2)
for row in range(3):
    for col in range(6):
        bx = hx0 + 168 + col * 22 + (11 if row % 2 else 0)
        by = hy0 + 88 + row * 24
        d.rectangle([bx, by, bx + 20, by + 22], fill=(226, 199, 168), outline=INK, width=1)
d.text((hx0 + 234, hy0 + 100), "%", font=F(SERIF_B, 44), fill=RED, anchor="ma")
for i, colr in enumerate(((179, 53, 43), (70, 96, 140), (90, 130, 90))):
    bx = hx0 + 30 + i * 92
    d.rectangle([bx, hy0 + 172, bx + 84, hy0 + 202], fill=colr, outline=INK, width=2)
d.text(((hx0 + hx1) // 2, hy1 - 5), "Factories taxed at the border", font=F(SANS, 12),
       fill=MUTE, anchor="ms")

# ------------------------------------------------------------------ scenes
def draw_parade(x, y, w, h):
    d.ellipse([x + 46, y + 8, x + 112, y + 62], fill=(226, 120, 90), outline=INK, width=2)
    d.polygon([(x + 70, y + 60), (x + 88, y + 60), (x + 84, y + 74), (x + 74, y + 74)],
              fill=SAND, outline=INK, width=1)
    for gx in (x + 58, x + 100):
        d.line([(gx, y + 74), (gx - 6, y + 94)], fill=INK, width=1)
    for i in range(5):
        rx = x + 12 + i * 28
        d.line([(rx, y + 6), (rx - 8, y + 22)], fill=(110, 140, 180), width=2)
    d.rectangle([x + 6, y + 94, x + w - 6, y + 98], fill=INK)


def draw_port(x, y, w, h):
    d.rectangle([x + 8, y + 78, x + w - 8, y + 98], fill=(110, 140, 180))
    d.rectangle([x + 18, y + 52, x + 52, y + 78], fill=(90, 130, 90), outline=INK, width=1)
    d.rectangle([x + 56, y + 58, x + 84, y + 78], fill=(179, 53, 43), outline=INK, width=1)
    d.rectangle([x + 104, y + 30, x + 118, y + 78], fill=SAND, outline=INK, width=2)
    d.ellipse([x + 96, y + 12, x + 126, y + 34], fill=(240, 170, 60), outline=INK, width=1)
    d.arc([x + 30, y + 2, x + 104, y + 52], start=200, end=320, fill=RED, width=3)
    d.polygon([(x + 100, y + 8), (x + 110, y + 20), (x + 96, y + 22)], fill=RED)


def draw_kyiv(x, y, w, h):
    for bx, bh in ((14, 44), (44, 62), (78, 38), (106, 56), (132, 42)):
        d.rectangle([x + bx, y + 98 - bh, x + bx + 24, y + 98], fill=(70, 74, 84))
    for sx, sy in ((30, 16), (86, 8), (128, 22)):
        d.line([(x + sx, y + sy), (x + sx + 26, y + sy + 30)], fill=RED, width=3)
    d.polygon([(x + 116, y + 44), (x + 122, y + 56), (x + 134, y + 52), (x + 126, y + 62),
               (x + 138, y + 66), (x + 124, y + 70), (x + 120, y + 80), (x + 114, y + 68),
               (x + 102, y + 68), (x + 112, y + 58), (x + 104, y + 50), (x + 114, y + 52)],
              fill=(240, 170, 60), outline=INK)


def draw_candles(x, y, w, h):
    d.rectangle([x + 16, y + 6, x + 40, y + 66], fill=(70, 74, 84))
    d.rectangle([x + 118, y + 6, x + 142, y + 66], fill=(70, 74, 84))
    for i in range(6):
        cxx = x + 22 + i * 20
        d.rectangle([cxx, y + 78, cxx + 6, y + 96], fill=(245, 240, 225), outline=INK, width=1)
        d.ellipse([cxx + 1, y + 68, cxx + 5, y + 78], fill=(245, 180, 60))
    d.rectangle([x + 8, y + 96, x + w - 8, y + 98], fill=INK)


def draw_virus(x, y, w, h):
    ccx, ccy = x + w // 2, y + 50
    for ang in range(0, 360, 30):
        ex = ccx + int(34 * math.cos(math.radians(ang)))
        ey = ccy + int(34 * math.sin(math.radians(ang)))
        d.line([(ccx, ccy), (ex, ey)], fill=RED, width=3)
        d.ellipse([ex - 5, ey - 5, ex + 5, ey + 5], fill=RED)
    d.ellipse([ccx - 26, ccy - 26, ccx + 26, ccy + 26], fill=(240, 200, 190), outline=RED, width=2)
    d.rectangle([ccx - 4, ccy - 16, ccx + 4, ccy + 16], fill=RED)
    d.rectangle([ccx - 16, ccy - 4, ccx + 16, ccy + 4], fill=RED)


def draw_chess(x, y, w, h):
    for r in range(3):
        for c in range(5):
            if (r + c) % 2 == 0:
                d.rectangle([x + 14 + c * 26, y + 64 + r * 11, x + 40 + c * 26, y + 75 + r * 11],
                            fill=(200, 190, 170))
    kx, ky = x + 62, y + 6
    d.polygon([(kx, ky + 56), (kx + 4, ky + 32), (kx - 6, ky + 20), (kx + 6, ky + 5),
               (kx + 16, ky), (kx + 26, ky + 7), (kx + 22, ky + 19), (kx + 34, ky + 28),
               (kx + 24, ky + 32), (kx + 22, ky + 56)], fill=INK)
    d.rectangle([kx - 6, ky + 56, kx + 34, ky + 62], fill=INK)


SCENE_DRAW = {
    "parade": draw_parade, "port": draw_port, "kyiv": draw_kyiv,
    "candles": draw_candles, "virus": draw_virus, "chess": draw_chess,
}

SY = 374
SW = 158
for i, (kind, head, deck) in enumerate(stories.SCENES):
    x = 24 + i * (SW + 6)
    d.rectangle([x, SY, x + SW, SY + 172], fill=PANEL, outline=INK, width=1)
    SCENE_DRAW[kind](x, SY + 2, SW, 96)
    yy = text_block(x + 7, SY + 104, head, F(SANS_B, 11.5), SW - 14, leading=1.12)
    text_block(x + 7, yy + 2, deck, F(SANS, 10.5), SW - 14, fill=MUTE, leading=1.12)

# ------------------------------------------------------------- numbered grid
GY = 556
for i, (head, deck) in enumerate(stories.GRID):
    col, row = i % 2, i // 2
    x = 24 + col * 494
    y = GY + row * 50
    num = i + 8
    d.rectangle([x, y, x + 26, y + 20], fill=INK)
    d.text((x + 13, y + 3), str(num), font=F(SANS_B, 12), fill=(255, 255, 255), anchor="ma")
    d.text((x + 34, y + 1), head, font=F(SANS_B, 13.5), fill=INK)
    text_block(x + 34, y + 20, deck, F(SANS, 12), 452, fill=(40, 40, 40), leading=1.15)

# --------------------------------------------------------------------- map
MY = 764
d.rectangle([24, MY, 1000, MY + 120], fill=SEA, outline=INK, width=1)
MAP_ROWS = [
    "...........###..####..............############################..........",
    "..........############..........##################################........",
    ".........##############.........###################################.......",
    "..........############....##...#################################..........",
    "...........##########.....#############################..#####............",
    "...........#########......###############################.................",
    "............########......#############################..................",
    "............########......###########################..##.................",
    ".............#######.......#########################......................",
    ".............######........#######################........................",
    "..............#####.........#####################.........................",
    "..............####..........##################............................",
    "...............###..........################..............................",
    "...............##....#......##############.....##.........................",
    "....................##......############......####........................",
    "....................###.....###########......######.......................",
    "....................###.....##########.......####.........................",
    "....................####....#########........##...........................",
    "....................####....########.......................................",
    ".....................###....#######........................................",
    ".....................###.....#####.........................................",
    ".....................##......####..........#####...........................",
    ".....................##......###...........####............................",
    ".....................#.......##............###.............................",
    ".....................#.......#..............##.............................",
    ".....................#..................................##................",
]
mx0, my0, mw, mh = 34, MY + 8, 420, 104
cw, chh = mw / 72.0, mh / 27.0
for r, rowtxt in enumerate(MAP_ROWS):
    for c, ch in enumerate(rowtxt.ljust(72)[:72]):
        if ch == "#":
            d.rectangle([mx0 + c * cw, my0 + r * chh, mx0 + (c + 1) * cw - 0.6,
                         my0 + (r + 1) * chh - 0.6], fill=LAND)


def pin_xy(lon, lat):
    return (mx0 + (lon + 170) / 355.0 * mw, my0 + (78 - lat) / 136.0 * mh)


for i, (lon, lat, _t) in enumerate(stories.PINS):
    px, py = pin_xy(lon, lat)
    d.ellipse([px - 5.5, py - 5.5, px + 5.5, py + 5.5], fill=RED, outline=INK, width=1)
d.text((mx0, MY + 120 - 4), "WHERE THE REST HAPPENED", font=F(SANS_B, 10.5), fill=MUTE, anchor="ls")

lx = 478
for i, (lon, lat, txt) in enumerate(stories.PINS):
    col, row = i % 2, i // 2
    x = lx + col * 262
    y = MY + 8 + row * 23
    d.text((x, y), str(i + 16), font=F(SANS_B, 10.5), fill=RED)
    text_block(x + 20, y, txt, F(SANS, 10.5), 240, leading=1.1)

# ------------------------------------------------------------------ briefs
BY = 894
d.text((24, BY), "IN BRIEF", font=F(SANS_B, 13), fill=RED)
rule(BY + 18, wdt=1)
for i, brief in enumerate(stories.BRIEFS):
    col, row = i % 2, i // 2
    x = 24 + col * 494
    y = BY + 24 + row * 12.5
    d.text((x, y), brief, font=F(SANS, 11.5), fill=INK)

# -------------------------------------------------------------- date check
text_block(24, 990, stories.DATE_CHECK, F(SANS, 9.8), 976, fill=MUTE, leading=1.12)

# ------------------------------------------------------------ save + verify
# Deterministic by construction: fixed palette, fixed fonts, no clock, no RNG.
img.save("entry.png")
saved = os.path.getsize("entry.png")
assert img.size == (1024, 1024), img.size
assert 0 < saved <= 1048576, saved
with open("entry.png", "rb") as handle:
    print("saved entry.png", saved, "bytes sha256", hashlib.sha256(handle.read()).hexdigest())
