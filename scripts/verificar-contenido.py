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
    "Datos y BI",
    "Business Analyst /",
    "prácticas como Business",
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
for ruta in ("index.html", "proyectos/index.html", "analisis/index.html", "datos/index.html", "datos/data-school-01/index.html", "formacion/index.html", "en/datos/index.html", "en/datos/data-school-01/index.html", "en/formacion/index.html",
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

# 5) presentación escrita y marcada como pendiente
presentacion = ROOT.parent / "PRESENTACION.md"
if not presentacion.exists():
    fallos.append("falta PRESENTACION.md en la raíz del proyecto")
else:
    texto_pres = presentacion.read_text(encoding="utf-8", errors="replace")
    if "pendiente del visto bueno" not in texto_pres.lower():
        fallos.append("PRESENTACION.md no está marcada como pendiente del visto bueno")

# 6) fichas de datos: tres huecos con la estructura fija de seis secciones
fichas = sorted((SRC / "content" / "datos").glob("*/index.mdx"))
if len(fichas) != 3:
    fallos.append(f"fichas de datos: {len(fichas)} (se esperan 3)")
SECCIONES = ["Pregunta", "Datos", "Proceso", "Hallazgo", "Qué aprendí", "Conceptos"]
for ficha in fichas:
    texto = ficha.read_text(encoding="utf-8", errors="replace")
    for seccion in SECCIONES:
        if f"## {seccion}" not in texto:
            fallos.append(f"{ficha.relative_to(ROOT)}: falta la sección «{seccion}»")

# 7) proyectos en marcha: la sección debe estar y no inventar fechas
proyectos_html = (DIST / "proyectos" / "index.html").read_text(encoding="utf-8", errors="replace")
EN_MARCHA = [
    "Proyectos en marcha", "Lyfta (Garmin)", "Fondo Popular (FACYLF)", "Cesta", "CUE Digital",
    "EntrenoLab", "OpoFuente", "Data School", "Datos · finanzas", "Datos · Fórmula 1", "Datos · fútbol",
]
for texto in EN_MARCHA:
    if texto not in proyectos_html:
        fallos.append(f"/proyectos/: falta «{texto}» en la sección de proyectos en marcha")
for texto in ("En desarrollo", "En preparación"):
    if texto not in proyectos_html:
        fallos.append(f"/proyectos/: falta el estado «{texto}»")

# 8) formación: seis cursos y marcas de certificado/coste
formacion_html = (DIST / "formacion" / "index.html").read_text(encoding="utf-8", errors="replace")
CURSOS = [
    "Introduction to Data Science", "Pandas", "Intro to Machine Learning", "Intro to SQL",
    "Google Analytics 4", "DP-900",
]
for curso in CURSOS:
    if curso not in formacion_html:
        fallos.append(f"/formacion/: falta el curso «{curso}»")
for texto in ("Certificado gratuito", "Badge gratuito al completarlo", "examen de pago"):
    if texto not in formacion_html:
        fallos.append(f"/formacion/: falta la marca «{texto}»")

# 9) la línea en versalitas de Salamanca no vuelve
inicio = (DIST / "index.html").read_text(encoding="utf-8", errors="replace")
for prohibido in ("Salamanca · Máster", "Salamanca · Master"):
    if prohibido in inicio:
        fallos.append(f"la portada vuelve a mostrar la línea en versalitas «{prohibido}»")

# 10) CV enlazado y PDF real
html = "\n".join(p.read_text(encoding="utf-8", errors="replace") for p in DIST.rglob("*.html"))
if "/cv.html" in html:
    fallos.append("queda un enlace a /cv.html")
if "/David-Perez-Velasco-CV.pdf" not in html:
    fallos.append("ninguna página enlaza el PDF del CV")
if 'href="/David-Perez-Velasco-CV.pdf"' not in (DIST / "index.html").read_text(encoding="utf-8", errors="replace"):
    fallos.append("la portada no enlaza el PDF del CV")
if 'href="/David-Perez-Velasco-CV.pdf"' not in (DIST / "404.html").read_text(encoding="utf-8", errors="replace"):
    fallos.append("la página 404 no enlaza el PDF del CV")
cv = ROOT / "public" / "David-Perez-Velasco-CV.pdf"
if not cv.is_file():
    fallos.append("falta public/David-Perez-Velasco-CV.pdf")
elif not cv.read_bytes().startswith(b"%PDF-"):
    fallos.append("public/David-Perez-Velasco-CV.pdf no es un PDF")
elif cv.stat().st_size < 100_000:
    fallos.append(f"el PDF del CV parece vacío ({cv.stat().st_size} bytes)")

if fallos:
    print(f"ROJO: {len(fallos)} problema(s)")
    for f in fallos:
        print("  -", f)
    sys.exit(1)
print("VERDE: 9 proyectos de perfil, sin frases de BA/BI, páginas y CV en su sitio")
