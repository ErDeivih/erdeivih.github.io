# Portfolio de David Pérez Velasco

Portfolio público bilingüe construido con Astro (salida 100 % estática) y pensado como material de
candidatura: reúne proyectos de datos y BI (ETL, modelos de datos, KPIs y calidad del dato) con sus
demos reales, su estado honesto y capturas tomadas de la aplicación.

Publicado en **https://erdeivih.github.io/**. Estado, URLs verificadas y cómo refrescar capturas:
`../PORTFOLIO.md`.

## Estructura

- `/` portada en español; `/proyectos/` archivo; `/proyectos/<slug>/` ficha de cada proyecto.
- `/en/…` versión inglesa.
- `/cv.html` y `/David-Perez-Velasco-CV.pdf` (copiados de `../cv/`).

## Proyectos publicados (14)

Fondo Popular (FACYLF), Cesta, Data School, OpoFuente, EntrenoLab, CUE Digital, Lyfta (Garmin),
Chollos, Panel de proyectos, Impresión 3D · escudos, CDMPLab, MuniPay, DocumentChain (TFG) y
FX Aeropuertos. Ocho tienen demo pública y se enlazan **solo si responden 200** en el momento de
publicar (`scripts/verificar-enlaces.py`).

Cada ficha vive en `src/content/projects/<slug>/`:

- `index.mdx` (español) e `index.en.mdx` (inglés) con el frontmatter y el caso.
- `type: project` para la ficha principal; cualquier otro `.mdx` se convierte en pestaña.
- `status`: `active` (funcional/demostrable), `planned` (en preparación), `complete`.
- `demo` solo con una URL pública que responda 200; `repo` solo si el repositorio es público.
- `captures`: 2–3 capturas reales con `src`, `alt` y pie de foto.
- `order` y `featured`: orden del archivo y presencia entre los destacados de la portada.

## Capturas

Las capturas viven en `public/projects/<slug>/` y su origen, fecha y pie se guardan en
`src/data/capturas.json`. Se generan con:

```bash
python scripts/capturar-demos.py     # Playwright contra las demos publicadas
```

Las apps que aún no tienen demo (Cesta y Lyfta en local, TFG DocumentChain) se capturan o copian de
sus carpetas `capturas/` y se documentan igual. No se inventa ninguna imagen.

## Desarrollo y build

```bash
pnpm install        # usa node-linker=hoisted (ver .npmrc: en F: fallaba el layout de enlaces)
pnpm dev
pnpm build          # astro check + astro build → dist/
```

## Comprobaciones

```bash
python scripts/verificar-enlaces.py   # HTTP real de demos y repos (falla si una demo no es 200)
python scripts/medir.py               # 390×844 y 1280×900 (requiere servir dist/)
python scripts/copiar-cv.py           # /cv.html y el PDF desde ../cv/
```

## Despliegue

Se publica el contenido de `dist/` en la rama `gh-pages` del repositorio
`ErDeivih/erdeivih.github.io`. El workflow de GitHub Actions del repositorio no se modifica.
