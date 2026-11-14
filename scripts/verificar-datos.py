# -*- coding: utf-8 -*-
"""Comprueba con HTTP real las URLs de las fichas de datos, cuando existan."""
import re, sys, urllib.error, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CAB = {"User-Agent": "verificador-datos/1.0", "Cache-Control": "no-cache"}
urls = []
for ficha in sorted((ROOT / "src" / "content" / "datos").glob("*/index.mdx")):
    texto = ficha.read_text(encoding="utf-8", errors="replace")
    for clave in ("datasetUrl", "repoUrl"):
        m = re.search(rf'^{clave}:\s*"([^"]+)"', texto, re.M)
        if m:
            urls.append((ficha.parent.name, clave, m.group(1)))

if not urls:
    print("OK  sin URLs todavía: los tres huecos están preparados y no se publica ningún enlace")
    sys.exit(0)

fallos = 0
for slug, clave, url in urls:
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=CAB), timeout=40) as r:
            code = r.status
    except urllib.error.HTTPError as exc:
        code = exc.code
    except Exception:
        code = 0
    print(f"{'OK ' if code == 200 else 'MAL'} {code:3} {slug} {clave} {url}")
    fallos += 0 if code == 200 else 1
print(f"{len(urls)} URLs de datos comprobadas; caídas: {fallos}")
sys.exit(1 if fallos else 0)
