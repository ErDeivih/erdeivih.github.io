# -*- coding: utf-8 -*-
"""Mide el sitio construido (dist/) a 390x844 y 1280x900 con Playwright.

Comprueba: viewport real, scroll horizontal, jerarquía (h1/h2), imágenes rotas, textos alternativos,
objetivos táctiles y que la animación de entrada no deja contenido invisible. Guarda capturas de
viewport 390 en capturas/ y el resultado en medicion-portfolio.json.

Uso:  python -m http.server 8788 --directory dist &  python scripts/medir.py
"""
import json
from pathlib import Path

from playwright.sync_api import sync_playwright

import os
BASE = os.environ.get("MEDIR_BASE", "http://127.0.0.1:8910")
ROOT = Path(__file__).resolve().parent.parent
CAPTURAS = ROOT.parent / "capturas"
PAGINAS = ["/", "/proyectos/", "/proyectos/facylf/", "/proyectos/documentchain/", "/analisis/", "/en/"]
VIEWPORTS = [(390, 844, "390"), (1280, 900, "escritorio")]


def medir(pagina, ruta, ancho, alto):
    pagina.set_viewport_size({"width": ancho, "height": alto})
    errores = []
    pagina.on("console", lambda m: errores.append(m.text) if m.type == "error" else None)
    pagina.goto(BASE + ruta, wait_until="networkidle", timeout=60000)
    pagina.wait_for_timeout(800)
    return {
        "ruta": ruta,
        "viewport": f"{ancho}x{alto}",
        "innerWidth": pagina.evaluate("innerWidth"),
        "innerHeight": pagina.evaluate("innerHeight"),
        "scrollWidth": pagina.evaluate("document.scrollingElement.scrollWidth"),
        "scrollHorizontal": pagina.evaluate("document.scrollingElement.scrollWidth > innerWidth"),
        "h1": pagina.evaluate("document.querySelector('h1')?.innerText?.replace(/\\s+/g,' ').trim().slice(0,90) || null"),
        "h2": pagina.evaluate("document.querySelector('h2')?.innerText?.replace(/\\s+/g,' ').trim().slice(0,90) || null"),
        "imagenes": pagina.evaluate("document.querySelectorAll('img').length"),
        "imagenesRotas": pagina.evaluate("[...document.querySelectorAll('img')].filter(i => i.complete && i.naturalWidth === 0).length"),
        "imagenesSinAlt": pagina.evaluate("[...document.querySelectorAll('img')].filter(i => !i.getAttribute('alt')).length"),
        "enlaces": pagina.evaluate("document.querySelectorAll('a').length"),
        "tapPequenos": pagina.evaluate("""[...document.querySelectorAll('a,button')].filter(e => {
            const r = e.getBoundingClientRect();
            if (!r.width || !r.height) return false;
            const inline = e.tagName === 'A' && getComputedStyle(e).display === 'inline';
            return !inline && (r.width < 44 || r.height < 44);
        }).length"""),
        "tapPequenosDetalle": pagina.evaluate("""[...document.querySelectorAll('a,button')].filter(e => {
            const r = e.getBoundingClientRect();
            if (!r.width || !r.height) return false;
            const inline = e.tagName === 'A' && getComputedStyle(e).display === 'inline';
            return !inline && (r.width < 44 || r.height < 44);
        }).slice(0, 10).map(e => ({ texto: (e.innerText || e.getAttribute('aria-label') || '').trim().slice(0, 30), w: Math.round(e.getBoundingClientRect().width), h: Math.round(e.getBoundingClientRect().height), clase: e.className?.toString?.().slice(0, 40) }))"""),
        "sinAltDetalle": pagina.evaluate("[...document.querySelectorAll('img')].filter(i => !i.getAttribute('alt')).map(i => i.getAttribute('src'))"),
        "primerRevealVisible": pagina.evaluate("""(() => {
            const el = document.querySelector('.reveal');
            if (!el) return null;
            const cs = getComputedStyle(el);
            return { opacity: Number(cs.opacity), transform: cs.transform };
        })()"""),
        "erroresConsola": errores[:5],
    }


def main():
    CAPTURAS.mkdir(parents=True, exist_ok=True)
    filas = []
    with sync_playwright() as p:
        navegador = p.chromium.launch(channel="msedge")
        for ruta in PAGINAS:
            for ancho, alto, etiqueta in VIEWPORTS:
                pagina = navegador.new_page(device_scale_factor=1)
                datos = medir(pagina, ruta, ancho, alto)
                filas.append(datos)
                if etiqueta == "390":
                    nombre = ruta.strip("/").replace("/", "-") or "inicio"
                    pagina.screenshot(path=str(CAPTURAS / f"ui-{nombre}-390.png"))
                print(f"{ruta:32} {etiqueta:10} innerW={datos['innerWidth']:>4} scrollW={datos['scrollWidth']:>4} "
                      f"scrollH={datos['scrollHorizontal']} imgs={datos['imagenes']} rotas={datos['imagenesRotas']} "
                      f"sinAlt={datos['imagenesSinAlt']} tapPequenos={datos['tapPequenos']} err={len(datos['erroresConsola'])}")
                pagina.close()
        navegador.close()
    (ROOT.parent / "medicion-portfolio.json").write_text(json.dumps(filas, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    malas = [f for f in filas if f["scrollHorizontal"] or f["imagenesRotas"] or f["erroresConsola"]]
    print("capturas en", CAPTURAS)
    if malas:
        print("FALLOS:", [(f["ruta"], f["viewport"]) for f in malas])
    else:
        print("OK: sin scroll horizontal, sin imagenes rotas y sin errores de consola")


if __name__ == "__main__":
    main()
