# -*- coding: utf-8 -*-
"""Mide /proyectos/ a 390×844: dónde cae la primera ficha, su imagen y su acción."""
import json, sys
from pathlib import Path
from playwright.sync_api import sync_playwright

base = sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:8962"
salida = Path(sys.argv[2] if len(sys.argv) > 2 else "proyectos.json")
with sync_playwright() as p:
    nav = p.chromium.launch(channel="msedge", headless=True)
    ctx = nav.new_context(viewport={"width": 390, "height": 844}, device_scale_factor=2, is_mobile=True)
    page = ctx.new_page()
    page.goto(base + "/proyectos/", wait_until="networkidle", timeout=60000)
    page.wait_for_timeout(600)
    datos = page.evaluate("""() => {
      const card = document.querySelector('[data-project-status]');
      const r = card.getBoundingClientRect();
      const h2 = card.querySelector('h2').getBoundingClientRect();
      const img = card.querySelector('img');
      const btn = [...card.querySelectorAll('a')].find(a => /Ver proyecto|View project/.test(a.textContent));
      const b = btn ? btn.getBoundingClientRect() : null;
      return { primeraFichaTop: Math.round(r.top), tituloTop: Math.round(h2.top), imagenAlto: img ? Math.round(img.getBoundingClientRect().height) : null,
               accion: b ? {w: Math.round(b.width), h: Math.round(b.height), top: Math.round(b.top)} : null,
               scrollW: document.documentElement.scrollWidth, innerW: window.innerWidth };
    }""")
    salida.write_text(json.dumps(datos, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(datos, ensure_ascii=False))
    page.screenshot(path=str(salida.with_suffix(".png")), full_page=False)
    nav.close()
