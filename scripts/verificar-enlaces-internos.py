# -*- coding: utf-8 -*-
"""Comprueba en vivo todos los enlaces internos del porfolio y sus anclas.

Recorre las páginas del sitemap publicado, extrae los enlaces internos, los pide de verdad y
comprueba que las anclas (#...) existen en la página de destino. Devuelve recuento y fallos.
"""
import re
import sys
import urllib.error
import urllib.request
from urllib.parse import urljoin, urlparse

BASE = "https://erdeivih.github.io"
CAB = {"User-Agent": "verificador-enlaces/1.0", "Cache-Control": "no-cache"}


def pedir(url):
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=CAB), timeout=40) as r:
            return r.status, r.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as exc:
        return exc.code, ""
    except Exception:
        return 0, ""


def paginas_sitemap():
    code, xml = pedir(BASE + "/sitemap-0.xml")
    if code != 200:
        return ["/", "/proyectos/", "/datos/", "/analisis/", "/formacion/", "/en/"]
    rutas = re.findall(r"<loc>https://erdeivih\.github\.io([^<]*)</loc>", xml)
    return sorted(set(rutas or ["/"]))


enlaces = {}
paginas = paginas_sitemap()
for ruta in paginas:
    code, html = pedir(BASE + ruta)
    if code != 200:
        continue
    for href in re.findall(r'href="([^"]+)"', html):
        if href.startswith(("mailto:", "tel:", "javascript:")):
            continue
        absoluto = urljoin(BASE + ruta, href)
        if urlparse(absoluto).netloc != "erdeivih.github.io":
            continue
        enlaces.setdefault(absoluto, set()).add(ruta)

fallos = []
for url, origen in sorted(enlaces.items()):
    code, html = pedir(url.split("#")[0])
    if code != 200:
        fallos.append(f"{url} → {code} (desde {', '.join(sorted(origen))})")
        continue
    fragmento = url.split("#", 1)[1] if "#" in url else ""
    if fragmento and f'id="{fragmento}"' not in html and f'name="{fragmento}"' not in html:
        fallos.append(f"{url} → ancla #{fragmento} no existe")

print(f"páginas: {len(paginas)} · enlaces internos únicos: {len(enlaces)} · fallos: {len(fallos)}")
for f in fallos:
    print("  -", f)
sys.exit(1 if fallos else 0)
