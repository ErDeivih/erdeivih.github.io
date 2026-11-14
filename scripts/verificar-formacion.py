# -*- coding: utf-8 -*-
"""Comprueba con HTTP real los enlaces de la formación publicada.

Lee las URLs de `src/data/formacion.ts`, hace una petición sin caché a cada una y falla si alguna
no responde 200. Así no se publica un enlace de curso que ya no exista.
"""
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATOS = ROOT / "src" / "data" / "formacion.ts"
CABECERAS = {"User-Agent": "verificador-formacion/1.0", "Cache-Control": "no-cache"}


def estado(url: str) -> int:
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=CABECERAS), timeout=40) as r:
            return r.status
    except urllib.error.HTTPError as exc:
        return exc.code
    except Exception:
        return 0


urls = sorted(set(re.findall(r'url: "(https://[^"]+)"', DATOS.read_text(encoding="utf-8"))))
if not urls:
    print("ROJO: no se encontró ningún enlace de formación")
    sys.exit(1)
fallos = 0
for url in urls:
    code = estado(url)
    print(f"{'OK ' if code == 200 else 'MAL'} {code}  {url}")
    fallos += 0 if code == 200 else 1
print(f"{len(urls)} enlaces de formación comprobados; caídos: {fallos}")
sys.exit(1 if fallos else 0)
