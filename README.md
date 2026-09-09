# Portfolio de David Pérez Velasco

Portfolio bilingüe construido con Astro. Presenta cuatro proyectos como casos de estudio: el problema,
las decisiones de arquitectura, el estado real y una forma de probar cada uno.

## Desarrollo

```bash
pnpm install
pnpm dev
```

## Comprobación y build

```bash
pnpm build
```

El resultado estático se genera en `dist/` y se publica en GitHub Pages mediante el workflow incluido
en `.github/workflows/`.

## Contenido

Cada proyecto vive en `src/content/projects/<slug>/`. Los archivos sin sufijo son la versión española;
los archivos `.en.mdx` contienen la versión inglesa. `index.mdx` define la ficha principal y el resto
se convierten en secciones navegables del caso de estudio.
