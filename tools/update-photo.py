#!/usr/bin/env python3
"""Prepare a source photo for the site.

    python3 tools/update-photo.py <source-image> [--out images/portrait.jpg]
                                 [--size 760] [--focus 0.5,0.35]

Produces a square, web-optimised JPEG. --focus is the (x, y) fraction of the
source that should end up in the centre of the crop; the default sits a little
above centre, which is usually where a face is.
"""
import argparse, os
from PIL import Image, ImageOps

ap = argparse.ArgumentParser()
ap.add_argument('source')
ap.add_argument('--out', default='images/portrait.jpg')
ap.add_argument('--size', type=int, default=760)
ap.add_argument('--focus', default='0.5,0.35')
ap.add_argument('--quality', type=int, default=86)
a = ap.parse_args()

fx, fy = (float(v) for v in a.focus.split(','))
im = ImageOps.exif_transpose(Image.open(a.source)).convert('RGB')
w, h = im.size
side = min(w, h)

left = min(max(int(w * fx - side / 2), 0), w - side)
top = min(max(int(h * fy - side / 2), 0), h - side)
im = im.crop((left, top, left + side, top + side)).resize((a.size, a.size), Image.LANCZOS)

os.makedirs(os.path.dirname(a.out) or '.', exist_ok=True)
im.save(a.out, 'JPEG', quality=a.quality, optimize=True, progressive=True)
print(f'{a.source} {w}x{h} -> {a.out} {a.size}x{a.size} '
      f'({os.path.getsize(a.out) // 1024} KB)')
