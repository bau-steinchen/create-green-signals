#!/usr/bin/env python3
"""Draw signal_green.png, the texture used by this pack's lamp models.

The texture is generated from scratch (no third-party image as input).
Layout (16x16, UVs in the model files must match):
  - x 0..5,  y 0..8    -> tube side faces   (white_tube.json, uv [0,0,6,9])
  - x 0..5,  y 10..15  -> tube top/bottom   (white_tube.json, uv [0,10,6,16])
  - x 8,     y 0       -> glow              (white_glow.json, uv [8,0,9,1])
Both models are rendered additively by Create, so alpha acts as intensity.

Usage:
  python3 tools/make_green_texture.py [--tube 1F8534] [--glow 33DA55]
"""
import argparse
from pathlib import Path

from PIL import Image

OUT = (Path(__file__).resolve().parent.parent
       / "pack/assets/create_green_signals/textures/block/signal_green.png")
TUBE_ALPHA = 124
GLOW_ALPHA = 96


def hex_rgb(s):
    return tuple(int(s[i:i + 2], 16) for i in (0, 2, 4))


def shade(color, f, alpha):
    return tuple(round(c * f) for c in color) + (alpha,)


def draw_tube(im, x0, y0, w, h, color):
    # Darker rim, brighter centre, plus a fixed diagonal sparkle pattern
    # so the lamp looks like a glowing filament instead of a flat block.
    cx, cy = (w - 1) / 2, (h - 1) / 2
    for y in range(h):
        for x in range(w):
            d = max(abs(x - cx) / (cx + 0.5), abs(y - cy) / (cy + 0.5))
            f = 1.0 - 0.3 * d
            if (x + 2 * y) % 5 == 0:
                f -= 0.08
            im.putpixel((x0 + x, y0 + y), shade(color, f, TUBE_ALPHA))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tube", default="1F8534", help="brightest tube colour as hex RGB")
    ap.add_argument("--glow", default="33DA55", help="glow colour as hex RGB")
    args = ap.parse_args()

    im = Image.new("RGBA", (16, 16), (0, 0, 0, 0))
    tube = hex_rgb(args.tube)
    draw_tube(im, 0, 0, 6, 9, tube)
    draw_tube(im, 0, 10, 6, 6, tube)
    im.putpixel((8, 0), hex_rgb(args.glow) + (GLOW_ALPHA,))

    OUT.parent.mkdir(parents=True, exist_ok=True)
    im.save(OUT)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
