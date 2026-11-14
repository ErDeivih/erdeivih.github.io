# -*- coding: utf-8 -*-
"""Capturas reales de las demos publicadas (Playwright con el Edge del sistema).

Cada demo se abre en 1280x900 y la pantalla principal también en 390x844. Las capturas se guardan
en public/projects/<slug>/ y su origen, fecha y pie de foto en src/data/capturas.json.

Uso:  python scripts/capturar-demos.py [slug ...]
Requisitos: Edge instalado, playwright de Python.
"""
import json
import sys
from datetime import date
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "public" / "projects"
META = ROOT / "src" / "data" / "capturas.json"

BASE = "https://erdeivih.github.io/"
DEMOS = {
    "facylf": {
        "titulo": "Fondo Popular",
        "shots": [
            ("01-inicio", BASE + "fondo-popular-demo/", None, "Búsqueda de equipos, jugadores y clubes con acceso a las competiciones de la temporada."),
            ("02-competiciones", BASE + "fondo-popular-demo/explorar/competiciones/", None, "Selector de competiciones por temporada, categoría, modalidad y provincia."),
            ("03-clasificacion", BASE + "fondo-popular-demo/explorar/competicion/3941/", None, "Competición real con su clasificación: 1.ª División Provincial de Aficionados."),
        ],
        "movil": "01-inicio",
    },
    "entrenolab": {
        "titulo": "EntrenoLab",
        "shots": [
            ("01-inicio", BASE + "entrenolab-demo/", None, "Entrada a la demo real de EntrenoLab, sin registro ni pago."),
            ("02-plantilla", BASE + "entrenolab-demo/", "Probar con equipo de ejemplo", "Plantilla del club de ejemplo cargada desde la propia demo."),
            ("03-sesiones", BASE + "entrenolab-demo/", "Sesiones", "Sesiones de entrenamiento con sus bloques y su duración."),
        ],
        "movil": "02-plantilla",
    },
    "data-school": {
        "titulo": "Data School",
        "shots": [
            ("01-portada", BASE + "data-school-site/", None, "Portada del portal con el índice por fases y el progreso de estudio."),
            ("02-proyectos", BASE + "data-school-site/#/proyectos", None, "Catálogo de proyectos del portal con su estado y sus paquetes descargables."),
            ("03-aprender", BASE + "data-school-site/#/aprender", None, "Ruta de aprendizaje por fases, con horas y prerrequisitos."),
        ],
        "movil": "01-portada",
    },
    "opofuente": {
        "titulo": "OpoFuente",
        "shots": [
            ("01-portada", BASE + "opofuente-demo/", None, "Portada de la demo con las convocatorias y la cobertura del temario."),
            ("02-cobertura", BASE + "opofuente-demo/#/cobertura", None, "Mapa de cobertura de los 40 temas: completos y pendientes."),
            ("03-practicas", BASE + "opofuente-demo/", "Prácticas", "Lista de prácticas con su estado de avance."),
        ],
        "movil": "01-portada",
    },
    "cuedigital": {
        "titulo": "CUE Digital",
        "shots": [
            ("01-hoy", BASE + "cuedigital-demo/", None, "Pantalla de hoy del cuaderno de campo, con los datos ficticios de la demo."),
            ("02-tierras", BASE + "cuedigital-demo/", "Tierras", "Parcelas de la explotación con su cultivo y su superficie."),
            ("03-cuaderno", BASE + "cuedigital-demo/", "Cuaderno", "Cuaderno de la campaña con las últimas labores y su estado."),
        ],
        "movil": "02-tierras",
    },
    "panel": {
        "titulo": "Panel de proyectos",
        "shots": [
            ("01-panel", BASE + "panel/", None, "Panel de proyectos: qué está en pie, qué se puede abrir y cuándo caduca el estado."),
            ("02-casos", BASE + "panel/casos.html", None, "Casos y ritmo de los proyectos, con su última comprobación."),
        ],
        "movil": "01-panel",
    },
    "impresion3d": {
        "titulo": "Impresión 3D · escudos",
        "shots": [
            ("01-productos", BASE + "impresion3d-demo/", "element:section[aria-labelledby='productos']", "Las tres piezas con su precio: cuadro de 4 escudos, casco y medallón."),
            ("02-como", BASE + "impresion3d-demo/", "element:section[aria-labelledby='como']", "Cómo funciona: prueba antes de imprimir y solicitud sin pago."),
        ],
        "movil": "01-productos",
    },
    "compra-alimentacion": {
        "titulo": "Cesta",
        "shots": [
            ("01-compra", BASE + "cesta-demo/#/compra", None, "Búsqueda y comparación de la compra con precio por unidad."),
            ("02-listas", BASE + "cesta-demo/#/compra/listas", None, "Listas de la compra guardadas, con lo que queda por coger."),
            ("03-vacio", BASE + "cesta-demo/?demo=vacio#/compra/listas", None, "Estado vacío de la demo: no hay listas, pero el buscador sigue en pie."),
            ("04-carga", BASE + "cesta-demo/?demo=carga#/compra/listas", None, "Estado de carga de la demo mientras se traen las listas."),
            ("05-error", BASE + "cesta-demo/?demo=error#/compra/listas", None, "Estado de error de la demo, con opción de volver a intentarlo."),
        ],
        "movil": "01-compra",
    },
    "munipay": {
        "titulo": "MuniPay",
        "shots": [
            ("01-acceso", "https://multas-c2fed.web.app/", None, "Acceso a MuniPay desde el navegador."),
        ],
        "movil": "01-acceso",
    },
    "cdmplab": {
        "titulo": "CDMPLab",
        "shots": [
            ("01-acceso", BASE + "CDMPLab/auth/login", None, "Acceso a la pizarra táctica: la demo pide cuenta para entrar."),
            ("02-registro", BASE + "CDMPLab/auth/register", None, "Creación de cuenta en CDMPLab: solo correo y contraseña."),
        ],
        "movil": "01-acceso",
    },
}


