# -*- coding: utf-8 -*-
"""Capturas móviles 390×844 de las demos publicadas, con nombre descriptivo.

Guarda en public/projects/<slug>/390-<nombre>.png y actualiza nada más: las fichas se editan aparte.
Uso: python scripts/capturar-moviles.py
"""
from pathlib import Path
from playwright.sync_api import sync_playwright

BASE = "https://erdeivih.github.io/"
OUT = Path(__file__).resolve().parent.parent / "public" / "projects"

# (slug, nombre, url, acción) — acción: None, ("texto", "texto del botón") o ("js", selector)
SHOTS = [
    ("facylf", "inicio", BASE + "fondo-popular-demo/", None),
    ("facylf", "competiciones", BASE + "fondo-popular-demo/#/explorar/competiciones", None),
    ("facylf", "clasificacion", BASE + "fondo-popular-demo/#/explorar/competicion/3941", None),
    ("compra-alimentacion", "compra", BASE + "cesta-demo/#/compra", None),
    ("compra-alimentacion", "listas", BASE + "cesta-demo/#/compra/listas", None),
    ("compra-alimentacion", "vacio", BASE + "cesta-demo/?demo=vacio#/compra/listas", None),
    ("data-school", "portada", BASE + "data-school-site/", None),
    ("data-school", "proyectos", BASE + "data-school-site/#/proyectos", None),
    ("data-school", "aprender", BASE + "data-school-site/#/aprender", None),
    ("opofuente", "portada", BASE + "opofuente-demo/", None),
    ("opofuente", "cobertura", BASE + "opofuente-demo/#/cobertura", None),
    ("opofuente", "practicas", BASE + "opofuente-demo/", ("texto", "Prácticas")),
    ("cue-digital", "hoy", BASE + "cuedigital-demo/", None),
    ("cue-digital", "tierras", BASE + "cuedigital-demo/", ("js", '[data-destino="tierras"]')),
    ("cue-digital", "cuaderno", BASE + "cuedigital-demo/", ("js", '[data-destino="cuaderno"]')),
    ("entrenolab", "inicio", BASE + "entrenolab-demo/", None),
    ("entrenolab", "plantilla", BASE + "entrenolab-demo/", ("texto", "Probar con equipo de ejemplo")),
    ("entrenolab", "sesiones", BASE + "entrenolab-demo/", ("texto", "Sesiones")),
    ("munipay", "acceso", "https://multas-c2fed.web.app/", None),
    ("munipay", "acceso-abajo", "https://multas-c2fed.web.app/", ("scroll", 600)),
]

with sync_playwright() as p:
    nav = p.chromium.launch(channel="msedge", headless=True)
    ctx = nav.new_context(viewport={"width": 390, "height": 844}, device_scale_factor=2, is_mobile=True, has_touch=True)
    page = ctx.new_page()
    for slug, nombre, url, accion in SHOTS:
        page.goto(url, wait_until="networkidle", timeout=90000)
        page.wait_for_timeout(900)
        if accion:
            tipo, valor = accion
            if tipo == "texto":
                try:
                    page.get_by_text(valor, exact=False).first.click(timeout=8000)
                except Exception:
                    page.evaluate("t => { const el = [...document.querySelectorAll('a,button,span')].find(e => e.textContent.trim() === t); if (!el) throw new Error('no está ' + t); el.click(); }", valor)
                page.wait_for_timeout(1200)
            elif tipo == "js":
                page.evaluate("sel => { const el = document.querySelector(sel); if (!el) throw new Error('no está ' + sel); el.click(); }", valor)
                page.wait_for_timeout(1200)
            elif tipo == "scroll":
                page.mouse.wheel(0, int(valor))
                page.wait_for_timeout(800)
        destino = OUT / slug / f"390-{nombre}.png"
        destino.parent.mkdir(parents=True, exist_ok=True)
        page.screenshot(path=str(destino), full_page=False)
        print("OK", slug, destino.name)
    nav.close()
