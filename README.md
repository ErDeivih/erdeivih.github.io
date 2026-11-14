# Portfolio de David Pérez Velasco

Portfolio público bilingüe construido con Astro y pensado como material de candidatura: reúne
proyectos de datos y BI (ETL, modelos de datos, KPIs y calidad de dato) junto a proyectos de
producto y desarrollo. Publicado en **https://erdeivih.github.io/**.

## Proyectos

Los cuatro primeros son los de datos y BI y son los que se muestran primero:

1. **Fondo Popular** — base de datos y web del fútbol federado de Castilla y León.
2. **Cesta** — comparación de la compra semanal entre seis supermercados.
3. **Data School** — portal de datos e IA con catálogo verificado.
4. **Chollos** — buscador de segunda mano con precio de referencia por mediana.
5. **OpoFuente** — temario y práctica de oposición con cobertura calculada.
6. **EntrenoLab** — gestión de un club de fútbol base.
7. **CDMPLab** — pizarra táctica del club.
8. **CUE Digital** — cuaderno de campo agrícola.
9. **MuniPay** — cuentas de un equipo deportivo.
10. **DocumentChain** — TFG sobre documentos cifrados y permisos.
11. **FX Aeropuertos** — proyecto de datos en preparación.
12. **Lyfta** — entrenamiento de fuerza con reloj Garmin.

Cada ficha tiene versión en español e inglés y distingue lo que está hecho de lo que está pendiente.

## Desarrollo

```bash
pnpm install
pnpm dev
```

## Comprobación y build

```bash
pnpm build
```

El script ejecuta `astro check` y `astro build`. El resultado estático se genera en `dist/`.

## Contenido

Cada proyecto vive en `src/content/projects/<slug>/`. Los archivos sin sufijo son la versión
española; los `.en.mdx` contienen la versión inglesa. `index.mdx` define la ficha principal y el
resto se convierten en secciones navegables del caso de estudio.

- `status: active`: proyecto en desarrollo o en uso; no implica una demo pública.
- `status: complete`: trabajo finalizado en el alcance indicado en su ficha.
- `status: planned`: en preparación; aparece con una ilustración atenuada.
- `demo`: añadir únicamente una dirección pública que se pueda visitar.
- `repo`: enlazar únicamente repositorios públicos.
- `order`: orden en la portada y en el archivo, en ambos idiomas.
- `featured`: marca de proyecto destacado; no altera el orden, que lo fija `order`.

Un valor que falta no se rellena: si un dato no está confirmado, se deja fuera del frontmatter o se
señala como pendiente en el texto.

## Capturas

Las capturas de `public/projects/` son capturas reales de las aplicaciones. Fondo Popular, Cesta,
Data School, Chollos, OpoFuente, Lyfta, CUE Digital y CDMPLab tienen la suya; EntrenoLab todavía no
tiene una captura propia y usa la ilustración por defecto.

## Despliegue

El sitio es 100 % estático. Esta entrega se publica de forma manual a partir de `dist/`; el workflow
`.github/workflows/deploy.yml` que ya existía en el repositorio no se ha modificado.

## Certificaciones

Se añaden en `src/data/certifications.ts` con `title`, `issuer`, `date` y `verification`.
La sección muestra las acreditaciones completadas o un estado vacío cuando no hay entradas.
No introducir credenciales previstas como si ya estuvieran obtenidas.

## Pendiente de publicación de las aplicaciones

El portfolio es estático. Publicarlo no despliega los servidores, recolectores o bases de datos de
los proyectos. Las fichas sin demo siguen sin enlace de acceso hasta que exista una versión pública,
y la ficha de Fondo Popular describe la demo estática y la app completa por separado.
