# -*- coding: utf-8 -*-
"""Puerta de contenido del posicionamiento.

Comprueba que el sitio publicado con `pnpm build`:
  1. tiene exactamente los proyectos de perfil previstos (y ninguno de los retirados);
  2. no contiene frases de Business Analyst / BI ni tics de IA en el texto visible;
  3. conserva las páginas del sitio: portada, proyectos, datos, inglés y CV en PDF;
  4. no enlaza la vieja /cv.html y sí enlaza el PDF del CV.

Uso:  python scripts/verificar-contenido.py
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
DIST = ROOT / "dist"

PROYECTOS = {
    "compra-alimentacion", "cue-digital", "data-school", "documentchain",
    "entrenolab", "facylf", "garmin", "munipay", "opofuente",
}
RETIRADOS = {"panel", "impresion3d", "cdmplab", "chollos", "airport-fx"}
FRASES = [
    "Business Analyst", "Data Analyst", "business analyst", "inteligencia de negocio",
    "enlaces y demos comprobados", "Enlaces y demos comprobados",
]
# «BI» suelto, no dentro de palabras como «BIBLIOTECA»
BI_SUELTO = re.compile(r"\bBI\b")

fallos = []

# 1) proyectos
actuales = {p.name for p in (SRC / "content" / "projects").iterdir() if p.is_dir()}
if actuales != PROYECTOS:
    fallos.append(f"proyectos en src: {sorted(actuales)} (esperados {sorted(PROYECTOS)})")
for slug in RETIRADOS:
    if (SRC / "content" / "projects" / slug).exists():
        fallos.append(f"proyecto retirado presente en src: {slug}")
    if (ROOT / "public" / "projects" / slug).exists():
        fallos.append(f"capturas del proyecto retirado: {slug}")

# 2) frases en fuente y en HTML construido
for base in (SRC, DIST):
    for path in base.rglob("*"):
        if path.suffix not in (".ts", ".astro", ".mdx", ".html", ".json"):
            continue
        if "node_modules" in str(path):
            continue
        texto = path.read_text(encoding="utf-8", errors="replace")
        for frase in FRASES:
            if frase in texto:
                fallos.append(f"{path.relative_to(ROOT)}: contiene «{frase}»")
        if base == DIST and BI_SUELTO.search(texto):
            fallos.append(f"{path.relative_to(ROOT)}: contiene «BI» suelto")

# 3) páginas
for ruta in ("index.html", "proyectos/index.html", "analisis/index.html",
             "en/index.html", "en/analisis/index.html", "David-Perez-Velasco-CV.pdf"):
    if not (DIST / ruta).exists():
        fallos.append(f"falta {ruta} en dist")

# 4) imágenes: todo fichero de public/projects y public/analisis debe estar referenciado
referenciados = set()
for path in list(SRC.rglob("*.mdx")) + list(SRC.rglob("*.ts")) + list(SRC.rglob("*.astro")):
    if "node_modules" in str(path):
        continue
    texto = path.read_text(encoding="utf-8", errors="replace")
    referenciados.update(re.findall(r'/(?:projects|analisis)/[A-Za-z0-9._/-]+', texto))
for carpeta in ("projects", "analisis"):
    for fichero in (ROOT / "public" / carpeta).rglob("*"):
        if fichero.is_file():
            rel = "/" + fichero.relative_to(ROOT / "public").as_posix()
            if rel not in referenciados:
                fallos.append(f"imagen sin referencia en el contenido: {rel}")
for rel in referenciados:
    if not (ROOT / "public" / rel.lstrip("/")).is_file():
        fallos.append(f"imagen referenciada y ausente: {rel}")

# 5) CV
html = "\n".join(p.read_text(encoding="utf-8", errors="replace") for p in DIST.rglob("*.html"))
if "/cv.html" in html:
    fallos.append("queda un enlace a /cv.html")
if "/David-Perez-Velasco-CV.pdf" not in html:
    fallos.append("ninguna página enlaza el PDF del CV")

if fallos:
    print(f"ROJO: {len(fallos)} problema(s)")
    for f in fallos:
        print("  -", f)
    sys.exit(1)
print("VERDE: 9 proyectos de perfil, sin frases de BA/BI, páginas y CV en su sitio")
