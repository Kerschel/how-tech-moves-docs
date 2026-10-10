# -*- coding: utf-8 -*-
"""Build How-Tech-Moves-10-Video-Concepts.pdf from the shared content model."""
import os

from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, Frame, PageTemplate, Paragraph,
                                Spacer, PageBreak, KeepTogether, HRFlowable)

import content

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.abspath(os.path.join(
    HERE, "..", "How-Tech-Moves-10-Video-Concepts.pdf"))

# ---------------------------------------------------------------- fonts
# Preferred: DejaVu Serif / DejaVu Sans / DejaVu Sans Mono, if the TTFs are on
# the box (matplotlib ships them). Fallback documented in the README.
TTF_DIR = None
for cand in [
    "/usr/local/lib/python3.12/dist-packages/matplotlib/mpl-data/fonts/ttf",
    "/usr/share/fonts/truetype/dejavu",
]:
    if os.path.exists(os.path.join(cand, "DejaVuSerif.ttf")):
        TTF_DIR = cand
        break
if TTF_DIR is None:
    import matplotlib
    TTF_DIR = os.path.join(os.path.dirname(matplotlib.__file__),
                           "mpl-data", "fonts", "ttf")

FONTS = {
    "Serif": "DejaVuSerif.ttf",
    "Serif-Bold": "DejaVuSerif-Bold.ttf",
    "Serif-Italic": "DejaVuSerif-Italic.ttf",
    "Sans": "DejaVuSans.ttf",
    "Sans-Bold": "DejaVuSans-Bold.ttf",
    "Sans-Oblique": "DejaVuSans-Oblique.ttf",
    "Mono": "DejaVuSansMono.ttf",
    "Mono-Bold": "DejaVuSansMono-Bold.ttf",
}
for name, fn in FONTS.items():
    path = os.path.join(TTF_DIR, fn)
    if os.path.exists(path):
        pdfmetrics.registerFont(TTFont(name, path))
pdfmetrics.registerFontFamily("Serif", normal="Serif", bold="Serif-Bold",
                              italic="Serif-Italic", boldItalic="Serif-Bold")
pdfmetrics.registerFontFamily("Sans", normal="Sans", bold="Sans-Bold",
                              italic="Sans-Oblique", boldItalic="Sans-Bold")
pdfmetrics.registerFontFamily("Mono", normal="Mono", bold="Mono-Bold",
                              italic="Mono", boldItalic="Mono-Bold")

# reportlab stamps an initial font resource on every page even when nothing is
# drawn with it; point that at an embedded face so the PDF lists no base-14
# font at all (clean for print/prepress).
from reportlab import rl_config          # noqa: E402
rl_config.canvas_basefontname = "Sans"

# ---------------------------------------------------------------- tokens
BODY_C = HexColor("#1F1E1D")
ACCENT = HexColor("#C0562F")
META_C = HexColor("#6B6A66")
HAIRLINE = HexColor("#DEDCD1")
CODE_BG = HexColor("#F0EEE6")
CODE_EDGE = HexColor("#E8E6DC")

MARGIN = 2.2 * cm
PAGE_W, PAGE_H = A4
TEXT_W = PAGE_W - 2 * MARGIN
FRAME_H = PAGE_H - 2 * MARGIN

# ---------------------------------------------------------------- styles
S_H1 = ParagraphStyle("h1", fontName="Serif-Bold", fontSize=23, leading=27,
                      textColor=ACCENT, spaceAfter=8, keepWithNext=1,
                      alignment=TA_LEFT)
S_SUB = ParagraphStyle("sub", fontName="Sans", fontSize=12.5, leading=17,
                       textColor=META_C, spaceAfter=4, keepWithNext=1)
S_H2 = ParagraphStyle("h2", fontName="Serif-Bold", fontSize=13.5, leading=17,
                      textColor=ACCENT, spaceBefore=20, spaceAfter=7,
                      keepWithNext=1)
S_H3 = ParagraphStyle("h3", fontName="Serif-Bold", fontSize=10.8, leading=14,
                      textColor=ACCENT, spaceBefore=11, spaceAfter=3,
                      keepWithNext=1)
S_BODY = ParagraphStyle("body", fontName="Sans", fontSize=10, leading=13.2,
                        textColor=BODY_C, spaceAfter=8)
S_LEAD = ParagraphStyle("lead", fontName="Sans-Bold", fontSize=10, leading=13.2,
                        textColor=BODY_C, spaceBefore=4, spaceAfter=5,
                        keepWithNext=1)
