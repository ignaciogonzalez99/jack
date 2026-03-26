#!/usr/bin/env bash
set -euo pipefail

echo "Comando listo: curl https://ascii.live/rick"
read -r -p "Presiona Enter para ejecutar..."

curl https://ascii.live/rick
