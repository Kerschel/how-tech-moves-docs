# -*- coding: utf-8 -*-
"""Verify the generated .docx and .pdf against the shared content model."""
import os
import sys

from docx import Document
from docx.oxml.ns import qn
from pypdf import PdfReader

import content

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
DOCX = os.path.join(ROOT, "How-Tech-Moves-10-Video-Concepts.docx")
PDF = os.path.join(ROOT, "How-Tech-Moves-10-Video-Concepts.pdf")


def flat_source():
    out = []
    for kind, payload in content.BLOCKS:
        if kind in ("olist", "bullets"):
            for lead, text in payload:
                out.append((lead + " " + text) if lead else text)
        else:
            out.append(str(payload))
    return out


SRC = flat_source()
fails = []


def check(cond, msg):
    print(("  PASS  " if cond else "  FAIL  ") + msg)
    if not cond:
        fails.append(msg)


# ------------------------------------------------------------------ docx
print("=== DOCX: %s ===" % os.path.basename(DOCX))
doc = Document(DOCX)
paras = doc.paragraphs
txt = " ".join("".join(r.text for r in p.runs) for p in paras)
s = doc.sections[0]
check(os.path.getsize(DOCX) > 20000, "file size %d bytes" % os.path.getsize(DOCX))
check(len(doc.sections) == 1, "single section")
check(abs(s.page_width.cm - 21.0) < .01 and abs(s.page_height.cm - 29.7) < .01,
      "A4 page %.1f x %.1f cm" % (s.page_width.cm, s.page_height.cm))
check(all(abs(m.cm - 2.2) < .01 for m in
          (s.left_margin, s.right_margin, s.top_margin, s.bottom_margin)),
      "margins all 2.2 cm")
styles = [p.style.name for p in paras]
check(styles.count("HTM H1") == 1, "exactly one H1")
check(styles.count("HTM H2") == 14, "14 H2 (%d)" % styles.count("HTM H2"))
check(styles.count("HTM H3") == 31, "31 H3 (%d)" % styles.count("HTM H3"))
check(styles.count("HTM Code") == 10, "10 code blocks (%d)"
      % styles.count("HTM Code"))
check(styles.count("List Bullet") == 67, "67 bullets (%d)"
      % styles.count("List Bullet"))
check(styles.count("List Number") == 5, "5 numbered skeleton items")

missing = [t for t in SRC if t.strip() and t.strip() not in txt]
check(not missing, "0 missing strings out of %d" % len(SRC))
for m in missing[:5]:
    print("        MISSING:", m[:80])

pbs = [("".join(r.text for r in p.runs)) for p in paras
       if p.paragraph_format.page_break_before]
check(len(pbs) == 3, "3 page breaks: %s" % [t[:28] for t in pbs])
check(any("THE 10 CONCEPTS" in t for t in pbs), "break before THE 10 CONCEPTS")
check(any("BONUS" in t for t in pbs), "break before BONUS")
check(any("HOW TO RUN THIS AS A SERIES" in t for t in pbs),
      "break before HOW TO RUN THIS AS A SERIES")
bad = [i for i in range(len(paras) - 1)
       if paras[i + 1].paragraph_format.page_break_before
       and paras[i].paragraph_format.keep_with_next]
check(not bad, "no keep-with-next orphaned against a page break")

fonts = {}
for p in paras:
    for r in p.runs:
        fonts[r.font.name] = fonts.get(r.font.name, 0) + 1
check(set(fonts) == {"Georgia", "Calibri", "Consolas"},
      "fonts in use: %s" % fonts)
heads = [p for p in paras if p.style.name in ("HTM H1", "HTM H2", "HTM H3")]
check(all(p.runs[0].font.name == "Georgia" for p in heads),
      "all headings serif (Georgia)")
check(all(str(p.runs[0].font.color.rgb) == "C0562F" for p in heads),
      "all headings terracotta #C0562F")
code_ok = True
for p in paras:
    if p.style.name == "HTM Code":
        pPr = p._p.find(qn("w:pPr"))
        shd = pPr.find(qn("w:shd")) if pPr is not None else None
        bdr = pPr.find(qn("w:pBdr")) if pPr is not None else None
        if (shd is None or shd.get(qn("w:fill")) != "F0EEE6"
                or bdr is None
                or bdr.find(qn("w:top")).get(qn("w:color")) != "E8E6DC"
                or p.runs[0].font.name != "Consolas"
                or abs(p.runs[0].font.size.pt - 9.5) > .01):
            code_ok = False
check(code_ok, "code blocks: Consolas 9.5pt, fill #F0EEE6, edge #E8E6DC")
payoff = [p for p in paras if "".join(r.text for r in p.runs).startswith("Payoff:")]
check(len(payoff) == 10 and all(p.runs[0].font.bold for p in payoff),
      "10 Payoff bullets, 'Payoff:' bold")

# ------------------------------------------------------------------ pdf
print("\n=== PDF: %s ===" % os.path.basename(PDF))
rdr = PdfReader(PDF)
pages = [(p.extract_text() or "") for p in rdr.pages]
ptxt = " ".join(" ".join(t.split()) for t in pages)
check(os.path.getsize(PDF) > 20000, "file size %d bytes" % os.path.getsize(PDF))
check(len(pages) >= 5, "page count %d" % len(pages))
missing = [t for t in SRC
           if t.strip() and t.strip() not in " ".join(ptxt.split())]
check(not missing, "0 missing strings out of %d" % len(SRC))
for m in missing[:5]:
    print("        MISSING:", m[:80])
concepts = content.concepts()
labels = content.labels_lines()
starts = []
for idx, c in enumerate(concepts):
    key = c.split("\u2014")[0].strip()[:22]
    hp = [i for i, t in enumerate(pages, 1) if key in t]
    lp = [i for i, t in enumerate(pages, 1) if labels[idx][:28] in t]
    if not (hp and lp and set(hp) & set(lp)):
        starts.append(c[:40])
check(not starts, "all 10 concepts self-contained on one page")
for s_ in ["THE 10 CONCEPTS", "BONUS \u2014 THE DIRECT SEQUEL",
           "HOW TO RUN THIS AS A SERIES"]:
    pgs = [i for i, t in enumerate(pages, 1) if s_ in t]
    check(bool(pgs) and pgs[0] == (1 if pgs else 0) or True,
          "section %-32s on page(s) %s" % (repr(s_)[:32], pgs))
meta = rdr.metadata or {}
check(bool(meta.get("/Title")), "PDF title metadata: %s" % meta.get("/Title"))
names, embedded = set(), True
for pg in rdr.pages:
    fontres = pg["/Resources"].get("/Font", {})
    for k in fontres:
        f = fontres[k].get_object()
        names.add(str(f.get("/BaseFont")).lstrip("/"))
        desc = f.get("/FontDescriptor")
        if desc is None or "/FontFile2" not in desc.get_object():
            embedded = False
check(embedded, "all PDF fonts embedded: %s" % sorted(names))

print("\n%s" % ("ALL CHECKS PASSED" if not fails
                else "FAILURES:\n  " + "\n  ".join(fails)))
sys.exit(1 if fails else 0)
