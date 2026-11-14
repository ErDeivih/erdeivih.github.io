# -*- coding: utf-8 -*-
"""Copia el CV bueno (el del Escritorio) al sitio como /David-Perez-Velasco-CV.pdf."""
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ORIGEN = Path(r"C:\Users\David\OneDrive\Escritorio\David_Pérez_Velasco_CV.pdf")
DESTINO = ROOT / "public" / "David-Perez-Velasco-CV.pdf"

shutil.copyfile(ORIGEN, DESTINO)
print("CV copiado:", DESTINO, DESTINO.stat().st_size, "bytes")
