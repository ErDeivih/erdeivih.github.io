#!/usr/bin/env bash
# Comprueba en la web publicada que cada ficha explica qué hizo David y qué no.
set -euo pipefail
BASE="https://erdeivih.github.io/proyectos"
FICHAS="facylf compra-alimentacion data-school opofuente cue-digital entrenolab garmin munipay documentchain"
fallos=0
for slug in $FICHAS; do
  cuerpo="$(curl -s --max-time 30 "$BASE/$slug/")"
  he=0; no=0
  grep -qF "Qué he hecho yo" <<<"$cuerpo" && he=1
  grep -qF "Qué no he hecho" <<<"$cuerpo" && no=1
  if [ "$he" = "1" ] && [ "$no" = "1" ]; then
    echo "OK   $slug"
  else
    echo "MAL  $slug (hecho=$he, no=$no)"
    fallos=$((fallos + 1))
  fi
done
if [ "$fallos" -ne 0 ]; then echo "ROJO: $fallos fichas sin explicación"; exit 1; fi
echo "VERDE: las 9 fichas publicadas explican qué he hecho yo y qué no"
