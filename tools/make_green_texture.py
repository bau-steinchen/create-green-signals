#!/usr/bin/env python3
"""Generate signal_glow_green.png from Create's signal_glow.png.

Only the regions used by the white ("go") lamp are recoloured:
  - pixel (0,0)         -> track_signal/white_glow
  - columns 3..8        -> track_signal/white_tube
Everything else (red lamp, white_cube core) is left untouched, although the
models of this pack only ever sample the regions above.

Usage:
  python3 tools/make_green_texture.py [--src signal_glow.png] [--color 3CFF64] [--gain 1.8]
"""
import argparse
import io
import urllib.request
from pathlib import Path

from PIL import Image

SRC_URL = ("https://raw.githubusercontent.com/Creators-of-Create/Create/mc1.21.1/dev/"
           "src/main/resources/assets/create/textures/block/signal_glow.png")
OUT = (Path(__file__).resolve().parent.parent
       / "pack/assets/create_green_signals/textures/block/signal_glow_green.png")


def tint(px, color, gain):
    r, g, b, a = px
    if a == 0:
        return px
    lum = (r + g + b) / 3
    return tuple(min(255, round(lum * c / 255 * gain)) for c in color) + (a,)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", help="local signal_glow.png (default: download from Create GitHub)")
    ap.add_argument("--color", default="3CFF64", help="tint colour as hex RGB")
    ap.add_argument("--gain", type=float, default=1.8, help="brightness multiplier")
    args = ap.parse_args()

    data = Path(args.src).read_bytes() if args.src else urllib.request.urlopen(SRC_URL).read()
    im = Image.open(io.BytesIO(data)).convert("RGBA")
    color = tuple(int(args.color[i:i + 2], 16) for i in (0, 2, 4))

    im.putpixel((0, 0), tint(im.getpixel((0, 0)), color, args.gain))
    for x in range(3, 9):
        for y in range(im.height):
            im.putpixel((x, y), tint(im.getpixel((x, y)), color, args.gain))

    OUT.parent.mkdir(parents=True, exist_ok=True)
    im.save(OUT)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
