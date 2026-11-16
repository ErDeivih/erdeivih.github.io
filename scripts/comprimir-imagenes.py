# -*- coding: utf-8 -*-
"""Comprime las imágenes del sitio que pasen de 200 KB, sin cambiar sus dimensiones.

PNG: cuantiza a 256 colores y guarda optimizado. og.png se limita a 1200×630.
Uso: python scripts/comprimir-imagenes.py [--seco]
"""
import sys
from pathlib import Path
from PIL import Image

LIMITE = 200 * 1024
PUBLIC = Path(__file__).resolve().parent.parent / "public"
seco = "--seco" in sys.argv


def peso_kb(n):
    return round(n / 1024)


for img in sorted(PUBLIC.rglob("*.png")):
    peso = img.stat().st_size
    if img.name == "og.png":
        with Image.open(img) as im:
            im = im.convert("RGB")
            im.thumbnail((1200, 630), Image.LANCZOS)
            if not seco:
                im.save(PUBLIC / "og.jpg", "JPEG", quality=82, optimize=True, progressive=True)
        print(f"og.png → og.jpg {peso_kb((PUBLIC / 'og.jpg').stat().st_size)} KB")
        continue
    if peso <= LIMITE:
        continue
    with Image.open(img) as im:
        im = im.convert("RGB").quantize(colors=256, method=Image.MEDIANCUT)
        if not seco:
            im.save(img, optimize=True)
    print(f"{img.relative_to(PUBLIC)} {peso_kb(peso)} → {peso_kb(img.stat().st_size)} KB")