def capturar(pagina, url, destino, ancho, alto, accion=None):
    pagina.set_viewport_size({"width": ancho, "height": alto})
    destino_url = url if url.startswith("http") else "https://erdeivih.github.io/" + url
    pagina.goto(destino_url, wait_until="networkidle", timeout=90000)
    pagina.wait_for_timeout(1200)
    if accion:
        if accion.startswith("scroll:"):
            objetivo = pagina.get_by_text(accion[7:], exact=False).first
            objetivo.scroll_into_view_if_needed(timeout=15000)
        elif accion.startswith("element:"):
            pagina.locator(accion[8:]).first.screenshot(path=str(destino))
            return pagina.title()
        else:
            pagina.get_by_text(accion, exact=False).first.click(timeout=15000)
        pagina.wait_for_timeout(1200)
    pagina.screenshot(path=str(destino), full_page=False)
    return pagina.title()


def main():
    slugs = sys.argv[1:] or list(DEMOS)
    META.parent.mkdir(parents=True, exist_ok=True)
    datos = json.loads(META.read_text(encoding="utf-8")) if META.exists() else {}
    hoy = date.today().isoformat()
    with sync_playwright() as p:
        navegador = p.chromium.launch(channel="msedge")
        pagina = navegador.new_page(device_scale_factor=1)
        for slug in slugs:
            cfg = DEMOS[slug]
            carpeta = OUT / slug
            carpeta.mkdir(parents=True, exist_ok=True)
            entradas, capturadas = [], {}
            for nombre, url, accion, pie in cfg["shots"]:
                destino = carpeta / f"{nombre}.png"
                try:
                    titulo = capturar(pagina, url, destino, 1280, 900, accion)
                    entradas.append({"archivo": f"/projects/{slug}/{nombre}.png", "url": url,
                                     "accion": accion, "viewport": "1280x900", "fecha": hoy, "pie": pie})
                    capturadas[nombre] = (url, accion, pie)
                    print(f"OK  {slug}/{nombre}.png  ({titulo})")
                except Exception as exc:
                    print(f"FALLO {slug}/{nombre}: {exc}")
            movil = cfg.get("movil")
            if movil and movil in capturadas:
                url, accion, pie = capturadas[movil]
                destino = carpeta / f"{movil}-390.png"
                try:
                    capturar(pagina, url, destino, 390, 844, accion)
                    entradas.append({"archivo": f"/projects/{slug}/{movil}-390.png", "url": url,
                                     "accion": accion, "viewport": "390x844", "fecha": hoy, "pie": pie})
                    print(f"OK  {slug}/{movil}-390.png")
                except Exception as exc:
                    print(f"FALLO {slug}/{movil}-390: {exc}")
            datos[slug] = {"titulo": cfg["titulo"], "fuente": "demo publicada", "capturas": entradas}
        navegador.close()
    META.write_text(json.dumps(datos, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("metadatos:", META)


if __name__ == "__main__":
    main()
