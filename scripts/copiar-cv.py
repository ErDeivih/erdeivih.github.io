# -*- coding: utf-8 -*-
"""Copia el CV y su PDF (fuente: cv/) a public/ y les añade el icono del sitio."""
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ORIGEN_HTML = ROOT.parent / "cv" / "cv-print.html"
ORIGEN_PDF = ROOT.parent / "cv" / "CV.pdf"
DESTINO_HTML = ROOT / "public" / "cv.html"
DESTINO_PDF = ROOT / "public" / "David-Perez-Velasco-CV.pdf"

html = ORIGEN_HTML.read_text(encoding="utf-8")
if 'rel="icon"' not in html:
    html = html.replace('</title>', '</title>\n<link rel="icon" type="image/svg+xml" href="/favicon.svg">')
DESTINO_HTML.write_text(html, encoding="utf-8", newline="\n")
shutil.copyfile(ORIGEN_PDF, DESTINO_PDF)
print("CV copiado a", DESTINO_HTML, "y", DESTINO_PDF)
