# How Tech Moves — 10 Cinematic Video Concepts

Typeset deliverables for the ten-video concept document.

## Files (repo root)

| File | Size | Description |
| --- | --- | --- |
| `How-Tech-Moves-10-Video-Concepts.docx` | 44.3 KB | Editable Word document |
| `How-Tech-Moves-10-Video-Concepts.pdf` | 98.6 KB | print-ready PDF, A4, 9 pages |

## Design

- A4, 2.2 cm margins, single column.
- Serif headings + humanist sans body: Georgia / Calibri (docx), DejaVu Serif / DejaVu Sans (pdf).
- Body `#1F1E1D`, headings `#C0562F`, meta text `#6B6A66`, hairlines `#DEDCD1`.
- Monospace `Labels:` blocks on a tinted `#F0EEE6` panel with a `#E8E6DC` hairline border.
- Page breaks before **THE 10 CONCEPTS**, **BONUS**, and **HOW TO RUN THIS AS A SERIES**.
  Each of the ten concepts is kept on a single page.

## Regenerating

Both files come from one shared content model, so they cannot drift apart.

```bash
pip install --break-system-packages python-docx reportlab matplotlib pypdf
python3 src/build_docx.py     # writes the .docx into the repo root
python3 src/build_pdf.py      # writes the .pdf into the repo root
python3 src/verify.py         # structural + verbatim checks on both files
```

`src/content.py` holds the approved copy verbatim. Do not edit the wording
without re-approval; the build and verify scripts assert that every string in
the model appears in both output files.
