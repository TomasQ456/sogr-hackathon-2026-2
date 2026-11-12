#!/usr/bin/env bash
# Uso:
#   ./probar.sh <prueba>/<ejercicio>           -> corre ejemplo.txt y compara con esperado.txt
#   ./probar.sh <prueba>/<ejercicio> oficial   -> corre entrada.txt y guarda salida.txt
set -u
dir="${1:?Uso: ./probar.sh <prueba>/<ejercicio> [oficial]}"
dir="${dir%/}"
modo="${2:-ejemplo}"

if [ "$modo" = "oficial" ]; then
  echo "$dir · entrada oficial"
  python3 "$dir/solucion.py" < "$dir/entrada.txt" > "$dir/salida.txt" || { echo "Error al ejecutar"; exit 1; }
  cat "$dir/salida.txt"
  echo "Salida guardada en $dir/salida.txt"
else
  echo "$dir · ejemplo"
  salida="$(python3 "$dir/solucion.py" < "$dir/ejemplo.txt")" || { echo "Error al ejecutar"; exit 1; }
  echo "$salida"
  if diff <(echo "$salida") "$dir/esperado.txt" > /dev/null; then
    echo "Coincide con esperado.txt"
  else
    echo "No coincide con esperado.txt"
    diff <(echo "$salida") "$dir/esperado.txt"
    exit 1
  fi
fi
