# -*- coding: utf-8 -*-
"""Puerta de fichas: cada proyecto publicado debe poder enseñarse.

Comprueba, para cada ficha española de `src/content/projects/*/index.mdx`:
  1. tiene imagen principal y el fichero existe en `public/`;
  2. tiene 2 o 3 capturas (salvo las fichas `planned` sin interfaz, que pueden ir sin capturas);
  3. cada captura tiene `src` existente, `alt` y pie de foto;
  4. si declara `demo`, responde 200 en el momento de la comprobación (HTTP real);
  5. si declara `repo`, responde 200.

Salida: lista por proyecto y resumen; exit 1 si algo falla. Sin caché.
"""
import sys
import urllib.request
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
CONTENIDO = ROOT / "src" / "content" / "projects"
PUBLIC = ROOT / "public"
CABECERAS = {"User-Agent": "verificador-fichas/1.0", "Cache-Control": "no-cache"}
import re

FM = re.compile(r"^---\n(.*?)\n---\n", re.S)


def estado(url):
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=CABECERAS, method="GET"), timeout=40) as r:
            return r.status
    except urllib.error.HTTPError as exc:
        return exc.code
    except Exception:
        return 0


def main():
    fallos = []
    for path in sorted(CONTENIDO.glob("*/index.mdx")):
        m = FM.match(path.read_text(encoding="utf-8"))
        if not m:
            continue
        d = yaml.safe_load(m.group(1)) or {}
        slug = path.parent.name
        status = d.get("status", "active")
        imagen = d.get("image")
        caps = d.get("captures") or []
        if imagen and not (PUBLIC / imagen.lstrip("/")).is_file():
            fallos.append(f"{slug}: imagen principal no existe ({imagen})")
        if not imagen and status != "planned":
            fallos.append(f"{slug}: sin imagen principal")
        minimo = 0 if status == "planned" else 2
        if len(caps) < minimo:
            fallos.append(f"{slug}: {len(caps)} capturas (mínimo {minimo} para estado {status})")
        for i, c in enumerate(caps, 1):
            src = c.get("src", "")
            if not src or not (PUBLIC / src.lstrip("/")).is_file():
                fallos.append(f"{slug}: captura {i} sin fichero ({src})")
            if not c.get("alt"):
                fallos.append(f"{slug}: captura {i} sin texto alternativo")
            if not c.get("caption"):
                fallos.append(f"{slug}: captura {i} sin pie de foto")
        for campo in ("demo", "repo"):
            url = d.get(campo)
            if not url:
                continue
            code = estado(url)
            marca = "OK " if code == 200 else "MAL"
            print(f"  {marca} {code} {campo:4} {slug:20} {url}")
            if code != 200:
                fallos.append(f"{slug}: {campo} responde {code} ({url})")
        print(f"  ficha {slug:20} estado={status:9} capturas={len(caps)} imagen={'sí' if imagen else 'no'}")
    print()
    if fallos:
        print(f"ROJO: {len(fallos)} problema(s) en fichas")
        for f in fallos:
            print("  -", f)
        sys.exit(1)
    print("VERDE: todas las fichas tienen imagen, capturas con alt y pie, y enlaces en 200")


if __name__ == "__main__":
    main()
