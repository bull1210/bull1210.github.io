#!/usr/bin/env python3
"""Render one Pinterest pin (1000 x 1500) per guide into assets/pins/<slug>.jpg.

The headline is the guide's title, the picture is the guide's screenshot from assets/shots/ (or the
sunflower icon when it has none), and the footer says "Free on Google Play". Run from the repo root:

  python tools/pins.py            # every guide
  python tools/pins.py hide-photos-vault
"""
from __future__ import annotations

import glob
import os
import re
import sys

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
W, H = 1000, 1500
INDIGO, TEAL = (63, 81, 181), (0, 137, 123)
BOLD = "C:/Windows/Fonts/segoeuib.ttf"
REG = "C:/Windows/Fonts/segoeui.ttf"
# Guides without a screenshot of their own borrow one, or show the icon.
FALLBACK = {  # plain phone captures from docs/store/raw of the nearest screen
    "backup-photo-app-settings": "raw/05_ai",
    "find-receipts-in-photos": "raw/05_ai",
    "hide-photos-vault": "raw/05_ai",
    "photo-collage-without-cropping": "raw/06_movie",
    "xiaomi-photos-no-location": "raw/03_moments",
}


def gradient() -> Image.Image:
    im = Image.new("RGB", (W, H))
    px = im.load()
    for y in range(H):
        t = y / (H - 1)
        for x in range(W):
            u = (t * 0.7 + x / W * 0.3)
            px[x, y] = tuple(int(INDIGO[i] + (TEAL[i] - INDIGO[i]) * u) for i in range(3))
    return im


def wrap(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont, width: int) -> list[str]:
    lines, line = [], ""
    for word in text.split():
        trial = (line + " " + word).strip()
        if draw.textlength(trial, font=font) <= width:
            line = trial
        else:
            lines.append(line)
            line = word
    if line:
        lines.append(line)
    return lines


def rounded(im: Image.Image, radius: int) -> Image.Image:
    mask = Image.new("L", im.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, im.width - 1, im.height - 1], radius, fill=255)
    out = im.convert("RGBA")
    out.putalpha(mask)
    return out


def render(slug: str, title: str, shot: str | None) -> str:
    im = gradient()
    draw = ImageDraw.Draw(im)
    margin = 70
    # Headline: shrink the font until it fits in five lines.
    size = 78
    while True:
        font = ImageFont.truetype(BOLD, size)
        lines = wrap(draw, title, font, W - 2 * margin)
        if len(lines) <= 5 or size <= 52:
            break
        size -= 4
    y = 90
    for line in lines:
        draw.text((margin, y), line, font=font, fill="white")
        y += int(size * 1.22)
    top = y + 40
    # Footer.
    foot_font = ImageFont.truetype(REG, 38)
    icon = Image.open(os.path.join(ROOT, "assets", "icon.png")).convert("RGBA").resize((72, 72))
    foot_y = H - 70 - 72
    im.paste(icon, (margin, foot_y), icon)
    draw.text((margin + 92, foot_y + 4), "PixOrg", font=ImageFont.truetype(BOLD, 40), fill="white")
    draw.text((margin + 92, foot_y + 46), "Free on Google Play", font=ImageFont.truetype(REG, 26), fill=(230, 230, 245))
    # Picture.
    bottom = foot_y - 50
    if shot:
        src = Image.open(shot).convert("RGB")
        ph = bottom - top
        pw = int(src.width * ph / src.height)
        if pw > W - 2 * margin:
            pw = W - 2 * margin
            ph = int(src.height * pw / src.width)
        pic = rounded(src.resize((pw, ph), Image.LANCZOS), 40)
        x = (W - pw) // 2
        shadow = Image.new("RGBA", (pw + 80, ph + 80), (0, 0, 0, 0))
        ImageDraw.Draw(shadow).rounded_rectangle([40, 50, pw + 40, ph + 50], 40, fill=(0, 0, 0, 110))
        shadow = shadow.filter(ImageFilter.GaussianBlur(22))
        im.paste(shadow, (x - 40, top - 40), shadow)
        im.paste(pic, (x, top), pic)
    else:
        big = Image.open(os.path.join(ROOT, "assets", "pixorg-card.png")).convert("RGB")
        pw = W - 2 * margin
        ph = int(big.height * pw / big.width)
        pic = rounded(big.resize((pw, ph), Image.LANCZOS), 40)
        im.paste(pic, (margin, top + (bottom - top - ph) // 2), pic)
    out = os.path.join(ROOT, "assets", "pins", f"{slug}.jpg")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    im.save(out, quality=88, optimize=True)
    return out


def main() -> int:
    want = set(sys.argv[1:])
    raw = "E:/apps/AndroidPhotoApp/docs/store/screenshots"
    for path in sorted(glob.glob(os.path.join(ROOT, "_guides", "*.md"))):
        slug = os.path.splitext(os.path.basename(path))[0]
        if want and slug not in want:
            continue
        text = open(path, encoding="utf-8").read()
        title = re.search(r"^title: (.*)$", text, re.M).group(1).strip().strip('"')
        m = re.search(r"^image: /assets/shots/(\w+)\.jpg$", text, re.M)
        name = m.group(1) if m else FALLBACK.get(slug)
        shot = None
        if name and name.startswith("raw/"):
            shot = os.path.join(raw, "..", "raw", name[4:] + ".png")
        elif name:
            full = os.path.join(raw, f"{name}.png")  # the 1080 px original when the PicOrg repo is beside us
            shot = full if os.path.exists(full) else os.path.join(ROOT, "assets", "shots", f"{name}.jpg")
        print(os.path.relpath(render(slug, title, shot), ROOT))
    return 0


if __name__ == "__main__":
    sys.exit(main())
