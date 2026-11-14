# Portfolio de David Pérez Velasco

Porfolio personal de **David Pérez Velasco**, Ingeniero Informático (Grado en Ingeniería Informática,
USAL, 2025) y estudiante del Máster en Ingeniería Informática en la USAL. Construido con Astro y
salida 100 % estática; publicado en **https://erdeivih.github.io/**.

El sitio enseña software y sistemas que ha construido, con capturas reales, enlace a la demo solo si
responde 200 y el estado honesto de cada proyecto. Tiene una sección aparte de **datos y análisis**
con tres análisis hechos con NumPy.

## Estructura

- `/` portada; `/proyectos/` archivo; `/proyectos/<slug>/` ficha de cada proyecto.
- `/analisis/` datos y análisis (español); `/en/...` todas las versiones inglesas.
- `/David-Perez-Velasco-CV.pdf`: el CV, copiado desde el Escritorio con `scripts/copiar-cv.py`.

## Contenido

- Proyectos en `src/content/projects/<slug>/` (`index.mdx` + `index.en.mdx`), con `status`, `demo`,
  `repo`, `captures` (2–3 con `src`, `alt` y pie), `order` y `featured`.
- Análisis en `src/data/analisis.ts`; los gráficos viven en `public/analisis/` y se generan con
  `scripts/analisis-datos.py`.
- La puerta `scripts/verificar-enlaces.py` comprueba con HTTP real cada demo y repo; un enlace que no
  responda 200 no se publica.

## Desarrollo y build

```bash
pnpm install        # usa node-linker=hoisted (.npmrc); en F: fallaba el layout de enlaces de pnpm
pnpm dev
pnpm build          # astro check + astro build → dist/
```

## Comprobaciones

```bash
python scripts/verificar-enlaces.py   # HTTP real de demos y repos
python scripts/verificar-fichas.py    # imagen, capturas con alt y pie, enlaces 200
python scripts/medir.py               # 390×844 y 1280×900 (sirviendo dist/)
python scripts/capturar-demos.py      # capturas de las demos publicadas
python scripts/analisis-datos.py      # regenera los gráficos de /analisis/
python scripts/copiar-cv.py           # CV desde el Escritorio
```

## Despliegue

Se publica el contenido de `dist/` en la rama `gh-pages` del repositorio
`ErDeivih/erdeivih.github.io`. Estado y URLs verificadas en `../PORTFOLIO.md`.
