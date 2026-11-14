# -*- coding: utf-8 -*-
"""Comprueba que `erdeivih.github.io` sirve exactamente lo que hay en `publicado/`.

Se publica en la raíz del sitio de usuario (rama `gh-pages` de `erdeivih.github.io`), no en
`/portfolio/` (esa ruta debe dar 404). Este script hace peticiones reales, compara el sha256 del
cuerpo con el fichero desplegado y falla si la web no está actualizada.

Uso:  python scripts/verificar-publicacion.py
"""
import hashlib
import sys
import urllib.error
import urllib.request
from pathlib import Path

BASE = "https://erdeivih.github.io"
PUBLICADO = Path(__file__).resolve().parent.parent.parent / "publicado"
CABECERAS = {"User-Agent": "verificador-publicacion/1.0", "Cache-Control": "no-cache", "Pragma": "no-cache"}

PAGINAS = [
    ("/", "index.html"),
    ("/proyectos/", "proyectos/index.html"),
    ("/formacion/", "formacion/index.html"),
    ("/datos/", "datos/index.html"),
    ("/analisis/", "analisis/index.html"),
    ("/en/", "en/index.html"),
    ("/David-Perez-Velasco-CV.pdf", "David-Perez-Velasco-CV.pdf"),
]


def descargar(ruta: str):
    req = urllib.request.Request(BASE + ruta, headers=CABECERAS)
    try:
        with urllib.request.urlopen(req, timeout=40) as r:
            return r.status, r.read(), r.headers.get("Content-Type", "")
    except urllib.error.HTTPError as exc:
        return exc.code, b"", exc.headers.get("Content-Type", "")
    except Exception:
        return 0, b"", ""


fallos = []
for ruta, fichero in PAGINAS:
    local = PUBLICADO / fichero
    if not local.is_file():
        fallos.append(f"no existe publicado/{fichero}")
        continue
    esperado = hashlib.sha256(local.read_bytes()).hexdigest()
    code, cuerpo, tipo = descargar(ruta)
    real = hashlib.sha256(cuerpo).hexdigest()
    ok = code == 200 and real == esperado
    print(f"{'OK ' if ok else 'MAL'} {code:3} {ruta:28} {tipo or '—'}")
    if code != 200:
        fallos.append(f"{ruta} responde {code}")
    elif real != esperado:
        fallos.append(f"{ruta} no sirve el build publicado (sha distinto)")

# La raíz es el sitio: /portfolio/ no debe existir.
code, _, _ = descargar("/portfolio/")
print(f"{'OK ' if code == 404 else 'MAL'} {code:3} /portfolio/ (debe dar 404)")
if code != 404:
    fallos.append(f"/portfolio/ responde {code} (debe ser 404: el sitio vive en la raíz)")

# Las dos secciones nuevas deben estar en la web, no solo en el build.
_, proyectos_html, _ = descargar("/proyectos/")
_, formacion_html, _ = descargar("/formacion/")
texto_proyectos = proyectos_html.decode("utf-8", "replace")
texto_formacion = formacion_html.decode("utf-8", "replace")
MARCHA = ["Proyectos en marcha", "Lyfta (Garmin)", "Fondo Popular (FACYLF)", "Cesta", "CUE Digital",
          "EntrenoLab", "OpoFuente", "Data School", "Datos · finanzas", "Datos · Fórmula 1", "Datos · fútbol"]
CURSOS = ["Introduction to Data Science", "Pandas", "Intro to Machine Learning", "Intro to SQL",
          "Google Analytics 4", "DP-900"]
for texto in MARCHA:
    if texto not in texto_proyectos:
        fallos.append(f"/proyectos/ no muestra «{texto}»")
for texto in CURSOS:
    if texto not in texto_formacion:
        fallos.append(f"/formacion/ no muestra el curso «{texto}»")
for marca in ("Certificado gratuito", "Badge gratuito al completarlo", "examen de pago"):
    if marca not in texto_formacion:
        fallos.append(f"/formacion/ no muestra la marca «{marca}»")
print(f"{'OK ' if not any('no muestra' in f for f in fallos) else 'MAL'} secciones: proyectos en marcha ({len(MARCHA)} líneas) y formación ({len(CURSOS)} cursos)")

if fallos:
    print(f"ROJO: {len(fallos)} problema(s)")
    for f in fallos:
        print("  -", f)
    sys.exit(1)
print("VERDE: la raíz de erdeivih.github.io sirve el build de publicado/ y /portfolio/ da 404")
