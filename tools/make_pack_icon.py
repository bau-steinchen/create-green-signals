#!/usr/bin/env python3
"""Draw pack/pack.png: a pixel-art signal panel with a lit green and an unlit red lamp.

Drawn at 32x32 and scaled 4x (nearest neighbour) to 128x128.

Usage:
  python3 tools/make_pack_icon.py
"""
from pathlib import Path

from PIL import Image, ImageDraw

OUT = Path(__file__).resolve().parent.parent / "pack/pack.png"
SIZE = 32
SCALE = 4

BG = (24, 28, 34, 255)
FRAME = (122, 92, 54, 255)
FRAME_HI = (176, 136, 82, 255)
FRAME_LO = (78, 58, 34, 255)
PANEL = (38, 40, 44, 255)
GREEN = [(20, 90, 36), (31, 133, 52), (70, 200, 100), (180, 255, 200)]
RED_OFF = [(52, 18, 16), (70, 26, 22), (84, 34, 28)]


def glow(img, cx, cy, radius, color):
    # Soft additive halo behind the lit lamp.
    px = img.load()
    for y in range(SIZE):
        for x in range(SIZE):
            d = ((x - cx) ** 2 + (y - cy) ** 2) ** 0.5
            if d < radius:
                k = (1 - d / radius) ** 2 * 0.55
                r, g, b, a = px[x, y]
                px[x, y] = (min(255, round(r + color[0] * k)),
                            min(255, round(g + color[1] * k)),
                            min(255, round(b + color[2] * k)), a)


def lamp(d, x0, y0, shades):
    # 6x10 tube: dark rim, mid body, bright core.
    d.rectangle([x0, y0, x0 + 5, y0 + 9], fill=shades[0])
    d.rectangle([x0 + 1, y0 + 1, x0 + 4, y0 + 8], fill=shades[1])
    d.rectangle([x0 + 2, y0 + 2, x0 + 3, y0 + 7], fill=shades[2])
    if len(shades) > 3:
        d.point([(x0 + 2, y0 + 3), (x0 + 3, y0 + 5), (x0 + 2, y0 + 6)], fill=shades[3])


def main():
    img = Image.new("RGBA", (SIZE, SIZE), BG)
    d = ImageDraw.Draw(img)

    # Mast below the panel
    d.rectangle([14, 24, 17, 31], fill=FRAME_LO)
    d.rectangle([15, 24, 16, 31], fill=FRAME)

    # Panel with bevelled brass frame
    d.rectangle([5, 6, 26, 25], fill=FRAME)
    d.line([5, 6, 26, 6], fill=FRAME_HI)
    d.line([5, 6, 5, 25], fill=FRAME_HI)
    d.line([5, 25, 26, 25], fill=FRAME_LO)
    d.line([26, 6, 26, 25], fill=FRAME_LO)
    d.rectangle([7, 8, 24, 23], fill=PANEL)

    glow(img, 11.5, 15.5, 11, GREEN[2])
    d = ImageDraw.Draw(img)
    lamp(d, 9, 11, GREEN)
    lamp(d, 17, 11, RED_OFF)

    img = img.resize((SIZE * SCALE, SIZE * SCALE), Image.NEAREST)
    img.save(OUT)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
