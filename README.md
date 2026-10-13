# Portfolio de David Pérez Velasco

Portfolio público bilingüe construido con Astro y publicado en **https://erdeivih.github.io/**.
Incluye CDMPLab, FACyLF, compra y alimentación, CUE Digital, OpoFuente, MuniPay, DocumentChain
y FX Aeropuertos. Cada ficha distingue las funciones actuales de los próximos pasos.

## Desarrollo

```bash
pnpm install
pnpm dev
```

## Comprobación y build

```bash
pnpm build
```

El resultado estático se genera en `dist/` y se publica en GitHub Pages mediante
`.github/workflows/deploy.yml` cuando se actualiza `main`. Pages debe tener **GitHub Actions**
como origen de publicación. Requisitos: Node 24 y pnpm 11.

Para revisar la build antes de publicar: `pnpm preview`.

## Contenido

Cada proyecto vive en `src/content/projects/<slug>/`. Los archivos sin sufijo son la versión española;
los archivos `.en.mdx` contienen la versión inglesa. `index.mdx` define la ficha principal y el resto
se convierten en secciones navegables del caso de estudio.

- `status: active`: proyecto en desarrollo; no implica una demo pública.
- `status: complete`: trabajo finalizado en el alcance indicado en su ficha.
- `status: planned`: en preparación; aparece con una ilustración atenuada.
- `demo`: añadir únicamente una dirección pública que se pueda visitar.
- `repo`: enlazar únicamente repositorios públicos.
- `order`: orden en la portada y en el archivo, en ambos idiomas.

Las ilustraciones son dibujos de los temas de cada proyecto, no capturas de aplicaciones ni resultados.
CDMPLab mantiene su captura real. No se utilizan fotografías de jugadores.

## Certificaciones

Se añaden en `src/data/certifications.ts` con `title`, `issuer`, `date` y `verification`.
La sección muestra las acreditaciones completadas o un estado vacío cuando no hay entradas.
No introducir credenciales previstas como si ya estuvieran obtenidas.

## Pendiente de publicación de las aplicaciones

El portfolio es estático. Publicarlo no despliega los servidores, recolectores o bases de datos
de los proyectos. Las fichas sin demo seguirán sin enlace de acceso hasta que exista una versión pública.
La apertura de CDMPLab requiere revisar los flujos de cuenta y permisos en su propio repositorio;
las fichas de FACyLF, compra, CUE Digital y OpoFuente recogen su alcance actual y sus siguientes pasos.
