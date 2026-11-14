#!/usr/bin/env bash
# Comprueba con curl lo que hay publicado de verdad, no el build local.
set -euo pipefail
BASE="https://erdeivih.github.io"
fallos=0
comprobar() { # ruta, texto
  local cuerpo
  cuerpo="$(curl -s --max-time 30 "$BASE$1")"
  if grep -qF "$2" <<<"$cuerpo"; then
    echo "OK   $1  contiene «$2»"
  else
    echo "MAL  $1  falta «$2»"
    fallos=$((fallos + 1))
  fi
}

comprobar "/" "Cisco"
comprobar "/" "Kaggle"
comprobar "/" "En desarrollo"
comprobar "/" "DocumentChain"
comprobar "/" "cesta"
comprobar "/proyectos/" "Sistemas y aplicaciones que he construido, del dato a la interfaz"
comprobar "/proyectos/" "Activos"
comprobar "/proyectos/" "Ver proyecto"
comprobar "/proyectos/" "390-"

if [ "$fallos" -ne 0 ]; then
  echo "ROJO: $fallos comprobaciones fallidas"
  exit 1
fi
echo "VERDE: lo publicado contiene la formación y los cuatro arreglos de proyectos"
