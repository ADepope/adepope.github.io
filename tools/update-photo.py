#!/usr/bin/env python3
"""Prepare a source photo for the site.

    python3 tools/update-photo.py <source-image> [--out images/portrait.jpg]
                                 [--size 760] [--focus 0.5,0.35] [--ratio 1:1]

Produces a cropped, web-optimised JPEG. --focus is the (x, y) fraction of the
source that should end up in the centre of the crop; the default sits a little
above centre, which is usually where a face is. --ratio is the output aspect
(1:1 for the hero portrait, 4:3 for the photo grid), and --size is the long edge.
"""
import argparse, os
from PIL import Image, ImageOps

ap = argparse.ArgumentParser()
ap.add_argument('source')
ap.add_argument('--out', default='images/portrait.jpg')
ap.add_argument('--size', type=int, default=760)
ap.add_argument('--focus', default='0.5,0.35')
ap.add_argument('--ratio', default='1:1',
                help="W:H to crop to, or 'none' to keep the source aspect")
ap.add_argument('--quality', type=int, default=86)
a = ap.parse_args()

fx, fy = (float(v) for v in a.focus.split(','))
im = ImageOps.exif_transpose(Image.open(a.source)).convert('RGB')
w, h = im.size

if a.ratio.lower() in ('none', 'native', 'keep'):
    cw, ch = w, h
else:
    rw, rh = (float(v) for v in a.ratio.replace('/', ':').split(':'))
    target = rw / rh
    # largest box of the requested aspect that fits inside the source
    cw, ch = (h * target, h) if w / h > target else (w, w / target)
    cw, ch = int(round(cw)), int(round(ch))
    left = min(max(int(w * fx - cw / 2), 0), w - cw)
    top = min(max(int(h * fy - ch / 2), 0), h - ch)
    im = im.crop((left, top, left + cw, top + ch))

scale = a.size / max(cw, ch)
im = im.resize((max(1, int(round(cw * scale))), max(1, int(round(ch * scale)))), Image.LANCZOS)

os.makedirs(os.path.dirname(a.out) or '.', exist_ok=True)
im.save(a.out, 'JPEG', quality=a.quality, optimize=True, progressive=True)
print(f'{a.source} {w}x{h} -> {a.out} {im.size[0]}x{im.size[1]} '
      f'({os.path.getsize(a.out) // 1024} KB)')