S_BULLET = ParagraphStyle("bullet", fontName="Sans", fontSize=10, leading=13,
                          textColor=BODY_C, spaceAfter=4.5, leftIndent=16,
                          bulletIndent=4, bulletFontName="Sans",
                          bulletFontSize=10)
S_NUM = ParagraphStyle("num", fontName="Sans", fontSize=10, leading=13,
                       textColor=BODY_C, spaceAfter=4.5, leftIndent=18,
                       bulletIndent=3, bulletFontName="Sans", bulletFontSize=10)

# code block: largest size in 8.6-9.5pt that keeps the longest label on one line
LABELS = content.labels_lines()
PAD = 7.0
avail = TEXT_W - 2 * PAD - 1
CODE_SIZE = 8.6
for size in [9.5, 9.4, 9.3, 9.2, 9.1, 9.0, 8.9, 8.8, 8.7, 8.6]:
    widest = max(pdfmetrics.stringWidth(t, "Mono", size) for t in LABELS)
    if widest <= avail:
        CODE_SIZE = size
        break

code_kwargs = dict(fontName="Mono", fontSize=CODE_SIZE,
                   leading=CODE_SIZE * 1.38, textColor=BODY_C,
                   backColor=CODE_BG, borderColor=CODE_EDGE, borderWidth=0.6,
                   borderPadding=PAD, spaceBefore=9, spaceAfter=13,
                   leftIndent=0, rightIndent=0)
if "borderRadius" in ParagraphStyle.defaults:
    code_kwargs["borderRadius"] = 5.5      # ~8px soft radius
S_CODE = ParagraphStyle("code", **code_kwargs)


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


# ---------------------------------------------------------------- build story
# Blocks accumulate into a "group" (a section). A group closes when the next
# H2 arrives, and is emitted wrapped in KeepTogether so a section that fits on
# one page is not split across a page boundary.
story = []
cur = []


def flush():
    global cur
    if not cur:
        return
    if len(cur) > 1:
        story.append(KeepTogether(cur))
    else:
        story.extend(cur)
    cur = []


pending_break = False

for kind, payload in content.BLOCKS:

    if kind == "pagebreak":
        pending_break = True
        continue

    if kind == "h2":
        flush()
        if pending_break:
            story.append(PageBreak())
            pending_break = False
        cur.append(Paragraph(esc(payload), S_H2))

    elif kind == "h1":
        cur.append(Paragraph(esc(payload), S_H1))

    elif kind == "subtitle":
        cur.append(Paragraph(esc(payload), S_SUB))

    elif kind == "rule":
        cur.append(Spacer(1, 12))
        cur.append(HRFlowable(width="100%", thickness=0.6, color=HAIRLINE,
                              spaceBefore=0, spaceAfter=8))

    elif kind == "h3":
        cur.append(Paragraph(esc(payload), S_H3))

    elif kind == "body":
        cur.append(Paragraph(esc(payload), S_BODY))

    elif kind == "lead":
        cur.append(Paragraph(esc(payload), S_LEAD))

    elif kind in ("olist", "bullets"):
        for i, (lead, text) in enumerate(payload, 1):
            html = ("<b>%s</b> %s" % (esc(lead), esc(text))) if lead else esc(text)
            if kind == "olist":
                cur.append(Paragraph(html, S_NUM, bulletText="%d." % i))
            else:
                cur.append(Paragraph(html, S_BULLET, bulletText="\u2022"))

    elif kind == "code":
        cur.append(Paragraph(esc(payload), S_CODE))

flush()


# ---------------------------------------------------------------- doc template
def footer(canv, doc):
    canv.saveState()
    canv.setFont("Sans", 8)
    canv.setFillColor(META_C)
    canv.drawCentredString(PAGE_W / 2.0, 1.15 * cm, str(canv.getPageNumber()))
    canv.restoreState()


doc = BaseDocTemplate(OUT, pagesize=A4,
                      leftMargin=MARGIN, rightMargin=MARGIN,
                      topMargin=MARGIN, bottomMargin=MARGIN,
                      title="How Tech Moves \u2014 10 Cinematic Video Concepts",
                      author="How Tech Moves", subject="Video concepts",
                      creator="How Tech Moves")
frame = Frame(MARGIN, MARGIN, TEXT_W, FRAME_H, id="body",
              leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
doc.addPageTemplates([PageTemplate(id="all", frames=[frame], onPage=footer)])
doc.build(story)

print("wrote", OUT, os.path.getsize(OUT), "bytes")
print("code block font size used:", CODE_SIZE, "pt")
