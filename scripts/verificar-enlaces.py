# -*- coding: utf-8 -*-
"""Comprueba con petición real (urllib, sin caché) cada `demo` y `repo` de las fichas.

Un enlace que no responda 200 no debe publicarse como demo. Salida: código HTTP por URL y
resumen; exit 1 si alguna demo falla. Escribe src/data/enlaces.json con la última comprobación.

Uso:  python scripts/verificar-enlaces.py
"""
import json
import re
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
CONTENIDO = ROOT / "src" / "content" / "projects"
SALIDA = ROOT / "src" / "data" / "enlaces.json"
FM = re.compile(r"^---\n(.*?)\n---\n", re.S)
CABECERAS = {"User-Agent": "verificador-porfolio/1.0", "Cache-Control": "no-cache", "Pragma": "no-cache"}


def estado(url: str) -> int:
    req = urllib.request.Request(url, headers=CABECERAS, method="GET")
    try:
        with urllib.request.urlopen(req, timeout=40) as r:
            return r.status
    except urllib.error.HTTPError as exc:
        return exc.code
    except Exception:
        return 0


def main():
    filas = []
    for path in sorted(CONTENIDO.glob("*/index.mdx")):
        m = FM.match(path.read_text(encoding="utf-8"))
        if not m:
            continue
        datos = yaml.safe_load(m.group(1)) or {}
        slug = path.parent.name
        for campo in ("demo", "repo"):
            url = datos.get(campo)
            if not url:
                continue
            code = estado(url)
            filas.append({"slug": slug, "campo": campo, "url": url, "code": code,
                          "comprobado": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")})
            marca = "OK " if code == 200 else "MAL"
            print(f"{marca} {code}  {campo:4} {slug:22} {url}")
    SALIDA.write_text(json.dumps(filas, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    malas = [f for f in filas if f["campo"] == "demo" and f["code"] != 200]
    print(f"{len(filas)} enlaces comprobados; demos caídas: {len(malas)}")
    sys.exit(1 if malas else 0)


if __name__ == "__main__":
    main()
