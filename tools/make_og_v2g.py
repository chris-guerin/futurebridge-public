# -*- coding: utf-8 -*-
"""Render the LinkedIn/OG card for the V2G paper from its own V1G-vs-V2G chart.

Regenerate with:
    python tools/make_og_v2g.py
Writes og-v2g-europe.png (1200x630) at the repo root.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
WHITE, INK, GREY, DIM = (255, 255, 255), (11, 11, 11), (75, 75, 85), (111, 111, 121)
RED, INDIGO, INDIGO_PALE, GREEN = (248, 78, 93), (63, 67, 173), (201, 202, 232), (27, 143, 112)
TRACK = (240, 240, 242)

FONTS = 'C:/Windows/Fonts/'
def font(name, size):
    return ImageFont.truetype(os.path.join(FONTS, name), size)

bold = lambda s: font('arialbd.ttf', s)
reg = lambda s: font('arial.ttf', s)


def tracked(d, xy, text, f, fill, spacing):
    """Draw text with manual letter-spacing (PIL has none)."""
    x, y = xy
    for ch in text:
        d.text((x, y), ch, font=f, fill=fill)
        x += d.textlength(ch, font=f) + spacing
    return x


def bar(d, y, label, value, frac_solid, colour, frac_pale=None):
    d.text((90, y), label, font=reg(25), fill=INK)
    vw = d.textlength(value, font=bold(34))
    d.text((1110 - vw, y - 8), value, font=bold(34), fill=INK)
    top = y + 46
    d.rectangle([90, top, 1110, top + 30], fill=TRACK)
    span = 1020
    if frac_pale:
        d.rectangle([90, top, 90 + span * frac_pale, top + 30], fill=INDIGO_PALE)
    d.rectangle([90, top, 90 + span * frac_solid, top + 30], fill=colour)


img = Image.new('RGB', (W, H), WHITE)
d = ImageDraw.Draw(img)

# red rule across the top
d.rectangle([0, 0, W, 8], fill=RED)

# eyebrow
tracked(d, (90, 58), 'FUTUREBRIDGE SIGNALS  ·  VEHICLE-TO-GRID', bold(19), RED, 2.6)

# headline
d.text((90, 108), 'V2G is quoted against', font=bold(62), fill=INK)
d.text((90, 180), 'the wrong baseline.', font=bold(62), fill=INK)

# bars -- scaled to the GBP 850 top of the quoted V2G range
bar(d, 300, 'Intelligent Octopus Go  ·  smart one-way charging', '£771',
    771 / 850.0, GREEN)
bar(d, 424, 'Power Pack  ·  vehicle-to-grid', '£620–850',
    620 / 850.0, INDIGO, frac_pale=1.0)

# footnote
d.text((90, 538), "Octopus' own published figures, both against a standard variable tariff.",
       font=reg(21), fill=GREY)
d.text((90, 568), 'Not like-for-like — which is the point.', font=reg(21), fill=DIM)

# wordmark device, bottom right
bx, by = 1046, 548
for i, w in enumerate((64, 45, 28)):
    d.rectangle([bx, by + i * 15, bx + w, by + i * 15 + 9], fill=INK)

out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   'og-v2g-europe.png')
img.save(out, 'PNG', optimize=True)
print('wrote', out, img.size, os.path.getsize(out), 'bytes')
