# -*- coding: utf-8 -*-
"""Mide el hero a 390×844: alto, dónde cae la prueba, filas de acciones y áreas táctiles."""
import json, sys
from pathlib import Path
from playwright.sync_api import sync_playwright

base = sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:8950"
salida = Path(sys.argv[2] if len(sys.argv) > 2 else "hero.json")
with sync_playwright() as p:
    nav = p.chromium.launch(channel="msedge", headless=True)
    ctx = nav.new_context(viewport={"width": 390, "height": 844}, device_scale_factor=2, is_mobile=True)
    page = ctx.new_page()
    page.goto(base + "/", wait_until="networkidle", timeout=60000)
    page.wait_for_timeout(700)
    datos = page.evaluate("""() => {
      const hero = document.querySelector('#inicio');
      const r = hero.getBoundingClientRect();
      const acciones = [...document.querySelectorAll('#inicio a')].map(a => { const b = a.getBoundingClientRect(); return {texto:a.textContent.trim(), w:Math.round(b.width), h:Math.round(b.height), top:Math.round(b.top)}; });
      const filas = new Set(acciones.map(a => a.top));
      const prueba = document.querySelector('#prueba');
      const pruebaTop = prueba ? Math.round(prueba.getBoundingClientRect().top) : null;
      return { altoHero: Math.round(r.height), acciones, filas: filas.size, pruebaTop, scrollW: document.documentElement.scrollWidth, innerW: window.innerWidth };
    }""")
    salida.write_text(json.dumps(datos, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(datos, ensure_ascii=False))
    page.screenshot(path=str(salida.with_suffix(".png")), full_page=False)
    nav.close()
