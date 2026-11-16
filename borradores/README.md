# Borradores de fichas de datos

Ficheros en `borradores/datos/` **no se publican**: no están en `src/content/datos`, así que Astro no
los recoge y no generan página ni entrada en `/datos/`.

- `clasificacion-simulada.mdx` — pendiente de contenido y URL de Data School.
- `undercuts.mdx` — pendiente de contenido y URL de Data School.

Para publicar una: rellenar las secciones, añadir `casoUrl`, `image` y captura a 390×844, mover el
fichero a `src/content/datos/<slug>/index.mdx` y pasar la puerta (`verificar-contenido.py`,
`verificar-datos.py`) antes de desplegar.
